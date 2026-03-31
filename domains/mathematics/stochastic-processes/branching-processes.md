---
id: branching-processes
title: Branching Processes
domain: mathematics
course: stochastic-processes
prerequisites:
- id: martingales-introduction
  type: hard
- id: moment-generating-functions
  type: hard
- id: conditional-expectation
  type: hard
- id: poisson-processes
  type: soft
tags:
- branching-processes
- galton-watson
- extinction-probability
- criticality
- population-dynamics
stage: expert
status: validated
---

# Branching Processes

## Core Idea
A Galton-Watson branching process models population dynamics: each individual in generation n independently produces a random number of offspring according to a fixed distribution {p_k}, forming generation n+1. The process is classified by the mean offspring number μ = E[X]: subcritical (μ < 1), critical (μ = 1), or supercritical (μ > 1). The extinction probability q — the probability the population eventually dies out — satisfies q = G(q) where G is the probability generating function of the offspring distribution. Extinction is certain (q = 1) if and only if μ ≤ 1; when μ > 1, the population survives with positive probability 1 - q, and the normalized process W_n = Z_n/μ^n is a non-negative martingale whose convergence determines the growth rate.

## Questions

```yaml
- question: "In a Galton-Watson process with offspring distribution P(X=0) = 1/4, P(X=1) = 1/2, P(X=2) = 1/4, the mean offspring number μ is 1. The extinction probability is:"
  type: multiple-choice
  options:
    - "0 — the population survives forever with probability 1"
    - "1 — extinction is certain, since μ = 1 (critical case)"
    - "1/2 — the process is a fair coin flip between survival and extinction"
    - "3/4 — determined by P(X=0) + P(X=1)"
  answer: 1
  explanation: "When μ = 1 (critical case), the extinction probability is 1, regardless of the offspring distribution (assuming the distribution is not degenerate at 1). The process is a non-negative martingale with mean 1 in every generation, but it is absorbed at 0. The expected population stays constant, but the variance accumulates: Var(Z_n) = nσ² grows without bound. The process drifts to extinction through random fluctuations — the expected value is maintained only because increasingly rare large populations compensate for the increasingly likely extinction."

- question: "The extinction probability q of a supercritical Galton-Watson process (μ > 1) is the smallest non-negative fixed point of the probability generating function G(s) = E[s^X]."
  type: true-false
  answer: true
  explanation: "The extinction probability satisfies q = P(Z_n → 0) = G(q), derived by conditioning on the first generation: q = Σ_k p_k · q^k = G(q). The PGF G is convex on [0,1] with G(1) = 1. When μ = G'(1) > 1, the convexity ensures G has a second fixed point q* < 1 in addition to s = 1. The extinction probability is this smaller fixed point. Geometrically, G(s) dips below the diagonal near s = q* and returns to it at s = 1. When μ ≤ 1, the only fixed point in [0,1] is s = 1, giving certain extinction."

- question: "The normalized population W_n = Z_n/μ^n in a supercritical Galton-Watson process is a martingale. Under what condition on the offspring distribution does W_n converge to a non-degenerate (not identically zero) limit?"
  type: short-answer
  answer: "W_n converges a.s. to a limit W by the martingale convergence theorem (since W_n ≥ 0 and E[W_n] = 1). The limit W is non-degenerate (P(W > 0) = 1 - q > 0 on the survival event) if and only if E[X log X] < ∞, the Kesten-Stigum condition (also called the X log X condition). When E[X log X] = ∞, the martingale converges to 0 a.s. even on the survival event — the population grows at rate μ^n but with such extreme variability that the normalized version degenerates."
  explanation: "The Kesten-Stigum theorem (1966) is the sharpest result on this question. The condition E[X log X] < ∞ controls the fluctuations: it ensures W_n is uniformly integrable, so L¹ convergence holds and E[W] = 1. When it fails, the offspring distribution has such a heavy right tail that rare individuals with enormous numbers of children dominate the population, and the ratio Z_n/μ^n cannot stabilize. This connects directly to the theory of martingale convergence — non-negative L¹-bounded martingales always converge a.s., but L¹ convergence (non-degeneracy) requires uniform integrability."

- question: "In a Galton-Watson process with Poisson(λ) offspring distribution, the PGF is G(s) = e^{λ(s-1)}. For λ = 2, the extinction probability q satisfies q = e^{2(q-1)}. This equation has a solution q ≈ 0.203, meaning:"
  type: multiple-choice
  options:
    - "About 20.3% of individuals in each generation will die"
    - "The population goes extinct with probability ≈ 0.203, and survives forever with probability ≈ 0.797"
    - "The population reaches 0 within 0.203 × n generations on average"
    - "Each individual has a 20.3% chance of producing no offspring"
  answer: 1
  explanation: "The extinction probability q ≈ 0.203 means that starting from a single individual, the entire population line eventually dies out with probability about 20.3%. With probability about 79.7%, the population grows exponentially (roughly as 2^n since μ = 2). Note P(X=0) = e^{-2} ≈ 0.135, which is smaller than q — extinction can occur even when the founder produces offspring, because all descendant lines must also eventually die. The extinction probability is the fixed point of G, not the zero-offspring probability."

- question: "A critical (μ = 1) Galton-Watson process with σ² = Var(X) ∈ (0,∞) satisfies P(Z_n > 0) ~ 2/(nσ²) as n → ∞. Interpret this result."
  type: short-answer
  answer: "The survival probability decays as 1/n, meaning extinction is certain but slow — it takes on the order of n generations for the process to die with high probability. Conditioned on survival to generation n, the population size Z_n is of order n (specifically, Z_n/n converges in distribution to an Exponential(2/σ²) random variable, the Yaglom limit). So the critical process shows a tension: it is doomed to extinction, but the rare surviving populations are large (order n), which keeps the unconditional expectation E[Z_n] = 1 despite the vanishing survival probability."
  explanation: "This asymptotic result, due to Kolmogorov (1938) and Yaglom (1947), reveals the delicate behavior at criticality. The product P(Z_n > 0) · E[Z_n | Z_n > 0] ≈ (2/nσ²) · (nσ²/2) = 1, consistent with E[Z_n] = 1 for all n. The critical case is a phase boundary between subcritical (exponential extinction) and supercritical (positive survival probability), and this 1/n decay rate characterizes the phase transition."
```

## Explainer

**Branching processes** are the fundamental stochastic model for population dynamics with random reproduction. The Galton-Watson process — introduced by Francis Galton and Henry Watson in 1874 to study the extinction of Victorian family surnames — begins with a single ancestor (Z_0 = 1) and evolves by each individual independently producing a random number of offspring drawn from a fixed distribution {p_k}_{k≥0}. The population in generation n+1 is Z_{n+1} = Σ_{i=1}^{Z_n} X_i^{(n)}, where the X_i^{(n)} are i.i.d. copies of the offspring variable X. The process is Markov with state space {0, 1, 2, ...}, and 0 is an absorbing state — once the population dies, it stays dead.

The **criticality classification** by the mean offspring number μ = E[X] governs the qualitative behavior. When μ < 1 (subcritical), E[Z_n] = μ^n → 0 exponentially, and extinction is certain with geometrically decaying survival probability. When μ = 1 (critical), E[Z_n] = 1 for all n, but extinction is still certain (assuming Var(X) > 0) — survival probability decays as 2/(nσ²). When μ > 1 (supercritical), the population grows exponentially on the survival event, with E[Z_n] = μ^n. The extinction probability q is the smallest fixed point of the probability generating function G(s) = E[s^X] = Σ_k p_k s^k: the equation q = G(q) follows from conditioning on the first-generation size and using the independence of descendant subtrees.

The **martingale connection** is central. The normalized population W_n = Z_n/μ^n is a non-negative martingale: E[W_{n+1} | ℱ_n] = Z_n · μ / μ^{n+1} = W_n. By the martingale convergence theorem, W_n → W a.s. for some non-negative random variable W. The question is whether W is degenerate (W = 0 a.s.) or has a genuine positive part. In the subcritical and critical cases, W = 0 a.s. In the supercritical case, {W = 0} = {extinction}, so P(W > 0) = 1 - q. But even in the supercritical case, the limit can degenerate if the offspring distribution has too heavy a tail. The **Kesten-Stigum theorem** provides the sharp criterion: W is non-degenerate (equivalently, W_n converges in L¹) if and only if E[X log X] < ∞. This X log X condition is the branching-process analogue of the uniform integrability condition in general martingale convergence theory.

**Extensions** of the basic Galton-Watson model are numerous and important. Multi-type branching processes allow several types of individuals with type-dependent reproduction, governed by a mean matrix M whose largest eigenvalue determines criticality. Continuous-time branching processes (Bellman-Harris processes) replace discrete generations with random lifetimes, connecting to renewal theory and age-dependent models. Branching processes in random environments (BPRE) let the offspring distribution vary randomly between generations, modeling fluctuating environmental conditions. In the continuous limit, the population process converges to a continuous-state branching process (CSBP), which is a Lévy process with a specific branching structure — these connect to superprocesses and measure-valued diffusions in modern probability theory. Branching processes also appear in applications far beyond biology: nuclear chain reactions (the original motivation for the Bellman-Harris model), epidemic spreading, the cascade structure of Galton-Watson trees in combinatorics, and the analysis of recursive algorithms in computer science.
