---
id: z-test-for-means
title: One-Sample Z-Test for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: standard-normal-and-z-scores
  type: hard
- id: central-limit-theorem
  type: soft
builds-toward:
- t-test-for-means
tags:
- z-test
- one-sample
- test-statistic
- known-variance
- hypothesis-testing
stage: formal-systems
status: draft
---

# One-Sample Z-Test for Means

## Core Idea
The one-sample z-test assesses whether a sample mean x̄ differs significantly from a hypothesized population mean μ₀, when the population standard deviation σ is known. The test statistic z = (x̄ − μ₀) / (σ/√n) follows a standard normal distribution under H₀, by the central limit theorem. The z-test is rarely applicable in practice (σ is almost never known) but provides the theoretical foundation for the more practical t-test.

## How It's Best Learned
Work through complete examples: state H₀ and Hₐ, compute z, find the p-value from the z-table, state the conclusion in context. Practice both one-tailed and two-tailed tests. Explicitly note that the z-test assumes σ is known — ask students why this is unrealistic.

## Common Misconceptions
- Dividing by σ instead of σ/√n — forgetting the standard error adjustment.
- Using the z-test when the population is non-normal and n is small.
- Stating the conclusion in terms of x̄ rather than the population parameter μ.
