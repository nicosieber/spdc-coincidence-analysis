# Coincidence probability and the Torontonian

So far only $P^{(\eta_H,\eta_V)}(0,0)$, the probability that *neither* detector clicks, has been computed. The experiment counts **coincidences**, i.e. events where *both* detectors click. This page shows that the same matrix $\sigma_Q'$ also gives the coincidence probability. It proceeds in four parts:

1. **Inclusion–exclusion:** write the coincidence probability through three no-click probabilities. One of them is [(46)](determinant.md#eq46); two are new.
2. **Quesada's $Q$-function derivation** of the same formula. Besides confirming it, it shows *what* the two new terms are in terms of $Q$: heights at the origin of its marginals.
3. **No click in one detector:** evaluate these two terms as $1/\sqrt{\det}$ of a $2\times2$ part of $\sigma_Q'$.
4. **Result:** assemble $P_{\mathrm{cc}}$ and recognise it as the Torontonian of <a href="#ref-quesada2018">[2]</a>.

## From clicks to no-clicks (inclusion–exclusion)

A bucket detector has two outcomes, "no click" with POVM element $\Pi_0^{(\eta)}=(1-\eta)^{\hat n}$ and "click" with $\Pi_{\text{click}}^{(\eta)}=\mathbb{1}-\Pi_0^{(\eta)}$ (see [POVM](../theory/povm.md#formula_P_cc_loss)). A coincidence is a click in both detectors. Multiplying out the product of the two click elements:

<span id="eq48"></span>

$$
\begin{aligned}
P_{\mathrm{cc}}
&=\langle\Psi\rvert\left(\mathbb{1}-\Pi_0^{(\eta_H)}\right)\otimes\left(\mathbb{1}-\Pi_0^{(\eta_V)}\right)\lvert\Psi\rangle\\
&=1-\underbrace{\langle\Psi\rvert\Pi_0^{(\eta_H)}\otimes\mathbb{1}\lvert\Psi\rangle}_{P_H^{(\eta_H)}(0)}
-\underbrace{\langle\Psi\rvert\mathbb{1}\otimes\Pi_0^{(\eta_V)}\lvert\Psi\rangle}_{P_V^{(\eta_V)}(0)}
+\underbrace{\langle\Psi\rvert\Pi_0^{(\eta_H)}\otimes\Pi_0^{(\eta_V)}\lvert\Psi\rangle}_{P^{(\eta_H,\eta_V)}(0,0)} .
\end{aligned}
\tag{48}
$$

This is equation (16) of [POVM](../theory/povm.md#formula_P_cc_loss). The probability of "both click" is written entirely through probabilities of "no click": "no click in $H$" (whatever $V$ does), "no click in $V$" (whatever $H$ does), and "no click in either". This rewriting is called *inclusion–exclusion*. The last term is [(46)](determinant.md#eq46). The first two, $P_H^{(\eta_H)}(0)$ and $P_V^{(\eta_V)}(0)$, are still missing.

<span id="cc_quesada"></span>

## The same formula from the $Q$ function (Quesada's derivation)

Quesada, Arrazola and Killoran <a href="#ref-quesada2018">[2]</a> obtain (48) without operator algebra: they write every click probability as an integral over the $Q$ function. Their argument is reproduced here for two detectors, because it also shows how to compute the missing terms. Equation numbers in square brackets, e.g. [2, Eq. (9)], refer to that paper. Part 1 treats ideal detectors and an arbitrary state; Part 2 adds the efficiencies.

### Part 1: ideal detectors, arbitrary state

**Step (a): ideal detectors.** An ideal bucket detector clicks whenever at least one photon arrives. Its POVM elements are [2, Eq. (3)]

$$
\Pi_0=\lvert 0\rangle\langle 0\rvert,
\qquad
\Pi_1=\mathbb{1}-\lvert 0\rangle\langle 0\rvert
$$

for "no click" and "click". (These are $\Pi_0^{(\eta)}$ and $\Pi_{\text{click}}^{(\eta)}$ at $\eta=1$, since $(1-1)^{\hat n}=\lvert 0\rangle\langle 0\rvert$.)

**Step (b): write each POVM element as a mixture of coherent-state projectors.** Any such operator can be written as

$$
\Pi=\int d^2\alpha\;P_\Pi(\alpha)\,\lvert\alpha\rangle\langle\alpha\rvert
$$

with a weight function $P_\Pi(\alpha)$ (its Glauber–Sudarshan $P$ function <a href="#ref-cahill1969">[6]</a>, <a href="#ref-leonhardt1997">[7, Sec. 3.2.2]</a>). For the two elements, the weights can be read off directly:

- $\lvert 0\rangle\langle 0\rvert$ is the coherent-state projector at $\alpha=0$, so its weight is concentrated at the origin: $P_0(\alpha)=\delta^{(2)}(\alpha)$. Indeed $\int d^2\alpha\,\delta^{(2)}(\alpha)\lvert\alpha\rangle\langle\alpha\rvert=\lvert 0\rangle\langle 0\rvert$.
- $\mathbb{1}=\int\frac{d^2\alpha}{\pi}\lvert\alpha\rangle\langle\alpha\rvert$ by the resolution of the identity (equation (11) of [Coherent states](../concepts_and_foundations/coherent_states.md#eq:coherent_identity)), so its weight is the constant $1/\pi$.
- Hence $\Pi_1=\mathbb{1}-\lvert 0\rangle\langle 0\rvert$ has $P_1(\alpha)=\frac{1}{\pi}-\delta^{(2)}(\alpha)$.

These are [2, Eqs. (10a), (10b)].

**Step (c): a probability is an integral over $Q$.** For a two-mode state $\rho$ with $Q$ function $Q_\rho(\boldsymbol\alpha)=\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle/\pi^2$ [(6)](covariance_matrix.md#eq6), and one POVM element per detector,

$$
\begin{aligned}
\operatorname{Tr}\!\left[\rho\,\Pi^{H}\otimes\Pi^{V}\right]
&=\int d^2\alpha_H\,d^2\alpha_V\;P^{H}(\alpha_H)\,P^{V}(\alpha_V)\;\operatorname{Tr}\!\left[\rho\,\lvert\alpha_H,\alpha_V\rangle\langle\alpha_H,\alpha_V\rvert\right]\\
&=\int d^2\alpha_H\,d^2\alpha_V\;P^{H}(\alpha_H)\,P^{V}(\alpha_V)\;\langle\alpha_H,\alpha_V\rvert\rho\lvert\alpha_H,\alpha_V\rangle\\
&=\pi^2\int d^2\alpha_H\,d^2\alpha_V\;P^{H}(\alpha_H)\,P^{V}(\alpha_V)\;Q_\rho(\alpha_H,\alpha_V).
\end{aligned}
$$

This is [2, Eq. (9)] for two modes.

**Step (d): coincidence = both weights are $P_1$.** For a click in both detectors:

$$
P_{\mathrm{cc}}=\pi^2\int d^2\alpha_H\,d^2\alpha_V\;\left(\frac{1}{\pi}-\delta^{(2)}(\alpha_H)\right)\left(\frac{1}{\pi}-\delta^{(2)}(\alpha_V)\right)Q_\rho(\alpha_H,\alpha_V).
$$

Multiplying out the bracket gives four integrals:

$$
\begin{aligned}
P_{\mathrm{cc}}
&=\underbrace{\pi^2\cdot\frac{1}{\pi^2}\int d^2\alpha_H\,d^2\alpha_V\;Q_\rho(\alpha_H,\alpha_V)}_{\text{(i)}}
\;-\;\underbrace{\pi^2\cdot\frac{1}{\pi}\int d^2\alpha_H\,d^2\alpha_V\;\delta^{(2)}(\alpha_V)\,Q_\rho(\alpha_H,\alpha_V)}_{\text{(ii)}}\\
&\quad-\;\underbrace{\pi^2\cdot\frac{1}{\pi}\int d^2\alpha_H\,d^2\alpha_V\;\delta^{(2)}(\alpha_H)\,Q_\rho(\alpha_H,\alpha_V)}_{\text{(iii)}}
\;+\;\underbrace{\pi^2\int d^2\alpha_H\,d^2\alpha_V\;\delta^{(2)}(\alpha_H)\,\delta^{(2)}(\alpha_V)\,Q_\rho(\alpha_H,\alpha_V)}_{\text{(iv)}} .
\end{aligned}
$$

**Step (e): identify each term.** The delta functions set the corresponding amplitude to zero, and each term turns out to be a *vacuum probability* of $\rho$.

- (i) $=\int Q_\rho=1$, by normalization of $Q_\rho$.
- (ii) $=\pi\int d^2\alpha_H\,Q_\rho(\alpha_H,0)$. Integrating over $\alpha_H$ removes mode $H$. With the one-mode resolution of the identity, $\int\frac{d^2\alpha_H}{\pi}\langle\alpha_H\rvert\rho\lvert\alpha_H\rangle=\operatorname{Tr}_H\rho=\rho_V$, the reduced state of mode $V$. So

    $$
    \pi\int d^2\alpha_H\,Q_\rho(\alpha_H,0)=\frac{1}{\pi}\int d^2\alpha_H\,\langle\alpha_H,0\rvert\rho\lvert\alpha_H,0\rangle=\langle 0\rvert\rho_V\lvert 0\rangle=:p_V(0),
    $$

    the probability that mode $V$ is empty.

- (iii) $=\langle 0\rvert\rho_H\lvert 0\rangle=:p_H(0)$, in the same way with $H$ and $V$ swapped.
- (iv) $=\pi^2\,Q_\rho(0,0)=\langle 0,0\rvert\rho\lvert 0,0\rangle=:p(0,0)$, by [(7)](covariance_matrix.md#eq7).

Therefore, for ideal detectors and any state,

$$
P_{\mathrm{cc}}=1-p_V(0)-p_H(0)+p(0,0).
$$

The inclusion–exclusion structure comes from multiplying out $\left(\frac{1}{\pi}-\delta^{(2)}\right)\left(\frac{1}{\pi}-\delta^{(2)}\right)$. Each $\frac1\pi$ ("anything may happen in this detector") integrates the mode out. Each $\delta^{(2)}$ ("no click") evaluates it at $\alpha=0$. For $N$ detectors the same expansion is the identity $\prod_{k=1}^{N}(1-x_k)=\sum_{Z}(-1)^{|Z|}\prod_{i\in Z}x_i$ that [2, Eq. (A7)] uses.

### Part 2: detector efficiency

**Step (f): include the detector efficiencies.** By [Detector efficiency](detector_efficiency.md), a detector with efficiency $\eta$ is an ideal detector behind a beam splitter of transmissivity $\eta$. The real experiment is therefore Part 1 applied to the state *after* the beam splitters, $\rho=\rho'$ of [(32)](detector_efficiency.md#eq32). By [(31)](detector_efficiency.md#eq31), each vacuum probability of $\rho'$ is the corresponding lossy no-click probability of the original state $\lvert\Psi\rangle$:

$$
\begin{aligned}
p(0,0)\big|_{\rho'}&=\langle 0,0\rvert\rho'\lvert 0,0\rangle=\langle\Psi\rvert(1-\eta_H)^{\hat n_H}(1-\eta_V)^{\hat n_V}\lvert\Psi\rangle=P^{(\eta_H,\eta_V)}(0,0),\\
p_H(0)\big|_{\rho'}&=\langle 0\rvert\rho'_H\lvert 0\rangle=\langle\Psi\rvert(1-\eta_H)^{\hat n_H}\lvert\Psi\rangle=P_H^{(\eta_H)}(0),\\
p_V(0)\big|_{\rho'}&=\langle 0\rvert\rho'_V\lvert 0\rangle=\langle\Psi\rvert(1-\eta_V)^{\hat n_V}\lvert\Psi\rangle=P_V^{(\eta_V)}(0).
\end{aligned}
$$

For the single-mode lines, only the beam splitter in front of that mode matters. The one in front of the other mode acts on a mode that is traced out and does not change the reduced state. Inserted into the result of Part 1, this is exactly (48).

**What the derivation adds.** Step (e) also says *how* each term is obtained from the $Q$ function of $\rho'$:

- $P^{(\eta_H,\eta_V)}(0,0)$ is the height of $Q_{\rho'}$ at the origin. This is what [Covariance matrix and vacuum probability](covariance_matrix.md#eq12) evaluated: $1/\sqrt{\det\sigma_Q'}$.
- $P_H^{(\eta_H)}(0)$ and $P_V^{(\eta_V)}(0)$ are heights at the origin of the **marginals** of $Q_{\rho'}$, i.e. of $Q_{\rho'}$ integrated over the other mode. These are evaluated next.

## No click in one detector

Take $P_H^{(\eta_H)}(0)=\langle 0\rvert\rho'_H\lvert 0\rangle$. Its $Q$ function is the marginal from step (e),

$$
Q_H(\alpha_H)=\frac{1}{\pi}\langle\alpha_H\rvert\rho'_H\lvert\alpha_H\rangle=\int d^2\alpha_V\;Q_{\rho'}(\alpha_H,\alpha_V).
$$

Integrating a bell curve over some of its variables gives again a bell curve in the remaining ones, whose covariance matrix is the corresponding part of the full one ([Marginals](../concepts_and_foundations/gaussian_peak_height.md#gauss:marginal)). Quantum mechanically: expectation values of operators acting only on mode $H$ are the same in $\rho'$ and in $\rho'_H$. So the covariance matrix of $Q_H$, built by the rule [(9)](covariance_matrix.md#eq9) for one mode, consists of those entries of $\sigma_Q'$ that contain only $\hat a_H$ and $\hat a_H^{\dagger}$. These are the entries in rows and columns $1$ and $3$ of [(35a)](detector_efficiency.md#eq35a):

$$
\sigma_Q'^{(H)}=
\begin{pmatrix}
\operatorname{Tr}\!\big[\rho'\,\hat a_H\hat a_H^{\dagger}\big] & \operatorname{Tr}\!\big[\rho'\,\hat a_H\hat a_H\big]\\
\operatorname{Tr}\!\big[\rho'\,\hat a_H^{\dagger}\hat a_H^{\dagger}\big] & \operatorname{Tr}\!\big[\rho'\,\hat a_H\hat a_H^{\dagger}\big]
\end{pmatrix}
=
\begin{pmatrix}
1+\nu\eta_H & \mu\eta_H S_4\\
\mu\eta_H S_4 & 1+\nu\eta_H
\end{pmatrix}.
$$

The one-mode version of [(11)](covariance_matrix.md#eq11)–[(12)](covariance_matrix.md#eq12), with $\pi$ instead of $\pi^2$, then gives

<span id="eq49"></span>

$$
P_H^{(\eta_H)}(0)=\pi\,Q_H(0)=\frac{1}{\sqrt{\det\sigma_Q'^{(H)}}}
=\frac{1}{\sqrt{(1+\nu\eta_H)^2-\mu^2\eta_H^2S_4^2}}
=\frac{1-\lambda^2}{\sqrt{\big(1-\lambda^2t_H\big)^2-\lambda^2\eta_H^2\sin^2(4\vartheta)}} .
\tag{49}
$$

The last form follows by multiplying the determinant by $(1-\lambda^2)^2$, using $(1-\lambda^2)(1+\nu\eta_H)=1-\lambda^2+\lambda^2\eta_H=1-\lambda^2t_H$ and $(1-\lambda^2)\mu=\lambda$.

For mode $V$, rows and columns $2$ and $4$ of [(35a)](detector_efficiency.md#eq35a) give

$$
\sigma_Q'^{(V)}=
\begin{pmatrix}
1+\nu\eta_V & -\mu\eta_V S_4\\
-\mu\eta_V S_4 & 1+\nu\eta_V
\end{pmatrix},
\qquad
P_V^{(\eta_V)}(0)=\frac{1}{\sqrt{\det\sigma_Q'^{(V)}}}
=\frac{1-\lambda^2}{\sqrt{\big(1-\lambda^2t_V\big)^2-\lambda^2\eta_V^2\sin^2(4\vartheta)}} .
$$

The minus signs drop out because the off-diagonal entry appears squared.

**Check: switch off the other detector.** A detector with $\eta_V=0$ never clicks, since $(1-0)^{\hat n_V}=\mathbb{1}$. So $P_H^{(\eta_H)}(0)$ must also equal [(46)](determinant.md#eq46) at $\eta_V=0$, i.e. $t_V=1$. Setting $t_V=1$ and $\eta_V=0$ in (46) indeed gives (49).

**What one arm alone looks like.**

- At $\vartheta=0$ ($S_4=0$): $P_H^{(\eta_H)}(0)=\frac{1-\lambda^2}{1-\lambda^2t_H}=\frac{1}{1+\nu\eta_H}$. Each arm alone is a round cloud with no squeezing, i.e. thermal light with mean photon number $\nu$. Indeed, for thermal light $\sum_n(1-\eta)^n\frac{\nu^n}{(1+\nu)^{n+1}}=\frac{1}{1+\eta\nu}$.
- At $\vartheta=\pi/8$ ($S_4=1$): $P_H^{(\eta_H)}(0)=\frac{1-\lambda^2}{\sqrt{(1-\lambda^2t_H)^2-\lambda^2\eta_H^2}}$, the no-click probability of a single-mode squeezed state.

## The coincidence probability

Inserting [(46)](determinant.md#eq46), (49) and its $V$ counterpart into (48):

<span id="eq50"></span>

$$
P_{\mathrm{cc}}=1-\frac{1}{\sqrt{\det\sigma_Q'^{(H)}}}-\frac{1}{\sqrt{\det\sigma_Q'^{(V)}}}+\frac{1}{\sqrt{\det\sigma_Q'}},
\tag{50}
$$

or written out,

$$
\begin{aligned}
P_{\mathrm{cc}}=1
&-\frac{1-\lambda^2}{\sqrt{\big(1-\lambda^2t_H\big)^2-\lambda^2\eta_H^2\sin^2(4\vartheta)}}
-\frac{1-\lambda^2}{\sqrt{\big(1-\lambda^2t_V\big)^2-\lambda^2\eta_V^2\sin^2(4\vartheta)}}\\
&+\frac{1-\lambda^2}{\sqrt{\big(1-\lambda^2t_Ht_V\big)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}} .
\end{aligned}
$$

All three determinants come from **one** matrix, $\sigma_Q'$: the full matrix and its two one-mode parts.

## The Torontonian

Quesada, Arrazola and Killoran <a href="#ref-quesada2018">[2]</a> package this calculation for any number of threshold detectors. In their notation, $\Sigma$ is the covariance matrix of the $Q$ function, i.e. our $\sigma_Q'$. The probability that exactly the detectors in a set $S$ click and all others stay dark is their Eqs. (11)–(12):

$$
p(S)=\frac{\operatorname{Tor}\big[O_{(S)}\big]}{\sqrt{\det\Sigma}},
\qquad
O_{(S)}=\mathbb{1}-\big(\Sigma^{-1}\big)_{(S)},
\qquad
\operatorname{Tor}(A)=\sum_{Z\in P([N])}(-1)^{|Z|}\frac{1}{\sqrt{\det\big(\mathbb{1}-A_{(Z)}\big)}} .
$$

Here $(\cdot)_{(S)}$ keeps only the rows and columns belonging to the modes in $S$, in each of the four blocks of the matrix. $N$ is the number of modes in $S$, and $P([N])$ is the set of all subsets $Z$ of these modes. The sum is called the **Torontonian**.

**It is the same as (50).** For a coincidence both detectors click, $S=\{H,V\}$, so $O=\mathbb{1}-\sigma_Q'^{-1}$ and $Z$ runs over $\emptyset$, $\{H\}$, $\{V\}$ and $\{H,V\}$. In each term, $\mathbb{1}-O_{(Z)}=(\sigma_Q'^{-1})_{(Z)}$ is a part of the *inverse* matrix. Jacobi's complementary-minor identity (equation (3) of [Block-matrix identities](../concepts_and_foundations/block_matrices.md#block:jacobi)) relates a part of the inverse to the complementary part of the matrix itself:

$$
\det\big(\sigma_Q'^{-1}\big)_{(Z)}=\frac{\det\sigma_Q'^{(\text{modes not in }Z)}}{\det\sigma_Q'} .
$$

Dividing each term of the Torontonian by $\sqrt{\det\sigma_Q'}$ therefore gives:

| $Z$ | sign $(-1)^{\lvert Z\rvert}$ | term $\dfrac{1}{\sqrt{\det\sigma_Q'}\sqrt{\det(\sigma_Q'^{-1})_{(Z)}}}$ | meaning |
|---|---|---|---|
| $\emptyset$ | $+$ | $\dfrac{1}{\sqrt{\det\sigma_Q'}}$ | $P^{(\eta_H,\eta_V)}(0,0)$ |
| $\{H\}$ | $-$ | $\dfrac{1}{\sqrt{\det\sigma_Q'^{(V)}}}$ | $P_V^{(\eta_V)}(0)$ |
| $\{V\}$ | $-$ | $\dfrac{1}{\sqrt{\det\sigma_Q'^{(H)}}}$ | $P_H^{(\eta_H)}(0)$ |
| $\{H,V\}$ | $+$ | $1$ | total probability |

For $\emptyset$ the determinant of an empty matrix is $1$. For $\{H,V\}$, $\det\sigma_Q'^{-1}\cdot\det\sigma_Q'=1$. Summing the four rows gives exactly (50). So the Torontonian is the inclusion–exclusion sum (48), written with the inverse matrix $\sigma_Q'^{-1}$ so that one matrix $O$ serves every click pattern. For $N$ detectors it has $2^N$ terms, one per subset of dark detectors. (The paper also relates the Torontonian to the hafnians that give photon-*number* probabilities, its Eqs. (13)–(14). That connection is not needed here.)

The [numerical check](../dashboard/comparison.md#numerical-check) confirms (50) against `thewalrus`'s Torontonian <a href="#ref-gupt2019">[4]</a> at five random parameter sets.

## References

<p id="ref-quesada2018">
[2] N. Quesada, J. M. Arrazola, N. Killoran,
<em>Gaussian boson sampling using threshold detectors</em>, Phys. Rev. A <strong>98</strong>, 062322 (2018). Available: https://arxiv.org/abs/1807.01639
</p>

<p id="ref-gupt2019">
[4] B. Gupt, J. Izaac, N. Quesada,
<em>The Walrus: a library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling</em>, J. Open Source Softw. <strong>4</strong>(44), 1705 (2019). Documentation: https://the-walrus.readthedocs.io
</p>

<p id="ref-cahill1969">
[6] K. E. Cahill, R. J. Glauber,
<em>Density Operators and Quasiprobability Distributions</em>, Phys. Rev. <strong>177</strong>, 1882 (1969). Available: https://doi.org/10.1103/PhysRev.177.1882
</p>

<p id="ref-leonhardt1997">
[7] U. Leonhardt,
<em>Measuring the Quantum State of Light</em>, Cambridge University Press, Cambridge (1997).
</p>
