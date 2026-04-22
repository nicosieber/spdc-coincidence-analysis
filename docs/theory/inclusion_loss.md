# Inclusion of loss

In realistic experimental scenarios, losses due to imperfect coupling, optical elements, and detector inefficiencies must be taken into account. These losses can be modeled as linear attenuation processes and are equivalent to introducing fictitious beam splitters with transmission $\eta$ in front of each detector.

Within the POVM framework, loss can be incorporated directly into the measurement operators. For a detector with efficiency $\eta$, the no-click operator becomes

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

Analogous to (\ref{formula:POVM_cc_probability}), the coincidence probability becomes

\begin{equation}
\label{POVM:coinc_prob_loss}
\begin{aligned}
    P_{\text{coinc}}^{(\eta)} = 1 - P_H^{(\eta)}(0) - P_V^{(\eta)}(0) + P^{(\eta)}(0,0),
\end{aligned}
\end{equation}

where the vacuum probabilities now include the effect of loss.

For symmetric losses in both modes, a single effective efficiency $\eta$ can be used to describe all linear loss processes in the system.

For non-symmetric losses on detectors $A$ and $B$, this becomes:

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
  <a class="nav-prev" href="../povm_bucket_detectors">
    ← Previous
  </a>

  <a class="nav-next" href="../tmsv">
    Next →
  </a>
</div>

## References