---
id: runges-phenomenon
title: Runge's Phenomenon
domain: mathematics
course: numerical-analysis
prerequisites:
- id: interpolation-error-analysis
  type: hard
builds-toward:
- chebyshev-nodes
- cubic-spline-interpolation
tags:
- runges-phenomenon
- oscillation
- interpolation
stage: abstract-reasoning
status: draft
---

# Runge's Phenomenon

## Core Idea
For certain smooth functions like f(x) = 1/(1+x²), polynomial interpolation on equally-spaced nodes exhibits wild oscillations that grow unboundedly as the number of nodes increases. This Runge phenomenon demonstrates that increasing polynomial degree with equally-spaced nodes is not a reliable path to better approximation. The root cause is the large node product |∏(x - x_i)| near the interval endpoints.

## Explainer

From interpolation error analysis, you know that if p_n(x) is the degree-n polynomial passing through n+1 nodes x₀, x₁, …, xₙ, the pointwise error is:

|f(x) − p_n(x)| = |ω_{n+1}(x)| · |f^(n+1)(ξ)| / (n+1)!

where ω_{n+1}(x) = (x−x₀)(x−x₁)···(x−xₙ) is the **node product** and ξ is some unknown point in the interval. To get accurate interpolation as n grows, *both* factors must stay small: the derivatives of f must not blow up, and the node product must remain controlled.

**Runge's phenomenon** is a concrete failure of the second condition. Consider f(x) = 1/(1+25x²) on [−1, 1]. This function is smooth — infinitely differentiable — so you might expect that adding more interpolation nodes would always improve accuracy. With equally spaced nodes, the opposite happens near the endpoints: the node product ω_{n+1}(x) grows very large. The spacing forces all the "wiggle room" of a degree-n polynomial toward the ends of the interval. Meanwhile, 1/(1+25x²) has complex singularities at x = ±i/5 that are close to the real axis, which causes the derivatives to grow fast enough that the error bound diverges as n → ∞. Plotting the degree-10 interpolant through 11 equally spaced points on [−1, 1] shows relatively good accuracy near the center but dramatic oscillations reaching amplitudes of 2 near x = ±1, even though the function itself never exceeds 1.

The lesson is that **more nodes do not automatically mean better approximation** — the placement of nodes matters as much as their number. The node product ω_{n+1}(x) is minimized (in the max-norm sense) when the nodes are the **Chebyshev nodes**: xₖ = cos((2k+1)π/(2n+2)) for k = 0, 1, …, n. These nodes cluster near the endpoints, precisely where equally spaced nodes leave large gaps. With Chebyshev nodes, the maximum value of |ω_{n+1}(x)| over the interval is 2^{−n}, which is as small as possible, and polynomial interpolation converges for a much broader class of functions.

Runge's phenomenon also motivates **piecewise polynomial** approaches like cubic splines: instead of fitting one high-degree polynomial to all the data, fit low-degree polynomials on each small subinterval. Cubic splines use degree-3 polynomials on each piece, avoiding high-degree oscillation entirely while still achieving smooth joins between pieces. The phenomenon is thus a cautionary tale about global polynomial interpolation and a primary historical motivation for both Chebyshev nodes and spline methods.
