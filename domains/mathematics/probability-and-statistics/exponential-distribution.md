---
id: exponential-distribution
title: The Exponential Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
- id: exponential-functions-review
  type: soft
tags:
- exponential-distribution
- waiting-time
- memoryless
- rate-parameter
- reliability
stage: formal-systems
status: draft
---

# The Exponential Distribution

## Core Idea
The exponential distribution with rate parameter λ models the waiting time until the next event from a Poisson process, with PDF f(x) = λe^(−λx) for x ≥ 0. Its mean is 1/λ and variance is 1/λ². Like the geometric distribution, it is memoryless: P(X > s + t | X > s) = P(X > t). It is the continuous analog of the geometric distribution and arises naturally in survival analysis, queueing theory, and reliability engineering.

## How It's Best Learned
Pair with the Poisson distribution: if calls arrive at rate λ per hour, then inter-arrival times follow Exp(λ). Compute CDF probabilities using F(x) = 1 − e^(−λx) without needing tables. The memoryless property can be derived directly from this formula.

## Common Misconceptions
- Confusing the rate parameter λ with the mean — the mean is 1/λ, not λ.
- Thinking the exponential distribution applies to any non-negative continuous random variable.
- Applying it to processes where waiting times are not memoryless (e.g., machine aging increases failure probability).
