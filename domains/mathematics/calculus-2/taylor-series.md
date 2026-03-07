---
id: taylor-series
title: Taylor Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: taylor-polynomials
    type: hard
  - id: power-series
    type: hard
  - id: radius-and-interval-of-convergence
    type: hard
builds-toward:
  - maclaurin-series
  - taylor-series-common-functions
tags: [series, Taylor, representation]
stage: formal-systems
status: draft
---

# Taylor Series

## Core Idea
The Taylor series of f centered at a is the infinite power series sum from n=0 to infinity of f^(n)(a)/n! * (x - a)^n. If this series converges to f(x), then f has a power series representation. The Taylor series extends the Taylor polynomial to infinite degree, providing an exact representation (not just an approximation) within the radius of convergence. Not all functions equal their Taylor series (the remainder must go to zero).

## How It's Best Learned
Derive Taylor series for e^x, sin(x), cos(x), and 1/(1 - x) from the definition. Verify convergence using the ratio test. Show that the remainder term goes to zero (at least for the standard functions). Practice manipulating known Taylor series (substitution, differentiation, integration) to find new ones.

## Common Misconceptions
- Assuming every infinitely differentiable function equals its Taylor series (counterexample: e^(-1/x^2) at 0).
- Confusing the Taylor series (infinite, representation) with Taylor polynomial (finite, approximation).
- Not checking that the remainder goes to zero, which is required for the series to equal the function.
