---
id: convergence-in-distribution
title: Convergence in Distribution
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: characteristic-functions
  type: soft
builds-toward:
- relationships-modes-convergence
- central-limit-theorem-rigorous
tags:
- convergence
- distribution
- limit-theorems
stage: formal-systems
status: draft
---

# Convergence in Distribution

## Core Idea
Xₙ converges to X in distribution if lim_{n→∞} Fₙ(x) = F(x) at continuity points of F, or equivalently lim_{n→∞} φₙ(t) = φ(t) for all t. This is the weakest form of convergence—Xₙ and X need not be defined on the same probability space. Characteristic function convergence provides the most convenient criterion.

## Explainer

From your study of distribution functions and densities, you know that a distribution function F(x) = P(X ≤ x) completely characterizes a random variable's probabilistic behavior. **Convergence in distribution** (also written Xₙ →_d X or Xₙ ⟹ X) says that the sequence of distributions, as described by their CDFs Fₙ, approaches the distribution F — not that the random variables themselves get close. This distinction is crucial and is what makes convergence in distribution the weakest of the three main modes.

To understand why "weakest" is meaningful, consider what stronger convergence demands. **Almost sure convergence** says that the actual sample paths Xₙ(ω) converge to X(ω) for nearly every outcome ω — the random variables must be defined on the same probability space and their values must track each other. **Convergence in probability** says that P(|Xₙ − X| > ε) → 0, again requiring both to live on the same space and their values to be close with high probability. Convergence in distribution only requires that probabilities of events like {X ≤ x} converge — it says nothing about whether Xₙ and X are close as numbers in any specific sample. In fact, Xₙ and X don't even need to be defined on the same probability space, since only their marginal distributions matter.

The CDF definition has a subtle caveat: convergence is required only at **continuity points of F**. This is necessary because CDFs can have jump discontinuities, and at a jump, a sequence of CDFs could converge to either boundary value. At continuity points, this ambiguity disappears. The **characteristic function criterion** — that convergence in distribution is equivalent to pointwise convergence of characteristic functions φₙ(t) = E[e^{itXₙ}] — is often more tractable in proofs. Characteristic functions are always continuous and bounded, so no caveat about continuity points is needed, and Fourier-analytic tools become available.

The Central Limit Theorem, which you'll encounter next, is the canonical example of convergence in distribution: for i.i.d. random variables with finite mean and variance, the standardized sums √n(X̄ₙ − μ)/σ converge in distribution to a standard normal N(0,1). Notice that this doesn't say the sample means literally converge to a normal — they converge in probability to μ by the law of large numbers. Rather, the *shape of their fluctuations*, properly scaled, approaches the normal distribution. Convergence in distribution is precisely the right tool for describing this kind of limiting shape, which is why it sits at the heart of classical probability theory.
