---
id: exponential-distribution
title: Exponential Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
tags:
- exponential
- waiting-time
- memoryless
stage: formal-systems
status: draft
---

# Exponential Distribution

## Core Idea
The exponential distribution with rate parameter λ > 0 has PDF f(x) = λe^(-λx) for x ≥ 0, and models waiting times until an event when events occur at a constant rate λ. Mean is 1/λ and variance is 1/λ². The exponential distribution is memoryless: P(X > s + t | X > s) = P(X > t), meaning remaining time doesn't depend on elapsed time. It naturally arises as the continuous analog of the geometric distribution.

## How It's Best Learned
Derive memoryless property algebraically. Model real waiting time scenarios (customer service, radioactive decay). Relate to Poisson processes.

## Common Misconceptions
Confusing rate λ with scale parameter 1/λ. Not recognizing memorylessness property. Applying exponential without constant rate assumption.
