# POVM of bucket detectors

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

Using equation (3) in [POVM](../povm/#completeness_relation), the click operator is then given by

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

<div class="nav-footer">
  <a class="nav-prev" href="../povm">
    ← Previous
  </a>

  <a class="nav-next" href="../inclusion_loss">
    Next →
  </a>
</div>

## References