# Vacuum probability: why $P(0,0)=1/\sqrt{\det\sigma_Q}$

[Covariance matrix](covariance_matrix.md) computed the $4\times4$ matrix $\sigma_Q$ of expectation values of pairs of ladder operators. This page shows why that matrix is enough to obtain the probability $P(0,0)=\langle 0,0\rvert\rho\lvert 0,0\rangle$ that both modes are empty. The argument has three steps:

1. **A probability distribution that contains $P(0,0)$.** With coherent states one builds a probability distribution $Q(\alpha_H,\alpha_V)$ over two complex numbers. Its value at $\alpha_H=\alpha_V=0$ is $P(0,0)/\pi^2$, eq. (22).
2. **Its covariance matrix is $\sigma_Q$.** The averages $\langle\alpha_i\alpha_j^{*}\rangle_Q$ and $\langle\alpha_i\alpha_j\rangle_Q$ over this distribution are exactly the entries of $\sigma_Q$, eq. (24).
3. **Height of a bell curve.** If $Q$ is a bell curve (Gaussian) centred at $0$, its height at the centre follows directly from the determinant of its covariance matrix. Together with step 1 this gives $P(0,0)=1/\sqrt{\det\sigma_Q}$, eq. (26).

The last section checks with the main derivation that $Q$ is indeed a bell curve for $\lvert\Psi\rangle$.

!!! note "Concepts used on this page"
    - **Coherent states** $\lvert\alpha\rangle$ ([Coherent states](../concepts_and_foundations/coherent_states.md)): eigenstates of the annihilation operator, $\hat a\lvert\alpha\rangle=\alpha\lvert\alpha\rangle$ with a complex number $\alpha$, and the resolution of the identity $\int\frac{d^2\alpha}{\pi}\lvert\alpha\rangle\langle\alpha\rvert=\mathbb{1}$, equation (11) of that page. Here $d^2\alpha=d(\operatorname{Re}\alpha)\,d(\operatorname{Im}\alpha)$ integrates over the complex plane. For two modes, $\lvert\boldsymbol\alpha\rangle=\lvert\alpha_H,\alpha_V\rangle$ and $d^4\alpha=d^2\alpha_H\,d^2\alpha_V$, so the identity reads $\int\frac{d^4\alpha}{\pi^2}\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\rvert=\mathbb{1}$.
    - **Density operator** $\rho$: for the pure state of the main derivation $\rho=\lvert\Psi\rangle\langle\Psi\rvert$, so that $\operatorname{Tr}[\rho\,\hat A]=\langle\Psi\rvert\hat A\lvert\Psi\rangle$ for any operator $\hat A$. The density operator is needed because after the detector losses of [Detector efficiency](detector_efficiency.md) the state is mixed and has no state vector.
    - **Peak height of a Gaussian** ([Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md)): the height of a bell curve at its centre is $1/\sqrt{\det}$ of its covariance matrix, up to factors of $\pi$.
    - **The matrix $\sigma_Q$** of [(6)](covariance_matrix.md#eq6) and its value [(20)](covariance_matrix.md#eq20) for $\lvert\Psi\rangle$.

## The $Q$ function

For any two-mode state $\rho$, define, with the two-mode coherent states $\lvert\boldsymbol\alpha\rangle=\lvert\alpha_H,\alpha_V\rangle$ of the [main derivation](../theory/cc_derivation.md#tmsv_coherent_identity),

<span id="eq21"></span>

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2}\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle .
\tag{21}
$$

$Q$ is the Husimi $Q$ function <a href="#ref-husimi1940">[5]</a>; a textbook introduction is in <a href="#ref-leonhardt1997">[7, Sec. 3.2.1]</a>. It measures how much the state $\rho$ overlaps with the coherent state $\lvert\boldsymbol\alpha\rangle$, i.e. with the classical field amplitudes $\alpha_H,\alpha_V$. It has three properties.

**It contains the answer.** At $\boldsymbol\alpha=0$ the coherent state is the vacuum, so

<span id="eq22"></span>

$$
P(0,0)=\langle 0,0\rvert\rho\lvert 0,0\rangle=\pi^2\,Q(0).
\tag{22}
$$

**It is a probability density.** $Q\ge0$, because $\rho$ is a positive operator, so $\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle\ge0$ for every $\lvert\boldsymbol\alpha\rangle$. By the resolution of the identity, equation (11) of [Coherent states](../concepts_and_foundations/coherent_states.md#eq:coherent_identity), $\int d^4\alpha\,Q=\operatorname{Tr}\rho=1$.

**Its covariance matrix is $\sigma_Q$.** For example, insert the resolution of the identity $\mathbb{1}=\int\frac{d^4\alpha}{\pi^2}\lvert\boldsymbol\alpha\rangle\langle\boldsymbol\alpha\rvert$ between the two operators. Because coherent states are eigenstates of the annihilation operators, $\hat a_i\lvert\boldsymbol\alpha\rangle=\alpha_i\lvert\boldsymbol\alpha\rangle$, and, taking the adjoint, $\langle\boldsymbol\alpha\rvert\hat a_j^{\dagger}=\alpha_j^{*}\langle\boldsymbol\alpha\rvert$, both operators turn into numbers:

<span id="eq23"></span>

$$
\operatorname{Tr}\!\left[\rho\,\hat a_i\hat a_j^{\dagger}\right]
=\operatorname{Tr}\!\left[\rho\,\hat a_i\,\mathbb{1}\,\hat a_j^{\dagger}\right]
=\int\frac{d^4\alpha}{\pi^2}\,\alpha_i\alpha_j^{*}\,\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle
=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\alpha_i\alpha_j^{*},
\tag{23}
$$

and in the same way $\operatorname{Tr}\!\left[\rho\,\hat a_i\hat a_j\right]=\int Q\,\alpha_i\alpha_j$. The operators must be in the order "annihilators left", so that $\hat a_i$ acts on $\lvert\boldsymbol\alpha\rangle$ to its right and $\hat a_j^{\dagger}$ on $\langle\boldsymbol\alpha\rvert$ to its left. This is exactly the rule of [(6)](covariance_matrix.md#eq6). (This order is called *antinormal* ordering. That the $Q$ function reproduces exactly the antinormally ordered expectation values is a general result of Cahill and Glauber <a href="#ref-cahill1969">[6]</a>.) Hence, with $\mathbf v=(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})^T$,

<span id="eq24"></span>

$$
\sigma_Q=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\mathbf v\,\mathbf v^{\dagger}.
\tag{24}
$$

So $\sigma_Q$ is the covariance matrix of the probability distribution $Q$. The $1$'s on its diagonal are the spread that even the vacuum has: $Q_{\text{vac}}=\pi^{-2}e^{-|\alpha_H|^2-|\alpha_V|^2}$.

**Classical counterpart.** Writing $\langle f\rangle_Q=\int d^4\alpha\,Q(\boldsymbol\alpha)\,f(\boldsymbol\alpha)$ for the average over $Q$, equation (24) says that $\sigma_Q$ is the matrix [(6)](covariance_matrix.md#eq6) with every $\hat a_i$ replaced by $\alpha_i$ and every $\hat a_i^{\dagger}$ by $\alpha_i^{*}$, e.g. $\operatorname{Tr}\!\left[\rho\,\hat a_H\hat a_V^{\dagger}\right]=\langle\alpha_H\alpha_V^{*}\rangle_Q$. The rule "annihilators to the left" is what makes this replacement exact.

For a complex random variable there are two kinds of averages, with and without complex conjugation. Splitting one amplitude into real and imaginary parts, $\alpha_H=x_H+iy_H$, shows what each kind measures:

$$
\langle\alpha_H\alpha_H^{*}\rangle_Q=\langle x_H^2\rangle_Q+\langle y_H^2\rangle_Q,
\qquad
\langle\alpha_H\alpha_H\rangle_Q=\langle x_H^2\rangle_Q-\langle y_H^2\rangle_Q+2i\,\langle x_Hy_H\rangle_Q .
$$

- The averages *with* conjugation (entries of the type $\langle\Psi\rvert\hat a_i^{\dagger}\hat a_j\lvert\Psi\rangle$) give the **size** of the cloud of $\alpha$ values. Quantum mechanically, $\langle\alpha_H\alpha_H^{*}\rangle_Q=\operatorname{Tr}\!\left[\rho\,\hat a_H\hat a_H^{\dagger}\right]=1+\operatorname{Tr}\!\left[\rho\,\hat n_H\right]$: vacuum noise plus photons.
- The averages *without* conjugation (entries of the type $\langle\Psi\rvert\hat a_i\hat a_j\lvert\Psi\rangle$) give the **shape**. If $\langle\alpha_H\alpha_H\rangle_Q=0$, then $\langle x_H^2\rangle_Q=\langle y_H^2\rangle_Q$ and $\langle x_Hy_H\rangle_Q=0$, so the cloud is round. If it is nonzero, the cloud is stretched into an ellipse, which is squeezing.

In this picture the two angles discussed after [(16)](covariance_matrix.md#eq16) look as follows: at $\vartheta=0$ each arm alone is a round cloud and only $\langle\alpha_H\alpha_V\rangle_Q=-\mu$ correlates the arms; at $\vartheta=\pi/8$ each arm alone is an ellipse.

## Height of a bell curve

Assume that $Q$ is a Gaussian bell curve centred at $0$. (Centred at $0$, because $\langle\Psi\rvert\hat a_H\lvert\Psi\rangle=\langle\Psi\rvert\hat a_V\lvert\Psi\rangle=0$, see [Covariance matrix](covariance_matrix.md#why-cov). That it is a bell curve at all is checked in the next section.) [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md) gives its height at the centre for **real** variables. $Q$, however, is a function of the complex amplitudes $\alpha_H,\alpha_V$, and $\sigma_Q$ is written with $\alpha$ and $\alpha^{*}$. The calculation below translates between the two descriptions in four steps.

**Step 1: real variables.** Split each amplitude into real and imaginary part, $\alpha_H=x_H+iy_H$ and $\alpha_V=x_V+iy_V$, and collect the four real numbers in

$$
\mathbf x=\begin{pmatrix}x_H\\x_V\\y_H\\y_V\end{pmatrix}.
$$

The measure is $d^4\alpha=d^2\alpha_H\,d^2\alpha_V=dx_H\,dy_H\,dx_V\,dy_V$, i.e. ordinary integration over $\mathbb R^4$. So $Q$ is an ordinary probability density of four real variables. Its covariance matrix is the real symmetric $4\times4$ matrix

<span id="eq25a"></span>

$$
\Sigma_{\mathbb R}=\int d^4\alpha\;Q(\boldsymbol\alpha)\,\mathbf x\,\mathbf x^T,
\qquad
\left(\Sigma_{\mathbb R}\right)_{ij}=\langle x_ix_j\rangle_Q ,
\tag{25a}
$$

and equation (4) of [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md#gauss:real) with $n=4$ variables gives

<span id="eq25b"></span>

$$
Q=\frac{1}{(2\pi)^{2}\sqrt{\det\Sigma_{\mathbb R}}}\exp\!\left(-\tfrac12\,\mathbf x^T\Sigma_{\mathbb R}^{-1}\mathbf x\right).
\tag{25b}
$$

The remaining task is to express $\det\Sigma_{\mathbb R}$ and $\mathbf x^T\Sigma_{\mathbb R}^{-1}\mathbf x$ through $\sigma_Q$ and $\mathbf v=(\alpha_H,\alpha_V,\alpha_H^{*},\alpha_V^{*})^T$.

**Step 2: from $\mathbf x$ to $\mathbf v$.** Since $\alpha_j=x_j+iy_j$ and $\alpha_j^{*}=x_j-iy_j$, the two vectors are related by a constant matrix $T$, written in $2\times2$ blocks:

<span id="eq25c"></span>

$$
\mathbf v=
\begin{pmatrix}\alpha_H\\\alpha_V\\\alpha_H^{*}\\\alpha_V^{*}\end{pmatrix}
=
\underbrace{\begin{pmatrix}1&0&i&0\\0&1&0&i\\1&0&-i&0\\0&1&0&-i\end{pmatrix}}_{T=\left(\begin{smallmatrix}\mathbb{1}&i\mathbb{1}\\ \mathbb{1}&-i\mathbb{1}\end{smallmatrix}\right)}
\begin{pmatrix}x_H\\x_V\\y_H\\y_V\end{pmatrix}
=T\,\mathbf x .
\tag{25c}
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

**Step 3: the two covariance matrices.** Inserting $\mathbf v=T\mathbf x$ and $\mathbf v^{\dagger}=\mathbf x^{\dagger}T^{\dagger}=\mathbf x^TT^{\dagger}$ (the $x_j,y_j$ are real) into (24), and pulling the constant matrices out of the integral:

<span id="eq25d"></span>

$$
\sigma_Q=\int d^4\alpha\;Q\,\mathbf v\,\mathbf v^{\dagger}
=T\left(\int d^4\alpha\;Q\,\mathbf x\,\mathbf x^T\right)T^{\dagger}
=T\,\Sigma_{\mathbb R}\,T^{\dagger}.
\tag{25d}
$$

This gives both quantities needed in (25b):

- **Determinant.** $\det\sigma_Q=\det T\,\det\Sigma_{\mathbb R}\,\det T^{\dagger}=\lvert\det T\rvert^2\det\Sigma_{\mathbb R}=16\,\det\Sigma_{\mathbb R}$, i.e.

    $$
    \det\Sigma_{\mathbb R}=\frac{\det\sigma_Q}{16}.
    $$

- **Exponent.** From (25d), $\sigma_Q^{-1}=(T\Sigma_{\mathbb R}T^{\dagger})^{-1}=(T^{\dagger})^{-1}\Sigma_{\mathbb R}^{-1}T^{-1}$. With $\mathbf x=T^{-1}\mathbf v$ and $\mathbf x^T=\mathbf x^{\dagger}=\mathbf v^{\dagger}(T^{\dagger})^{-1}$:

    <span id="eq25e"></span>

    $$
    \mathbf x^T\Sigma_{\mathbb R}^{-1}\mathbf x
    =\mathbf v^{\dagger}(T^{\dagger})^{-1}\,\Sigma_{\mathbb R}^{-1}\,T^{-1}\mathbf v
    =\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v .
    \tag{25e}
    $$

**Step 4: insert into (25b).** The prefactor becomes

$$
(2\pi)^2\sqrt{\det\Sigma_{\mathbb R}}
=4\pi^2\sqrt{\frac{\det\sigma_Q}{16}}
=4\pi^2\,\frac{\sqrt{\det\sigma_Q}}{4}
=\pi^2\sqrt{\det\sigma_Q},
$$

and the exponent is (25e). Hence

<span id="eq25"></span>

$$
Q(\boldsymbol\alpha)=\frac{1}{\pi^2\sqrt{\det\sigma_Q}}\exp\!\left(-\tfrac12\,\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v\right),
\qquad
Q(0)=\frac{1}{\pi^2\sqrt{\det\sigma_Q}} ,
\tag{25}
$$

where $Q(0)$ follows from $\mathbf v=0$ and $e^{0}=1$. So the factor $(2\pi)^2$ of four real variables turns into $\pi^2$, because $\lvert\det T\rvert^2=16$ cancels the $2^2$ inside $(2\pi)^2$. The same calculation for one mode is in [Complex variables](../concepts_and_foundations/gaussian_peak_height.md#gauss:complex).

**Check with the vacuum.** For $\rho=\lvert 0,0\rangle\langle 0,0\rvert$, directly from (21) and $\langle 0\vert\alpha\rangle=e^{-\lvert\alpha\rvert^2/2}$ (the $n=0$ term of the Fock expansion, equation (1) of [Coherent states](../concepts_and_foundations/coherent_states.md)):

$$
Q_{\text{vac}}(\boldsymbol\alpha)=\frac{1}{\pi^2}\,\lvert\langle 0,0\vert\alpha_H,\alpha_V\rangle\rvert^2=\frac{1}{\pi^2}\,e^{-\lvert\alpha_H\rvert^2-\lvert\alpha_V\rvert^2}.
$$

From (25): the vacuum has $\sigma_Q=\mathbb{1}$ (eq. [(20)](covariance_matrix.md#eq20) at $\lambda=0$, where $\nu=\mu=0$), so $\det\sigma_Q=1$ and

$$
\mathbf v^{\dagger}\mathbf v=\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2+\lvert\alpha_H^{*}\rvert^2+\lvert\alpha_V^{*}\rvert^2=2\left(\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2\right),
\qquad
Q=\frac{1}{\pi^2}\,e^{-\frac12\cdot2\left(\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2\right)}=\frac{1}{\pi^2}\,e^{-\lvert\alpha_H\rvert^2-\lvert\alpha_V\rvert^2}\ ✓
$$

**Result.** Combining (25) with (22):

$$
P(0,0)=\pi^2\,Q(0)=\pi^2\cdot\frac{1}{\pi^2\sqrt{\det\sigma_Q}},
$$

i.e.

<span id="eq26"></span>

$$
\boxed{\;P(0,0)=\frac{1}{\sqrt{\det\sigma_Q}}\;}
\tag{26}
$$

This is the zero-photon case of the central formula of Gaussian boson sampling <a href="#ref-hamilton2017">[1]</a>. The square root is the ordinary positive one, because $\sigma_Q$ is a covariance matrix and $\det\sigma_Q>0$.

## Is $Q$ really a bell curve? Check with the main derivation

The calculation of the previous section assumed two things: that $Q$ is a bell curve centred at $0$, and that its covariance matrix is $\sigma_Q$, so that its exponent is $-\tfrac12\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v$. For the loss-free state $\rho=\lvert\Psi\rangle\langle\Psi\rvert$ both can be checked directly: compute $Q$ in closed form from the state vector [(2)](notation.md#eq2) and compare it, exponent and prefactor, with (25).

**Step 1: the overlap $\langle\boldsymbol\alpha\vert\Psi\rangle$.** By (2),

$$
\langle\boldsymbol\alpha\vert\Psi\rangle=\Lambda\,\langle\boldsymbol\alpha\rvert\,e^{\frac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^TM\mathbf{\hat a^{\dagger}}}\lvert 0,0\rangle .
$$

The adjoint of the eigenvalue equation $\hat a_i\lvert\boldsymbol\alpha\rangle=\alpha_i\lvert\boldsymbol\alpha\rangle$ is $\langle\boldsymbol\alpha\rvert\hat a_i^{\dagger}=\alpha_i^{*}\langle\boldsymbol\alpha\rvert$. Applied factor by factor, every creation operator standing directly to the right of $\langle\boldsymbol\alpha\rvert$ is replaced by a number:

$$
\langle\boldsymbol\alpha\rvert\,(\mathbf{\hat a^{\dagger}})^TM\mathbf{\hat a^{\dagger}}
=\sum_{i,j}M_{ij}\,\langle\boldsymbol\alpha\rvert\hat a_i^{\dagger}\hat a_j^{\dagger}
=\sum_{i,j}M_{ij}\,\alpha_i^{*}\alpha_j^{*}\,\langle\boldsymbol\alpha\rvert
=(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}\,\langle\boldsymbol\alpha\rvert ,
$$

and the same holds for every power $\big((\mathbf{\hat a^{\dagger}})^TM\mathbf{\hat a^{\dagger}}\big)^n$, hence for every term of the exponential series. This is the step of the main derivation at [the overlap with coherent states](../theory/cc_derivation.md#overlap_coherent), written for creation operators. With $\langle\boldsymbol\alpha\vert 0,0\rangle=e^{-\frac12(\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2)}=e^{-\frac12\boldsymbol\alpha^{\dagger}\boldsymbol\alpha}$ (the $n=0$ term of equation (1) of [Coherent states](../concepts_and_foundations/coherent_states.md)):

<span id="eq27"></span>

$$
\langle\boldsymbol\alpha\vert\Psi\rangle=\Lambda\,e^{\frac{\lambda}{2}(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}}\,\langle\boldsymbol\alpha\vert 0,0\rangle
=\Lambda\,e^{\frac{\lambda}{2}(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}-\frac12\boldsymbol\alpha^{\dagger}\boldsymbol\alpha}.
\tag{27}
$$

**Step 2: the $Q$ function.** For the pure state, $\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle=\langle\boldsymbol\alpha\vert\Psi\rangle\langle\Psi\vert\boldsymbol\alpha\rangle=\lvert\langle\boldsymbol\alpha\vert\Psi\rangle\rvert^2$. For a complex exponent $z$, $\lvert e^{z}\rvert^2=e^{z}\,e^{z^{*}}=e^{z+z^{*}}$. Since $\lambda$, $\Lambda$ and $M$ are real, the complex conjugate of the exponent of (27) is

$$
\Big(\tfrac{\lambda}{2}(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}-\tfrac12\boldsymbol\alpha^{\dagger}\boldsymbol\alpha\Big)^{*}
=\tfrac{\lambda}{2}\boldsymbol\alpha^TM\boldsymbol\alpha-\tfrac12\boldsymbol\alpha^{\dagger}\boldsymbol\alpha ,
$$

and with (21):

<span id="eq28"></span>

$$
Q(\boldsymbol\alpha)=\frac{\lvert\langle\boldsymbol\alpha\vert\Psi\rangle\rvert^2}{\pi^2}
=\frac{\Lambda^2}{\pi^2}\exp\!\left(-\boldsymbol\alpha^{\dagger}\boldsymbol\alpha+\frac{\lambda}{2}\boldsymbol\alpha^TM\boldsymbol\alpha+\frac{\lambda}{2}(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}\right),
\tag{28}
$$

with $\boldsymbol\alpha^{\dagger}\boldsymbol\alpha=\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2$.

**Step 3: the exponent as a quadratic form in $\mathbf v$.** To compare with (25), write the exponent with $\mathbf v=(\boldsymbol\alpha,\boldsymbol\alpha^{*})^T$ and $\mathbf v^{\dagger}=\big((\boldsymbol\alpha^{*})^T,\boldsymbol\alpha^T\big)$. For a $4\times4$ matrix with $2\times2$ blocks,

$$
\mathbf v^{\dagger}\begin{pmatrix}P&R\\R&P\end{pmatrix}\mathbf v
=\boldsymbol\alpha^{\dagger}P\boldsymbol\alpha+(\boldsymbol\alpha^{*})^TR\,\boldsymbol\alpha^{*}+\boldsymbol\alpha^TR\,\boldsymbol\alpha+\boldsymbol\alpha^TP\,\boldsymbol\alpha^{*}.
$$

With $P=\mathbb{1}$ the first and last terms are both $\boldsymbol\alpha^{\dagger}\boldsymbol\alpha$. Choosing $R=-\lambda M$ therefore gives $\mathbf v^{\dagger}(\cdots)\mathbf v=2\boldsymbol\alpha^{\dagger}\boldsymbol\alpha-\lambda(\boldsymbol\alpha^{*})^TM\boldsymbol\alpha^{*}-\lambda\boldsymbol\alpha^TM\boldsymbol\alpha$, which is $-2$ times the exponent of (28). Hence

<span id="eq29"></span>

$$
Q(\boldsymbol\alpha)=\frac{\Lambda^2}{\pi^2}\exp\!\left(-\tfrac12\,\mathbf v^{\dagger}A\,\mathbf v\right),
\qquad
A=\begin{pmatrix}\mathbb{1}&-\lambda M\\-\lambda M&\mathbb{1}\end{pmatrix}.
\tag{29}
$$

**Step 4: $Q$ is a bell curve centred at $0$.** The exponent contains no terms linear in $\mathbf v$, so the curve is centred at $\mathbf v=0$. It is a bell curve (it falls off in every direction) if $A$ is positive definite. $A$ is real symmetric of the block form $\left(\begin{smallmatrix}A_0&B_0\\B_0&A_0\end{smallmatrix}\right)$, which the rotation $K$ of [Block-matrix identities](../concepts_and_foundations/block_matrices.md#block:rotation) brings to $\operatorname{diag}(\mathbb{1}-\lambda M,\;\mathbb{1}+\lambda M)$ without changing the eigenvalues. $M$ of [(3)](notation.md#eq3) is real symmetric with $\operatorname{tr}M=S_4-S_4=0$ and $\det M=-S_4^2-C_4^2=-1$, so its characteristic polynomial is $t^2-(\operatorname{tr}M)\,t+\det M=t^2-1$ and its eigenvalues are $\pm1$. The eigenvalues of $A$ are therefore $1+\lambda$ and $1-\lambda$ (each twice), all positive for $0\le\lambda<1$. Concretely, $\mathbf v^{\dagger}A\mathbf v\ge(1-\lambda)\,\mathbf v^{\dagger}\mathbf v=2(1-\lambda)\,\boldsymbol\alpha^{\dagger}\boldsymbol\alpha$, so

$$
Q(\boldsymbol\alpha)\le\frac{\Lambda^2}{\pi^2}\,e^{-(1-\lambda)(\lvert\alpha_H\rvert^2+\lvert\alpha_V\rvert^2)} ,
$$

which decays in every direction of the complex $\alpha_H$ and $\alpha_V$ planes.

**Step 5: the exponent agrees with (25), i.e. $A=\sigma_Q^{-1}$.** By [(20)](covariance_matrix.md#eq20), $\sigma_Q$ has the same block form, $\sigma_Q=\left(\begin{smallmatrix}(1+\nu)\mathbb{1}&\mu M\\ \mu M&(1+\nu)\mathbb{1}\end{smallmatrix}\right)$. Multiplying block by block and using $M^2=\mathbb{1}$ ([(4)](notation.md#eq4)):

$$
\begin{aligned}
\sigma_Q A
&=
\begin{pmatrix}
(1+\nu)\mathbb{1}-\lambda\mu M^2 & -\lambda(1+\nu)M+\mu M\\
\mu M-\lambda(1+\nu)M & -\lambda\mu M^2+(1+\nu)\mathbb{1}
\end{pmatrix}\\
&=
\begin{pmatrix}
(1+\nu-\lambda\mu)\,\mathbb{1} & \big(\mu-\lambda(1+\nu)\big)M\\
\big(\mu-\lambda(1+\nu)\big)M & (1+\nu-\lambda\mu)\,\mathbb{1}
\end{pmatrix}.
\end{aligned}
$$

With $1+\nu=\frac{1}{1-\lambda^2}$ and $\mu=\frac{\lambda}{1-\lambda^2}$ from [(18)](covariance_matrix.md#eq18):

$$
1+\nu-\lambda\mu=\frac{1-\lambda^2}{1-\lambda^2}=1,
\qquad
\mu-\lambda(1+\nu)=\frac{\lambda-\lambda}{1-\lambda^2}=0 .
$$

<span id="eq29a"></span>

$$
\sigma_QA=\mathbb{1}_4,\qquad\text{i.e.}\qquad A=\sigma_Q^{-1}.
\tag{29a}
$$

So the exponent of the exact $Q$ function (29) is exactly the exponent $-\tfrac12\mathbf v^{\dagger}\sigma_Q^{-1}\mathbf v$ of (25): the covariance matrix computed on [Covariance matrix](covariance_matrix.md) is the covariance matrix of this bell curve.

**Step 6: the prefactor agrees with (25).** By (29a), $\det\sigma_Q=1/\det A$. The block rule [(36)](determinant.md#eq36) (derived in [Block-matrix identities](../concepts_and_foundations/block_matrices.md#block:det_ABBA)) and, for a $2\times2$ matrix, $\det(\mathbb{1}\pm\lambda M)=1\pm\lambda\operatorname{tr}M+\lambda^2\det M=1-\lambda^2$ give

<span id="eq29b"></span>

$$
\det A=\det(\mathbb{1}-\lambda M)\,\det(\mathbb{1}+\lambda M)=(1-\lambda^2)^2,
\qquad
\det\sigma_Q=\frac{1}{(1-\lambda^2)^2}.
\tag{29b}
$$

Hence the prefactor of (25) is $\frac{1}{\pi^2\sqrt{\det\sigma_Q}}=\frac{1-\lambda^2}{\pi^2}=\frac{\Lambda^2}{\pi^2}$, the prefactor of (29). Together with step 5, (25) and (29) are the same function.

**Consequence.** For $\lvert\Psi\rangle$, (26) gives $P(0,0)=1/\sqrt{\det\sigma_Q}=1-\lambda^2$. This agrees with the vacuum amplitude read off directly from (2): only the $n=0$ term of the exponential series contributes to $\langle 0,0\vert\Psi\rangle=\Lambda$, so $P(0,0)=\lvert\langle 0,0\vert\Psi\rangle\rvert^2=\Lambda^2=1-\lambda^2$ ✓.

**What is imported.** After the losses of [Detector efficiency](detector_efficiency.md) the state is no longer pure, and steps 1–2 (which use the state vector $\lvert\Psi\rangle$) no longer apply. That $Q$ is still a bell curve then is the one general fact the formalism relies on: beam splitters with vacuum inputs map Gaussian states to Gaussian states <a href="#ref-weedbrook2012">[8]</a>, <a href="#ref-ferraro2005">[9]</a>. (How the beam splitter models the loss is shown in [Detector loss as a beam splitter](../concepts_and_foundations/loss_beam_splitter.md).) The [numerical check](../dashboard/comparison.md#numerical-check) confirms it for this case.

## References

<p id="ref-hamilton2017">
[1] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Gaussian Boson Sampling</em>, Phys. Rev. Lett. <strong>119</strong>, 170501 (2017). Available: https://arxiv.org/abs/1612.01199
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
