---
id: geometric-distribution
title: Geometric Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
- id: independence-and-multiplication-rule
  type: hard
tags:
- geometric
- waiting-time
- first-success
stage: formal-systems
status: draft
---

# Geometric Distribution

## Core Idea
The geometric distribution models the number of trials needed to achieve the first success in a sequence of independent Bernoulli trials with success probability p. Its PMF is P(X = k) = (1-p)^(k-1) × p for k = 1, 2, 3, ... Mean is 1/p and variance is (1-p)/p². This distribution is memoryless: the probability of success on the next trial doesn't depend on how many failures have occurred.

## How It's Best Learned
Compare with binomial by noting geometric counts until first success, while binomial counts successes in fixed trials. Demonstrate memorylessness with examples.

## Common Misconceptions
Confusing when to use geometric vs. binomial. Different conventions for support (some start at 0, others at 1).
