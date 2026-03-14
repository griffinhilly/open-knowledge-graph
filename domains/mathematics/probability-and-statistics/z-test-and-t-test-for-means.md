---
id: z-test-and-t-test-for-means
title: Z-Tests and T-Tests for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: standard-normal-and-z-scores
  type: hard
- id: confidence-intervals-means
  type: soft
tags:
- z-test
- t-test
- test-statistic
- p-value
stage: formal-systems
status: draft
---

# Z-Tests and T-Tests for Means

## Core Idea
A z-test tests hypotheses about a population mean when the population standard deviation σ is known (rare in practice). The test statistic is z = (x̄ - μ₀) / (σ/√n). A t-test is used when σ is unknown and replaced by sample standard deviation s; the test statistic is t = (x̄ - μ₀) / (s/√n), which follows a t-distribution with n-1 degrees of freedom. The t-distribution has heavier tails than normal, so t-tests account for additional uncertainty from estimating σ. Both tests compare observed sample means to hypothesized population means.

## How It's Best Learned
Compute z and t statistics from data. Use tables or software to find p-values. Compare z-test and t-test on the same data for large and small samples. Understand why t-distribution is appropriate for small samples.

## Common Misconceptions
Using z-test when σ is unknown. Confusing degrees of freedom in t-distribution. Thinking larger t values have larger p-values (opposite is true). Misapplying tests without checking normality assumptions for small samples.
