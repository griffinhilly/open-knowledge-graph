---
id: sampling-distributions
title: Sampling Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: sample-spaces-and-events
  type: soft
builds-toward:
- central-limit-theorem
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- sampling-distribution
- sample-mean
- sample-proportion
stage: formal-systems
status: draft
---

# Sampling Distributions

## Core Idea
A sampling distribution is the probability distribution of a statistic (like sample mean or sample proportion) computed from all possible samples of a given size from a population. The sampling distribution of the sample mean x̄ has mean μ and standard deviation σ/√n (the standard error). Sampling distributions form the foundation of statistical inference by describing how statistics vary from sample to sample and enabling us to quantify uncertainty in estimators.

## How It's Best Learned
Simulate drawing many samples and computing statistics for each. Observe that the sampling distribution of means is less spread out than the population. Verify theoretical standard errors match simulation results.

## Common Misconceptions
Confusing the population distribution with the sampling distribution. Thinking larger samples have larger standard errors. Assuming sampling distribution is normal without sufficient sample size or population normality.
