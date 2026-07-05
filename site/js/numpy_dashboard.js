/**
 * numpy_dashboard.js — UI controller for the NumPy-engine coincidence
 * dashboard. Draws the analytic closed-form curve (instant) and overlays a
 * live truncated-Fock simulation at fixed N=60 (open-circle markers) plus a
 * log-scale residual break-off panel. All physics comes from the shared
 * window.SPDC module (spdc_physics.js): closed form via SPDC.coincidence,
 * numeric via SPDC.fockCoincidence (browser twin of spdc.fock_numpy).
 *
 * The Fock state depends only on (lam, theta, N, nmax) — NOT on the
 * efficiencies — so SPDC.fockCoincidence builds it once per marker and takes
 * three weighted no-click sums. 15 markers at N=60 recompute in well under
 * one animation frame, so the overlay stays live on every drag tick.
 */
const N_FOCK = 60;
const NMAX_FOCK = 45;
const N_MARKERS = 15;
const RESID_FLOOR = 1e-16;

let stepInterval = null;

function readNumber(id) {
    return parseFloat(document.getElementById(id).value.replace(",", "."));
}

function clamp(value, minValue, maxValue) {
    return Math.min(Math.max(value, minValue), maxValue);
}

function writeNumber(id, value) {
    document.getElementById(id).value = value.toFixed(2);
}

function stepValue(id, delta) {
    let value = readNumber(id);
    if (isNaN(value)) value = 0;

    value += delta;

    if (id === "lam") {
        value = clamp(value, 0.01, 0.9999);
    } else {
        value = clamp(value, 0, 1);
    }

    writeNumber(id, value);
    updatePlot();
}

function startStepping(id, delta) {
    stopStepping();
    stepValue(id, delta);

    stepInterval = setInterval(() => {
        stepValue(id, delta);
    }, 90);
}

function stopStepping() {
    if (stepInterval !== null) {
        clearInterval(stepInterval);
        stepInterval = null;
    }
}

window.addEventListener("mouseup", stopStepping);
window.addEventListener("touchend", stopStepping);

function updatePlot() {
    const lam = readNumber("lam");
    const etaH = readNumber("etaH");
    const etaV = readNumber("etaV");

    if (isNaN(lam) || isNaN(etaH) || isNaN(etaV)) return;

    // --- closed-form curve (instant analytic) --------------------------
    const theta = SPDC.linspace(0, Math.PI / 4, 1000);
    const C = theta.map(t => SPDC.coincidence(lam, etaH, etaV, t));
    const Cmax = Math.max(...C);
    const Cmin = Math.min(...C);
    const Cnorm = C.map(v => v / Cmax);
    const visibility = (Cmax - Cmin) / (Cmax + Cmin);

    // --- Fock markers + residual (live, N=60) --------------------------
    const thetaM = SPDC.linspace(0, Math.PI / 4, N_MARKERS);
    const closedM = thetaM.map(t => SPDC.coincidence(lam, etaH, etaV, t) / Cmax);
    const fockM = thetaM.map(
        t => SPDC.fockCoincidence(lam, etaH, etaV, t, N_FOCK, NMAX_FOCK) / Cmax
    );

    let maxResid = 0;
    const resid = new Array(thetaM.length);
    for (let i = 0; i < thetaM.length; i++) {
        const d = Math.abs(fockM[i] - closedM[i]);
        if (d > maxResid) maxResid = d;
        resid[i] = Math.max(d, RESID_FLOOR);   // log panel never sees zero
    }

    document.getElementById("readout").innerHTML =
        `λ=${lam.toFixed(4)}, η<sub>H</sub>=${etaH.toFixed(4)}, η<sub>V</sub>=${etaV.toFixed(4)}, ` +
        `V=${visibility.toFixed(4)}, max|numeric−closed|=${maxResid.toExponential(2)}`;

    // trace 0: closed line, trace 1: Fock markers (both top),
    // trace 2: residual (bottom).
    Plotly.update("coincidence-plot", {
        x: [theta, thetaM, thetaM],
        y: [Cnorm, fockM, resid]
    });
}