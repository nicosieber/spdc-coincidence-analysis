# Determinant relations

## Determinant of a 2 by 2 block matrix

The determinant of a $2\times2$ block matrix can be expressed in terms of its sub-blocks. This result is particularly useful when one of the blocks is invertible.

Consider the matrix

\begin{equation}
\begin{aligned}
Q=
\begin{pmatrix}
Q_{11} & Q_{12}\\[2mm]
Q_{21} & Q_{22}
\end{pmatrix}
\end{aligned}
\end{equation}

Under suitable conditions (in particular, assuming the required inverses exist), its determinant can be written as

\begin{equation}
\label{appendix:det_of_blockmatrix}
\det Q = \det(Q_{11}-Q_{12}Q_{22}^{-1}Q_{21})\det Q_{11}
\end{equation}

This expression allows the determinant of a block matrix to be reduced to determinants of smaller matrices (see <a href="#ref-powell2011">[1]</a>).

---

## Determinant identity for scaled matrices

A useful identity for determinants of $2\times2$ matrices is derived in the following.

Consider the expression

\begin{equation}
\det(\mathbb{1}-\lambda^2 X),
\end{equation}

where $X$ is an arbitrary $2\times2$ matrix. The goal is to express this determinant in terms of invariants of $X$.

Let

\begin{equation}
\begin{aligned}
X=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\quad
(X\in\mathbb{C}^{2\times2}).
\end{aligned}
\end{equation}

Then the matrix $\mathbb{1}-\lambda^2 X$ takes the form

\begin{equation}
\begin{aligned}
\mathbb{1}-\lambda^2X
=
\begin{pmatrix}
1-\lambda^2 a & -\lambda^2 b\\
-\lambda^2 c & 1-\lambda^2 d
\end{pmatrix}.
\end{aligned}
\end{equation}

The determinant of a general $2\times2$ matrix is given by

\begin{equation}
\begin{aligned}
\det
\begin{pmatrix}
p&q\\
r&s
\end{pmatrix}
=ps-qr,
\end{aligned}
\end{equation}

which can now be applied directly:

\begin{equation}
\begin{aligned}
\det(\mathbb{1}-\lambda^2X)
&=
(1-\lambda^2 a)(1-\lambda^2 d)-(-\lambda^2 b)(-\lambda^2 c)\\
&=
(1-\lambda^2 a)(1-\lambda^2 d)-\lambda^4bc\\
&=
1-\lambda^2(a+d)+\lambda^4(ad-bc).
\end{aligned}
\end{equation}

The result can be expressed more compactly by recalling the definitions

\begin{equation}
\begin{aligned}
\mathrm{Tr}(X)=a+d,
\qquad
\det(X)=ad-bc.
\end{aligned}
\end{equation}

Substituting these into the previous expression yields

<span id="appendix:det_1minusl2X"></span>

\begin{equation}
\label{appendix:det_1minusl2X}
\begin{aligned}
\det(\mathbb{1}-\lambda^2X)
=
1-\lambda^2\mathrm{Tr}(X)+\lambda^4\det(X)
\end{aligned}
\end{equation}

This shows that, for any $2\times2$ matrix $X$, the determinant of $\mathbb{1}-\lambda^2X$ depends only on the trace and determinant of $X$.

---

## References

<p id="ref-powell2011">
[1] P. D. Powell, <em>Calculating Determinants of Block Matrices</em>, 2011. Available: https://arxiv.org/abs/1112.4379
</p>