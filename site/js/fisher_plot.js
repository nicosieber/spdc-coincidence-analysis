/**
 * fisher_plot.js — UI controller for the Fisher-information dashboard.
 * All physics (Fisher F(phi) and the shot-noise limit) comes from the
 * shared window.SPDC module (spdc_physics.js).
 */
(function () {
  const N = 1000;

  // Build phi grid and both curves. phi = 4*theta, theta in [0, pi/4].
  function buildCurve(lam, etaH, etaV) {
    const phis = [], Fvals = [], SNLvals = [];
    for (let i = 0; i < N; i++) {
      const phi = 1e-4 + (Math.PI - 2e-4) * i / (N - 1);
      phis.push(phi);
      Fvals.push(SPDC.fisherPhi(lam, etaH, etaV, phi));
      SNLvals.push(SPDC.snlPhi(lam, etaH, etaV, phi));
    }
    const Fmax = Math.max(...Fvals);
    const SNLmax = Math.max(...SNLvals);
    return { phis, Fvals, SNLvals, Fmax, SNLmax };
  }

  let stepInterval = null;

  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  function step(id, delta) {
    const el = document.getElementById(id);
    const lo = 0.01;
    const hi = id === "lam" ? 0.99 : 1.00;
    const val = clamp(parseFloat(el.value) + delta, lo, hi);
    el.value = val.toFixed(2);
    updatePlot();
  }

  window.startStepping = function (id, delta) {
    step(id, delta);
    stepInterval = setInterval(() => step(id, delta), 120);
  };

  window.stopStepping = function () {
    clearInterval(stepInterval);
    stepInterval = null;
  };

  window.updatePlot = function () {
    const lam = clamp(parseFloat(document.getElementById("lam").value), 0.01, 0.99);
    const etaH = clamp(parseFloat(document.getElementById("etaH").value), 0.01, 1.00);
    const etaV = clamp(parseFloat(document.getElementById("etaV").value), 0.01, 1.00);

    if (isNaN(lam) || isNaN(etaH) || isNaN(etaV)) return;

    const { phis, Fvals, SNLvals, Fmax, SNLmax } = buildCurve(lam, etaH, etaV);

    // y-range covers whichever curve is higher, so the SNL stays visible
    const yTop = Math.max(Fmax, SNLmax) * 1.05;

    Plotly.update("fisher-plot",
      { x: [phis, phis], y: [Fvals, SNLvals] },
      { "yaxis.range": [0, yTop] }
    );

    document.getElementById("readout").innerHTML =
      `λ=${lam.toFixed(4)}, η<sub>H</sub>=${etaH.toFixed(4)}, ` +
      `η<sub>V</sub>=${etaV.toFixed(4)}, ` +
      `<i>F</i><sub>max</sub>=${Fmax.toFixed(4)}`;
  };
})();
