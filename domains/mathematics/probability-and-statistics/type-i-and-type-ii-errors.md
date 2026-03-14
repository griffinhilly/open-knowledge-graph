---
id: type-i-and-type-ii-errors
title: Type I and Type II Errors
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
builds-toward:
- z-test-and-t-test-for-means
tags:
- type-i-error
- type-ii-error
- false-positive
- false-negative
stage: formal-systems
status: draft
---

# Type I and Type II Errors

## Core Idea
A Type I error (false positive) occurs when we reject H₀ when it is actually true; its probability is the significance level α. A Type II error (false negative) occurs when we fail to reject H₀ when the alternative is actually true; its probability is β. The power of a test is 1 - β, the probability of correctly rejecting a false H₀. Decreasing α (more conservative) increases β, so trade-offs exist. Larger sample sizes reduce both α and β for a fixed α threshold.

## How It's Best Learned
Create a 2×2 table (truth vs. decision) and label all four outcomes. Relate Type I/II errors to real consequences (medical testing, legal trials). Discuss why lower α increases Type II error.

## Common Misconceptions
Confusing Type I with Type II error. Thinking we can make α = β = 0 simultaneously. Forgetting that α is fixed at the start; we don't compute it from data. Misunderstanding power in the context of sample size.
