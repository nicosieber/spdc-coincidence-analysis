/**
 * comparison_eq51_plot.js — UI controller for the eq. (51) dashboard.
 * Shows the 2x2 matrix 1 - lam^2 MDMD of the main derivation next to the
 * 4x4 lossy covariance matrix sigma_Q' of the Gaussian formalism, and the
 * two sides of det(1 - lam^2 MDMD) = (1 - lam^2)^2 det sigma_Q'.
 * Physics from the shared window.SPDC module (spdc_physics.js).
 */
const TEXT = "#404040";
const MUTED = "#6a6a6a";
const FONT = "Lato, proxima-nova, Helvetica Neue, Arial, sans-serif";

// Diverging scale: negative entries blue, zero neutral gray, positive orange.
const DIVERGING = [[0, "#2980b9"], [0.5, "#f1f0ec"], [1, "#e67e22"]];

const MAIN_LABELS = ["H", "V"];
const GAUSS_LABELS = ["α<sub>H</sub>", "α<sub>V</sub>", "α<sub>H</sub>*", "α<sub>V</sub>*"];

// ---- spinbox controls (same behaviour as the other dashboards) ----
const LIMITS = {
    lam: [0.01, 0.99],
    etaH: [0, 1],
    etaV: [0, 1],
    theta: [0, Math.PI / 4],
};

let stepInterval = null;

function readNumber(id) {
    return parseFloat(document.getElementById(id).value.replace(",", "."));
}

function clamp(value, minValue, maxValue) {
    return Math.min(Math.max(value, minValue), maxValue);
}

function readParameter(id) {
    const value = readNumber(id);
    return isNaN(value) ? NaN : clamp(value, ...LIMITS[id]);
}

function stepValue(id, delta) {
    let value = readNumber(id);
    if (isNaN(value)) value = 0;

    value = clamp(value + delta, ...LIMITS[id]);
    document.getElementById(id).value = value.toFixed(id === "theta" ? 3 : 2);
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

// Entry font size: scale with the cell width so the numbers fit on narrow
// screens, capped at the desktop size.
function entryFontSize(plotId, n) {
    const width = document.getElementById(plotId).clientWidth;
    return Math.max(8, Math.min(14, width / (n * 6)));
}

function heatmapTrace(matrix, labels, fontSize) {
    const zmax = Math.max(...matrix.flat().map(Math.abs));
    return {
        type: "heatmap",
        z: matrix,
        x: labels,
        y: labels,
        zmin: -zmax,
        zmax: zmax,
        colorscale: DIVERGING,
        showscale: false,
        xgap: 2,
        ygap: 2,
        text: matrix.map(row => row.map(z => (z >= 0 ? "+" : "−") + Math.abs(z).toFixed(3))),
        texttemplate: "%{text}",
        textfont: { color: TEXT, size: fontSize },
        hovertemplate: "row %{y}, column %{x}<br>%{z:.6f}<extra></extra>",
    };
}

function heatmapLayout(title) {
    return {
        title: { text: title, font: { color: TEXT, size: 15 }, x: 0.5 },
        margin: { l: 48, r: 8, t: 40, b: 36 },
        font: { color: TEXT, family: FONT },
        paper_bgcolor: "#ffffff",
        plot_bgcolor: "#ffffff",
        xaxis: { side: "bottom", tickfont: { color: MUTED, size: 14 }, fixedrange: true },
        yaxis: { autorange: "reversed", tickfont: { color: MUTED, size: 14 }, fixedrange: true, scaleanchor: "x" },
    };
}

const CONFIG = { displaylogo: false, responsive: true, displayModeBar: false };

// Resize the embedding iframe to the card's height, so the page shows no
// empty space below the dashboard at any width. (The document's scrollHeight
// cannot be used: it never drops below the current iframe height.)
// window.frameElement is null when the dashboard is opened on its own.
function fitFrame() {
    const frame = window.frameElement;
    const card = document.querySelector(".plot-card");
    if (frame) frame.style.height = `${Math.ceil(card.getBoundingClientRect().height)}px`;
}

function updatePlot() {
    const lam = readParameter("lam");
    const etaH = readParameter("etaH");
    const etaV = readParameter("etaV");
    const theta = readParameter("theta");

    if (isNaN(lam) || isNaN(etaH) || isNaN(etaV) || isNaN(theta)) return;

    document.getElementById("readout").innerHTML =
        `λ=${lam.toFixed(4)}, η<sub>H</sub>=${etaH.toFixed(4)}, η<sub>V</sub>=${etaV.toFixed(4)}, ` +
        `ϑ=${(theta / (Math.PI / 8)).toFixed(3)}·π/8`;

    const mainMatrix = SPDC.mainMatrix(lam, etaH, etaV, theta);
    const sigmaQ = SPDC.sigmaQLossy(lam, etaH, etaV, theta);

    Plotly.react("main-matrix-plot", [heatmapTrace(mainMatrix, MAIN_LABELS, entryFontSize("main-matrix-plot", 2))],
        heatmapLayout("Main derivation: 𝟙 − λ²MDMD"), CONFIG);
    Plotly.react("sigma-q-plot", [heatmapTrace(sigmaQ, GAUSS_LABELS, entryFontSize("sigma-q-plot", 4))],
        heatmapLayout("Gaussian formalism: σ′<sub>Q</sub>"), CONFIG);

    const detMain = SPDC.det(mainMatrix);
    const detGauss = (1 - lam * lam) ** 2 * SPDC.det(sigmaQ);

    document.getElementById("det-main").textContent = detMain.toFixed(12);
    document.getElementById("det-gauss").textContent = detGauss.toFixed(12);
    document.getElementById("p00-main").textContent = ((1 - lam * lam) / Math.sqrt(detMain)).toFixed(12);
    document.getElementById("p00-gauss").textContent = (1 / Math.sqrt(SPDC.det(sigmaQ))).toFixed(12);
    document.getElementById("difference").textContent =
        `Difference of the two sides of (51): ${Math.abs(detMain - detGauss).toExponential(1)} (floating-point rounding only; the identity is exact).`;

    fitFrame();
}

window.addEventListener("resize", updatePlot);
updatePlot();
