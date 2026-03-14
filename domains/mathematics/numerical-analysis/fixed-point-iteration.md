---
id: fixed-point-iteration
title: Fixed Point Iteration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: mean-value-theorem
  type: soft
builds-toward:
- order-of-convergence
- jacobi-iterative-method
tags:
- fixed-point
- iteration
- convergence
stage: advanced
status: draft
---

# Fixed Point Iteration

## Core Idea
Fixed point iteration solves equations of the form g(x) = x by iterating x_{n+1} = g(x_n) from an initial guess. Convergence is guaranteed when g is a contraction mapping near the fixed point, quantified by the Banach Fixed Point Theorem: if |g'(x)| < 1 in a neighborhood of the solution, iteration converges linearly.
