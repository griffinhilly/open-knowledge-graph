---
id: type-i-and-type-ii-errors
title: Type I and Type II Errors
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: p-values-and-significance
  type: soft
tags:
- type-I-error
- type-II-error
- false-positive
- false-negative
- power
- alpha
- beta
stage: formal-systems
status: validated
---

# Type I and Type II Errors

## Core Idea
A Type I error (false positive) occurs when H₀ is true but we reject it; its probability equals α, the significance level. A Type II error (false negative) occurs when H₀ is false but we fail to reject it; its probability is β. The power of a test, 1 − β, is the probability of correctly rejecting a false H₀. Reducing α decreases Type I errors but increases Type II errors — the two error rates trade off. Increasing sample size is the primary way to reduce both simultaneously.

## How It's Best Learned
Use a medical testing analogy: Type I error = wrongly diagnosing a healthy person with disease; Type II error = missing a true disease. Different domains have different tolerances for each error type. Draw the four-cell outcome table (H₀ true/false × reject/fail to reject) and fill in each cell's meaning and probability.

## Common Misconceptions
- Thinking α is the probability of making an error overall — it is the probability of a specific error (Type I) when H₀ is true.
- Assuming that a non-significant result means H₀ is true — it may simply reflect low power.
- Confusing power (1 − β) with the significance level α.
