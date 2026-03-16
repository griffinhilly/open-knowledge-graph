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
- id: power-series
  type: soft
- id: binomial-theorem-expansion
  type: soft
builds-toward:
- taylor-series
tags:
- series
- Taylor
- approximation
- polynomials
stage: formal-systems
status: validated
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

## Explainer

You already know **linear approximation**: near a point a, a differentiable function behaves like its tangent line L(x) = f(a) + f'(a)(x − a). This first-degree polynomial is exact at x = a (it matches f(a)) and its slope matches f'(a), so it is the best straight-line approximation near that point. A **Taylor polynomial** extends this idea: instead of matching only the value and first derivative, match the value and the first n derivatives simultaneously. Each additional derivative matched adds one more polynomial term and corrects a new layer of curvature that the previous approximation missed.

The formula forces itself on you once you accept the goal. If you want a polynomial P(x) = c₀ + c₁(x−a) + c₂(x−a)² + ··· + cₙ(x−a)ⁿ such that P^(k)(a) = f^(k)(a) for k = 0, 1, ..., n, you can solve for each coefficient by differentiating. When you differentiate P k times and set x = a, only the k-th term survives: P^(k)(a) = k! · cₖ. Setting this equal to f^(k)(a) gives **cₖ = f^(k)(a)/k!**. The k! in the denominator is not arbitrary — it is exactly what cancels the k! that differentiating a k-th degree monomial produces. The full formula is the sum from k=0 to n of f^(k)(a)/k! · (x−a)^k.

For the most useful Taylor polynomials centered at 0 (called **Maclaurin polynomials**), the pattern is memorable. For eˣ, every derivative evaluated at 0 is 1, so the polynomial is 1 + x + x²/2! + x³/3! + ···. For sin(x), the odd derivatives at 0 alternate ±1 and even derivatives vanish, giving x − x³/3! + x⁵/5! − ···. For cos(x), the reverse: 1 − x²/2! + x⁴/4! − ···. Plotting these polynomials of increasing degree against the true function on the same axes is the best way to internalize the idea: P₁ hugs the curve briefly near x = 0, P₃ hugs it longer, P₅ longer still.

The **Lagrange remainder** R_n(x) = f^(n+1)(c)/(n+1)! · (x−a)^(n+1) (for some c between a and x) tells you the maximum error you are making with your n-th degree approximation. This is Taylor's inequality in practice: bound |f^(n+1)| on the interval, then the remainder formula gives a concrete error guarantee. This turns Taylor polynomials from a neat algebraic trick into a rigorous engineering tool — you can certify that your approximation is within, say, 0.001 of the true value on a given interval, which is exactly what software and calculators do when they compute transcendental functions.
