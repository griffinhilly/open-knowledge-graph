---
id: confidence-intervals-proportions
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: central-limit-theorem
  type: hard
- id: binomial-distribution
  type: soft
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- proportion
- binomial
stage: formal-systems
status: draft
---

# Confidence Intervals for Proportions

## Core Idea
A confidence interval for a population proportion p is computed from sample proportion p̂. When the sample size is large enough that both np̂ and n(1-p̂) exceed 10, the sample proportion is approximately normal, and we can use: p̂ ± z* × √(p̂(1-p̂)/n). The margin of error decreases with larger sample size and larger confidence level. For smaller samples, exact binomial methods or continuity corrections provide better coverage.

## How It's Best Learned
Compute confidence intervals for proportions in polling contexts. Understand how sample size affects margin of error. Compare normal approximation to exact binomial.

## Common Misconceptions
Using normal approximation when np̂ or n(1-p̂) < 10. Confusing sample proportion p̂ with population proportion p. Thinking margin of error accounts for all sources of error (sampling only).
