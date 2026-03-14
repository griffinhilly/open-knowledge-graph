---
id: sampling-distributions
title: Sampling Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-methods
  type: hard
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: soft
builds-toward:
- central-limit-theorem
- confidence-intervals-means
tags:
- sampling-distribution
- sample-mean
- standard-error
- variability
stage: formal-systems
status: validated
---

# Sampling Distributions

## Core Idea
A sampling distribution is the probability distribution of a statistic (like the sample mean x̄) over all possible samples of a given size n from a population. If the population has mean μ and standard deviation σ, then the sampling distribution of x̄ has mean μ (unbiased) and standard deviation σ/√n (the standard error). The standard error shrinks as n increases, meaning larger samples produce more precise estimates of μ.

## How It's Best Learned
Run repeated sampling simulations: draw 100 random samples of size n from a known population, compute x̄ for each, and plot the distribution of x̄ values. This concretely shows that statistics are themselves random variables with their own distributions.

## Common Misconceptions
- Confusing the population standard deviation σ with the standard error σ/√n.
- Thinking the sampling distribution describes the distribution of individual data values.
- Not recognizing that increasing sample size reduces standard error but does not change the population distribution.
