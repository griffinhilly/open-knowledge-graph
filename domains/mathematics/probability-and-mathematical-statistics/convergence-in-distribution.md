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
stage: advanced
status: draft
---

# Convergence in Distribution

## Core Idea
Xₙ converges to X in distribution if lim_{n→∞} Fₙ(x) = F(x) at continuity points of F, or equivalently lim_{n→∞} φₙ(t) = φ(t) for all t. This is the weakest form of convergence—Xₙ and X need not be defined on the same probability space. Characteristic function convergence provides the most convenient criterion.

## Questions

```yaml
- question: "Suppose Xₙ converges in distribution to X, where X ~ N(0,1). Which of the following can we conclude?"
  type: multiple-choice
  options:
    - "For large n, P(|Xₙ − X| > 0.01) is small — the values of Xₙ are close to the values of X"
    - "Xₙ and X must be defined on the same probability space for the limit to make sense"
    - "The CDF of Xₙ approaches the standard normal CDF at all continuity points, but Xₙ and X may not be close as numbers"
    - "Xₙ converges in probability to X, since distributional convergence implies probabilistic closeness"
  answer: 2
  explanation: "Convergence in distribution only requires that the CDFs Fₙ(x) → F(x) at continuity points. It says nothing about how close Xₙ and X are as random variable values. Xₙ and X need not even be defined on the same probability space — only their marginal distributions matter. Option A describes convergence in probability, which is strictly stronger and does not follow from distributional convergence. Option D is backwards: convergence in probability implies convergence in distribution, not the reverse. The classic illustration is that if Xₙ ~ N(0,1) for all n, and X ~ N(0,1) independently, then Xₙ →d X, but |Xₙ − X| is not small."

- question: "A statistics student claims: 'By the Central Limit Theorem, for large n, the sample mean X̄ₙ is approximately normally distributed.' What is the precise flaw in this statement?"
  type: multiple-choice
  options:
    - "There is no flaw — the CLT says the sample mean is approximately normal for large n"
    - "The sample mean converges in probability to μ, not to a normal distribution"
    - "The CLT applies to the standardized sum √n(X̄ₙ − μ)/σ, not to X̄ₙ itself, which converges to the constant μ"
    - "The CLT only applies when the population distribution is already normal"
  answer: 2
  explanation: "The CLT says that √n(X̄ₙ − μ)/σ converges in distribution to N(0,1) — the properly centered and scaled version of the sample mean. X̄ₙ itself converges in probability to the constant μ (by the law of large numbers), so its distribution collapses to a point mass, not a normal curve. The student's phrasing is common shorthand and is technically imprecise: what is approximately normal is the standardized sample mean, not X̄ₙ itself. Convergence in distribution is the exactly right tool here — it describes how the shape of the fluctuations, once scaled to be of order 1, approaches the standard normal."

- question: "If Xₙ and X need not be defined on the same probability space, then convergence in distribution is a weaker notion than convergence in probability."
  type: true-false
  answer: true
  explanation: "True. Convergence in probability requires both P(|Xₙ − X| > ε) → 0 for all ε > 0, which presupposes Xₙ and X are defined on a common probability space so that Xₙ − X is a well-defined random variable. Convergence in distribution requires only that the CDFs converge pointwise (at continuity points), a purely marginal condition that makes no reference to joint behavior. Because convergence in probability implies convergence in distribution but not conversely, distributional convergence is strictly weaker: a sequence can converge in distribution to X without the actual values of Xₙ being close to X at all."

- question: "If Xₙ converges in distribution to X, then Xₙ must also converge in distribution to any random variable Y that has the same distribution as X."
  type: true-false
  answer: true
  explanation: "True, and this highlights the distributional nature of this convergence mode. Convergence in distribution is entirely about the limiting CDF, not about which specific random variable X is. If Y has the same distribution as X (i.e., F_Y = F_X), then Fₙ(x) → F_X(x) = F_Y(x) at all continuity points, so Xₙ →d Y as well. This is consistent with the fact that Xₙ and X need not be on the same probability space — 'X' in 'Xₙ →d X' is just a convenient name for the limiting distribution, not a specific random variable with a specific sample path."

- question: "The definition of convergence in distribution requires CDF convergence only at continuity points of the limiting distribution F, not at all points. Explain why the continuity-point caveat is necessary."
  type: short-answer
  answer: "CDFs can have jump discontinuities at points where the limiting distribution places positive probability mass. At a jump point x₀, F(x₀⁻) < F(x₀), and a sequence of CDFs Fₙ could converge to either boundary value as n → ∞, depending on the sequence. If we required Fₙ(x₀) → F(x₀) at jump points, we could inadvertently exclude sequences whose distributions are genuinely approaching the limiting distribution but whose CDFs happen to converge to the left-hand limit at the jump. At continuity points, no such ambiguity exists: F is continuous there, so F(x⁻) = F(x), and the convergence condition is unambiguous."
  explanation: "The characteristic function criterion (φₙ(t) → φ(t) for all t) avoids this issue entirely because characteristic functions are always continuous — there are no jump discontinuities to worry about. This is one practical reason the characteristic function approach is preferred in theoretical work."
```

## Explainer

From your study of distribution functions and densities, you know that a distribution function F(x) = P(X ≤ x) completely characterizes a random variable's probabilistic behavior. **Convergence in distribution** (also written Xₙ →_d X or Xₙ ⟹ X) says that the sequence of distributions, as described by their CDFs Fₙ, approaches the distribution F — not that the random variables themselves get close. This distinction is crucial and is what makes convergence in distribution the weakest of the three main modes.

To understand why "weakest" is meaningful, consider what stronger convergence demands. **Almost sure convergence** says that the actual sample paths Xₙ(ω) converge to X(ω) for nearly every outcome ω — the random variables must be defined on the same probability space and their values must track each other. **Convergence in probability** says that P(|Xₙ − X| > ε) → 0, again requiring both to live on the same space and their values to be close with high probability. Convergence in distribution only requires that probabilities of events like {X ≤ x} converge — it says nothing about whether Xₙ and X are close as numbers in any specific sample. In fact, Xₙ and X don't even need to be defined on the same probability space, since only their marginal distributions matter.

The CDF definition has a subtle caveat: convergence is required only at **continuity points of F**. This is necessary because CDFs can have jump discontinuities, and at a jump, a sequence of CDFs could converge to either boundary value. At continuity points, this ambiguity disappears. The **characteristic function criterion** — that convergence in distribution is equivalent to pointwise convergence of characteristic functions φₙ(t) = E[e^{itXₙ}] — is often more tractable in proofs. Characteristic functions are always continuous and bounded, so no caveat about continuity points is needed, and Fourier-analytic tools become available.

The Central Limit Theorem, which you'll encounter next, is the canonical example of convergence in distribution: for i.i.d. random variables with finite mean and variance, the standardized sums √n(X̄ₙ − μ)/σ converge in distribution to a standard normal N(0,1). Notice that this doesn't say the sample means literally converge to a normal — they converge in probability to μ by the law of large numbers. Rather, the *shape of their fluctuations*, properly scaled, approaches the normal distribution. Convergence in distribution is precisely the right tool for describing this kind of limiting shape, which is why it sits at the heart of classical probability theory.
