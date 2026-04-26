# Positive Operator-Valued Measure (POVM)
## General POVM formalism
The measurement process can be described rigorously using the formalism of POVMs. In this framework, measurements are described by measurement operators $M_i$ performed on quantum systems in the state $\lvert \Psi \rangle$.  The probability $P(i)$ of obtaining outcome $i$ is given by

\begin{equation}
  \begin{aligned}
  P(i) = \langle \Psi \rvert M^{\dagger}_iM_i \lvert \Psi \rangle.
  \end{aligned}
\end{equation}

Defining

\begin{equation}
\begin{aligned}
  \Pi_i\equiv M^{\dagger}_iM_i,
\end{aligned}
\end{equation}

$\Pi_i$ is a positive operator such that 

\begin{equation}
\label{formula:completeness_relation}
\begin{aligned}
  \sum_i \Pi_i = \mathbb{1}, \quad P(i) = \langle \Psi \rvert M^{\dagger}_iM_i \lvert \Psi \rangle,
\end{aligned}
\end{equation}

with $I$ as the identity matrix. Following the relation in equation \(\eqref{formula:completeness_relation}\), the set of operators $\Pi_i$ are known as POVM elements associated with the measurement, whereas the complete set $\{\Pi_i\}$ is known as a POVM and is completely sufficient to determine  the probabilities of the different measurement outcomes (see Nielsen and Chuang <a href="#ref-nc">[1]</a>).

## POVM of bucket detectors

In this work, the coincidence probabilities of click detectors - also called bucket detectors - are of interest. A bucket detector distinguishes only between two possible outcomes: no click (no photons detected) and click (at least one photon detected). Following, the two-way-outcome POVM is $\{\Pi_0, \Pi_{\text{click}}\}$.

The no-click event corresponds to the situation in which the field is in the vacuum state. This requirement can be formulated as

\begin{equation}
\label{braket}
\begin{aligned}
 \langle n \rvert\Pi_0 \lvert n \rangle =
    \begin{cases}
        1, & n = 0, \\
        0, & n > 0.
    \end{cases}
\end{aligned}
\end{equation}

The unique operator satisfying this condition is the projector onto the vacuum state,

\begin{align}
    \Pi_0 = \lvert 0 \rangle \langle 0 \rvert.
\end{align}

Using equation \(\eqref{formula:completeness_relation}\), the click operator is then given by

\begin{equation}
\begin{aligned}
    \Pi_{\text{click}} = \mathbb{1} - \lvert 0 \rangle \langle 0 \rvert.
\end{aligned}
\end{equation}

For two detectors measuring the horizontal and vertical modes, the coincidence measurement operator is given by

\begin{equation}
\begin{aligned}
    \Pi_{\text{coinc}} = (\mathbb{1} - \lvert 0 \rangle \langle 0 \rvert)_H \otimes (\mathbb{1} - \lvert 0 \rangle \langle 0 \rvert)_V.
\end{aligned}
\end{equation}

Expanding this operator yields

\begin{equation}
\begin{aligned}
    \Pi_{\text{coinc}} = \mathbb{1} \otimes \mathbb{1} 
    - \lvert 0 \rangle \langle 0 \rvert \otimes \mathbb{1} 
    - \mathbb{1} \otimes \lvert 0 \rangle \langle 0 \rvert 
    + \lvert 0,0 \rangle \langle 0,0 \rvert.
\end{aligned}
\end{equation}

Using the expansion of $\Pi_{\text{coinc}}$, the probability of measuring coincidences with bucket detectors can be expressed as

\begin{equation}
\begin{aligned}
    P_{\text{coinc}} &= \langle \Psi \rvert \mathbb{1} \otimes \mathbb{1} \lvert \Psi \rangle
    - \langle \Psi \rvert (|0\rangle\langle 0| \otimes \mathbb{1}) \lvert \Psi \rangle \notag \\
    &\quad - \langle \Psi \rvert (\mathbb{1} \otimes |0\rangle\langle 0|) \lvert \Psi \rangle
    + \langle \Psi \rvert 0,0\rangle\langle 0,0 \lvert \Psi \rangle.
\end{aligned}
\end{equation}

The individual terms evaluate to

\begin{equation}
\begin{aligned}
    \langle \Psi \rvert \mathbb{1} \otimes \mathbb{1} \lvert \Psi \rangle &= 1, \\
    \langle \Psi \rvert (|0\rangle\langle 0| \otimes \mathbb{1}) \lvert \Psi \rangle &= P_H(0), \\
    \langle \Psi \rvert (\mathbb{1} \otimes |0\rangle\langle 0|) \lvert \Psi \rangle &= P_V(0), \\
    \langle \Psi \rvert 0,0 \rangle\langle 0,0 \lvert \Psi \rangle &= P(0,0),
\end{aligned}
\end{equation}

which leads to

\begin{equation}
\label{formula:POVM_cc_probability}
\begin{aligned}
    P_{\text{coinc}} = 1 - P_H(0) - P_V(0) + P(0,0),
\end{aligned}
\end{equation}

where $P_H(0)$ and $P_V(0)$ denote the probabilities of detecting no photons in the respective modes, and $P(0,0)$ is the joint vacuum probability. 

## Inclusion of loss into the detector model

In realistic experimental scenarios, losses due to imperfect coupling, optical elements, and detector inefficiencies must be taken into account. These losses can be modeled as linear attenuation processes and are equivalent to introducing fictitious beam splitters with transmission $\eta$ in front of each detector.

Within the POVM framework, loss can be incorporated directly into the measurement operators. For a detector with efficiency $\eta$, the no-click operator becomes (see <a href="#ref-akhlaghi2011">[2]</a>, <a href="#ref-christ2012">[3]</a>, <a href="#ref-silberhorn2007">[4]</a>)

\begin{equation}
\label{POVM:loss}
\begin{aligned}
    \Pi_0^{(\eta)} = \sum_{n=0}^{\infty} (1-\eta)^{\hat n} \lvert n \rangle \langle n \rvert,
\end{aligned}
\end{equation}

which reflects the probability that all photons are lost before detection.

The corresponding click operator is then

\begin{equation}
\begin{aligned}
    \Pi_{\text{click}}^{(\eta)} = \mathbb{1} - \Pi_0^{(\eta)}.
\end{aligned}
\end{equation}

The coincidence operator in the presence of loss is given by

\begin{equation}
\begin{aligned}
    \Pi_{\text{coinc}}^{(\eta)} = (\mathbb{1} - \Pi_0^{(\eta)})_H \otimes (\mathbb{1} - \Pi_0^{(\eta)})_V.
\end{aligned}
\end{equation}

Analogous to \(\eqref{formula:POVM_cc_probability}\), the coincidence probability becomes

\begin{equation}
\label{POVM:coinc_prob_loss}
\begin{aligned}
    P_{\text{coinc}}^{(\eta)} = 1 - P_H^{(\eta)}(0) - P_V^{(\eta)}(0) + P^{(\eta)}(0,0),
\end{aligned}
\end{equation}

where the vacuum probabilities now include the effect of loss.

For symmetric losses in both modes, a single effective efficiency $\eta$ can be used to describe all linear loss processes in the system.

For non-symmetric losses on detectors $A$ and $B$, this becomes:

<span id="formula_P_cc_loss"></span>

\begin{equation}
\label{formula_P_cc_loss}
\begin{aligned}
    P_{\text{coinc}}^{(\eta_A,\eta_B)} &= \langle \Psi \rvert\Pi_{\text{click}}^{\eta_A}\otimes\Pi_{\text{click}}^{\eta_B}\lvert \Psi \rangle\\
    &=\langle \Psi \rvert\left[\mathbb{1}-\left(1-\eta_A\right)^{\hat{n}_A}\right]\otimes \left[\mathbb{1}-\left(1-\eta_B\right)^{\hat{n}_B}\right]\lvert \Psi \rangle\\
    &=\\
    &+1\\
    &-\langle \Psi \rvert\mathbb{1}\otimes\left(1-\eta_B\right)^{\hat{n}_B}\lvert \Psi \rangle\\
    &-\langle \Psi \rvert\left(1-\eta_A\right)^{\hat{n}_A}\otimes \mathbb{1}\lvert \Psi \rangle\\
    &+\langle \Psi \rvert\left(1-\eta_A\right)^{\hat{n}_A}\otimes \left(1-\eta_B\right)^{\hat{n}_B}\lvert \Psi \rangle\\
    &= 1 - P_H^{(\eta_A,\eta_B)}(0) - P_V^{(\eta_A,\eta_B)}(0) + P^{(\eta_A,\eta_B)}(0,0)
\end{aligned}
\end{equation}


<div class="nav-footer">
  <a class="nav-prev" href="simplified_example.md">
    ← Previous
  </a>

  <a class="nav-next" href="tmsv.md">
    Next →
  </a>
</div>

## References

<p id="ref-nc">
[1] M. A. Nielsen and I. L. Chuang, <em>Quantum Computation and Quantum Information</em>, 10th Anniversary Edition, Cambridge University Press, 2010.
</p>

<p id="ref-akhlaghi2011">
[2] M. K. Akhlaghi, A. H. Majedi, and J. S. Lundeen,
“Nonlinearity in single photon detection: modeling and quantum tomography,”
<em>Optics Express</em>, vol. 19, no. 22, pp. 21305–21312, 2011.
</p>

<p id="ref-christ2012">
[3] A. Christ and C. Silberhorn,
“Limits on the deterministic creation of pure single-photon states using parametric down-conversion,”
<em>Physical Review A</em>, vol. 85, no. 2, p. 023829, 2012.
</p>

<p id="ref-silberhorn2007">
[4] C. Silberhorn,
“Detecting quantum light,”
<em>Contemporary Physics</em>, vol. 48, no. 3, pp. 143–156, 2007.
</p>