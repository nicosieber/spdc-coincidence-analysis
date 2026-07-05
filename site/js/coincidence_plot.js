/**
 * coincidence_plot.js — UI controller for the coincidence dashboard.
 * All physics comes from the shared window.SPDC module (spdc_physics.js);
 * this file only wires the spinboxes to a Plotly redraw.
 */
let stepInterval = null;

function linspace(start, stop, num) {
    return SPDC.linspace(start, stop, num);
}

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

    const theta = SPDC.linspace(0, Math.PI / 4, 1000);

    const C = theta.map(t => SPDC.coincidence(lam, etaH, etaV, t));

    const Cmax = Math.max(...C);
    const Cmin = Math.min(...C);
    const Cnorm = C.map(v => v / Cmax);
    const visibility = (Cmax - Cmin) / (Cmax + Cmin);

    document.getElementById("readout").innerHTML =
        `λ=${lam.toFixed(4)}, η<sub>H</sub>=${etaH.toFixed(4)}, η<sub>V</sub>=${etaV.toFixed(4)}, Visibility=${visibility.toFixed(4)}`;

    Plotly.update("coincidence-plot", {
        x: [theta],
        y: [Cnorm]
    });
}
