# Covariance matrix of $\lvert\Psi\rangle$

<span id="why-cov"></span>

## Why the covariance matrix?

Before computing anything: why should expectation values of two ladder operators be the right thing to compute at all?

**Classical picture.** A bell-shaped (Gaussian) probability distribution of $n$ real variables $x_1,\dots,x_n$, centred at $0$, is **completely determined** by its covariance matrix $\Sigma$, the matrix of all averages $\langle x_ix_j\rangle$: knowing $\Sigma$, one can write down the whole distribution. In particular, its height at the centre **follows directly from $\Sigma$**:

$$
p(0)=\frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}} .
$$

The wider the distribution (the larger $\det\Sigma$), the lower its peak. This is derived step by step in [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md).

**Quantum counterpart.** [Vacuum probability](vacuum_probability.md) shows that the state can be described by a probability distribution $Q(\alpha_H,\alpha_V)$ over coherent-state amplitudes. For our states this distribution is a bell curve centred at $\alpha=0$ (states with this property are called *Gaussian states* <a href="#ref-weedbrook2012">[8]</a>, <a href="#ref-ferraro2005">[9]</a>), and its height at the centre is exactly the no-click probability $P(0,0)$. So, as in the classical case:

$$
\text{covariance matrix of }Q\;\Longrightarrow\;\text{width of the bell curve}\;\Longrightarrow\;\text{height at }0\;=\;P(0,0).
$$

The entries of the covariance matrix of $Q$ are averages of products of two amplitudes, $\alpha_i\alpha_j$ and $\alpha_i\alpha_j^{*}$. These averages are expectation values of two ladder operators, e.g. $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$ and $\langle\Psi\rvert\hat a_i\hat a_j^{\dagger}\lvert\Psi\rangle$, eq. [(23)](vacuum_probability.md#eq23). This is why this page computes expectation values of **pairs** of ladder operators, and nothing else.

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

Written as one $4\times4$ matrix, with the rule "annihilation operators to the left of creation operators" (the reason for this rule follows in [Vacuum probability](vacuum_probability.md#eq23)), all 16 expectation values form the covariance matrix, which the Gaussian boson sampling literature calls $\sigma_Q$ <a href="#ref-hamilton2017">[1]</a>, <a href="#ref-kruse2019">[3]</a>

<span id="eq6"></span>

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

**Why not stay with $\lvert\Psi\rangle$?** The detector efficiency ([Detector efficiency](detector_efficiency.md)) turns $\lvert\Psi\rangle$ into a mixed state, which no longer has the exponential form [(2)](notation.md#eq2). The covariance matrix, by contrast, keeps its meaning and changes in a very simple way: its entries get multiplied by factors of $\sqrt{\eta}$.

## Why we look at $\hat a\lvert\Psi\rangle$

So this page needs numbers like

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

<span id="key-relation"></span>

## The key relation

Call the exponent of [(2)](notation.md#eq2) $\hat X$. Here $\mathbf{\hat a^{\dagger}}=(\hat a_H^{\dagger},\hat a_V^{\dagger})^T$ is the column of creation operators, and $(\mathbf{\hat a^{\dagger}})^T$ is the same entries as a row (a plain transpose, not a dagger). Row times $M$ times column is a sum over the four entries of [(3)](notation.md#eq3), and the two off-diagonal terms are equal because $\hat a_H^{\dagger}\hat a_V^{\dagger}=\hat a_V^{\dagger}\hat a_H^{\dagger}$:

<span id="eq7"></span>

$$
\hat X:=\frac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^T M\mathbf{\hat a^{\dagger}}
=\frac{\lambda}{2}\sum_{i,j\in\{H,V\}}M_{ij}\,\hat a_i^{\dagger}\hat a_j^{\dagger}
=\frac{\lambda}{2}\left(S_4\,\hat a_H^{\dagger 2}-2C_4\,\hat a_H^{\dagger}\hat a_V^{\dagger}-S_4\,\hat a_V^{\dagger 2}\right).
\tag{7}
$$

Now commute $\hat a_H$ with each of the three terms. Everything follows from $[\hat a_H,\hat a_H^{\dagger}]=1$, $[\hat a_H,\hat a_V^{\dagger}]=0$ and the product rule $[\hat A,\hat B\hat C]=[\hat A,\hat B]\,\hat C+\hat B\,[\hat A,\hat C]$ (equation (2) of [Commutator with an operator exponential](../concepts_and_foundations/commutator_exponential.md#comm:product)):

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

The commutator is linear in its second argument (equation (1) of [Commutator with an operator exponential](../concepts_and_foundations/commutator_exponential.md#comm:linear)). So $[\hat a_H,\hat X]$ is the sum of the three commutators above, weighted with the coefficients of (7):

$$
[\hat a_H,\hat X]
=\frac{\lambda}{2}\left(S_4\cdot2\hat a_H^{\dagger}-2C_4\cdot\hat a_V^{\dagger}-S_4\cdot0\right)
=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right).
$$

For $\hat a_V$ the roles swap: $[\hat a_V,\hat a_H^{\dagger 2}]=0$, $[\hat a_V,\hat a_H^{\dagger}\hat a_V^{\dagger}]=\hat a_H^{\dagger}$ and $[\hat a_V,\hat a_V^{\dagger 2}]=2\hat a_V^{\dagger}$, so $[\hat a_V,\hat X]=\frac{\lambda}{2}\left(-2C_4\,\hat a_H^{\dagger}-S_4\cdot2\hat a_V^{\dagger}\right)$. Together:

<span id="eq8"></span>

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

It remains to evaluate $[\hat a_H,e^{\hat X}]$. By (8), $[\hat a_H,\hat X]$ contains only creation operators, and so does $\hat X$, so the two commute. For exactly this situation, equation (4) of [Commutator with an operator exponential](../concepts_and_foundations/commutator_exponential.md#comm:exp) gives

$$
[\hat a_H,e^{\hat X}]=[\hat a_H,\hat X]\,e^{\hat X},
$$

the operator version of $\frac{d}{dx}e^{f(x)}=f'(x)\,e^{f(x)}$. The same holds for $\hat a_V$. Together with (8):

<span id="eq9"></span>

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

## The two blocks $N$ and $\mathcal{M}$

As motivated [above](#why-cov), the eight independent second-order expectation values are abbreviated by two $2\times2$ matrices:

<span id="eq10"></span>

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

$N$ holds photon numbers, with mean photon numbers on its diagonal. $\mathcal{M}$ holds the pair correlations created by SPDC. All other second-order expectation values follow from these through $[\hat a_i,\hat a_j^{\dagger}]=\delta_{ij}$ and complex conjugation.

### One entry step by step

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

### All eight entries

For the photon-number type $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j\lvert\Psi\rangle$, the operator $\hat a_j$ is replaced:

<span id="eq11a"></span>

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

<span id="eq11b"></span>

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

### Matrix form

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

<span id="eq12"></span>

$$
N=\lambda\,\mathcal{M}^{*}M,
\qquad
\mathcal{M}=\lambda M+\lambda\,N^TM .
\tag{12}
$$

### Solving for $\mathcal{M}$

Take the transpose of the first equation of (12). With $(XY)^T=Y^TX^T$ and the symmetry of $M$ and $\mathcal{M}$ ($M^T=M$, $(\mathcal{M}^{*})^T=\mathcal{M}^{*}$):

$$
N^T=\lambda\,(\mathcal{M}^{*}M)^T=\lambda\,M\mathcal{M}^{*}.
$$

Inserting this into the second equation of (12) gives an equation for $\mathcal{M}$ alone:

<span id="eq13"></span>

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

With $M^2=MM=\mathbb{1}$ from [(4)](notation.md#eq4), $MMM=M$ and $MM\,\mathcal{M}\,MM=\mathcal{M}$, so

$$
\mathcal{M}=\lambda M+\lambda^3 M+\lambda^4\mathcal{M}
\quad\Longrightarrow\quad
(1-\lambda^4)\,\mathcal{M}=\lambda(1+\lambda^2)\,M .
$$

Since $1-\lambda^4=(1-\lambda^2)(1+\lambda^2)$ and $\lambda<1$, divide by $1-\lambda^4\neq0$:

<span id="eq14"></span>

$$
\mathcal{M}=\frac{\lambda}{1-\lambda^2}\,M .
\tag{14}
$$

So the pair matrix $\mathcal{M}$ is the HWP matrix $M$ times a number that depends only on $\lambda$. The derivation determines $\mathcal{M}$ uniquely: no guess was made.

The photon-number matrix follows from the first equation of (12), using $\mathcal{M}^{*}=\mathcal{M}$ (it is real) and $M^2=\mathbb{1}$: $N=\lambda\,\mathcal{M}^{*}M=\frac{\lambda^2}{1-\lambda^2}\,\mathbb{1}$.

### The abbreviations $\nu$ and $\mu$

The two numbers in these results appear throughout the rest of this section, so they get names:

<span id="eq15"></span>

$$
\nu=\frac{\lambda^2}{1-\lambda^2},
\qquad
\mu=\frac{\lambda}{1-\lambda^2}.
\tag{15}
$$

With $\lambda=\tanh r$ and $1-\tanh^2 r=1/\cosh^2 r$, they are $\nu=\sinh^2 r$ (the mean photon number per arm) and $\mu=\sinh r\cosh r$ (the pair amplitude). With these names, the result is

<span id="eq16"></span>

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

<span id="eq17"></span>

$$
\langle\Psi\rvert\hat n_H\lvert\Psi\rangle=(1-\lambda^2)\sum_n n\lambda^{2n}=\frac{\lambda^2}{1-\lambda^2}=\nu,
\qquad
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle=(1-\lambda^2)\sum_n(n+1)(-\lambda)^{2n+1}=-\frac{\lambda}{1-\lambda^2}=-\mu .
\tag{17}
$$

Two identities used later:

<span id="eq18"></span>

$$
1+\nu=\frac{1}{1-\lambda^2},
\qquad
\nu^2-\mu^2=\frac{\lambda^4-\lambda^2}{(1-\lambda^2)^2}=-\nu .
\tag{18}
$$

## The matrix $\sigma_Q$

With $N$ and $\mathcal{M}$ known, the covariance matrix (6) can be filled in. Its rewritten form from [Why the covariance matrix?](#why-cov) is, in terms of the blocks of (10),

<span id="eq19"></span>

$$
\sigma_Q=
\begin{pmatrix}
\mathbb{1}+N^T & \mathcal{M}\\
\mathcal{M}^{*} & \mathbb{1}+N
\end{pmatrix}.
\tag{19}
$$

Plugging in (16) for $\lvert\Psi\rangle$:

<span id="eq20"></span>

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

`thewalrus.quantum.Qmat` <a href="#ref-gupt2019">[4]</a> returns this matrix (checked entry by entry, see the [numerical check](../dashboard/comparison.md#numerical-check)). The library stores states differently internally, but `Qmat` converts to this form.

## References

<p id="ref-hamilton2017">
[1] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Gaussian Boson Sampling</em>, Phys. Rev. Lett. <strong>119</strong>, 170501 (2017). Available: https://arxiv.org/abs/1612.01199
</p>

<p id="ref-kruse2019">
[3] R. Kruse, C. S. Hamilton, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Detailed study of Gaussian boson sampling</em>, Phys. Rev. A <strong>100</strong>, 032326 (2019). Available: https://arxiv.org/abs/1801.07488
</p>

<p id="ref-gupt2019">
[4] B. Gupt, J. Izaac, N. Quesada,
<em>The Walrus: a library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling</em>, J. Open Source Softw. <strong>4</strong>(44), 1705 (2019). Documentation: https://the-walrus.readthedocs.io
</p>

<p id="ref-weedbrook2012">
[8] C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, S. Lloyd,
<em>Gaussian quantum information</em>, Rev. Mod. Phys. <strong>84</strong>, 621 (2012). Available: https://arxiv.org/abs/1110.3234
</p>

<p id="ref-ferraro2005">
[9] A. Ferraro, S. Olivares, M. G. A. Paris,
<em>Gaussian states in continuous variable quantum information</em>, 2005. Available: https://arxiv.org/abs/quant-ph/0503237
</p>
