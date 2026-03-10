---
id: binomial-distribution
title: The Binomial Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: combinations
  type: hard
- id: independence-and-multiplication-rule
  type: hard
- id: expected-value
  type: soft
builds-toward:
- geometric-distribution
- confidence-intervals-proportions
tags:
- binomial-distribution
- bernoulli
- trials
- n-choose-k
- success-failure
stage: formal-systems
status: draft
---

# The Binomial Distribution

## Core Idea
A binomial random variable counts the number of successes in n independent trials, each with success probability p. Its PMF is P(X = k) = C(n, k) · pᵏ · (1−p)ⁿ⁻ᵏ. The mean is μ = np and variance is σ² = np(1−p). The binomial distribution applies when: fixed number of trials, each trial is independent, only two outcomes (success/failure), and constant p.

## How It's Best Learned
The four BINS conditions (Binary, Independent, Number-fixed, Same-probability) give students a checklist. Practice identifying whether a scenario qualifies before computing. Use normal approximation to binomial for large n as a preview of the central limit theorem.

## Common Misconceptions
- Applying binomial without checking the independence condition (sampling without replacement from small populations violates this).
- Confusing n (number of trials) with k (number of successes).
- Using n instead of np for the mean.
