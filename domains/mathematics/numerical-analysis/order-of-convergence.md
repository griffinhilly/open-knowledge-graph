---
id: order-of-convergence
title: Order of Convergence
domain: mathematics
course: numerical-analysis
prerequisites:
- id: bisection-method
  type: hard
- id: newton-method-convergence
  type: hard
tags:
- convergence
- error-reduction
- rates
stage: abstract-reasoning
status: draft
---

# Order of Convergence

## Core Idea
The order of convergence describes how fast iteration errors decrease. Linear convergence (order 1) reduces error by a constant factor each step; quadratic (order 2) roughly squares the error each step. Higher orders reach tolerance in fewer iterations, but convergence order only holds asymptotically near the solution—far away, even superlinear methods may behave slowly.

## How It's Best Learned
Compare error reduction for bisection, Newton, and secant methods on the same problem, plotting error vs. iteration on a log scale to see the different slopes.

## Common Misconceptions
- Confusing order of convergence with speed; a method with lower order but fewer function evaluations per step may be faster overall.
- Assuming quadratic convergence from the first iteration; convergence order applies only in the final iterations when close to the solution.
