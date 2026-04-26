# POVM as a function of the number operator

Considering the operator

\begin{equation}
A := \sum_{k=0}^{\infty} x^k \, |k\rangle\langle k|.
\end{equation}

The Fock states $|k\rangle$ are eigenstates of the number operator

\begin{equation}
\hat{n} = \hat{a}^\dagger \hat{a}, 
\qquad 
\hat{n} |k\rangle = k |k\rangle.
\end{equation}

## Action of exponentials of the number operator

For any function $f$, the operator $f(\hat{n})$ is defined via its power series. 
In particular,

\begin{equation}
x^{\hat{n}} = e^{(\ln x)\hat{n}}
= \sum_{j=0}^{\infty} \frac{(\ln x)^j}{j!} \, \hat{n}^{\,j}.
\end{equation}

Since $|m\rangle$ is an eigenstate of $\hat{n}$, we have

\begin{equation}
\hat{n}^{\,j} |m\rangle = m^j |m\rangle,
\end{equation}

and therefore

\begin{equation}
\begin{aligned}
x^{\hat{n}} |m\rangle
&= \sum_{j=0}^{\infty} \frac{(\ln x)^j}{j!} \, m^j |m\rangle \\
&= \left( \sum_{j=0}^{\infty} \frac{(\ln x)^j m^j}{j!} \right) |m\rangle \\
&= e^{m \ln x} |m\rangle \\
&= x^m |m\rangle.
\end{aligned}
\end{equation}

## Action of A on number states

Acting with $A$ on an arbitrary number state $|m\rangle$ yields

\begin{equation}
\begin{aligned}
A|m\rangle
&= \sum_{k=0}^{\infty} x^k |k\rangle \langle k|m\rangle \\
&= \sum_{k=0}^{\infty} x^k |k\rangle \delta_{k,m} \\
&= x^m |m\rangle.
\end{aligned}
\end{equation}

Since both operators act identically on all basis states, we conclude

\begin{equation}
\sum_{k=0}^{\infty} x^k |k\rangle\langle k| = x^{\hat{n}}.
\end{equation}

In particular, for $x = 1-\eta$,

\begin{equation}
\Pi_0^{(\eta)} = (1-\eta)^{\hat{n}}.
\end{equation}