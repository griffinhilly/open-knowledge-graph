---
id: central-limit-theorem
title: Central Limit Theorem
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
- id: normal-distribution
  type: hard
builds-toward:
- confidence-intervals-means
- hypothesis-testing-fundamentals
tags:
- central-limit-theorem
- clt
- approximate-normality
stage: formal-systems
status: draft
---

# Central Limit Theorem

## Core Idea
The Central Limit Theorem states that for samples of size n drawn from any distribution with mean μ and standard deviation σ, the sample mean x̄ is approximately normally distributed with mean μ and standard deviation σ/√n, regardless of the population's shape—provided n is sufficiently large. This remarkable result justifies using normal-based inference methods for non-normal populations and explains why the normal distribution is so prevalent in statistics.

## How It's Best Learned
Simulate sampling from non-normal populations (uniform, exponential, bimodal). Observe that sample means become more normal as n increases. Verify the standard error formula σ/√n.

## Common Misconceptions
Thinking CLT applies to individual observations (it applies to sample means/sums). Assuming small samples have normal sampling distributions. Forgetting that the population doesn't need to be normal—only sample means do.
