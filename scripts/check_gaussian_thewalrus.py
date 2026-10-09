"""
Numerical check of the Gaussian formalism against ``thewalrus``.

Builds the lossy state with an independent library (two-mode squeezer =
SPDC source, interferometer(U) = HWP, loss = detector efficiency) and
compares, at random parameters,

1. the closed form P(0,0), eq. (46),
2. 1/sqrt(det sigma_Q') with sigma_Q' = thewalrus.quantum.Qmat,
3. thewalrus' threshold-detection probability for "no click",

and the coincidence probability, eq. (50), with the library's Torontonian.
Then Qmat is compared entry by entry with the explicit matrix (35a).

Finally a figure compares P(0,0) and P_cc with thewalrus over the full HWP
range 0 <= theta <= pi/4 for three squeezing parameters (top row) and shows
the absolute differences on a log scale (bottom row). It is saved as
``check_gaussian_thewalrus.png`` in the current directory, or at the path
given as the first command-line argument.

``thewalrus`` is not a project dependency; run in a throwaway environment:

    uv run --with thewalrus --with numpy --with matplotlib python scripts/check_gaussian_thewalrus.py

Tested with thewalrus 0.22.0. Results are shown on the docs page
"Comparison and numerical checks".
"""
import sys

import matplotlib.pyplot as plt
import numpy as np
from thewalrus import threshold_detection_prob
from thewalrus.quantum import Qmat
from thewalrus.symplectic import interferometer, loss, two_mode_squeezing


def P00_closed(th, lam, eH, eV):
    detQ = (1 - lam**2*(1-eH)*(1-eV))**2 - lam**2*(eH-eV)**2*np.sin(4*th)**2
    return (1 - lam**2)/np.sqrt(detQ)

def Pcc_closed(th, lam, eH, eV):
    return (1 - P00_closed(th, lam, eH, 0) - P00_closed(th, lam, 0, eV)
            + P00_closed(th, lam, eH, eV))

def lossy_cov(th, lam, eH, eV, hbar=2):
    r = np.arctanh(lam)
    c, s = np.cos(2*th), np.sin(2*th)
    U = np.array([[c, s], [s, -c]])               # HWP at angle th
    S = interferometer(U) @ two_mode_squeezing(r, 0)
    cov = hbar/2 * S @ S.T                         # pure state, xxpp ordering
    mu = np.zeros(4)
    mu, cov = loss(mu, cov, eH, 0, hbar=hbar)      # efficiency = transmissivity
    mu, cov = loss(mu, cov, eV, 1, hbar=hbar)
    return mu, cov

rng = np.random.default_rng(8)
for _ in range(5):
    th, lam = rng.uniform(0, np.pi), rng.uniform(0, .95)
    eH, eV = rng.uniform(0, 1), rng.uniform(0, 1)
    mu, cov = lossy_cov(th, lam, eH, eV)
    p00_Q  = 1/np.sqrt(np.linalg.det(Qmat(cov)).real)
    p00_tw = threshold_detection_prob(mu, cov, [0, 0]).real
    pcc_tw = threshold_detection_prob(mu, cov, [1, 1]).real
    pcc_cf = Pcc_closed(th, lam, eH, eV)
    print(f"{P00_closed(th,lam,eH,eV):.12f} {p00_Q:.12f} {p00_tw:.12f} | "
          f"{pcc_cf:.12f} {pcc_tw:.12f}")

# Entry-by-entry comparison of Qmat with the explicit matrix (35a)
th, lam, eH, eV = 0.37, 0.6, 0.7, 0.45
nu, mu = lam**2/(1 - lam**2), lam/(1 - lam**2)
S4, C4 = np.sin(4*th), np.cos(4*th)
r = np.sqrt(eH*eV)
sigQ = np.array([
    [1 + nu*eH, 0,          mu*eH*S4,  -mu*r*C4],
    [0,         1 + nu*eV, -mu*r*C4,   -mu*eV*S4],
    [mu*eH*S4, -mu*r*C4,    1 + nu*eH,  0],
    [-mu*r*C4, -mu*eV*S4,   0,          1 + nu*eV]])
_, cov = lossy_cov(th, lam, eH, eV)
print(f"max |Qmat - (35a)| = {np.max(np.abs(Qmat(cov) - sigQ)):.1e}")

# Figure: closed forms (lines) vs thewalrus (markers) over the HWP range
eH, eV = 0.7, 0.45
lams = [0.3, 0.6, 0.9]
colors = ["#2a78d6", "#eb6834", "#1baf7a"]
th_line = np.linspace(0, np.pi/4, 400)
th_pts = np.linspace(0, np.pi/4, 25)
FLOOR = 1e-17   # exact agreement would be log(0); plot it at this floor

fig, axs = plt.subplots(2, 2, figsize=(11, 7), sharex=True,
                        gridspec_kw=dict(height_ratios=[2, 1]))
for lam, color in zip(lams, colors):
    p00_tw, pcc_tw = [], []
    for th in th_pts:
        mu, cov = lossy_cov(th, lam, eH, eV)
        p00_tw.append(threshold_detection_prob(mu, cov, [0, 0]).real)
        pcc_tw.append(threshold_detection_prob(mu, cov, [1, 1]).real)
    p00_tw, pcc_tw = np.array(p00_tw), np.array(pcc_tw)

    for col, closed, tw in [(0, P00_closed, p00_tw), (1, Pcc_closed, pcc_tw)]:
        axs[0, col].plot(th_line, closed(th_line, lam, eH, eV), color=color, lw=2,
                         label=rf"$\lambda={lam}$")
        axs[0, col].plot(th_pts, tw, "o", ms=6, mfc="white", mec=color, mew=1.5)
        diff = np.abs(closed(th_pts, lam, eH, eV) - tw)
        axs[1, col].semilogy(th_pts, np.maximum(diff, FLOOR), "o-", color=color,
                             ms=4, lw=1)

axs[0, 0].set_title(r"$P(0,0)$: closed form (46) vs. thewalrus")
axs[0, 1].set_title(r"$P_{\mathrm{cc}}$: closed form (50) vs. Torontonian")
axs[0, 0].set_ylabel("probability")
axs[1, 0].set_ylabel("|closed form − thewalrus|")
axs[0, 0].legend(frameon=False, title="lines: closed form\nmarkers: thewalrus")
for ax in axs[1]:
    ax.set_xlabel(r"HWP angle $\vartheta$")
    ax.set_ylim(FLOOR / 3, 1e-10)
    ax.set_xticks([0, np.pi/16, np.pi/8, 3*np.pi/16, np.pi/4])
    ax.set_xticklabels(["0", r"$\pi/16$", r"$\pi/8$", r"$3\pi/16$", r"$\pi/4$"])
for ax in axs.flat:
    ax.grid(color="#e1e4e5", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle(rf"$\eta_H={eH}$, $\eta_V={eV}$; differences of exactly 0 are drawn at {FLOOR:.0e}")
fig.tight_layout()

out = sys.argv[1] if len(sys.argv) > 1 else "check_gaussian_thewalrus.png"
fig.savefig(out, dpi=150)
print(f"Wrote {out}")
