# Generalizing the optical element

In the [main derivation](https://nicosieber.github.io/spdc-coincidence-analysis/theory/cc_derivation/)
the optical element between source and detectors was a half-wave plate. This
section shows that the HWP was not special: the entire derivation of
\(P^{(\eta_H,\eta_V)}(0,0)\) goes through unchanged if the HWP is replaced by
**any** passive lossless element (a beam splitter, a phase shifter, a wave plate
at any angle, or any sequence of these). Only one matrix in the calculation
changes, and the final formula keeps exactly the same shape.

## The matrix \(M\) already contains the optics

Recall from [TMSV](https://nicosieber.github.io/spdc-coincidence-analysis/theory/tmsv/#eq:alpha_vec)
that the state after the HWP was written as

\[\begin{equation}
\label{eq:state_M}
\lvert \Psi \rangle
=
\Lambda\, e^{\frac{\lambda}{2}\,(\mathbf{\hat a^{\dagger}})^T M\,\mathbf{\hat a^{\dagger}}}\lvert 0,0 \rangle,
\qquad
M=
\begin{pmatrix}
 2cs & s^2-c^2 \\
 s^2-c^2 & -2cs
\end{pmatrix},
\end{equation}\]

with \(c=\cos(2\vartheta)\), \(s=\sin(2\vartheta)\) and \(\Lambda=\sqrt{1-|\lambda|^2}\).
It is worth seeing where this particular \(M\) comes from, because that is the
step we are going to generalize.

The TMSV **before** any optics is the special case \(\vartheta=0\), i.e.
\(c=1,\,s=0\). Its generator is the bare pair-creation term
\(\lambda\,\hat a_H^\dagger\hat a_V^\dagger\), i.e.

\[\begin{equation}
\label{eq:M0}
M_0=
\begin{pmatrix}
 0 & 1\\
 1 & 0
\end{pmatrix},
\qquad
\tfrac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^T M_0\,\mathbf{\hat a^{\dagger}}
=\lambda\,\hat a_H^\dagger \hat a_V^\dagger .
\end{equation}\]

The HWP acts on the two creation operators as a
matrix \(U\),

\[\begin{equation}
\label{eq:U_HWP}
\mathbf{\hat a^{\dagger}}\;\to\; U\,\mathbf{\hat a^{\dagger}},
\qquad
U_{\mathrm{HWP}}=
\begin{pmatrix}
 c & s\\
 s & -c
\end{pmatrix},
\end{equation}\]

exactly the linear combinations
\(c\,\hat a_H^\dagger + s\,\hat a_V^\dagger\) and
\(s\,\hat a_H^\dagger - c\,\hat a_V^\dagger\) that appear inside
\(\hat K^\dagger\). Substituting \(\mathbf{\hat a^{\dagger}}\to U\mathbf{\hat a^{\dagger}}\)
into the exponent of \(\eqref{eq:M0}\):

\[\begin{equation}
\label{eq:congruence}
\tfrac{\lambda}{2}\,(\mathbf{\hat a^{\dagger}})^T M_0\,\mathbf{\hat a^{\dagger}}
\;\to\;
\tfrac{\lambda}{2}\,(U\mathbf{\hat a^{\dagger}})^T M_0\,(U\mathbf{\hat a^{\dagger}})
=
\tfrac{\lambda}{2}\,(\mathbf{\hat a^{\dagger}})^T \underbrace{U^T M_0\, U}_{=\,M}\,\mathbf{\hat a^{\dagger}} .
\end{equation}\]

So the effect of the optics is nothing but a congruence of the source matrix,

\[\begin{equation}
\label{eq:M_from_U}
\boxed{\,M = U^T M_0\, U\,.}
\end{equation}\]

A quick check that this reproduces \(\eqref{eq:state_M}\):

\[\begin{equation}
\begin{aligned}
U^T M_0 U
&=
\begin{pmatrix} c & s\\ s & -c\end{pmatrix}
\begin{pmatrix} 0 & 1\\ 1 & 0\end{pmatrix}
\begin{pmatrix} c & s\\ s & -c\end{pmatrix}
=
\begin{pmatrix} 2cs & s^2-c^2\\ s^2-c^2 & -2cs\end{pmatrix}
=M .
\end{aligned}
\end{equation}\]

## Replacing the HWP by an arbitrary element

The generalization is now a single sentence: **let \(U\) be an arbitrary
\(2\times2\) unitary.** Every passive lossless element is of this form. For
example

\[\begin{equation}
U_{\text{phase}}=
\begin{pmatrix}1 & 0\\ 0 & e^{i\varphi}\end{pmatrix},
\qquad
U_{\text{BS}}=
\begin{pmatrix}\cos\theta_b & \sin\theta_b\\ -\sin\theta_b & \cos\theta_b\end{pmatrix},
\end{equation}\]

and a sequence of elements is just the product of their matrices. Unitarity is
not an extra assumption: it is precisely the condition that the transformed
operators still obey \([\hat a_i,\hat a_j^\dagger]=\delta_{ij}\), i.e. that the
element neither adds nor removes photons (it is lossless).

For any such \(U\), the state keeps the form \(\eqref{eq:state_M}\) with

\[\begin{equation}
M = U^T M_0\, U,
\qquad
M_0=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\end{equation}\]

The one property the derivation actually uses is that \(M\) is **symmetric**,
which holds for every \(U\): from \(\eqref{eq:M_from_U}\),
\((U^T M_0 U)^T=U^T M_0^T U=U^T M_0 U\) since \(M_0^T=M_0\). Symmetry of \(M\) is
all that the operator manipulations and the Gaussian integral on the main page
require, so they carry over verbatim.

!!! note "Real vs. complex elements"

    Wave plates and beam splitters are described by **real** \(U\) (rotations),
    so their \(M\) is real. Elements with a genuine phase, such as
    \(U_{\text{phase}}\), give a **complex** \(M\). This matters at exactly one
    place below: the bra side of the overlap carries \(M^{*}\), not \(M\), so
    the determinant that appears is
    \(\det(\mathbb 1-\lambda^2 M D M^{*}D)\). For real \(M\) this is identical
    to the main page's \(\det(\mathbb 1-\lambda^2 MDMD)\); we keep the
    conjugate explicit so the formula stays correct for complex elements too.

## The derivation is unchanged up to the determinant

Everything on the [coincidence-probability page](https://nicosieber.github.io/spdc-coincidence-analysis/theory/cc_derivation/)
between equation \(\eqref{eq:state_M}\) and the determinant is a manipulation of
the *operators* and of the coherent-state integral. None of those steps used the
specific entries of \(M\) — they used only that \(M\) is a symmetric
\(2\times2\) matrix, which holds for any \(U\). In particular the loss step

\[\begin{equation}
S\,\mathbf{\hat a^{\dagger}}\,S^{-1}=D\,\mathbf{\hat a^{\dagger}},
\qquad
D=\begin{pmatrix}t_H&0\\0&t_V\end{pmatrix},
\qquad t_{H,V}=1-\eta_{H,V},
\end{equation}\]

turns the exponent matrix \(M\) into \(DMD\) exactly as before, and the complex
Gaussian integral gives

\[\begin{equation}
P^{(\eta_H,\eta_V)}(0,0)
=\frac{\Lambda^2}{\sqrt{\det Q}},
\qquad
\det Q=\det\!\big(\mathbb 1-\lambda^2 M D M^{*}D\big).
\end{equation}\]

For real optics (\(M^{*}=M\)) this is the main page's
\(\det(\mathbb 1-\lambda^2 MDMD)\). So the **only** thing that depends on the
choice of optical element is this single \(2\times2\) determinant. We evaluate
it for a general \(M\), then specialize.

### The determinant for a general element

Using [determinant relation (9)](https://nicosieber.github.io/spdc-coincidence-analysis/concepts_and_foundations/determinant_relations/#appendix:det_1minusl2X)
for a \(2\times2\) matrix \(X=MDM^{*}D\),

\[\begin{equation}
\label{eq:detQ_general}
\det Q
=1-\lambda^2\,\mathrm{Tr}(MDM^{*}D)+\lambda^4\det(MDM^{*}D).
\end{equation}\]

The last term is fixed for every passive element: since \(M=U^TM_0U\) with \(U\)
unitary and \(\det M_0=-1\), we have \(|\det M|=1\), hence

\[\begin{equation}
\det(MDM^{*}D)=\det M\,\det M^{*}\,(\det D)^2=|\det M|^2\,t_H^2t_V^2=t_H^2t_V^2 .
\end{equation}\]

Only the trace \(\mathrm{Tr}(MDM^{*}D)\) carries the element-dependence, and it
is a short computation for whatever \(M\) the element produces.

### Specializing to the HWP

Insert the HWP matrix \(M\) of \(\eqref{eq:state_M}\). With
\(D=\mathrm{diag}(t_H,t_V)\),

\[\begin{equation}
MD=
\begin{pmatrix}
2cs\,t_H & (s^2-c^2)t_V\\
(s^2-c^2)t_H & -2cs\,t_V
\end{pmatrix},
\end{equation}\]

and squaring gives \(MDMD=\big(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\big)\)
with diagonal entries

\[\begin{equation}
\begin{aligned}
a&=(2cs)^2t_H^2+(s^2-c^2)^2t_Ht_V,\\
d&=(s^2-c^2)^2t_Ht_V+(2cs)^2t_V^2,
\end{aligned}
\end{equation}\]

exactly as on the main page. The trace is their sum,

\[\begin{equation}
\begin{aligned}
\mathrm{Tr}(MDMD)
&=a+d
=(2cs)^2(t_H^2+t_V^2)+2(s^2-c^2)^2\,t_Ht_V\\
&=(t_H^2+t_V^2)\sin^2(4\vartheta)+2t_Ht_V\cos^2(4\vartheta),
\end{aligned}
\end{equation}\]

using \(2cs=\sin(4\vartheta)\) and \(s^2-c^2=-\cos(4\vartheta)\). Substituting
this and \(\det(MDMD)=t_H^2t_V^2\) into \(\eqref{eq:detQ_general}\),

\[\begin{equation}
\det Q
=1-\lambda^2\big[(t_H^2+t_V^2)\sin^2(4\vartheta)+2t_Ht_V\cos^2(4\vartheta)\big]
+\lambda^4 t_H^2t_V^2 .
\end{equation}\]

The bracket collects into a perfect square plus a remainder,

\[\begin{equation}
(t_H^2+t_V^2)\sin^2(4\vartheta)+2t_Ht_V\cos^2(4\vartheta)
=2t_Ht_V+(t_H-t_V)^2\sin^2(4\vartheta),
\end{equation}\]

(using \(\cos^2=1-\sin^2\) and \(t_H^2+t_V^2-2t_Ht_V=(t_H-t_V)^2\)), so that

\[\begin{equation}
\det Q=(1-\lambda^2 t_Ht_V)^2-\lambda^2(t_H-t_V)^2\sin^2(4\vartheta),
\end{equation}\]

and with \(t_{H,V}=1-\eta_{H,V}\) and \(\Lambda^2=1-\lambda^2\) we recover
equation (1) of the main page:

\[\begin{equation}
\label{eq:P00_final}
\boxed{\;
P^{(\eta_H,\eta_V)}(0,0)
=\dfrac{1-\lambda^2}
{\sqrt{\big(1-\lambda^2(1-\eta_H)(1-\eta_V)\big)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}}\; .}
\end{equation}\]

The generalization has therefore cost nothing: the closed form for *any* passive
element is \(\eqref{eq:detQ_general}\), and each specific element only fixes the
single trace \(\mathrm{Tr}(MDM^{*}D)\).

## Two worked elements

### A phase shifter alone produces no fringe

Take \(U=U_{\text{phase}}\). Then

\[\begin{equation}
M=U^T M_0 U
=\begin{pmatrix}1&0\\0&e^{i\varphi}\end{pmatrix}
 \begin{pmatrix}0&1\\1&0\end{pmatrix}
 \begin{pmatrix}1&0\\0&e^{i\varphi}\end{pmatrix}
=e^{i\varphi}\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\end{equation}\]

This \(M\) is complex, so we use the conjugated determinant. With
\(M^{*}=e^{-i\varphi}\big(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\big)\),
the phases cancel in the product \(MDM^{*}D\):

\[\begin{equation}
MDM^{*}D
=e^{i\varphi}\begin{pmatrix}0&1\\1&0\end{pmatrix}D\,
 e^{-i\varphi}\begin{pmatrix}0&1\\1&0\end{pmatrix}D
=\begin{pmatrix}t_Ht_V&0\\0&t_Ht_V\end{pmatrix},
\end{equation}\]

so \(\mathrm{Tr}(MDM^{*}D)=2t_Ht_V\) and \(\det(MDM^{*}D)=t_H^2t_V^2\). Then

\[\begin{equation}
\det Q=1-2\lambda^2 t_Ht_V+\lambda^4t_H^2t_V^2=(1-\lambda^2 t_Ht_V)^2,
\qquad
P^{(\eta_H,\eta_V)}(0,0)=\frac{1-\lambda^2}{1-\lambda^2(1-\eta_H)(1-\eta_V)} .
\end{equation}\]

No \(\varphi\) survives. Physically: bucket detectors count photons, and a phase
alone moves no photons between the arms. To convert a phase into a detectable
change the modes must first be *mixed* — which is exactly what the HWP (or a
beam splitter) does, and why the interferometer sits where it does. (Had we
forgotten the conjugate and used \(MDMD\), \(\det Q\) would have come out
complex — a useful sign that the conjugated form is the correct one.)

### A beam splitter is the HWP with a relabelled angle

Take \(U=U_{\text{BS}}\). The same one-line multiplication as for the HWP gives

\[\begin{equation}
M=U^T M_0 U
=\begin{pmatrix}
-\sin 2\theta_b & \cos 2\theta_b\\
\cos 2\theta_b & \sin 2\theta_b
\end{pmatrix},
\end{equation}\]

which is the HWP matrix \(\eqref{eq:state_M}\) under
\(\sin 4\vartheta\to\sin 2\theta_b\), \(\cos 4\vartheta\to\cos 2\theta_b\) (up to
signs that square away in \(MDMD\)). Every formula on the main page therefore
holds for a variable beam splitter after the single replacement

\[\begin{equation}
\sin^2(4\vartheta)\;\longrightarrow\;\sin^2(2\theta_b).
\end{equation}\]

This also explains the location of the coincidence dip: \(\vartheta=\pi/8\)
means \(4\vartheta=\pi/2\), i.e. the HWP acts as a **balanced** beam splitter
(\(\theta_b=\pi/4\)) — the dip is a Hong–Ou–Mandel suppression in disguise.

!!! note "Beyond two modes"

    Nothing above was two-dimensional in an essential way. For a source of
    several Schmidt modes (e.g. a multimode JSA) the vector
    \(\mathbf{\hat a^{\dagger}}\) has more entries, \(M_0\) becomes
    block-diagonal with one \(\big(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\big)\)
    block per mode pair scaled by that mode's \(\lambda_k\), \(U\) is an
    \(m\times m\) unitary, and the very same steps give
    \(P(0,\dots,0)=\Lambda^2/\sqrt{\det(\mathbb 1-MDMD\,\text{-type})}\) as an
    \(m\times m\) determinant. What the closed form does require is that every
    element stay Gaussian — passive optics, squeezing and bucket detection all
    qualify; photon-number-resolving projections or feed-forward do not.


<div class="nav-footer">
  <a class="nav-prev" href="cc_derivation.md">
    ← Previous
  </a>
</div>