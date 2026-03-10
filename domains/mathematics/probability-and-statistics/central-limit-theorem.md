---
id: central-limit-theorem
title: The Central Limit Theorem
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
- id: normal-distribution-intro
  type: hard
builds-toward:
- confidence-intervals-means
- z-test-for-means
tags:
- central-limit-theorem
- CLT
- normal-approximation
- sample-size
- convergence
stage: formal-systems
status: draft
---

# The Central Limit Theorem

## Core Idea
The Central Limit Theorem (CLT) states that for sufficiently large sample sizes, the sampling distribution of the sample mean x̄ is approximately normal, regardless of the shape of the underlying population distribution. Formally, x̄ ~ N(μ, σ²/n) approximately when n is large (a common rule of thumb is n ≥ 30 for symmetric populations, larger for skewed ones). The CLT is the theoretical justification for using normal-based inference methods on non-normal populations.

## How It's Best Learned
Demonstrate the CLT visually: start with a strongly skewed population (e.g., exponential), draw samples of increasing size n = 2, 5, 10, 30, 100, and show the distribution of x̄ becoming increasingly bell-shaped. This simulation is the most convincing proof available at this level.

## Common Misconceptions
- Thinking the CLT says the population becomes normal as n increases — it says the sampling distribution of x̄ does.
- Applying the n ≥ 30 rule as an absolute threshold rather than a rough guideline.
- Forgetting that the CLT applies to x̄, not to individual observations from the population.
