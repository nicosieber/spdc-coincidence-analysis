"""
Generate the QuTiP-engine coincidence dashboard iframe.

QuTiP twin of ``make_cc_plot_numpy.py``. On top of the closed-form coincidence
curve it overlays a numerical truncated-Fock simulation at fixed Hilbert
dimension N=60: open-circle markers sampled at a handful of HWP angles, plus a
log-scale residual break-off panel showing |numeric - closed| at those angles.

The *static default render* here is computed by genuine QuTiP
(``spdc.fock_qutip.brute_Pcoinc`` — sparse operators, power series on the
state). The browser cannot run QuTiP, so the *live* recompute on drag uses the
shared array engine ``spdc_physics.js`` (fockCoincidence), which is the
validated numerical twin of spdc.fock_qutip (agreement to the truncation floor,
~1e-11, at every benchmark point). The pedagogical point matches the NumPy
page: as lambda grows the mean photon number climbs past what N=60 Fock states
can represent, so the numerical markers lift off the (truncation-free) closed
form.

The in-browser recompute lives in docs/js/qutip_dashboard.js.
"""
from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from spdccc import coincidence
from spdccc .fock_qutip import brute_Pcoinc

# Fixed Fock-space parameters (mirrored in qutip_dashboard.js).
N_FOCK = 60
NMAX_FOCK = 45
N_MARKERS = 15


def make_curves(lam, eta_H, eta_V):
    theta = np.linspace(0, np.pi / 4, 1000)
    C = coincidence(lam, eta_H, eta_V, theta)
    Cmax = np.max(C)
    C_norm = C / Cmax

    theta_m = np.linspace(0, np.pi / 4, N_MARKERS)
    closed_m = coincidence(lam, eta_H, eta_V, theta_m) / Cmax
    fock_m = np.array(
        [brute_Pcoinc(lam, eta_H, eta_V, t, N=N_FOCK, nmax=NMAX_FOCK) for t in theta_m]
    ) / Cmax
    resid = np.abs(fock_m - closed_m)

    Cmin = np.min(C)
    visibility = (Cmax - Cmin) / (Cmax + Cmin)
    return theta, C_norm, theta_m, closed_m, fock_m, resid, visibility


output_dir = Path("docs/assets/plots")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "coincidence_plot.html"

default_lam = 0.6
default_eta_H = 0.7
default_eta_V = 0.7

(theta, y, theta_m, closed_m, fock_m, resid, visibility) = make_curves(
    default_lam, default_eta_H, default_eta_V
)

page_bg = "#1f222b"
panel = "#252936"
lime = "#c9f23c"
text = "#e8ebf2"
muted = "#aeb4c2"
grid = "#3a4050"
amber = "#ff9f43"  # QuTiP markers / residual — reads as "the numeric one"

tick_vals = [0, np.pi / 16, np.pi / 8, 3 * np.pi / 16, np.pi / 4]
tick_text = ["0", "π/16", "π/8", "3π/16", "π/4"]

# Floor residuals so the log panel never sees a zero.
resid_floor = np.maximum(resid, 1e-16)

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    row_heights=[0.72, 0.28],
    vertical_spacing=0.07,
)

# --- top: closed-form curve + QuTiP markers ----------------------------
fig.add_trace(
    go.Scatter(
        x=theta,
        y=y,
        mode="lines",
        line=dict(width=3, color=lime),
        name="closed form",
        hovertemplate="ϑ=%{x:.4f}<br>C/Cmax=%{y:.4f}<extra>closed form</extra>",
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=theta_m,
        y=fock_m,
        mode="markers",
        marker=dict(
            symbol="circle-open",
            size=9,
            color=amber,
            line=dict(width=2, color=amber),
        ),
        name=f"QuTiP N={N_FOCK}",
        hovertemplate="ϑ=%{x:.4f}<br>C/Cmax=%{y:.4f}<extra>QuTiP N=60</extra>",
    ),
    row=1,
    col=1,
)

# --- bottom: residual break-off (log scale) ----------------------------
fig.add_trace(
    go.Scatter(
        x=theta_m,
        y=resid_floor,
        mode="lines+markers",
        line=dict(width=1.5, color=amber),
        marker=dict(symbol="circle", size=5, color=amber),
        name="|QuTiP − closed|",
        hovertemplate="ϑ=%{x:.4f}<br>|Δ|=%{y:.2e}<extra></extra>",
    ),
    row=2,
    col=1,
)

fig.update_layout(
    height=560,
    paper_bgcolor=panel,
    plot_bgcolor=panel,
    margin=dict(l=72, r=20, t=4, b=10),
    font=dict(
        color=text,
        family="system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
    ),
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="right",
        x=1.0,
        font=dict(color=muted, size=11),
        bgcolor="rgba(0,0,0,0)",
    ),
)

# Top y-axis (normalized coincidence)
fig.update_yaxes(
    title=dict(text="Normalized coincidence", font=dict(color=text)),
    range=[0, 1.08],
    gridcolor=grid,
    zerolinecolor=grid,
    linecolor=text,
    linewidth=2,
    tickfont=dict(color=muted),
    row=1,
    col=1,
)
# Bottom y-axis (log residual)
fig.update_yaxes(
    title=dict(text="|QuTiP - closed|", font=dict(color=text)),
    type="log",
    range=[-16, -0.3],
    gridcolor=grid,
    zerolinecolor=grid,
    linecolor=text,
    linewidth=2,
    tickfont=dict(color=muted),
    dtick=3,  # decade gridlines every 4 orders
    exponentformat="power",      # 10^-n labels, not SI prefixes (µ, n, p)
    showexponent="all",
    row=2,
    col=1,
)
# Shared x-axis (angle) — label only on bottom
fig.update_xaxes(
    range=[0, np.pi / 4],
    gridcolor=grid,
    zerolinecolor=grid,
    linecolor=text,
    linewidth=2,
    tickfont=dict(color=muted),
    tickvals=tick_vals,
    ticktext=tick_text,
    row=1,
    col=1,
)
fig.update_xaxes(
    title=dict(text="Half-wave plate angle 𝝑", font=dict(color=text), standoff=8),
    range=[0, np.pi / 4],
    gridcolor=grid,
    zerolinecolor=grid,
    linecolor=text,
    linewidth=2,
    tickfont=dict(color=muted),
    tickvals=tick_vals,
    ticktext=tick_text,
    row=2,
    col=1,
)

html = fig.to_html(
    include_plotlyjs="cdn",
    full_html=True,
    div_id="coincidence-plot",
    config={"displaylogo": False, "responsive": True},
)

max_resid = float(np.max(resid))

controls = f"""
<div class="plot-card">
  <div class="header">
    <div id="readout" class="readout">
      λ={default_lam:.4f}, η<sub>H</sub>={default_eta_H:.4f}, η<sub>V</sub>={default_eta_V:.4f}, V={visibility:.4f}, max|numeric−closed|={max_resid:.2e}
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
<style>
  /* Page-scoped override: the shared coincidence_plots.css is sized for the
     single-panel widget (body/card clamped to 580px, #coincidence-plot forced
     to 420px). This two-panel figure (coincidence + residual break-off) needs
     more room, so we relax the clamps for THIS page only. */
  html, body { height: auto !important; overflow: visible !important; }
  .plot-card { height: auto !important; overflow: visible !important; }
  #coincidence-plot { height: 560px !important; }
  /* Two-line readout: let it wrap instead of overflowing the card. */
  .readout { white-space: normal !important; line-height: 1.45; }
</style>
"""

html = html.replace("<head>", f"<head>{css_link}")
html = html.replace("<body>", f"<body>{controls}")

script_tag = """
<script src="../../js/spdc_physics.js"></script>
<script src="../../js/qutip_dashboard.js"></script>
"""

html = html.replace("</body>", f"</div>{script_tag}</body>")

output_file.write_text(html, encoding="utf-8")

print(f"Wrote {output_file}")