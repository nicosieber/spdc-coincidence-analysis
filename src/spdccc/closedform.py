"""
spdccc.closedform
===============
Single source of truth for the *analytic* physics of the SPDC
coincidence-analysis project.

System: a type-II SPDC two-mode squeezed vacuum (TMSV) in H/V modes,
rotated by a half-wave plate (HWP) at angle ``theta``, split at a PBS and
measured by two lossy bucket (click / no-click) detectors.

Conventions
-----------
lam        squeezing parameter, |lam| < 1  (tanh r)
etaH, etaV total detection efficiency of the H / V arm, in [0, 1]
theta      HWP angle; the coincidence dip sits at theta = pi/8
phi        optical phase phi = 4*theta  (used for Fisher information)

Every generator script and every derived quantity in this project imports
from here, so the closed form is defined exactly once.
"""
import numpy as np

__all__ = [
    "p00", "marginal_noclick", "coincidence", "click_probability",
    "visibility", "visibility_ideal", "nbar_per_mode",
    "fisher_phi", "snl_phi",
    # backward-compatible aliases used by the notebook pages / engines
    "closed_P00", "closed_Pcoinc",
]


# --------------------------------------------------------------------------
# Joint no-click probability  P^{(eta_H,eta_V)}(0,0)
# --------------------------------------------------------------------------
def p00(lam, etaH, etaV, theta):
    """Joint no-click probability P(0,0): neither detector fires.

        P(0,0) = (1 - lam^2) /
                 sqrt[ (1 - lam^2 t_H t_V)^2 - lam^2 (eta_H-eta_V)^2 sin^2(4 theta) ]

    with t_{H,V} = 1 - eta_{H,V}.
    """
    tH, tV = 1.0 - etaH, 1.0 - etaV
    num = 1.0 - lam ** 2
    den = np.sqrt((1.0 - lam ** 2 * tH * tV) ** 2
                  - lam ** 2 * (etaH - etaV) ** 2 * np.sin(4.0 * theta) ** 2)
    return num / den


def marginal_noclick(lam, eta, theta, arm):
    """Single-arm no-click probability.

    A single-arm no-click term is P(0,0) with the *opposite* detector made
    transparent (eta = 0), so that detector can never fire.

    arm='H' -> only H can click  (etaV = 0);  arm='V' -> only V can click.
    """
    if arm == "H":
        return p00(lam, eta, 0.0, theta)
    elif arm == "V":
        return p00(lam, 0.0, eta, theta)
    raise ValueError("arm must be 'H' or 'V'")


def coincidence(lam, etaH, etaV, theta):
    """Coincidence-click probability via inclusion-exclusion:

        P_coinc = 1 - P_H(no click) - P_V(no click) + P(0,0)

    where each single-arm no-click term sets the OPPOSITE detector
    transparent (eta = 0).
    """
    P00 = p00(lam, etaH, etaV, theta)
    PH0 = p00(lam, etaH, 0.0, theta)   # only H can click
    PV0 = p00(lam, 0.0, etaV, theta)   # only V can click
    return 1.0 - PH0 - PV0 + P00


def click_probability(lam, etaH, etaV, theta):
    """Probability that at least one detector fires, P_click = 1 - P(0,0)."""
    return 1.0 - p00(lam, etaH, etaV, theta)


# --------------------------------------------------------------------------
# Derived observables
# --------------------------------------------------------------------------
def visibility(lam, etaH, etaV, ntheta=4001):
    """Interference visibility V = (Cmax - Cmin)/(Cmax + Cmin) of the
    coincidence curve over theta in [0, pi/4]."""
    th = np.linspace(0.0, np.pi / 4, ntheta)
    C = coincidence(lam, etaH, etaV, th)
    Cmax, Cmin = float(C.max()), float(C.min())
    return (Cmax - Cmin) / (Cmax + Cmin)


def visibility_ideal(lam):
    """Multi-pair visibility ceiling for perfect detectors:
    V_ideal(lam) = sqrt(1 - lam^2)."""
    return np.sqrt(1.0 - lam ** 2)


def nbar_per_mode(lam):
    """Mean photon pairs per mode, <n> = lam^2 / (1 - lam^2)."""
    return lam ** 2 / (1.0 - lam ** 2)


# --------------------------------------------------------------------------
# Fisher information for estimating the optical phase phi = 4*theta
# --------------------------------------------------------------------------
# Exact analytic derivatives of the click-conditioned outcome probabilities,
# obtained once via sympy at import time and lambdified to numpy.
def _build_fisher():
    import sympy as sp
    lam_s, etaH_s, etaV_s, th_s = sp.symbols(
        "lambda eta_H eta_V theta", positive=True)

    def _P00(eH, eV):
        num = 1 - lam_s ** 2
        t1 = 1 - lam_s ** 2 * (1 - eH) * (1 - eV)
        den = sp.sqrt(t1 ** 2 - lam_s ** 2 * (eH - eV) ** 2 * sp.sin(4 * th_s) ** 2)
        return num / den

    P00 = _P00(etaH_s, etaV_s)
    PH0 = _P00(etaH_s, 0)
    PV0 = _P00(0, etaV_s)
    Pclick = 1 - P00

    p11 = (1 - PH0 - PV0 + P00) / Pclick   # coincidence
    p20 = (PV0 - P00) / Pclick             # H-only
    p02 = (PH0 - P00) / Pclick             # V-only

    syms = (lam_s, etaH_s, etaV_s, th_s)
    fp = [sp.lambdify(syms, x, "numpy") for x in (p11, p20, p02)]
    fdp = [sp.lambdify(syms, sp.diff(x, th_s), "numpy") for x in (p11, p20, p02)]
    return fp, fdp


_FISHER_CACHE = None


def _fisher_funcs():
    global _FISHER_CACHE
    if _FISHER_CACHE is None:
        _FISHER_CACHE = _build_fisher()
    return _FISHER_CACHE


def fisher_phi(lam, etaH, etaV, phi):
    """Classical Fisher information F(phi) for the optical phase phi = 4*theta
    implemented by a HWP at angle theta.

        F_phi = F_theta / 16       (chain rule: d theta / d phi = 1/4)
        F_theta = sum_{i in 11,20,02} (d p_i/d theta)^2 / p_i

    p_i are the click-conditioned outcome probabilities (recorded trials
    only). Requires sympy (analytic derivatives, built once and cached).
    """
    fp, fdp = _fisher_funcs()
    phi = np.asarray(phi, dtype=float)
    th = phi / 4.0
    eps = 1e-15
    F = np.zeros_like(th)
    for f, df in zip(fp, fdp):
        p = f(lam, etaH, etaV, th)
        dp = df(lam, etaH, etaV, th)
        F = F + np.where(p > eps, dp ** 2 / p, 0.0)
    return F / 16.0


def snl_phi(lam, etaH, etaV, phi):
    """Shot-noise limit F_SNL(phi) = mean photons per recorded trial.

        F_SNL = n_bar / P_click,  n_bar = 2 lam^2 / (1 - lam^2)

    Flat in phi for symmetric losses; weakly phase-dependent otherwise
    through the (eta_H - eta_V)^2 sin^2(4 theta) term in P(0,0).
    """
    phi = np.asarray(phi, dtype=float)
    th = phi / 4.0
    n_mean = 2.0 * lam ** 2 / (1.0 - lam ** 2)
    return n_mean / click_probability(lam, etaH, etaV, th)


# --------------------------------------------------------------------------
# Backward-compatible aliases (names used by the notebook pages & engines)
# --------------------------------------------------------------------------
closed_P00 = p00
closed_Pcoinc = coincidence
