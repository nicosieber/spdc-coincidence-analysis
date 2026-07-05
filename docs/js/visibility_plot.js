/**
 * visibility_plot.js — UI controller for the visibility dashboard.
 * Physics from the shared window.SPDC module (spdc_physics.js).
 */
let stepInterval = null;

function paddedRange(values, frac = 0.03) {
    const Vmin = Math.min(...values);
    const Vmax = Math.max(...values);

    let padding = frac * (Vmax - Vmin);

    if (padding === 0) {
        padding = 0.03 * Math.max(Math.abs(Vmax), 1e-6);
    }

    return [Vmin - padding, Vmax + padding];
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
    const etaV = readNumber("etaV");

    if (isNaN(lam) || isNaN(etaV)) return;

    const etaH = SPDC.linspace(0.01, 1.0, 1000);
    const V = etaH.map(eh => SPDC.visibility(lam, eh, etaV));

    const [ymin, ymax] = paddedRange(V, 0.03);

    document.getElementById("readout").innerHTML =
        `λ=${lam.toFixed(4)}, η<sub>V</sub>=${etaV.toFixed(4)}`;

    Plotly.update(
        "visibility-plot",
        {
            x: [etaH],
            y: [V]
        },
        {
            "yaxis.range": [ymin, ymax]
        }
    );
}
