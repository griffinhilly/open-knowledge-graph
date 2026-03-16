---
id: standard-normal-z-scores-theory
title: Standard Normal Distribution and Z-Score Standardization
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: normal-distribution-theory
  type: hard
builds-toward:
- confidence-intervals-means
- z-test-for-means
tags:
- standard-normal
- z-score
stage: formal-systems
status: draft
---

# Standard Normal Distribution and Z-Score Standardization

## Core Idea
Standard normal N(0,1) has mean 0 and variance 1. Transform: Z=(X−μ)/σ converts any normal to standard normal. Z-scores measure standardized distance from mean, enabling comparison across scales and use of standard normal tables.

## Explainer

From your study of the normal distribution, you know that X ~ N(μ, σ²) describes a bell-shaped distribution centered at μ with spread determined by σ. The standard normal N(0, 1) is not a different kind of object — it is the same bell curve, simply recentered at 0 and rescaled so that one standard deviation equals one unit. The transformation Z = (X − μ)/σ accomplishes exactly this: subtracting μ shifts the center to 0, and dividing by σ rescales the spread to 1. Every normal distribution, regardless of its mean and variance, collapses to the same N(0, 1) under this transformation.

The **Z-score** Z = (X − μ)/σ has an immediate interpretation: it tells you how many standard deviations the value X sits above or below the mean. A Z-score of 2 means X is two standard deviations above μ; a Z-score of −1.5 means it is 1.5 standard deviations below. This standardized distance is scale-free, which makes it useful for comparison. If a student scores 72 on a test with μ = 65, σ = 10, and 85 on another with μ = 80, σ = 15, the Z-scores are (72−65)/10 = 0.7 and (85−80)/15 = 0.33 respectively — the first score was actually stronger relative to its distribution.

The practical power of standardization comes from probability tables. Computing P(X ≤ x) for an arbitrary N(μ, σ²) requires integrating the normal density, which has no closed form. But the transformation P(X ≤ x) = P(Z ≤ (x−μ)/σ) = Φ((x−μ)/σ) converts the problem to a lookup in a single table of the **standard normal CDF** Φ(z). This is why a single Z-table can answer probability questions for any normal distribution — the shape is universal once you standardize.

The Z-score framework also underlies the structure of hypothesis testing you will encounter when building on this topic. When you later test hypotheses about a population mean, you compute a test statistic of the form Z = (X̄ − μ₀)/(σ/√n), which is exactly standardization applied to the sample mean. The denominator σ/√n is the standard deviation of X̄, so this Z-score measures how many "sampling standard deviations" the observed mean sits from the hypothesized value. The logic is the same: translate a raw difference into a standardized, scale-free number that can be located on the universal normal curve.
