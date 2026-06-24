from pathlib import Path

import numpy as np
import sympy as sp
import plotly.graph_objects as go


# ── Symbolic setup: exact analytic derivatives via sympy ────────────────────
#
# We differentiate w.r.t. theta, then apply the chain rule to get F w.r.t.
# the optical phase phi = 4*theta:
#
#   F_phi = F_theta * (d theta / d phi)^2 = F_theta / 16

lam_s, etaH_s, etaV_s, th_s = sp.symbols("lambda eta_H eta_V theta", positive=True)


def _P00_sym(etaH_, etaV_, th_):
    num = 1 - lam_s**2
    t1  = 1 - lam_s**2 * (1 - etaH_) * (1 - etaV_)
    den = sp.sqrt(t1**2 - lam_s**2 * (etaH_ - etaV_)**2 * sp.sin(4 * th_)**2)
    return num / den


P00    = _P00_sym(etaH_s, etaV_s, th_s)
PH0    = _P00_sym(etaH_s, 0,      th_s)
PV0    = _P00_sym(0,      etaV_s, th_s)
Pclick = 1 - P00

p11_sym = (1 - PH0 - PV0 + P00) / Pclick   # coincidence
p20_sym = (PV0 - P00)            / Pclick   # H-only
p02_sym = (PH0 - P00)            / Pclick   # V-only

_syms = (lam_s, etaH_s, etaV_s, th_s)

_fp  = [sp.lambdify(_syms, x,                   "numpy") for x in (p11_sym, p20_sym, p02_sym)]
_fdp = [sp.lambdify(_syms, sp.diff(x, th_s),    "numpy") for x in (p11_sym, p20_sym, p02_sym)]


# ── Fisher information w.r.t. phi = 4*theta ────────────────────────────────

def fisher_phi(lam, eta_H, eta_V, phi):
    """
    Classical Fisher information F(phi) for estimating the optical phase
    phi = 4*theta implemented by a HWP at angle theta.

    F_phi = F_theta / 16   (chain rule: d theta/d phi = 1/4)

    where  F_theta = sum_{i in {11,20,02}} [d p_i / d theta]^2 / p_i

    and p_i are the click-conditioned probabilities (recorded trials only).
    Derivatives are exact analytic expressions obtained via sympy.
    """
    phi  = np.asarray(phi, dtype=float)
    th   = phi / 4.0
    eps  = 1e-15
    F    = np.zeros_like(th)
    for fp, fdp in zip(_fp, _fdp):
        p  = fp(lam, eta_H, eta_V, th)
        dp = fdp(lam, eta_H, eta_V, th)
        F += np.where(p > eps, dp**2 / p, 0.0)
    return F / 16.0


def snl_phi(lam, eta_H, eta_V, phi):
    """
    Shot-noise limit F_SNL(phi) = mean photons per recorded trial.

    F_SNL = n_bar / P_click,  with  n_bar = 2*lambda^2/(1-lambda^2)
    the mean TMSV photon number per SPDC attempt, and
    P_click = 1 - P00 the probability that at least one detector fires.

    Flat in phi for symmetric losses (eta_H = eta_V); weakly phase-dependent
    otherwise, through the (eta_H - eta_V)^2 sin^2(4 theta) term in P00.
    """
    phi    = np.asarray(phi, dtype=float)
    th     = phi / 4.0
    n_mean = 2.0 * lam**2 / (1.0 - lam**2)
    t1     = 1.0 - lam**2 * (1.0 - eta_H) * (1.0 - eta_V)
    P00v   = (1.0 - lam**2) / np.sqrt(t1**2 - lam**2 * (eta_H - eta_V)**2 * np.sin(4.0 * th)**2)
    return n_mean / (1.0 - P00v)


def make_curve(lam, eta_H, eta_V):
    # phi = 4*theta, theta in [0, pi/4]  =>  phi in [0, pi]
    phi   = np.linspace(1e-4, np.pi - 1e-4, 1000)
    F     = fisher_phi(lam, eta_H, eta_V, phi)
    SNL   = snl_phi(lam, eta_H, eta_V, phi)
    F_max = float(np.max(F))
    return phi, F, SNL, F_max


# ── Build HTML ───────────────────────────────────────────────────────────────

output_dir  = Path("docs/assets/plots")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "fisher_plot.html"

default_lam   = 0.1235
default_eta_H = 0.8
default_eta_V = 0.8

phi, F, SNL, F_max = make_curve(default_lam, default_eta_H, default_eta_V)

# ── Style (matches coincidence_plot.html) ────────────────────────────────────
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

# ── Controls (same spinbox pattern as coincidence_plot.html) ─────────────────

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

# ── Inline JS ────────────────────────────────────────────────────────────────
#
# F_phi(phi) = F_theta(theta) / 16,  with theta = phi / 4
#
# p_i and dp_i/dtheta are exact analytic expressions from sympy.ccode.
# The /16 chain-rule factor is applied in fisherAt().
#
# F_SNL(phi) = n_bar / (1 - P00),  n_bar = 2*lam^2/(1-lam^2)

script = r"""
<script>
(function () {
  // ── Exact analytic expressions (generated by sympy.ccode) ──────────────
  // All functions take (lam, etaH, etaV, th) where th = phi/4.

  function P00(lam, etaH, etaV, th) {
    const t1 = 1 - Math.pow(lam, 2)*(1 - etaH)*(1 - etaV);
    return (1 - Math.pow(lam, 2))/Math.sqrt(t1*t1 - Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2));
  }

  function p11(lam, etaH, etaV, th) {
    return ((1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) - (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaV, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaV) + 1, 2)) - (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaH, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH) + 1, 2)) + 1)/(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1);
  }

  function p20(lam, etaH, etaV, th) {
    return (-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaV, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaV) + 1, 2)))/(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1);
  }

  function p02(lam, etaH, etaV, th) {
    return (-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaH, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH) + 1, 2)))/(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1);
  }

  function dp11(lam, etaH, etaV, th) {
    return 4*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.pow(etaH - etaV, 2)*((1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) - (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaV, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaV) + 1, 2)) - (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaH, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH) + 1, 2)) + 1)*Math.sin(4*th)*Math.cos(4*th)/(Math.pow(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1, 2)*Math.pow(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2), 3.0/2.0)) + (-4*Math.pow(etaH, 2)*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(etaH, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH) + 1, 2), 3.0/2.0) - 4*Math.pow(etaV, 2)*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(etaV, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaV) + 1, 2), 3.0/2.0) + 4*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.pow(etaH - etaV, 2)*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2), 3.0/2.0))/(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1);
  }

  function dp20(lam, etaH, etaV, th) {
    return 4*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.pow(etaH - etaV, 2)*(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaV, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaV) + 1, 2)))*Math.sin(4*th)*Math.cos(4*th)/(Math.pow(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1, 2)*Math.pow(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2), 3.0/2.0)) + (4*Math.pow(etaV, 2)*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(etaV, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaV) + 1, 2), 3.0/2.0) - 4*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.pow(etaH - etaV, 2)*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2), 3.0/2.0))/(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1);
  }

  function dp02(lam, etaH, etaV, th) {
    return 4*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.pow(etaH - etaV, 2)*(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + (1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(etaH, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH) + 1, 2)))*Math.sin(4*th)*Math.cos(4*th)/(Math.pow(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1, 2)*Math.pow(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2), 3.0/2.0)) + (4*Math.pow(etaH, 2)*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(etaH, 2)*Math.pow(lam, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH) + 1, 2), 3.0/2.0) - 4*Math.pow(lam, 2)*(1 - Math.pow(lam, 2))*Math.pow(etaH - etaV, 2)*Math.sin(4*th)*Math.cos(4*th)/Math.pow(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2), 3.0/2.0))/(-(1 - Math.pow(lam, 2))/Math.sqrt(-Math.pow(lam, 2)*Math.pow(etaH - etaV, 2)*Math.pow(Math.sin(4*th), 2) + Math.pow(-Math.pow(lam, 2)*(1 - etaH)*(1 - etaV) + 1, 2)) + 1);
  }

  // ── F_phi at a single phi value ─────────────────────────────────────────
  // Chain rule: F_phi = F_theta / 16  (since theta = phi/4, d theta/d phi = 1/4)
  function fisherAt(lam, etaH, etaV, phi) {
    const th  = phi / 4;
    const eps = 1e-15;
    const pairs = [
      [p11(lam, etaH, etaV, th), dp11(lam, etaH, etaV, th)],
      [p20(lam, etaH, etaV, th), dp20(lam, etaH, etaV, th)],
      [p02(lam, etaH, etaV, th), dp02(lam, etaH, etaV, th)],
    ];
    const F_theta = pairs.reduce((s, [p, dp]) => s + (p > eps ? dp * dp / p : 0), 0);
    return F_theta / 16;
  }

  // ── Shot-noise limit at a single phi value ──────────────────────────────
  // F_SNL = n_bar / P_click,  n_bar = 2*lam^2/(1-lam^2),  P_click = 1 - P00
  function snlAt(lam, etaH, etaV, phi) {
    const th     = phi / 4;
    const n_mean = 2 * Math.pow(lam, 2) / (1 - Math.pow(lam, 2));
    return n_mean / (1 - P00(lam, etaH, etaV, th));
  }

  // ── Build phi grid and both curves ──────────────────────────────────────
  // phi = 4*theta, theta in [0, pi/4]  =>  phi in [0, pi]
  const N = 1000;
  function buildCurve(lam, etaH, etaV) {
    const phis = [], Fvals = [], SNLvals = [];
    for (let i = 0; i < N; i++) {
      const phi = 1e-4 + (Math.PI - 2e-4) * i / (N - 1);
      phis.push(phi);
      Fvals.push(fisherAt(lam, etaH, etaV, phi));
      SNLvals.push(snlAt(lam, etaH, etaV, phi));
    }
    const Fmax   = Math.max(...Fvals);
    const SNLmax = Math.max(...SNLvals);
    return { phis, Fvals, SNLvals, Fmax, SNLmax };
  }

  // ── Stepping logic (matches coincidence_plot.js pattern) ─────────────────
  let stepInterval = null;

  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  function step(id, delta) {
    const el  = document.getElementById(id);
    const lo  = 0.01;
    const hi  = id === "lam" ? 0.99 : 1.00;
    const val = clamp(parseFloat(el.value) + delta, lo, hi);
    el.value  = val.toFixed(2);
    updatePlot();
  }

  window.startStepping = function (id, delta) {
    step(id, delta);
    stepInterval = setInterval(() => step(id, delta), 120);
  };

  window.stopStepping = function () {
    clearInterval(stepInterval);
    stepInterval = null;
  };

  // ── Update Plotly trace ──────────────────────────────────────────────────
  window.updatePlot = function () {
    const lam  = clamp(parseFloat(document.getElementById("lam").value),  0.01, 0.99);
    const etaH = clamp(parseFloat(document.getElementById("etaH").value), 0.01, 1.00);
    const etaV = clamp(parseFloat(document.getElementById("etaV").value), 0.01, 1.00);

    if (isNaN(lam) || isNaN(etaH) || isNaN(etaV)) return;

    const { phis, Fvals, SNLvals, Fmax, SNLmax } = buildCurve(lam, etaH, etaV);

    // y-range covers whichever curve is higher, so the SNL stays visible
    const yTop = Math.max(Fmax, SNLmax) * 1.05;

    Plotly.update("fisher-plot",
      { x: [phis, phis], y: [Fvals, SNLvals] },
      { "yaxis.range": [0, yTop] }
    );

    document.getElementById("readout").innerHTML =
      `λ=${lam.toFixed(4)}, η<sub>H</sub>=${etaH.toFixed(4)}, ` +
      `η<sub>V</sub>=${etaV.toFixed(4)}, ` +
      `<i>F</i><sub>max</sub>=${Fmax.toFixed(4)}`;
  };
})();
</script>
"""

html = html.replace("</body>", f"</div>{script}</body>")

output_file.write_text(html, encoding="utf-8")
print(f"Wrote {output_file}")