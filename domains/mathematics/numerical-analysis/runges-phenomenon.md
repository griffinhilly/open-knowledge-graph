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
stage: advanced
status: validated
---

# Runge's Phenomenon

## Core Idea
For certain smooth functions like f(x) = 1/(1+x²), polynomial interpolation on equally-spaced nodes exhibits wild oscillations that grow unboundedly as the number of nodes increases. This Runge phenomenon demonstrates that increasing polynomial degree with equally-spaced nodes is not a reliable path to better approximation. The root cause is the large node product |∏(x - x_i)| near the interval endpoints.

## Questions

```yaml
- question: "A student interpolates f(x) = 1/(1+25x²) on [−1, 1] with 15 equally spaced nodes and observes large oscillations near x = ±1. She adds 10 more equally spaced nodes hoping to fix the problem. What will most likely happen?"
  type: multiple-choice
  options:
    - "The oscillations near the endpoints will decrease as the polynomial better fits the smooth function"
    - "The oscillations near the endpoints will get worse — adding more equally spaced nodes increases the maximum of the node product near the endpoints"
    - "The oscillations will disappear because 25 nodes are always sufficient for any smooth function"
    - "The error will decrease uniformly across the whole interval"
  answer: 1
  explanation: "This is Runge's phenomenon: for f(x) = 1/(1+25x²) with equally spaced nodes, the interpolation error grows without bound near the endpoints as the degree increases. Adding more equally spaced nodes makes the node product |ω_{n+1}(x)| larger near x = ±1, not smaller, because equally spaced nodes leave large gaps at the endpoints while packing interior nodes tightly. The function's complex singularities at x = ±i/5 amplify this problem. The correct response is not more nodes but different node placement (Chebyshev nodes) or a different interpolation strategy (splines)."

- question: "What is the fundamental reason that Chebyshev nodes reduce interpolation error compared to equally spaced nodes?"
  type: multiple-choice
  options:
    - "Chebyshev nodes avoid placing points near the endpoints where the function may be undefined or have large values"
    - "Chebyshev nodes minimize the maximum value of the node product |ω_{n+1}(x)| over the interval by clustering nodes near the endpoints where the product would otherwise be largest"
    - "Chebyshev nodes are computed using a numerically stable algorithm that equally spaced nodes lack"
    - "Chebyshev nodes are optimal only for polynomials with no complex singularities"
  answer: 1
  explanation: "The interpolation error bound is proportional to |ω_{n+1}(x)| = |(x−x₀)(x−x₁)···(x−xₙ)|. Equally spaced nodes leave large gaps near the endpoints, making this product large there. Chebyshev nodes cluster near the endpoints precisely because the endpoints are where the node product is hardest to control — they balance the product across the entire interval, reducing its maximum value to 2^{−n}. This is the minimax property: Chebyshev nodes minimize the worst-case node product over the interval."

- question: "Runge's phenomenon can occur even for functions that are infinitely differentiable and have no singularities on the real interval being interpolated."
  type: true-false
  answer: true
  explanation: "f(x) = 1/(1+25x²) is infinitely differentiable on [−1,1] — it has no real singularities on the real line. The problem arises from complex singularities at x = ±i/5, which are close to the real axis. These cause the higher derivatives to grow rapidly even though the function looks smooth. Runge's phenomenon is a reminder that smoothness on the real line is not sufficient to guarantee convergence of high-degree polynomial interpolation — the behavior in the complex plane also matters. This is precisely what makes the phenomenon surprising and important."

- question: "Increasing the degree of a polynomial interpolant by adding more equally spaced nodes is typically a reliable strategy for improving approximation accuracy over the entire interval."
  type: true-false
  answer: false
  explanation: "This is exactly what Runge's phenomenon disproves. For functions with complex singularities near the real axis (like 1/(1+25x²)), polynomial interpolation on equally spaced nodes diverges near the endpoints as the degree increases — the approximation actively gets worse, not better. The key lesson is that accuracy depends on both the number of nodes AND their placement. More nodes with poor placement can increase error. Chebyshev nodes or piecewise polynomial methods (splines) are needed for reliable high-accuracy approximation."

- question: "Why does the placement of interpolation nodes matter as much as their number, and how does the node product |ω_{n+1}(x)| explain why equally spaced nodes cause oscillations near the endpoints of the interval?"
  type: short-answer
  answer: "The interpolation error at a point x is proportional to |ω_{n+1}(x)| = |(x−x₀)(x−x₁)···(x−xₙ)|, the product of distances from x to each node. With equally spaced nodes on [−1,1], the interior nodes are tightly clustered but the endpoints have no nearby nodes to make the factors (x−xᵢ) small. Near x = ±1, several factors are large simultaneously, making the node product large. With more equally spaced nodes, this worsens because the interior becomes more crowded but the endpoint region remains relatively sparse. Chebyshev nodes fix this by clustering at the endpoints, making the factors near x = ±1 small and distributing the node product's size more uniformly across the interval."
  explanation: "The insight is that the node product cannot be made uniformly small — it must be large somewhere. Chebyshev nodes distribute this unavoidable largeness as evenly as possible (minimax). Equally spaced nodes stack all the largeness at the endpoints, which is the worst possible choice for bounding the maximum error."
```

## Explainer

From interpolation error analysis, you know that if p_n(x) is the degree-n polynomial passing through n+1 nodes x₀, x₁, …, xₙ, the pointwise error is:

|f(x) − p_n(x)| = |ω_{n+1}(x)| · |f^(n+1)(ξ)| / (n+1)!

where ω_{n+1}(x) = (x−x₀)(x−x₁)···(x−xₙ) is the **node product** and ξ is some unknown point in the interval. To get accurate interpolation as n grows, *both* factors must stay small: the derivatives of f must not blow up, and the node product must remain controlled.

**Runge's phenomenon** is a concrete failure of the second condition. Consider f(x) = 1/(1+25x²) on [−1, 1]. This function is smooth — infinitely differentiable — so you might expect that adding more interpolation nodes would always improve accuracy. With equally spaced nodes, the opposite happens near the endpoints: the node product ω_{n+1}(x) grows very large. The spacing forces all the "wiggle room" of a degree-n polynomial toward the ends of the interval. Meanwhile, 1/(1+25x²) has complex singularities at x = ±i/5 that are close to the real axis, which causes the derivatives to grow fast enough that the error bound diverges as n → ∞. Plotting the degree-10 interpolant through 11 equally spaced points on [−1, 1] shows relatively good accuracy near the center but dramatic oscillations reaching amplitudes of 2 near x = ±1, even though the function itself never exceeds 1.

The lesson is that **more nodes do not automatically mean better approximation** — the placement of nodes matters as much as their number. The node product ω_{n+1}(x) is minimized (in the max-norm sense) when the nodes are the **Chebyshev nodes**: xₖ = cos((2k+1)π/(2n+2)) for k = 0, 1, …, n. These nodes cluster near the endpoints, precisely where equally spaced nodes leave large gaps. With Chebyshev nodes, the maximum value of |ω_{n+1}(x)| over the interval is 2^{−n}, which is as small as possible, and polynomial interpolation converges for a much broader class of functions.

Runge's phenomenon also motivates **piecewise polynomial** approaches like cubic splines: instead of fitting one high-degree polynomial to all the data, fit low-degree polynomials on each small subinterval. Cubic splines use degree-3 polynomials on each piece, avoiding high-degree oscillation entirely while still achieving smooth joins between pieces. The phenomenon is thus a cautionary tale about global polynomial interpolation and a primary historical motivation for both Chebyshev nodes and spline methods.
