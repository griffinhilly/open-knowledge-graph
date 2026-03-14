---
id: newton-divided-differences
title: Newton's Divided Differences
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- interpolation-error-analysis
tags:
- divided-differences
- interpolation
- newton
stage: abstract-reasoning
status: draft
---

# Newton's Divided Differences

## Core Idea
Newton's divided difference formula represents the interpolating polynomial as P(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + ..., where divided differences are defined recursively. This form is numerically stable and allows efficient addition of new points by appending terms without recomputing previous coefficients.

## How It's Best Learned
Construct divided difference tables by hand for small datasets, then implement the recurrence relation to see how coefficients build up naturally.

## Common Misconceptions
- Thinking divided differences are the same as derivatives; they are discrete approximations that approach derivatives as points converge.
- Assuming the divided difference formula is just a rearrangement of Lagrange; it expresses the same polynomial more stably and flexibly.
