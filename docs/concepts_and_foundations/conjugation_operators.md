# Conjugation of creation operators

The identity

\begin{equation}
x^{\hat n_H} a_H^\dagger x^{-\hat n_H} = x\, a_H^\dagger
\end{equation}

is proven by evaluating the action of both sides on number states.

To begin, recall how exponentials of the number operator act on Fock states:

<span id="eq:xpownm"></span>

\begin{equation}
\label{eq:x pow n m}
x^{-\hat n_H} |m\rangle = x^{-m} |m\rangle.
\end{equation}

This follows directly from the fact that $|m\rangle$ is an eigenstate of $\hat n_H$.

Applying the creation operator to this result gives

\begin{equation}
a_H^\dagger x^{-\hat n_H} |m\rangle
= x^{-m} a_H^\dagger |m\rangle
= x^{-m} \sqrt{m+1}\, |m+1\rangle.
\end{equation}

Next, the operator $x^{\hat n_H}$ is applied. Since $|m+1\rangle$ is also an eigenstate of $\hat n_H$, its action is straightforward:

\begin{equation}
\begin{aligned}
x^{\hat n_H} a_H^\dagger x^{-\hat n_H} |m\rangle
&= x^{-m} \sqrt{m+1}\, x^{m+1} |m+1\rangle \\
&= x \sqrt{m+1} |m+1\rangle.
\end{aligned}
\end{equation}

For comparison, the direct action of $x\,a_H^\dagger$ on the same state is

\begin{equation}
x a_H^\dagger |m\rangle = x \sqrt{m+1} |m+1\rangle.
\end{equation}

Since both expressions produce the same result for arbitrary $|m\rangle$, the operator identity follows:

<span id="eq:xpownadagger1"></span>

\begin{equation}\label{eq:x pow n a dagger}
x^{\hat n_H} a_H^\dagger x^{-\hat n_H} = x\, a_H^\dagger.
\end{equation}

For the $V$ mode, the commutation relation $[\hat n_H, a_V^\dagger]=0$ implies that the operators commute. As a result, the conjugation has no effect:

<span id="eq:xpownadagger2"></span>

\begin{equation}
\label{eq:x pow n a dagger2}
x^{\hat n_H} a_V^\dagger x^{-\hat n_H} = a_V^\dagger.
\end{equation}