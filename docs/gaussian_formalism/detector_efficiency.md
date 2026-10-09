# Detector efficiency as a beam splitter

## Why this is allowed

A beam splitter with transmissivity $\eta$, whose other input is vacuum, loses $k$ of $n$ photons with binomial probability. Its effect on a state is described by the operators (Kraus operators)

<span id="eq30"></span>

$$
\hat K_k=\sum_{n=k}^{\infty}\sqrt{\binom{n}{k}}\,\eta^{\frac{n-k}{2}}(1-\eta)^{\frac{k}{2}}\,\lvert n-k\rangle\langle n\rvert,
\qquad
\rho\;\longrightarrow\;\mathcal{E}_\eta(\rho)=\sum_{k=0}^{\infty}\hat K_k\,\rho\,\hat K_k^{\dagger}.
\tag{30}
$$

Only the term $n=k$ ("all photons lost") ends in the vacuum, so $\langle 0\rvert\hat K_k\lvert n\rangle=\delta_{nk}(1-\eta)^{n/2}$. Therefore

<span id="eq31"></span>

$$
\langle 0\rvert\mathcal{E}_\eta(\rho)\lvert 0\rangle
=\sum_{n}(1-\eta)^{n}\langle n\rvert\rho\lvert n\rangle
=\operatorname{Tr}\!\left[\rho\,(1-\eta)^{\hat n}\right].
\tag{31}
$$

Where the Kraus operators (30) come from, and the step to (31) written out, is shown in [Detector loss as a beam splitter](../concepts_and_foundations/loss_beam_splitter.md).

The right-hand side of (31) is the no-click POVM element $\Pi_0^{(\eta)}$ from [POVM](../theory/povm.md#formula_P_cc_loss). So [(1)](overview.md#eq1) becomes

<span id="eq32"></span>

$$
P^{(\eta_H,\eta_V)}(0,0)
=\langle 0,0\rvert\,\rho'\,\lvert 0,0\rangle,
\qquad
\rho'=(\mathcal{E}_{\eta_H}\otimes\mathcal{E}_{\eta_V})\big(\lvert\Psi\rangle\langle\Psi\rvert\big):
\tag{32}
$$

an inefficient detector is a perfect detector behind a beam splitter. This beam-splitter model of absorption is standard in quantum optics <a href="#ref-leonhardt1997">[7, Sec. 4.1.4]</a>; in the language of Gaussian channels it is the pure-loss channel <a href="#ref-weedbrook2012">[8]</a>. By [(26)](vacuum_probability.md#eq26), $P(0,0)=1/\sqrt{\det\sigma_Q'}$, where $\sigma_Q'$ is the matrix [(6)](covariance_matrix.md#eq6) of $\rho'$.

## What the beam splitter does to the covariance matrix

Expectation values in $\rho'$ are easiest to compute by letting the beam splitter act on the operators (Heisenberg picture, <a href="#ref-leonhardt1997">[7, Sec. 4.1.1]</a>). A new mode $\hat b_H$ (or $\hat b_V$) in the vacuum enters the unused port:

<span id="eq33"></span>

$$
\hat a_H\;\longrightarrow\;\sqrt{\eta_H}\,\hat a_H+\sqrt{1-\eta_H}\,\hat b_H,
\qquad
\hat a_V\;\longrightarrow\;\sqrt{\eta_V}\,\hat a_V+\sqrt{1-\eta_V}\,\hat b_V .
\tag{33}
$$

Insert (33) into the blocks $N$ and $\mathcal{M}$ of [(10)](covariance_matrix.md#eq10). Because the $\hat b$ modes are in the vacuum and uncorrelated with $\lvert\Psi\rangle$, every term containing a $\hat b$ vanishes: $\langle 0\rvert\hat b\lvert 0\rangle=\langle 0\rvert\hat b^{\dagger}\hat b\lvert 0\rangle=\langle 0\rvert\hat b\hat b\lvert 0\rangle=0$. (This is why $N$ and $\mathcal{M}$ are transformed rather than the entries of $\sigma_Q$: $\langle 0\rvert\hat b\hat b^{\dagger}\lvert 0\rangle=1$ would not vanish.) For example,

<span id="eq34"></span>

$$
\begin{aligned}
\operatorname{Tr}\!\big[\rho'\,\hat a_H^{\dagger}\hat a_H\big]
&=\eta_H\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle+(1-\eta_H)\underbrace{\langle 0\rvert\hat b_H^{\dagger}\hat b_H\lvert 0\rangle}_{0}+\text{cross terms with }\langle 0\rvert\hat b_H\lvert 0\rangle=0
=\eta_H\,\nu,\\
\operatorname{Tr}\!\big[\rho'\,\hat a_H\hat a_V\big]
&=\sqrt{\eta_H\eta_V}\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle=-\sqrt{\eta_H\eta_V}\,\mu C_4,\\
\operatorname{Tr}\!\big[\rho'\,\hat a_H\hat a_H\big]&=\eta_H\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle=\eta_H\,\mu S_4,
\qquad
\operatorname{Tr}\!\big[\rho'\,\hat a_V\hat a_V\big]=\eta_V\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle=-\eta_V\,\mu S_4 .
\end{aligned}
\tag{34}
$$

In words: every factor $\hat a_H$ or $\hat a_H^{\dagger}$ in an expectation value brings a $\sqrt{\eta_H}$, and every $\hat a_V$ or $\hat a_V^{\dagger}$ brings a $\sqrt{\eta_V}$. A pair correlation between $H$ and $V$ survives only if both photons are detected, which has amplitude factor $\sqrt{\eta_H\eta_V}$.

<span id="sigmaQ_prime"></span>

## The lossy matrix $\sigma_Q'$

Putting (34) into the pattern [(6)](covariance_matrix.md#eq6), with $\operatorname{Tr}\!\big[\rho'\,\hat a_i\hat a_i^{\dagger}\big]=1+\operatorname{Tr}\!\big[\rho'\,\hat a_i^{\dagger}\hat a_i\big]$:

<span id="eq35a"></span>

$$
\sigma_Q'=
\begin{pmatrix}
1+\nu\eta_H & 0 & \mu\eta_H S_4 & -\mu\sqrt{\eta_H\eta_V}\,C_4\\
0 & 1+\nu\eta_V & -\mu\sqrt{\eta_H\eta_V}\,C_4 & -\mu\eta_V S_4\\
\mu\eta_H S_4 & -\mu\sqrt{\eta_H\eta_V}\,C_4 & 1+\nu\eta_H & 0\\
-\mu\sqrt{\eta_H\eta_V}\,C_4 & -\mu\eta_V S_4 & 0 & 1+\nu\eta_V
\end{pmatrix}
=
\begin{pmatrix}
A & B\\
B & A
\end{pmatrix}
\tag{35a}
$$

with the two $2\times2$ blocks

<span id="eq35b"></span>

$$
A=\begin{pmatrix}1+\nu\eta_H & 0\\ 0 & 1+\nu\eta_V\end{pmatrix}=\mathbb{1}+\nu(\mathbb{1}-D),
\qquad
B=\mu\begin{pmatrix}\eta_H S_4 & -\sqrt{\eta_H\eta_V}\,C_4\\ -\sqrt{\eta_H\eta_V}\,C_4 & -\eta_V S_4\end{pmatrix}.
\tag{35b}
$$

Setting $\eta_H=\eta_V=1$ gives back [(20)](covariance_matrix.md#eq20), and $\eta_H=\eta_V=0$ gives $\mathbb{1}$, the vacuum.

## References

<p id="ref-leonhardt1997">
[7] U. Leonhardt,
<em>Measuring the Quantum State of Light</em>, Cambridge University Press, Cambridge (1997).
</p>

<p id="ref-weedbrook2012">
[8] C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, S. Lloyd,
<em>Gaussian quantum information</em>, Rev. Mod. Phys. <strong>84</strong>, 621 (2012). Available: https://arxiv.org/abs/1110.3234
</p>
