---
id: fixed-point-iteration
title: Fixed Point Iteration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: contraction-mapping
  type: soft
builds-toward:
- order-of-convergence
- newton-method-convergence
tags:
- fixed-point
- iteration
- root-finding
stage: abstract-reasoning
status: draft
---

# Fixed Point Iteration

## Core Idea
Fixed point iteration solves f(x) = 0 by rewriting it as x = g(x) and iterating x_{n+1} = g(x_n). Convergence is guaranteed by the contraction mapping theorem if |g'(x)| < 1 near the fixed point. This method is foundational to understanding iterative algorithms and generalizes to systems of equations and complex domains.
