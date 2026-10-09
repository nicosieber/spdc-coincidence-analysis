# Commutator with an operator exponential

In the [Gaussian formalism](../gaussian_formalism/covariance_matrix.md#key-relation), an annihilation operator $\hat a_H$ has to be moved past the exponential $e^{\hat X}$ of the TMSV. This page derives the identity used there,

$$
[\hat A,e^{\hat X}]=[\hat A,\hat X]\,e^{\hat X}\qquad\text{if }[\hat A,\hat X]\text{ commutes with }\hat X,
$$

from three elementary properties of the commutator $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$.

<span id="comm:linear"></span>

## Linearity

The commutator is linear in its second argument: for numbers $c,d$,

\begin{equation}
\label{comm:linear}
[\hat A,c\hat B+d\hat C]
=\hat A\,(c\hat B+d\hat C)-(c\hat B+d\hat C)\,\hat A
=c\,(\hat A\hat B-\hat B\hat A)+d\,(\hat A\hat C-\hat C\hat A)
=c\,[\hat A,\hat B]+d\,[\hat A,\hat C],
\end{equation}

using only that operator products distribute over sums and that numbers can be pulled out. The same holds term by term for an infinite sum such as a power series.

<span id="comm:product"></span>

## Product rule

The commutator with a product acts on one factor at a time:

\begin{equation}
\label{comm:product}
[\hat A,\hat B\hat C]=[\hat A,\hat B]\,\hat C+\hat B\,[\hat A,\hat C].
\end{equation}

To check it, expand the right-hand side: $(\hat A\hat B-\hat B\hat A)\hat C+\hat B(\hat A\hat C-\hat C\hat A)=\hat A\hat B\hat C-\hat B\hat A\hat C+\hat B\hat A\hat C-\hat B\hat C\hat A=\hat A\hat B\hat C-\hat B\hat C\hat A$, which is the left-hand side.

<span id="comm:power"></span>

## Commutator with a power

For $n=2$, the product rule \(\eqref{comm:product}\) gives

$$
[\hat A,\hat X\hat X]=[\hat A,\hat X]\,\hat X+\hat X\,[\hat A,\hat X].
$$

Now assume that $[\hat A,\hat X]$ commutes with $\hat X$. (In the application, $\hat A=\hat a_H$ and both $[\hat a_H,\hat X]$ and $\hat X$ contain only creation operators, which all commute with each other.) Then $\hat X\,[\hat A,\hat X]=[\hat A,\hat X]\,\hat X$, and the two terms are equal:

$$
[\hat A,\hat X^2]=2\,[\hat A,\hat X]\,\hat X .
$$

For general $n$, applying the product rule repeatedly gives $n$ terms, one for each factor $\hat X$ that the commutator "hits":

\begin{equation}
\label{comm:power}
[\hat A,\hat X^n]=\sum_{k=0}^{n-1}\hat X^{k}\,[\hat A,\hat X]\,\hat X^{n-1-k}
=n\,[\hat A,\hat X]\,\hat X^{n-1},
\end{equation}

where in each term $[\hat A,\hat X]$ was moved past the $\hat X^{k}$ in front of it. For $n=0$ the commutator vanishes, $[\hat A,\mathbb{1}]=0$.

<span id="comm:exp"></span>

## Summing the series

Insert the series $e^{\hat X}=\sum_{n=0}^{\infty}\hat X^n/n!$. By linearity \(\eqref{comm:linear}\), applied term by term with $c=1/n!$, the commutator can be taken inside the sum. With \(\eqref{comm:power}\):

\begin{equation}
\label{comm:exp}
[\hat A,e^{\hat X}]
=\sum_{n=0}^{\infty}\frac{[\hat A,\hat X^n]}{n!}
=\sum_{n=1}^{\infty}\frac{n\,[\hat A,\hat X]\,\hat X^{n-1}}{n!}
=[\hat A,\hat X]\sum_{n=1}^{\infty}\frac{\hat X^{n-1}}{(n-1)!}
=[\hat A,\hat X]\sum_{m=0}^{\infty}\frac{\hat X^{m}}{m!}
=[\hat A,\hat X]\,e^{\hat X}.
\end{equation}

The sum starts at $n=1$ because the $n=0$ term vanishes. Then $\frac{n}{n!}=\frac{1}{(n-1)!}$, and renaming $m=n-1$ turns the sum back into the full exponential series $\sum_{m=0}^{\infty}\hat X^m/m!=e^{\hat X}$.

This is the operator version of $\frac{d}{dx}e^{f(x)}=f'(x)\,e^{f(x)}$: the commutator with $\hat A$ acts like a derivative (it obeys the product rule \(\eqref{comm:product}\)), and the condition that $[\hat A,\hat X]$ commutes with $\hat X$ lets $f'$ be pulled out in front just as for ordinary functions.
