"""
spdccc.fock_numpy
===============
From-scratch NumPy Fock-space simulation of the SPDC coincidence experiment.

An independent numerical route to the joint no-click / coincidence
probability: build the HWP-rotated TMSV explicitly in a truncated two-mode
Fock space and apply the lossy bucket-detector POVM directly. Agreement with
:mod:`spdccc.closedform` to the Fock-truncation floor validates the closed form.

No external quantum library is used here -- only numpy. The QuTiP twin lives
in :mod:`spdccc.fock_qutip`.
"""
import numpy as np

from .closedform import p00 as closed_P00, coincidence as closed_Pcoinc

__all__ = ["brute_P00", "brute_Pcoinc", "closed_P00", "closed_Pcoinc"]


def brute_P00(lam, etaH, etaV, theta, N=60, nmax=45):
    """P(0,0) by explicit construction of the HWP-rotated TMSV in a
    truncated two-mode Fock space of dimension ``N`` per mode.

        |Psi> = sqrt(1-lam^2) * exp(lam K^dag) |0,0>,
        K^dag = (cos2t a_H^dag + sin2t a_V^dag)(sin2t a_H^dag - cos2t a_V^dag).

    exp(lam K^dag) is applied as a power series *on the state* (never as a
    dense operator exponential). Returns ``(P00, norm)``.
    """
    c, s = np.cos(2 * theta), np.sin(2 * theta)
    Lam = np.sqrt(1.0 - lam ** 2)

    adag_1 = np.diag(np.sqrt(np.arange(1, N)), k=-1)   # √(n+1) sub-diagonal, built once

    def adag(psi, mode):
        if mode == 'H':
            return adag_1 @ psi        # left-multiply → acts on the ROW index n_H
        else:
            return psi @ adag_1.T      # right-multiply by transpose → acts on the COLUMN index n_V

    def Kdag(psi):
        t1 = s * adag(psi, "H") - c * adag(psi, "V")
        return c * adag(t1, "H") + s * adag(t1, "V")

    psi = np.zeros((N, N)); psi[0, 0] = 1.0
    acc = np.zeros((N, N)); term = psi.copy()
    for n in range(nmax):                 # exp(lam K^dag) power series on state
        acc += term
        term = Kdag(term) * (lam / (n + 1))
    psi = Lam * acc

    i = np.arange(N)[:, None]; j = np.arange(N)[None, :]
    w = (1 - etaH) ** i * (1 - etaV) ** j   # <n_H,n_V| t_H^{n_H} t_V^{n_V} |.>
    p2 = np.abs(psi) ** 2
    return float(np.sum(p2 * w)), float(np.sum(p2))


def brute_Pcoinc(lam, etaH, etaV, theta, N=60, nmax=45):
    """Coincidence probability by inclusion-exclusion from three Fock-space
    no-click evaluations (both arms, then each arm alone)."""
    P00, _ = brute_P00(lam, etaH, etaV, theta, N, nmax)
    PH0, _ = brute_P00(lam, etaH, 0.0, theta, N, nmax)
    PV0, _ = brute_P00(lam, 0.0, etaV, theta, N, nmax)
    return 1.0 - PH0 - PV0 + P00
