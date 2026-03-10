---
id: poisson-distribution
title: The Poisson Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: expected-value
  type: soft
tags:
- poisson-distribution
- rate
- count
- rare-events
- lambda
stage: formal-systems
status: draft
---

# The Poisson Distribution

## Core Idea
The Poisson distribution models the number of events occurring in a fixed interval of time or space, given a constant average rate λ and events that occur independently of one another. Its PMF is P(X = k) = e^(−λ) · λᵏ / k!, and both the mean and variance equal λ. It arises as a limiting case of the binomial distribution when n is large and p is small, with np = λ.

## How It's Best Learned
Classic examples: number of calls to a call center per hour, defects per meter of wire, cars arriving at an intersection. Have students verify that the Poisson conditions (independence, constant rate, events don't cluster) are plausible. Compute cumulative probabilities using tables or software.

## Common Misconceptions
- Applying Poisson when events are not independent (e.g., disease spread is contagious).
- Confusing λ as the count of expected events per trial vs. per interval — always specify the interval.
- Thinking variance must differ from mean in real data; Poisson's equality of mean and variance is a useful diagnostic.
