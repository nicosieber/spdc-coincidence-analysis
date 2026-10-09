# Comparison and numerical checks

<span id="comparison"></span>

## Comparison with the main derivation

| | [Main derivation](../theory/cc_derivation.md) | Gaussian formalism |
|---|---|---|
| Works with | the state vector $\lvert\Psi\rangle$ | the numbers $\langle\Psi\rvert\hat a\hat a\lvert\Psi\rangle$, $\langle\Psi\rvert\hat a^{\dagger}\hat a\lvert\Psi\rangle$ collected in $\sigma_Q$ |
| Efficiency | $t^{\hat n}$ moved through the exponential: $\mathbf{\hat a^{\dagger}}\to D\,\mathbf{\hat a^{\dagger}}$ | beam splitter on the covariance matrix, factors $\sqrt{\eta}$ |
| Object computed | overlap $\langle 0\rvert e^{\frac\lambda2\mathbf{\hat a}^TM\mathbf{\hat a}}e^{\frac\lambda2(\mathbf{\hat a^{\dagger}})^TDMD\mathbf{\hat a^{\dagger}}}\lvert 0\rangle$ | covariance matrix of $\lvert\Psi\rangle$, then vacuum probability |
| Where coherent states enter | resolution of $\mathbb{1}$, complex Gaussian integral | $Q$ function, height of a real bell curve |
| Matrix | $\mathbb{1}-\lambda^2MDMD$ ($2\times2$) | $\sigma_Q'$ ($4\times4$, symmetric, positive definite) |
| Hard part | the complex Gaussian integral | the vacuum formula [(26)](vacuum_probability.md#eq26), imported |
| Sign of the square root | determined separately via $P\ge0$ ([Lean](../theory/cc_derivation.md#P00_lean)) | automatic |

Both routes meet at

<span id="eq51"></span>

$$
\det\!\left(\mathbb{1}-\lambda^2MDMD\right)=(1-\lambda^2)^2\,\det\sigma_Q' .
\tag{51}
$$

The Gaussian formalism also carries over to the setting of [Generalizing the optical element](../theory/generalization.md). For any passive element in front of the PBS, [(9)](covariance_matrix.md#eq9) holds with that element's $M$, and the same steps apply. For a complex $M$ the lower-left block becomes $B^{*}$. Effects that are awkward in the state-vector picture are simply extra terms in the covariance matrix: thermal background adds to $N$, and a mixed or multimode source changes $N$ and $\mathcal{M}$.

<span id="numerical-check"></span>

## Numerical check

### With `thewalrus`

The script uses the library `thewalrus` <a href="#ref-gupt2019">[4]</a> and compares three things:

1. the closed form [(46)](determinant.md#eq46),
2. $1/\sqrt{\det\sigma_Q'}$ computed by `thewalrus`,
3. the library's threshold-detection probability.

It also compares $P_{\mathrm{cc}}$ from [(50)](coincidence.md#eq50) with the library's Torontonian <a href="#ref-quesada2018">[2]</a>.

`thewalrus` builds states from "symplectic" matrices and stores them as $x,p$ covariance matrices. You can treat these lines as a black box that produces $\lvert\Psi\rangle$ with losses: `two_mode_squeezing` is the SPDC source, `interferometer(U)` the HWP and `loss` the detector efficiency. `Qmat` turns the result into the $\sigma_Q'$ of [(35a)](detector_efficiency.md#eq35a).

`thewalrus` is not a project dependency, so run it in a throwaway environment, e.g. `uv run --with thewalrus --with numpy python script.py`. This was tested with `thewalrus` 0.22.0.

```python
import numpy as np
from thewalrus.quantum import Qmat
from thewalrus.symplectic import two_mode_squeezing, interferometer, loss
from thewalrus import threshold_detection_prob

def P00_closed(th, lam, eH, eV):
    detQ = (1 - lam**2*(1-eH)*(1-eV))**2 - lam**2*(eH-eV)**2*np.sin(4*th)**2
    return (1 - lam**2)/np.sqrt(detQ)

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
    pcc_cf = (1 - P00_closed(th, lam, eH, 0) - P00_closed(th, lam, 0, eV)
              + P00_closed(th, lam, eH, eV))
    print(f"{P00_closed(th,lam,eH,eV):.12f} {p00_Q:.12f} {p00_tw:.12f} | "
          f"{pcc_cf:.12f} {pcc_tw:.12f}")
```

Output:

```text
0.371058949784 0.371058949784 0.371058949784 | 0.141826213062 0.141826213062
0.398349140074 0.398349140074 0.398349140074 | 0.010433305259 0.010433305259
0.890949357824 0.890949357824 0.890949357824 | 0.017971948976 0.017971948976
0.855038232771 0.855038232771 0.855038232771 | 0.061344652949 0.061344652949
0.434027166501 0.434027166501 0.434027166501 | 0.446652713512 0.446652713512
```

`Qmat(cov)` from this script was also compared entry by entry with the explicit matrix [(35a)](detector_efficiency.md#eq35a) at $\vartheta=0.37$, $\lambda=0.6$, $\eta_H=0.7$, $\eta_V=0.45$. The largest difference is $2\times10^{-16}$, i.e. the matrices agree, including all signs.

### Symbolic check

This snippet confirms three things exactly with `sympy` <a href="#ref-meurer2017">[11]</a>:

- the determinant identity [(45)](determinant.md#eq45), using the explicit matrix [(35a)](detector_efficiency.md#eq35a),
- $M^2=\mathbb{1}$,
- that $\mathcal{M}=\mu M$ and $N=\nu\mathbb{1}$ solve [(12)](covariance_matrix.md#eq12).

```python
import sympy as sp
l, eH, eV, th = sp.symbols('lambda eta_H eta_V theta', real=True)
S4, C4 = sp.sin(4*th), sp.cos(4*th)
M  = sp.Matrix([[S4, -C4], [-C4, -S4]])
nu, mu = l**2/(1-l**2), l/(1-l**2)
r = sp.sqrt(eH*eV)
sigQ = sp.Matrix([
    [1+nu*eH, 0,        mu*eH*S4, -mu*r*C4],
    [0,       1+nu*eV, -mu*r*C4,  -mu*eV*S4],
    [mu*eH*S4, -mu*r*C4, 1+nu*eH, 0],
    [-mu*r*C4, -mu*eV*S4, 0,      1+nu*eV]])
detQ = (1 - l**2*(1-eH)*(1-eV))**2 - l**2*(eH-eV)**2*S4**2
print(sp.simplify(sp.trigsimp(sigQ.det() - detQ/(1-l**2)**2)))   # 0
print(sp.simplify(M*M - sp.eye(2)))                                # zero matrix
Mcal, N = mu*M, nu*sp.eye(2)
print(sp.simplify(N - l*Mcal.conjugate()*M),                       # zero matrix
      sp.simplify(Mcal - (l*M + l*N.T*M)))                         # zero matrix
```

## References

<p id="ref-quesada2018">
[2] N. Quesada, J. M. Arrazola, N. Killoran,
<em>Gaussian boson sampling using threshold detectors</em>, Phys. Rev. A <strong>98</strong>, 062322 (2018). Available: https://arxiv.org/abs/1807.01639
</p>

<p id="ref-gupt2019">
[4] B. Gupt, J. Izaac, N. Quesada,
<em>The Walrus: a library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling</em>, J. Open Source Softw. <strong>4</strong>(44), 1705 (2019). Documentation: https://the-walrus.readthedocs.io
</p>

<p id="ref-meurer2017">
[11] A. Meurer et al.,
<em>SymPy: symbolic computing in Python</em>, PeerJ Comput. Sci. <strong>3</strong>, e103 (2017). Available: https://doi.org/10.7717/peerj-cs.103
</p>
