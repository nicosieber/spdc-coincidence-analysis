# Covariance matrix and vacuum probability

This page derives the vacuum formula $P(0,0)=1/\sqrt{\det\sigma_Q}$ and computes the matrix $\sigma_Q$ for the state $\lvert\Psi\rangle$ behind the HWP. The argument follows one line:

1. **Classical picture.** A bell curve (Gaussian distribution) is completely determined by its covariance matrix. In particular, its height at the centre follows directly from the determinant of that matrix.
2. **Quantum counterpart: the $Q$ function.** With coherent states one builds a probability distribution $Q(\alpha_H,\alpha_V)$ over two complex numbers. Its value at $\alpha_H=\alpha_V=0$ is $P(0,0)/\pi^2$, eq. [(7)](#eq7). Its covariance matrix $\sigma_Q$ consists of expectation values of pairs of ladder operators, eqs. [(9)](#eq9)–[(10)](#eq10).
3. **Height of the bell curve.** If $Q$ is a bell curve centred at $0$, steps 1 and 2 together give $P(0,0)=1/\sqrt{\det\sigma_Q}$, eq. [(12)](#eq12).
4. **$\sigma_Q$ for $\lvert\Psi\rangle$.** One relation, $\mathbf{\hat a}\lvert\Psi\rangle=\lambda M\mathbf{\hat a^{\dagger}}\lvert\Psi\rangle$, gives all entries of $\sigma_Q$ without Fock-state sums, eq. [(26)](#eq26).

!!! note "Concepts used on this page"
    - **Coherent states** $\lvert\alpha\rangle$ ([Coherent states](../concepts_and_foundations/coherent_states.md)): eigenstates of the annihilation operator, $\hat a\lvert\alpha\rangle=\alpha\lvert\alpha\rangle$ with a complex number $\alpha$, and the resolution of the identity $\int\frac{d^2\alpha}{\pi}\lvert\alpha\rangle\langle\alpha\rvert=\mathbb{1}$, equation (11) of that page. Here $d^2\alpha=d(\operatorname{Re}\alpha)\,d(\operatorname{Im}\alpha)$ integrates over the complex plane. For two modes, $\lvert\boldsymbol\alpha\rangle=\lvert\alpha_H,\alpha_V\rangle$ and $d^4\alpha=d^2\alpha_H\,d^2\alpha_V$, so the identity reads $\int\frac{d^4\alpha}{\pi^2}\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\rvert=\mathbb{1}$.
    - **Density operator** $\rho$: for the pure state of the main derivation $\rho=\lvert\Psi\rangle\langle\Psi\rvert$, so that $\operatorname{Tr}[\rho\,\hat A]=\langle\Psi\rvert\hat A\lvert\Psi\rangle$ for any operator $\hat A$. The density operator is needed because after the detector losses of [Detector efficiency](detector_efficiency.md) the state is mixed and has no state vector.
    - **Peak height of a Gaussian** ([Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md)): the height of a bell curve at its centre is $1/\sqrt{\det}$ of its covariance matrix, up to factors of $\pi$.
    - **The state** $\lvert\Psi\rangle$ and the matrix $M$ of [Notation](notation.md), eqs. [(2)](notation.md#eq2)–[(4)](notation.md#eq4).

<span id="why-cov"></span>

## The classical picture: a bell curve and its covariance matrix

A bell-shaped (Gaussian) probability distribution of $n$ real variables $x_1,\dots,x_n$, centred at $0$, is **completely determined** by its covariance matrix $\Sigma$, the matrix of all averages $\langle x_ix_j\rangle$. Knowing $\Sigma$, one can write down the whole distribution. With $\mathbf x=(x_1,\dots,x_n)^T$ it reads

$$
p(\mathbf x)=\frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}}\,e^{-\frac12\mathbf x^T\Sigma^{-1}\mathbf x} .
$$

The exponent describes the shape: how fast $p$ falls off in each direction is set by $\Sigma^{-1}$. The prefactor makes the total probability equal to $1$. In particular, the height at the centre **follows directly from $\Sigma$**: at $\mathbf x=0$ the exponential equals $e^0=1$, so

$$
p(0)=\frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}} .
$$

The wider the distribution (the larger $\det\Sigma$), the lower its peak. This is derived step by step in [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md).

So to know the height of a bell curve at its centre, the whole distribution is not needed: the averages of all products of **two** variables are enough. The next section builds the quantum counterpart of this situation: a probability distribution whose height at the centre is the no-click probability $P(0,0)$.

## The quantum counterpart: the $Q$ function

For any two-mode state $\rho$, define, with the two-mode coherent states $\lvert\boldsymbol\alpha\rangle=\lvert\alpha_H,\alpha_V\rangle$ of the [main derivation](../theory/cc_derivation.md#tmsv_coherent_identity),

<span id="eq6"></span>

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2}\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle .
\tag{6}
$$

Written out, the two-mode coherent state is the product $\lvert\boldsymbol\alpha\rangle=\lvert\alpha_H\rangle\otimes\lvert\alpha_V\rangle$ of the single-mode coherent states of [Coherent states](../concepts_and_foundations/coherent_states.md), each expanded in the number basis as $\lvert\alpha\rangle=e^{-\lvert\alpha\rvert^2/2}\sum_{n}\frac{\alpha^n}{\sqrt{n!}}\lvert n\rangle$. Inserting this expansion for both modes on both sides of $\rho$ gives

$$
\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle
=\langle\alpha_H,\alpha_V\rvert\rho\lvert\alpha_H,\alpha_V\rangle
=e^{-\lvert\alpha_H\rvert^2-\lvert\alpha_V\rvert^2}
\sum_{n,m,n',m'=0}^{\infty}
\frac{(\alpha_H^{*})^{n}\,(\alpha_V^{*})^{m}\,\alpha_H^{n'}\,\alpha_V^{m'}}{\sqrt{n!\,m!\,n'!\,m'!}}\,
\langle n,m\rvert\rho\lvert n',m'\rangle ,
$$

where $\lvert n,m\rangle$ has $n$ photons in mode $H$ and $m$ photons in mode $V$. For the pure state $\rho=\lvert\Psi\rangle\langle\Psi\rvert$ the matrix element is $\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle=\lvert\langle\alpha_H,\alpha_V\vert\Psi\rangle\rvert^2$.

$Q$ is the Husimi $Q$ function <a href="#ref-husimi1940">[5]</a>; a textbook introduction is in <a href="#ref-leonhardt1997">[7, Sec. 3.2.1]</a>. It measures how much the state $\rho$ overlaps with the coherent state $\lvert\boldsymbol\alpha\rangle$, i.e. with the classical field amplitudes $\alpha_H,\alpha_V$. Two of its properties matter immediately.

**It contains the answer.** At $\boldsymbol\alpha=0$ the coherent state is the vacuum: in the expansion above every term with a nonzero power of $\alpha_H$, $\alpha_H^{*}$, $\alpha_V$ or $\alpha_V^{*}$ vanishes, and only $n=m=n'=m'=0$ survives. So

<span id="eq7"></span>

$$
P(0,0)=\langle 0,0\rvert\rho\lvert 0,0\rangle=\pi^2\,Q(0).
\tag{7}
$$

**It is a probability density.** $Q\ge0$, because $\rho$ is a positive operator, so $\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle\ge0$ for every $\lvert\boldsymbol\alpha\rangle$. By the resolution of the identity, equation (11) of [Coherent states](../concepts_and_foundations/coherent_states.md#eq:coherent_identity), $\int d^4\alpha\,Q=\operatorname{Tr}\rho=1$.

So $Q$ is a probability distribution over the four real numbers $\operatorname{Re}\alpha_H,\operatorname{Im}\alpha_H,\operatorname{Re}\alpha_V,\operatorname{Im}\alpha_V$, and its height at the centre is $P(0,0)/\pi^2$. By the classical picture, what is needed next is its covariance matrix.

<span id="sigma-q"></span>

## The covariance matrix $\sigma_Q$ of the $Q$ function

Write $\langle f\rangle_Q=\int d^4\alpha\,Q(\boldsymbol\alpha)\,f(\boldsymbol\alpha)$ for the average over $Q$. The covariance matrix of $Q$ consists of the averages of products of two amplitudes. For complex amplitudes there are two kinds, with and without complex conjugation: $\langle\alpha_i\alpha_j^{*}\rangle_Q$ and $\langle\alpha_i\alpha_j\rangle_Q$ (and their complex conjugates), with $i,j\in\{H,V\}$.

### Averages over $Q$ are expectation values of ladder operators

Take the pure state $\rho=\lvert\Psi\rangle\langle\Psi\rvert$ and the expectation value $\langle\Psi\rvert\hat a_i\hat a_j^{\dagger}\lvert\Psi\rangle$. Insert the resolution of the identity $\mathbb{1}=\int\frac{d^4\alpha}{\pi^2}\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\rvert$ between the two operators. This splits the expectation value into the two matrix elements $\langle\Psi\rvert\hat a_i\lvert\boldsymbol\alpha\rangle$ and $\langle\boldsymbol\alpha\rvert\hat a_j^{\dagger}\lvert\Psi\rangle$. Coherent states are eigenstates of the annihilation operators, $\hat a_i\lvert\boldsymbol\alpha\rangle=\alpha_i\lvert\boldsymbol\alpha\rangle$, and, taking the adjoint, $\langle\boldsymbol\alpha\rvert\hat a_j^{\dagger}=\alpha_j^{*}\langle\boldsymbol\alpha\rvert$. So both operators turn into numbers:

<span id="eq8"></span>

$$
\begin{aligned}
\langle\Psi\rvert\hat a_i\hat a_j^{\dagger}\lvert\Psi\rangle
&=\int\frac{d^4\alpha}{\pi^2}\,\langle\Psi\rvert\hat a_i\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\rvert\hat a_j^{\dagger}\lvert\Psi\rangle
=\int\frac{d^4\alpha}{\pi^2}\,\alpha_i\alpha_j^{*}\,\langle\Psi\vert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\vert\Psi\rangle\\
&=\int\frac{d^4\alpha}{\pi^2}\,\alpha_i\alpha_j^{*}\,\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle
=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\alpha_i\alpha_j^{*}
=\langle\alpha_i\alpha_j^{*}\rangle_Q .
\end{aligned}
\tag{8}
$$

In the second line the two numbers $\langle\Psi\vert\boldsymbol\alpha\rangle$ and $\langle\boldsymbol\alpha\vert\Psi\rangle$ were swapped, so that $\langle\boldsymbol\alpha\vert\Psi\rangle\langle\Psi\vert\boldsymbol\alpha\rangle=\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle$.

The averages without conjugation work the same way. The identity is inserted where both operators can act on a coherent state: to the right of two annihilators, and to the left of two creators,

$$
\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle
=\int\frac{d^4\alpha}{\pi^2}\,\langle\Psi\rvert\hat a_i\hat a_j\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\vert\Psi\rangle
=\langle\alpha_i\alpha_j\rangle_Q,
\qquad
\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j^{\dagger}\lvert\Psi\rangle
=\langle\alpha_i^{*}\alpha_j^{*}\rangle_Q .
$$

This only works when every annihilator stands to the left of every creator: then $\hat a_i$ can act on $\lvert\boldsymbol\alpha\rangle$ to its right and $\hat a_j^{\dagger}$ on $\langle\boldsymbol\alpha\rvert$ to its left. (This order is called *antinormal* ordering. That the $Q$ function reproduces exactly the antinormally ordered expectation values is a general result of Cahill and Glauber <a href="#ref-cahill1969">[6]</a>.)

For a mixed state, the expectation value $\langle\Psi\rvert\hat A\lvert\Psi\rangle$ is replaced by $\operatorname{Tr}[\rho\,\hat A]$. A mixed $\rho$ is a weighted sum of pure states $\lvert\Psi_k\rangle\langle\Psi_k\rvert$, and both sides of [(8)](#eq8) are linear in $\rho$, so [(8)](#eq8) holds unchanged.

### All averages in one matrix

Collect the amplitudes in the vector $\mathbf v=(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})^T$. The $4\times4$ matrix of all averages $\langle v_iv_j^{*}\rangle_Q$ is, by [(8)](#eq8) and the rule "annihilation operators to the left of creation operators", the matrix of 16 expectation values that the Gaussian boson sampling literature calls $\sigma_Q$ <a href="#ref-hamilton2017">[1]</a>, <a href="#ref-kruse2019">[3]</a>:

<span id="eq9"></span>

$$
\sigma_Q=
\begin{pmatrix}
\langle\Psi\rvert\hat a_H\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H^{\dagger}\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_H^{\dagger}\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V^{\dagger}\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V^{\dagger}\lvert\Psi\rangle
\end{pmatrix},
\tag{9}
$$

i.e. every $\hat a_i$ in an entry is replaced by $\alpha_i$ and every $\hat a_i^{\dagger}$ by $\alpha_i^{*}$:

<span id="eq10"></span>

$$
\sigma_Q=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\mathbf v\,\mathbf v^{\dagger}.
\tag{10}
$$

So $\sigma_Q$ is the covariance matrix of the probability distribution $Q$. This is why only expectation values of **pairs** of ladder operators are needed, and nothing else.

**Most entries are redundant.** Two rules relate them:

- $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j^{\dagger}\lvert\Psi\rangle=\langle\Psi\rvert\hat a_j\hat a_i\lvert\Psi\rangle^{*}$, by taking the complex conjugate (adjoint) of the operator,
- $\langle\Psi\rvert\hat a_i\hat a_j^{\dagger}\lvert\Psi\rangle=\delta_{ij}+\langle\Psi\rvert\hat a_j^{\dagger}\hat a_i\lvert\Psi\rangle$, by the commutator $[\hat a_i,\hat a_j^{\dagger}]=\delta_{ij}$.

Applying them to every entry of [(9)](#eq9) rewrites it with only the types $\langle\Psi\rvert\hat a^{\dagger}\hat a\lvert\Psi\rangle$ and $\langle\Psi\rvert\hat a\hat a\lvert\Psi\rangle$:

$$
\sigma_Q=
\begin{pmatrix}
1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle & 1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*} & \langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*} & 1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle & \langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle\\
\langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle^{*} & \langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle^{*} & \langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle & 1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle
\end{pmatrix}.
$$

The lower half contains no new numbers: it repeats the upper half, complex-conjugated or reordered. So only eight expectation values have to be computed: the four $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j\lvert\Psi\rangle$ (upper-left $2\times2$ part) and the four $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$ (upper-right $2\times2$ part). Below they are abbreviated as the $2\times2$ matrices $N$ and $\mathcal{M}$ of [(16)](#eq16). These are only names for these parts of the full matrix above. Single operators are not needed: $\langle\Psi\rvert\hat a_H\lvert\Psi\rangle=\langle\Psi\rvert\hat a_V\lvert\Psi\rangle=0$, because photons come in pairs and $\hat a$ changes the photon number by one. This means the bell curve is centred at $0$.

**What the two kinds of averages mean.** Splitting one amplitude into real and imaginary parts, $\alpha_H=x_H+iy_H$, shows what each kind measures:

$$
\langle\alpha_H\alpha_H^{*}\rangle_Q=\langle x_H^2\rangle_Q+\langle y_H^2\rangle_Q,
\qquad
\langle\alpha_H\alpha_H\rangle_Q=\langle x_H^2\rangle_Q-\langle y_H^2\rangle_Q+2i\,\langle x_Hy_H\rangle_Q .
$$

- The averages *with* conjugation give the **size** of the cloud of $\alpha$ values. Quantum mechanically, $\langle\alpha_H\alpha_H^{*}\rangle_Q=\langle\Psi\rvert\hat a_H\hat a_H^{\dagger}\lvert\Psi\rangle=1+\langle\Psi\rvert\hat n_H\lvert\Psi\rangle$: vacuum noise plus photons. The $1$'s on the diagonal of $\sigma_Q$ are the spread that even the vacuum has, $Q_{\text{vac}}=\pi^{-2}e^{-|\alpha_H|^2-|\alpha_V|^2}$. The photon number $\langle\Psi\rvert\hat n_H\lvert\Psi\rangle$ is the quantity a detector responds to. The off-diagonal $\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle$ measures coherence between the arms.
- The averages *without* conjugation give the **shape**. If $\langle\alpha_H\alpha_H\rangle_Q=0$, then $\langle x_H^2\rangle_Q=\langle y_H^2\rangle_Q$ and $\langle x_Hy_H\rangle_Q=0$, so the cloud is round. If it is nonzero, the cloud is stretched into an ellipse, which is squeezing. Quantum mechanically, $\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle$ is the amplitude for **removing a pair** of photons. It is zero for vacuum and thermal light, and nonzero here precisely because SPDC creates photons in pairs. (For laser light $\langle\alpha\rvert\hat a\hat a\lvert\alpha\rangle=\alpha^2$ is nonzero too, but only because $\langle\alpha\rvert\hat a\lvert\alpha\rangle=\alpha\neq0$. For our states $\langle\Psi\rvert\hat a\lvert\Psi\rangle=0$, so a nonzero $\langle\Psi\rvert\hat a\hat a\lvert\Psi\rangle$ is a genuine pair correlation.)


## Height of a bell curve

Assume that $Q$ is a Gaussian bell curve centred at $0$. (Centred at $0$, because $\langle\Psi\rvert\hat a_H\lvert\Psi\rangle=\langle\Psi\rvert\hat a_V\lvert\Psi\rangle=0$, see [above](#sigma-q). That it is a bell curve at all is the one general fact the formalism imports: the state $\lvert\Psi\rangle$ is a Gaussian state, and beam splitters with vacuum inputs, which model the detector losses of [Detector efficiency](detector_efficiency.md), map Gaussian states to Gaussian states <a href="#ref-weedbrook2012">[8]</a>, <a href="#ref-ferraro2005">[9]</a>. The [numerical check](../dashboard/comparison.md#numerical-check) confirms it for this case.) [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md) gives its height at the centre for **real** variables. $Q$, however, is a function of the complex amplitudes $\alpha_H,\alpha_V$, and $\sigma_Q$ is written with $\alpha$ and $\alpha^{*}$. The calculation below translates between the two descriptions in four steps.

**Step 1: real variables.** Split each amplitude into real and imaginary part, $\alpha_H=x_H+iy_H$ and $\alpha_V=x_V+iy_V$, and collect the four real numbers in

$$
\mathbf x=\begin{pmatrix}x_H\\x_V\\y_H\\y_V\end{pmatrix}.
$$

The measure is $d^4\alpha=d^2\alpha_H\,d^2\alpha_V=dx_H\,dy_H\,dx_V\,dy_V$, i.e. ordinary integration over $\mathbb R^4$. So $Q$ is an ordinary probability density of four real variables. Its covariance matrix is the real symmetric $4\times4$ matrix

<span id="eq11a"></span>

$$
\Sigma_{\mathbb R}=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\mathbf x\,\mathbf x^T,
\qquad
\left(\Sigma_{\mathbb R}\right)_{ij}=\langle x_ix_j\rangle_Q ,
\tag{11a}
$$

and equation (4) of [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md#gauss:real) with $n=4$ variables gives

<span id="eq11b"></span>

$$
Q=\frac{1}{(2\pi)^{2}\sqrt{\det\Sigma_{\mathbb R}}}\exp\!\left(-\tfrac12\,\mathbf x^T\Sigma_{\mathbb R}^{-1}\mathbf x\right).
\tag{11b}
$$

The remaining task is to express $\det\Sigma_{\mathbb R}$ and $\mathbf x^T\Sigma_{\mathbb R}^{-1}\mathbf x$ through $\sigma_Q$ and $\mathbf v=(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})^T$.

**Step 2: from $\mathbf x$ to $\mathbf v$.** Since $\alpha_j=x_j+iy_j$ and $\alpha_j^{*}=x_j-iy_j$, the two vectors are related by a constant matrix $T$, written in $2\times2$ blocks:

<span id="eq11c"></span>

$$
\mathbf v=
\begin{pmatrix}\alpha_H\\\alpha_V\\\alpha_H^{*}\\\alpha_V^{*}\end{pmatrix}
=
\underbrace{\begin{pmatrix}1&0&i&0\\0&1&0&i\\1&0&-i&0\\0&1&0&-i\end{pmatrix}}_{T=\left(\begin{smallmatrix}\mathbb{1}&i\mathbb{1}\\ \mathbb{1}&-i\mathbb{1}\end{smallmatrix}\right)}
\begin{pmatrix}x_H\\x_V\\y_H\\y_V\end{pmatrix}
=T\,\mathbf x .
\tag{11c}
$$

Two properties of $T$ are needed. Multiplying out the blocks,

$$
T\,T^{\dagger}
=\begin{pmatrix}\mathbb{1}&i\mathbb{1}\\ \mathbb{1}&-i\mathbb{1}\end{pmatrix}
\begin{pmatrix}\mathbb{1}&\mathbb{1}\\ -i\mathbb{1}&i\mathbb{1}\end{pmatrix}
=\begin{pmatrix}\mathbb{1}+\mathbb{1}&\mathbb{1}-\mathbb{1}\\ \mathbb{1}-\mathbb{1}&\mathbb{1}+\mathbb{1}\end{pmatrix}
=2\,\mathbb{1}_4 ,
\qquad\text{so}\qquad
T^{-1}=\tfrac12\,T^{\dagger},
$$

and, taking the determinant of $TT^{\dagger}=2\,\mathbb{1}_4$,

$$
\det T\,\det T^{\dagger}=\lvert\det T\rvert^2=\det(2\,\mathbb{1}_4)=2^4=16 .
$$

**Step 3: the two covariance matrices.** Inserting $\mathbf v=T\mathbf x$ and $\mathbf v^{\dagger}=\mathbf x^{\dagger}T^{\dagger}=\mathbf x^TT^{\dagger}$ (the $x_j,y_j$ are real) into [(10)](#eq10), and pulling the constant matrices out of the integral:

<span id="eq11d"></span>

$$
\sigma_Q=\int d^4\alpha\;Q\,\mathbf v\,\mathbf v^{\dagger}
=T\left(\int d^4\alpha\;Q\,\mathbf x\,\mathbf x^T\right)T^{\dagger}
=T\,\Sigma_{\mathbb R}\,T^{\dagger}.
\tag{11d}
$$

This gives both quantities needed in [(11b)](#eq11b):

- **Determinant.** $\det\sigma_Q=\det T\,\det\Sigma_{\mathbb R}\,\det T^{\dagger}=\lvert\det T\rvert^2\det\Sigma_{\mathbb R}=16\,\det\Sigma_{\mathbb R}$, i.e.

    $$
    \det\Sigma_{\mathbb R}=\frac{\det\sigma_Q}{16}.
    $$

- **Exponent.** From [(11d)](#eq11d), $\sigma_Q^{-1}=(T\Sigma_{\mathbb R}T^{\dagger})^{-1}=(T^{\dagger})^{-1}\Sigma_{\mathbb R}^{-1}T^{-1}$. With $\mathbf x=T^{-1}\mathbf v$ and $\mathbf x^T=\mathbf x^{\dagger}=\mathbf v^{\dagger}(T^{\dagger})^{-1}$:

    <span id="eq11e"></span>

    $$
    \mathbf x^T\Sigma_{\mathbb R}^{-1}\mathbf x
    =\mathbf v^{\dagger}(T^{\dagger})^{-1}\,\Sigma_{\mathbb R}^{-1}\,T^{-1}\mathbf v
    =\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v .
    \tag{11e}
    $$

**Step 4: insert into [(11b)](#eq11b).** The prefactor becomes

$$
(2\pi)^2\sqrt{\det\Sigma_{\mathbb R}}
=4\pi^2\sqrt{\frac{\det\sigma_Q}{16}}
=4\pi^2\,\frac{\sqrt{\det\sigma_Q}}{4}
=\pi^2\sqrt{\det\sigma_Q},
$$

and the exponent is [(11e)](#eq11e). Hence

<span id="eq11"></span>

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2\sqrt{\det\sigma_Q}}\exp\!\left(-\tfrac12\,\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v\right),
\qquad
Q(0)=\frac{1}{\pi^2\sqrt{\det\sigma_Q}} ,
\tag{11}
$$

where $Q(0)$ follows from $\mathbf v=0$ and $e^{0}=1$. So the factor $(2\pi)^2$ of four real variables turns into $\pi^2$, because $\lvert\det T\rvert^2=16$ cancels the $2^2$ inside $(2\pi)^2$. The same calculation for one mode is in [Complex variables](../concepts_and_foundations/gaussian_peak_height.md#gauss:complex).

**Check with the vacuum.** For $\rho=\lvert 0,0\rangle\langle 0,0\rvert$, directly from [(6)](#eq6) and $\langle 0\vert\alpha\rangle=e^{-\lvert\alpha\rvert^2/2}$ (the $n=0$ term of the Fock expansion, equation (1) of [Coherent states](../concepts_and_foundations/coherent_states.md)):

$$
Q_{\text{vac}}(\boldsymbol\alpha)=\frac{1}{\pi^2}\,\lvert\langle 0,0\vert\alpha_H,\alpha_V\rangle\rvert^2=\frac{1}{\pi^2}\,e^{-\lvert\alpha_H\rvert^2-\lvert\alpha_V\rvert^2}.
$$

From [(11)](#eq11): for the vacuum every entry of [(9)](#eq9) vanishes except $\langle 0\rvert\hat a_i\hat a_i^{\dagger}\lvert 0\rangle=1$, so $\sigma_Q=\mathbb{1}$, $\det\sigma_Q=1$ and

$$
\mathbf v^{\dagger}\mathbf v=\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2+\lvert\alpha_H^{*}\rvert^2+\lvert\alpha_V^{*}\rvert^2=2\left(\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2\right),
\qquad
Q=\frac{1}{\pi^2}\,e^{-\frac12\cdot2\left(\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2\right)}=\frac{1}{\pi^2}\,e^{-\lvert\alpha_H\rvert^2-\lvert\alpha_V\rvert^2}\ ✓
$$

**Result.** Combining [(11)](#eq11) with [(7)](#eq7):

$$
P(0,0)=\pi^2\,Q(0)=\pi^2\cdot\frac{1}{\pi^2\sqrt{\det\sigma_Q}},
$$

i.e.

<span id="eq12"></span>

$$
\boxed{\;P(0,0)=\frac{1}{\sqrt{\det\sigma_Q}}\;}
\tag{12}
$$

This is the zero-photon case of the central formula of Gaussian boson sampling <a href="#ref-hamilton2017">[1]</a>. The square root is the ordinary positive one, because $\sigma_Q$ is a covariance matrix and $\det\sigma_Q>0$.

<span id="psi-cov"></span>

## $\sigma_Q$ for the state $\lvert\Psi\rangle$

Equation [(12)](#eq12) holds for any state whose $Q$ function is a bell curve centred at $0$. For the state $\lvert\Psi\rangle$ of [(2)](notation.md#eq2), the eight independent entries of $\sigma_Q$ remain to be computed.

**Why $\sigma_Q$ rather than $\lvert\Psi\rangle$?** The detector efficiency ([Detector efficiency](detector_efficiency.md)) turns $\lvert\Psi\rangle$ into a mixed state, which no longer has the exponential form [(2)](notation.md#eq2). The covariance matrix, by contrast, keeps its meaning and changes in a very simple way: its entries get multiplied by factors of $\sqrt{\eta}$.

### Why we look at $\hat a\lvert\Psi\rangle$

So the numbers needed are

$$
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle,
\qquad
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle,
\qquad
\dots
$$

The brute-force way is to expand $\lvert\Psi\rangle$ in Fock states and evaluate double sums over photon numbers for a general HWP angle. That works, but it is messy.

There is a shortcut. In every one of these expectation values, the **right-most operator is an annihilation operator acting directly on $\lvert\Psi\rangle$**. If we know what $\hat a_H\lvert\Psi\rangle$ and $\hat a_V\lvert\Psi\rangle$ are, we can replace them and the expectation value simplifies. The next subsection shows that removing a photon from $\lvert\Psi\rangle$ is the same as *adding* one, times $\lambda M$. Inserted into an expectation value, this turns it into a combination of *other* expectation values. This gives a small linear system of equations that yields all of them at once, eq. [(18)](#eq18), without any Fock sums.

The idea is familiar from coherent states, where $\hat a\lvert\alpha\rangle=\alpha\lvert\alpha\rangle$ replaces the annihilation operator by a number. For the squeezed state $\lvert\Psi\rangle$ it is replaced by creation operators instead.

<span id="key-relation"></span>

### The key relation

Call the exponent of [(2)](notation.md#eq2) $\hat X$. Here $\mathbf{\hat a^{\dagger}}=(\hat a_H^{\dagger},\hat a_V^{\dagger})^T$ is the column of creation operators, and $(\mathbf{\hat a^{\dagger}})^T$ is the same entries as a row (a plain transpose, not a dagger). Row times $M$ times column is a sum over the four entries of [(3)](notation.md#eq3), and the two off-diagonal terms are equal because $\hat a_H^{\dagger}\hat a_V^{\dagger}=\hat a_V^{\dagger}\hat a_H^{\dagger}$:

<span id="eq13"></span>

$$
\hat X:=\frac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^T M\mathbf{\hat a^{\dagger}}
=\frac{\lambda}{2}\sum_{i,j\in\{H,V\}}M_{ij}\,\hat a_i^{\dagger}\hat a_j^{\dagger}
=\frac{\lambda}{2}\left(S_4\,\hat a_H^{\dagger 2}-2C_4\,\hat a_H^{\dagger}\hat a_V^{\dagger}-S_4\,\hat a_V^{\dagger 2}\right).
\tag{13}
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

The commutator is linear in its second argument (equation (1) of [Commutator with an operator exponential](../concepts_and_foundations/commutator_exponential.md#comm:linear)). So $[\hat a_H,\hat X]$ is the sum of the three commutators above, weighted with the coefficients of [(13)](#eq13):

$$
[\hat a_H,\hat X]
=\frac{\lambda}{2}\left(S_4\cdot2\hat a_H^{\dagger}-2C_4\cdot\hat a_V^{\dagger}-S_4\cdot0\right)
=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right).
$$

For $\hat a_V$ the roles swap: $[\hat a_V,\hat a_H^{\dagger 2}]=0$, $[\hat a_V,\hat a_H^{\dagger}\hat a_V^{\dagger}]=\hat a_H^{\dagger}$ and $[\hat a_V,\hat a_V^{\dagger 2}]=2\hat a_V^{\dagger}$, so $[\hat a_V,\hat X]=\frac{\lambda}{2}\left(-2C_4\,\hat a_H^{\dagger}-S_4\cdot2\hat a_V^{\dagger}\right)$. Together:

<span id="eq14"></span>

$$
[\hat a_H,\hat X]=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right),
\qquad
[\hat a_V,\hat X]=\lambda\left(-C_4\,\hat a_H^{\dagger}-S_4\,\hat a_V^{\dagger}\right).
\tag{14}
$$

Now apply $\hat a_H$ to $\lvert\Psi\rangle=\Lambda e^{\hat X}\lvert 0,0\rangle$. Writing $\hat a_He^{\hat X}=[\hat a_H,e^{\hat X}]+e^{\hat X}\hat a_H$ and using $\hat a_H\lvert 0,0\rangle=0$:

$$
\hat a_H\lvert\Psi\rangle
=\Lambda\left([\hat a_H,e^{\hat X}]+e^{\hat X}\hat a_H\right)\lvert 0,0\rangle
=\Lambda\,[\hat a_H,e^{\hat X}]\lvert 0,0\rangle .
$$

It remains to evaluate $[\hat a_H,e^{\hat X}]$. By [(14)](#eq14), $[\hat a_H,\hat X]$ contains only creation operators, and so does $\hat X$, so the two commute. For exactly this situation, equation (4) of [Commutator with an operator exponential](../concepts_and_foundations/commutator_exponential.md#comm:exp) gives

$$
[\hat a_H,e^{\hat X}]=[\hat a_H,\hat X]\,e^{\hat X},
$$

the operator version of $\frac{d}{dx}e^{f(x)}=f'(x)\,e^{f(x)}$. The same holds for $\hat a_V$. Together with [(14)](#eq14):

<span id="eq15"></span>

$$
\begin{aligned}
\hat a_H\lvert\Psi\rangle&=\lambda\left(S_4\,\hat a_H^{\dagger}-C_4\,\hat a_V^{\dagger}\right)\lvert\Psi\rangle,\\
\hat a_V\lvert\Psi\rangle&=\lambda\left(-C_4\,\hat a_H^{\dagger}-S_4\,\hat a_V^{\dagger}\right)\lvert\Psi\rangle,
\end{aligned}
\qquad\text{i.e.}\qquad
\mathbf{\hat a}\lvert\Psi\rangle=\lambda M\,\mathbf{\hat a^{\dagger}}\lvert\Psi\rangle .
\tag{15}
$$

Equation [(15)](#eq15) says that an annihilation operator acting on $\lvert\Psi\rangle$ can be traded for creation operators. It is all that is needed to compute the covariance matrix.

**Check at $\vartheta=0$.** Here $S_4=0$ and $C_4=1$, and [(15)](#eq15) reads $\hat a_H\lvert\Psi\rangle=-\lambda\,\hat a_V^{\dagger}\lvert\Psi\rangle$. At this angle the state is $\lvert\Psi\rangle=\Lambda\sum_n(-\lambda)^n\lvert n,n\rangle$ (see [(23)](#eq23) below). Both sides can be evaluated in the Fock basis:

$$
\hat a_H\lvert\Psi\rangle=\Lambda\sum_{n}(-\lambda)^n\sqrt{n}\,\lvert n-1,n\rangle,
\qquad
-\lambda\,\hat a_V^{\dagger}\lvert\Psi\rangle=\Lambda\sum_{m}(-\lambda)^{m+1}\sqrt{m+1}\,\lvert m,m+1\rangle .
$$

Renaming $m=n-1$ in the second sum makes the two sides identical.

Physically, the photons of $\lvert\Psi\rangle$ come in $H$–$V$ pairs. Removing one $H$ photon leaves a state with one more $V$ photon than $H$ photons, which is the same as adding a $V$ photon to the pair state, up to the factor $-\lambda$. For other angles the HWP mixes $H$ and $V$, and $M$ keeps track of which photon is "added".

### The two blocks $N$ and $\mathcal{M}$

As shown [above](#sigma-q), the eight independent second-order expectation values are abbreviated by two $2\times2$ matrices:

<span id="eq16"></span>

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
\tag{16}
$$

$N$ holds photon numbers, with mean photon numbers on its diagonal. $\mathcal{M}$ holds the pair correlations created by SPDC. All other second-order expectation values follow from these through $[\hat a_i,\hat a_j^{\dagger}]=\delta_{ij}$ and complex conjugation.

#### One entry step by step

Each entry is computed with the same three moves:

1. replace the annihilator next to the ket by [(15)](#eq15),
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

<span id="eq17a"></span>

$$
\begin{aligned}
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-C_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\Big),\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}-C_4\,\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle^{*}\Big),\\
\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-S_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\Big),\\
\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}-S_4\,\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle^{*}\Big),
\end{aligned}
\tag{17a}
$$

and for the pair type $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$, again the right-hand operator $\hat a_j$ is replaced:

<span id="eq17b"></span>

$$
\begin{aligned}
\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-C_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\Big),\\
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-S_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\Big),\\
\langle\Psi\rvert\hat a_V\hat a_H\lvert\Psi\rangle&=\lambda\Big(S_4\,\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle-C_4\,\big(1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle\big)\Big),\\
\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle&=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle-S_4\,\big(1+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_V\lvert\Psi\rangle\big)\Big).
\end{aligned}
\tag{17b}
$$

[(17a)](#eq17a) and [(17b)](#eq17b) are eight linear equations for the eight unknown expectation values. No Fock-state sums were needed.

#### Matrix form

The eight equations have a pattern. In every line, the coefficients $S_4$, $-C_4$ (first line of [(15)](#eq15)) or $-C_4$, $-S_4$ (second line of [(15)](#eq15)) are a row of $M$. So the equations are matrix products with $M$. With the matrices $N$ and $\mathcal{M}$ of [(16)](#eq16), [(17a)](#eq17a) is entry by entry the product $\lambda\,\mathcal{M}^{*}M$. For example, the third line is the $(H,V)$ entry:

$$
\big(\lambda\,\mathcal{M}^{*}M\big)_{HV}
=\lambda\Big(\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}\,M_{HV}+\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\,M_{VV}\Big)
=\lambda\Big(-C_4\,\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle^{*}-S_4\,\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle^{*}\Big)
=\langle\Psi\rvert\hat a_H^{\dagger}\hat a_V\lvert\Psi\rangle .
$$

Likewise, [(17b)](#eq17b) is entry by entry $\lambda M+\lambda N^TM$, where $\lambda M$ collects the terms with the $1$'s. For example, the $(H,V)$ entry:

$$
\big(\lambda M+\lambda N^TM\big)_{HV}
=\lambda\Big(M_{HV}+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\,M_{HV}+\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\,M_{VV}\Big)
=\lambda\Big(-C_4\big(1+\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle\big)-S_4\,\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle\Big)
=\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle .
$$

Here $(N^T)_{HV}=N_{VH}=\langle\Psi\rvert\hat a_V^{\dagger}\hat a_H\lvert\Psi\rangle$. Together:

<span id="eq18"></span>

$$
N=\lambda\,\mathcal{M}^{*}M,
\qquad
\mathcal{M}=\lambda M+\lambda\,N^TM .
\tag{18}
$$

#### Solving for $\mathcal{M}$

Take the transpose of the first equation of [(18)](#eq18). With $(XY)^T=Y^TX^T$ and the symmetry of $M$ and $\mathcal{M}$ ($M^T=M$, $(\mathcal{M}^{*})^T=\mathcal{M}^{*}$):

$$
N^T=\lambda\,(\mathcal{M}^{*}M)^T=\lambda\,M\mathcal{M}^{*}.
$$

Inserting this into the second equation of [(18)](#eq18) gives an equation for $\mathcal{M}$ alone:

<span id="eq19"></span>

$$
\mathcal{M}=\lambda M+\lambda^2\,M\mathcal{M}^{*}M .
\tag{19}
$$

Equation [(19)](#eq19) contains $\mathcal{M}^{*}$ on the right. Its complex conjugate gives an expression for it. Since $\lambda$ and $M$ are real,

$$
\mathcal{M}^{*}=\lambda M+\lambda^2\,M\mathcal{M}M .
$$

Insert this back into the right-hand side of [(19)](#eq19):

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

<span id="eq20"></span>

$$
\mathcal{M}=\frac{\lambda}{1-\lambda^2}\,M .
\tag{20}
$$

So the pair matrix $\mathcal{M}$ is the HWP matrix $M$ times a number that depends only on $\lambda$. The derivation determines $\mathcal{M}$ uniquely: no guess was made.

The photon-number matrix follows from the first equation of [(18)](#eq18), using $\mathcal{M}^{*}=\mathcal{M}$ (it is real) and $M^2=\mathbb{1}$: $N=\lambda\,\mathcal{M}^{*}M=\frac{\lambda^2}{1-\lambda^2}\,\mathbb{1}$.

#### The abbreviations $\nu$ and $\mu$

The two numbers in these results appear throughout the rest of this section, so they get names:

<span id="eq21"></span>

$$
\nu=\frac{\lambda^2}{1-\lambda^2},
\qquad
\mu=\frac{\lambda}{1-\lambda^2}.
\tag{21}
$$

With $\lambda=\tanh r$ and $1-\tanh^2 r=1/\cosh^2 r$, they are $\nu=\sinh^2 r$ (the mean photon number per arm) and $\mu=\sinh r\cosh r$ (the pair amplitude). With these names, the result is

<span id="eq22"></span>

$$
N=\nu\,\mathbb{1},
\qquad
\mathcal{M}=\mu M .
\tag{22}
$$

**Reading it physically:**

- Each arm carries $\nu=\sinh^2r$ photons on average, for every HWP angle. The HWP only redistributes the *pairs*, not the mean photon number.
- At $\vartheta=0$: $S_4=0$ and $C_4=1$. Only $\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle=-\mu$ is nonzero, so each pair is split into one $H$ and one $V$ photon.
- At $\vartheta=\pi/8$: $S_4=1$ and $C_4=0$. Now $\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle=\mu$ and $\langle\Psi\rvert\hat a_V\hat a_V\lvert\Psi\rangle=-\mu$, so both photons of a pair go to the same port, as in Hong-Ou-Mandel bunching.

In the picture of the $Q$ function as a cloud of amplitudes ([above](#sigma-q)): at $\vartheta=0$ each arm alone is a round cloud and only $\langle\alpha_H\alpha_V\rangle_Q=-\mu$ correlates the arms; at $\vartheta=\pi/8$ each arm alone is an ellipse.

**Cross-check at $\vartheta=0$.** Here $\lvert\Psi\rangle=\Lambda\sum_n(-\lambda)^n\lvert n,n\rangle$. With $\hat a_H\hat a_V\lvert n+1,n+1\rangle=(n+1)\lvert n,n\rangle$:

<span id="eq23"></span>

$$
\langle\Psi\rvert\hat n_H\lvert\Psi\rangle=(1-\lambda^2)\sum_n n\lambda^{2n}=\frac{\lambda^2}{1-\lambda^2}=\nu,
\qquad
\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle=(1-\lambda^2)\sum_n(n+1)(-\lambda)^{2n+1}=-\frac{\lambda}{1-\lambda^2}=-\mu .
\tag{23}
$$

Two identities used later:

<span id="eq24"></span>

$$
1+\nu=\frac{1}{1-\lambda^2},
\qquad
\nu^2-\mu^2=\frac{\lambda^4-\lambda^2}{(1-\lambda^2)^2}=-\nu .
\tag{24}
$$

### The matrix $\sigma_Q$

With $N$ and $\mathcal{M}$ known, the covariance matrix [(9)](#eq9) can be filled in. Its rewritten form from [above](#sigma-q) is, in terms of the blocks of [(16)](#eq16),

<span id="eq25"></span>

$$
\sigma_Q=
\begin{pmatrix}
\mathbb{1}+N^T & \mathcal{M}\\
\mathcal{M}^{*} & \mathbb{1}+N
\end{pmatrix}.
\tag{25}
$$

Plugging in [(22)](#eq22) for $\lvert\Psi\rangle$:

<span id="eq26"></span>

$$
\sigma_Q=
\begin{pmatrix}
1+\nu & 0 & \mu S_4 & -\mu C_4\\
0 & 1+\nu & -\mu C_4 & -\mu S_4\\
\mu S_4 & -\mu C_4 & 1+\nu & 0\\
-\mu C_4 & -\mu S_4 & 0 & 1+\nu
\end{pmatrix}.
\tag{26}
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

<p id="ref-husimi1940">
[5] K. Husimi,
<em>Some Formal Properties of the Density Matrix</em>, Proc. Phys.-Math. Soc. Jpn. <strong>22</strong>, 264 (1940). Available: https://doi.org/10.11429/ppmsj1919.22.4_264
</p>

<p id="ref-cahill1969">
[6] K. E. Cahill, R. J. Glauber,
<em>Density Operators and Quasiprobability Distributions</em>, Phys. Rev. <strong>177</strong>, 1882 (1969). Available: https://doi.org/10.1103/PhysRev.177.1882
</p>

<p id="ref-leonhardt1997">
[7] U. Leonhardt,
<em>Measuring the Quantum State of Light</em>, Cambridge University Press, Cambridge (1997).
</p>

<p id="ref-weedbrook2012">
[8] C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, S. Lloyd,
<em>Gaussian quantum information</em>, Rev. Mod. Phys. <strong>84</strong>, 621 (2012). Available: https://arxiv.org/abs/1110.3234
</p>

<p id="ref-ferraro2005">
[9] A. Ferraro, S. Olivares, M. G. A. Paris,
<em>Gaussian states in continuous variable quantum information</em>, 2005. Available: https://arxiv.org/abs/quant-ph/0503237
</p>
