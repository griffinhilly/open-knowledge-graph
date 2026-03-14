---
id: expected-value-and-variance
title: Expected Value and Variance
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
builds-toward:
- continuous-random-variables
- binomial-distribution
- normal-distribution
tags:
- expected-value
- mean
- variance
- standard-deviation
stage: formal-systems
status: draft
---

# Expected Value and Variance

## Core Idea
The expected value E[X] = Σ x × p(x) is the long-run average value of a random variable, representing its center. Variance Var(X) = E[(X - E[X])²] measures the spread of the distribution around its mean. Standard deviation σ = √Var(X) is variance expressed in the original units. These moments summarize key features of a distribution's shape and behavior.

## How It's Best Learned
Compute expected value and variance for simple distributions (fair die, coin flip). Verify that variance increases when probability mass spreads away from the mean.

## Common Misconceptions
Thinking E[X] is always the most likely value. Confusing variance with standard deviation in interpretation. Misunderstanding that E[aX + b] = aE[X] + b but Var(aX + b) = a²Var(X).
