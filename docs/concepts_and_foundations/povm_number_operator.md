# POVM as a function of the number operator

Consider the operator

\begin{equation}
A := \sum_{k=0}^{\infty} x^k \, |k\rangle\langle k|.
\end{equation}

This operator is diagonal in the Fock basis. The states $|k\rangle$ are eigenstates of the number operator

\begin{equation}
\hat{n} = \hat{a}^\dagger \hat{a}, 
\qquad 
\hat{n} |k\rangle = k |k\rangle.
\end{equation}

This property will be used to relate $A$ to a function of the number operator.

---

## Action of exponentials of the number operator

For any function $f$, the operator $f(\hat{n})$ can be defined via its power series expansion. 
In particular, the operator $x^{\hat{n}}$ can be written as

\begin{equation}
x^{\hat{n}} = e^{(\ln x)\hat{n}}
= \sum_{j=0}^{\infty} \frac{(\ln x)^j}{j!} \, \hat{n}^{\,j}.
\end{equation}

Since $|m\rangle$ is an eigenstate of $\hat{n}$, repeated application of $\hat{n}$ gives

\begin{equation}
\hat{n}^{\,j} |m\rangle = m^j |m\rangle.
\end{equation}

Substituting this into the series expansion yields

\begin{equation}
\begin{aligned}
x^{\hat{n}} |m\rangle
&= \sum_{j=0}^{\infty} \frac{(\ln x)^j}{j!} \, m^j |m\rangle \\
&= \left( \sum_{j=0}^{\infty} \frac{(\ln x)^j m^j}{j!} \right) |m\rangle \\
&= e^{m \ln x} |m\rangle \\
&= x^m |m\rangle.
\end{aligned}
\end{equation}

Thus, the operator $x^{\hat{n}}$ acts diagonally in the Fock basis with eigenvalues $x^m$.

---

## Action of $A$ on number states

The action of $A$ on an arbitrary number state $|m\rangle$ is given by

\begin{equation}
\begin{aligned}
A|m\rangle
&= \sum_{k=0}^{\infty} x^k |k\rangle \langle k|m\rangle \\
&= \sum_{k=0}^{\infty} x^k |k\rangle \delta_{k,m} \\
&= x^m |m\rangle.
\end{aligned}
\end{equation}

This shows that $A$ is also diagonal in the Fock basis and has the same eigenvalues $x^m$.

---

## Identification of the operators

Since both $A$ and $x^{\hat{n}}$ act identically on all basis states $|m\rangle$, they represent the same operator. Therefore,

\begin{equation}
\sum_{k=0}^{\infty} x^k |k\rangle\langle k| = x^{\hat{n}}.
\end{equation}

In particular, for $x = 1-\eta$, this yields

\begin{equation}
\Pi_0^{(\eta)} = (1-\eta)^{\hat{n}}.
\end{equation}