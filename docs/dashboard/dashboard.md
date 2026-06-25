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

## Motivation: Reading the Phase from Click Patterns

To estimate the half-wave plate phase, we repeat the experiment many times and record what
the two bucket detectors report on each trial. Each trial ends in one of three
distinguishable outcomes: both detectors click, only the H-detector
clicks, or only the V-detector clicks. The no-click outcome carries no phase information and is discarded from the analysis.

Throughout this section we follow the convention of <a href="#ref-slussarenko2017">[1]</a>
and parametrise the half-wave plate setting by the phase

\begin{equation}
\varphi = 4\vartheta,
\end{equation}

so that \(\varphi\) runs over \([0, \pi]\) while \(\vartheta\) runs over \([0, \pi/4]\).
This substitution is purely a relabelling of the horizontal axis and does not affect the
physics, but it is the convention used when comparing [Fisher Information](../concepts_and_foundations/fisher_information.md) values to
<a href="#ref-slussarenko2017">[1]</a>. Because \(\varphi = 4\vartheta\), the chain rule
introduces a factor of \(1/16\) whenever a derivative with respect to \(\vartheta\) is
converted to one with respect to \(\varphi\):

\begin{equation}
\frac{\partial}{\partial\vartheta} = 4\,\frac{\partial}{\partial\varphi}
\quad\Longrightarrow\quad
\left(\frac{\partial p_i}{\partial\varphi}\right)^2
=
\frac{1}{16}\left(\frac{\partial p_i}{\partial\vartheta}\right)^2.
\end{equation}

The Fisher information quoted per unit of \(\varphi\) is therefore smaller by a factor of
\(16\) compared to the same quantity quoted per unit of \(\vartheta\).

Each of the three outcomes occurs with a probability that depends on \(\varphi\):

\begin{equation}
p_{11}(\varphi) = P_{\mathrm{coinc}}(\varphi), \qquad
p_H(\varphi) = P_H(\varphi), \qquad
p_V(\varphi) = P_V(\varphi).
\end{equation}

If these probabilities were flat — the same value for every \(\varphi\) — no amount of
data could tell us where the wave plate is set. Conversely, the more steeply they vary
with \(\varphi\), the more information each trial carries. Intuitively, when the
coincidence dip is steep, a small rotation of the wave plate shifts photons from the
coincidence outcome into the \(H\)-only or \(V\)-only outcomes in a detectable way; the
imbalance between \(p_H\) and \(p_V\) breaks the symmetry and further pins down the
phase. The Fisher information formalises exactly this intuition: it weights the slope of
each outcome probability by the inverse of that probability, penalising outcomes that are
rare (and therefore statistically noisy) and rewarding outcomes that are both sensitive to
\(\varphi\) *and* frequently observed. The result is a single number
\(\mathcal{F}(\varphi)\) that captures, per trial, how much the full click pattern
constrains the unknown phase.

## The SNL for the TMSV Model

The photon source in this setup is a two-mode squeezed vacuum (TMSV) with squeezing parameter $\lambda$. The mean number of photons generated per SPDC attempt is

\begin{equation}
\label{eq:n_mean_tmsv}
\langle \hat{n}_H + \hat{n}_V \rangle = \frac{2\lambda^2}{1 - \lambda^2},
\end{equation}

which follows directly from the photon-number distribution of the TMSV state (see [TMSV section](../theory/tmsv.md)).
Not every generated pair leads to a recorded click: detection succeeds with probability
$P_{\mathrm{click}} = 1 - P^{(\eta_H, \eta_V)}(0,0)$, where $P^{(\eta_H, \eta_V)}(0,0)$
is the joint vacuum (no-click) probability derived [here](../theory/cc_derivation.md).
The Fisher information is defined per *recorded trial*, so the mean photon number
committed per recorded trial — the true resource cost — is

\begin{equation}
\label{eq:n_per_trial}
\bar{n}(\varphi) = \frac{\langle \hat{n}_H + \hat{n}_V \rangle}{P_{\mathrm{click}}(\varphi)} = \frac{2\lambda^2/(1-\lambda^2)}{1 - P^{(\eta_H,\eta_V)}(0,0)\big|_{\vartheta = \varphi/4}}.
\end{equation}

Dividing by $P_{\mathrm{click}}$ accounts for the fact that most SPDC attempts produce no
detectable photon pair: the photon budget must be charged only against trials that actually
contribute to the Fisher information sum. Using the total number of SPDC attempts instead
would undercount the resource cost per useful event and artificially inflate the apparent
advantage over the SNL.

The SNL for this model is therefore

\begin{equation}
\label{eq:snl_tmsv}
\boxed{
\mathcal{F}_{\mathrm{SNL}}(\varphi)
=
\frac{2\lambda^2/(1-\lambda^2)}{1 - P^{(\eta_H,\eta_V)}(0,0)\big|_{\vartheta=\varphi/4}}
}.
\end{equation}

### Flat SNL for symmetric losses
A direct symbolic calculation shows that $\partial \mathcal{F}_{\mathrm{SNL}} / \partial \varphi = 0$ whenever $\eta_H = \eta_V$: the SNL is then completely flat in the phase. This is physically sensible — with symmetric detection the probability of registering *any* click does not depend on how the HWP routes the photons, so the resource cost per trial is the same at every phase. For asymmetric losses the SNL acquires a weak $\varphi$-dependence through the same $(\eta_H - \eta_V)^2\sin^2(4\vartheta)$ interference term that appears in $P^{(\eta_H,\eta_V)}(0,0)$.

### Comparison to the experiment of Slussarenko et al 
Reference <a href="#ref-slussarenko2017">[1]</a> defines
$\mathcal{F}_{\mathrm{SNL}} = N\tilde{k}/k$, where $N = 2$ (photon pair) and $\tilde{k}/k = (1+\xi)/\eta_{\min}$, with $\xi$ the multi-pair emission probability and $\eta_{\min}$ the minimum click probability over all phases and outcomes. This is the worst-case (most conservative) version of the same resource counting. The expression in equation \(\eqref{eq:snl_tmsv}\) is exact for all $\lambda$ and recovers the same value in the limit $\lambda \to 0$ (few-pair, $N=2$-dominant regime): numerically, with $\lambda = 0.1235$ and $\eta_H = \eta_V = 0.80$ it gives $\mathcal{F}_{\mathrm{SNL}} \approx 2.114$, versus the reported $2.096$ — the small difference originating from the multi-pair correction factor $\xi \approx 0.155\,\%$ and the experimental $\eta_{\min} = 0.9556$.

---

## References

<p id="ref-slussarenko2017">
[1] S. Slussarenko et al., Unconditional violation of the shot-noise limit in photonic quantum metrology, Nature Photonics 11, 700–703 (2017). Open-access preprint: https://arxiv.org/abs/1707.08977. 
</p>