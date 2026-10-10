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
| Hard part | the complex Gaussian integral | the vacuum formula [(12)](../gaussian_formalism/covariance_matrix.md#eq12), imported |
| Sign of the square root | determined separately via $P\ge0$ ([Lean](../theory/cc_derivation.md#P00_lean)) | automatic |

Both routes meet at

<span id="eq51"></span>

$$
\det\!\left(\mathbb{1}-\lambda^2MDMD\right)=(1-\lambda^2)^2\,\det\sigma_Q' .
\tag{51}
$$

The Gaussian formalism also carries over to the setting of [Generalizing the optical element](../theory/generalization.md). For any passive element in front of the PBS, [(15)](../gaussian_formalism/covariance_matrix.md#eq15) holds with that element's $M$, and the same steps apply. For a complex $M$ the lower-left block becomes $B^{*}$. Effects that are awkward in the state-vector picture are simply extra terms in the covariance matrix: thermal background adds to $N$, and a mixed or multimode source changes $N$ and $\mathcal{M}$.

<span id="dashboard-eq51"></span>

## Dashboard: both routes meet at (51)

<iframe
  src="../../assets/plots/comparison_eq51_plot.html"
  width="100%"
  height="670"
  style="border:0;"
  loading="lazy">
</iframe>

The controls set the squeezing parameter $\lambda$, the detection efficiencies $\eta_H,\eta_V$ and the half-wave-plate angle $\vartheta$. The left heatmap is the $2\times2$ matrix $\mathbb{1}-\lambda^2MDMD$ of the [main derivation](../theory/cc_derivation.md), with rows and columns labelled by the modes $H,V$. The right heatmap is the $4\times4$ matrix $\sigma_Q'$ of [(35a)](../gaussian_formalism/detector_efficiency.md#eq35a), with rows and columns in the order $(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})$. Positive entries are orange, negative entries blue, zero entries gray. The table below the heatmaps evaluates both sides of (51) and the joint no-click probability $P^{(\eta_H,\eta_V)}(0,0)$ obtained from each route. The two columns agree to the last printed digit; the remaining difference of order $10^{-16}$ is floating-point rounding, since (51) is an exact identity.

Things to try:

- **The block structure of $\sigma_Q'$.** The diagonal blocks $A=\operatorname{diag}(1+\nu\eta_H,\,1+\nu\eta_V)$ do not depend on $\vartheta$. Changing $\vartheta$ only changes the off-diagonal blocks $B$, which contain $S_4=\sin4\vartheta$ and $C_4=\cos4\vartheta$, see [(35b)](../gaussian_formalism/detector_efficiency.md#eq35b).
- **Equal efficiencies, $\eta_H=\eta_V$.** Then $D=(1-\eta_H)\mathbb{1}$ and, with $M^2=\mathbb{1}$, the left matrix becomes $\left(1-\lambda^2(1-\eta_H)^2\right)\mathbb{1}$: its off-diagonal entries vanish and nothing on the left moves with $\vartheta$. The entries of $\sigma_Q'$ still move with $\vartheta$, but its determinant does not. Both statements follow directly from (46), where $\vartheta$ only enters through the factor $(\eta_H-\eta_V)^2$.
- **No detection, $\eta_H=\eta_V=0$.** The left matrix is $(1-\lambda^2)\mathbb{1}$ and $\sigma_Q'=\mathbb{1}$, so both routes give $P^{(0,0)}(0,0)=1$, since a detector with zero efficiency never clicks.

<span id="dashboard-qfunction"></span>

## Dashboard: vacuum probability as the height of the $Q$ function

<iframe
  src="../../assets/plots/comparison_qfunction_plot.html"
  width="100%"
  height="640"
  style="border:0;"
  loading="lazy">
</iframe>

In the Gaussian formalism the joint no-click probability is the height of a bell curve. By [(11)](../gaussian_formalism/covariance_matrix.md#eq11) the $Q$ function of the lossy state is

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2\sqrt{\det\sigma_Q'}}\exp\!\left(-\tfrac12\,\mathbf v^{\dagger}\sigma_Q'^{-1}\mathbf v\right),
\qquad
\mathbf v=(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})^T,
$$

and by [(12)](../gaussian_formalism/covariance_matrix.md#eq12) its value at the origin gives $P^{(\eta_H,\eta_V)}(0,0)=\pi^2Q(0)=1/\sqrt{\det\sigma_Q'}$.

$Q$ is a function of four real variables, the real and imaginary parts of $\alpha_H$ and $\alpha_V$. The left plot shows the slice through the origin with $\operatorname{Im}\alpha_H=\operatorname{Im}\alpha_V=0$. There $\mathbf v=(x,y,x,y)^T$ with $x=\operatorname{Re}\alpha_H$, $y=\operatorname{Re}\alpha_V$, and the exponent becomes a quadratic form in $(x,y)$ whose matrix is the sum of the four $2\times2$ blocks of $\sigma_Q'^{-1}$. Darker means larger $Q$; the orange dot marks the maximum $Q(0)$. The plot range is fixed for given $\lambda,\eta_H,\eta_V$, so moving $\vartheta$ shows the bell curve rotating and deforming rather than being rescaled. The right plot shows the peak height $\pi^2Q(0)=P^{(\eta_H,\eta_V)}(0,0)$ over the full range $0\le\vartheta\le\pi/4$, with the orange dot at the current $\vartheta$. The line below the plots compares $\pi^2Q(0)$ with the closed form [(46)](../gaussian_formalism/determinant.md#eq46).

!!! note "A slice does not determine the peak height"
    The peak height is completely determined by the full $4\times4$ matrix $\sigma_Q'$ through $\det\sigma_Q'$, i.e. by the width of $Q$ in all four directions. The slice shows only two of them. A slice can therefore get wider while the peak gets higher, because the bell curve simultaneously gets narrower in the two directions $\operatorname{Im}\alpha_H,\operatorname{Im}\alpha_V$ that are not shown.

Things to try:

- **Unequal efficiencies** (the default, $\eta_H=0.9$, $\eta_V=0.2$). The slice rotates with $\vartheta$ and the peak height varies visibly, with its maximum at the coincidence dip $\vartheta=\pi/8$.
- **Equal efficiencies, $\eta_H=\eta_V$.** The slice still changes with $\vartheta$, but the right curve is flat: as in the first dashboard, $\det\sigma_Q'$ does not depend on $\vartheta$ in this case.
- **Weak squeezing, $\lambda\to0$.** Then $\sigma_Q'\to\mathbb{1}$, the slice becomes the round vacuum bell curve $e^{-(x^2+y^2)}/\pi^2$, and the peak height approaches $P^{(\eta_H,\eta_V)}(0,0)=1$.

<span id="numerical-check"></span>

## Numerical check

### With `thewalrus`

The Python library `thewalrus` <a href="#ref-gupt2019">[4]</a> implements the Gaussian formalism independently of this project. It builds the state from the physical elements: a two-mode squeezer as the SPDC source, an interferometer as the HWP and a loss channel per mode as the detector efficiency. From this state it computes the matrix $\sigma_Q'$ (its function `Qmat`), the no-click probability and the coincidence probability for threshold detectors. At five random parameter sets $(\vartheta,\lambda,\eta_H,\eta_V)$ with $0\le\lambda\le0.95$, the check compares

1. the closed form [(46)](../gaussian_formalism/determinant.md#eq46),
2. $1/\sqrt{\det\sigma_Q'}$ with $\sigma_Q'$ computed by `thewalrus`,
3. the library's threshold-detection probability for "no click",

and the coincidence probability $P_{\mathrm{cc}}$ from [(50)](../gaussian_formalism/coincidence.md#eq50) with the library's Torontonian <a href="#ref-quesada2018">[2]</a>:

| $P(0,0)$, closed form (46) | $1/\sqrt{\det\sigma_Q'}$, `thewalrus` | $P(0,0)$, `thewalrus` | $P_{\mathrm{cc}}$, (50) | $P_{\mathrm{cc}}$, Torontonian |
|---|---|---|---|---|
| 0.151471248630 | 0.151471248630 | 0.151471248630 | 0.548197750498 | 0.548197750498 |
| 0.906354851079 | 0.906354851079 | 0.906354851079 | 0.002401363616 | 0.002401363616 |
| 0.897732507566 | 0.897732507566 | 0.897732507566 | 0.003633792201 | 0.003633792201 |
| 0.970969940602 | 0.970969940602 | 0.970969940602 | 0.005746838768 | 0.005746838768 |
| 0.716428613696 | 0.716428613696 | 0.716428613696 | 0.162660602478 | 0.162660602478 |

In addition, the matrix $\sigma_Q'$ from `thewalrus` was compared entry by entry with the explicit matrix [(35a)](../gaussian_formalism/detector_efficiency.md#eq35a) at $\vartheta=0.37$, $\lambda=0.6$, $\eta_H=0.7$, $\eta_V=0.45$. The largest difference is $2\times10^{-16}$, i.e. the matrices agree, including all signs.

The check is the script [`scripts/check_gaussian_thewalrus.py`](https://github.com/nicosieber/spdccc/blob/main/scripts/check_gaussian_thewalrus.py) (tested with `thewalrus` 0.22.0).

### Symbolic check

With the computer-algebra library `sympy` <a href="#ref-meurer2017">[11]</a> three statements are confirmed exactly, i.e. for all values of $\vartheta,\lambda,\eta_H,\eta_V$ and not only at sample points:

- the determinant identity [(45)](../gaussian_formalism/determinant.md#eq45), using the explicit matrix [(35a)](../gaussian_formalism/detector_efficiency.md#eq35a),
- $M^2=\mathbb{1}$,
- that $\mathcal{M}=\mu M$ and $N=\nu\mathbb{1}$ solve [(18)](../gaussian_formalism/covariance_matrix.md#eq18).

In each case the difference of the two sides simplifies to zero. The check is the script [`scripts/check_gaussian_symbolic.py`](https://github.com/nicosieber/spdccc/blob/main/scripts/check_gaussian_symbolic.py).

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
