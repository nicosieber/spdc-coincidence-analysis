# Coherent states

\begin{equation}
\begin{aligned}
\lvert \alpha \rangle & =e^{-\frac{|\alpha|²}{2}}\sum_{n=0}^\infty\dfrac{\alpha^n}{\sqrt{n!}}\lvert n \rangle\\
    \langle \alpha \rvert & =e^{-\frac{|\alpha|²}{2}}\sum_{m=0}^\infty\dfrac{(\alpha^*)^m}{\sqrt{m!}}\langle m \rvert
\end{aligned}
\end{equation}

<span id="formula:coherent_state_matrix"></span>

\begin{equation}
\label{formula:coherent_state matrix}
\lvert \alpha \rangle\langle \alpha \rvert=e^{-|\alpha|²}\sum_{n,m=0}^\infty\dfrac{\alpha^n(\alpha^*)^m}{\sqrt{n!m!}}\lvert n \rangle \langle m \rvert
\end{equation}

Integrating both sides of \(\eqref{formula:coherent_state matrix}\) with $d^2\alpha/\pi$ gives:

\begin{equation}
\label{formula:coherent_state matrix_integral}
\int \dfrac{d^2\alpha}{\pi}\lvert \alpha \rangle\langle \alpha \rvert=\sum_{n,m=0}^\infty\dfrac{\lvert n \rangle \langle m \rvert}{\sqrt{n!m!}}\int\dfrac{d^2\alpha}{\pi}e^{-|\alpha|^2}\alpha^n(\alpha^*)^m
\end{equation}

Switching to polar coordinates with

\begin{equation}
\begin{aligned}
\alpha &=re^{i\phi},\\
d^2\alpha &=rdrd\phi,
\end{aligned}
\end{equation}

transforms the integral of expression \(\eqref{formula:coherent_state matrix_integral}\) into:

\begin{equation}
\label{formula:coherent_state_integral}
\begin{aligned}
&\int \dfrac{d^2\alpha}{\pi}e^{-|\alpha^2|}\alpha^n(\alpha^*)\\
&=\int\dfrac{rdrd\phi}{\pi}e^{-r^2}\left(re^{i\phi}\right)^n\left(re^{-i\phi}\right)^m\\
&=\int_{0}^{\infty}\dfrac{r^{n+m+1}e^{-r^2}}{\pi}dr\int_{0}^{2\pi}e^{i(n-m)\phi}d\phi
\end{aligned}
\end{equation}

Since

\begin{equation}
\begin{aligned}
\int_{0}^{2\pi}e^{i(n-m)\phi}d\phi=
\begin{cases}
    2\pi, & n = m, \\
    0, & n\neq m,
\end{cases}
\end{aligned}
\end{equation}

equation \(\eqref{formula:coherent_state_integral}\) transforms into

\begin{equation}
2\pi\int_{0}^{\infty}\dfrac{r^{2n+1}e^{-r^2}}{\pi}dr\
\end{equation}

for $n=m$. Using the substitution

\begin{equation}
\begin{aligned}
u&=r^2,\\
du&=2rdr,
\end{aligned}
\end{equation}

the integral transforms into the Gamma-function:

\begin{equation}
2\int_{0}^{\infty}r^{n2n+1}e^{-r^2}dr=\int_{0}^{\infty}u^ne^{-u}du=\Gamma(n+1)=n!
\end{equation}

So finally \(\eqref{formula:coherent_state_integral}\) becomes

\begin{equation}
\int \dfrac{d^2\alpha}{\pi}e^{-|\alpha^2|}\alpha^n(\alpha^*)=n!,
\end{equation}

and as a result \(\eqref{formula:coherent_state matrix_integral}\) becomes:

<span id="eq:coherent_identity"></span>

\begin{equation}
\label{eq:coherent_identity}
\int \dfrac{d^2\alpha}{\pi}\lvert \alpha \rangle \langle \alpha \rvert=\sum_{n=0}^\infty \lvert n \rangle \langle n \rvert=\mathbb{1}
\end{equation}