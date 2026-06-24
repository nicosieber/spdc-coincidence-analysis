# Normalized coincidence probability of the TMSV
<iframe
  src="../assets/plots/coincidence_plot.html"
  width="100%"
  height="600"
  style="border:0;"
  loading="lazy">
</iframe>

This dashboard visualizes the normalized coincidence probability as a function of the half-wave plate angle \(\vartheta\). The plotted quantity is based on the coincidence probability derived in [Derivation of the coincidence probability](../theory/cc_derivation.md#eq:Pcoinc_inclusion_exclusion):

\begin{equation}
\label{eq:dashboard_pcc}
P_{\mathrm{coinc}}
=
1
-
P_H^{(\eta_H)}(0)
-
P_V^{(\eta_V)}(0)
+
P^{(\eta_H,\eta_V)}(0,0).
\end{equation}

The joint no-click probability entering this expression is given by

\begin{equation}
\label{eq:dashboard_p00}
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

The marginal no-click probabilities are obtained from the same expression by setting the efficiency of the opposite detector to zero:

\begin{equation}
\begin{aligned}
P_H^{(\eta_H)}(0)
&=
P^{(\eta_H,\eta_V=0)}(0,0),
\\
P_V^{(\eta_V)}(0)
&=
P^{(\eta_H=0,\eta_V)}(0,0).
\end{aligned}
\end{equation}

## Normalization 

The dashboard plots the coincidence probability normalized by its maximum value over the displayed interval

\begin{equation}
0 \leq \vartheta \leq \frac{\pi}{4}.
\end{equation}

For fixed values of \(\lambda\), \(\eta_H\), and \(\eta_V\), the unnormalized coincidence curve is

\begin{equation}
C(\vartheta)
=
P_{\mathrm{coinc}}(\vartheta).
\end{equation}

The plotted normalized coincidence is

\begin{equation}
\label{eq:dashboard_normalized_coincidence}
C_{\mathrm{norm}}(\vartheta)
=
\frac{C(\vartheta)}{C_{\max}},
\end{equation}

where

\begin{equation}
C_{\max}
=
\max_{\vartheta \in [0,\pi/4]} C(\vartheta).
\end{equation}

Thus, the largest value of the displayed curve is always equal to one. This makes it easier to compare the shape of the coincidence dip for different values of \(\lambda\), \(\eta_H\), and \(\eta_V\).

# Visibility

<iframe
  src="../assets/plots/visibility_vs_etaH_plot.html"
  width="100%"
  height="600"
  style="border:0;"
  loading="lazy">
</iframe>

The visibility shown in the dashboard quantifies the relative depth of the coincidence modulation. It is computed from the unnormalized coincidence curve as

\begin{equation}
\label{eq:dashboard_visibility}
V
=
\frac{C_{\max}-C_{\min}}{C_{\max}+C_{\min}},
\end{equation}

with

\begin{equation}
C_{\min}
=
\min_{\vartheta \in [0,\pi/4]} C(\vartheta).
\end{equation}

A larger visibility therefore corresponds to a deeper coincidence dip, while \(V=0\) would correspond to a flat coincidence curve.

# Fisher Information and Quantum Sensing

<iframe
  src="../assets/plots/fisher_plot.html"
  width="100%"
  height="600"
  style="border:0;"
  loading="lazy">
</iframe>

## Classical Fisher Information

Estimating an unknown parameter $\varphi$ — here the half-wave plate phase — proceeds by repeating a measurement many times and observing outcomes $\{i\}$ drawn from a probability distribution $\{p_i(\varphi)\}$.
After $\nu$ independent trials, the variance of any unbiased estimator $\hat{\varphi}$ is bounded below by the **Cramér–Rao bound** <a href="#ref-paris2009">[1]</a><a href="#ref-toth2014">[2]</a>

$$
\label{eq:cramer_rao}
\mathrm{Var}(\hat{\varphi}) \geq \frac{1}{\nu\, \mathcal{F}(\varphi)},
$$

where $\nu$ is the number of independent repetitions of the experiment and the **classical Fisher information** is

$$
\label{eq:fisher_def}
\mathcal{F}(\varphi) = \sum_{i} \frac{1}{p_i(\varphi)}\left(\frac{\partial p_i(\varphi)}{\partial \varphi}\right)^2.
$$

A larger Fisher information means the probability distribution changes more steeply with $\varphi$, so each trial carries more information about the parameter. The Cramér–Rao bound is asymptotically tight: it is achieved by the maximum-likelihood estimator in the limit of many trials<a href="#ref-paris2009">[1]</a>.

## From Classical to Quantum Fisher Information

In a quantum experiment, the choice of measurement is itself a degree of freedom. For a given quantum state $\hat{\rho}(\varphi)$, different positive-operator valued measures (POVMs) yield different classical Fisher informations. The **quantum Fisher information** (QFI) $\mathcal{F}_Q$ is defined as the maximum of $\mathcal{F}$ over all allowed POVMs <a href="#ref-paris2009">[1]</a><a href="#ref-toth2014">[2]</a>

$$
\label{eq:qfi_def}
\mathcal{F}_Q(\varphi) = \max_{\{M_i\}} \mathcal{F}(\varphi),
$$

and the resulting **quantum Cramér–Rao bound** (QCRB)

$$
\label{eq:qcrb}
\mathrm{Var}(\hat{\varphi}) \geq \frac{1}{\nu\, \mathcal{F}_Q(\varphi)}
$$

is the fundamental precision limit set by quantum mechanics, independent of which measurement is performed. The QFI depends only on the geometry of the quantum state in parameter space and is saturated by an optimal projective measurement constructed from the symmetric logarithmic derivative of $\hat{\rho}(\varphi)$<a href="#ref-paris2009">[1]</a>.

The measurement considered here is not optimised over all POVMs: it is fixed to a pair of bucket detectors after the PBS, which defines a specific POVM with three outcomes $\{11, H\text{-only}, V\text{-only}\}$ (see [POVM section](../theory/povm.md)). The classical Fisher information computed from these three probabilities is therefore a lower bound to the QFI, and quantifies how well this specific measurement scheme can estimate $\varphi$.

## The Shot-Noise Limit

The shot-noise limit (SNL), also called the standard quantum limit, is the best precision achievable with $\bar{n}$ independent (unentangled) probes per recorded trial<a href="#ref-toth2014">[2]</a>. For $N$ independent photons each carrying phase information, the Fisher information scales linearly with the number of probes:

$$
\label{eq:snl_general}
\mathcal{F}_{\mathrm{SNL}} = \bar{n}.
$$

The corresponding phase uncertainty $\Delta\varphi_{\mathrm{SNL}} = 1/\sqrt{\nu\bar{n}}$ decreases as $1/\sqrt{\bar{n}}$. Quantum entanglement can in principle push this to the **Heisenberg limit** $\Delta\varphi_{\mathrm{HL}} = 1/(\sqrt{\nu}\,\bar{n})$, scaling as $1/\bar{n}$ <a href="#ref-toth2014">[2]</a><a href="#ref-giovanetti2011">[3]</a>. A key result of quantum metrology is that entanglement is *necessary* to surpass the shot-noise scaling in a general linear interferometer<a href="#ref-toth2014">[2]</a>. Beating the SNL — i.e. achieving $\mathcal{F}(\varphi) > \mathcal{F}_{\mathrm{SNL}}$ — is therefore the standard signature of a genuinely quantum metrological advantage.

## The SNL for the TMSV Model

The photon source in this setup is a two-mode squeezed vacuum (TMSV) with squeezing parameter $\lambda$. The mean number of photons generated per SPDC attempt is

\begin{eqation}
\label{eq:n_mean_tmsv}
\langle \hat{n}_H + \hat{n}_V \rangle = \frac{2\lambda^2}{1 - \lambda^2},
\end{equation}

which follows directly from the photon-number distribution of the TMSV state (see [TMSV section](../theory/tmsv.md)).
Not every generated pair leads to a recorded click: detection succeeds with probability $P_{\mathrm{click}} = 1 - P^{(\eta_H, \eta_V)}(0,0)$, where $P^{(\eta_H, \eta_V)}(0,0)$ is the joint vacuum (no-click) probability derived [here](../theory/cc_derivation.md).
The Fisher information is defined per *recorded trial*, so the mean photon number committed per recorded trial — the true resource cost — is

$$
\label{eq:n_per_trial}
\bar{n}(\varphi) = \frac{\langle \hat{n}_H + \hat{n}_V \rangle}{P_{\mathrm{click}}(\varphi)} = \frac{2\lambda^2/(1-\lambda^2)}{1 - P^{(\eta_H,\eta_V)}(0,0)\big|_{\vartheta = \varphi/4}}.
$$

The SNL for this model is therefore

\begin{equation}
\label{eq:snl_tmsv}
\boxed{
\mathcal{F}_{\mathrm{SNL}}(\varphi)
=
\frac{2\lambda^2/(1-\lambda^2)}{1 - P^{(\eta_H,\eta_V)}(0,0)\big|_{\vartheta=\varphi/4}}
}
\end{equation}

with the joint vacuum probability

$$
P^{(\eta_H,\eta_V)}(0,0)
=
\frac{1-\lambda^2}{\sqrt{
\left(1-\lambda^2(1-\eta_H)(1-\eta_V)\right)^2
-
\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)
}}.
$$

**Flat SNL for symmetric losses.** A direct symbolic calculation shows that $\partial \mathcal{F}_{\mathrm{SNL}} / \partial \varphi = 0$ whenever $\eta_H = \eta_V$: the SNL is then completely flat in the phase. This is physically sensible — with symmetric detection the probability of registering *any* click does not depend on how the HWP routes the photons, so the resource cost per trial is the same at every phase. For asymmetric losses the SNL acquires a weak $\varphi$-dependence through the same $(\eta_H - \eta_V)^2\sin^2(4\vartheta)$ interference term that appears in $P^{(\eta_H,\eta_V)}(0,0)$.

**Comparison to the experiment of Slussarenko et al.** Reference <a href="#ref-slussarenko2017">[4]</a> defines
$\mathcal{F}_{\mathrm{SNL}} = N\tilde{k}/k$, where $N = 2$ (photon pair) and $\tilde{k}/k = (1+\xi)/\eta_{\min}$, with $\xi$ the multi-pair emission probability and $\eta_{\min}$ the minimum click probability over all phases and outcomes. This is the worst-case (most conservative) version of the same resource counting. The expression in equation \(\eqref{eq:snl_tmsv}\) is exact for all $\lambda$ and recovers the same value in the limit $\lambda \to 0$ (few-pair, $N=2$-dominant regime): numerically, with $\lambda = 0.1235$ and $\eta_H = \eta_V = 0.80$ it gives $\mathcal{F}_{\mathrm{SNL}} \approx 2.114$, versus the reported $2.096$ — the small difference originating from the multi-pair correction factor $\xi \approx 0.155\,\%$ and the experimental $\eta_{\min} = 0.9556$.

---

## References

<p id="ref-paris2009">
[1] M. G. A. Paris, Quantum estimation for quantum technology, Int. J. Quantum Inf. 7, 125–137 (2009). Open access: https://arxiv.org/abs/0804.2981.
</p>

<p id="ref-toth2014">
[2] G. Tóth and I. Apellaniz, Quantum metrology from a quantum information science perspective, J. Phys. A: Math. Theor.47, 424006 (2014). Open access: https://arxiv.org/abs/1405.4878. 
</p>

<p id="ref-giovanetti2011">
[3] V. Giovannetti, S. Lloyd, and L. Maccone, Advances in quantum metrology, Nature Photonics 5, 222–229 (2011). Open-access preprint: https://arxiv.org/abs/1102.2318. 
</p>

<p id="ref-slussarenko2017">
[4] S. Slussarenko et al., Unconditional violation of the shot-noise limit in photonic quantum metrology, Nature Photonics 11, 700–703 (2017). Open-access preprint: https://arxiv.org/abs/1707.08977. 
</p>
