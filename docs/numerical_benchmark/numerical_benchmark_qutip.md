# Numerical benchmark — QuTiP

The [NumPy page](numerical_benchmark_numpy.md) validated the closed form by building the
Fock-space simulation from scratch with array shifts. This page does the **same physics
with [QuTiP](https://qutip.org/)**, a purpose-built quantum-optics toolkit. The value is
twofold: it is a second, independent implementation (different library, different operator
algebra, same answer), and it is the natural starting point for extensions the closed form
cannot express — dark counts, number-resolving detectors, dephasing and mixed states.

The whole physics reduces to a handful of operator lines.

!!! note "Same benchmark, different engine"
    - **Closed form** — the analytic result derived on the site.
    - **QuTiP** — construct $|\Psi\rangle=\sqrt{1-\lambda^2}\,e^{\lambda K^\dagger}|0,0\rangle$
      with QuTiP operators and evaluate the detector POVM.

    Agreement to the truncation floor confirms both the closed form and the NumPy engine.

## 1 — Operators and the generator

QuTiP builds two-mode operators by tensoring single-mode ones. The horizontal mode is the
first tensor factor, the vertical the second:

$$a_H=\texttt{tensor(destroy(N), qeye(N))},\qquad
a_V=\texttt{tensor(qeye(N), destroy(N))}.$$

`Kdag` assembles the HWP-rotated pair-creation generator
$K^\dagger=(c\,a_H^\dagger+s\,a_V^\dagger)(s\,a_H^\dagger-c\,a_V^\dagger)$ with
$c=\cos 2\vartheta,\ s=\sin 2\vartheta$, and returns it as a **sparse** `Qobj`.

```python
import numpy as np
from qutip import destroy, qeye, num, tensor, basis

def closed_P00(lam, etaH, etaV, theta):
    tH, tV = 1 - etaH, 1 - etaV
    return (1 - lam**2) / np.sqrt(
        (1 - lam**2*tH*tV)**2 - lam**2*(etaH - etaV)**2*np.sin(4*theta)**2)

def closed_Pcoinc(lam, etaH, etaV, theta):
    return (1 - closed_P00(lam, etaH, 0.0, theta)
              - closed_P00(lam, 0.0, etaV, theta)
              + closed_P00(lam, etaH, etaV, theta))

def Kdag(N, theta):
    """Pair-creation generator K† as a (sparse) two-mode Qobj."""
    aHd = tensor(destroy(N), qeye(N)).dag()   # a_H†
    aVd = tensor(qeye(N), destroy(N)).dag()   # a_V†
    c, s = np.cos(2*theta), np.sin(2*theta)
    return (c*aHd + s*aVd) * (s*aHd - c*aVd)
```

## 2 — The state (why not `.expm()`)

The state is $|\Psi\rangle=\sqrt{1-\lambda^2}\,e^{\lambda K^\dagger}|0,0\rangle$. The obvious
call is `(lam * Kdag(N, theta)).expm() * vac` — and it is a trap. QuTiP keeps $K^\dagger$
**sparse**, but `.expm()` **densifies** the $N^2\times N^2$ operator: at $N=60$ that is a
$3600\times3600$ matrix, costing about $10^3\times$ more time and memory for an identical
result.

Instead, sum the exponential **power series applied to the state vector**,
$|\Psi\rangle=\sum_n\frac{\lambda^n}{n!}(K^\dagger)^n|0,0\rangle$. Each term is the previous
one hit once more with the sparse $K^\dagger$, so the operator never densifies. `.unit()`
normalises, which is exactly the $\sqrt{1-\lambda^2}$ prefactor.

```python
def state_vector(lam, theta, N=60, nmax=45):
    """|Psi> = sqrt(1-lam^2) exp(lam K†)|0,0>, summed as a series on the STATE.
    K† stays sparse -> fast and low-memory. Do NOT use .expm() (it densifies)."""
    Kd = Kdag(N, theta)
    vac = tensor(basis(N, 0), basis(N, 0))
    term = vac.copy()
    acc  = vac.copy()
    for n in range(1, nmax + 1):
        term = (Kd * term) * (lam / n)
        acc  = acc + term
        if term.norm() < 1e-16:
            break
    return acc.unit()
```

## 3 — Bucket detectors and probabilities

A bucket detector with efficiency $\eta$ stays dark on $n$ photons with probability
$(1-\eta)^n$. In the Fock basis the no-click POVM element is diagonal, so the joint
both-dark probability is the photon-number distribution contracted against
$t_H^{\,n_H}t_V^{\,n_V}$. We read the number operators straight off QuTiP's `num(N)` and
combine the two arms by the **same inclusion–exclusion** as the closed form.

```python
def _noclick_weights(etaH, etaV, N):
    """Diagonal loss weight t_H^{n_H} t_V^{n_V} over the two-mode basis."""
    nH = np.diag(tensor(num(N), qeye(N)).full()).real
    nV = np.diag(tensor(qeye(N), num(N)).full()).real
    return (1 - etaH)**nH * (1 - etaV)**nV

def brute_P00(lam, etaH, etaV, theta, N=60, nmax=45):
    psi = state_vector(lam, theta, N, nmax)
    p = np.abs(psi.full().ravel())**2
    return float(np.sum(p * _noclick_weights(etaH, etaV, N)))

def brute_Pcoinc(lam, etaH, etaV, theta, N=60, nmax=45):
    P00 = brute_P00(lam, etaH, etaV, theta, N, nmax)
    PH0 = brute_P00(lam, etaH, 0.0, theta, N, nmax)
    PV0 = brute_P00(lam, 0.0, etaV, theta, N, nmax)
    return 1 - PH0 - PV0 + P00
```

## 4 — Result

Evaluated at the same demanding point as the NumPy page ($\lambda=0.7$, so
$\bar n\approx0.96$ pairs per mode; $\eta_H=\eta_V=0.85$; $N=60$):

![QuTiP engine vs closed form](img/qutip_validation.png)

The QuTiP markers land on the closed-form curve, with residuals at the **$10^{-11}$
level** — set by Fock truncation, not by the choice of library. All three engines
(closed form, NumPy, QuTiP) agree to machine-limited precision.

## 5 — Why QuTiP, if the closed form is exact

For *this* source the closed form already gives the exact answer, so QuTiP is a cross-check
rather than a necessity. Its value is in what comes next: building the state and detector
model explicitly is what makes extensions tractable that the closed form cannot express —

- **dark counts** — replace the no-click element $(1-\eta)^n$ with $(1-p_\text{dark})(1-\eta)^n$;
- **number-resolving detectors** — swap the click/no-click POVM for a photon-number POVM;
- **dephasing / mixed states** — evolve a density matrix with `mesolve` instead of a pure ket;
- **spectral multimode** — add mode pairs to the tensor product.

Each drops out of the same $K^\dagger$/POVM scaffolding once $|\Psi\rangle$ is in hand.

!!! tip "Reproduce it"
    The functions above are the complete engine. The same code, with a self-test and the
    `visibility` helpers, lives in `spdc_coincidence_qutip.py` in the repository.
