let stepInterval = null;

function p00(lam, theta, eta_H, eta_V) {
    const radicand =
        Math.pow(1 - Math.pow(lam, 2) * (1 - eta_H) * (1 - eta_V), 2)
        - Math.pow(lam, 2) * Math.pow(eta_H - eta_V, 2) * Math.pow(Math.sin(4 * theta), 2);

    return (1 - Math.pow(lam, 2)) / Math.sqrt(radicand);
}

function linspace(start, stop, num) {
    const arr = [];
    const step = (stop - start) / (num - 1);
    for (let i = 0; i < num; i++) arr.push(start + step * i);
    return arr;
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

    const theta = linspace(0, Math.PI / 4, 1000);

    const C = theta.map(t => {
        const p00val = p00(lam, t, etaH, etaV);
        const pH0 = p00(lam, t, etaH, 0);
        const pV0 = p00(lam, t, 0, etaV);
        return 1 - pH0 - pV0 + p00val;
    });

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