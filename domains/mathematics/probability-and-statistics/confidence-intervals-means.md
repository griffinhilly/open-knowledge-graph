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
- confidence-intervals-proportions
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- margin-of-error
- z-interval
- estimation
- coverage
stage: formal-systems
status: validated
---

# Confidence Intervals for Means

## Core Idea
A confidence interval for a population mean is an interval estimate x̄ ± z* · (σ/√n) that captures the true mean with a specified probability (confidence level) in repeated sampling. The z* critical value depends on the confidence level (z* = 1.96 for 95% confidence). Importantly, a 95% confidence interval means that 95% of all intervals constructed this way will contain the true mean — it does not mean the true mean has a 95% probability of being in this particular interval.

## How It's Best Learned
Simulate 100 confidence intervals from repeated samples of a known population, then count how many actually capture the true mean. Watching roughly 95 of 100 intervals cover the truth makes the frequentist interpretation concrete and precise.

## Common Misconceptions
- 'There is a 95% probability the population mean is in this interval' — after construction, the interval either contains μ or it doesn't; probability refers to the long-run procedure.
- Increasing confidence level narrows the interval — it widens it.
- Confusing confidence level (95%) with the proportion of data within the interval.
