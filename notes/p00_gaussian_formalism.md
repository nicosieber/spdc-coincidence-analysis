# $P^{(\eta_H,\eta_V)}(0,0)$ in Quesada's Gaussian formalism

> Standalone note. It is not part of the zensical site (it lives outside `docs/`).
> Relative links point into `docs/` so they work when browsing the repository.

The [main derivation](../docs/theory/cc_derivation.md) evaluates

$$
P^{(\eta_H,\eta_V)}(0,0)=\langle \Psi \rvert\left(1-\eta_H\right)^{\hat{n}_H}\otimes \left(1-\eta_V\right)^{\hat{n}_V}\lvert \Psi \rangle
\tag{1}
$$

by moving $t^{\hat n}$ through the exponential, inserting coherent states and doing a complex Gaussian integral. This note gets the same result with the method N. Quesada and co-workers use for Gaussian boson sampling with threshold ("click") detectors <a href="#ref-hamilton2017">[1]</a>, <a href="#ref-quesada2018">[2]</a>, <a href="#ref-kruse2019">[3]</a>. The same method is implemented in the Python library `thewalrus` <a href="#ref-gupt2019">[4]</a>.

Everything is written with the same objects as the docs: the vector $\mathbf{\hat a}=(\hat a_H,\hat a_V)^T$, the matrix $M$, the matrix $D$ and coherent states $\lvert\alpha_H,\alpha_V\rangle$. No quadratures ($\hat x,\hat p$) and no Wigner functions are needed.

## Outline of Quesada's approach

### The core idea

The main derivation works with the **state vector** $\lvert\Psi\rangle$: it carries the whole exponential $e^{\frac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^TM\mathbf{\hat a^{\dagger}}}$ through every step. Quesada's approach rests on two observations that make this unnecessary.

1. **The state is fixed by its covariance matrix.** For states like the TMSV (Gaussian states), all information is contained in the expectation values of products of *two* ladder operators: $\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle$, $\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle$, $\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle$, … These numbers are collected in a single $4\times4$ matrix $\sigma_Q$, the (Husimi) **covariance matrix**. Every later step works with this matrix instead of the state vector.
2. **"No click" is a determinant.** The probability that none of the detectors clicks is given by one universal formula, $P(0,0)=1/\sqrt{\det\sigma_Q}$. Click probabilities (coincidences) follow from such no-click probabilities by inclusion-exclusion.

The physics of the setup (source, HWP, detector efficiency) thus only enters through which numbers stand in $\sigma_Q$.

### The steps

| Step | What is done | Input | Output | Section |
|---|---|---|---|---|
| 1 | Compute the second-order expectation values (covariance matrix) of the state behind the HWP | $\lvert\Psi\rangle$, i.e. $\lambda$ and $M$ | $4\times4$ matrix $\sigma_Q$, eq. (20) | [Step 1](#step1) |
| 2 | Justify the vacuum formula $P(0,0)=1/\sqrt{\det\sigma_Q}$ | coherent states, the $Q$ function | eq. (26) | [Step 2](#why) |
| 3 | Include the detector efficiency as a beam splitter in front of a perfect detector | $\sigma_Q$, $\eta_H$, $\eta_V$ | lossy matrix $\sigma_Q'$, eq. (35a) | [Step 3](#step3) |
| 4 | Evaluate $\det\sigma_Q'$ | $\sigma_Q'$ | $P^{(\eta_H,\eta_V)}(0,0)$, eq. (46) | [Step 4](#step4) |
| 5 | Write coincidences through no-click probabilities and evaluate them | $\sigma_Q'$ and its one-mode parts | $P_{\mathrm{cc}}$, eq. (50) | [Step 5](#coincidence) |

In more detail:

1. **Covariance matrix.** One relation, $\mathbf{\hat a}\lvert\Psi\rangle=\lambda M\mathbf{\hat a^{\dagger}}\lvert\Psi\rangle$, lets every second-order expectation value be computed without expanding $\lvert\Psi\rangle$ in Fock states. The result is remarkably simple: the photon-number matrix is $\nu\mathbb{1}$ and the pair-correlation matrix is $\mu M$, with $\nu$ and $\mu$ depending only on $\lambda$.
2. **Vacuum formula.** $\sigma_Q$ is exactly the covariance matrix of the probability distribution $Q(\boldsymbol\alpha)=\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle/\pi^2$ built from coherent states. For a bell-shaped $Q$, the height at $\boldsymbol\alpha=0$ is fixed by its spread, $\pi^2Q(0)=1/\sqrt{\det\sigma_Q}$, and $\pi^2Q(0)$ is the vacuum probability. This is the one general result the method imports.
3. **Detector efficiency.** The no-click element $(1-\eta)^{\hat n}$ of the lossy POVM equals the vacuum probability behind a beam splitter of transmissivity $\eta$. On the covariance matrix, this beam splitter acts very simply: every $\hat a_H$ or $\hat a_H^{\dagger}$ in an expectation value brings a factor $\sqrt{\eta_H}$, and likewise for $V$. No operator ordering or conjugation through exponentials is needed.
4. **Determinant.** $\sigma_Q'$ has the block form $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$, so its determinant splits into two $2\times2$ determinants, $\det(A+B)\det(A-B)$. The result is $\det\sigma_Q'=\det(\mathbb{1}-\lambda^2MDMD)/(1-\lambda^2)^2$, i.e. your formula.
5. **Coincidences.** "Both click" is rewritten through "no click" probabilities (inclusion–exclusion). Each of them is the height of a bell curve at the origin: of the full $Q$ function, or of its one-mode marginals, whose covariance matrices are $2\times2$ parts of $\sigma_Q'$. The resulting formula is what Quesada et al. call the **Torontonian**.

A side-by-side comparison with the main derivation is at the [end of the note](#comparison).

## Notation

As in equation (18) of [TMSV](../docs/theory/tmsv.md#formula:tmsv_as_exp_2):

$$
\lvert \Psi \rangle=\Lambda\, e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}}\lvert 0,0 \rangle,
\qquad
\Lambda=\sqrt{1-\lambda^2},
\qquad
\mathbf{\hat a}=\begin{pmatrix}\hat a_H\\ \hat a_V\end{pmatrix},
\tag{2}
$$

with real $\lambda=\tanh r$. The matrix $M$ was defined in [TMSV](../docs/theory/tmsv.md) through $c=\cos(2\vartheta)$ and $s=\sin(2\vartheta)$, where $\vartheta$ is the HWP angle. Its entries simplify with the double-angle identities

$$
2cs=2\sin(2\vartheta)\cos(2\vartheta)=\sin(4\vartheta),
\qquad
s^2-c^2=\sin^2(2\vartheta)-\cos^2(2\vartheta)=-\cos(4\vartheta),
$$

the same identities the main derivation uses for $\det Q$. Since $\sin(4\vartheta)$ and $\cos(4\vartheta)$ appear in almost every matrix below, this note uses the **shorthand**

$$
\boxed{\;S_4:=\sin(4\vartheta),\qquad C_4:=\cos(4\vartheta)\;}
$$

The subscript $4$ refers to the angle $4\vartheta$. $S_4$ has nothing to do with the operator $S=t_H^{\hat n_H}t_V^{\hat n_V}$ of the main derivation. With this shorthand,

$$
M=
\begin{pmatrix}
2cs & s^2-c^2\\
s^2-c^2 & -2cs
\end{pmatrix}
=
\begin{pmatrix}
S_4 & -C_4\\
-C_4 & -S_4
\end{pmatrix}.
\tag{3}
$$

The only property of $M$ used below is

$$
M^2=
\begin{pmatrix}
S_4^2+C_4^2 & -S_4C_4+C_4S_4\\
-C_4S_4+S_4C_4 & C_4^2+S_4^2
\end{pmatrix}
=\mathbb{1}.
\tag{4}
$$

The detector matrices are

$$
D=\begin{pmatrix}t_H&0\\0&t_V\end{pmatrix}=\begin{pmatrix}1-\eta_H&0\\0&1-\eta_V\end{pmatrix},
\qquad
\mathbb{1}-D=\begin{pmatrix}\eta_H&0\\0&\eta_V\end{pmatrix}.
\tag{5}
$$

$D$ holds the probabilities that a photon is *missed*, and $\mathbb{1}-D$ the probabilities that it is *detected*. In this note the second one appears.

<span id="step1"></span>

## Step 1: the covariance matrix of $\lvert\Psi\rangle$

### Why the covariance matrix?

Before computing anything: why should expectation values of two ladder operators be the right thing to compute at all?

**A word on terminology.** In probability theory, averages like $\langle x\rangle$ and $\langle x^2\rangle$ are called the first and second *moments* of a distribution. The papers on Gaussian states mostly speak of the **mean** (or displacement) and the **covariance matrix** instead, and this note follows them. The only place the word "moment" appears is the classical analogy below.

**Classical picture.** Take a random variable $x$ with a bell-shaped (Gaussian) distribution centred at $0$:

$$
p(x)=\frac{1}{\sqrt{2\pi\langle x^2\rangle}}\,e^{-x^2/2\langle x^2\rangle}.
$$

The whole curve is fixed by **one number**, the second moment $\langle x^2\rangle$. In particular its height at the centre, $p(0)=1/\sqrt{2\pi\langle x^2\rangle}$, is fixed by it: the wider the curve, the lower its peak. With several variables $x_1,x_2,\dots$ one needs all second moments $\langle x_ix_j\rangle$, collected in the covariance matrix $\Sigma$, and the height at the centre becomes $1/\sqrt{\det\Sigma}$ (up to factors of $2\pi$). The determinant arises in two steps.

*Independent variables: the determinant is a product of variances.* If $x_1$ and $x_2$ are independent, the joint distribution is a product of two 1D bell curves:

$$
p(x_1,x_2)=\frac{e^{-x_1^2/2\langle x_1^2\rangle}}{\sqrt{2\pi\langle x_1^2\rangle}}\cdot\frac{e^{-x_2^2/2\langle x_2^2\rangle}}{\sqrt{2\pi\langle x_2^2\rangle}},
\qquad
p(0,0)=\frac{1}{2\pi\sqrt{\langle x_1^2\rangle\langle x_2^2\rangle}}=\frac{1}{2\pi\sqrt{\det\Sigma}},
\qquad
\Sigma=\begin{pmatrix}\langle x_1^2\rangle&0\\0&\langle x_2^2\rangle\end{pmatrix}.
$$

For a diagonal $\Sigma$, "$\det$" simply means "multiply all variances".

*Correlated variables: rotate until they are independent.* If $\langle x_1x_2\rangle\neq0$, the bell curve is a tilted ellipse with $\Sigma=\left(\begin{smallmatrix}\langle x_1^2\rangle&\langle x_1x_2\rangle\\\langle x_1x_2\rangle&\langle x_2^2\rangle\end{smallmatrix}\right)$. Rotating the coordinate axes onto the axes of the ellipse makes the variables independent, so the previous case applies. A rotation keeps the origin fixed (same height at the centre), keeps areas fixed (same normalization) and keeps the determinant fixed. Hence

$$
p(0,0)=\frac{1}{2\pi\sqrt{\det\Sigma}},
\qquad
\det\Sigma=\langle x_1^2\rangle\langle x_2^2\rangle-\langle x_1x_2\rangle^2 ,
$$

holds for any covariance matrix. Mathematically, this is the normalization integral $\int d^nx\,e^{-\frac12x^T\Sigma^{-1}x}=(2\pi)^{n/2}\sqrt{\det\Sigma}$, the same Gaussian integral as in the [main derivation](../docs/theory/cc_derivation.md#GIntegral).

*Intuition.* Correlations ($\langle x_1x_2\rangle\neq0$) squeeze the cloud of points into a thinner ellipse that covers less area. Since the total probability stays $1$, the peak must be higher. A smaller determinant means a higher peak, and a larger determinant (a wider cloud) means a lower peak.

**Quantum counterpart.** Step 2 shows that the state can be described by a probability distribution $Q(\alpha_H,\alpha_V)$ over coherent-state amplitudes. For our states this distribution is a bell curve centred at $\alpha=0$, and its height at the centre is exactly the no-click probability $P(0,0)$. So, as in the classical case:

$$
\text{covariance matrix of }Q\;\Longrightarrow\;\text{width of the bell curve}\;\Longrightarrow\;\text{height at }0\;=\;P(0,0).
$$

The entries of the covariance matrix of $Q$ are averages of products of two amplitudes, $\alpha_i\alpha_j$ and $\alpha_i\alpha_j^{*}$. These averages are expectation values of two ladder operators, e.g. $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$ and $\langle\Psi\rvert\hat a_i\hat a_j^{\dagger}\lvert\Psi\rangle$, eq. (23). This is why Step 1 computes expectation values of **pairs** of ladder operators, and nothing else.

**Which pairs?** With two modes, every product of two ladder operators is of one of four types:

$$
\hat a_i\hat a_j,\qquad
\hat a_i^{\dagger}\hat a_j^{\dagger},\qquad
\hat a_i^{\dagger}\hat a_j,\qquad
\hat a_i\hat a_j^{\dagger},
\qquad i,j\in\{H,V\},
$$

i.e. $4\times4=16$ numbers. Most of them are redundant:

- $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j^{\dagger}\lvert\Psi\rangle=\langle\Psi\rvert\hat a_j\hat a_i\lvert\Psi\rangle^{*}$, by taking the complex conjugate (adjoint) of the operator,
- $\langle\Psi\rvert\hat a_i\hat a_j^{\dagger}\lvert\Psi\rangle=\delta_{ij}+\langle\Psi\rvert\hat a_j^{\dagger}\hat a_i\lvert\Psi\rangle$, by the commutator $[\hat a_i,\hat a_j^{\dagger}]=\delta_{ij}$.

Written as one $4\times4$ matrix, with the rule "annihilation operators to the left of creation operators" (the reason for this rule follows in Step 2), all 16 expectation values form the covariance matrix

$$
\sigma_Q=
\begin{pmatrix}
\langle\Psi\rvert\hat a_H\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H^{\dagger}\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_H^{\dagger}\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V^{\dagger}\lvert\Psi\rangle
\end{pmatrix}.
\tag{6}
$$

Applying the two rules above to every entry rewrites it with only the types $\langle\Psi\rvert\hat a^{\dagger}\hat a\lvert\Psi\rangle$ and $\langle\Psi\rvert\hat a\hat a\lvert\Psi\rangle$:

$$
\sigma_Q=
\begin{pmatrix}
1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle & 1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*} & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*} & 1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle^{*} & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle^{*} & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle & 1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle
\end{pmatrix}.
$$

The lower half contains no new numbers: it repeats the upper half, complex-conjugated or reordered. So only eight expectation values have to be computed: the four $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j\lvert\Psi\rangle$ (upper-left $2\times2$ part) and the four $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$ (upper-right $2\times2$ part). Below they are abbreviated as the $2\times2$ matrices $N$ and $\mathcal{M}$ of (10). These are only names for these parts of the full matrix above. Single operators are not needed: $\langle\Psi\rvert\hat a_H\lvert\Psi\rangle=\langle\Psi\rvert\hat a_V\lvert\Psi\rangle=0$, because photons come in pairs and $\hat a$ changes the photon number by one. This means the bell curve is centred at $0$.

**What they mean physically.**

- $\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle=\langle\Psi\rvert\hat n_H\lvert\Psi\rangle$ is the mean photon number in arm $H$, the quantity a detector responds to. The off-diagonal $\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle$ measures coherence between the arms.
- $\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle$ is the amplitude for **removing a pair** of photons. It is zero for vacuum and thermal light, and nonzero here precisely because SPDC creates photons in pairs. (For laser light $\langle\alpha\rvert\hat a\hat a\lvert\alpha\rangle=\alpha^2$ is nonzero too, but only because $\langle\alpha\rvert\hat a\lvert\alpha\rangle=\alpha\neq0$. For our states $\langle\Psi\rvert\hat a\lvert\Psi\rangle=0$, so a nonzero $\langle\Psi\rvert\hat a\hat a\lvert\Psi\rangle$ is a genuine pair correlation.) It is the "squeezing" part of the state.

**Why not stay with $\lvert\Psi\rangle$?** The detector efficiency (Step 3) turns $\lvert\Psi\rangle$ into a mixed state, which no longer has the exponential form (2). The covariance matrix, by contrast, keeps its meaning and changes in a very simple way: its entries get multiplied by factors of $\sqrt{\eta}$.

### Why we look at $\hat a\lvert\Psi\rangle$

So Step 1 needs numbers like

$$
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle,
\qquad
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle,
\qquad
\dots
$$

The brute-force way is to expand $\lvert\Psi\rangle$ in Fock states and evaluate double sums over photon numbers for a general HWP angle. That works, but it is messy.

There is a shortcut. In every one of these expectation values, the **right-most operator is an annihilation operator acting directly on $\lvert\Psi\rangle$**. If we know what $\hat a_H\lvert\Psi\rangle$ and $\hat a_V\lvert\Psi\rangle$ are, we can replace them and the expectation value simplifies. The next subsection shows that removing a photon from $\lvert\Psi\rangle$ is the same as *adding* one, times $\lambda M$. Inserted into an expectation value, this turns it into a combination of *other* expectation values. This gives a small linear system of equations that yields all of them at once, eq. (12), without any Fock sums.

The idea is familiar from coherent states, where $\hat a\lvert\alpha\rangle=\alpha\lvert\alpha\rangle$ replaces the annihilation operator by a number. For the squeezed state $\lvert\Psi\rangle$ it is replaced by creation operators instead.

### The key relation

Call the exponent of (2) $\hat X$. Here $\mathbf{\hat a^{\dagger}}=(\hat a_H^{\dagger},\hat a_V^{\dagger})^T$ is the column of creation operators, and $(\mathbf{\hat a^{\dagger}})^T$ is the same entries as a row (a plain transpose, not a dagger). Row times $M$ times column is a sum over the four entries of (3), and the two off-diagonal terms are equal because $\hat a_H^{\dagger}\hat a_V^{\dagger}=\hat a_V^{\dagger}\hat a_H^{\dagger}$:

$$
\hat X:=\frac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^T M\mathbf{\hat a^{\dagger}}
=\frac{\lambda}{2}\sum_{i,j\in\{H,V\}}M_{ij}\,\hat a_i^{\dagger}\hat a_j^{\dagger}
=\frac{\lambda}{2}\left(S_4\,\hat a_H^{\dagger 2}-2C_4\,\hat a_H^{\dagger}\hat a_V^{\dagger}-S_4\,\hat a_V^{\dagger 2}\right).
\tag{7}
$$

Now commute $\hat a_H$ with each of the three terms. Everything follows from $[\hat a_H,\hat a_H^{\dagger}]=1$, $[\hat a_H,\hat a_V^{\dagger}]=0$ and the product rule $[\hat A,\hat B\hat C]=[\hat A,\hat B]\,\hat C+\hat B\,[\hat A,\hat C]$:

$$
\begin{aligned}
[\hat a_H,\hat a_H^{\dagger}\hat a_H^{\dagger}]
&=[\hat a_H,\hat a_H^{\dagger}]\,\hat a_H^{\dagger}+\hat a_H^{\dagger}\,[\hat a_H,\hat a_H^{\dagger}]
=\hat a_H^{\dagger}+\hat a_H^{\dagger}=2\hat a_H^{\dagger},\\
[\hat a_H,\hat a_H^{\dagger}\hat a_V^{\dagger}]
&=[\hat a_H,\hat a_H^{\dagger}]\,\hat a_V^{\dagger}+\hat a_H^{\dagger}\,[\hat a_H,\hat a_V^{\dagger}]
=\hat a_V^{\dagger}+0=\hat a_V^{\dagger},\\
[\hat a_H,\hat a_V^{\dagger}\hat a_V^{\dagger}]
&=[\hat a_H,\hat a_V^{\dagger}]\,\hat a_V^{\dagger}+\hat a_V^{\dagger}\,[\hat a_H,\hat a_V^{\dagger}]
=0 .
\end{aligned}
$$

The commutator is linear in its second argument: for numbers $c,d$,

$$
[\hat A,c\hat B+d\hat C]
=\hat A\,(c\hat B+d\hat C)-(c\hat B+d\hat C)\,\hat A
=c\,(\hat A\hat B-\hat B\hat A)+d\,(\hat A\hat C-\hat C\hat A)
=c\,[\hat A,\hat B]+d\,[\hat A,\hat C],
$$

using only that operator products distribute over sums and that numbers can be pulled out. So $[\hat a_H,\hat X]$ is the sum of the three commutators above, weighted with the coefficients of (7):

$$
[\hat a_H,\hat X]
=\frac{\lambda}{2}\left(S_4\cdot2\hat a_H^{\dagger}-2C_4\cdot\hat a_V^{\dagger}-S_4\cdot0\right)
=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right).
$$

For $\hat a_V$ the roles swap: $[\hat a_V,\hat a_H^{\dagger 2}]=0$, $[\hat a_V,\hat a_H^{\dagger}\hat a_V^{\dagger}]=\hat a_H^{\dagger}$ and $[\hat a_V,\hat a_V^{\dagger 2}]=2\hat a_V^{\dagger}$, so $[\hat a_V,\hat X]=\frac{\lambda}{2}\left(-2C_4\,\hat a_H^{\dagger}-S_4\cdot2\hat a_V^{\dagger}\right)$. Together:

$$
[\hat a_H,\hat X]=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right),
\qquad
[\hat a_V,\hat X]=\lambda\left(-C_4\,\hat a_H^{\dagger}-S_4\,\hat a_V^{\dagger}\right).
\tag{8}
$$

Now apply $\hat a_H$ to $\lvert\Psi\rangle=\Lambda e^{\hat X}\lvert 0,0\rangle$. Writing $\hat a_He^{\hat X}=[\hat a_H,e^{\hat X}]+e^{\hat X}\hat a_H$ and using $\hat a_H\lvert 0,0\rangle=0$:

$$
\hat a_H\lvert\Psi\rangle
=\Lambda\left([\hat a_H,e^{\hat X}]+e^{\hat X}\hat a_H\right)\lvert 0,0\rangle
=\Lambda\,[\hat a_H,e^{\hat X}]\lvert 0,0\rangle .
$$

It remains to evaluate $[\hat a_H,e^{\hat X}]$. This takes three steps.

**1. Expand the exponential.** Insert the series $e^{\hat X}=\sum_{n=0}^{\infty}\hat X^n/n!$. By the linearity of the commutator shown above, applied term by term to the series (with $c=1/n!$), the commutator can be taken inside the sum:

$$
[\hat a_H,e^{\hat X}]=\sum_{n=0}^{\infty}\frac{[\hat a_H,\hat X^n]}{n!} .
$$

**2. Commutator with a power.** The product rule for commutators, $[\hat A,\hat B\hat C]=[\hat A,\hat B]\,\hat C+\hat B\,[\hat A,\hat C]$, lets $\hat a_H$ act on one factor at a time. For $n=2$:

$$
[\hat a_H,\hat X\hat X]=[\hat a_H,\hat X]\,\hat X+\hat X\,[\hat a_H,\hat X].
$$

Now use that $[\hat a_H,\hat X]$ commutes with $\hat X$: by (8) it contains only creation operators, and so does $\hat X$. So $\hat X\,[\hat a_H,\hat X]=[\hat a_H,\hat X]\,\hat X$, and the two terms are equal:

$$
[\hat a_H,\hat X^2]=2\,[\hat a_H,\hat X]\,\hat X .
$$

For general $n$, the product rule gives $n$ terms, one for each factor $\hat X$ that the commutator "hits":

$$
[\hat a_H,\hat X^n]=\sum_{k=0}^{n-1}\hat X^{k}\,[\hat a_H,\hat X]\,\hat X^{n-1-k}
=n\,[\hat a_H,\hat X]\,\hat X^{n-1},
$$

where in each term $[\hat a_H,\hat X]$ was moved past the $\hat X^{k}$ in front of it. For $n=0$ the commutator vanishes, $[\hat a_H,\mathbb{1}]=0$.

**3. Sum the series.** Inserting step 2 into step 1:

$$
[\hat a_H,e^{\hat X}]
=\sum_{n=1}^{\infty}\frac{n\,[\hat a_H,\hat X]\,\hat X^{n-1}}{n!}
=[\hat a_H,\hat X]\sum_{n=1}^{\infty}\frac{\hat X^{n-1}}{(n-1)!}
=[\hat a_H,\hat X]\sum_{m=0}^{\infty}\frac{\hat X^{m}}{m!}
=[\hat a_H,\hat X]\,e^{\hat X}.
$$

The sum starts at $n=1$ because the $n=0$ term vanishes. Then $\frac{n}{n!}=\frac{1}{(n-1)!}$, and renaming $m=n-1$ turns the sum back into the full exponential series $\sum_{m=0}^{\infty}\hat X^m/m!=e^{\hat X}$.

This is the operator version of $\frac{d}{dx}e^{f(x)}=f'(x)\,e^{f(x)}$. The same holds for $\hat a_V$. Together with (8):

$$
\begin{aligned}
\hat a_H\lvert\Psi\rangle&=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right)\lvert\Psi\rangle,\\
\hat a_V\lvert\Psi\rangle&=\lambda\left(-C_4\,\hat a_H^{\dagger}-S_4\,\hat a_V^{\dagger}\right)\lvert\Psi\rangle,
\end{aligned}
\qquad\text{i.e.}\qquad
\mathbf{\hat a}\lvert\Psi\rangle=\lambda M\,\mathbf{\hat a^{\dagger}}\lvert\Psi\rangle .
\tag{9}
$$

Equation (9) says that an annihilation operator acting on $\lvert\Psi\rangle$ can be traded for creation operators. It is all that is needed to compute the covariance matrix.

**Check at $\vartheta=0$.** Here $S_4=0$ and $C_4=1$, and (9) reads $\hat a_H\lvert\Psi\rangle=-\lambda\,\hat a_V^{\dagger}\lvert\Psi\rangle$. At this angle the state is $\lvert\Psi\rangle=\Lambda\sum_n(-\lambda)^n\lvert n,n\rangle$ (see (17) below). Both sides can be evaluated in the Fock basis:

$$
\hat a_H\lvert\Psi\rangle=\Lambda\sum_{n}(-\lambda)^n\sqrt{n}\,\lvert n-1,n\rangle,
\qquad
-\lambda\,\hat a_V^{\dagger}\lvert\Psi\rangle=\Lambda\sum_{m}(-\lambda)^{m+1}\sqrt{m+1}\,\lvert m,m+1\rangle .
$$

Renaming $m=n-1$ in the second sum makes the two sides identical.

Physically, the photons of $\lvert\Psi\rangle$ come in $H$–$V$ pairs. Removing one $H$ photon leaves a state with one more $V$ photon than $H$ photons, which is the same as adding a $V$ photon to the pair state, up to the factor $-\lambda$. For other angles the HWP mixes $H$ and $V$, and $M$ keeps track of which photon is "added".

### The two blocks $N$ and $\mathcal{M}$

As motivated [above](#step1), the eight independent second-order expectation values are abbreviated by two $2\times2$ matrices:

$$
N=
\begin{pmatrix}
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle
\end{pmatrix},
\qquad
\mathcal{M}=
\begin{pmatrix}
\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle
\end{pmatrix},
\tag{10}
$$

$N$ holds photon numbers, with mean photon numbers on its diagonal. $\mathcal{M}$ holds the pair correlations created by SPDC. All other second-order expectation values are fixed by these through $[\hat a_i,\hat a_j^{\dagger}]=\delta_{ij}$ and complex conjugation.

#### One entry step by step

Each entry is computed with the same three moves:
1. replace the annihilator next to the ket by (9),
2. pull out the numbers $\lambda$, $S_4$, $C_4$,
3. rewrite the remaining expectation value with complex conjugation or the commutator.

**Photon-number type.** For $\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle$, step 3 uses $\langle\Psi\rvert\hat O^{\dagger}\lvert\Psi\rangle=\langle\Psi\rvert\hat O\lvert\Psi\rangle^{*}$ with $(\hat a_H^{\dagger}\hat a_V^{\dagger})^{\dagger}=\hat a_V\hat a_H=\hat a_H\hat a_V$ (different modes commute):

$$
\begin{aligned}
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle
&=\langle\Psi\rvert\hat a_H^{\dagger}\,\big(\hat a_H\lvert\Psi\rangle\big)
=\lambda\,\langle\Psi\rvert\hat a_H^{\dagger}\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right)\lvert\Psi\rangle\\
&=\lambda S_4\,\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H^{\dagger}\lvert\Psi\rangle-\lambda C_4\,\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V^{\dagger}\lvert\Psi\rangle
=\lambda S_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-\lambda C_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*} .
\end{aligned}
$$

**Pair type.** For $\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle$, the replacement leaves an annihilator *left* of a creator. Step 3 reorders them with $\hat a_H\hat a_H^{\dagger}=1+\hat a_H^{\dagger}\hat a_H$ and $\hat a_H\hat a_V^{\dagger}=\hat a_V^{\dagger}\hat a_H$:

$$
\begin{aligned}
\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle
&=\langle\Psi\rvert\hat a_H\,\big(\hat a_H\lvert\Psi\rangle\big)
=\lambda S_4\,\langle\Psi\rvert\hat a_H\hat a_H^{\dagger}\lvert\Psi\rangle-\lambda C_4\,\langle\Psi\rvert\hat a_H\hat a_V^{\dagger}\lvert\Psi\rangle\\
&=\lambda S_4\,\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-\lambda C_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle .
\end{aligned}
$$

So photon numbers are expressed through pair correlations and vice versa. The $1$ from the commutator is the only term without an unknown.

#### All eight entries

For the photon-number type $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j\lvert\Psi\rangle$, the operator $\hat a_j$ is replaced:

$$
\begin{aligned}
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-C_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\Big),\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}-C_4\,\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle^{*}\Big),\\
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-S_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\Big),\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}-S_4\,\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle^{*}\Big),
\end{aligned}
\tag{11a}
$$

and for the pair type $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$, again the right-hand operator $\hat a_j$ is replaced:

$$
\begin{aligned}
\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-C_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\Big),\\
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-S_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\Big),\\
\langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle-C_4\,\big(1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle\big)\Big),\\
\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle-S_4\,\big(1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle\big)\Big).
\end{aligned}
\tag{11b}
$$

(11a) and (11b) are eight linear equations for the eight unknown expectation values. No Fock-state sums were needed.

#### Matrix form

The eight equations have a pattern. In every line, the coefficients $S_4$, $-C_4$ (first line of (9)) or $-C_4$, $-S_4$ (second line of (9)) are a row of $M$. So the equations are matrix products with $M$. With the matrices $N$ and $\mathcal{M}$ of (10), (11a) is entry by entry the product $\lambda\,\mathcal{M}^{*}M$. For example, the third line is the $(H,V)$ entry:

$$
\big(\lambda\,\mathcal{M}^{*}M\big)_{HV}
=\lambda\Big(\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}\,M_{HV}+\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\,M_{VV}\Big)
=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-S_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\Big)
=\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle .
$$

Likewise, (11b) is entry by entry $\lambda M+\lambda N^TM$, where $\lambda M$ collects the terms with the $1$'s. For example, the $(H,V)$ entry:

$$
\big(\lambda M+\lambda N^TM\big)_{HV}
=\lambda\Big(M_{HV}+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\,M_{HV}+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\,M_{VV}\Big)
=\lambda\Big(-C_4\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-S_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\Big)
=\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle .
$$

Here $(N^T)_{HV}=N_{VH}=\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle$. Together:

$$
N=\lambda\,\mathcal{M}^{*}M,
\qquad
\mathcal{M}=\lambda M+\lambda\,N^TM .
\tag{12}
$$

#### Solving for $\mathcal{M}$

Take the transpose of the first equation of (12). With $(XY)^T=Y^TX^T$ and the symmetry of $M$ and $\mathcal{M}$ ($M^T=M$, $(\mathcal{M}^{*})^T=\mathcal{M}^{*}$):

$$
N^T=\lambda\,(\mathcal{M}^{*}M)^T=\lambda\,M\mathcal{M}^{*}.
$$

Inserting this into the second equation of (12) gives an equation for $\mathcal{M}$ alone:

$$
\mathcal{M}=\lambda M+\lambda^2\,M\mathcal{M}^{*}M .
\tag{13}
$$

Equation (13) contains $\mathcal{M}^{*}$ on the right. Its complex conjugate gives an expression for it. Since $\lambda$ and $M$ are real,

$$
\mathcal{M}^{*}=\lambda M+\lambda^2\,M\mathcal{M}M .
$$

Insert this back into the right-hand side of (13):

$$
\begin{aligned}
\mathcal{M}
&=\lambda M+\lambda^2\,M\left(\lambda M+\lambda^2\,M\mathcal{M}M\right)M\\
&=\lambda M+\lambda^3\,MMM+\lambda^4\,MM\,\mathcal{M}\,MM .
\end{aligned}
$$

With $M^2=MM=\mathbb{1}$ from (4), $MMM=M$ and $MM\,\mathcal{M}\,MM=\mathcal{M}$, so

$$
\mathcal{M}=\lambda M+\lambda^3 M+\lambda^4\mathcal{M}
\quad\Longrightarrow\quad
(1-\lambda^4)\,\mathcal{M}=\lambda(1+\lambda^2)\,M .
$$

Since $1-\lambda^4=(1-\lambda^2)(1+\lambda^2)$ and $\lambda<1$, divide by $1-\lambda^4\neq0$:

$$
\mathcal{M}=\frac{\lambda}{1-\lambda^2}\,M .
\tag{14}
$$

So the pair matrix $\mathcal{M}$ is the HWP matrix $M$ times a number that depends only on $\lambda$. The derivation determines $\mathcal{M}$ uniquely: no guess was made.

The photon-number matrix follows from the first equation of (12), using $\mathcal{M}^{*}=\mathcal{M}$ (it is real) and $M^2=\mathbb{1}$: $N=\lambda\,\mathcal{M}^{*}M=\frac{\lambda^2}{1-\lambda^2}\,\mathbb{1}$.

#### The abbreviations $\nu$ and $\mu$

The two numbers in these results appear throughout the rest of the note, so they get names:

$$
\nu=\frac{\lambda^2}{1-\lambda^2},
\qquad
\mu=\frac{\lambda}{1-\lambda^2}.
\tag{15}
$$

With $\lambda=\tanh r$ and $1-\tanh^2 r=1/\cosh^2 r$, they are $\nu=\sinh^2 r$ (the mean photon number per arm) and $\mu=\sinh r\cosh r$ (the pair amplitude). With these names, the result is

$$
N=\nu\,\mathbb{1},
\qquad
\mathcal{M}=\mu M .
\tag{16}
$$

**Reading it physically:**
- Each arm carries $\nu=\sinh^2r$ photons on average, for every HWP angle. The HWP only redistributes the *pairs*, not the mean photon number.
- At $\vartheta=0$: $S_4=0$ and $C_4=1$. Only $\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle=-\mu$ is nonzero, so each pair is split into one $H$ and one $V$ photon.
- At $\vartheta=\pi/8$: $S_4=1$ and $C_4=0$. Now $\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle=\mu$ and $\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle=-\mu$, so both photons of a pair go to the same port, as in Hong-Ou-Mandel bunching.

**Cross-check at $\vartheta=0$.** Here $\lvert\Psi\rangle=\Lambda\sum_n(-\lambda)^n\lvert n,n\rangle$. With $\hat a_H\hat a_V\lvert n+1,n+1\rangle=(n+1)\lvert n,n\rangle$:

$$
\langle\Psi\rvert\hat n_H\lvert\Psi\rangle=(1-\lambda^2)\sum_n n\lambda^{2n}=\frac{\lambda^2}{1-\lambda^2}=\nu,
\qquad
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle=(1-\lambda^2)\sum_n(n+1)(-\lambda)^{2n+1}=-\frac{\lambda}{1-\lambda^2}=-\mu .
\tag{17}
$$

Two identities used later:

$$
1+\nu=\frac{1}{1-\lambda^2},
\qquad
\nu^2-\mu^2=\frac{\lambda^4-\lambda^2}{(1-\lambda^2)^2}=-\nu .
\tag{18}
$$

### The matrix $\sigma_Q$

With $N$ and $\mathcal{M}$ known, the covariance matrix (6) can be filled in. Its rewritten form from [Why the covariance matrix?](#step1) is, in terms of the blocks of (10),

$$
\sigma_Q=
\begin{pmatrix}
\mathbb{1}+N^T & \mathcal{M}\\
\mathcal{M}^{*} & \mathbb{1}+N
\end{pmatrix}.
\tag{19}
$$

Plugging in (16) for $\lvert\Psi\rangle$:

$$
\sigma_Q=
\begin{pmatrix}
1+\nu & 0 & \mu S_4 & -\mu C_4\\
0 & 1+\nu & -\mu C_4 & -\mu S_4\\
\mu S_4 & -\mu C_4 & 1+\nu & 0\\
-\mu C_4 & -\mu S_4 & 0 & 1+\nu
\end{pmatrix}.
\tag{20}
$$

`thewalrus.quantum.Qmat` returns this matrix (checked entry by entry, see the [numerical check](#numerical-check)). The library stores states differently internally, but `Qmat` converts to this form.

<span id="why"></span>

## Step 2: why $P(0,0)=1/\sqrt{\det\sigma_Q}$

### The $Q$ function

For any two-mode state $\rho$, define, with your coherent states $\lvert\boldsymbol\alpha\rangle=\lvert\alpha_H,\alpha_V\rangle$,

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2}\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle .
\tag{21}
$$

It has three properties.

**It contains the answer.** At $\boldsymbol\alpha=0$ the coherent state is the vacuum, so

$$
P(0,0)=\langle 0,0\rvert\rho\lvert 0,0\rangle=\pi^2\,Q(0).
\tag{22}
$$

**It is a probability density.** $Q\ge0$, and by the resolution of the identity, equation (11) of [Coherent states](../docs/concepts_and_foundations/coherent_states.md#eq:coherent_identity), $\int d^4\alpha\,Q=\operatorname{Tr}\rho=1$.
**Its covariance matrix is $\sigma_Q$.** For example, inserting $\mathbb{1}=\int\frac{d^4\alpha}{\pi^2}\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\rvert$ and using $\hat a_i\lvert\boldsymbol\alpha\rangle=\alpha_i\lvert\boldsymbol\alpha\rangle$ and $\langle\boldsymbol\alpha\rvert\hat a_j^{\dagger}=\alpha_j^{*}\langle\boldsymbol\alpha\rvert$:

$$
\operatorname{Tr}\!\left[\rho\,\hat a_i\hat a_j^{\dagger}\right]
=\operatorname{Tr}\!\left[\rho\,\hat a_i\,\mathbb{1}\,\hat a_j^{\dagger}\right]
=\int\frac{d^4\alpha}{\pi^2}\,\alpha_i\alpha_j^{*}\,\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle
=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\alpha_i\alpha_j^{*},
\tag{23}
$$

and in the same way $\operatorname{Tr}\!\left[\rho\,\hat a_i\hat a_j\right]=\int Q\,\alpha_i\alpha_j$. The operators must be in the order "annihilators left", which is exactly the rule of (6). Hence, with $\mathbf v=(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})^T$,

$$
\sigma_Q=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\mathbf v\,\mathbf v^{\dagger}.
\tag{24}
$$

So $\sigma_Q$ is the covariance matrix of the probability distribution $Q$. The $1$'s on its diagonal are the spread that even the vacuum has: $Q_{\text{vac}}=\pi^{-2}e^{-|\alpha_H|^2-|\alpha_V|^2}$.

**Classical counterpart.** Writing $\langle f\rangle_Q=\int d^4\alpha\,Q(\boldsymbol\alpha)\,f(\boldsymbol\alpha)$ for the average over $Q$, equation (24) says that $\sigma_Q$ is the matrix (6) with every $\hat a_i$ replaced by $\alpha_i$ and every $\hat a_i^{\dagger}$ by $\alpha_i^{*}$, e.g. $\operatorname{Tr}\!\left[\rho\,\hat a_H\hat a_V^{\dagger}\right]=\langle\alpha_H\alpha_V^{*}\rangle_Q$. The rule "annihilators to the left" is what makes this replacement exact.

For a complex random variable there are two kinds of averages, with and without complex conjugation. Splitting one amplitude into real and imaginary parts, $\alpha_H=x_H+iy_H$, shows what each kind measures:

$$
\langle\alpha_H\alpha_H^{*}\rangle_Q=\langle x_H^2\rangle_Q+\langle y_H^2\rangle_Q,
\qquad
\langle\alpha_H\alpha_H\rangle_Q=\langle x_H^2\rangle_Q-\langle y_H^2\rangle_Q+2i\,\langle x_Hy_H\rangle_Q .
$$

- The averages *with* conjugation (entries of the type $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j\lvert\Psi\rangle$) give the **size** of the cloud of $\alpha$ values. Quantum mechanically, $\langle\alpha_H\alpha_H^{*}\rangle_Q=\operatorname{Tr}\!\left[\rho\,\hat a_H\hat a_H^{\dagger}\right]=1+\operatorname{Tr}\!\left[\rho\,\hat n_H\right]$: vacuum noise plus photons.
- The averages *without* conjugation (entries of the type $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$) give the **shape**. If $\langle\alpha_H\alpha_H\rangle_Q=0$, then $\langle x_H^2\rangle_Q=\langle y_H^2\rangle_Q$ and $\langle x_Hy_H\rangle_Q=0$, so the cloud is round. If it is nonzero, the cloud is stretched into an ellipse, which is squeezing.

In this picture the two angles discussed after (16) look as follows: at $\vartheta=0$ each arm alone is a round cloud and only $\langle\alpha_H\alpha_V\rangle_Q=-\mu$ correlates the arms; at $\vartheta=\pi/8$ each arm alone is an ellipse.

### Height of a bell curve

If $Q$ is a Gaussian bell curve centred at $0$, its height at the centre is fixed by its spread, as in [Why the covariance matrix?](#step1). With four real variables ($\operatorname{Re}\alpha_{H,V}$, $\operatorname{Im}\alpha_{H,V}$) the same normalization argument gives

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2\sqrt{\det\sigma_Q}}\exp\!\left(-\tfrac12\,\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v\right),
\qquad
Q(0)=\frac{1}{\pi^2\sqrt{\det\sigma_Q}} .
\tag{25}
$$

The factor $\pi^2$ instead of $(2\pi)^2$ comes from writing $\mathbf v$ in terms of $\alpha,\alpha^{*}$: going from $(\operatorname{Re}\alpha,\operatorname{Im}\alpha)$ to $(\alpha,\alpha^{*})$ changes the determinant by $2^4$, and $(2\pi)^2/\sqrt{2^4}=\pi^2$. For the vacuum, $\sigma_Q=\mathbb{1}$ and (25) gives back $\pi^{-2}e^{-|\boldsymbol\alpha|^2}$. Combining with (22):

$$
\boxed{\;P(0,0)=\frac{1}{\sqrt{\det\sigma_Q}}\;}
\tag{26}
$$

This is the zero-photon case of the central formula of Gaussian boson sampling <a href="#ref-hamilton2017">[1]</a>. The square root is the ordinary positive one, because $\sigma_Q$ is a covariance matrix and $\det\sigma_Q>0$.

### Is $Q$ really a bell curve? Check with your own calculation

For $\lvert\Psi\rangle$ this can be checked directly with the tools of the main derivation. There, $\langle 0\rvert e^{\frac{\lambda}{2}\mathbf{\hat a}^TM\mathbf{\hat a}}\lvert\boldsymbol\alpha\rangle=e^{\frac{\lambda}{2}\boldsymbol\alpha^TM\boldsymbol\alpha-\frac12\boldsymbol\alpha^{\dagger}\boldsymbol\alpha}$ was shown. Its complex conjugate is

$$
\langle\boldsymbol\alpha\vert\Psi\rangle=\Lambda\,e^{\frac{\lambda}{2}(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}-\frac12\boldsymbol\alpha^{\dagger}\boldsymbol\alpha},
\tag{27}
$$

so

$$
Q(\boldsymbol\alpha)=\frac{\Lambda^2}{\pi^2}\exp\!\left(-\lvert\alpha_H\rvert^2-\lvert\alpha_V\rvert^2+\frac{\lambda}{2}\boldsymbol\alpha^TM\boldsymbol\alpha+\frac{\lambda}{2}(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}\right).
\tag{28}
$$

The exponent is quadratic in $\alpha,\alpha^{*}$, so $Q$ is a bell curve, and its height is $Q(0)=\Lambda^2/\pi^2=(1-\lambda^2)/\pi^2$. Now compute $\det\sigma_Q$ from (20) with the block rule (36) derived below:

$$
\det\sigma_Q=\det\!\big((1+\nu)\mathbb{1}+\mu M\big)\det\!\big((1+\nu)\mathbb{1}-\mu M\big)
=\big[(1+\nu)^2-\mu^2\big]^2=\frac{1}{(1-\lambda^2)^2}.
\tag{29}
$$

Here $\det(a\mathbb{1}\pm\mu M)=a^2-\mu^2$ because $M$ has eigenvalues $\pm1$, and $(1+\nu)^2-\mu^2=1/(1-\lambda^2)$ by (18). So (26) gives $1/\sqrt{\det\sigma_Q}=1-\lambda^2$, the same as $\pi^2Q(0)=\Lambda^2$ ✓.

**What is imported.** After the losses of Step 3 the state is no longer pure, and (27) no longer applies. That $Q$ is still a bell curve then is the one general fact the formalism relies on: beam splitters with vacuum inputs map Gaussian states to Gaussian states. The [numerical check](#numerical-check) confirms it for this case.

<span id="step3"></span>

## Step 3: detector efficiency as a beam splitter

### Why this is allowed

A beam splitter with transmissivity $\eta$, whose other input is vacuum, loses $k$ of $n$ photons with binomial probability. Its effect on a state is described by the operators (Kraus operators)

$$
\hat K_k=\sum_{n=k}^{\infty}\sqrt{\binom{n}{k}}\,\eta^{\frac{n-k}{2}}(1-\eta)^{\frac{k}{2}}\,\lvert n-k\rangle\langle n\rvert,
\qquad
\rho\;\longrightarrow\;\mathcal{E}_\eta(\rho)=\sum_{k=0}^{\infty}\hat K_k\,\rho\,\hat K_k^{\dagger}.
\tag{30}
$$

Only the term $n=k$ ("all photons lost") ends in the vacuum, so $\langle 0\rvert\hat K_k\lvert n\rangle=\delta_{nk}(1-\eta)^{n/2}$. Therefore

$$
\langle 0\rvert\mathcal{E}_\eta(\rho)\lvert 0\rangle
=\sum_{n}(1-\eta)^{n}\langle n\rvert\rho\lvert n\rangle
=\operatorname{Tr}\!\left[\rho\,(1-\eta)^{\hat n}\right].
\tag{31}
$$

The right-hand side is your no-click POVM element $\Pi_0^{(\eta)}$ from [POVM](../docs/theory/povm.md#formula_P_cc_loss). So (1) becomes

$$
P^{(\eta_H,\eta_V)}(0,0)
=\langle 0,0\rvert\,\rho'\,\lvert 0,0\rangle,
\qquad
\rho'=(\mathcal{E}_{\eta_H}\otimes\mathcal{E}_{\eta_V})\big(\lvert\Psi\rangle\langle\Psi\rvert\big):
\tag{32}
$$

an inefficient detector is a perfect detector behind a beam splitter. By (26), $P(0,0)=1/\sqrt{\det\sigma_Q'}$, where $\sigma_Q'$ is the matrix (6) of $\rho'$.

### What the beam splitter does to the covariance matrix

Expectation values in $\rho'$ are easiest to compute by letting the beam splitter act on the operators. A new mode $\hat b_H$ (or $\hat b_V$) in the vacuum enters the unused port:

$$
\hat a_H\;\longrightarrow\;\sqrt{\eta_H}\,\hat a_H+\sqrt{1-\eta_H}\,\hat b_H,
\qquad
\hat a_V\;\longrightarrow\;\sqrt{\eta_V}\,\hat a_V+\sqrt{1-\eta_V}\,\hat b_V .
\tag{33}
$$

Insert (33) into the blocks $N$ and $\mathcal{M}$ of (10). Because the $\hat b$ modes are in the vacuum and uncorrelated with $\lvert\Psi\rangle$, every term containing a $\hat b$ vanishes: $\langle 0\rvert\hat b\lvert 0\rangle=\langle 0\rvert\hat b^{\dagger}\hat b\lvert 0\rangle=\langle 0\rvert\hat b\hat b\lvert 0\rangle=0$. (This is why $N$ and $\mathcal{M}$ are transformed rather than the entries of $\sigma_Q$: $\langle 0\rvert\hat b\hat b^{\dagger}\lvert 0\rangle=1$ would not vanish.) For example,

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

### The lossy matrix $\sigma_Q'$

Putting (34) into the pattern (6), with $\operatorname{Tr}\!\big[\rho'\,\hat a_i\hat a_i^{\dagger}\big]=1+\operatorname{Tr}\!\big[\rho'\,\hat a_i^{\dagger}\hat a_i\big]$:

<span id="sigmaQ_prime"></span>

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

$$
A=\begin{pmatrix}1+\nu\eta_H & 0\\ 0 & 1+\nu\eta_V\end{pmatrix}=\mathbb{1}+\nu(\mathbb{1}-D),
\qquad
B=\mu\begin{pmatrix}\eta_H S_4 & -\sqrt{\eta_H\eta_V}\,C_4\\ -\sqrt{\eta_H\eta_V}\,C_4 & -\eta_V S_4\end{pmatrix}.
\tag{35b}
$$

Setting $\eta_H=\eta_V=1$ gives back (20), and $\eta_H=\eta_V=0$ gives $\mathbb{1}$, the vacuum.

<span id="step4"></span>

## Step 4: the determinant

### Reducing $4\times4$ to two $2\times2$ determinants

For any matrix of the form $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$:
1. Add the lower block row to the upper one. This does not change the determinant.
2. Subtract the left block column from the right one. This does not change it either.

$$
\begin{pmatrix}A&B\\B&A\end{pmatrix}
\;\xrightarrow{\;\text{row}\;}\;
\begin{pmatrix}A+B&A+B\\B&A\end{pmatrix}
\;\xrightarrow{\;\text{column}\;}\;
\begin{pmatrix}A+B&0\\B&A-B\end{pmatrix}.
$$

The result is block-triangular, so

$$
\det\sigma_Q'=\det(A+B)\,\det(A-B).
\tag{36}
$$

In our case:

$$
A\pm B=
\begin{pmatrix}
1+\nu\eta_H\pm\mu\eta_H S_4 & \mp\mu\sqrt{\eta_H\eta_V}\,C_4\\
\mp\mu\sqrt{\eta_H\eta_V}\,C_4 & 1+\nu\eta_V\mp\mu\eta_V S_4
\end{pmatrix}.
\tag{37}
$$

### Evaluating the two factors

The $2\times2$ determinant of (37) is "diagonal product minus off-diagonal product":

$$
\det(A\pm B)=\left(1+\nu\eta_H\pm\mu\eta_H S_4\right)\left(1+\nu\eta_V\mp\mu\eta_V S_4\right)-\mu^2\eta_H\eta_V C_4^2 .
\tag{38}
$$

Multiplying out the first product, the terms without $\pm$ and the terms with $\pm$ separate:

$$
\det(A\pm B)
=\underbrace{\Big[(1+\nu\eta_H)(1+\nu\eta_V)-\mu^2\eta_H\eta_V S_4^2-\mu^2\eta_H\eta_V C_4^2\Big]}_{\mathcal{P}}
\;\pm\;\underbrace{\Big[\mu\eta_H S_4\,(1+\nu\eta_V)-\mu\eta_V S_4\,(1+\nu\eta_H)\Big]}_{\Delta},
\tag{39}
$$

so that

$$
\det\sigma_Q'=(\mathcal{P}+\Delta)(\mathcal{P}-\Delta)=\mathcal{P}^2-\Delta^2 .
\tag{40}
$$

**The part $\mathcal{P}$.** The two terms with $S_4^2$ and $C_4^2$ combine, and the HWP angle drops out:

$$
\mu^2\eta_H\eta_V S_4^2+\mu^2\eta_H\eta_V C_4^2=\mu^2\eta_H\eta_V\left(S_4^2+C_4^2\right)=\mu^2\eta_H\eta_V .
\tag{41}
$$

Then, using $\nu^2-\mu^2=-\nu$ from (18),

$$
\mathcal{P}=(1+\nu\eta_H)(1+\nu\eta_V)-\mu^2\eta_H\eta_V
=1+\nu(\eta_H+\eta_V)+(\nu^2-\mu^2)\eta_H\eta_V
=1+\nu\left(\eta_H+\eta_V-\eta_H\eta_V\right).
\tag{42}
$$

Since $\eta_H+\eta_V-\eta_H\eta_V=1-(1-\eta_H)(1-\eta_V)=1-t_Ht_V$ and $\nu=\lambda^2/(1-\lambda^2)$:

$$
(1-\lambda^2)\,\mathcal{P}=1-\lambda^2+\lambda^2(1-t_Ht_V)=1-\lambda^2t_Ht_V .
\tag{43}
$$

**The part $\Delta$.** The $\nu\eta_H\eta_V$ terms cancel:

$$
\Delta=\mu S_4\big[(1+\nu\eta_V)\eta_H-(1+\nu\eta_H)\eta_V\big]=\mu\,(\eta_H-\eta_V)\,S_4,
\qquad
(1-\lambda^2)\,\Delta=\lambda\,(\eta_H-\eta_V)\sin(4\vartheta).
\tag{44}
$$

### Result

Inserting (43) and (44) into (40):

$$
\det\sigma_Q'
=\frac{\left(1-\lambda^2t_Ht_V\right)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}{(1-\lambda^2)^2}
=\frac{\det Q}{(1-\lambda^2)^2},
\tag{45}
$$

where $\det Q=\det(\mathbb{1}-\lambda^2MDMD)$ is the determinant of the [main derivation](../docs/theory/cc_derivation.md). With (26) and (32):

$$
\boxed{\;
P^{(\eta_H,\eta_V)}(0,0)=\frac{1}{\sqrt{\det\sigma_Q'}}
=\frac{1-\lambda^2}
{\sqrt{\big(1-\lambda^2(1-\eta_H)(1-\eta_V)\big)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}}\; .}
\tag{46}
$$

**By-product: $\det Q>0$.** The same split can be done as a rotation. With the orthogonal matrix $K=\frac{1}{\sqrt2}\left(\begin{smallmatrix}\mathbb{1}&\mathbb{1}\\\mathbb{1}&-\mathbb{1}\end{smallmatrix}\right)$, one finds $K\sigma_Q'K=\left(\begin{smallmatrix}A+B&0\\0&A-B\end{smallmatrix}\right)$. $\sigma_Q'$ is a covariance matrix, hence positive definite, and a rotation keeps it so. Therefore $A+B$ and $A-B$ are positive definite, and both factors

$$
(1-\lambda^2)(\mathcal{P}\pm\Delta)=1-\lambda^2t_Ht_V\pm\lambda(\eta_H-\eta_V)\sin(4\vartheta)
\tag{47}
$$

are strictly positive. Their product is $\det Q$, which shows $\det Q>0$ for all $0\le\lambda<1$ and $0\le\eta_{H,V}\le1$.

### Sanity checks

| Limit | $\det\sigma_Q'$ | $P^{(\eta_H,\eta_V)}(0,0)$ | Meaning |
|---|---|---|---|
| $\eta_H=\eta_V=0$ | $1$ | $1$ | blind detectors never click |
| $\eta_H=\eta_V=1$ | $(1-\lambda^2)^{-2}$ | $1-\lambda^2$ | vacuum part $\Lambda^2$ of the TMSV |
| $\eta_H=\eta_V=\eta$ | $\dfrac{(1-\lambda^2(1-\eta)^2)^2}{(1-\lambda^2)^2}$ | $\dfrac{1-\lambda^2}{1-\lambda^2(1-\eta)^2}$ | no $\vartheta$ dependence |
| $\lambda=0$ | $1$ | $1$ | no pump |

The third row explains why $\Delta\propto(\eta_H-\eta_V)$. If both detectors are equally efficient, the "beam splitter in front of the detector" acts identically on both modes, so it can be moved in front of the HWP. The HWP then only rotates the modes before two identical detectors, and that cannot change $P(0,0)$.

<span id="coincidence"></span>

## Step 5: coincidence probability and the Torontonian

So far only $P^{(\eta_H,\eta_V)}(0,0)$, the probability that *neither* detector clicks, has been computed. The experiment counts **coincidences**, i.e. events where *both* detectors click. This step shows that the same matrix $\sigma_Q'$ also gives the coincidence probability. It proceeds in four parts:

1. **Inclusion–exclusion:** write the coincidence probability through three no-click probabilities. One of them is (46); two are new.
2. **Quesada's $Q$-function derivation** of the same formula. Besides confirming it, it shows *what* the two new terms are in terms of $Q$: heights at the origin of its marginals.
3. **No click in one detector:** evaluate these two terms as $1/\sqrt{\det}$ of a $2\times2$ part of $\sigma_Q'$.
4. **Result:** assemble $P_{\mathrm{cc}}$ and recognise it as the Torontonian of <a href="#ref-quesada2018">[2]</a>.

### From clicks to no-clicks (inclusion–exclusion)

A bucket detector has two outcomes, "no click" with POVM element $\Pi_0^{(\eta)}=(1-\eta)^{\hat n}$ and "click" with $\Pi_{\text{click}}^{(\eta)}=\mathbb{1}-\Pi_0^{(\eta)}$ (see [POVM](../docs/theory/povm.md#formula_P_cc_loss)). A coincidence is a click in both detectors. Multiplying out the product of the two click elements:

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

This is equation (16) of [POVM](../docs/theory/povm.md#formula_P_cc_loss). The probability of "both click" is written entirely through probabilities of "no click": "no click in $H$" (whatever $V$ does), "no click in $V$" (whatever $H$ does), and "no click in either". This rewriting is called *inclusion–exclusion*. The last term is (46). The first two, $P_H^{(\eta_H)}(0)$ and $P_V^{(\eta_V)}(0)$, are still missing.

<span id="cc_quesada"></span>

### The same formula from the $Q$ function (Quesada's derivation)

Quesada, Arrazola and Killoran <a href="#ref-quesada2018">[2]</a> obtain (48) without operator algebra: they write every click probability as an integral over the $Q$ function. Their argument is reproduced here for two detectors, because it also shows how to compute the missing terms. Equation numbers in square brackets, e.g. [2, Eq. (9)], refer to that paper. Part 1 treats ideal detectors and an arbitrary state; Part 2 adds the efficiencies.

#### Part 1: ideal detectors, arbitrary state

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

with a weight function $P_\Pi(\alpha)$ (its $P$ function). For the two elements, the weights can be read off directly:

- $\lvert 0\rangle\langle 0\rvert$ is the coherent-state projector at $\alpha=0$, so its weight is concentrated at the origin: $P_0(\alpha)=\delta^{(2)}(\alpha)$. Indeed $\int d^2\alpha\,\delta^{(2)}(\alpha)\lvert\alpha\rangle\langle\alpha\rvert=\lvert 0\rangle\langle 0\rvert$.
- $\mathbb{1}=\int\frac{d^2\alpha}{\pi}\lvert\alpha\rangle\langle\alpha\rvert$ by the resolution of the identity (equation (11) of [Coherent states](../docs/concepts_and_foundations/coherent_states.md#eq:coherent_identity)), so its weight is the constant $1/\pi$.
- Hence $\Pi_1=\mathbb{1}-\lvert 0\rangle\langle 0\rvert$ has $P_1(\alpha)=\frac{1}{\pi}-\delta^{(2)}(\alpha)$.

These are [2, Eqs. (10a), (10b)].

**Step (c): a probability is an integral over $Q$.** For a two-mode state $\rho$ with $Q$ function $Q_\rho(\boldsymbol\alpha)=\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle/\pi^2$ (21), and one POVM element per detector,

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
- (iv) $=\pi^2\,Q_\rho(0,0)=\langle 0,0\rvert\rho\lvert 0,0\rangle=:p(0,0)$, by (22).

Therefore, for ideal detectors and any state,

$$
P_{\mathrm{cc}}=1-p_V(0)-p_H(0)+p(0,0).
$$

The inclusion–exclusion structure comes from multiplying out $\left(\frac{1}{\pi}-\delta^{(2)}\right)\left(\frac{1}{\pi}-\delta^{(2)}\right)$. Each $\frac1\pi$ ("anything may happen in this detector") integrates the mode out. Each $\delta^{(2)}$ ("no click") evaluates it at $\alpha=0$. For $N$ detectors the same expansion is the identity $\prod_{k=1}^{N}(1-x_k)=\sum_{Z}(-1)^{|Z|}\prod_{i\in Z}x_i$ that [2, Eq. (A7)] uses.

#### Part 2: detector efficiency

**Step (f): include the detector efficiencies.** By Step 3, a detector with efficiency $\eta$ is an ideal detector behind a beam splitter of transmissivity $\eta$. The real experiment is therefore Part 1 applied to the state *after* the beam splitters, $\rho=\rho'$ of (32). By (31), each vacuum probability of $\rho'$ is the corresponding lossy no-click probability of the original state $\lvert\Psi\rangle$:

$$
\begin{aligned}
p(0,0)\big|_{\rho'}&=\langle 0,0\rvert\rho'\lvert 0,0\rangle=\langle\Psi\rvert(1-\eta_H)^{\hat n_H}(1-\eta_V)^{\hat n_V}\lvert\Psi\rangle=P^{(\eta_H,\eta_V)}(0,0),\\
p_H(0)\big|_{\rho'}&=\langle 0\rvert\rho'_H\lvert 0\rangle=\langle\Psi\rvert(1-\eta_H)^{\hat n_H}\lvert\Psi\rangle=P_H^{(\eta_H)}(0),\\
p_V(0)\big|_{\rho'}&=\langle 0\rvert\rho'_V\lvert 0\rangle=\langle\Psi\rvert(1-\eta_V)^{\hat n_V}\lvert\Psi\rangle=P_V^{(\eta_V)}(0).
\end{aligned}
$$

For the single-mode lines, only the beam splitter in front of that mode matters. The one in front of the other mode acts on a mode that is traced out and does not change the reduced state. Inserted into the result of Part 1, this is exactly (48).

**What the derivation adds.** Step (e) also says *how* each term is obtained from the $Q$ function of $\rho'$:
- $P^{(\eta_H,\eta_V)}(0,0)$ is the height of $Q_{\rho'}$ at the origin. This is what Step 2 evaluated: $1/\sqrt{\det\sigma_Q'}$.
- $P_H^{(\eta_H)}(0)$ and $P_V^{(\eta_V)}(0)$ are heights at the origin of the **marginals** of $Q_{\rho'}$, i.e. of $Q_{\rho'}$ integrated over the other mode. These are evaluated next.

### No click in one detector

Take $P_H^{(\eta_H)}(0)=\langle 0\rvert\rho'_H\lvert 0\rangle$. Its $Q$ function is the marginal from step (e),

$$
Q_H(\alpha_H)=\frac{1}{\pi}\langle\alpha_H\rvert\rho'_H\lvert\alpha_H\rangle=\int d^2\alpha_V\;Q_{\rho'}(\alpha_H,\alpha_V).
$$

Integrating a bell curve over some of its variables gives again a bell curve in the remaining ones. Its covariance matrix is the corresponding part of the full one: expectation values of operators acting only on mode $H$ are the same in $\rho'$ and in $\rho'_H$. So the covariance matrix of $Q_H$, built by the rule (6) for one mode, consists of those entries of $\sigma_Q'$ that contain only $\hat a_H$ and $\hat a_H^{\dagger}$. These are the entries in rows and columns $1$ and $3$ of (35a):

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

The one-mode version of (25)–(26), with $\pi$ instead of $\pi^2$, then gives

$$
P_H^{(\eta_H)}(0)=\pi\,Q_H(0)=\frac{1}{\sqrt{\det\sigma_Q'^{(H)}}}
=\frac{1}{\sqrt{(1+\nu\eta_H)^2-\mu^2\eta_H^2S_4^2}}
=\frac{1-\lambda^2}{\sqrt{\big(1-\lambda^2t_H\big)^2-\lambda^2\eta_H^2\sin^2(4\vartheta)}} .
\tag{49}
$$

The last form follows by multiplying the determinant by $(1-\lambda^2)^2$, using $(1-\lambda^2)(1+\nu\eta_H)=1-\lambda^2+\lambda^2\eta_H=1-\lambda^2t_H$ and $(1-\lambda^2)\mu=\lambda$.

For mode $V$, rows and columns $2$ and $4$ of (35a) give

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

**Check: switch off the other detector.** A detector with $\eta_V=0$ never clicks, since $(1-0)^{\hat n_V}=\mathbb{1}$. So $P_H^{(\eta_H)}(0)$ must also equal (46) at $\eta_V=0$, i.e. $t_V=1$. Setting $t_V=1$ and $\eta_V=0$ in (46) indeed gives (49).

**What one arm alone looks like.**
- At $\vartheta=0$ ($S_4=0$): $P_H^{(\eta_H)}(0)=\frac{1-\lambda^2}{1-\lambda^2t_H}=\frac{1}{1+\nu\eta_H}$. Each arm alone is a round cloud with no squeezing, i.e. thermal light with mean photon number $\nu$. Indeed, for thermal light $\sum_n(1-\eta)^n\frac{\nu^n}{(1+\nu)^{n+1}}=\frac{1}{1+\eta\nu}$.
- At $\vartheta=\pi/8$ ($S_4=1$): $P_H^{(\eta_H)}(0)=\frac{1-\lambda^2}{\sqrt{(1-\lambda^2t_H)^2-\lambda^2\eta_H^2}}$, the no-click probability of a single-mode squeezed state.

### The coincidence probability

Inserting (46), (49) and its $V$ counterpart into (48):

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

### The Torontonian

Quesada, Arrazola and Killoran <a href="#ref-quesada2018">[2]</a> package this calculation for any number of threshold detectors. In their notation, $\Sigma$ is the covariance matrix of the $Q$ function, i.e. our $\sigma_Q'$. The probability that exactly the detectors in a set $S$ click and all others stay dark is their Eqs. (11)–(12):

$$
p(S)=\frac{\operatorname{Tor}\big[O_{(S)}\big]}{\sqrt{\det\Sigma}},
\qquad
O_{(S)}=\mathbb{1}-\big(\Sigma^{-1}\big)_{(S)},
\qquad
\operatorname{Tor}(A)=\sum_{Z\in P([N])}(-1)^{|Z|}\frac{1}{\sqrt{\det\big(\mathbb{1}-A_{(Z)}\big)}} .
$$

Here $(\cdot)_{(S)}$ keeps only the rows and columns belonging to the modes in $S$, in each of the four blocks of the matrix. $N$ is the number of modes in $S$, and $P([N])$ is the set of all subsets $Z$ of these modes. The sum is called the **Torontonian**.

**It is the same as (50).** For a coincidence both detectors click, $S=\{H,V\}$, so $O=\mathbb{1}-\sigma_Q'^{-1}$ and $Z$ runs over $\emptyset$, $\{H\}$, $\{V\}$ and $\{H,V\}$. In each term, $\mathbb{1}-O_{(Z)}=(\sigma_Q'^{-1})_{(Z)}$ is a part of the *inverse* matrix. Jacobi's complementary-minor identity relates a part of the inverse to the complementary part of the matrix itself:

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

The [numerical check](#numerical-check) confirms (50) against `thewalrus`'s Torontonian at five random parameter sets.

<span id="comparison"></span>

## Comparison with the main derivation

| | [Main derivation](../docs/theory/cc_derivation.md) | This note |
|---|---|---|
| Works with | the state vector $\lvert\Psi\rangle$ | the numbers $\langle\Psi\rvert\hat a\hat a\lvert\Psi\rangle$, $\langle\Psi\rvert\hat a^{\dagger}\hat a\lvert\Psi\rangle$ collected in $\sigma_Q$ |
| Efficiency | $t^{\hat n}$ moved through the exponential: $\mathbf{\hat a^{\dagger}}\to D\,\mathbf{\hat a^{\dagger}}$ | beam splitter on the covariance matrix, factors $\sqrt{\eta}$ |
| Object computed | overlap $\langle 0\rvert e^{\frac\lambda2\mathbf{\hat a}^TM\mathbf{\hat a}}e^{\frac\lambda2(\mathbf{\hat a^{\dagger}})^TDMD\mathbf{\hat a^{\dagger}}}\lvert 0\rangle$ | covariance matrix of $\lvert\Psi\rangle$, then vacuum probability |
| Where coherent states enter | resolution of $\mathbb{1}$, complex Gaussian integral | $Q$ function, height of a real bell curve |
| Matrix | $\mathbb{1}-\lambda^2MDMD$ ($2\times2$) | $\sigma_Q'$ ($4\times4$, symmetric, positive definite) |
| Hard part | the complex Gaussian integral | the vacuum formula (26), imported |
| Sign of the square root | fixed separately via $P\ge0$ ([Lean](../docs/theory/cc_derivation.md#P00_lean)) | automatic |

Both routes meet at

$$
\det\!\left(\mathbb{1}-\lambda^2MDMD\right)=(1-\lambda^2)^2\,\det\sigma_Q' .
\tag{51}
$$

The method of this note also carries over to the setting of [Generalization](../docs/theory/generalization.md). For any passive element in front of the PBS, (9) holds with that element's $M$, and the same steps apply. For a complex $M$ the lower-left block becomes $B^{*}$. Effects that are awkward in the state-vector picture are simply extra terms in the covariance matrix: thermal background adds to $N$, and a mixed or multimode source changes $N$ and $\mathcal{M}$.

<span id="numerical-check"></span>

## Numerical check

### With `thewalrus`

The script compares three things:

1. the closed form (46),
2. $1/\sqrt{\det\sigma_Q'}$ computed by `thewalrus`,
3. the library's threshold-detection probability.

It also compares $P_{\mathrm{cc}}$ from (50) with the library's Torontonian.

`thewalrus` builds states from "symplectic" matrices and stores them as $x,p$ covariance matrices. You can treat these lines as a black box that produces $\lvert\Psi\rangle$ with losses: `two_mode_squeezing` is the SPDC source, `interferometer(U)` the HWP and `loss` the detector efficiency. `Qmat` turns the result into the $\sigma_Q'$ of (35a).

`thewalrus` is not a project dependency, so run it in a throwaway environment, e.g. `uv run --with thewalrus --with numpy python script.py`. This was tested with `thewalrus` 0.22.0.

```python
import numpy as np
from thewalrus.quantum import Qmat
from thewalrus.symplectic import two_mode_squeezing, interferometer, loss
from thewalrus import threshold_detection_prob

def P00_closed(th, lam, eH, eV):
    detQ = (1 - lam**2*(1-eH)*(1-eV))**2 - lam**2*(eH-eV)**2*np.sin(4*th)**2
    return (1 - lam**2)/np.sqrt(detQ)

def lossy_cov(th, lam, eH, eV, hbar=2):
    r = np.arctanh(lam)
    c, s = np.cos(2*th), np.sin(2*th)
    U = np.array([[c, s], [s, -c]])               # HWP at angle th
    S = interferometer(U) @ two_mode_squeezing(r, 0)
    cov = hbar/2 * S @ S.T                         # pure state, xxpp ordering
    mu = np.zeros(4)
    mu, cov = loss(mu, cov, eH, 0, hbar=hbar)      # efficiency = transmissivity
    mu, cov = loss(mu, cov, eV, 1, hbar=hbar)
    return mu, cov

rng = np.random.default_rng(8)
for _ in range(5):
    th, lam = rng.uniform(0, np.pi), rng.uniform(0, .95)
    eH, eV = rng.uniform(0, 1), rng.uniform(0, 1)
    mu, cov = lossy_cov(th, lam, eH, eV)
    p00_Q  = 1/np.sqrt(np.linalg.det(Qmat(cov)).real)
    p00_tw = threshold_detection_prob(mu, cov, [0, 0]).real
    pcc_tw = threshold_detection_prob(mu, cov, [1, 1]).real
    pcc_cf = (1 - P00_closed(th, lam, eH, 0) - P00_closed(th, lam, 0, eV)
              + P00_closed(th, lam, eH, eV))
    print(f"{P00_closed(th,lam,eH,eV):.12f} {p00_Q:.12f} {p00_tw:.12f} | "
          f"{pcc_cf:.12f} {pcc_tw:.12f}")
```

Output:

```text
0.371058949784 0.371058949784 0.371058949784 | 0.141826213062 0.141826213062
0.398349140074 0.398349140074 0.398349140074 | 0.010433305259 0.010433305259
0.890949357824 0.890949357824 0.890949357824 | 0.017971948976 0.017971948976
0.855038232771 0.855038232771 0.855038232771 | 0.061344652949 0.061344652949
0.434027166501 0.434027166501 0.434027166501 | 0.446652713512 0.446652713512
```

`Qmat(cov)` from this script was also compared entry by entry with the explicit matrix (35a) at $\vartheta=0.37$, $\lambda=0.6$, $\eta_H=0.7$, $\eta_V=0.45$. The largest difference is $2\times10^{-16}$, i.e. the matrices agree, including all signs.

### Symbolic check

This snippet confirms three things exactly with `sympy`:
- the determinant identity (45), using the explicit matrix (35a),
- $M^2=\mathbb{1}$,
- that $\mathcal{M}=\mu M$ and $N=\nu\mathbb{1}$ solve (12).

```python
import sympy as sp
l, eH, eV, th = sp.symbols('lambda eta_H eta_V theta', real=True)
S4, C4 = sp.sin(4*th), sp.cos(4*th)
M  = sp.Matrix([[S4, -C4], [-C4, -S4]])
nu, mu = l**2/(1-l**2), l/(1-l**2)
r = sp.sqrt(eH*eV)
sigQ = sp.Matrix([
    [1+nu*eH, 0,        mu*eH*S4, -mu*r*C4],
    [0,       1+nu*eV, -mu*r*C4,  -mu*eV*S4],
    [mu*eH*S4, -mu*r*C4, 1+nu*eH, 0],
    [-mu*r*C4, -mu*eV*S4, 0,      1+nu*eV]])
detQ = (1 - l**2*(1-eH)*(1-eV))**2 - l**2*(eH-eV)**2*S4**2
print(sp.simplify(sp.trigsimp(sigQ.det() - detQ/(1-l**2)**2)))   # 0
print(sp.simplify(M*M - sp.eye(2)))                                # zero matrix
Mcal, N = mu*M, nu*sp.eye(2)
print(sp.simplify(N - l*Mcal.conjugate()*M),                       # zero matrix
      sp.simplify(Mcal - (l*M + l*N.T*M)))                         # zero matrix
```

## References

<p id="ref-hamilton2017">
[1] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Gaussian Boson Sampling</em>, Phys. Rev. Lett. <strong>119</strong>, 170501 (2017). Available: https://arxiv.org/abs/1612.01199
</p>

<p id="ref-quesada2018">
[2] N. Quesada, J. M. Arrazola, N. Killoran,
<em>Gaussian boson sampling using threshold detectors</em>, Phys. Rev. A <strong>98</strong>, 062322 (2018). Available: https://arxiv.org/abs/1807.01639
</p>

<p id="ref-kruse2019">
[3] R. Kruse, C. S. Hamilton, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Detailed study of Gaussian boson sampling</em>, Phys. Rev. A <strong>100</strong>, 032326 (2019). Available: https://arxiv.org/abs/1801.07488
</p>

<p id="ref-gupt2019">
[4] B. Gupt, J. Izaac, N. Quesada,
<em>The Walrus: a library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling</em>, J. Open Source Softw. <strong>4</strong>(44), 1705 (2019). Documentation: https://the-walrus.readthedocs.io
</p>
