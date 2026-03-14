---
id: poisson-distribution
title: Poisson Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
builds-toward:
- sampling-distributions
tags:
- poisson
- rate
- rare-events
stage: formal-systems
status: draft
---

# Poisson Distribution

## Core Idea
The Poisson distribution models the number of events occurring in a fixed interval when events occur at a constant average rate λ and independently. Its PMF is P(X = k) = e^(-λ) × λ^k / k!. Both mean and variance equal λ. The Poisson distribution approximates the binomial distribution when n is large and p is small (so np ≈ λ), and arises naturally as a limit of binomial processes.

## How It's Best Learned
Derive Poisson as a limit of binomial. Model real phenomena (phone calls, website traffic) using Poisson. Compare Poisson and binomial approximations for large n and small p.

## Common Misconceptions
Using Poisson for events in fixed counts rather than fixed intervals/regions. Forgetting that mean and variance are equal. Applying Poisson without the independence assumption.
