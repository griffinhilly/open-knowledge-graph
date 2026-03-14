---
id: binomial-distribution
title: Binomial Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
- id: independence-and-multiplication-rule
  type: hard
builds-toward:
- normal-distribution
- sampling-distributions
tags:
- binomial
- discrete-distribution
- bernoulli
- trials
stage: formal-systems
status: draft
---

# Binomial Distribution

## Core Idea
The binomial distribution models the number of successes in n independent Bernoulli trials, each with success probability p. Its PMF is P(X = k) = C(n,k) × p^k × (1-p)^(n-k), where C(n,k) is the binomial coefficient. The mean is np and variance is np(1-p). Binomial distributions arise whenever we count successes in a fixed number of identical, independent trials.

## How It's Best Learned
Derive the binomial formula from first principles using counting and independence. Explore how the distribution changes with n and p using simulation or calculation.

## Common Misconceptions
Assuming binomial applies without independent trials or equal p. Confusing binomial coefficients with probabilities. Misremembering whether variance is np or np(1-p).
