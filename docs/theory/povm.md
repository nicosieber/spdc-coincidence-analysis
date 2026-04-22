# Positive Operator-Valued Measure (POVM)
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

<span id="completeness_relation"></span>

\begin{equation}
\label{formula:completeness_relation}
\begin{aligned}
  \sum_i \Pi_i = \mathbb{1}, \quad P(i) = \langle \Psi \rvert M^{\dagger}_iM_i \lvert \Psi \rangle,
\end{aligned}
\end{equation}

with $I$ as the identity matrix. Following the relation in equation \(\eqref{formula:completeness_relation}\), the set of operators $\Pi_i$ are known as POVM elements associated with the measurement, whereas the complete set $\{\Pi_i\}$ is known as a POVM and is completely sufficient to determine  the probabilities of the different measurement outcomes[@nielsen_chuang].

<div class="nav-footer">
  <a class="nav-prev" href="../simplified_example">
    ← Previous
  </a>

  <a class="nav-next" href="../povm_bucket_detectors">
    Next →
  </a>
</div>

## References