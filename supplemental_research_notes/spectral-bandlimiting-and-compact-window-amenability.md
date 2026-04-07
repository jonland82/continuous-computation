---
title: Spectral Bandlimiting and Compact-Window Amenability
author: |
  **J. R. Landers**  
  *Supplementary research note*
fontsize: 11pt
geometry: margin=1.1in
header-includes:
  - |
    \usepackage{amsmath,amssymb}
---

This note supplements [the-geometry-of-computable-trajectories.html](../the-geometry-of-computable-trajectories.html), especially its spectral discussion, and the worked contrast in [when-continuous-trajectories-can-and-cannot-compute.html](../when-continuous-trajectories-can-and-cannot-compute.html). The geometry paper states a transfer-operator spectral criterion for membership in the amenable set $\mathcal{A}$; the worked examples paper shows, concretely, that bounded crossing density rather than smoothness is the decisive geometric feature. The present note gives a constructive Fourier-side surrogate: low-pass projection sends an $L^2$ signal into an entire-function class whose zero crossings are locally finite on every compact window.

This is intentionally weaker than the global function-space claim in the main geometry paper. It produces compact-window amenability rather than a uniform global dwell-time bound. That limitation matters, and it is stated explicitly below. The companion note [finite-horizon-geometry-of-computational-amenability.md](finite-horizon-geometry-of-computational-amenability.md) shows how such compact-window control feeds into a finite-horizon $(\varepsilon,\eta,\lambda)$ budget.

We work in the setting of the preceding papers. Let $\mathcal{A} \subset C(\mathbb{R})$ denote the set of trajectories admitting a coarse-graining $\Pi$ with positive minimum dwell time $\tau_{\min} > 0$, and let $\mathcal{N} = C(\mathbb{R}) \setminus \mathcal{A}$ denote its complement. Since $\mathcal{A}$ is not a vector space, there is no orthogonal projection $C(\mathbb{R}) \to \mathcal{A}$. The Fourier transform nevertheless furnishes a canonical family of maps into an amenable subclass, parameterized by bandwidth.

**Proposition (Spectral projection into a compact-window amenable class).** Let $x \in L^2(\mathbb{R})$ have Fourier transform
$$
\hat{X}(f) = \int_{\mathbb{R}} x(t) e^{-2\pi i f t}\,dt.
$$

For $W > 0$, define the bandlimited projection
$$
x_W(t) = \int_{-W}^{W} \hat{X}(f) e^{2\pi i f t}\,df.
$$

Then:

(i) $x_W$ extends to an entire function of exponential type $2\pi W$.

(ii) If $x_W \not\equiv 0$, then its zero set
$$
Z(x_W) = \{t \in \mathbb{R} : x_W(t) = 0\}
$$
is discrete and has no accumulation point. In particular, $Z(x_W) \cap [a,b]$ is finite for every compact interval $[a,b]$.

(iii) For the binary coarse-graining
$$
\Pi(x) =
\begin{cases}
R, & x \ge 0,\\
L, & x < 0,
\end{cases}
$$
the minimum dwell time satisfies
$$
\tau_{\min}(x_W,\Pi)\big|_{[a,b]} > 0
$$
on every compact interval $[a,b]$. Consequently, $x_W$ is computation-amenable on every compact observation window.

(iv) The number of zeros in any interval of length $T$ satisfies
$$
\lvert Z(x_W) \cap [a,a+T] \rvert \le 2WT + O(1),
$$
where the implicit constant depends on $x_W$ but not on $a$ or $T$.

*Proof.* Statement (i) is the Paley-Wiener theorem: a function whose Fourier transform has compact support in $[-W,W]$ extends to an entire function of exponential type $\sigma = 2\pi W$.

For (ii), the zeros of a nonzero entire function are isolated by the identity theorem. Since $x_W$ is entire, if $x_W \not\equiv 0$, then $Z(x_W)$ has no accumulation point in $\mathbb{C}$, and hence none in $\mathbb{R}$. Finiteness on compact intervals follows immediately.

For (iii), finiteness of $Z(x_W) \cap [a,b]$ implies that the consecutive zeros $t_1 < \cdots < t_m$ have positive minimum gap,
$$
\min_j (t_{j+1} - t_j) > 0.
$$

Between consecutive zeros, continuity prevents $x_W$ from changing sign, so the trajectory remains in a single cell of $\Pi$ for at least that duration. Thus the induced symbolic trajectory has positive minimum dwell time on every compact interval.

For (iv), the classical zero-density estimate for entire functions of exponential type $\sigma$ gives a counting-function bound
$$
n(T) \le \frac{\sigma T}{\pi} + O(1).
$$

Substituting $\sigma = 2\pi W$ yields
$$
n(T) \le 2WT + O(1).
$$

This completes the proof.

**Definition (Spectral amenability ratio).** Let $x \in L^2(\mathbb{R})$ with $\lVert x \rVert_2 > 0$, and let the dwell-time target be $\tau > 0$. Set
$$
W(\tau) = \frac{1}{2\tau}
$$
and define
$$
\rho_{\mathcal{A}}(x,\tau)
= \frac{\displaystyle \int_{-W(\tau)}^{W(\tau)} \lvert \hat{X}(f) \rvert^2\,df}{\displaystyle \int_{\mathbb{R}} \lvert \hat{X}(f) \rvert^2\,df}.
$$

By Parseval's theorem,
$$
\rho_{\mathcal{A}}(x,\tau) = \frac{\lVert x_{W(\tau)} \rVert_2^2}{\lVert x \rVert_2^2} \in [0,1],
$$
so $\rho_{\mathcal{A}}$ is the fraction of total signal energy preserved by the spectral projection into the compact-window amenable class at timescale $\tau$. The complementary fraction,
$$
1 - \rho_{\mathcal{A}}(x,\tau),
$$
is the energy that must be discarded, or physically damped, to enforce amenability at that timescale.

**Basic properties.**

(a) $\rho_{\mathcal{A}}(x,\tau)$ is monotone decreasing in $\tau$: demanding longer dwell times forces the projection to discard more high-frequency energy.

(b) For a pure tone $x(t) = \sin(\omega_0 t)$,
$$
\rho_{\mathcal{A}}(x,\tau) = 1
$$
whenever $\tau < \pi / \omega_0$, since all of the energy is concentrated at the two frequencies $\pm \omega_0/(2\pi)$.

(c) For a Brownian-like finite-window surrogate with broad spectral mass and an effective $1/f^2$ tail, one expects
$$
\rho_{\mathcal{A}}(x,\tau) \to 0 \quad \text{as} \quad \tau \to \infty,
$$
not as $\tau \to 0$. Long required dwell times force almost all of the energy in the high-frequency tail to be discarded. This matches the geometry paper's claim that generic Brownian paths are non-amenable, while also respecting the present note's narrower $L^2$ setup: actual Brownian paths are not themselves elements of $L^2(\mathbb{R})$.

This heuristic is the analytic companion to [fig4_script.py](../arxiv_paper_draft/fig4_script.py), which plots the same monotone comparison for pure-tone, narrowband, Brownian-like, and white-noise signal classes.

**Remark.** As written, part (iii) proves compact-window amenability. A uniform global lower bound on dwell time would require an additional hypothesis guaranteeing uniform separation of real zeros.
