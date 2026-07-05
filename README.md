# SPDC Coincidence Analysis

An **exact** analytical framework — with two independent numerical validators and a set of
live interactive dashboards — for coincidence-click probabilities in type-II SPDC experiments
with lossy bucket (click / no-click) detectors.

👉 **Live site / interactive dashboards:** https://nicosieber.github.io/spdc-coincidence-analysis/

---

## Overview

Photon-pair sources based on type-II spontaneous parametric down-conversion (SPDC) produce, in
the degenerate regime, a two-mode squeezed vacuum (TMSV) in the horizontal and vertical
polarization modes. When this state is rotated by a half-wave plate (HWP), split at a polarizing
beam splitter, and measured with non-photon-number-resolving **bucket** detectors, the accessible
quantity is a coincidence probability rather than the full photon-number distribution.

The usual approach truncates the TMSV to low photon number — valid only for weak pumping. This
project instead derives a **closed form that keeps all photon-number contributions exactly**, with
detector inefficiency folded in through a POVM description of the lossy detectors. The result is a
compact expression for the joint no-click probability, and from it the coincidence probability,
visibility, and phase-estimation (Fisher) information.

Two from-scratch Fock-space simulations — one in pure NumPy, one in QuTiP — reproduce the closed
form to the truncation floor, so the analytics are independently validated rather than merely
asserted.

---

## The physics package (`spdccc`)

```
src/spdccc/
├── closedform.py   analytic closed form — single source of truth (numpy; sympy only for Fisher)
├── fock_numpy.py   from-scratch NumPy Fock-space simulation (ground truth)
└── fock_qutip.py   QuTiP twin of the Fock simulation (requires qutip)
```

The closed form is defined **exactly once** in `closedform.py`; every generator script, dashboard,
and derived quantity imports from it. The Fock engines are imported lazily — `import spdccc` does
**not** require QuTiP; only `import spdccc.fock_qutip` does.

Central expression — joint no-click probability:

$$
P^{(\eta_H,\eta_V)}(0,0)=\frac{1-\lambda^{2}}
{\sqrt{(1-\lambda^{2}t_Ht_V)^{2}-\lambda^{2}(\eta_H-\eta_V)^{2}\sin^{2}(4\vartheta)}},
\qquad t_{H,V}=1-\eta_{H,V},
$$

with the coincidence probability following by inclusion–exclusion,
$P_\text{coinc}=1-P_H(\text{no click})-P_V(\text{no click})+P(0,0)$.

### Public API

| Function | Meaning |
|---|---|
| `p00(lam, etaH, etaV, theta)` | joint no-click probability $P(0,0)$ |
| `coincidence(lam, etaH, etaV, theta)` | coincidence-click probability |
| `click_probability(...)` | $1-P(0,0)$ |
| `visibility(lam, etaH, etaV)` | interference visibility of the coincidence curve |
| `visibility_ideal(lam)` | multi-pair visibility ceiling $\sqrt{1-\lambda^2}$ |
| `nbar_per_mode(lam)` | mean pairs per mode $\lambda^2/(1-\lambda^2)$ |
| `fisher_phi(lam, etaH, etaV, phi)` | classical Fisher information for phase $\phi=4\vartheta$ |
| `snl_phi(lam, etaH, etaV, phi)` | shot-noise limit |

Conventions: `lam` = squeezing parameter $\tanh r$ ($|\lambda|<1$); `etaH, etaV` = per-arm detection
efficiencies in $[0,1]$; `theta` = HWP angle, with the coincidence dip at $\vartheta=\pi/8$.

---

## Install & run

```bash
git clone https://github.com/nicosieber/spdc-coincidence-analysis.git
cd spdc-coincidence-analysis
pip install -e .            # core package (numpy, scipy, sympy)
pip install -e ".[docs]"    # + zensical, to build the docs site locally
```

Requires Python ≥ 3.14.

### Self-test (closed form vs. Fock engines)

```bash
python -m spdccc           # numpy engine only  (no qutip needed)
python -m spdccc --qutip   # also run the QuTiP twin
```

Example use:

```python
import numpy as np
from spdccc import coincidence, visibility, visibility_ideal

coincidence(0.6, 0.7, 0.7, np.pi/8)   # coincidence dip
visibility(0.5, 1.0, 1.0), visibility_ideal(0.5)   # agree to ~1e-14 at eta=1
```

---

## Numerical validation

Both engines build the HWP-rotated TMSV explicitly in a truncated two-mode Fock space
(`N = 60` per mode) and apply the bucket-detector POVM directly — no shared code with the closed
form. `exp(λ K†)` is applied as a power series **on the state**, never as a dense operator
exponential. At λ = 0.7, η = 0.85:

| Engine | max \|closed − numerical\| |
|---|---|
| NumPy Fock (`fock_numpy`) | ~1 × 10⁻¹⁰ |
| QuTiP Fock (`fock_qutip`) | ~6 × 10⁻¹¹ |

Both residuals are set by Fock truncation, not by the analytics — confirming the closed form is
exact.

---

## Interactive dashboards

The live site hosts browser dashboards that recompute on every slider drag, powered by a shared
JavaScript physics module (`docs/js/spdc_physics.js`) that mirrors the Python package:

- **Coincidence probability** — NumPy and QuTiP twin pages, each overlaying the closed form against
  a live Fock-engine recomputation with a residual panel that exposes the truncation error
- **Visibility** vs. detector efficiency, against the $\sqrt{1-\lambda^2}$ ceiling
- **Fisher information** for phase estimation, against the shot-noise limit

---

## Deployment

The documentation site is built with [Zensical](https://github.com/zensical/zensical) and
deployed automatically to GitHub Pages via GitHub Actions (`.github/workflows/docs.yml`) on every
push to `main`.

---

## Author

**Nico Sieber**
🔗 [LinkedIn](https://www.linkedin.com/in/nico-sieber-0a7204156/)

Feedback, issues, and pull requests welcome.