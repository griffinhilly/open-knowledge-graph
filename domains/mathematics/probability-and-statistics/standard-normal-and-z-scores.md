---
id: standard-normal-and-z-scores
title: Standard Normal Distribution and Z-Scores
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: normal-distribution-intro
  type: hard
- id: measures-of-spread
  type: hard
- id: continuous-random-variables
  type: soft
builds-toward:
- confidence-intervals-means
- z-test-for-means
- p-values-and-significance
tags:
- z-score
- standard-normal
- standardization
- z-table
- normal-distribution
stage: formal-systems
status: validated
---
# Standard Normal Distribution and Z-Scores

## Core Idea
The standard normal distribution N(0,1) has mean 0 and standard deviation 1, and its CDF Φ(z) gives the probability P(Z ≤ z). Any normal random variable X ~ N(μ, σ²) is standardized by Z = (X − μ)/σ, converting it to a standard normal. Z-scores measure how many standard deviations an observation is from the mean: a z-score of 2 means the value lies 2 standard deviations above the mean. All normal probabilities are computed via z-score conversion and table or software lookup.

## How It's Best Learned
Begin with the 68-95-99.7 rule to build intuition, then use z-tables for precise probabilities. Have students translate back and forth between raw scores and z-scores in context. Emphasize that standardization shifts the distribution to mean 0 and scales to standard deviation 1 without changing its shape.

## Common Misconceptions
- Reading z-table values as percentiles rather than cumulative probabilities.
- Using σ² (variance) instead of σ (standard deviation) in the z-score formula.
- Confusing 'z = 1.96' as a special cutoff that always applies — it is specific to the 95% level.
