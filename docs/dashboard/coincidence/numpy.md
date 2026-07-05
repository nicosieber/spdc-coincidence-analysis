# Coincidence dashboard (NumPy)

<iframe
  src="../../assets/plots/coincidence_plot_numpy.html"
  width="100%"
  height="660"
  style="border:0;"
  loading="lazy">
</iframe>

The dashboard above plots the coincidence probability normalized by its maximum over
\(0\le\vartheta\le\pi/4\), so the peak of the displayed curve is always one. The lime line is
the closed form, whereas the amber open circles are from a truncated-Fock simulation at fixed
Hilbert dimension \(N=60\). The lower panel shows the residual
\(\lvert\text{numeric}-\text{closed}\rvert\) at each marker (log scale), and the readout
reports its maximum over the scan.

Vary \(\lambda\) and watch the markers: at low squeezing they sit exactly on the analytic
curve, but as \(\lambda\) climbs past \(\approx 0.85\) the mean photon number
\(\bar n=\lambda^2/(1-\lambda^2)\) grows until the true state carries appreciable weight above
\(N=60\) photons per mode. That weight is simply truncated away, so the numerical markers lift
off the closed form — visibly by \(\lambda\approx 0.9\), blatantly by \(\lambda\approx 0.95\).
The binding knob is \(N\), the Hilbert-space dimension (capped here at 60 for compute), not the
number of power-series terms, which converges quickly. The closed form has no Hilbert space to
truncate, so it stays exact everywhere — that is precisely where it earns its keep.

The plotted quantity is the closed-form [coincidence probability of the
half-wave-plate-rotated TMSV](../../theory/cc_derivation.md),

\begin{equation}
\label{eq:numpy_dashboard_pcc}
P_{\mathrm{coinc}}
=
1
-
P_H^{(\eta_H)}(0)
-
P_V^{(\eta_V)}(0)
+
P^{(\eta_H,\eta_V)}(0,0),
\end{equation}

with the joint no-click probability

\begin{equation}
\label{eq:numpy_dashboard_p00}
P^{(\eta_H,\eta_V)}(0,0)
=
\dfrac{1-\lambda^2}{
\sqrt{
\left(1-\lambda^2(1-\eta_H)(1-\eta_V)\right)^2
-
\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)
}
}.
\end{equation}

A closed form is only as trustworthy as the independent check behind it. The rest of this
page builds that check **from scratch in NumPy**: it constructs the quantum state in a
truncated Fock space, applies the lossy-detector model directly, and compares the result to
the analytic expression at every wave-plate angle. Nothing here depends on a specialised
quantum library — only `numpy`. The [companion QuTiP dashboard](qutip.md) does the same
thing with a purpose-built quantum-optics toolkit; the two agree, which is the point.

!!! note "What is being validated"
    Two independent routes to the same number:

    - **Closed form** — the analytic result derived on the site,
      $P^{(\eta_H,\eta_V)}(0,0)=\dfrac{1-\lambda^2}{\sqrt{(1-\lambda^2 t_H t_V)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2 4\vartheta}}$,
      with $t_{H,V}=1-\eta_{H,V}$, combined by inclusion–exclusion.
    - **Fock-space simulation** — build
      $|\Psi\rangle=\sqrt{1-\lambda^2}\,e^{\lambda K^\dagger}|0,0\rangle$ explicitly on a
      photon-number grid and evaluate the detector POVM numerically.

    If the two agree to the Fock-truncation floor across all $\vartheta$, the closed form
    is confirmed.

## The closed form

`closed_P00` returns the probability that **neither** detector clicks. The half-wave plate
enters only through $\sin^2 4\vartheta$, so the curve is $\pi/2$-periodic and symmetric
about $\vartheta=\pi/4$. `closed_Pcoinc` turns that no-click quantity into a
**coincidence** probability by inclusion–exclusion, where each single-arm no-click probability 
is $P(0,0)$ evaluated with the *opposite* detector made transparent ($\eta=0$, so it can never click).

```python
import numpy as np

def closed_P00(lam, etaH, etaV, theta):
    """Joint no-click probability P^{(eta_H,eta_V)}(0,0)."""
    tH, tV = 1.0 - etaH, 1.0 - etaV
    num = 1.0 - lam**2
    den = np.sqrt((1.0 - lam**2 * tH * tV)**2
                  - lam**2 * (etaH - etaV)**2 * np.sin(4.0 * theta)**2)
    return num / den

def closed_Pcoinc(lam, etaH, etaV, theta):
    """P_coinc = 1 - P_H(no click) - P_V(no click) + P(0,0)."""
    P00 = closed_P00(lam, etaH, etaV, theta)
    PH0 = closed_P00(lam, etaH, 0.0, theta)   # only H can click
    PV0 = closed_P00(lam, 0.0, etaV, theta)   # only V can click
    return 1.0 - PH0 - PV0 + P00
```

## The Fock-space simulation

The state is $|\Psi\rangle=\sqrt{1-\lambda^2}\,e^{\lambda K^\dagger}|0,0\rangle$ with the
HWP-rotated pair-creation generator

$$K^\dagger=(\cos 2\vartheta\,a_H^\dagger+\sin 2\vartheta\,a_V^\dagger)
(\sin 2\vartheta\,a_H^\dagger-\cos 2\vartheta\,a_V^\dagger).$$

We represent the two-mode state as an $N\times N$ NumPy array indexed by photon numbers
$(n_H,n_V)$. Two ideas keep it exact and fast:

1. **Creation operators act by array shifting.** $a^\dagger$ maps
   $|n\rangle\mapsto\sqrt{n+1}\,|n+1\rangle$, i.e. a shift-by-one along the relevant axis
   with a $\sqrt{n}$ weight — no dense matrix is ever formed.
2. **The exponential is summed as a power series applied to the state**,
   $|\Psi\rangle=\sum_n\frac{\lambda^n}{n!}(K^\dagger)^n|0,0\rangle$. Each term is the
   previous one hit once more with $K^\dagger$, so the whole state costs a handful of
   array shifts per order.

A bucket detector that sees $n$ photons stays dark with probability $(1-\eta)^n$, so the
both-dark probability is the photon-number distribution $|\langle n_H,n_V|\Psi\rangle|^2$
contracted against the diagonal weight $t_H^{\,n_H}t_V^{\,n_V}$.

```python
def brute_P00(lam, etaH, etaV, theta, N=60, nmax=45):
    """
    P(0,0) by explicit construction of the HWP-rotated TMSV in a
    truncated two-mode Fock space of dimension N per mode.

        |Psi> = sqrt(1-lam^2) * exp(lam K^dag) |0,0>,
        K^dag = (cos2t a_H^dag + sin2t a_V^dag)(sin2t a_H^dag - cos2t a_V^dag).

    exp(lam K^dag) is applied as a power series *on the state* (never as a
    dense operator exponential). Returns (P00, norm).
    """
    c, s = np.cos(2 * theta), np.sin(2 * theta)
    Lam = np.sqrt(1.0 - lam ** 2)

    adag_1 = np.diag(np.sqrt(np.arange(1, N)), k=-1)   # √(n+1) sub-diagonal, built once

    def adag(psi, mode):
        if mode == 'H':
            return adag_1 @ psi        # left-multiply -> acts on the ROW index n_H
        else:
            return psi @ adag_1.T      # right-multiply by transpose -> acts on the COLUMN index n_V

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
```

