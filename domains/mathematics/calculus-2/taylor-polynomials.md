---
id: taylor-polynomials
title: Taylor Polynomials
domain: mathematics
course: calculus-2
prerequisites:
  - id: higher-order-derivatives
    type: hard
  - id: linear-approximation
    type: hard
builds-toward:
  - taylor-series
tags: [series, Taylor, approximation, polynomials]
stage: formal-systems
status: draft
---

# Taylor Polynomials

## Core Idea
The nth-degree Taylor polynomial of f centered at a is P_n(x) = sum from k=0 to n of f^(k)(a)/k! * (x - a)^k. It is the unique polynomial of degree n that matches f and its first n derivatives at x = a. Taylor polynomials extend linear approximation to higher-order approximation: P_1 is the tangent line, P_2 adds curvature correction, and each additional term improves accuracy near a. The error (remainder) can be bounded by Taylor's inequality.

## How It's Best Learned
Start from linear approximation (n = 1), add the quadratic term (n = 2), and observe improvement. Compute Taylor polynomials for e^x, sin(x), cos(x) centered at 0. Plot the polynomials against the true function to see convergence. Introduce the Lagrange remainder for error estimation.

## Common Misconceptions
- Confusing Taylor polynomials (finite, exact at a) with Taylor series (infinite, convergent on an interval).
- Forgetting the k! in the denominator.
- Not understanding that the polynomial is exact at x = a and approximate elsewhere.
