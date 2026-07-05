from pathlib import Path

import numpy as np
import plotly.graph_objects as go


def p00(lam, theta, eta_H, eta_V):
    radicand = (
        (1 - lam**2 * (1 - eta_H) * (1 - eta_V)) ** 2
        - lam**2 * (eta_H - eta_V) ** 2 * np.sin(4 * theta) ** 2
    )
    return (1 - lam**2) / np.sqrt(radicand)


def make_curve(lam, eta_H, eta_V):
    theta = np.linspace(0, np.pi / 4, 1000)

    p00_vals = p00(lam, theta, eta_H, eta_V)
    pH0 = p00(lam, theta, eta_H, 0)
    pV0 = p00(lam, theta, 0, eta_V)

    C = 1 - pH0 - pV0 + p00_vals
    C_norm = C / np.max(C)

    Cmax = np.max(C)
    Cmin = np.min(C)
    visibility = (Cmax - Cmin) / (Cmax + Cmin)

    return theta, C_norm, visibility


output_dir = Path("docs/assets/plots")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "coincidence_plot.html"

default_lam = 0.6
default_eta_H = 0.7
default_eta_V = 0.7

theta, y, visibility = make_curve(default_lam, default_eta_H, default_eta_V)

page_bg = "#1f222b"
panel = "#252936"
lime = "#c9f23c"
text = "#e8ebf2"
muted = "#aeb4c2"
grid = "#3a4050"

tick_vals = [0, np.pi / 16, np.pi / 8, 3 * np.pi / 16, np.pi / 4]
tick_text = ["0", "π/16", "π/8", "3π/16", "π/4"]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=theta,
        y=y,
        mode="lines",
        line=dict(width=3, color=lime),
        hovertemplate="ϑ=%{x:.4f}<br>C/Cmax=%{y:.4f}<extra></extra>",
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
            text="Half-wave plate angle 𝝑",
            font=dict(color=text),
            standoff=8,
        ),
        range=[0, np.pi / 4],
        gridcolor=grid,
        zerolinecolor=grid,
        linecolor=text,
        linewidth=2,
        tickfont=dict(color=muted),
        tickvals=tick_vals,
        ticktext=tick_text,
    ),
    yaxis=dict(
        title=dict(text="Normalized coincidence", font=dict(color=text)),
        range=[0, 1.05],
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
    div_id="coincidence-plot",
    config={"displaylogo": False, "responsive": True},
)

controls = f"""
<div class="plot-card">
  <div class="header">
    <div class="eyebrow">INTERACTIVE PLOT</div>

    <div id="readout" class="readout">
      λ={default_lam:.4f}, η<sub>H</sub>={default_eta_H:.4f}, η<sub>V</sub>={default_eta_V:.4f}, Visibility={visibility:.4f}
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
<link rel="stylesheet"
      href="../../stylesheets/coincidence_plots.css">
"""

html = html.replace(
    "<head>",
    f"<head>{css_link}"
)


html = html.replace("<body>", f"<body>{controls}")

script_tag = """
<script src="../../js/coincidence_plot.js"></script>
"""

html = html.replace(
    "</body>",
    f"</div>{script_tag}</body>"
)

output_file.write_text(html, encoding="utf-8")

print(f"Wrote {output_file}")