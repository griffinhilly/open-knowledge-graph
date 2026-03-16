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
tags:
- likelihood-ratio-tests
- hypothesis-testing
- statistics
stage: advanced
status: draft
---

# Likelihood Ratio Tests

## Core Idea
The likelihood ratio test rejects H₀ when Λ = L(θ̂₀|X)/L(θ̂|X) < c, where θ̂₀ is the MLE under H₀ and θ̂ is the unrestricted MLE. Under H₀, -2log(Λ) converges in distribution to χ²_r where r is the dimension reduction. LR tests are general and achieve optimal Type II error (power) asymptotically.
