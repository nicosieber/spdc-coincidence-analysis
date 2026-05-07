import numpy as np
import plotly.graph_objects as go
from pathlib import Path


def p00(lam, theta, eta_H, eta_V):
    radicand = (
        (1 - lam**2 * (1 - eta_H) * (1 - eta_V))**2
        - lam**2 * (eta_H - eta_V)**2 * np.sin(4 * theta)**2
    )
    radicand = np.maximum(radicand, 1e-15)
    return (1 - lam**2) / np.sqrt(radicand)


def coincidence(lam, theta, eta_H, eta_V):
    pHV0 = p00(lam, theta, eta_H, eta_V)
    pH0 = p00(lam, theta, eta_H, 0)
    pV0 = p00(lam, theta, 0, eta_V)
    return 1 - pH0 - pV0 + pHV0


def visibility(lam, eta_H, eta_V):
    Cmax = coincidence(lam, 0, eta_H, eta_V)
    Cmin = coincidence(lam, np.pi / 8, eta_H, eta_V)
    return (Cmax - Cmin) / (Cmax + Cmin)


def make_curve(lam, eta_V):
    eta_H = np.linspace(0.01, 1.0, 1000)
    V = visibility(lam, eta_H, eta_V)
    return eta_H, V


def padded_range(values, frac=0.03):
    vmin = np.min(values)
    vmax = np.max(values)
    pad = frac * (vmax - vmin)

    if pad == 0:
        pad = 0.03 * max(abs(vmax), 1e-6)

    return vmin - pad, vmax + pad


output_dir = Path("docs/assets/plots")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "visibility_vs_etaH_plot.html"

default_lam = 0.93
default_eta_V = 0.3

eta_H, V = make_curve(default_lam, default_eta_V)
ymin, ymax = padded_range(V)

page_bg = "#1f222b"
panel = "#252936"
lime = "#c9f23c"
text = "#e8ebf2"
muted = "#aeb4c2"
grid = "#3a4050"

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=eta_H,
        y=V,
        mode="lines",
        line=dict(width=3, color=lime),
        hovertemplate="ηH=%{x:.4f}<br>V=%{y:.4f}<extra></extra>",
    )
)

fig.update_layout(
    height=480,
    paper_bgcolor=panel,
    plot_bgcolor=panel,
    margin=dict(l=72, r=20, t=4, b=10),
    font=dict(
        color=text,
        family="system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
    ),
    xaxis=dict(
        title=dict(text="Detector efficiency ηH", font=dict(color=text), standoff=8),
        range=[0.01, 1.0],
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=2,
        tickfont=dict(color=muted),
    ),
    yaxis=dict(
        title=dict(text="Visibility", font=dict(color=text)),
        range=[ymin, ymax],
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=2,
        tickfont=dict(color=muted),
    ),
    showlegend=False,
)

html = fig.to_html(
    include_plotlyjs="cdn",
    full_html=True,
    div_id="visibility-plot",
    config={"displaylogo": False, "responsive": True},
)

controls = f"""
<div class="plot-card">
  <div class="header">
    <div class="eyebrow">INTERACTIVE PLOT</div>

    <div id="readout" class="readout">
      λ={default_lam:.4f}, η<sub>V</sub>={default_eta_V:.4f}
    </div>
  </div>

  <div class="controls">
    <div class="input-group">
      <span>λ</span>
      <div class="spinbox">
        <button
          onmousedown="startStepping('lam', -0.01)"
          onmouseup="stopStepping()"
          onmouseleave="stopStepping()"
          ontouchstart="startStepping('lam', -0.01)"
          ontouchend="stopStepping()"
        >-</button>
        <input id="lam" type="text" inputmode="decimal" value="{default_lam}" oninput="updatePlot()">
        <button
          onmousedown="startStepping('lam', 0.01)"
          onmouseup="stopStepping()"
          onmouseleave="stopStepping()"
          ontouchstart="startStepping('lam', 0.01)"
          ontouchend="stopStepping()"
        >+</button>
      </div>
    </div>

    <div class="input-group">
      <span>η<sub>V</sub></span>
      <div class="spinbox">
        <button
          onmousedown="startStepping('etaV', -0.01)"
          onmouseup="stopStepping()"
          onmouseleave="stopStepping()"
          ontouchstart="startStepping('etaV', -0.01)"
          ontouchend="stopStepping()"
        >-</button>
        <input id="etaV" type="text" inputmode="decimal" value="{default_eta_V}" oninput="updatePlot()">
        <button
          onmousedown="startStepping('etaV', 0.01)"
          onmouseup="stopStepping()"
          onmouseleave="stopStepping()"
          ontouchstart="startStepping('etaV', 0.01)"
          ontouchend="stopStepping()"
        >+</button>
      </div>
    </div>
  </div>
"""

styles = f"""
<style>
html, body {{
  width: 100%;
  height: 580px;
  margin: 0;
  padding: 0;
  background: {page_bg};
  color: {text};
  overflow: hidden;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

.plot-card {{
  box-sizing: border-box;
  width: 100%;
  height: 580px;
  background: {panel};
  border-radius: 18px;
  padding: 18px 20px 10px 20px;
  overflow: hidden;
}}

.header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 12px;
}}

.eyebrow {{
  color: {lime};
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.16em;
}}

.readout {{
  color: {lime};
  font-size: 0.92rem;
  font-weight: 700;
  white-space: nowrap;
  padding-top: 2px;
}}

.controls {{
  display: flex;
  gap: 28px;
  align-items: center;
  margin-bottom: 4px;
}}

.input-group {{
  display: flex;
  align-items: center;
  gap: 8px;
  color: {text};
  font-weight: 700;
}}

.input-group > span {{
  color: {lime};
  font-size: 1.05rem;
}}

sub {{
  font-size: 0.7em;
  vertical-align: sub;
}}

.spinbox {{
  display: flex;
  align-items: center;
  border: 1px solid {lime};
  border-radius: 12px;
  overflow: hidden;
  background: #171a22;
}}

.spinbox input {{
  width: 76px;
  background: #171a22;
  color: {text};
  border: none;
  text-align: center;
  padding: 6px 4px;
  font-size: 0.95rem;
  outline: none;
}}

.spinbox button {{
  width: 30px;
  height: 32px;
  background: #171a22;
  color: {lime};
  border: none;
  font-size: 0.95rem;
  font-weight: 800;
  cursor: pointer;
  user-select: none;
  touch-action: none;
}}

.spinbox button:hover {{
  background: {lime};
  color: #171a22;
}}

#visibility-plot {{
  height: 420px !important;
}}
</style>
"""

custom_js = r"""
<script>
let stepInterval = null;

function p00(lam, theta, eta_H, eta_V) {
    const radicand =
        Math.pow(1 - Math.pow(lam, 2) * (1 - eta_H) * (1 - eta_V), 2)
        - Math.pow(lam, 2)
        * Math.pow(eta_H - eta_V, 2)
        * Math.pow(Math.sin(4 * theta), 2);

    return (1 - Math.pow(lam, 2)) / Math.sqrt(Math.max(radicand, 1e-15));
}

function coincidence(lam, theta, eta_H, eta_V) {
    const pHV0 = p00(lam, theta, eta_H, eta_V);
    const pH0 = p00(lam, theta, eta_H, 0);
    const pV0 = p00(lam, theta, 0, eta_V);

    return 1 - pH0 - pV0 + pHV0;
}

function visibility(lam, eta_H, eta_V) {
    const Cmax = coincidence(lam, 0, eta_H, eta_V);
    const Cmin = coincidence(lam, Math.PI / 8, eta_H, eta_V);

    return (Cmax - Cmin) / (Cmax + Cmin);
}

function paddedRange(values, frac = 0.03) {
    const Vmin = Math.min(...values);
    const Vmax = Math.max(...values);

    let padding = frac * (Vmax - Vmin);

    if (padding === 0) {
        padding = 0.03 * Math.max(Math.abs(Vmax), 1e-6);
    }

    return [Vmin - padding, Vmax + padding];
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
    const etaV = readNumber("etaV");

    if (isNaN(lam) || isNaN(etaV)) return;

    const etaH = linspace(0.01, 1.0, 1000);
    const V = etaH.map(eh => visibility(lam, eh, etaV));

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
</script>
"""

html = html.replace("<head>", f"<head>{styles}")
html = html.replace("<body>", f"<body>{controls}")
html = html.replace("</body>", f"</div>{custom_js}</body>")

output_file.write_text(html, encoding="utf-8")

print(f"Wrote {output_file}")