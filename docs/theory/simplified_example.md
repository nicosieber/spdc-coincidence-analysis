# Simplified example

First I show a simplified example of the calculation by only passing the state 

<span id="initial_state"></span>

\begin{equation}
\lvert 1_{H},1_{V} \rangle =\hat a_H^\dagger \hat a_V^\dagger\lvert 0,0 \rangle
\label{initial_state_simple}
\end{equation}

through the HWP. 

In equation \(\eqref{initial_state_simple}\), $\hat a_{H,V}^\dagger$ are the bosonic creation operators (for $H$- and $V$-polarized light) following the relation

\begin{equation}
\lvert n_H, n_V \rangle
=
\frac{(\hat a_H^\dagger)^{n_H}(\hat a_V^\dagger)^{n_V}}{\sqrt{n_H!n_V!}}
\lvert 0,0 \rangle
\label{eq:fock}
\end{equation}

Assuming that the fast axis of the HWP is aligned with the horizontal axis, the Jones matrix is given by [@collett2005fieldguidepolarization]

\begin{equation}
\label{Jones}
    U_{\text{HWP}}(\vartheta) = 
    \begin{pmatrix}
    \cos(2\vartheta) & \sin(2\vartheta) \\
    \sin(2\vartheta) & -\cos(2\vartheta) 
    \end{pmatrix},
\end{equation}

with $\vartheta$ being the angle of the HWP. With \(\eqref{initial_state_simple}\) and \(\eqref{Jones}\) we get the transformation

\begin{equation}
\label{Transformation:trafo}
\begin{pmatrix}
\hat a_{H,\text{new}}^\dagger \\
\hat a_{V,\text{new}}^\dagger
\end{pmatrix}
=
\begin{pmatrix}
\cos(2\vartheta) & \sin(2\vartheta) \\
\sin(2\vartheta) & -\cos(2\vartheta)
\end{pmatrix}
\begin{pmatrix}
\hat a_{H,\text{old}}^\dagger \\
\hat a_{V,\text{old}}^\dagger
\end{pmatrix}
\end{equation}

which can be used to write the state after the HWP as

\begin{equation}
\label{Transformation:state_simple}
\begin{aligned}
    \lvert 1_H,1_V\rangle&=\hat a_H^\dagger \hat a_V^\dagger\lvert 0,0 \rangle\notag\\
    &\overset{\eqref{Transformation:trafo}}{\Rightarrow} \left(\hat a_H^\dagger\cos(2\vartheta)+\hat a_V^\dagger\sin(2\vartheta)\right)\notag\\
    &\times\left(\hat a_H^\dagger\sin(2\vartheta)-\hat a_V^\dagger\cos(2\vartheta)\right)\lvert 0,0 \rangle.
\end{aligned}
\end{equation}

Evaluating the terms of \(\eqref{Transformation:state_simple}\) results in:

\begin{equation}
\label{Transformation:terms_simple}
\begin{aligned}
\cos(2\vartheta)\sin(2\vartheta)(\hat a_H^\dagger)^2\lvert 0,0 \rangle
&= \sqrt{2}\cos(2\vartheta)\sin(2\vartheta)\lvert 2,0 \rangle \\
-\cos(2\vartheta)\sin(2\vartheta)(\hat a_V^\dagger)^2\lvert 0,0 \rangle
&= -\sqrt{2}\cos(2\vartheta)\sin(2\vartheta)\lvert 0,2 \rangle \\
-\cos^2(2\vartheta)\hat a_H^\dagger \hat a_V^\dagger\lvert 0,0 \rangle
&= -\cos^2(2\vartheta)\lvert 1,1 \rangle \\
\sin^2(2\vartheta)\hat a_H^\dagger \hat a_V^\dagger\lvert 0,0 \rangle
&= \sin^2(2\vartheta)\lvert 1,1 \rangle 
\end{aligned}
\end{equation}

Remark on notation: In the equations of \(\eqref{Transformation:terms_simple}\), the indices for polarization were left out and further won't be used anymore due to convenience. To further make it easier to differentiate which polarization is meant, the convention of choosing $H$ polarization for the first and $V$ polarization for the second mode when using the $\lvert \cdot \rangle$-notation will strictly be followed (when using operator notation indices will be used).

Looking at the terms of \(\eqref{Transformation:terms_simple}\), we see that for the $\vartheta=\pi/8+k\pi/4$ and $k=0,1,2,3,...$, the terms containing one $H$ and one $V$ photon cancel each other due to destructive interference. However, this case only happens under the following conditions:

- The $H$ and $V$ photons occupy the same spatial mode.
- The photons must be indistinguishable in all degrees of freedom besides polarization.

Consequently, for $\vartheta=\pi/8$, the sum of terms in \(\eqref{Transformation:terms_simple}\) becomes

\begin{equation}
\label{Transformation:state_simple_special}
\begin{aligned}
\lvert 1_H,1_V \rangle
&= \hat a_H^\dagger \hat a_V^\dagger \lvert 0,0 \rangle \notag\\
&\overset{\eqref{Transformation:trafo},\,\vartheta=\pi/8}{\Rightarrow}
\dfrac{1}{\sqrt{2}}\left(\lvert 2,0\rangle - \lvert 0,2 \rangle\right)
\end{aligned}
\end{equation}



<div class="nav-footer">
  <a class="nav-prev" href="overview.md">
    ← Previous
  </a>

  <a class="nav-next" href="povm.md">
    Next →
  </a>
</div>

## References