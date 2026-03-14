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
If Y = aX + b, then E[Y] = aE[X] + b and Var(Y) = a²Var(X). These rules extend to sums: E[X+Y] = E[X] + E[Y] and Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y). Linear transformations are fundamental to standardization and inference.
