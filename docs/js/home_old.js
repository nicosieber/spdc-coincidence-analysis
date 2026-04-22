document.addEventListener("DOMContentLoaded", () => {
  const tiles = document.querySelectorAll(".tile");

  tiles.forEach((tile, index) => {
    tile.style.opacity = "0";
    tile.style.transform = "translateY(12px)";

    setTimeout(() => {
      tile.style.transition =
        "opacity 300ms ease, transform 300ms ease, border-color 180ms ease, box-shadow 180ms ease, background 180ms ease";
      tile.style.opacity = "1";
      tile.style.transform = "translateY(0)";
    }, 80 * index);
  });

  tiles.forEach((tile) => {
    tile.addEventListener("mousemove", (e) => {
      const rect = tile.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      tile.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(64,81,181,0.12), rgba(64,81,181,0.03) 40%, transparent 70%)`;
    });

    tile.addEventListener("mouseleave", () => {
      tile.style.background = "rgba(255, 255, 255, 0.03)";
    });
  });
});