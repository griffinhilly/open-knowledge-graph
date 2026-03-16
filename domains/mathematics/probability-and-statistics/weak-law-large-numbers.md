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
status: draft
---

# Weak Law of Large Numbers

## Core Idea
The weak law of large numbers states that the sample mean converges in probability to the true mean: for any ε > 0, P(|X̄ₙ - μ| > ε) → 0 as n → ∞. This justifies using sample averages to estimate population means.

## Explainer

From your study of expected value, you know that E[X] = μ is the long-run average of a random variable — the center of mass of the distribution. But expected value is a theoretical quantity, computed from a probability model. In practice, you have data: a finite sample of observations X₁, X₂, …, Xₙ drawn from that distribution. The **sample mean** X̄ₙ = (X₁ + X₂ + … + Xₙ)/n is what you can actually compute. The weak law of large numbers is the theorem that says these two quantities — the theoretical mean and the sample mean — converge to each other as the sample grows.

The precise statement uses a concept called **convergence in probability**. It does not say that X̄ₙ will equal μ exactly after enough observations (that would be the strong law). It says that for any tolerance ε > 0, no matter how small, the probability that X̄ₙ differs from μ by more than ε shrinks to zero as n grows. In symbols: P(|X̄ₙ - μ| > ε) → 0 as n → ∞. Think of it this way — fix a margin of error, say ε = 0.01. The WLLN guarantees that with enough observations, you can make the chance of being outside that margin as small as you like.

The intuition behind why this works comes from variance. Each observation Xᵢ has variance σ². Since the Xᵢ are independent, the variance of X̄ₙ is σ²/n — it shrinks as n grows. By Chebyshev's inequality (which you can derive directly from the definition of expected value), P(|X̄ₙ - μ| > ε) ≤ σ²/(nε²). The right side goes to zero as n → ∞ for any fixed ε. Averaging reduces noise: random fluctuations in individual observations tend to cancel out, and the cancellations become more reliable with more data.

The difference between **weak** and **strong** convergence matters conceptually. Weak convergence (convergence in probability) says that for any fixed ε, the probability of being far from μ vanishes. Strong convergence (almost sure convergence, the strong law) says that the sample path of X̄ₙ actually settles at μ — the event {X̄ₙ → μ} happens with probability 1. The strong law is the more powerful statement, but the weak law is easier to prove and sufficient for most applications.

The practical significance of the WLLN is enormous: it is the foundational justification for statistics. Every time you estimate a population mean from a sample — computing an average test score, a polling result, a drug trial outcome — you are implicitly relying on the law of large numbers. The theorem tells you that larger samples are better, and gives a precise sense in which "better" means something: the sample mean concentrates around the true mean. The central limit theorem, your next destination, will sharpen this further by describing the shape of the distribution of X̄ₙ around μ.
