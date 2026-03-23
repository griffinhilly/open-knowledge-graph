---
id: convergence-in-probability
title: Convergence in Probability
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: limit-definition-intuitive
  type: soft
builds-toward:
- relationships-modes-convergence
- weak-law-of-large-numbers
tags:
- convergence
- probability
- limit-theorems
stage: advanced
status: validated
---

# Convergence in Probability

## Core Idea
A sequence {Xₙ} converges to X in probability if for all ε > 0, lim_{n→∞} P(|Xₙ - X| > ε) = 0. Intuitively, Xₙ is close to X with high probability for large n. Convergence in probability is weaker than almost sure convergence but stronger than convergence in distribution.

## Questions

```yaml
- question: "A sequence {Xₙ} converges to 0 in probability. Which of the following is necessarily true for large n?"
  type: multiple-choice
  options:
    - "Xₙ = 0 almost surely — the random variable eventually equals its limit"
    - "The variance of Xₙ approaches 0"
    - "For any ε > 0, P(|Xₙ| > ε) → 0 as n → ∞"
    - "Xₙ converges to 0 almost surely — every sample path eventually stays near 0"
  answer: 2
  explanation: "Option (c) is the literal definition of convergence in probability, so it is necessarily true. Option (a) is wrong — Xₙ can still take non-zero values; what matters is that the probability of large deviations vanishes, not that Xₙ equals zero. Option (d) would be almost sure convergence — a strictly stronger notion. Option (b) is not necessarily true: consider Xₙ = n with probability 1/n and 0 otherwise. This converges to 0 in probability (P(|Xₙ|>ε) = 1/n → 0), yet Var(Xₙ) = n·(1/n) = 1 (or can be made to diverge)."

- question: "Which scenario correctly describes how convergence in probability can fail to imply almost sure convergence?"
  type: multiple-choice
  options:
    - "Almost sure convergence requires a finite probability space; convergence in probability applies to any space"
    - "A sequence may converge in probability to X, yet individual sample paths may not converge to X — the 'typewriter sequence' is a canonical counterexample"
    - "Almost sure convergence requires the sequence to be monotone; convergence in probability has no such restriction"
    - "Convergence in probability is actually stronger than almost sure convergence, because it must hold for all ε simultaneously"
  answer: 1
  explanation: "The typewriter sequence is constructed on [0,1] with uniform probability: X₁ = 1_{[0,1]}, X₂ = 1_{[0,1/2]}, X₃ = 1_{[1/2,1]}, X₄ = 1_{[0,1/4]}, X₅ = 1_{[1/4,1/2]}, ... and so on, cycling through finer and finer intervals. The probability P(Xₙ = 1) → 0, so Xₙ → 0 in probability. But for every outcome ω ∈ [0,1], Xₙ(ω) = 1 infinitely often (the intervals eventually cover every point repeatedly), so Xₙ(ω) does not converge to 0 for any ω. Individual paths misbehave; only the probability of misbehavior vanishes."

- question: "If Xₙ converges to X in probability, then for sufficiently large n, every realization of Xₙ will fall within ε of X with probability 1."
  type: true-false
  answer: false
  explanation: "Convergence in probability means P(|Xₙ − X| > ε) → 0, not that it ever equals 0. The probability of a large deviation merely becomes arbitrarily small, not zero. Individual realizations can still land far from X; the claim is that such events become increasingly rare, not that they become impossible. Almost sure convergence requires a stronger statement: the set of sample paths that ever deviate from X by more than ε (eventually) has probability zero."

- question: "The Weak Law of Large Numbers establishes that the sample mean converges to the true mean in probability (not almost surely)."
  type: true-false
  answer: true
  explanation: "This is correct. The WLLN states that for iid random variables with finite mean μ, the sample mean X̄ₙ → μ in probability: P(|X̄ₙ − μ| > ε) → 0 for all ε > 0. The Strong Law of Large Numbers gives the stronger almost sure convergence result, requiring the same conditions plus finite variance (or just finite first moment under certain formulations). The distinction matters: WLLN says most samples will be close to the mean; SLLN says the sample mean path almost surely converges."

- question: "What is the key difference between convergence in probability and almost sure convergence, and why is the weaker notion still mathematically useful?"
  type: short-answer
  answer: "Almost sure convergence requires that for almost every individual sample path (every outcome except a set of probability zero), Xₙ(ω) → X(ω). The sequence behaves well path-by-path. Convergence in probability only requires that the probability of any given path deviating from X by more than ε goes to zero — but some paths may still be badly behaved. Convergence in probability is weaker: almost sure convergence implies it, but not vice versa. It remains useful because (1) many important theorems (WLLN, consistency of estimators) naturally produce it, (2) it is often easier to prove, and (3) for many statistical applications — estimators converging to true parameters — this weaker guarantee is sufficient to justify procedures."
  explanation: "The hierarchy of convergence modes matters in probability theory: almost sure → in probability → in distribution. Knowing which mode you have tells you what properties carry through limiting arguments and which do not. Convergence in probability suffices to pass continuous functions through limits (continuous mapping theorem), for example, which makes it highly practical for asymptotic statistics."
```

## Explainer

In deterministic analysis, a sequence of numbers xₙ converges to L if xₙ gets arbitrarily close to L for large enough n — every number in the tail of the sequence eventually lands near L. For random variables, the situation is richer: Xₙ is not a single number but a whole distribution. What does it mean for a random variable to "converge"? There are several answers depending on what you require. **Convergence in probability** is the most commonly encountered notion, and it has a natural intuitive reading.

The formal definition says: Xₙ converges to X in probability if, for every tolerance ε > 0, the probability that Xₙ is more than ε away from X goes to zero as n → ∞. In notation: P(|Xₙ − X| > ε) → 0 for all ε > 0. Concretely, pick any small margin — say, ε = 0.01. For large enough n, the chance that Xₙ differs from X by more than 0.01 becomes negligible. It's not that Xₙ is guaranteed to be close to X; it's that *most* of the probability mass of Xₙ is concentrated near X, and the exceptional events (large deviations) become rarer and rarer.

Think of a shrinking distribution as the key image. If Xₙ has a normal distribution with mean 0 and variance 1/n, then as n → ∞, the distribution collapses to a spike at 0. For any ε, the probability of landing outside (−ε, ε) is the tail probability of N(0, 1/n), which goes to 0. So Xₙ → 0 in probability. Notice that no individual outcome is guaranteed to be close to 0 — the randomness doesn't disappear, but the mass of the distribution concentrates. This is different from saying "Xₙ always stays near 0."

This distinction matters when comparing convergence modes. **Almost sure convergence** requires that the set of outcomes where Xₙ does *not* converge to X has probability zero — every path (except a null set) eventually stays near X. Convergence in probability is weaker: it only requires that the *probability* of straying far from X vanishes, not that every path behaves well. A classic counterexample (the "typewriter sequence") shows that convergence in probability does not imply almost sure convergence. Convergence in probability is the mode relevant to the **Weak Law of Large Numbers**: the sample mean converges in probability to the true mean, even though individual samples may occasionally be far off.
