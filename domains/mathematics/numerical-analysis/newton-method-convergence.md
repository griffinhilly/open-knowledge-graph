---
id: newton-method-convergence
title: 'Newton''s Method: Convergence Analysis'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: fixed-point-iteration
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- order-of-convergence
- secant-method
tags:
- newton-method
- root-finding
- convergence
stage: abstract-reasoning
status: draft
---

# Newton's Method: Convergence Analysis

## Core Idea
Newton's method iterates x_{n+1} = x_n - f(x_n)/f'(x_n) to find roots of f. Under suitable conditions (f' continuous and nonzero at the root, sufficiently close initial guess), Newton's method converges quadratically—the number of correct digits roughly doubles with each iteration. The method is fast and powerful but requires derivative computation and can fail with poor initial guesses.

## How It's Best Learned
Implement Newton's method for familiar functions like finding √2, observing how error shrinks quadratically compared to bisection's linear shrinkage.

## Common Misconceptions
- Thinking Newton's method always converges from any starting point; convergence is local, requiring closeness to the root.
- Assuming Newton's method is cheaper than bisection; it requires derivative evaluation, which may be expensive or unavailable.
