"""
spdccc.fock_qutip
===============
QuTiP twin of :mod:`spdc.fock_numpy`.

Same physics, expressed in QuTiP's operator algebra. Validated to the
Fock-truncation floor against :mod:`spdc.closedform`.

State (type-II SPDC TMSV rotated by a HWP at angle theta):

    |Psi> = sqrt(1-lam^2) exp(lam K^dag) |0,0>
    K^dag = (c a_H^dag + s a_V^dag)(s a_H^dag - c a_V^dag),  c=cos2t, s=sin2t

Operator mapping (H = first tensor factor, V = second):
    a_H = tensor(destroy(N), qeye(N)),  a_V = tensor(qeye(N), destroy(N))

Bucket (click / no-click) detector, efficiency eta, no dark counts:
    no-click POVM on a mode = (1-eta)^n  (diagonal in Fock basis)
    => P(no click both) = <Psi| t_H^{n_H} t_V^{n_V} |Psi>,  t = 1 - eta
"""
import numpy as np
from qutip import destroy, qeye, num, tensor, basis

from .closedform import p00 as closed_P00, coincidence as closed_Pcoinc

__all__ = ["Kdag", "state_vector", "brute_P00", "brute_Pcoinc",
           "closed_P00", "closed_Pcoinc"]


def Kdag(N, theta):
    """Pair-creation generator K^dag as a (sparse) two-mode Qobj."""
    aHd = tensor(destroy(N), qeye(N)).dag()
    aVd = tensor(qeye(N), destroy(N)).dag()
    c, s = np.cos(2 * theta), np.sin(2 * theta)
    return (c * aHd + s * aVd) * (s * aHd - c * aVd)


def state_vector(lam, theta, N=60, nmax=45):
    """|Psi> = sqrt(1-lam^2) exp(lam K^dag)|0,0>.

    Power series applied to the STATE (K^dag stays sparse -> fast, low
    memory). Do NOT use ``.expm()``: it densifies the N^2 x N^2 operator.
    """
    Kd = Kdag(N, theta)
    vac = tensor(basis(N, 0), basis(N, 0))
    term = vac.copy()
    acc = vac.copy()
    for n in range(1, nmax + 1):
        term = (Kd * term) * (lam / n)
        acc = acc + term
        if term.norm() < 1e-16:
            break
    return acc.unit()          # normalisation = multiply by sqrt(1-lam^2)


def _noclick_weights(etaH, etaV, N):
    """Diagonal loss weight t_H^{n_H} t_V^{n_V} as a flat array over the basis."""
    nH = np.real(np.diag(tensor(num(N), qeye(N)).full()))
    nV = np.real(np.diag(tensor(qeye(N), num(N)).full()))
    return (1 - etaH) ** nH * (1 - etaV) ** nV


def brute_P00(lam, etaH, etaV, theta, N=60, nmax=45):
    psi = state_vector(lam, theta, N, nmax)
    p = np.abs(psi.full().ravel()) ** 2
    return float(np.sum(p * _noclick_weights(etaH, etaV, N)))


def brute_Pcoinc(lam, etaH, etaV, theta, N=60, nmax=45):
    P00 = brute_P00(lam, etaH, etaV, theta, N, nmax)
    PH0 = brute_P00(lam, etaH, 0.0, theta, N, nmax)
    PV0 = brute_P00(lam, 0.0, etaV, theta, N, nmax)
    return 1.0 - PH0 - PV0 + P00
