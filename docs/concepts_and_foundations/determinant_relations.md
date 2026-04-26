# Determinant relations

## Determinant of a 2 by 2 block matrix

According to Powell[@powell2011blockdet], the determinant of a $2\times2$ block matrix 

\begin{equation}
\begin{aligned}
Q=
\begin{pmatrix}
Q_{11} & Q_{12}\\[2mm]
Q_{21} & Q_{22}
\end{pmatrix}
\end{aligned}
\end{equation}

can be calculated by

\begin{equation}
\label{appendix:det_of_blockmatrix}
\det Q = \det(Q_{11}-Q_{12}Q_{22}^{-1}Q_{21})\det Q_{11}
\end{equation}

## Determinant identity for scaled matrices

Here I show the derivation of a useful identity for the determinant of a $2\times 2$ matrix of the form

\begin{equation}
\det(\mathbb{1}-\lambda^2 X),
\end{equation}

where $X$ is an arbitrary $2\times2$ matrix.

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

Then

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

Using the determinant formula for a $2\times2$ matrix,

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

one obtains

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

Now recall that for the matrix $X$,

\begin{equation}
\begin{aligned}
\mathrm{Tr}(X)=a+d,
\qquad
\det(X)=ad-bc.
\end{aligned}
\end{equation}

Therefore:

<span id="appendix:det_1minusl2X"></span>

\begin{equation}
\label{appendix:det_1minusl2X}
\begin{aligned}
\det(\mathbb{1}-\lambda^2X)
=
1-\lambda^2\mathrm{Tr}(X)+\lambda^4\det(X)
\end{aligned}
\end{equation}

Thus, for any $2\times2$ matrix $X$, the determinant of $\mathbb{1}-\lambda^2X$ can always be written in terms of the trace and determinant of $X$.