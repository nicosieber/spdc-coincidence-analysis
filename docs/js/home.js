document.addEventListener("DOMContentLoaded", () => {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const tiles = document.querySelectorAll(".tile:not(.tile--disabled)");

  if (!tiles.length) return;

  // -------------------------
  // 1. Lightweight stagger-in
  // -------------------------
  if (!prefersReducedMotion) {
    tiles.forEach((tile, index) => {
      tile.animate(
        [
          { opacity: 0, transform: "translateY(10px)" },
          { opacity: 1, transform: "translateY(0)" }
        ],
        {
          duration: 320,
          delay: index * 70,
          easing: "ease-out",
          fill: "both"
        }
      );
    });
  }

  // -------------------------
  // 2. Cursor-follow glow
  // Uses requestAnimationFrame
  // to avoid too many updates
  // -------------------------
  tiles.forEach((tile) => {
    let rafId = null;
    let pendingX = null;
    let pendingY = null;

    const updateGlow = () => {
      tile.style.setProperty("--tile-glow-x", `${pendingX}px`);
      tile.style.setProperty("--tile-glow-y", `${pendingY}px`);
      rafId = null;
    };

    const onMouseMove = (event) => {
      if (prefersReducedMotion) return;

      const rect = tile.getBoundingClientRect();
      pendingX = event.clientX - rect.left;
      pendingY = event.clientY - rect.top;

      if (rafId === null) {
        rafId = window.requestAnimationFrame(updateGlow);
      }
    };

    const onMouseLeave = () => {
      tile.style.setProperty("--tile-glow-x", "50%");
      tile.style.setProperty("--tile-glow-y", "50%");
    };

    tile.addEventListener("mousemove", onMouseMove, { passive: true });
    tile.addEventListener("mouseleave", onMouseLeave, { passive: true });
  });
});

