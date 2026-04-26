# Conjugation of creation operators

We prove the identity

\begin{equation}
x^{\hat n_H} a_H^\dagger x^{-\hat n_H} = x\, a_H^\dagger
\end{equation}

by acting on number states.

First, note that

<span id="eq:xpownm"></span>

\begin{equation}
\label{eq:x pow n m}
x^{-\hat n_H} |m\rangle = x^{-m} |m\rangle.
\end{equation}

Applying the creation operator gives

\begin{equation}
a_H^\dagger x^{-\hat n_H} |m\rangle
= x^{-m} a_H^\dagger |m\rangle
= x^{-m} \sqrt{m+1}\, |m+1\rangle.
\end{equation}

Now act with $x^{\hat n_H}$:

\begin{equation}
\begin{aligned}
x^{\hat n_H} a_H^\dagger x^{-\hat n_H} |m\rangle
&= x^{-m} \sqrt{m+1}\, x^{m+1} |m+1\rangle \\
&= x \sqrt{m+1} |m+1\rangle.
\end{aligned}
\end{equation}

On the other hand,

\begin{equation}
x a_H^\dagger |m\rangle = x \sqrt{m+1} |m+1\rangle.
\end{equation}

Thus,

<span id="eq:xpownadagger1"></span>

\begin{equation}\label{eq:x pow n a dagger}
x^{\hat n_H} a_H^\dagger x^{-\hat n_H} = x\, a_H^\dagger.
\end{equation}

For the $V$ mode, note that $[\hat n_H, a_V^\dagger]=0$. Therefore,

<span id="eq:xpownadagger2"></span>

\begin{equation}
\label{eq:x pow n a dagger2}
x^{\hat n_H} a_V^\dagger x^{-\hat n_H} = a_V^\dagger.
\end{equation}