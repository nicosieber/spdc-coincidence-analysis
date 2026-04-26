# Coherent states

The definition of coherent states in the Fock basis. These states are eigenstates of the annihilation operator and can be expanded in the number basis as:

\begin{equation}
\begin{aligned}
\lvert \alpha \rangle & =e^{-\frac{|\alpha|²}{2}}\sum_{n=0}^\infty\dfrac{\alpha^n}{\sqrt{n!}}\lvert n \rangle\\
    \langle \alpha \rvert & =e^{-\frac{|\alpha|²}{2}}\sum_{m=0}^\infty\dfrac{(\alpha^*)^m}{\sqrt{m!}}\langle m \rvert
\end{aligned}
\end{equation}

Taking the outer product of the coherent state with itself gives the corresponding density operator:

<span id="formula:coherent_state_matrix"></span>

\begin{equation}
\label{formula:coherent_state matrix}
\lvert \alpha \rangle\langle \alpha \rvert=e^{-|\alpha|²}\sum_{n,m=0}^\infty\dfrac{\alpha^n(\alpha^*)^m}{\sqrt{n!m!}}\lvert n \rangle \langle m \rvert
\end{equation}

Now, both sides of \(\eqref{formula:coherent_state matrix}\) are integrated over the phase space with the measure $d^2\alpha/\pi$. This is to show that coherent states form an overcomplete basis that resolves the identity.

Integrating both sides of \(\eqref{formula:coherent_state matrix}\) with $d^2\alpha/\pi$ gives:

\begin{equation}
\label{formula:coherent_state matrix_integral}
\int \dfrac{d^2\alpha}{\pi}\lvert \alpha \rangle\langle \alpha \rvert=\sum_{n,m=0}^\infty\dfrac{\lvert n \rangle \langle m \rvert}{\sqrt{n!m!}}\int\dfrac{d^2\alpha}{\pi}e^{-|\alpha|^2}\alpha^n(\alpha^*)^m
\end{equation}

Thus, the problem reduces to evaluating the phase-space integral appearing on the right-hand side.

To evaluate this integral, a switch to polar coordinates in the complex plane is done:

\begin{equation}
\begin{aligned}
\alpha &=re^{i\phi},\\
d^2\alpha &=rdrd\phi,
\end{aligned}
\end{equation}

This transformation separates the integral into radial and angular parts. Substituting into \(\eqref{formula:coherent_state matrix_integral}\), results in:

\begin{equation}
\label{formula:coherent_state_integral}
\begin{aligned}
&\int \dfrac{d^2\alpha}{\pi}e^{-|\alpha^2|}\alpha^n(\alpha^*)\\
&=\int\dfrac{rdrd\phi}{\pi}e^{-r^2}\left(re^{i\phi}\right)^n\left(re^{-i\phi}\right)^m\\
&=\int_{0}^{\infty}\dfrac{r^{n+m+1}e^{-r^2}}{\pi}dr\int_{0}^{2\pi}e^{i(n-m)\phi}d\phi
\end{aligned}
\end{equation}

The angular integral enforces orthogonality between different number states:

\begin{equation}
\begin{aligned}
\int_{0}^{2\pi}e^{i(n-m)\phi}d\phi=
\begin{cases}
    2\pi, & n = m, \\
    0, & n\neq m,
\end{cases}
\end{aligned}
\end{equation}

This shows that only the diagonal terms with $n=m$ contribute to the integral. Therefore, equation \(\eqref{formula:coherent_state_integral}\) simplifies to

\begin{equation}
2\pi\int_{0}^{\infty}\dfrac{r^{2n+1}e^{-r^2}}{\pi}dr\
\end{equation}

for $n=m$.

To evaluate the remaining radial integral, the substitution following substitution is done:

\begin{equation}
\begin{aligned}
u&=r^2,\\
du&=2rdr.
\end{aligned}
\end{equation}

As a result the integral transforms into a standard Gamma-function:

\begin{equation}
2\int_{0}^{\infty}r^{n2n+1}e^{-r^2}dr=\int_{0}^{\infty}u^ne^{-u}du=\Gamma(n+1)=n!
\end{equation}

Using this result, \(\eqref{formula:coherent_state_integral}\) evaluates to

\begin{equation}
\int \dfrac{d^2\alpha}{\pi}e^{-|\alpha^2|}\alpha^n(\alpha^*)=n!.
\end{equation}

Finally, substituting this back into \(\eqref{formula:coherent_state matrix_integral}\), the following identity can be obtained:

<span id="eq:coherent_identity"></span>

\begin{equation}
\label{eq:coherent_identity}
\int \dfrac{d^2\alpha}{\pi}\lvert \alpha \rangle \langle \alpha \rvert=\sum_{n=0}^\infty \lvert n \rangle \langle n \rvert=\mathbb{1}
\end{equation}

This shows that coherent states resolve the identity operator, demonstrating that they form an overcomplete basis in Hilbert space.