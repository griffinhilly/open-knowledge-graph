---
id: normal-distribution
title: Normal Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
- id: expected-value-and-variance
  type: soft
builds-toward:
- standard-normal-and-z-scores
- central-limit-theorem
- confidence-intervals-means
tags:
- normal
- gaussian
- bell-curve
stage: formal-systems
status: draft
---

# Normal Distribution

## Core Idea
The normal distribution with mean μ and standard deviation σ has PDF f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²)). It is symmetric, bell-shaped, and completely determined by its mean and variance. The normal distribution is ubiquitous in statistics because many naturally occurring phenomena approximate it, and because of the central limit theorem, which states that means of large samples are approximately normal regardless of the original distribution.

## How It's Best Learned
Visualize how mean shifts and standard deviation stretches the bell curve. Use the empirical rule (68-95-99.7). Compare distributions with different μ and σ.

## Common Misconceptions
Assuming all bell-shaped distributions are normal. Thinking the normal distribution can be negative (values are on ℝ, but probabilities decay in tails). Confusing standard deviation with variance.
