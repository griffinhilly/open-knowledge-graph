---
id: weak-law-large-numbers
title: Weak Law of Large Numbers
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: soft
- id: expected-value
  type: hard
builds-toward:
- central-limit-theorem
- law-of-large-numbers
tags:
- convergence
- probability
- foundations
stage: formal-systems
status: validated
---

# Weak Law of Large Numbers

## Core Idea
The weak law of large numbers states that the sample mean converges in probability to the true mean: for any ε > 0, P(|X̄ₙ - μ| > ε) → 0 as n → ∞. This justifies using sample averages to estimate population means.

## Questions

```yaml
- question: "The weak law of large numbers guarantees that as n → ∞, the sample mean X̄ₙ will:"
  type: multiple-choice
  options:
    - "Eventually equal the population mean μ exactly, with certainty"
    - "Make the probability of differing from μ by any fixed positive amount shrink to zero"
    - "Converge to μ with probability 1 along every sample path"
    - "Equal μ for all n larger than some threshold determined by the variance"
  answer: 1
  explanation: "The WLLN says: for any ε > 0, P(|X̄ₙ − μ| > ε) → 0 as n → ∞. This is 'convergence in probability' — you can make the chance of being far from μ as small as you like by taking n large enough. It does NOT say X̄ₙ will equal μ exactly (that would require infinitely many observations), and it does NOT guarantee that every sample path converges to μ (that is the stronger claim of the strong law). Options A and D describe a certainty the weak law does not provide."

- question: "Why does averaging n independent observations reduce the error in estimating the population mean?"
  type: multiple-choice
  options:
    - "Averaging cancels all outliers by symmetry, so only typical values remain"
    - "The variance of the sample mean is σ²/n, which shrinks as n grows, concentrating the distribution around μ"
    - "The law of averages ensures extreme values become rarer in larger samples"
    - "Larger samples include a greater fraction of the population, making the sample more representative"
  answer: 1
  explanation: "The variance of X̄ₙ = (X₁ + ⋯ + Xₙ)/n is Var(X̄ₙ) = σ²/n, which follows from independence and the scaling of variance. As n increases, σ²/n → 0, meaning the distribution of X̄ₙ becomes increasingly concentrated around μ. By Chebyshev's inequality, P(|X̄ₙ − μ| > ε) ≤ σ²/(nε²) → 0. This is the precise mechanism: random fluctuations cancel out via variance reduction. Option A ('the law of averages') is a common misconception suggesting that extreme values are 'due' to be compensated — but past observations don't influence future ones."

- question: "The weak law of large numbers applies for any fixed margin of error ε > 0, no matter how small, as long as the sample size is large enough."
  type: true-false
  answer: true
  explanation: "This is the quantifier structure of the WLLN: for ANY ε > 0, P(|X̄ₙ − μ| > ε) → 0. There is no lower bound on ε — even ε = 0.000001 works. The catch is that the required n may be very large for tiny ε (since the bound σ²/(nε²) shows n must grow as ε shrinks). But the guarantee holds for every positive ε. This universality is what makes the WLLN the foundational justification for using sample averages."

- question: "The weak law of large numbers and the strong law of large numbers make the same guarantee — both say the sample mean converges to the population mean."
  type: true-false
  answer: false
  explanation: "The two laws describe different modes of convergence. The weak law (convergence in probability) says that for any fixed ε, the probability of being far from μ vanishes — but it says nothing about the long-run behavior of any single sample path. The strong law (almost sure convergence) says that the event {X̄ₙ → μ} has probability 1 — the sample path of X̄ₙ actually settles at μ with probability 1. The strong law is strictly more powerful. The weak law does not imply the strong law."

- question: "What does 'convergence in probability' mean for the weak law of large numbers, and how does it differ from saying 'the sample mean will eventually equal the population mean'?"
  type: short-answer
  answer: "Convergence in probability means: for any tolerance ε > 0, however small, the probability that X̄ₙ differs from μ by more than ε can be made arbitrarily small by taking n large enough. It is a statement about probabilities approaching zero, not about sample paths reaching an exact value. Saying the sample mean 'will eventually equal μ' would mean the outcome is certain after enough observations — which is false. Even with a million observations, there is still a small (but now tiny) probability of being far from μ. The WLLN says that probability can be made as small as desired, not that it ever reaches zero."
  explanation: "The distinction matters for how we use the WLLN in practice. It tells us that large samples give reliable estimates (the chance of a large error is small) without promising exact equality. This is the right foundation for statistics: confidence increases with sample size, but certainty is never achieved from finite samples."
```

## Explainer

From your study of expected value, you know that E[X] = μ is the long-run average of a random variable — the center of mass of the distribution. But expected value is a theoretical quantity, computed from a probability model. In practice, you have data: a finite sample of observations X₁, X₂, …, Xₙ drawn from that distribution. The **sample mean** X̄ₙ = (X₁ + X₂ + … + Xₙ)/n is what you can actually compute. The weak law of large numbers is the theorem that says these two quantities — the theoretical mean and the sample mean — converge to each other as the sample grows.

The precise statement uses a concept called **convergence in probability**. It does not say that X̄ₙ will equal μ exactly after enough observations (that would be the strong law). It says that for any tolerance ε > 0, no matter how small, the probability that X̄ₙ differs from μ by more than ε shrinks to zero as n grows. In symbols: P(|X̄ₙ - μ| > ε) → 0 as n → ∞. Think of it this way — fix a margin of error, say ε = 0.01. The WLLN guarantees that with enough observations, you can make the chance of being outside that margin as small as you like.

The intuition behind why this works comes from variance. Each observation Xᵢ has variance σ². Since the Xᵢ are independent, the variance of X̄ₙ is σ²/n — it shrinks as n grows. By Chebyshev's inequality (which you can derive directly from the definition of expected value), P(|X̄ₙ - μ| > ε) ≤ σ²/(nε²). The right side goes to zero as n → ∞ for any fixed ε. Averaging reduces noise: random fluctuations in individual observations tend to cancel out, and the cancellations become more reliable with more data.

The difference between **weak** and **strong** convergence matters conceptually. Weak convergence (convergence in probability) says that for any fixed ε, the probability of being far from μ vanishes. Strong convergence (almost sure convergence, the strong law) says that the sample path of X̄ₙ actually settles at μ — the event {X̄ₙ → μ} happens with probability 1. The strong law is the more powerful statement, but the weak law is easier to prove and sufficient for most applications.

The practical significance of the WLLN is enormous: it is the foundational justification for statistics. Every time you estimate a population mean from a sample — computing an average test score, a polling result, a drug trial outcome — you are implicitly relying on the law of large numbers. The theorem tells you that larger samples are better, and gives a precise sense in which "better" means something: the sample mean concentrates around the true mean. The central limit theorem, your next destination, will sharpen this further by describing the shape of the distribution of X̄ₙ around μ.
