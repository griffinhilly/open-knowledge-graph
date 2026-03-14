---
id: confidence-intervals-proportions
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: binomial-distribution
  type: hard
- id: confidence-intervals-means
  type: soft
tags:
- confidence-interval
- proportion
- p-hat
- margin-of-error
stage: formal-systems
status: validated
---

# Confidence Intervals for Proportions

## Core Idea
A confidence interval for a population proportion p uses the sample proportion p̂ = x/n as the point estimate, giving the interval p̂ ± z* · √(p̂(1−p̂)/n). The standard error √(p̂(1−p̂)/n) is maximized at p̂ = 0.5, making the 'worst case' margin of error 1/(2√n). The normal approximation is valid when both np̂ ≥ 10 and n(1−p̂) ≥ 10. This interval is widely used in polling, survey research, and quality control.

## How It's Best Learned
Connect to political polling: most news reports cite a ±3% margin of error. Show students how this corresponds to n ≈ 1000 at the 95% confidence level using the worst-case formula. Emphasize that p̂ = 0.5 gives the widest interval.

## Common Misconceptions
- Using the formula when success/failure conditions are not met (very small or very large p̂).
- Forgetting that the margin of error depends on p̂ — it is not simply ±1/√n.
- Misinterpreting the confidence level as the probability that the true p is in the interval.
