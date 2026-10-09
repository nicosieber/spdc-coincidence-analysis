# Block-matrix identities

The covariance matrices of the [Gaussian formalism](../gaussian_formalism/overview.md) have a repeated-block structure $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$, and the Torontonian involves parts of an inverse matrix. This page collects the three matrix identities used for them.

<span id="block:det_ABBA"></span>

## Determinant of $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$

Let $A$ and $B$ be square matrices of the same size. Two operations that do not change the determinant (adding one row to another, and subtracting one column from another, here done block-wise):

1. Add the lower block row to the upper one.
2. Subtract the left block column from the right one.

$$
\begin{pmatrix}A&B\\B&A\end{pmatrix}
\;\xrightarrow{\;\text{row}\;}\;
\begin{pmatrix}A+B&A+B\\B&A\end{pmatrix}
\;\xrightarrow{\;\text{column}\;}\;
\begin{pmatrix}A+B&0\\B&A-B\end{pmatrix}.
$$

The result is block-triangular, and the determinant of a block-triangular matrix is the product of the determinants of its diagonal blocks. So

\begin{equation}
\label{block:det_ABBA}
\det\begin{pmatrix}A&B\\B&A\end{pmatrix}=\det(A+B)\,\det(A-B).
\end{equation}

A $4\times4$ determinant thus reduces to two $2\times2$ determinants. This is used in [(29)](../gaussian_formalism/vacuum_probability.md#eq29) and [(36)](../gaussian_formalism/determinant.md#eq36).

<span id="block:rotation"></span>

## Block diagonalization by a rotation

The same split can be done as a rotation. With the identity $\mathbb{1}$ of the size of $A$, let

$$
K=\frac{1}{\sqrt2}\begin{pmatrix}\mathbb{1}&\mathbb{1}\\\mathbb{1}&-\mathbb{1}\end{pmatrix},
\qquad
K^T=K,\qquad K^2=\mathbb{1}.
$$

$K$ is symmetric and its own inverse, hence orthogonal (a rotation combined with a reflection). Multiplying out,

\begin{equation}
\label{block:rotation}
K\begin{pmatrix}A&B\\B&A\end{pmatrix}K
=\frac12\begin{pmatrix}A+B&A+B\\A-B&B-A\end{pmatrix}\begin{pmatrix}\mathbb{1}&\mathbb{1}\\\mathbb{1}&-\mathbb{1}\end{pmatrix}
=\begin{pmatrix}A+B&0\\0&A-B\end{pmatrix}.
\end{equation}

Since $\det K^2=1$, this gives \(\eqref{block:det_ABBA}\) once more. It also gives a statement about **positivity**. Suppose $\sigma=\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$ is real symmetric and positive definite, i.e. $\mathbf z^T\sigma\mathbf z>0$ for every $\mathbf z\neq0$. For any $\mathbf y\neq0$, set $\mathbf z=K(\mathbf y,0)^T\neq0$ (since $K$ is invertible). Then

$$
\mathbf y^T(A+B)\,\mathbf y=(\mathbf y,0)\,K\sigma K\begin{pmatrix}\mathbf y\\0\end{pmatrix}=\mathbf z^T\sigma\,\mathbf z>0,
$$

and in the same way with $(0,\mathbf y)^T$ for $A-B$. So $A+B$ and $A-B$ are positive definite, and in particular $\det(A+B)>0$ and $\det(A-B)>0$. This is used for the by-product $\det Q>0$ in [The determinant](../gaussian_formalism/determinant.md#eq47).

<span id="block:jacobi"></span>

## Jacobi's complementary-minor identity

Let $\sigma$ be an invertible matrix and split its indices into two sets $Z$ and its complement $\bar Z$. Write $(\cdot)_{(Z)}$ for the square submatrix that keeps only the rows and columns in $Z$. Then

\begin{equation}
\label{block:jacobi}
\det\big(\sigma^{-1}\big)_{(Z)}=\frac{\det\sigma_{(\bar Z)}}{\det\sigma}:
\end{equation}

a part of the *inverse* is related to the *complementary* part of the matrix itself.

**Derivation.** Reordering rows and columns by the same permutation changes neither determinants nor the relation between a matrix and its inverse, so the indices in $Z$ can be put first:

$$
\sigma=\begin{pmatrix}P&R\\R^T&S\end{pmatrix},
\qquad
P=\sigma_{(Z)},\quad S=\sigma_{(\bar Z)} .
$$

(Here $\sigma$ is symmetric, as all covariance matrices of this documentation are; the argument works the same way without symmetry.) Assume $S$ is invertible and define the *Schur complement* $C=P-RS^{-1}R^T$. Multiplying out shows the factorization

$$
\sigma=\begin{pmatrix}\mathbb{1}&RS^{-1}\\0&\mathbb{1}\end{pmatrix}\begin{pmatrix}C&0\\0&S\end{pmatrix}\begin{pmatrix}\mathbb{1}&0\\S^{-1}R^T&\mathbb{1}\end{pmatrix}.
$$

The two outer factors are block-triangular with identity blocks on the diagonal, so their determinant is $1$, and

$$
\det\sigma=\det C\,\det S .
$$

Inverting the factorization (each outer factor is inverted by flipping the sign of its off-diagonal block):

$$
\sigma^{-1}=\begin{pmatrix}\mathbb{1}&0\\-S^{-1}R^T&\mathbb{1}\end{pmatrix}\begin{pmatrix}C^{-1}&0\\0&S^{-1}\end{pmatrix}\begin{pmatrix}\mathbb{1}&-RS^{-1}\\0&\mathbb{1}\end{pmatrix}.
$$

Its upper-left block is $\big(\sigma^{-1}\big)_{(Z)}=C^{-1}$. Therefore

$$
\det\big(\sigma^{-1}\big)_{(Z)}=\frac{1}{\det C}=\frac{\det S}{\det\sigma}=\frac{\det\sigma_{(\bar Z)}}{\det\sigma},
$$

which is \(\eqref{block:jacobi}\). For a positive definite $\sigma$, every $S=\sigma_{(\bar Z)}$ is positive definite and hence invertible, so the assumption is always met. In the edge cases, $Z=\emptyset$ gives $1=\det\sigma/\det\sigma$ (the determinant of an empty matrix is $1$), and $\bar Z=\emptyset$ gives $\det\sigma^{-1}=1/\det\sigma$.

This identity turns the Torontonian into the inclusion–exclusion sum in [Coincidence probability](../gaussian_formalism/coincidence.md).
