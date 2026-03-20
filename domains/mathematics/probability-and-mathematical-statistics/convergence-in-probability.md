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
status: draft
---

# Convergence in Probability

## Core Idea
A sequence {Xₙ} converges to X in probability if for all ε > 0, lim_{n→∞} P(|Xₙ - X| > ε) = 0. Intuitively, Xₙ is close to X with high probability for large n. Convergence in probability is weaker than almost sure convergence but stronger than convergence in distribution.

## Explainer

In deterministic analysis, a sequence of numbers xₙ converges to L if xₙ gets arbitrarily close to L for large enough n — every number in the tail of the sequence eventually lands near L. For random variables, the situation is richer: Xₙ is not a single number but a whole distribution. What does it mean for a random variable to "converge"? There are several answers depending on what you require. **Convergence in probability** is the most commonly encountered notion, and it has a natural intuitive reading.

The formal definition says: Xₙ converges to X in probability if, for every tolerance ε > 0, the probability that Xₙ is more than ε away from X goes to zero as n → ∞. In notation: P(|Xₙ − X| > ε) → 0 for all ε > 0. Concretely, pick any small margin — say, ε = 0.01. For large enough n, the chance that Xₙ differs from X by more than 0.01 becomes negligible. It's not that Xₙ is guaranteed to be close to X; it's that *most* of the probability mass of Xₙ is concentrated near X, and the exceptional events (large deviations) become rarer and rarer.

Think of a shrinking distribution as the key image. If Xₙ has a normal distribution with mean 0 and variance 1/n, then as n → ∞, the distribution collapses to a spike at 0. For any ε, the probability of landing outside (−ε, ε) is the tail probability of N(0, 1/n), which goes to 0. So Xₙ → 0 in probability. Notice that no individual outcome is guaranteed to be close to 0 — the randomness doesn't disappear, but the mass of the distribution concentrates. This is different from saying "Xₙ always stays near 0."

This distinction matters when comparing convergence modes. **Almost sure convergence** requires that the set of outcomes where Xₙ does *not* converge to X has probability zero — every path (except a null set) eventually stays near X. Convergence in probability is weaker: it only requires that the *probability* of straying far from X vanishes, not that every path behaves well. A classic counterexample (the "typewriter sequence") shows that convergence in probability does not imply almost sure convergence. Convergence in probability is the mode relevant to the **Weak Law of Large Numbers**: the sample mean converges in probability to the true mean, even though individual samples may occasionally be far off.
