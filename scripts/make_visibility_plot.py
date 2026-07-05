"""
Generate the interactive visibility-vs-efficiency Plotly iframe.

Physics is imported from the shared ``spdc`` package (single source of
truth); the in-browser slider recompute uses ``docs/js/spdc_physics.js``.
"""
from pathlib import Path

import numpy as np
import plotly.graph_objects as go

from spdccc import coincidence


def make_curve(lam, eta_V):
    eta_H = np.linspace(0.01, 1.0, 1000)
    # Visibility from the coincidence extremes: Cmax at theta=0, Cmin at
    # theta=pi/8 (identical convention to spdc_physics.js SPDC.visibility).
    Cmax = coincidence(lam, eta_H, eta_V, 0.0)
    Cmin = coincidence(lam, eta_H, eta_V, np.pi / 8)
    V = (Cmax - Cmin) / (Cmax + Cmin)
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

custom_js = """
<script src="../../js/spdc_physics.js"></script>
<script src="../../js/visibility_plot.js"></script>
"""

html = html.replace("<head>", f"<head>{styles}")
html = html.replace("<body>", f"<body>{controls}")
html = html.replace("</body>", f"</div>{custom_js}</body>")

output_file.write_text(html, encoding="utf-8")

print(f"Wrote {output_file}")