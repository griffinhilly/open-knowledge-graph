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

## Explainer

The Poisson distribution's origin is a limit of the binomial. Suppose you split a fixed time interval into n very short sub-intervals, each so short that at most one event can occur in it, with probability p = λ/n. As n → ∞ with λ = np held fixed, the binomial PMF converges to P(X = k) = e^(-λ) λ^k / k!. This derivation reveals exactly when Poisson applies: "large number of opportunities, each with small individual probability, independent." Phone calls per hour, typos per page, radioactive decays per second — all fit this description. The parameter λ is both the rate and the expected count over the interval.

The equal-mean-and-variance property is a diagnostic signature, not just a curiosity. When you fit count data to a Poisson model, checking whether the sample mean ≈ sample variance is a quick model adequacy test. If the variance substantially exceeds the mean — a pattern called **overdispersion** — the Poisson model is inadequate, often because events cluster (a car accident makes another more likely, not less). Overdispersed count data frequently requires a **negative binomial model** instead. Conversely, underdispersion suggests that events regulate each other.

The PMF P(X = k) = e^(-λ) λ^k / k! has a memorable structure once you see why it sums to 1: the sum over all k of λ^k / k! is exactly e^λ, so the e^(-λ) factor is precisely the normalizing constant. As k increases from 0, probabilities first rise (λ^k grows faster than k! for small k) then fall (k! dominates for large k). The mode is at ⌊λ⌋. For small λ (rare events), the distribution is sharply right-skewed — the most likely outcome is zero. For large λ, by the central limit theorem, Poisson(λ) is well approximated by Normal(λ, λ), and tables or normal calculations can substitute.

Applying Poisson correctly requires checking three conditions: events occur at a **constant average rate** λ, they are **independent** (past events don't affect future ones), and **simultaneous events** are impossible (probability of two events in an infinitesimal interval is negligible). These are violated more often than beginners realize. Earthquakes trigger aftershocks (dependence). Website traffic spikes at lunch hour (non-constant rate). When these assumptions fail but you use Poisson anyway, your variance estimate will be wrong and any confidence intervals or predictions based on it will be misleading.
