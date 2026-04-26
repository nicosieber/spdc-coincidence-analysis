# Derivation of the coincidence probability
To derive the analytical expression for the coincidence probability, equation (16) of [POVM](povm.md#formula_P_cc_loss) will be evaluated using the TMSV of the form depicted in equation (18) of [TMSV](tmsv.md#formula:tmsv_as_exp_2). For now, the focus now shall only be the evaluation of the term

\begin{equation}
\label{formula:last_term1}
\begin{aligned}
P^{(\eta_H,\eta_V)}(0,0)=&\langle \Psi \rvert\left(1-\eta_H\right)^{\hat{n}_H}\otimes \left(1-\eta_V\right)^{\hat{n}_V}\lvert \Psi \rangle\\
=&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} t_H^{\hat{n}_H} t_V^{\hat{n}_V} e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle
\end{aligned}
\end{equation}

where the abbreviations

\begin{equation}
    \label{eq:t_eta}
    t_{H,V}=1-\eta_{H,V}
\end{equation}

are used and the $\otimes$ was omitted for readability. Further,

\begin{equation}
S=t_H^{\hat{n}_H} t_V^{\hat{n}_V}
\end{equation}

and

\begin{equation}
\begin{aligned}
D=
\begin{pmatrix}
    t_H & 0 \\
    0 & t_V 
    \end{pmatrix}
\end{aligned}
\end{equation}

are introduced. It follows that

\begin{equation}
\label{formula:SaS_Da}
S\mathbf{\hat a^{\dagger}}S^{-1}=D\mathbf{\hat a^{\dagger}},
\end{equation}

and since $D$ is diagonal:

\begin{equation}
\left(D\mathbf{\hat a^{\dagger}}\right)^T=(\mathbf{\hat a^{\dagger}})^T D
\end{equation}

Due to the relations in equations (6) and (7) of [Conjugation of creation of operators](../concepts_and_foundations/conjugation_operators.md#eq:xpownadagger1) we get:

\begin{equation}
S\hat a_{H,V}^{\dagger}S^{-1}=t_{H,V}\hat a_{H,V}^{\dagger}.
\end{equation}

Then \(\eqref{formula:last_term1}\) becomes

\begin{equation}
\begin{aligned}
&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} t_H^{\hat{n}_H} t_V^{\hat{n}_V} e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle\\
=&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} S e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle\\
=&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} S e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}}S^{-1}S \lvert 0 \rangle\\
=&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} e^{\frac{\lambda}{2} S (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}S^{-1}}S \lvert 0 \rangle,
\end{aligned}
\end{equation}

which is achieved by inserting $S^{-1}S=\mathbf{1}$ and usage of the relation (9) of [Operator relations](../concepts_and_foundations/operator_relations.md#appendix:powerseries_final). By inserting $S^{-1}S=\mathbf{1}$ into the exponent and using \(\eqref{formula:SaS_Da}\) we get

\begin{equation}
\label{formula:tmsv_DaMDa}
\begin{aligned}
&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} e^{\frac{\lambda}{2} S (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}S^{-1}}S \lvert 0 \rangle\\
=&\Lambda^2\langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} e^{\frac{\lambda}{2} (S (\mathbf{\hat a^{\dagger}})^T S^{-1}) M (S \mathbf{\hat a^{\dagger}}S^{-1})}S \lvert 0 \rangle\\
=&\Lambda^2\langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} e^{\frac{\lambda}{2} (D\mathbf{\hat a^{\dagger}})^T M D\mathbf{\hat a^{\dagger}}}S \lvert 0 \rangle\\
=&\Lambda^2\langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T D M D\mathbf{\hat a^{\dagger}}}S \lvert 0 \rangle.
\end{aligned}
\end{equation}

Here, we made use of the fact that you can expand the indices of $(\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}$ which results in:

\begin{equation}
\begin{aligned}
&S\left((\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}\right)S^{-1}\\=&S\left(\sum_{i,j}M_{i,j}\hat a_i^{\dagger}\hat a_j^{\dagger}\right)S^{-1}\\
=&\sum_{i,j}M_{i,j}S\hat a_i^{\dagger}\hat a_j^{\dagger}S^{-1}\\
=&\sum_{i,j}M_{i,j}\left(S\hat a_i^{\dagger}S^{-1}\right)\left(S\hat a_j^{\dagger}S^{-1}\right)\\
=&\left(S(\mathbf{\hat a^{\dagger}})^TS^{-1}\right)M\left(S\mathbf{\hat a^{\dagger}}S^{-1}\right)
\end{aligned}
\end{equation}

By further using equation (2) of [Conjugation of creation operators](../concepts_and_foundations/conjugation_operators.md#eq:xpownm) we can see that

\begin{equation}
S \lvert 0 \rangle =\lvert 0 \rangle,
\end{equation}

which gives us

\begin{equation}
\label{eq:tmsv_aDMDa}
\begin{aligned}
&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}} t_H^{\hat{n}_H} t_V^{\hat{n}_V} e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T M \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle\\
=&\Lambda^2\langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}}  e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T DMD \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle
\end{aligned}
\end{equation}

Using die identity from equation (11) of [Coherent states](../concepts_and_foundations/coherent_states.md#eq:coherent_identity), expression \(\eqref{eq:tmsv_aDMDa}\) becomes

\begin{equation}
\label{eq:tmsv_coherent_identity}
\begin{aligned}
&\Lambda^2\langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}}
e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T L \mathbf{\hat a^{\dagger}}}\lvert 0 \rangle \\
=&\Lambda^2\int \dfrac{d^4\alpha}{\pi^2}   \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}}\lvert \alpha \rangle \langle \alpha \rvert e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T L \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle,
\end{aligned}
\end{equation}

with $DMD=L$ as an abbreviation. Also note that $\pi$ and $d^2\alpha$ are squared since we have a to modes:

\begin{equation}
\lvert \alpha \rangle=\lvert \alpha_H,\alpha_V \rangle
\end{equation}

By inserting the coherent-state resolution of the identity, the operator expression is transformed into an integral over phase-space variables. This reformulation introduces classical field amplitudes as integration variables, while the underlying quantum correlations remain encoded in the resulting Gaussian weight. 

In order to evaluate the expression \(\eqref{eq:tmsv_coherent_identity}\), we first need to show how $\mathbf{\hat a}^T M\mathbf{\hat a}$ acts on $\lvert \alpha \rangle$ . We can write 

\begin{equation}
\begin{aligned}
\hat a_{H}\lvert \alpha_H,\alpha_V \rangle&=\alpha_{H}\lvert \alpha_H,\alpha_V \rangle,\\
\hat a_{V}\lvert \alpha_H,\alpha_V \rangle&=\alpha_{V}\lvert \alpha_H,\alpha_V \rangle.
\end{aligned}
\end{equation}

Then we can write $\mathbf{\hat a}^T M\mathbf{\hat a}$ as

\begin{equation}
\label{eq:ama_1}
\begin{aligned}
&\mathbf{\hat a}^T M\mathbf{\hat a}\\
&=\sum_{i,j}\hat a_i M_{i,j}\hat a_j\\
&=2cs\hat a_H^2+(s^2-c^2)\hat a_H\hat a_V+(s^2-c^2)\hat a_V\hat a_H-2cs\hat a_V^2.
\end{aligned}
\end{equation}

Since the annihilation operators commute

\begin{equation}
\left[\hat a_H,\hat a_V\right]=0,
\end{equation}

we can shorten expression \(\eqref{eq:ama_1}\) a little bit:

\begin{equation}
\begin{aligned}
&\dfrac{1}{2}\mathbf{\hat a}^T M\mathbf{\hat a}\\
=&cs\hat a_H^2+(s^2-c^2)\hat a_H\hat a_V-cs\hat a_V^2
\end{aligned}
\end{equation}

Consequently, we can write

\begin{equation}
\begin{aligned}
&\mathbf{\hat a}^T M\mathbf{\hat a}\lvert \alpha \rangle\\
=&\left(cs\hat a_H^2+(s^2-c^2)\hat a_H\hat a_V-cs\hat a_V^2\right)\lvert \alpha_H,\alpha_V \rangle\\
=&\left(cs\alpha_H^2+(s^2-c^2)\alpha_H\alpha_V-cs\alpha_V^2\right)\lvert \alpha_H,\alpha_V \rangle\\
=&\alpha^TM\alpha \lvert \alpha \rangle
\end{aligned}
\end{equation}

Following that we can see how the exponential of \(\eqref{eq:tmsv_coherent_identity}\) evaluates by writing it as an infinite sum:

\begin{equation}
\begin{aligned}
\langle 0 \rvert \phi \rangle e^{\frac{\lambda}{2}\mathbf{\hat a}^T M\mathbf{\hat a}}\lvert \alpha \rangle&=\sum_{n=0}^\infty\dfrac{(\frac{\lambda}{2}\mathbf{\hat a}^T M\mathbf{\hat a})^n}{n!}\langle 0 \rvert \alpha \rangle\\
&=\sum_{n=0}^\infty\dfrac{(\frac{\lambda}{2}\alpha^TM\alpha)^n}{n!}\langle 0 \rvert \alpha \rangle\\
&=e^{\frac{\lambda}{2}\alpha^TM\alpha}\langle 0 \rvert \alpha \rangle
\end{aligned}
\end{equation}

For a normalized two-mode coherent state we can evaluate $\langle 0 \rvert \alpha \rangle$ (with the help of the equation (2) of [Coherent states](../concepts_and_foundations/coherent_states.md#formula:coherent_state_matrix)  and equation (17) of [TMSV](tmsv.md#eq:alpha_vec) to

\begin{equation}
\langle 0 \rvert \alpha \rangle=e^{-\frac{|\alpha_H|^2}{2}}e^{-\frac{|\alpha_V|^2}{2}}=e^{-\frac{\alpha^{\dagger}\alpha}{2}}.
\end{equation}

Following, we can see that 

\begin{equation}
\begin{aligned}
\langle 0 \rvert e^{\frac{\lambda}{2}\mathbf{\hat a}^T M\mathbf{\hat a}}\lvert \alpha \rangle
=e^{\frac{\lambda}{2}\alpha^TM\alpha-\frac{\alpha^{\dagger}\alpha}{2}},
\end{aligned}
\end{equation}

and following a similar logic, we can see that

\begin{equation}
\begin{aligned}
\langle \alpha \rvert e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T L \mathbf{\hat a^{\dagger}}} \lvert 0 \rangle=e^{\frac{\lambda}{2}(\alpha^*)^TL\alpha^*-\frac{\alpha^{\dagger}\alpha}{2}}.
\end{aligned}
\end{equation}

As an intermediate step, we now can rewrite \(\eqref{eq:tmsv_coherent_identity}\) as

\begin{equation}
\label{eq:intermediate}
\begin{aligned}
&\Lambda^2 \langle 0 \rvert e^{\frac{\lambda}{2} \mathbf{\hat a}^T M\mathbf{\hat a}}
e^{\frac{\lambda}{2} (\mathbf{\hat a^{\dagger}})^T L \mathbf{\hat a^{\dagger}}}\lvert 0 \rangle \\
=&\Lambda^2\int \dfrac{d^4\alpha}{\pi^2}   e^{\frac{\lambda}{2}(\alpha^*)^TL\alpha^* +\frac{\lambda}{2}\alpha^TM\alpha-\alpha^{\dagger}\alpha}
\end{aligned}
\end{equation}

Introduce the real variables

\begin{equation}
\begin{aligned}
\alpha=\frac{x+iy}{\sqrt{2}},
\qquad
\alpha^*=\frac{x-iy}{\sqrt{2}},
\qquad
x,y\in\mathbb R^2,
\end{aligned}
\end{equation}

and define

\begin{equation}
\begin{aligned}
\xi:=
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
x_H\\
x_V\\
y_H\\
y_V\\
\end{pmatrix}
\in\mathbb R^4.
\end{aligned}
\end{equation}

Then

\begin{equation}
\begin{aligned}
\chi:=
\begin{pmatrix}
\alpha\\
\alpha^*
\end{pmatrix}
=
W\xi,
\qquad
W:=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
\mathbb{1} & i\mathbb{1}\\
\mathbb{1} & -i\mathbb{1}
\end{pmatrix}.
\end{aligned}
\end{equation}

Moreover, the exponent can be written as

\begin{equation}
\begin{aligned}
\frac{\lambda}{2}(\alpha^*)^T L\,\alpha^*
+
\frac{\lambda}{2}\alpha^T M\,\alpha
-
\alpha^\dagger \alpha
=
-\frac12\,\chi^T Q\,\chi,
\end{aligned}
\end{equation}

with

\begin{equation}
\label{eq:Q}
\begin{aligned}
Q=
\begin{pmatrix}
-\lambda M & \mathbb{1}\\
\mathbb{1} & -\lambda L
\end{pmatrix}.
\end{aligned}
\end{equation}

Using \(\chi=W\xi\), this becomes

\begin{equation}
-\frac12\,\chi^T Q\,\chi
=
-\frac12\,\xi^T W^T Q W\,\xi.
\end{equation}

Hence, defining

\begin{equation}
A:=W^T Q W,
\end{equation}

we obtain

\begin{equation}
I
=
\int \frac{d^2\alpha}{\pi^2}\,
\exp\!\left(-\frac12\,\xi^T A\,\xi\right),
\end{equation}

with $I$ being only the integral of equation \(\eqref{eq:intermediate}\). Now the measure transforms as

\begin{equation}
d^4\alpha
=
d^2\alpha_H\,d^2\alpha_V
=
\frac14\,dx_H\,dy_H\,dx_V\,dy_V
=
\frac14\,d^4\xi,
\end{equation}

so that

\begin{equation}
\frac{d^4\alpha}{\pi^2}
=
\frac{d^4\xi}{(2\pi)^2}.
\end{equation}

Therefore,

\begin{equation}
I
=
\int \frac{d^4\xi}{(2\pi)^2}
\exp\!\left(-\frac12\,\xi^T A\,\xi\right),
\qquad
A=W^T Q W.
\end{equation}

Evaluating \(A\) explicitly gives

\begin{equation}
\begin{aligned}
A&=
\begin{pmatrix}
\mathbb{1}-\dfrac{\lambda}{2}(L+M) & \dfrac{i\lambda}{2}(L-M)\\[2mm]
\dfrac{i\lambda}{2}(L-M) & \mathbb{1}+\dfrac{\lambda}{2}(L+M)
\end{pmatrix}\\
&=
\begin{pmatrix}
\mathbb{1}-\dfrac{\lambda}{2}(L+M) & 0\\[2mm]
0 & \mathbb{1}+\dfrac{\lambda}{2}(L+M)
\end{pmatrix}\\
&+
i\begin{pmatrix}
0 & \dfrac{\lambda}{2}(L-M)\\[2mm]
\dfrac{\lambda}{2}(L-M) & 0
\end{pmatrix}\\
&=B+iC=\mathbb{R}(A)+i\mathbb{I}(A)
\end{aligned}
\end{equation}

## Evaluation of the complex Gaussian integral

We now evaluate

\begin{equation}
\begin{aligned}
I
=
\int \frac{d^4\xi}{(2\pi)^2}
\exp\!\left(-\frac12\,\xi^T A\,\xi\right),
\qquad
A=W^TQW.
\end{aligned}
\end{equation}

Since $A$ is not purely real, we write it as

\begin{equation}
A=B+iC,
\end{equation}

where $B=\mathbb{R}(A)$ and $C=\mathbb{I}(A)$ are real $4\times4$ matrices. From the explicit form of $A$ we see that both $B$ and $C$ are symmetric, hence

\begin{equation}
A^T=A,\qquad B^T=B,\qquad C^T=C.
\end{equation}

Therefore,

\begin{equation}
\xi^T A\xi=\xi^T B\xi+i\,\xi^T C\xi.
\end{equation}

The integral thus becomes

\begin{equation}
\begin{aligned}
I
=
\int \frac{d^4\xi}{(2\pi)^2}
\exp\!\left(-\frac12\,\xi^T B\xi\right)
\exp\!\left(-\frac{i}{2}\,\xi^T C\xi\right).
\end{aligned}
\end{equation}

As long as $B$ is positive definite, the integral converges absolutely, since

\begin{equation}
\left|
\exp\!\left(-\frac12\,\xi^T A\xi\right)
\right|
=
\exp\!\left(-\frac12\,\xi^T B\xi\right).
\end{equation}

Because $B$ is real symmetric and positive definite, it possesses a real symmetric square root $B^{1/2}$ with inverse $B^{-1/2}$. We may therefore factorize $A$ as

<span id="A_factorization"></span>

\begin{equation}
A
=
B^{1/2}\left(\mathbb{1}+iK\right)B^{1/2},
\qquad
K:=B^{-1/2}CB^{-1/2}.
\end{equation}

Since $C$ is real symmetric, $K$ is also real symmetric:

\begin{equation}
K^T=K.
\end{equation}

Next, we perform the change of variables

\begin{equation}
y=B^{1/2}\xi,
\qquad
\xi=B^{-1/2}y.
\end{equation}

The Jacobian of this transformation is

\begin{equation}
d^4\xi=\frac{d^4y}{\sqrt{\det B}}.
\end{equation}

Moreover,

\begin{equation}
\begin{aligned}
\xi^T A\xi
&=\xi^T B^{1/2}\left(\mathbb{1}+iK\right)B^{1/2}\xi\\
&=y^T\left(\mathbb{1}+iK\right)y.
\end{aligned}
\end{equation}

Hence the integral becomes

\begin{equation}
I
=
\frac{1}{\sqrt{\det B}}
\int \frac{d^4y}{(2\pi)^2}
\exp\!\left[
-\frac12\,y^T\left(\mathbb{1}+iK\right)y
\right].
\end{equation}

Since $K$ is real symmetric, it can be diagonalized by an orthogonal matrix. Thus, there exists (see <a href="#ref-axler2024">[1]</a>) an orthogonal matrix $O$ such that

\begin{equation}
K=O^T\Lambda O,
\qquad
\Lambda=\mathrm{diag}(\kappa_1,\kappa_2,\kappa_3,\kappa_4),
\end{equation}

with real eigenvalues $\kappa_j$. We now define

\begin{equation}
z=Oy.
\end{equation}

Because $O$ is orthogonal, we have

\begin{equation}
d^4y=d^4z,
\qquad
y^Ty=z^Tz.
\end{equation}

Furthermore,

\begin{equation}
\begin{aligned}
y^T\left(\mathbb{1}+iK\right)y
&=
y^Ty+i\,y^TKy\\
&=
z^Tz+i\,z^T\Lambda z\\
&=
\sum_{j=1}^4 (1+i\kappa_j)z_j^2.
\end{aligned}
\end{equation}

Therefore, the integral factorizes into four one-dimensional Gaussian integrals:

\begin{equation}
I
=
\frac{1}{\sqrt{\det B}}
\prod_{j=1}^4
\int \frac{dz_j}{\sqrt{2\pi}}
\exp\!\left[
-\frac12(1+i\kappa_j)z_j^2
\right].
\end{equation}

Each factor is a convergent Gaussian integral because

\begin{equation}
\mathbb{R}(1+i\kappa_j)=1>0.
\end{equation}

Using the standard Gaussian formula

\begin{equation}
\int_{-\infty}^{\infty}\frac{dz}{\sqrt{2\pi}}
\exp\!\left(-\frac{a}{2}z^2\right)
=
\frac{1}{\sqrt{a}},
\qquad
\mathbb{R}(a)>0,
\end{equation}

we obtain

\begin{equation}
\int \frac{dz_j}{\sqrt{2\pi}}
\exp\!\left[
-\frac12(1+i\kappa_j)z_j^2
\right]
=
\frac{1}{\sqrt{1+i\kappa_j}}.
\end{equation}

Thus,

\begin{equation}
\begin{aligned}
I
&=
\frac{1}{\sqrt{\det B}}
\prod_{j=1}^4 \frac{1}{\sqrt{1+i\kappa_j}}\\
&=
\frac{1}{\sqrt{\det B}}
\frac{1}{\sqrt{\prod_{j=1}^4 (1+i\kappa_j)}}.
\end{aligned}
\end{equation}

Since

\begin{equation}
\prod_{j=1}^4 (1+i\kappa_j)
=
\det(\mathbb{1}+iK),
\end{equation}

this becomes

\begin{equation}
I
=
\frac{1}{\sqrt{\det B\,\det(\mathbb{1}+iK)}}.
\end{equation}

Finally, using

\begin{equation}
A
=
B^{1/2}\left(\mathbb{1}+iK\right)B^{1/2},
\end{equation}

we get

\begin{equation}
\begin{aligned}
\det A
&=
\det(B^{1/2})\det(\mathbb{1}+iK)\det(B^{1/2})\\
&=
\det(B)\det(\mathbb{1}+iK).
\end{aligned}
\end{equation}

Therefore,

\begin{equation}
I
=
\int \frac{d^4\xi}{(2\pi)^2}
\exp\!\left(-\frac12\,\xi^T A\,\xi\right)
=
\frac{1}{\sqrt{\det A}}.
\end{equation}

After transforming the expression into a real quadratic form, the problem reduces to a multivariate Gaussian integral. Expressions of this form are equivalent to those encountered in the phase-space description of Gaussian states via the Wigner function formalism, where the matrix $A$ can be interpreted as an effective inverse covariance matrix  (see <a href="#ref-ferraro2005">[2]</a>, <a href="#ref-brask2022">[3]</a>).

While this connection provides useful conceptual insight, the following calculation is carried out within the present operator-based framework in order to maintain a direct and explicit derivation. In order to evaluate $\det A$, we recall that $A=W^TQW$. Consequently, the determinant of $A$ is

\begin{equation}
\begin{aligned}
\det A &= \det(W^TQW)\\
&=\det (W)^2\det Q\\
&=\det Q,
\end{aligned}
\end{equation}

with $\det(W)^2=\mathbb 1$. Using (\ref{appendix:det_of_blockmatrix}) and (\ref{eq:Q}), we are able to rewrite $\det A$ as:

\begin{equation}
\begin{aligned}
\det A&=\det(\lambda^2ML-\mathbb{1})\\
&=\det(\mathbb{1}-\lambda^2ML)\\
&=\det(\mathbb{1}-\lambda^2MDMD)
\end{aligned}
\end{equation}

## Evaluation of the determinant

\begin{equation}
\begin{aligned}
MD&=
\begin{pmatrix}
2cs\,t_H & (s^2-c^2)t_V\\
(s^2-c^2)t_H & -2cs\,t_V
\end{pmatrix},
\end{aligned}
\end{equation}

and therefore

\begin{equation}
\label{eq:mdmd_abbreviation}
\begin{aligned}
MDMD=
\begin{pmatrix}
a &
b
\\
c &
d
\end{pmatrix},
\end{aligned}
\end{equation}

with

\begin{equation}
\begin{aligned}
a&=(2cs)^2t_H^2+(s^2-c^2)^2t_Ht_V\\
b&=2cs(s^2-c^2)t_V(t_H-t_V)\\
c&=2cs(s^2-c^2)t_H(t_H-t_V)\\
d&=(s^2-c^2)^2t_Ht_V+(2cs)^2t_V^2.
\end{aligned}
\end{equation}

Using equation (9) of [Determinant relations](../concepts_and_foundations/determinant_relations.md#appendix:det_1minusl2X) $\det Q$ becomes

\begin{equation}
\begin{aligned}
\det Q
&=\det\!\left(\mathbb{1}-\lambda^2MDMD\right)\\
&=
1-\lambda^2\mathrm{Tr}(MDMD)
+\lambda^4 \det(MDMD).
\end{aligned}
\end{equation}

Using

\begin{equation}
2cs=\sin(4\vartheta),
\qquad
s^2-c^2=-\cos(4\vartheta),
\end{equation}

this becomes

\begin{equation}
\begin{aligned}
\det Q
=
&1\\
-&\lambda^2\left((t_H^2+t_V^2)\sin^2(4\vartheta)+2t_Ht_V\cos^2(4\vartheta)\right)\notag\\
+&\lambda^4 t_H^2t_V^2.
\end{aligned}
\end{equation}

Equivalently,

\begin{equation}
\det Q
=
(1-\lambda^2 t_Ht_V)^2
-\lambda^2(t_H-t_V)^2\sin^2(4\vartheta),
\end{equation}

or with \(\eqref{eq:t_eta}\)

\begin{equation}
\begin{aligned}
\det Q
&=
\left(1-\lambda^2(1-\eta_H)(1-\eta_V)\right)^2\\
&-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta).
\end{aligned}
\end{equation}

Finally, we can write $P^{(\eta_H,\eta_V)}(0,0)$ from equation \(\eqref{formula:last_term1}\) as

\begin{equation}
\begin{aligned}
&P^{(\eta_H,\eta_V)}(0,0)=\langle \Psi \rvert \left(1-\eta_H\right)^{\hat{n}_H}\otimes \left(1-\eta_V\right)^{\hat{n}_V}\lvert \Psi \rangle\\
=&\dfrac{(1-\lambda^2)}{\sqrt{\left(1-\lambda^2(1-\eta_H)(1-\eta_V)\right)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}}.
\end{aligned}
\end{equation}

In order to calculate $P^{(\eta_{H})}_{H}(0)$ or $P^{(\eta_{V})}_{V}(0)$, we can set $\eta_{V}=0$ or $\eta_{H}=0$. For $P^{(\eta_{H})}_{H}(0)$ we therefore get

\begin{equation}
\begin{aligned}
P^{(\eta_{H})}_{H}(0)&=P^{(\eta_H,\eta_V=0)}(0,0)\\
&=\dfrac{(1-\lambda^2)}{\sqrt{\left(1-\lambda^2(1-\eta_H)\right)^2-\lambda^2\eta_H^2\sin^2(4\vartheta)}},
\end{aligned}
\end{equation}

and $P^{(\eta_{V})}_{V}(0)$ we get

\begin{equation}
\begin{aligned}
P^{(\eta_{V})}_{V}(0)&=P^{(\eta_H=0,\eta_V)}(0,0)\\
&=\dfrac{(1-\lambda^2)}{\sqrt{\left(1-\lambda^2(1-\eta_V)\right)^2-\lambda^2\eta_V^2\sin^2(4\vartheta)}}.
\end{aligned}
\end{equation}

## Interpretation of the no-click and coincidence probabilities

For two bucket detectors measuring the $H$ and $V$ output modes, each detector has only two possible outcomes:
click or no click. Therefore, in each trial there are four mutually exclusive joint outcomes:

\begin{equation}
\begin{aligned}
&\text{(i) no click in either arm}, \nonumber\\
&\text{(ii) only the $H$ detector clicks}, \nonumber\\
&\text{(iii) only the $V$ detector clicks}, \nonumber\\
&\text{(iv) both detectors click (coincidence).} \nonumber
\end{aligned}
\end{equation}

It is useful to assign probabilities to these four elementary outcomes:

\begin{equation}
\begin{aligned}
P_{00} &:= \Pr(\text{no click in $H$ and no click in $V$}),\\
P_{H\text{-only}} &:= \Pr(\text{$H$ clicks and $V$ does not click}),\\
P_{V\text{-only}} &:= \Pr(\text{$V$ clicks and $H$ does not click}),\\
P_{\mathrm{cc}} &:= \Pr(\text{$H$ clicks and $V$ clicks}).
\end{aligned}
\end{equation}

Since these four events are disjoint and exhaustive, their probabilities must sum to unity:

\begin{equation}
1 = P_{00} + P_{H\text{-only}} + P_{V\text{-only}} + P_{\mathrm{cc}}.
\label{eq:four_outcomes_sum}
\end{equation}

## Connection to the notation $P_H^{(\eta)}(0)$, $P_V^{(\eta)}(0)$, and $P^{(\eta_H,\eta_V)}(0,0)$

The quantity

\begin{equation}
P_H^{(\eta_H)}(0)
=
\langle \Psi | (1-\eta_H)^{\hat n_H}\otimes I |\Psi\rangle
\end{equation}

is the probability that the $H$ detector does not click, irrespective of what happens in the $V$ arm. Hence it contains two of the four elementary outcomes:

\begin{equation}
P_H^{(\eta_H)}(0) = P_{00} + P_{V\text{-only}}.
\label{eq:PH_meaning}
\end{equation}


Similarly,

\begin{equation}
P_V^{(\eta_V)}(0)
=
\langle \Psi | I\otimes (1-\eta_V)^{\hat n_V} |\Psi\rangle
\end{equation}

is the probability that the $V$ detector does not click, regardless of what happens in the $H$ arm, so that

\begin{equation}
P_V^{(\eta_V)}(0) = P_{00} + P_{H\text{-only}}.
\label{eq:PV_meaning}
\end{equation}

Finally, the joint no-click probability is

\begin{equation}
P^{(\eta_H,\eta_V)}(0,0)
=
\langle \Psi | (1-\eta_H)^{\hat n_H}\otimes (1-\eta_V)^{\hat n_V} |\Psi\rangle,
\end{equation}

which is precisely the probability that neither detector clicks:

\begin{equation}
P^{(\eta_H,\eta_V)}(0,0)=P_{00}.
\label{eq:P00_meaning}
\end{equation}

## Connection to the coincidence probability

The coincidence probability is the probability that both detectors click:

\begin{equation}
P_{\mathrm{coinc}}
=
P_{\mathrm{cc}}.
\end{equation}

Using equations~\eqref{eq:PH_meaning}--\eqref{eq:P00_meaning}, it follows that

\begin{equation}
P_{\mathrm{coinc}}
=
1 - P_H^{(\eta_H)}(0) - P_V^{(\eta_V)}(0) + P^{(\eta_H,\eta_V)}(0,0),
\label{eq:Pcoinc_inclusion_exclusion}
\end{equation}

which is just the inclusion--exclusion formula for the event that both detectors click.

## Connection to the lossless notation

In the lossless discussion, one often groups the four elementary outcomes into only three classes:

\begin{equation}
\begin{aligned}
P_{\text{no-click}} &:= P_{00},\\
P_{\text{1-click}} &:= P_{H\text{-only}} + P_{V\text{-only}},\\
P_{\text{coinc.}} &:= P_{\mathrm{cc}}.
\end{aligned}
\end{equation}

Equation~\eqref{eq:four_outcomes_sum} then becomes

\begin{equation}
1 \overset{!}{=} P_{\text{no-click}} + P_{\text{1-click}} + P_{\text{coinc.}}.
\label{eq:lossless_grouped}
\end{equation}

Thus, the quantities $P_H^{(\eta_H)}(0)$ and $P_V^{(\eta_V)}(0)$ are not additional detector outcomes by themselves. Rather, they are marginal no-click probabilities, i.e.\ partial sums over the four elementary outcomes:

\begin{equation}
\begin{aligned}
P_H^{(\eta_H)}(0) &= P_{\text{no-click}} + P_{V\text{-only}},\\
P_V^{(\eta_V)}(0) &= P_{\text{no-click}} + P_{H\text{-only}}.
\end{aligned}
\end{equation}

They appear naturally when expanding the POVM expression for the coincidence event.

## References
<p id="ref-axler2024">
[1] S. Axler, <em>Linear Algebra Done Right</em>, 4th ed., Springer, 2024. Available: https://linear.axler.net/LADR4e.pdf
</p>

<p id="ref-ferraro2005">
[2] A. Ferraro, S. Olivares, and M. G. A. Paris, 
<em>Gaussian states in continuous variable quantum information</em>, 2005. Available: https://arxiv.org/abs/quant-ph/0503237
</p>

<p id="ref-brask2022">
[3] J. B. Brask, 
<em>Gaussian states and operations -- a quick reference</em>, 2022. Available: https://arxiv.org/abs/2102.05748
</p>