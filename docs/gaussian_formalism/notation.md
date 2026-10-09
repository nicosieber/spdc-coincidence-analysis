# Notation

As in equation (18) of [TMSV](../theory/tmsv.md#formula:tmsv_as_exp_2):

<span id="eq2"></span>

$$
\lvert \Psi \rangle=\Lambda\, e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}}\lvert 0,0 \rangle,
\qquad
\Lambda=\sqrt{1-\lambda^2},
\qquad
\mathbf{\hat a}=\begin{pmatrix}\hat a_H\\ \hat a_V\end{pmatrix},
\tag{2}
$$

with real $\lambda=\tanh r$ and squeezing parameter $r$ <a href="#ref-lvovsky2014">[12]</a>. The matrix $M$ was defined in [TMSV](../theory/tmsv.md) through $c=\cos(2\vartheta)$ and $s=\sin(2\vartheta)$, where $\vartheta$ is the HWP angle. Its entries simplify with the double-angle identities

$$
2cs=2\sin(2\vartheta)\cos(2\vartheta)=\sin(4\vartheta),
\qquad
s^2-c^2=\sin^2(2\vartheta)-\cos^2(2\vartheta)=-\cos(4\vartheta),
$$

the same identities the main derivation uses for $\det Q$. Since $\sin(4\vartheta)$ and $\cos(4\vartheta)$ appear in almost every matrix of this section, the following **shorthand** is used:

$$
\boxed{\;S_4:=\sin(4\vartheta),\qquad C_4:=\cos(4\vartheta)\;}
$$

The subscript $4$ refers to the angle $4\vartheta$. $S_4$ has nothing to do with the operator $S=t_H^{\hat n_H}t_V^{\hat n_V}$ of the main derivation. With this shorthand,

<span id="eq3"></span>

$$
M=
\begin{pmatrix}
2cs & s^2-c^2\\
s^2-c^2 & -2cs
\end{pmatrix}
=
\begin{pmatrix}
S_4 & -C_4\\
-C_4 & -S_4
\end{pmatrix}.
\tag{3}
$$

The only property of $M$ used in this section is

<span id="eq4"></span>

$$
M^2=
\begin{pmatrix}
S_4^2+C_4^2 & -S_4C_4+C_4S_4\\
-C_4S_4+S_4C_4 & C_4^2+S_4^2
\end{pmatrix}
=\mathbb{1}.
\tag{4}
$$

The detector matrices are

<span id="eq5"></span>

$$
D=\begin{pmatrix}t_H&0\\0&t_V\end{pmatrix}=\begin{pmatrix}1-\eta_H&0\\0&1-\eta_V\end{pmatrix},
\qquad
\mathbb{1}-D=\begin{pmatrix}\eta_H&0\\0&\eta_V\end{pmatrix}.
\tag{5}
$$

$D$ holds the probabilities that a photon is *missed*, and $\mathbb{1}-D$ the probabilities that it is *detected*. In this section the second one appears.

## References

<p id="ref-lvovsky2014">
[12] A. I. Lvovsky,
<em>Squeezed Light</em>, 2014. Available: https://arxiv.org/abs/1401.4118
</p>
