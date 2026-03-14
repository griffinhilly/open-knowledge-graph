---
id: confidence-intervals-means
title: Confidence Intervals for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: central-limit-theorem
  type: hard
- id: standard-normal-and-z-scores
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- interval-estimation
- t-distribution
stage: formal-systems
status: draft
---

# Confidence Intervals for Means

## Core Idea
A confidence interval for a population mean is an interval (estimate ± margin of error) computed so that, in repeated sampling, it contains the true mean with a specified confidence level (typically 95%). For large samples, use the normal (z) distribution: x̄ ± z* × (s/√n). For smaller samples, use the t-distribution: x̄ ± t* × (s/√n). The confidence level describes the long-run proportion of intervals that capture the parameter, not the probability that the true mean lies in a specific computed interval.

## How It's Best Learned
Compute confidence intervals for various sample sizes and confidence levels. Interpret them correctly in context. Observe that wider confidence levels produce narrower intervals and vice versa.

## Common Misconceptions
Thinking a 95% CI means 95% probability the true mean is in the interval (it's fixed; the interval is random). Confusing confidence level with p-value. Misunderstanding how sample size affects margin of error.
