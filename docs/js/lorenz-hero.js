/*
 * lorenz-hero.js
 * ==============================================================
 * Animated Lorenz-attractor background for the site hero,
 * in the spirit of the zensical.org landing page.
 *
 * Usage (Zensical)
 * --------------------------------------
 * 1. Put this file at:  docs/javascripts/lorenz-hero.js
 *
 * 2. Register it in zensical.toml under the [project] scope. If you
 *    already have an extra_javascript array, just add to it:
 *
 *        [project]
 *        extra_javascript = ["javascripts/lorenz-hero.js"]
 *
 *    (Paths are relative to docs_dir. This is a plain classic script,
 *    not an ES module, so Zensical loads it as a normal <script>.)
 *
 * 3. Give the hero a canvas. In the home page's template override
 *    (e.g. overrides/home.html) or in the index markdown, add:
 *
 *        <canvas id="lorenz-hero" aria-hidden="true"></canvas>
 *
 *    and style it so it sits behind the hero content (put this in a
 *    stylesheet registered via extra_css):
 *
 *        #lorenz-hero{
 *          position:absolute; inset:0; width:100%; height:100%;
 *          z-index:0; pointer-events:none;
 *        }
 *        .hero-inner{ position:relative; z-index:1; }
 *
 * Notes:
 * - Re-initializes on Zensical instant navigation via the document$
 *   observable (falls back to DOMContentLoaded if it isn't present).
 * - No-ops gracefully if the canvas is absent, so it's safe to load
 *   site-wide even though the canvas only exists on the home page.
 * - Honours prefers-reduced-motion by drawing a single static frame.
 * ==============================================================
 */
(function () {
  "use strict";

  var CANVAS_ID = "lorenz-hero";

  // Lorenz system parameters (classic butterfly values)
  var SIGMA = 10, RHO = 28, BETA = 8 / 3;

  // Integration + look
  var DT = 0.005;             // integration step
  var STEPS_PER_FRAME = 5;    // attractor advance per animation frame
  var TRAIL = 3200;           // points kept in the ribbon (higher = silkier)
  var LINE_WIDTH = 0.9;       // thin strands read as a ribbon, not wire

  // Placement / size. Two placements: an "intro" pose shown on page load
  // (large, centred) and a "background" pose the attractor settles into
  // as the user scrolls the hero away. Scroll progress blends between them.
  var INTRO_FILL = 1.05, INTRO_X = 0.5,  INTRO_Y = 0.5;
  var BG_FILL    = 0.62, BG_X    = 0.72, BG_Y    = 0.52;
  var TILT = 0.42;            // fixed x-axis tilt (radians) for a 3-D read
  var SPIN = 0.0012;          // rotation speed about the vertical axis

  function reducedMotion() {
    return window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  // Read the theme once per resize. Material/Zensical set
  // data-md-color-scheme="slate" (dark) or "default" (light) on <body>.
  function isDark() {
    var el = document.body;
    var scheme = el && el.getAttribute("data-md-color-scheme");
    if (scheme) return scheme === "slate";
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function start() {
    var canvas = document.getElementById(CANVAS_ID);
    if (!canvas) return;
    var ctx = canvas.getContext("2d");
    if (!ctx) return;

    var dpr = Math.max(1, window.devicePixelRatio || 1);
    var W = 0, H = 0, dark = isDark();

    // Attractor state and rolling trail of projected points.
    var x = 0.1, y = 0, z = 0;
    var pts = [];
    // Slow rotation of the 3-D attractor about the vertical axis so the
    // butterfly turns gently rather than sitting flat.
    var angle = 0;

    // scrollP: 0 = hero fully in view (intro pose), 1 = hero scrolled away
    // (background pose). Live-interpolated placement derived from it.
    var scrollP = 0;
    var FILL = INTRO_FILL, CENTER_X = INTRO_X, CENTER_Y = INTRO_Y;
    function applyScroll(p) {
      scrollP = p;
      FILL     = INTRO_FILL + (BG_FILL - INTRO_FILL) * p;
      CENTER_X = INTRO_X    + (BG_X    - INTRO_X)    * p;
      CENTER_Y = INTRO_Y    + (BG_Y    - INTRO_Y)    * p;
    }

    function resize() {
      var rect = canvas.getBoundingClientRect();
      W = Math.max(1, rect.width);
      H = Math.max(1, rect.height);
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      dark = isDark();
    }

    // Project a Lorenz (x,y,z) point to canvas space with a real 3-D
    // rotation. We spin about the vertical axis (angle) and apply a fixed
    // forward tilt (TILT), then use the rotated depth to fade far strands.
    // Returns [sx, sy, depth] with depth in ~[0,1] (0 = far, 1 = near).
    function project(px, py, pz) {
      var ox = px, oy = py, oz = pz - RHO;   // centre z around rho
      var ca = Math.cos(angle), sa = Math.sin(angle);
      var rx = ox * ca - oy * sa;            // yaw about vertical
      var rz = ox * sa + oy * ca;            // this becomes depth
      var ct = Math.cos(TILT), st = Math.sin(TILT);
      var ry = oz * ct - rz * st;            // pitch: tilt toward viewer
      var depth = oz * st + rz * ct;         // final depth axis

      var scale = Math.min(W, H) / 60 * FILL;
      var persp = 1 + depth * 0.010;         // mild perspective
      var cx = W * CENTER_X;
      var cy = H * CENTER_Y;
      var dNorm = (depth + 30) / 60;         // ~[0,1]
      if (dNorm < 0) dNorm = 0; else if (dNorm > 1) dNorm = 1;
      return [
        cx + rx * scale * persp,
        cy - ry * scale * persp,             // flip y-down
        dNorm
      ];
    }

    function step() {
      var dx = SIGMA * (y - x);
      var dy = x * (RHO - z) - y;
      var dz = x * y - BETA * z;
      x += dx * DT;
      y += dy * DT;
      z += dz * DT;
    }

    function pushPoint() {
      var p = project(x, y, z);
      pts.push(p[0], p[1], p[2]);            // flat [x,y,depth, ...]
      if (pts.length > TRAIL * 3) pts.splice(0, pts.length - TRAIL * 3);
    }

    // Base ink colour per mode; alpha is applied per segment.
    function ink() {
      return dark ? [186, 205, 240] : [38, 66, 116];
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var n = pts.length / 3;
      if (n < 2) return;
      ctx.lineCap = "round";
      ctx.lineJoin = "round";
      var col = ink();
      var head = dark ? [150, 225, 255] : [90, 120, 200]; // brighter leading tip
      // Per-segment stroke: opacity from age (older = fainter) times depth
      // (far = fainter). Draw far-to-near by relying on trail order; the
      // slight overdraw at crossings reads as the ribbon layering.
      for (var i = 1; i < n; i++) {
        var ax = pts[(i - 1) * 3], ay = pts[(i - 1) * 3 + 1], ad = pts[(i - 1) * 3 + 2];
        var bx = pts[i * 3], by = pts[i * 3 + 1], bd = pts[i * 3 + 2];
        var age = i / n;                     // 0 tail … 1 head
        var d = (ad + bd) * 0.5;             // 0 far … 1 near
        var base = dark ? 0.34 : 0.24;
        var a = base * (0.12 + 0.88 * age) * (0.30 + 0.70 * d);
        var c = age > 0.985 ? head : col;   // tiny bright tip
        ctx.strokeStyle = "rgba(" + c[0] + "," + c[1] + "," + c[2] + "," + a.toFixed(3) + ")";
        ctx.lineWidth = LINE_WIDTH * (0.6 + 0.8 * d);
        ctx.beginPath();
        ctx.moveTo(ax, ay);
        ctx.lineTo(bx, by);
        ctx.stroke();
      }
    }

    var running = true;
    function frame() {
      if (!running) return;
      for (var s = 0; s < STEPS_PER_FRAME; s++) {
        step();
        pushPoint();
      }
      angle += SPIN;               // gentle rotation about vertical
      draw();
      requestAnimationFrame(frame);
    }

    // Seed the trail so the first painted frame is already a full ribbon.
    function seed() {
      for (var i = 0; i < TRAIL; i++) { step(); pushPoint(); }
    }

    resize();
    seed();

    if (reducedMotion()) {
      draw();                      // one static frame, no animation loop
    } else {
      requestAnimationFrame(frame);
    }

    // ---- Scroll-driven cross-fade -----------------------------------
    // As the hero scrolls up, fade the attractor out and the text in, and
    // let the attractor drift from its intro pose to its background pose.
    // The hero element is the canvas's offsetParent (it is positioned).
    var hero = canvas.parentElement;
    function onScroll() {
      var rect = hero.getBoundingClientRect();
      // Progress 0 while the hero top is at/below the viewport top, rising
      // to 1 once the hero has scrolled up by ~70% of its own height.
      var travelled = -rect.top;
      var span = rect.height * 0.7;
      var p = span > 0 ? travelled / span : 0;
      if (p < 0) p = 0; else if (p > 1) p = 1;
      applyScroll(p);
      // Expose fades to CSS: attractor strong at top, text strong lower.
      hero.style.setProperty("--lorenz-canvas-opacity", (1 - 0.75 * p).toFixed(3));
      hero.style.setProperty("--lorenz-text-opacity", (0.25 + 0.75 * p).toFixed(3));
      if (reducedMotion()) draw();   // static mode: redraw on scroll
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();                       // set initial intro state

    // Pause when the tab is not visible to save battery.
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        running = false;
      } else if (!reducedMotion() && !running) {
        running = true;
        requestAnimationFrame(frame);
      }
    });

    var rt;
    window.addEventListener("resize", function () {
      clearTimeout(rt);
      rt = setTimeout(function () {
        dpr = Math.max(1, window.devicePixelRatio || 1);
        resize();
        draw();
      }, 150);
    });

    // React to Material's light/dark toggle without a reload.
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

  // Track the canvas we've already attached to, so re-running start()
  // under instant navigation doesn't spawn a second animation loop on
  // the same element.
  var activeCanvas = null;
  function boot() {
    var canvas = document.getElementById(CANVAS_ID);
    if (!canvas || canvas === activeCanvas) return;
    activeCanvas = canvas;
    start();
  }

  // Zensical / Material expose a `document$` RxJS observable that emits
  // on every (instant) navigation. Prefer it so the hero re-initializes
  // when the user navigates back to the home page without a full reload.
  if (typeof window.document$ !== "undefined" &&
      window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(boot);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();