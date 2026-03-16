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

## Explainer

From fixed-point iteration, you know that iterating g(x) gives linear convergence when |g'(r)| < 1 at the fixed point r — the error shrinks by a constant factor |g'(r)| each step. Newton's method is a special case of fixed-point iteration: applying it to f(x) = 0 means iterating g(x) = x - f(x)/f'(x). What makes Newton's method special is that g'(r) = 0 when f(r) = 0, meaning the linear-convergence factor vanishes entirely. This is why the method is so fast.

The Taylor series from your prerequisites makes this precise. Expand f around the current guess x_n near the true root r: f(r) = f(x_n) + f'(x_n)(r - x_n) + (f''(ξ)/2)(r - x_n)² for some ξ between x_n and r. Since f(r) = 0, rearranging gives: r - x_{n+1} = r - (x_n - f(x_n)/f'(x_n)) = -(f''(ξ)/2f'(x_n)) · (r - x_n)². If you write e_n = x_n - r for the error at step n, this becomes e_{n+1} ≈ C · e_n² where C = f''(r)/(2f'(r)). The error is squared each step — this is **quadratic convergence**.

The practical consequence is dramatic: if your current error is 0.01, after one Newton step it is roughly (0.01)² = 0.0001; after another it is roughly 0.00000001. The number of correct decimal digits roughly doubles with each iteration. Compare this to bisection or fixed-point iteration, which add roughly one correct bit per step. Starting from a reasonable initial guess, Newton's method typically converges in 5–10 iterations to machine precision, regardless of the problem.

However, quadratic convergence is a local guarantee. The analysis assumes x_n is already close to r, f' is nonzero at r, and f'' is bounded nearby. Far from the root, Newton's method can cycle, diverge, or converge to a different root than intended. A flat derivative f'(x_n) ≈ 0 means dividing by a near-zero number, sending the iterate far from r. This is why the common practice is to use a globally-convergent method like bisection to get within the neighborhood, then switch to Newton's method for the final rapid convergence — combining reliability with speed.
