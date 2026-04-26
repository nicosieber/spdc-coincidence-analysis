# Operator relations

In this section, the relation

\begin{equation}
    Se^XS^{-1}=e^{SXS^{-1}}
\end{equation}

for operators $S$ and $X$ is derived. This identity expresses how operator exponentials transform under similarity transformations.

First, recall the power series definition of the exponential of an operator:

\begin{equation}
    e^X=\sum_{n=0}^\infty\dfrac{X^n}{n!}.
\end{equation}

Using this expansion, the left-hand side can be written as

\begin{equation}
    Se^XS^{-1}=S\left(\sum_{n=0}^\infty\dfrac{X^n}{n!}\right)S^{-1}.
\end{equation}

Since $S$ is a linear operator, it can be distributed over the sum, allowing $S$ and $S^{-1}$ to be moved inside:

\begin{equation}
    \label{appendix:powerseries1}
    Se^XS^{-1}=\sum_{n=0}^\infty\dfrac{SX^nS^{-1}}{n!}
\end{equation}

The problem is thus reduced to evaluating the transformed powers $SX^nS^{-1}$.

To proceed, recall the identity

\begin{equation}
S(AB)S^{-1}=\left(SAS^{-1}\right)\left(SBS^{-1}\right),
\end{equation}

which shows how products of operators transform under conjugation.

Applying this relation to powers of $X$, for $n=2$ one obtains

\begin{equation}
SX^2S^{-1}=\left(SXS^{-1}\right)\left(SXS^{-1}\right),
\end{equation}

and for $n=3$

\begin{equation}
SX^3S^{-1}=\left(SXS^{-1}\right)\left(SXS^{-1}\right)\left(SXS^{-1}\right).
\end{equation}

This pattern generalizes to arbitrary $n$, yielding

\begin{equation}
    SX^nS^{-1}=\left(SXS^{-1}\right)^n,
\end{equation}

so that each term in the series transforms into a corresponding power of the conjugated operator.

Substituting this result back into \(\eqref{appendix:powerseries1}\) gives

<span id="appendix:powerseries_final"></span>

\begin{equation}
\label{appendix:powerseries_final}
\begin{aligned}
Se^XS^{-1}&=\sum_{n=0}^\infty\dfrac{\left(SXS^{-1}\right)^n}{n!}=e^{SXS^{-1}}
\end{aligned}
\end{equation}

This establishes the desired relation, showing that exponentiation and similarity transformation commute.