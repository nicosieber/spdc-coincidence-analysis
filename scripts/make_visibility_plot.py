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

panel = "#ffffff"
blue = "#2980b9"
text = "#404040"
muted = "#6a6a6a"
grid = "#e1e4e5"

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=eta_H,
        y=V,
        mode="lines",
        line=dict(width=3, color=blue),
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
        family="Lato, proxima-nova, Helvetica Neue, Arial, sans-serif",
    ),
    xaxis=dict(
        title=dict(text="Detector efficiency ηH", font=dict(color=text), standoff=8),
        range=[0.01, 1.0],
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=1,
        tickfont=dict(color=muted),
    ),
    yaxis=dict(
        title=dict(text="Visibility", font=dict(color=text)),
        range=[ymin, ymax],
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=1,
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

styles = """
<link rel="stylesheet" href="../../stylesheets/coincidence_plots.css">
<style>
  #visibility-plot { height: 420px !important; }
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