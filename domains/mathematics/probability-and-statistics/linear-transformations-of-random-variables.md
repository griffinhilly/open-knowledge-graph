---
id: linear-transformations-of-random-variables
title: Linear Transformations of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: hard
builds-toward:
- sampling-distributions
- confidence-intervals-means
tags:
- transformations
- random-variables
- probability
stage: formal-systems
status: draft
---

# Linear Transformations of Random Variables

## Core Idea
Linear transformations are the workhorses of probability. If Y = aX + b, then E[Y] = aE[X] + b and Var(Y) = a²Var(X)—expectation is linear while variance scales quadratically and is unaffected by shifts. For sums of random variables, E[X + Y] = E[X] + E[Y] always holds, but Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), so independence simplifies the variance formula. These properties underpin standardization (converting any distribution to mean 0 and variance 1), the construction of confidence intervals, and the derivation of sampling distributions used throughout statistical inference.

## How It's Best Learned
Derive the rules algebraically from the definition of expectation, then verify them numerically with a simple example: roll a die, let X be the result, compute E[3X + 2] and Var(3X + 2) both by formula and by enumerating all outcomes.

## Common Misconceptions
Students frequently forget the squared coefficient in Var(aX) = a²Var(X) and write aVar(X) instead. Another common error is assuming Var(X + Y) = Var(X) + Var(Y) without checking independence—the covariance term is only zero when X and Y are uncorrelated.

