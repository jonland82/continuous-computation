# When Continuous Physical Processes Can Compute

**[→ Homepage](https://jonland82.github.io/continuous-computation/)**

This repo is about a simple question: when does a continuous physical process count as a real computation rather than just a changing signal? The answer developed here is that computation appears only when coarse-grained states are readable, stable, and predictive, and those properties are usually thermodynamic achievements rather than free gifts of description. The four HTML pages present that argument as an overview plus three connected papers spanning framework, worked examples, and geometry.

This repository is a small static HTML project about when a continuous physical process can genuinely support a finite symbolic computation.

It currently contains four files:

- [index.html](index.html) - landing page that introduces the three-paper arc and summarizes the central results.
- [dissipation-and-the-emergence-of-computation.html](dissipation-and-the-emergence-of-computation.html) - the main framework paper.
- [when-continuous-trajectories-can-and-cannot-compute.html](when-continuous-trajectories-can-and-cannot-compute.html) - the worked examples paper.
- [the-geometry-of-computable-trajectories.html](the-geometry-of-computable-trajectories.html) - the geometry/structure paper.

There is no build step. Open [index.html](index.html) in a browser to navigate the set.

## Project Intuition

The central claim of the repo is that computation is not fundamental just because a system can be described continuously in time. A continuous process only counts as a usable computation when an observer can extract a stable alphabet from it, and when that alphabet has predictive closure of its own.

In practical terms, a coarse-graining has to do three things:

1. Make the current symbolic state readable.
2. Make that state persist long enough to be used.
3. Make the next symbolic state depend mainly on the current symbol, not on unresolved micro-detail inside the symbol's cell.

The papers then push that idea in three directions:

- physics: what thermodynamic cost buys those properties,
- examples: why some trajectories can never be repaired into computations,
- geometry: what the set of computation-amenable trajectories looks like inside function space.

## Files

### [index.html](index.html)

This is the front page for the project. It gives a high-level overview of the three papers, frames the overall problem, and presents six headline theorems in compact card form.

Use this page when you want the shortest entry point into the repo.

### [dissipation-and-the-emergence-of-computation.html](dissipation-and-the-emergence-of-computation.html)

This is the conceptual core of the project. It asks when a continuous physical process supports an emergent finite-state machine, and what energetic cost is required to keep that machine reliable.

Content:

- defines the three operative conditions: decodability, stability, and approximate lumpability,
- derives a Markov approximation result for the induced symbolic dynamics,
- introduces the computation epoch $T_{\mathrm{comp}}$,
- argues that lumpability is not free structure but a thermodynamic achievement,
- derives dissipation-based bounds on symbolic reliability,
- includes observer costs through a co-dissipation bound.

Intuition:

- A symbolic state is only real if an observer can read it.
- A readable state is only useful if it persists.
- A persistent state is only computational if it predicts its own successor at the symbolic level.
- Dissipation is what suppresses micro-level ambiguity strongly enough for the symbolic description to become causally meaningful.

Some of the mathematics:

- decodability is expressed schematically as $H(A_n \mid R_n) \le \varepsilon$,
- stability as $\Pr(A_{n+1} \neq A_n) \le \eta$,
- lumpability error $\lambda$ measures how much the next-step law changes within a coarse-grained cell,
- the Markov approximation bound is of the form

$$
\|\mathcal{L}(A_0,\ldots,A_N) - \mathcal{L}(M_0,\ldots,M_N)\|_{\mathrm{TV}}
\;\lesssim\;
N\bigl(\lambda + p_\varepsilon + \eta\bigr),
$$

- the dissipation-lumpability relation is of the form

$$
\lambda(P,\Pi)
\approx
\lambda_{\mathrm{eq}}(\Pi) - c(\Pi)\sqrt{\sigma(P)},
$$

- positive causal computation gain requires nonzero entropy production.

### [when-continuous-trajectories-can-and-cannot-compute.html](when-continuous-trajectories-can-and-cannot-compute.html)

This paper is the shortest and most concrete. It compares two trajectories with the same range and the same binary coarse-graining:

- $x(t) = \sin(t)$,
- $x(t) = \sin(1/t)$.

Content:

- shows how the three conditions behave in a minimal worked example,
- demonstrates that $\sin(1/t)$ fails because zero crossings accumulate without bound near the origin,
- shows that $\sin(t)$ satisfies the conditions for suitable sampling scale $\Delta$,
- uses the contrast to argue that amenability is a dwell-time property, not a smoothness property.

Intuition:

- $\sin(t)$ has evenly spaced zero crossings, so symbolic labels have time to persist.
- $\sin(1/t)$ crosses too rapidly near $t = 0$, so no observer can choose a sampling rate that makes the symbolic alphabet simultaneously stable and predictive there.
- If the trajectory does not provide dwell time, dissipation cannot manufacture it.

Some of the mathematics:

- the coarse-graining is

$$
\Pi(x) =
\begin{cases}
R, & x \ge 0, \\
L, & x < 0,
\end{cases}
$$

- stability is controlled by the spacing between sign changes,
- lumpability fails when microstates inside the same symbolic cell have very different next-symbol behavior,
- the comparison makes the failure mechanism geometric rather than merely analytic.

### [the-geometry-of-computable-trajectories.html](the-geometry-of-computable-trajectories.html)

This paper lifts the previous results to the level of function space. It studies the set $\mathcal{A}$ of trajectories that admit a computation-supporting coarse-graining, and its complement $\mathcal{N}$.

Content:

- defines the amenable set $\mathcal{A}$ and non-amenable set $\mathcal{N}$,
- studies structural properties of $\mathcal{A}$ such as non-convexity and lack of closure,
- interprets minimum dwell time as a geometric depth coordinate,
- shows that $\mathcal{A}$ has measure zero under Wiener measure,
- connects amenability to a spectral-gap characterization.

Intuition:

- Computation-supporting trajectories are not generic; they are special, structured, and thermodynamically maintained.
- The boundary of computation is the boundary where metastability disappears.
- Dissipation can be read geometrically as motion from generic noisy trajectories toward the interior of the amenable region.

Some of the mathematics:

- $\mathcal{A}$ consists of trajectories for which some $(\Pi,\Delta)$ satisfies the three symbolic conditions,
- the minimum dwell time $\tau_{\min}$ stratifies the interior of $\mathcal{A}$,
- under Wiener measure,

$$
\mu_W(\mathcal{A}) = 0,
$$

- the boundary of $\mathcal{A}$ is tied to closure of a transfer-operator spectral gap.

## Core Mathematical Thread

Across the three papers, the same backbone repeats:

1. Start with a continuous process and a coarse-graining $\Pi$.
2. Ask whether the induced symbols are decodable, stable, and lumpable.
3. If they are, the symbolic dynamics is close to a finite-state Markov process for a finite epoch.
4. The size of that epoch depends on how much dissipation suppresses micro-level ambiguity.
5. Computation-amenable trajectories form a thin, non-generic subset of all continuous trajectories.

## Selected References

- Claude E. Shannon (1948), <em>A Mathematical Theory of Communication</em>, <em>Bell System Technical Journal</em> 27(3), 379-423; 27(4), 623-656. Foundational source for entropy, mutual information, and coding.
- John G. Kemeny and J. Laurie Snell (1960), <em>Finite Markov Chains</em>. Classical reference for aggregation and finite-state reductions.
- Peter Buchholz (1994), <em>Exact and ordinary lumpability in finite Markov chains</em>, <em>Journal of Applied Probability</em> 31(1), 59-75. Canonical structural reference for lumpability.
- Rolf Landauer (1961), <em>Irreversibility and Heat Generation in the Computing Process</em>, <em>IBM Journal of Research and Development</em> 5, 183-191. Foundational thermodynamic limit for computation.
- Charles H. Bennett (1982), <em>The Thermodynamics of Computation: A Review</em>, <em>International Journal of Theoretical Physics</em> 21, 905-940. Classic review of reversible computation and Landauer's principle.
- Mark I. Freidlin and Alexander D. Wentzell, <em>Random Perturbations of Dynamical Systems</em>. Standard reference on metastability, escape, and dwell-time structure in noisy systems.
- Erik P. Hoel, Larissa Albantakis, and Giulio Tononi (2013), <em>Quantifying causal emergence shows that macro can beat micro</em>, <em>PNAS</em> 110(49), 19790-19795. Background for causal emergence and effective information.
- Peter Deuflhard and Marcus Weber (2005), <em>Robust Perron cluster analysis in conformation dynamics</em>, <em>Linear Algebra and its Applications</em> 398, 161-184. Spectral and transfer-operator perspective on metastable coarse-grainings.
- Christof Schuette and Marco Sarich (2013), <em>Metastability and Markov State Models in Molecular Dynamics</em>. Modern reference on spectral gaps, transfer operators, and metastable decompositions.
- Peter Morters and Yuval Peres (2010), <em>Brownian Motion</em>. Standard reference for Wiener measure and Brownian path geometry.

## Purpose

The repo reframes "physical computation" as a precise question in non-equilibrium statistical mechanics instead of treating computation as automatically present whenever one can impose labels on a system.

That is the unifying idea behind all four HTML files: symbolic computation is an emergent, thermodynamically sustained regime, not a default property of continuous dynamics.

