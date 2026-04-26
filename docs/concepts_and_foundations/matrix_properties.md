# Matrix properties

Here I provide a detailed justification that the matrix $B = \Re(A)$ introduced in equation (36) during the [derivation of the coincidence probability](../theory/cc_derivation.md#ABiC) is real symmetric and positive definite under physically relevant conditions. This property is essential for the convergence of the [Gaussian integral](../theory/cc_derivation.md#GIntegral) and for the existence of the [factorization of $A$](../theory/cc_derivation.md#A_factorization).

## Structure of B

[As we see in the derivation of the coincidence probability](../theory/cc_derivation.md#ABiC), the matrix $A$ can be decomposed into its real and imaginary parts as

\begin{equation}
A = B + iC.
\end{equation}

The real part is explicitly given by

\begin{equation}
B =
\begin{pmatrix}
I - \frac{\lambda}{2}(L + M) & 0 \\
0 & I + \frac{\lambda}{2}(L + M)
\end{pmatrix}.
\end{equation}

Link to the definitions of:

- [Matrix $M$](../theory/tmsv.md#eq:alpha_vec)
- [Matrix $D$](../theory/cc_derivation.md#MatrixD)

The matrix $L = DMD$ is used as an abbreviation. First, observe that both $M$ and $D$ are real symmetric matrices. Since the product of symmetric matrices of the form $DMD$ preserves symmetry, it follows that $L$ is also real symmetric. Consequently, $B$ is real symmetric as it consists of symmetric blocks on the diagonal.

## Spectral properties of M

The matrix $M$ has the explicit form

\begin{equation}
M =
\begin{pmatrix}
2cs & s^2 - c^2 \\
s^2 - c^2 & -2cs
\end{pmatrix},
\end{equation}

where $c = \cos(2\vartheta)$ and $s = \sin(2\vartheta)$. A direct computation shows that

\begin{equation}
(2cs)^2 + (s^2 - c^2)^2 = 1,
\end{equation}

which implies

\begin{equation}
M^2 = \mathbb{1}.
\end{equation}

This relation has an important consequence for the spectrum of $M$. If $v$ is an eigenvector of $M$ with eigenvalue $\lambda$, then

\begin{equation}
M^2 v = \lambda^2 v.
\end{equation}

Since $M^2 = \mathbb{1}$, it follows that $\lambda^2 = 1$, and therefore $\lambda = \pm 1$. Thus, all eigenvalues of $M$ lie in the set $\{-1,1\}$.

Because $M$ is real symmetric, its operator norm is equal to the largest absolute value of its eigenvalues (see <a href="#GilbertIntroductionToLinearAlgebra2016">[1]</a>). Hence,

\begin{equation}
\|M\|_2 = 1.
\end{equation}

## Bound on L

Next, we analyze the matrix $L = DMD$. The matrix $D = \mathrm{diag}(t_H, t_V)$ encodes detector losses, where $t_{H,V} = 1 - \eta_{H,V}$ and $0 \le \eta_{H,V} \le 1$. Therefore,

\begin{equation}
0 \le t_H, t_V \le 1.
\end{equation}

For diagonal matrices, the operator norm is given by the largest absolute diagonal entry, and hence

\begin{equation}
\|D\|_2 = \max(t_H, t_V) \le 1.
\end{equation}

Using the submultiplicativity of the operator norm,

\begin{equation}
\|AB\|_2 \le \|A\|_2 \|B\|_2,
\end{equation}

we obtain

\begin{equation}
\|L\|_2 = \|DMD\|_2 \le \|D\|_2^2 \|M\|_2 \le 1.
\end{equation}

We now consider the sum $L + M$. Using the triangle inequality,

\begin{equation}
\|L + M\|_2 \le \|L\|_2 + \|M\|_2 \le 2.
\end{equation}

Since $L+M$ is real symmetric, this bound implies that all of its eigenvalues lie in the interval $[-2,2]$.

## Positivity of B

We now determine the eigenvalues of $B$. Due to its block-diagonal structure, the eigenvalues of $B$ are given by those of the two blocks

\begin{equation}
\mathbb{1} \pm \frac{\lambda}{2}(L+M).
\end{equation}

Let $v$ be an eigenvector of $L+M$ with eigenvalue $\mu$. Then

\begin{equation}
(L+M)v = \mu v.
\end{equation}

Applying the block matrices to $v$ yields

\begin{equation}
\left(\mathbb{1} \pm \frac{\lambda}{2}(L+M)\right)v
= \left(1 \pm \frac{\lambda}{2}\mu\right)v.
\end{equation}

Thus, the eigenvalues of $B$ are

\begin{equation}
\lambda_\pm = 1 \pm \frac{\lambda}{2}\mu.
\end{equation}

Since $\mu \in [-2,2]$, the smallest possible value of $\lambda_\pm$ occurs for $\mu = \pm 2$, yielding

\begin{equation}
\lambda_\pm \ge 1 - \lambda.
\end{equation}

For finite squeezing parameter $r$, we have $\lambda = \tanh(r)$ with $0 \le \lambda < 1$, and therefore

\begin{equation}
\lambda_\pm > 0.
\end{equation}

Hence, all eigenvalues of $B$ are strictly positive, and we conclude that $B$ is positive definite.

## Existence and uniqueness of the matrix square root of B

Since $B$ is real symmetric, the spectral theorem guarantees an orthogonal diagonalization

\begin{equation}
B = Q \Lambda Q^T,
\end{equation}

where $Q$ is orthogonal and $\Lambda = \mathrm{diag}(\lambda_1,\dots,\lambda_n)$ contains the eigenvalues of $B$ (see <a href="#GilbertIntroductionToLinearAlgebra2016">[1]</a>). Since $B$ is positive definite, all eigenvalues satisfy $\lambda_i > 0$.

We define

\begin{equation}
B^{1/2} := Q \Lambda^{1/2} Q^T,
\end{equation}

where $\Lambda^{1/2} = \mathrm{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_n})$. By construction,

\begin{equation}
B^{1/2} B^{1/2} = B.
\end{equation}

Since all eigenvalues $\lambda_i$ are strictly positive, their square roots are well-defined and nonzero, implying that $B^{1/2}$ is invertible. The inverse is given by

\begin{equation}
B^{-1/2} = Q \Lambda^{-1/2} Q^T.
\end{equation}

The square root constructed in this way is the unique real symmetric positive definite square root of $B$ (see <a href="#GilbertIntroductionToLinearAlgebra2016">[1]</a>).

## Conclusion

We have shown that $B$ is real symmetric and positive definite for all physically relevant parameters ($0 \le \eta_{H,V} \le 1$, finite squeezing $r$). This ensures both the convergence of the Gaussian integral and the validity of the factorization used in equation (43) of [Derivation of the coincidence probability](../theory/cc_derivation.md#A_factorization).

## References
<p id="GilbertIntroductionToLinearAlgebra2016">
[1] Gilbert Strang,
“Introduction to Linear Algebra,”
<em>Wellesley - Cambridge Press</em>, ed. 5, isbn 978-0-9802327-7-6, 2016.
</p>

