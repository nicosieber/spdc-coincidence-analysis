/**
 * comparison_qfunction_plot.js — UI controller for the Q-function dashboard.
 * Left: the slice of the Husimi Q function of the lossy state at real
 * amplitudes (Re alpha_H, Re alpha_V), i.e. v = (x, y, x, y) in eq. (25):
 *   Q = exp(-1/2 v^T sigma_Q'^{-1} v) / (pi^2 sqrt(det sigma_Q')).
 * Right: the peak height pi^2 Q(0) = 1/sqrt(det sigma_Q') = P(0,0), eq. (26),
 * against the HWP angle theta.
 * Physics from the shared window.SPDC module (spdc_physics.js).
 */
const TEXT = "#404040";
const MUTED = "#6a6a6a";
const GRID = "#e1e4e5";
const BLUE = "#2980b9";
const ORANGE = "#e67e22";
const FONT = "Lato, proxima-nova, Helvetica Neue, Arial, sans-serif";

// Sequential scale: one hue, light (low Q) to dark (high Q).
const SEQUENTIAL = [[0, "#f4f8fd"], [0.35, "#86b6ef"], [0.7, "#1c5cab"], [1, "#0d366b"]];

const N_GRID = 121;
const N_THETA = 300;
const THETA_MAX = Math.PI / 4;

const CONFIG = { displaylogo: false, responsive: true, displayModeBar: false };

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

// Quadratic form of the real slice: v^T sigma^{-1} v with v = (x, y, x, y)
// equals (x, y) K (x, y)^T, where K sums the four 2x2 blocks of sigma^{-1}.
function sliceMatrix(sigmaInv) {
    const K = [[0, 0], [0, 0]];
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            K[i][j] = sigmaInv[i][j] + sigmaInv[i][j + 2]
                    + sigmaInv[i + 2][j] + sigmaInv[i + 2][j + 2];
        }
    }
    return K;
}

// Largest eigenvalue of the symmetric 2x2 matrix K^{-1}, i.e. the squared
// long half-axis of the 1/sqrt(e) contour of the slice.
function longAxisSquared(K) {
    const detK = K[0][0] * K[1][1] - K[0][1] * K[1][0];
    const tr = K[0][0] + K[1][1];
    const smallest = tr / 2 - Math.sqrt((tr * tr) / 4 - detK);
    return 1 / smallest;
}

// Plot range that stays fixed while theta moves, so the slice visibly
// rotates and deforms instead of being rescaled.
function sliceRange(lam, etaH, etaV) {
    let maxAxis = 0;
    for (const th of SPDC.linspace(0, THETA_MAX, 46)) {
        const K = sliceMatrix(SPDC.inv(SPDC.sigmaQLossy(lam, etaH, etaV, th)));
        maxAxis = Math.max(maxAxis, longAxisSquared(K));
    }
    return 3 * Math.sqrt(maxAxis);
}

// y-range of the peak-height plot. For eta_H = eta_V the curve is exactly
// flat (det sigma_Q' does not depend on theta), and autoscaling would zoom
// into floating-point noise of order 1e-16; show a flat line instead.
function peakAxisRange(peaks) {
    const lo = Math.min(...peaks);
    const hi = Math.max(...peaks);
    const mid = (lo + hi) / 2;
    if (hi - lo < 1e-10 * mid) return [mid - 0.01 * mid, mid + 0.01 * mid];
    const pad = 0.05 * (hi - lo);
    return [lo - pad, hi + pad];
}

// Side length of the square slice plot: the largest square that fits the
// container. With equal left+right and top+bottom margins the plot area is
// then square as well, so the range [-R, R] fills it exactly in both axes.
const SLICE_MARGIN = { l: 60, r: 20, t: 40, b: 40 };

const MAX_SLICE_SIZE = 430;

function sliceSize() {
    const box = document.getElementById("q-slice-plot");
    const size = Math.min(box.clientWidth, MAX_SLICE_SIZE);
    // Shrink the plot row to the square so the note below follows directly.
    box.parentElement.style.height = `${size}px`;
    return size;
}

function axisStyle(title) {
    return {
        title: { text: title, font: { color: TEXT }, standoff: 6 },
        tickfont: { color: MUTED },
        gridcolor: GRID,
        zerolinecolor: GRID,
        linecolor: TEXT,
        linewidth: 1,
    };
}

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

    // Slice of Q at the current parameters
    const sigmaQ = SPDC.sigmaQLossy(lam, etaH, etaV, theta);
    const detSigma = SPDC.det(sigmaQ);
    const K = sliceMatrix(SPDC.inv(sigmaQ));
    const Q0 = 1 / (Math.PI * Math.PI * Math.sqrt(detSigma));

    const R = sliceRange(lam, etaH, etaV);
    const axis = SPDC.linspace(-R, R, N_GRID);
    const Z = axis.map(y => axis.map(x => {
        const q = K[0][0] * x * x + 2 * K[0][1] * x * y + K[1][1] * y * y;
        return Q0 * Math.exp(-q / 2);
    }));

    const sliceTraces = [
        {
            type: "contour",
            x: axis,
            y: axis,
            z: Z,
            zmin: 0,
            zmax: Q0,
            colorscale: SEQUENTIAL,
            autocontour: false,
            contours: { start: Q0 / 14, end: Q0, size: Q0 / 14, coloring: "fill", showlines: true },
            line: { color: "#ffffff", width: 0.5 },
            showscale: false,
            hovertemplate: "Re α<sub>H</sub>=%{x:.2f}<br>Re α<sub>V</sub>=%{y:.2f}<br>Q=%{z:.4f}<extra></extra>",
        },
        {
            type: "scatter",
            x: [0],
            y: [0],
            mode: "markers",
            marker: { size: 11, color: ORANGE, line: { color: "#ffffff", width: 2 } },
            hovertemplate: `Q(0)=${Q0.toFixed(5)}<extra></extra>`,
        },
    ];

    const size = sliceSize();
    Plotly.react("q-slice-plot", sliceTraces, {
        title: { text: "Slice of Q at real α<sub>H</sub>, α<sub>V</sub>", font: { color: TEXT, size: 15 }, x: 0.5 },
        width: size,
        height: size,
        autosize: false,
        margin: SLICE_MARGIN,
        font: { color: TEXT, family: FONT },
        paper_bgcolor: "#ffffff",
        plot_bgcolor: "#ffffff",
        xaxis: { ...axisStyle("Re α<sub>H</sub>"), range: [-R, R], fixedrange: true, showgrid: false, zeroline: false },
        yaxis: { ...axisStyle("Re α<sub>V</sub>"), range: [-R, R], fixedrange: true, showgrid: false, zeroline: false },
        showlegend: false,
    }, { ...CONFIG, responsive: false });

    // Peak height pi^2 Q(0) = P(0,0) over the full theta range
    const thetas = SPDC.linspace(0, THETA_MAX, N_THETA);
    const peaks = thetas.map(th => 1 / Math.sqrt(SPDC.det(SPDC.sigmaQLossy(lam, etaH, etaV, th))));
    const P00 = Math.PI * Math.PI * Q0;
    const peakRange = peakAxisRange(peaks);

    Plotly.react("peak-height-plot", [
        {
            type: "scatter",
            x: thetas,
            y: peaks,
            mode: "lines",
            line: { width: 3, color: BLUE },
            hovertemplate: "ϑ=%{x:.3f}<br>π²Q(0)=%{y:.6f}<extra></extra>",
        },
        {
            type: "scatter",
            x: [theta],
            y: [P00],
            mode: "markers",
            marker: { size: 11, color: ORANGE, line: { color: "#ffffff", width: 2 } },
            hovertemplate: "ϑ=%{x:.3f}<br>π²Q(0)=%{y:.6f}<extra></extra>",
        },
    ], {
        title: { text: "Peak height π²Q(0) = P(0,0)", font: { color: TEXT, size: 15 }, x: 0.5 },
        // Same height and top/bottom margins as the square slice, so both
        // plotting areas line up.
        height: size,
        margin: { l: 64, r: 12, t: SLICE_MARGIN.t, b: SLICE_MARGIN.b },
        font: { color: TEXT, family: FONT },
        paper_bgcolor: "#ffffff",
        plot_bgcolor: "#ffffff",
        xaxis: {
            ...axisStyle("ϑ"),
            range: [0, THETA_MAX],
            tickvals: [0, Math.PI / 16, Math.PI / 8, 3 * Math.PI / 16, Math.PI / 4],
            ticktext: ["0", "π/16", "π/8", "3π/16", "π/4"],
            fixedrange: true,
        },
        yaxis: { ...axisStyle("P(0,0)"), range: peakRange, fixedrange: true, automargin: true },
        showlegend: false,
    }, CONFIG);

    document.getElementById("peak-note").textContent =
        `Q(0) = ${Q0.toFixed(6)},  π²Q(0) = ${P00.toFixed(6)},  closed form (46): P(0,0) = ${SPDC.p00(lam, etaH, etaV, theta).toFixed(6)}`;

    fitFrame();
}

window.addEventListener("resize", updatePlot);
updatePlot();
