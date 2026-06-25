# Fisher Information
<span id="concept:fisher_information"></span>

Estimating an unknown parameter $\varphi$ — here the half-wave plate phase — proceeds by repeating a measurement many times and observing outcomes $\{i\}$ drawn from a probability distribution $\{p_i(\varphi)\}$.
After $\nu$ independent trials, the variance of any unbiased estimator $\hat{\varphi}$ is bounded below by the **Cramér–Rao bound** <a href="#ref-paris2009">[1]</a><a href="#ref-toth2014">[2]</a>

\begin{equation}
\label{eq:cramer_rao}
\mathrm{Var}(\hat{\varphi}) \geq \frac{1}{\nu\, \mathcal{F}(\varphi)},
\end{equation}

where $\nu$ is the number of independent repetitions of the experiment and the **classical Fisher information** is

\begin{equation}
\label{eq:fisher_def}
\mathcal{F}(\varphi) = \sum_{i} \frac{1}{p_i(\varphi)}\left(\frac{\partial p_i(\varphi)}{\partial \varphi}\right)^2.
\end{equation}

A larger Fisher information means the probability distribution changes more steeply with $\varphi$, so each trial carries more information about the parameter. The Cramér–Rao bound is asymptotically tight: it is achieved by the maximum-likelihood estimator in the limit of many trials <a href="#ref-paris2009">[1]</a>.

Note that the probabilities $p_i(\varphi)$ entering equation \eqref{eq:fisher_def} are
conditioned on a click being recorded — they are the outcome probabilities *given* that at
least one detector fired. This conditioning is necessary because trials in which neither
detector clicks (\(00\) outcome) are not recorded and carry no phase information. The
unnormalized outcome probabilities must therefore be divided by the total click probability
$P_{\mathrm{click}} = 1 - P^{(\eta_H,\eta_V)}(0,0)$ before entering the Fisher
information sum. As a consequence, $\mathcal{F}(\varphi)$ as defined here is the Fisher
information **per recorded trial**, which is the natural figure of merit when comparing
to the shot-noise limit defined on the same per-recorded-trial basis.

## From Classical to Quantum Fisher Information

In a quantum experiment, the choice of measurement is itself a degree of freedom. For a given quantum state $\hat{\rho}(\varphi)$, different positive-operator valued measures (POVMs) yield different classical Fisher informations. The **quantum Fisher information** (QFI) $\mathcal{F}_Q$ is defined as the maximum of $\mathcal{F}$ over all allowed POVMs <a href="#ref-paris2009">[1]</a><a href="#ref-toth2014">[2]</a>

\begin{equation}
\label{eq:qfi_def}
\mathcal{F}_Q(\varphi) = \max_{\{M_i\}} \mathcal{F}(\varphi),
\end{equation}

and the resulting **quantum Cramér–Rao bound** (QCRB)

\begin{equation}
\label{eq:qcrb}
\mathrm{Var}(\hat{\varphi}) \geq \frac{1}{\nu\, \mathcal{F}_Q(\varphi)}
\end{equation}

is the fundamental precision limit set by quantum mechanics, independent of which measurement is performed. The QFI depends only on the geometry of the quantum state in parameter space and is saturated by an optimal projective measurement constructed from the symmetric logarithmic derivative of $\hat{\rho}(\varphi)$ <a href="#ref-paris2009">[1]</a>.

The measurement considered here is not optimised over all POVMs: it is fixed to a pair of bucket detectors after the PBS, which defines a specific POVM with three outcomes $\{11, H\text{-only}, V\text{-only}\}$ (see [POVM section](../theory/povm.md)). The classical Fisher information computed from these three probabilities is therefore a lower bound to the QFI, and quantifies how well this specific measurement scheme can estimate $\varphi$.

## The Shot-Noise Limit

The shot-noise limit (SNL), also called the standard quantum limit, is the best precision achievable with $\bar{n}$ independent (unentangled) probes per recorded trial <a href="#ref-toth2014">[2]</a>. For $N$ independent photons each carrying phase information, the Fisher information scales linearly with the number of probes:

\begin{equation}
\label{eq:snl_general}
\mathcal{F}_{\mathrm{SNL}} = \bar{n}.
\end{equation}

The corresponding phase uncertainty $\Delta\varphi_{\mathrm{SNL}} = 1/\sqrt{\nu\bar{n}}$ decreases as $1/\sqrt{\bar{n}}$. Quantum entanglement can in principle push this to the **Heisenberg limit** $\Delta\varphi_{\mathrm{HL}} = 1/(\sqrt{\nu}\,\bar{n})$, scaling as $1/\bar{n}$ <a href="#ref-toth2014">[2]</a><a href="#ref-giovanetti2011">[3]</a>. A key result of quantum metrology is that entanglement is *necessary* to surpass the shot-noise scaling in a general linear interferometer <a href="#ref-toth2014">[2]</a>. Beating the SNL — i.e. achieving $\mathcal{F}(\varphi) > \mathcal{F}_{\mathrm{SNL}}$ — is therefore the standard signature of a genuinely quantum metrological advantage.

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
