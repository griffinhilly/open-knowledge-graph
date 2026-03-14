---
id: likelihood-ratio-tests
title: Likelihood Ratio Tests
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: neyman-pearson-lemma
  type: hard
- id: convergence-in-distribution
  type: soft
builds-toward:
- uniformly-most-powerful-tests
- confidence-intervals-rigorous
tags:
- hypothesis-testing
- likelihood-ratio
- wilks-theorem
stage: abstract-reasoning
status: draft
---

# Likelihood Ratio Tests

## Core Idea
The likelihood ratio statistic is Λ = L(θ̂_H0)/L(θ̂). Under H_0, -2 log Λ converges in distribution to χ²_{df} by Wilks' theorem (df = dim(Θ) - dim(Θ_0)). LRTs are asymptotically optimal and invariant to reparameterization, unifying many standard tests.
