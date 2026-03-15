---
id: maximum-likelihood-estimation-theory
title: Maximum Likelihood Estimation (Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: optimization-problems
  type: soft
builds-toward:
- consistency-of-estimators
- asymptotic-normality-mle
- likelihood-ratio-tests
tags:
- mle
- estimation
- statistics
stage: abstract-reasoning
status: draft
---

# Maximum Likelihood Estimation (Theory)

## Core Idea
The maximum likelihood estimator (MLE) θ̂ₙ maximizes the likelihood L(θ|X) = ∏ᵢ f(Xᵢ|θ). MLEs have desirable asymptotic properties: consistency, asymptotic normality, and efficiency (achieving the Cramer-Rao bound asymptotically). Under regularity conditions, θ̂ₙ solves ∂log L/∂θ = 0 and is unique.

## How It's Best Learned
Compute MLEs for standard families (normal, exponential, binomial). Verify regularity conditions. Apply the asymptotic normality result to construct confidence intervals.

## Common Misconceptions
- Thinking MLEs are always unbiased; MLEs can be biased for finite samples. - Assuming the MLE always has a closed form; many MLEs require numerical optimization. - Forgetting that asymptotic normality requires regularity conditions.
