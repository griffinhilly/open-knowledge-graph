---
id: uniform-distribution-continuous
title: Continuous Uniform Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
builds-toward:
- exponential-distribution
tags:
- uniform
- continuous-distribution
stage: formal-systems
status: draft
---

# Continuous Uniform Distribution

## Core Idea
The continuous uniform distribution on [a, b] has constant PDF f(x) = 1/(b-a) for a ≤ x ≤ b, and zero elsewhere. Every subinterval of equal length has equal probability. Mean is (a+b)/2 and variance is (b-a)²/12. Uniform distributions model scenarios where outcomes are equally likely throughout an interval, such as random selection from a continuous range.

## How It's Best Learned
Visualize the constant PDF. Compute probabilities as areas of rectangles. Compare variance across different interval widths.

## Common Misconceptions
Confusing PDF value (1/(b-a)) with probability for a single point. Misremembering the variance formula.
