"""
Generate the interactive Fisher-information Plotly iframe.

Physics is imported from the shared ``spdc`` package (single source of
truth): ``fisher_phi`` and ``snl_phi`` are the same analytic, sympy-derived
functions used everywhere in the project. The in-browser slider recompute
uses ``docs/js/spdc_physics.js`` (whose Fisher expressions are emitted by
sympy.jscode from the identical symbolic closed form).
"""
from pathlib import Path

import numpy as np
import plotly.graph_objects as go

from spdccc import fisher_phi, snl_phi


def make_curve(lam, eta_H, eta_V):
    # phi = 4*theta, theta in [0, pi/4]  =>  phi in [0, pi]
    phi   = np.linspace(1e-4, np.pi - 1e-4, 1000)
    F     = fisher_phi(lam, eta_H, eta_V, phi)
    SNL   = snl_phi(lam, eta_H, eta_V, phi)
    F_max = float(np.max(F))
    return phi, F, SNL, F_max


# Build HTML

output_dir  = Path("docs/assets/plots")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "fisher_plot.html"

default_lam   = 0.1235
default_eta_H = 0.8
default_eta_V = 0.8

phi, F, SNL, F_max = make_curve(default_lam, default_eta_H, default_eta_V)

# Style
panel  = "#252936"
lime   = "#c9f23c"
orange = "#ff9d4d"   # F_SNL reference line
text   = "#e8ebf2"
muted  = "#aeb4c2"
grid   = "#3a4050"


# phi in [0, pi]: use clean quarter-pi tick marks
tick_vals = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
tick_text = ["0", "π/4", "π/2", "3π/4", "π"]

fig = go.Figure()

# Fisher information curve
fig.add_trace(
    go.Scatter(
        x=phi,
        y=F,
        mode="lines",
        name="<i>F</i>(φ)",
        line=dict(width=3, color=lime),
        hovertemplate="φ=%{x:.4f}<br><i>F</i>=%{y:.4f}<extra></extra>",
    )
)

# Shot-noise limit
fig.add_trace(
    go.Scatter(
        x=phi,
        y=SNL,
        mode="lines",
        name="<i>F</i>_SNL(φ)",
        line=dict(width=2, color=orange, dash="dash"),
        hovertemplate="φ=%{x:.4f}<br><i>F</i>_SNL=%{y:.4f}<extra></extra>",
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
        title=dict(
            text="Optical phase φ = 4ϑ",
            font=dict(color=text),
            standoff=8,
        ),
        range=[0, np.pi],
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=2,
        tickfont=dict(color=muted),
        tickvals=tick_vals,
        ticktext=tick_text,
    ),
    yaxis=dict(
        title=dict(text="Fisher information <i>F</i>(φ)", font=dict(color=text)),
        rangemode="tozero",
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=2,
        tickfont=dict(color=muted),
    ),
    legend=dict(
        x=0.99, y=0.95, xanchor="right", yanchor="top",
        bgcolor="rgba(37,41,54,0.7)",
        font=dict(color=text, size=12),
    ),
    showlegend=True,
)

html = fig.to_html(
    include_plotlyjs="cdn",
    full_html=True,
    div_id="fisher-plot",
    config={"displaylogo": False, "responsive": True},
)

# Controls

controls = f"""
<div class="plot-card">
  <div class="header">
    <div class="eyebrow">INTERACTIVE PLOT</div>
    <div id="readout" class="readout">
      λ={default_lam:.4f},
      η<sub>H</sub>={default_eta_H:.4f},
      η<sub>V</sub>={default_eta_V:.4f},
      <i>F</i><sub>max</sub>={F_max:.4f}
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
      <span>η<sub>H</sub></span>
      <div class="spinbox">
        <button
          onmousedown="startStepping('etaH', -0.01)"
          onmouseup="stopStepping()"
          onmouseleave="stopStepping()"
          ontouchstart="startStepping('etaH', -0.01)"
          ontouchend="stopStepping()"
        >-</button>
        <input id="etaH" type="text" inputmode="decimal" value="{default_eta_H}" oninput="updatePlot()">
        <button
          onmousedown="startStepping('etaH', 0.01)"
          onmouseup="stopStepping()"
          onmouseleave="stopStepping()"
          ontouchstart="startStepping('etaH', 0.01)"
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

css_link = """
<link rel="stylesheet" href="../../stylesheets/coincidence_plots.css">
"""

html = html.replace("<head>", f"<head>{css_link}")
html = html.replace("<body>", f"<body>{controls}")

script = """
<script src="../../js/spdc_physics.js"></script>
<script src="../../js/fisher_plot.js"></script>
"""

html = html.replace("</body>", f"</div>{script}</body>")

output_file.write_text(html, encoding="utf-8")
print(f"Wrote {output_file}")