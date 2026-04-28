# Two-Mode Squeezed Vacuum
## Mathematical description of the quantum state

The next step is to do the same steps which we did for the state in equation (1) of the [simplified example](simplified_example.md#initial_state)  for the two-mode squeezed vacuum (TMSV). In this section, we first will look at the mathematical formulation of the TMSV, how it behaves when transformed by the HWP, and how relevant detection probabilities can be derived using the POVM for lossy bucket detectors.

For the correct phase-matching conditions the previously mentioned conditions of spatial overlap and indistinguishability are met. Mathematically, the TMSV state can be expressed as <a href="#ref-lvovsky2014">[1]</a>

\begin{equation}
\label{tmsv}
\begin{aligned}
    \lvert \Psi \rangle &=\sqrt{1-|\lambda|^2}\sum_{n=0}^{\infty}\lambda^n \lvert n,n \rangle\\
                     &=\sqrt{1-|\lambda|^2}\sum_{n=0}^{\infty}\dfrac{\lambda^n}{n!}\left(\hat a_H^\dagger\right)^n\left(\hat a_V^\dagger\right)^n\lvert 0,0 \rangle,
\end{aligned}
\end{equation}

with $n$ as the photon number and

\begin{equation}
\begin{aligned}
    \lambda=\tanh(r),
\end{aligned}
\end{equation}

where $r$ is the squeezing parameter. 

## TMSV rotated by a HWP

Sending the TMSV through a HWP results in

\begin{equation}
\label{TMSV_HWP:full}
\begin{aligned}
    \lvert \Psi \rangle =\Lambda&\sum_{n=0}^{\infty}\dfrac{\lambda^n}{n!}\left(\cos(2\vartheta)\hat a_H^\dagger+\sin(2\vartheta)\hat a_V^\dagger\right)^n\\ 
    &\times\left(\sin(2\vartheta)\hat a_H^\dagger-\cos(2\vartheta)\hat a_V^\dagger\right)^n \lvert 0,0 \rangle.
\end{aligned}
\end{equation}

Using the shorthand notation

\begin{equation}
c:=\cos(2\vartheta),
\qquad
s:=\sin(2\vartheta),
\end{equation}

\(\eqref{TMSV_HWP:full}\) can be transformed into

\begin{equation}
\label{eq:TMSV_HWP_sum}
\begin{aligned}
|\Psi\rangle
=
\Lambda \sum_{n=0}^{\infty}
\frac{\lambda^n}{n!}
\left(c\,\hat a_H^\dagger + s\,\hat a_V^\dagger\right)^n
\left(s\,\hat a_H^\dagger - c\,\hat a_V^\dagger\right)^n
|0,0\rangle.
\end{aligned}
\end{equation}

## TMSV written as an exponential

We now define the operator

\begin{equation}
\label{eq:Kdag_def}
\begin{aligned}
\hat K^\dagger
:=
\left(c\,\hat a_H^\dagger + s\,\hat a_V^\dagger\right)
\left(s\,\hat a_H^\dagger - c\,\hat a_V^\dagger\right).
\end{aligned}
\end{equation}

Since all creation operators commute,

\begin{equation}
[\hat a_H^\dagger,\hat a_V^\dagger] = 0
\end{equation}

the two factors in \(\eqref{eq:Kdag_def}\) commute as well. Hence,

\begin{equation}
\begin{aligned}
    (\hat K^\dagger)^n
    & =
    \left[
    \left(c\,\hat a_H^\dagger + s\,\hat a_V^\dagger\right)
    \left(s\,\hat a_H^\dagger - c\,\hat a_V^\dagger\right)
    \right]^n \\
    & =
    \left(c\,\hat a_H^\dagger + s\,\hat a_V^\dagger\right)^n
    \left(s\,\hat a_H^\dagger - c\,\hat a_V^\dagger\right)^n.
\end{aligned}
\end{equation}

Substituting this into \(\eqref{eq:TMSV_HWP_sum}\) gives

\begin{equation}
\begin{aligned}
    |\Psi\rangle
    =
    \Lambda \sum_{n=0}^{\infty}
    \frac{\lambda^n}{n!}
    (\hat K^\dagger)^n
    |0,0\rangle.
\end{aligned}
\end{equation}

Using the Taylor series of the exponential,

\begin{equation}
\begin{aligned}
e^{\lambda \hat K^\dagger}
=
\sum_{n=0}^{\infty}
\frac{(\lambda \hat K^\dagger)^n}{n!}
=
\sum_{n=0}^{\infty}
\frac{\lambda^n}{n!}
(\hat K^\dagger)^n,
\end{aligned}
\end{equation}

we finally obtain the compact exponential form

\begin{equation}
\label{formula:tmsv_as_exp}
\begin{aligned}
|\Psi\rangle
=
\Lambda\, e^{\lambda \hat K^\dagger}|0,0\rangle
\end{aligned}
\end{equation}

If desired, one may also expand $\hat K^\dagger$ explicitly:

\begin{equation}
\begin{aligned}
\hat K^\dagger
&=
\left(c\,\hat a_H^\dagger + s\,\hat a_V^\dagger\right)
\left(s\,\hat a_H^\dagger - c\,\hat a_V^\dagger\right) \\
&=
cs\,(\hat a_H^\dagger)^2
-c^2 \hat a_H^\dagger \hat a_V^\dagger
+s^2 \hat a_V^\dagger \hat a_H^\dagger
-cs\,(\hat a_V^\dagger)^2.
\end{aligned}
\end{equation}

Because

\begin{equation}
\begin{aligned}
\hat a_V^\dagger \hat a_H^\dagger
=
\hat a_H^\dagger \hat a_V^\dagger,
\end{aligned}
\end{equation}

this becomes

\begin{equation}
\begin{aligned}
\hat K^\dagger
=
cs\,(\hat a_H^\dagger)^2
+
(s^2-c^2)\hat a_H^\dagger \hat a_V^\dagger
-cs\,(\hat a_V^\dagger)^2.
\end{aligned}
\end{equation}

Using

\begin{equation}
\begin{aligned}
2cs=\sin(4\vartheta),
\qquad
s^2-c^2=-\cos(4\vartheta),
\end{aligned}
\end{equation}

one may write

\begin{equation}
\begin{aligned}
\hat K^\dagger
=
\frac{\sin(4\vartheta)}{2}(\hat a_H^\dagger)^2
-\cos(4\vartheta)\,\hat a_H^\dagger \hat a_V^\dagger
-\frac{\sin(4\vartheta)}{2}(\hat a_V^\dagger)^2.
\end{aligned}
\end{equation}

With

<span id="eq:alpha_vec"></span>

\begin{equation}
\label{eq:alpha_vec}
\begin{aligned}
    \mathbf{\hat a^{\dagger}}=
    \begin{pmatrix}
    a_{H}^\dagger  \\
    a_{V}^\dagger
    \end{pmatrix}\quad \text{and}\quad 
    M=
    \begin{pmatrix}
    2cs & s^2-c^2 \\
    s^2-c^2 & -2cs
    \end{pmatrix},
\end{aligned}
\end{equation}

equation \(\eqref{formula:tmsv_as_exp}\) becomes:

<span id="formula:tmsv_as_exp_2"></span>

\begin{equation}
\label{formula:tmsv_as_exp_2}
\begin{aligned}
|\Psi\rangle
=
\Lambda\, e^{\frac{\lambda}{2} \mathbf{\hat a^{\dagger}}^TM\mathbf{\hat a^{\dagger}}}|0,0\rangle.
\end{aligned}
\end{equation}

<div class="nav-footer">
  <a class="nav-prev" href="povm.md">
    ← Previous
  </a>

  <a class="nav-next" href="cc_derivation.md">
    Next →
  </a>
</div>

## References
<p id="ref-lvovsky2014">
[1] A. I. Lvovsky, 
<em>Squeezed Light</em>, 2014. Available: https://arxiv.org/abs/1401.4118
</p>