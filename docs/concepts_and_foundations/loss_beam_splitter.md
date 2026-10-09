# Detector loss as a beam splitter

A detector with efficiency $\eta$ can be modelled as a perfect detector behind a beam splitter of transmissivity $\eta$, whose unused input port is in the vacuum: the transmitted photons reach the detector, the reflected ones are lost. This page derives what this beam splitter does to a state, and shows that it reproduces the lossy no-click POVM element $(1-\eta)^{\hat n}$ of [POVM](../theory/povm.md#formula_P_cc_loss). The result is used in [Detector efficiency](../gaussian_formalism/detector_efficiency.md).

## The beam splitter on photon-number states

Call the signal mode $\hat a$ and the mode entering the unused port $\hat b$. The beam splitter sends each incoming photon of mode $a$ into the transmitted output (still called $a$) with amplitude $\sqrt\eta$ and into the reflected output $b$ with amplitude $\sqrt{1-\eta}$:

<span id="bs:creation"></span>

\begin{equation}
\label{bs:creation}
\hat a^{\dagger}\;\longrightarrow\;\sqrt{\eta}\,\hat a^{\dagger}+\sqrt{1-\eta}\,\hat b^{\dagger}.
\end{equation}

(Phases on the reflected path are irrelevant here, because mode $b$ is discarded at the end.) A Fock state $\lvert n\rangle_a=\frac{(\hat a^{\dagger})^n}{\sqrt{n!}}\lvert 0\rangle$ with vacuum in mode $b$ therefore becomes, by the binomial theorem (the operators $\hat a^{\dagger}$ and $\hat b^{\dagger}$ commute),

$$
\frac{1}{\sqrt{n!}}\left(\sqrt{\eta}\,\hat a^{\dagger}+\sqrt{1-\eta}\,\hat b^{\dagger}\right)^n\lvert 0,0\rangle
=\frac{1}{\sqrt{n!}}\sum_{k=0}^{n}\binom{n}{k}\eta^{\frac{n-k}{2}}(1-\eta)^{\frac{k}{2}}\,(\hat a^{\dagger})^{n-k}(\hat b^{\dagger})^{k}\lvert 0,0\rangle .
$$

With $(\hat a^{\dagger})^{n-k}\lvert 0\rangle=\sqrt{(n-k)!}\,\lvert n-k\rangle$, $(\hat b^{\dagger})^{k}\lvert 0\rangle=\sqrt{k!}\,\lvert k\rangle$ and $\binom{n}{k}\sqrt{(n-k)!\,k!}/\sqrt{n!}=\sqrt{\binom{n}{k}}$:

<span id="bs:fock"></span>

\begin{equation}
\label{bs:fock}
\lvert n\rangle_a\lvert 0\rangle_b\;\longrightarrow\;\sum_{k=0}^{n}\sqrt{\binom{n}{k}}\,\eta^{\frac{n-k}{2}}(1-\eta)^{\frac{k}{2}}\,\lvert n-k\rangle_a\lvert k\rangle_b .
\end{equation}

The squared amplitudes $\binom{n}{k}\eta^{n-k}(1-\eta)^k$ are the binomial distribution: each of the $n$ photons is transmitted with probability $\eta$, independently of the others, and $k$ of them are lost.

## Kraus operators

The lost photons in mode $b$ are never looked at, so mode $b$ is traced out. Projecting \(\eqref{bs:fock}\) onto $\lvert k\rangle_b$ ("$k$ photons lost") defines one operator on mode $a$ for each $k$:

<span id="bs:kraus"></span>

\begin{equation}
\label{bs:kraus}
\hat K_k=\sum_{n=k}^{\infty}\sqrt{\binom{n}{k}}\,\eta^{\frac{n-k}{2}}(1-\eta)^{\frac{k}{2}}\,\lvert n-k\rangle\langle n\rvert,
\qquad
\rho\;\longrightarrow\;\mathcal{E}_\eta(\rho)=\sum_{k=0}^{\infty}\hat K_k\,\rho\,\hat K_k^{\dagger}.
\end{equation}

The sum over $k$ is the partial trace over mode $b$. The operators $\hat K_k$ are called *Kraus operators*, and $\mathcal{E}_\eta$ is the *loss channel*. Even for a pure input state, $\mathcal{E}_\eta(\rho)$ is in general mixed, because the information carried away by mode $b$ is lost.

## The vacuum probability behind the beam splitter

A perfect detector behind the beam splitter does not click if the transmitted mode is empty. Only the term $n=k$ of \(\eqref{bs:kraus}\) ("all photons lost") ends in the vacuum, so

$$
\langle 0\rvert\hat K_k\lvert n\rangle=\delta_{nk}\,(1-\eta)^{n/2}.
$$

Inserting a resolution of the identity on both sides of $\rho$:

<span id="bs:vacuum"></span>

\begin{equation}
\label{bs:vacuum}
\langle 0\rvert\mathcal{E}_\eta(\rho)\lvert 0\rangle
=\sum_{k}\sum_{n,m}\langle 0\rvert\hat K_k\lvert n\rangle\langle n\rvert\rho\lvert m\rangle\langle m\rvert\hat K_k^{\dagger}\lvert 0\rangle
=\sum_{n}(1-\eta)^{n}\langle n\rvert\rho\lvert n\rangle
=\operatorname{Tr}\!\left[\rho\,(1-\eta)^{\hat n}\right].
\end{equation}

The right-hand side is the expectation value of the no-click POVM element $\Pi_0^{(\eta)}=(1-\eta)^{\hat n}$ of a lossy bucket detector. So "lossy detector" and "beam splitter + perfect detector" give the same no-click probability for every state $\rho$.

## The beam splitter on operators

Instead of transforming the state, the beam splitter can act on the operators whose expectation values are taken. The annihilation operator of the transmitted mode is then

<span id="bs:heisenberg"></span>

\begin{equation}
\label{bs:heisenberg}
\hat a\;\longrightarrow\;\sqrt{\eta}\,\hat a+\sqrt{1-\eta}\,\hat b ,
\end{equation}

with $\hat b$ in the vacuum. In a product of ladder operators with all creation operators to the left of all annihilation operators (*normal order*), every term containing $\hat b$ or $\hat b^{\dagger}$ vanishes, since $\hat b\lvert 0\rangle=0$ on the right and $\langle 0\rvert\hat b^{\dagger}=0$ on the left. Only the terms with $\sqrt\eta\,\hat a$ and $\sqrt\eta\,\hat a^{\dagger}$ survive. For example,

$$
\operatorname{Tr}\!\big[\mathcal{E}_\eta(\rho)\,\hat a^{\dagger}\hat a\big]=\eta\,\operatorname{Tr}\!\big[\rho\,\hat a^{\dagger}\hat a\big],
\qquad
\operatorname{Tr}\!\big[\mathcal{E}_\eta(\rho)\,\hat a\hat a\big]=\eta\,\operatorname{Tr}\!\big[\rho\,\hat a\hat a\big].
$$

So in a normally ordered expectation value, every $\hat a$ or $\hat a^{\dagger}$ simply brings a factor $\sqrt\eta$. For products that are not normally ordered this fails: $\langle 0\rvert\hat b\hat b^{\dagger}\lvert 0\rangle=1$ does not vanish.
