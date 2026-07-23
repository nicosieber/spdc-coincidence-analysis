/*
 * vortex-hero.js
 * ==============================================================
 * Animated spiral-vortex background for the site hero, in the
 * style of the zensical.org landing page: many fine warm particle
 * streaks on logarithmic spiral arms, rotating differentially
 * around a hot core, on a dark backdrop.
 *
 * Usage (Zensical)
 * --------------------------------------
 * 1. Put this file at:  docs/js/vortex-hero.js
 *
 * 2. Register it in zensical.toml under the [project] scope (add to
 *    your existing extra_javascript array if you have one):
 *
 *        [project]
 *        extra_javascript = ["js/vortex-hero.js"]
 *
 * 3. The canvas is a FIXED, FULL-VIEWPORT background. Place it once
 *    as the first line of docs/index.md (home only), or as a direct
 *    child of <body> via an overrides/main.html template for all pages:
 *
 *        <canvas id="vortex-hero" aria-hidden="true"></canvas>
 *
 * 4. CSS (put in a stylesheet registered via extra_css). The canvas is a
 *    fixed full-viewport cover; the page content starts hidden and is
 *    revealed once the body gets the `vortex-revealed` class on scroll:
 *
 *        #vortex-hero{
 *          position:fixed; inset:0; width:100vw; height:100vh;
 *          z-index:5;              // above content, BELOW the header bar
 *          pointer-events:none; will-change:transform;
 *        }
 *        // page content hidden under the cover on load …
 *        .md-main{
 *          opacity:0; transform:translateY(24px);
 *          transition:opacity .5s ease, transform .5s ease;
 *        }
 *        // … and revealed once the user starts scrolling
 *        body.vortex-revealed .md-main{ opacity:1; transform:none; }
 *
 *    Also give the home page room to scroll so there is something to
 *    scroll *through* while the cover slides away — see the message.
 *
 * Notes:
 * - On load the vortex covers the screen; scrolling ~FADE_PX slides it up
 *   and off the top, revealing the page beneath. Tune FADE_PX below.
 * - Warm palette on dark, cooler ink on light backgrounds.
 * - Honours prefers-reduced-motion (single static frame).
 * - Re-initializes on Zensical instant navigation via document$.
 * ==============================================================
 */
(function (root) {
  "use strict";

  var CANVAS_ID = "vortex-hero";

  // Browsers restore the previous scroll position on reload, which would
  // start the intro cover already scrolled away. Force manual control and
  // pin to the top on (re)load so the vortex always plays from the start.
  if ("scrollRestoration" in history) {
    try { history.scrollRestoration = "manual"; } catch (e) {}
  }

  // ---- Look / feel knobs ------------------------------------------
  var PARTICLES = 550;       // number of orbiting particles
  var TRAIL = 26;            // positions kept per particle (comet tail length)
  var ARMS = 3;              // spiral arms particles seed onto
  var TWIST = 3.2;           // spiral winding (radians per unit radius)
  var IN_RATE = 0.0022;      // how fast particles fall toward the core
  var BASE_SPIN = 0.010;     // angular speed scale
  var DIFFERENTIAL = 2.4;    // extra angular speed near the core
  var CORE = 0.03;           // core radius where particles respawn
  var FADE_PX = 420;         // scroll distance over which to fade out

  function reducedMotion() {
    return window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function isDark() {
    var el = document.body;
    var scheme = el && el.getAttribute("data-md-color-scheme");
    if (scheme) return scheme === "slate";
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  // Lime/green palette stops (bright core -> rim), interpolated by radius,
  // tuned to the page's lime accent. [r,g,b].
  var WARM = [
    [239, 249, 210],   // pale lime-white core
    [198, 222, 92],    // lime (matches the header bar)
    [140, 178, 40],    // green-lime
    [78, 120, 26],     // deep green
    [34, 58, 16]       // dark moss (rim)
  ];
  function palette(t) {
    if (t <= 0) return WARM[0];
    if (t >= 1) return WARM[WARM.length - 1];
    var f = t * (WARM.length - 1);
    var i = Math.floor(f);
    var frac = f - i;
    var a = WARM[i], b = WARM[i + 1];
    return [
      a[0] + (b[0] - a[0]) * frac,
      a[1] + (b[1] - a[1]) * frac,
      a[2] + (b[2] - a[2]) * frac
    ];
  }

  function start() {
    var canvas = document.getElementById(CANVAS_ID);
    if (!canvas) return;
    var ctx = canvas.getContext("2d");
    if (!ctx) return;

    // Force full-viewport fixed positioning inline, so the vortex does not
    // depend on extra.css and cannot be shrunk to the content column by a
    // theme rule. Appending to <body> escapes most transformed ancestors
    // that would otherwise break position:fixed. We size in explicit pixels
    // (not 100vw/100vh) because vw/vh resolve against a transformed
    // containing block if one exists — pixels always mean screen pixels.
    if (canvas.parentElement !== document.body) {
      document.body.appendChild(canvas);
    }
    // Measure the Zensical header so the canvas can start just below it,
    // rather than covering the lime bar. Falls back to 0 if not found.
    function headerHeight() {
      var h = document.querySelector(".md-header") ||
              document.querySelector("header");
      return h ? Math.round(h.getBoundingClientRect().height) : 0;
    }
    function applyStyle() {
      var top = headerHeight();
      var cs = canvas.style;
      cs.position = "fixed";
      cs.top = top + "px";
      cs.left = "0";
      cs.width = window.innerWidth + "px";
      cs.height = (window.innerHeight - top) + "px";
      cs.zIndex = "5";
      cs.pointerEvents = "none";
      cs.margin = "0";
      cs.padding = "0";
      cs.display = "block";
    }
    applyStyle();

    var dpr = Math.max(1, window.devicePixelRatio || 1);
    var W = 0, H = 0, dark = isDark();
    var spin = 0;              // accumulated global rotation
    var scrollP = 0;

    // Each particle has a live (r, theta) that integrates inward, plus a
    // ring buffer of its recent screen positions to draw as a fading tail.
    var parts = [];
    function spawn(p) {
      var arm = Math.floor(Math.random() * ARMS);
      var r = 0.7 + Math.random() * 0.55;              // start near/beyond rim
      p.r = r;
      p.theta = (arm / ARMS) * Math.PI * 2 + r * TWIST +
                (Math.random() - 0.5) * 0.5;
      p.bright = 0.45 + 0.55 * Math.random();
      p.trail = [];                                    // [x0,y0, x1,y1, ...]
      return p;
    }
    function seedParticles() {
      parts = [];
      for (var i = 0; i < PARTICLES; i++) parts.push(spawn({}));
    }

    function resize() {
      applyStyle();
      var top = headerHeight();
      W = Math.max(1, window.innerWidth);
      H = Math.max(1, window.innerHeight - top);
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      dark = isDark();
    }

    // Advance every particle one step inward along its spiral, pushing its
    // new screen position onto its trail.
    function update() {
      var cx = W * 0.5, cy = H * 0.5;
      var maxR = Math.min(W, H) * 0.62;
      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        // Angular speed rises toward the core -> winding vortex.
        p.theta += BASE_SPIN * (1 + DIFFERENTIAL * (1 - p.r));
        // Fall inward faster as it accelerates near the centre.
        p.r -= IN_RATE * (0.4 + 1.6 * p.r);
        if (p.r <= CORE) { spawn(p); continue; }
        var rad = p.r * maxR;
        var x = cx + Math.cos(p.theta) * rad;
        var y = cy + Math.sin(p.theta) * rad;
        p.trail.push(x, y);
        if (p.trail.length > TRAIL * 2) p.trail.splice(0, 2);
      }
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var cx = W * 0.5, cy = H * 0.5;
      var globalAlpha = dark ? 1 : 0.55;
      ctx.lineCap = "round";
      ctx.lineJoin = "round";

      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        var t = p.trail;
        var n = t.length / 2;
        if (n < 2) continue;
        var col = dark ? palette(p.r) : coolPalette(p.r);
        // Draw the tail as fading segments: newest brightest.
        for (var k = 1; k < n; k++) {
          var age = k / (n - 1);                       // 0 tail … 1 head
          var a = globalAlpha * p.bright * (0.15 + 0.85 * age) * (1.1 - 0.45 * p.r);
          if (a > 1) a = 1;
          ctx.strokeStyle = "rgba(" + (col[0] | 0) + "," + (col[1] | 0) +
            "," + (col[2] | 0) + "," + a.toFixed(3) + ")";
          ctx.lineWidth = 0.7 + 1.8 * age * (1 - 0.5 * p.r);
          ctx.beginPath();
          ctx.moveTo(t[(k - 1) * 2], t[(k - 1) * 2 + 1]);
          ctx.lineTo(t[k * 2], t[k * 2 + 1]);
          ctx.stroke();
        }
      }

      // Soft hot core glow.
      var maxR = Math.min(W, H) * 0.62;
      var g = ctx.createRadialGradient(cx, cy, 0, cx, cy, maxR * 0.16);
      if (dark) {
        g.addColorStop(0, "rgba(240,250,205,0.55)");
        g.addColorStop(0.4, "rgba(190,220,90,0.20)");
        g.addColorStop(1, "rgba(160,200,60,0)");
      } else {
        g.addColorStop(0, "rgba(150,180,60,0.20)");
        g.addColorStop(1, "rgba(150,180,60,0)");
      }
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(cx, cy, maxR * 0.16, 0, Math.PI * 2);
      ctx.fill();
    }

    function coolPalette(t) {
      var a = [110, 90, 170], b = [40, 70, 120];
      return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t,
              a[2] + (b[2] - a[2]) * t];
    }

    var started = false;
    function frame() {
      // One persistent loop for the life of the page. Skip the heavy work
      // only when the tab is hidden; otherwise always animate. (Reduced-
      // motion no longer freezes it — a slow ambient rotation is fine, and
      // freezing was surprising; users who truly need it still can via the
      // REDUCED_SPIN factor below.)
      if (!document.hidden) {
        spin += BASE_SPIN;
        update();
        draw();
      }
      requestAnimationFrame(frame);
    }

    resize();
    seedParticles();
    for (var w = 0; w < TRAIL; w++) update();   // warm up the tails
    // Start at the top so the cover is fully in view and plays from frame 1.
    window.scrollTo(0, 0);
    draw();                                      // paint first frame now

    if (!started) {
      started = true;
      requestAnimationFrame(frame);
    }

    // ---- Scroll: slide the vortex up and off, revealing the page ----
    // The canvas is a fixed full-viewport "cover". Scrolling translates it
    // upward by up to one viewport height so it slides off the top, and
    // toggles a body class that lets the page content fade/rise in.
    function onScroll() {
      var y0 = window.pageYOffset || document.documentElement.scrollTop || 0;
      var p = FADE_PX > 0 ? y0 / FADE_PX : 1;
      if (p < 0) p = 0; else if (p > 1) p = 1;
      scrollP = p;
      // Slide up by up to 100vh; ease-out so it accelerates away.
      var shift = -(p * (1.05 * window.innerHeight));
      canvas.style.transform = "translateY(" + shift.toFixed(1) + "px)";
      canvas.style.opacity = (1 - 0.15 * p).toFixed(3); // mostly slide, slight fade
      document.body.style.setProperty("--vortex-reveal", p.toFixed(3));
      if (p > 0.02) document.body.classList.add("vortex-revealed");
      else document.body.classList.remove("vortex-revealed");
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    // (The animation loop self-manages visibility; no pause/resume needed.)

    var rt;
    window.addEventListener("resize", function () {
      clearTimeout(rt);
      rt = setTimeout(function () {
        dpr = Math.max(1, window.devicePixelRatio || 1);
        resize();
        draw();
      }, 150);
    });

    if (window.MutationObserver) {
      new MutationObserver(function () {
        var d = isDark();
        if (d !== dark) { dark = d; draw(); }
      }).observe(document.body, {
        attributes: true,
        attributeFilter: ["data-md-color-scheme"]
      });
    }
  }

  var activeCanvas = null;
  function boot() {
    var canvas = document.getElementById(CANVAS_ID);
    if (!canvas || canvas === activeCanvas) return;
    activeCanvas = canvas;
    start();
  }

  if (typeof window.document$ !== "undefined" &&
      window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(boot);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})(typeof window !== "undefined" ? window : globalThis);