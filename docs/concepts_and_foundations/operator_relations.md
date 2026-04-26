# Operator relations

In this section the relation

\begin{equation}
    Se^XS^{-1}=e^{SXS^{-1}}
\end{equation}

for operators $S$ and $X$ will be derived. First, recall that

\begin{equation}
    e^X=\sum_{n=0}^\infty\dfrac{X^n}{n!}.
\end{equation}

Following that, we get

\begin{equation}
    Se^XS^{-1}=S\left(\sum_{n=0}^\infty\dfrac{X^n}{n!}\right)S^{-1}.
\end{equation}

With $S$ as a linear operator, we can move $S$ and $S^{-1}$ inside the sum:

\begin{equation}
    \label{appendix:powerseries1}
    Se^XS^{-1}=\sum_{n=0}^\infty\dfrac{SX^nS^{-1}}{n!}
\end{equation}

Therefore, the next step is to understand how $SX^nS^{-1}$ is evaluated.
Recall that

\begin{equation}
S(AB)S^{-1}=\left(SAS^{-1}\right)\left(SBS^{-1}\right),
\end{equation}

so for $n=2$ we get

\begin{equation}
SX^2S^{-1}=\left(SXS^{-1}\right)\left(SXS^{-1}\right),
\end{equation}

and for $n=3$ we get

\begin{equation}
SX^3S^{-1}=\left(SXS^{-1}\right)\left(SXS^{-1}\right)\left(SXS^{-1}\right).
\end{equation}

In general we get

\begin{equation}
    SX^nS^{-1}=\left(SXS^{-1}\right)^n,
\end{equation}

which can be inserted back into \(\eqref{appendix:powerseries1}\) resulting in the relation which we wanted to prove at the beginning:

<span id="appendix:powerseries_final"></span>

\begin{equation}
\label{appendix:powerseries_final}
\begin{aligned}
Se^XS^{-1}&=\sum_{n=0}^\infty\dfrac{\left(SXS^{-1}\right)^n}{n!}=e^{SXS^{-1}}
\end{aligned}
\end{equation}