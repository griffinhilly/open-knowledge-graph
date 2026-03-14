---
id: central-limit-theorem-rigorous
title: Central Limit Theorem (Rigorous via Characteristic Functions)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: characteristic-functions
  type: hard
- id: convergence-in-distribution
  type: hard
- id: multivariate-normal-distribution
  type: soft
builds-toward:
- maximum-likelihood-estimation-theory
- confidence-intervals-rigorous-theory
- asymptotic-normality-mle
tags:
- central-limit-theorem
- limit-theorems
- probability
stage: abstract-reasoning
status: draft
---

# Central Limit Theorem (Rigorous via Characteristic Functions)

## Core Idea
If {Xₙ} are i.i.d. with mean μ and variance σ², then (Sₙ - nμ)/(σ√n) converges in distribution to N(0,1). The rigorous proof uses characteristic functions: φₙ(t/√n) → e^{-t²/2} for all t. The CLT explains why the normal distribution is ubiquitous—sums of many independent random variables are approximately normal regardless of the original distribution.

## How It's Best Learned
Prove the CLT using characteristic functions. Apply the CLT to non-normal parent distributions to verify the approximation. Use the CLT to justify normal approximations in statistical inference.

## Common Misconceptions
- Thinking the CLT applies without finite variance; finite variance is required. - Assuming convergence means they are equal for all n; it is only in the limit. - Forgetting that convergence is in distribution, not almost sure.
