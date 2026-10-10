# Peak height of a Gaussian distribution

In the [Gaussian formalism](../gaussian_formalism/overview.md), the no-click probability turns out to be the height of a bell-shaped probability distribution at its centre. This page shows why that height follows from the covariance matrix alone,

$$
p(0)=\frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}},
$$

and how the formula changes when the variables are complex amplitudes $\alpha,\alpha^{*}$ instead of real numbers.

**A word on terminology.** In probability theory, averages like $\langle x\rangle$ and $\langle x^2\rangle$ are called the first and second *moments* of a distribution. The papers on Gaussian states mostly speak of the **mean** (or displacement) and the **covariance matrix** instead. All distributions on this page are centred at $0$, so the mean vanishes and the covariance matrix is the matrix of second moments $\langle x_ix_j\rangle$.

## One variable

Take a random variable $x$ with a bell-shaped (Gaussian) distribution centred at $0$:

<span id="gauss:1d"></span>

\begin{equation}
\label{gauss:1d}
p(x)=\frac{1}{\sqrt{2\pi\langle x^2\rangle}}\,e^{-x^2/2\langle x^2\rangle},
\qquad
p(0)=\frac{1}{\sqrt{2\pi\langle x^2\rangle}}.
\end{equation}

The whole curve is completely determined by **one number**, the second moment $\langle x^2\rangle$. In particular its height at the centre follows directly from it: the wider the curve, the lower its peak. With several variables $x_1,x_2,\dots$ one needs all second moments $\langle x_ix_j\rangle$, collected in the covariance matrix $\Sigma$, and the height at the centre becomes $1/\sqrt{\det\Sigma}$ (up to factors of $2\pi$). The determinant arises in two steps.

## Independent variables: the determinant is a product of variances

If $x_1$ and $x_2$ are independent, the joint distribution is a product of two one-dimensional bell curves:

<span id="gauss:independent"></span>

\begin{equation}
\label{gauss:independent}
p(x_1,x_2)=\frac{e^{-x_1^2/2\langle x_1^2\rangle}}{\sqrt{2\pi\langle x_1^2\rangle}}\cdot\frac{e^{-x_2^2/2\langle x_2^2\rangle}}{\sqrt{2\pi\langle x_2^2\rangle}},
\qquad
p(0,0)=\frac{1}{2\pi\sqrt{\langle x_1^2\rangle\langle x_2^2\rangle}}=\frac{1}{2\pi\sqrt{\det\Sigma}},
\qquad
\Sigma=\begin{pmatrix}\langle x_1^2\rangle&0\\0&\langle x_2^2\rangle\end{pmatrix}.
\end{equation}

For a diagonal $\Sigma$, "$\det$" simply means "multiply all variances".

## Correlated variables: rotate until they are independent

If $\langle x_1x_2\rangle\neq0$, the bell curve is a tilted ellipse with

$$
\Sigma=\begin{pmatrix}\langle x_1^2\rangle&\langle x_1x_2\rangle\\\langle x_1x_2\rangle&\langle x_2^2\rangle\end{pmatrix}.
$$

Rotating the coordinate axes onto the axes of the ellipse makes the variables independent, so the previous case applies. A rotation leaves the origin where it is (same height at the centre), leaves areas unchanged (same normalization) and leaves the determinant unchanged. Hence

$$
p(0,0)=\frac{1}{2\pi\sqrt{\det\Sigma}},
\qquad
\det\Sigma=\langle x_1^2\rangle\langle x_2^2\rangle-\langle x_1x_2\rangle^2 ,
$$

holds for any covariance matrix. The same argument works for any number $n$ of variables: rotate onto the principal axes, where $\Sigma$ is diagonal and the distribution is a product of $n$ one-dimensional bell curves \(\eqref{gauss:1d}\). Hence

<span id="gauss:real"></span>

\begin{equation}
\label{gauss:real}
p(\mathbf x)=\frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}}\,e^{-\frac12\mathbf x^T\Sigma^{-1}\mathbf x},
\qquad
p(0)=\frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}} .
\end{equation}

Mathematically, this is the normalization integral $\int d^nx\,e^{-\frac12\mathbf x^T\Sigma^{-1}\mathbf x}=(2\pi)^{n/2}\sqrt{\det\Sigma}$, the same Gaussian integral as in the [main derivation](../theory/cc_derivation.md#GIntegral).

**Intuition.** Correlations ($\langle x_1x_2\rangle\neq0$) squeeze the cloud of points into a thinner ellipse that covers less area. Since the total probability stays $1$, the peak must be higher. A smaller determinant means a higher peak, and a larger determinant (a wider cloud) means a lower peak.

<span id="gauss:complex"></span>

## Complex variables

The $Q$ function of the Gaussian formalism is a distribution over complex amplitudes $\alpha=x+iy$, and its covariance matrix is written with $\alpha$ and $\alpha^{*}$ instead of $x$ and $y$. This only changes the prefactor.

For one complex amplitude, collect the real variables in $(x,y)^T$ with covariance matrix $\Sigma_{\mathbb R}$, and the complex ones in $\mathbf v=(\alpha,\alpha^{*})^T$ with covariance matrix $\sigma=\langle\mathbf v\mathbf v^{\dagger}\rangle$. The two are related by a constant matrix $T$:

$$
\mathbf v=\begin{pmatrix}\alpha\\\alpha^{*}\end{pmatrix}=\underbrace{\begin{pmatrix}1&i\\1&-i\end{pmatrix}}_{T}\begin{pmatrix}x\\y\end{pmatrix},
\qquad
\sigma=T\,\Sigma_{\mathbb R}\,T^{\dagger},
\qquad
\det\sigma=\lvert\det T\rvert^2\det\Sigma_{\mathbb R}=\lvert-2i\rvert^2\det\Sigma_{\mathbb R}=4\det\Sigma_{\mathbb R}.
$$

With $m$ complex amplitudes there are $n=2m$ real variables and $\det\sigma=4^m\det\Sigma_{\mathbb R}$. Inserting $\det\Sigma_{\mathbb R}=\det\sigma/4^m$ into \(\eqref{gauss:real}\):

<span id="gauss:complex_eq"></span>

\begin{equation}
\label{gauss:complex}
p(0)=\frac{1}{(2\pi)^m\sqrt{\det\sigma/4^m}}=\frac{1}{\pi^m\sqrt{\det\sigma}} .
\end{equation}

For two modes ($m=2$) this is the factor $\pi^2$ of [(11)](../gaussian_formalism/covariance_matrix.md#eq11), and for one mode the factor $\pi$ of [(49)](../gaussian_formalism/coincidence.md#eq49).

**Check with the vacuum.** The vacuum $Q$ function of one mode is $\pi^{-1}e^{-\lvert\alpha\rvert^2}$, i.e. $\langle x^2\rangle=\langle y^2\rangle=\tfrac12$, $\langle xy\rangle=0$. Then $\det\Sigma_{\mathbb R}=\tfrac14$, $\det\sigma=1$, and \(\eqref{gauss:complex}\) gives $p(0)=1/\pi$ ✓.

<span id="gauss:marginal"></span>

## Marginals

Integrating a Gaussian distribution over some of its variables gives the distribution of the remaining ones (its *marginal*). Two facts are needed:

1. **The marginal is again Gaussian.** The exponent is quadratic in all variables. Completing the square in the variables that are integrated out leaves an exponent that is still quadratic in the remaining ones.
2. **Its covariance matrix is the corresponding part of the full one.** An average $\langle x_ix_j\rangle$ of kept variables $x_i,x_j$ does not care whether the other variables were integrated out first. So the covariance matrix of the marginal consists of the rows and columns of $\Sigma$ belonging to the kept variables.

Together with \(\eqref{gauss:real}\) or \(\eqref{gauss:complex}\), the height of the marginal at the origin is $1/\sqrt{\det}$ of that part of $\Sigma$ (times the appropriate power of $2\pi$ or $\pi$). This is used for the one-detector no-click probabilities in [Coincidence probability](../gaussian_formalism/coincidence.md).
