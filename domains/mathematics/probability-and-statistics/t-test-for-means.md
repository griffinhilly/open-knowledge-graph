---
id: t-test-for-means
title: One-Sample and Two-Sample T-Tests
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: z-test-for-means
  type: soft
- id: measures-of-spread
  type: hard
builds-toward:
- anova-one-way
tags:
- t-test
- t-distribution
- degrees-of-freedom
- two-sample
- paired
stage: formal-systems
status: draft
---

# One-Sample and Two-Sample T-Tests

## Core Idea
The t-test replaces the z-test when the population standard deviation σ is unknown, estimating it with the sample standard deviation s. The test statistic t = (x̄ − μ₀) / (s/√n) follows a t-distribution with n − 1 degrees of freedom — a bell-shaped distribution with heavier tails than the normal. Two-sample t-tests compare means of two independent groups; paired t-tests account for matched pairs by analyzing differences. As n increases, the t-distribution approaches the standard normal.

## How It's Best Learned
Use technology for p-value computation — the t-distribution CDF is not tabulated conveniently. Focus on conditions: nearly normal population or large n, independent observations. Practice deciding which t-test applies: one-sample, two-sample independent, or paired.

## Common Misconceptions
- Using pooled variance when population variances are not assumed equal (Welch's t-test is safer).
- Forgetting to compute differences first in a paired design — treating paired data as independent.
- Not checking normality conditions before applying the t-test to small samples.
