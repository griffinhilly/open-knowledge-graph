---
id: chebyshev-nodes-optimal-interpolation
title: Chebyshev Nodes and Optimal Interpolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: interpolation-error-analysis
  type: hard
builds-toward:
- cubic-spline-interpolation
- gaussian-quadrature
tags:
- chebyshev-nodes
- optimal-nodes
- equioscillation
stage: formal-systems
status: validated
---

# Chebyshev Nodes and Optimal Interpolation

## Core Idea
Chebyshev nodes, the roots of the Chebyshev polynomial of the first kind, minimize the maximum nodal polynomial and are optimal for polynomial interpolation. They cluster near the endpoints of the interval, matching the increasing derivatives of smooth functions there. Using Chebyshev nodes eliminates Runge's phenomenon and provides near-optimal error bounds for smooth functions.

## Questions

```yaml
- question: "You are interpolating a smooth function on [-1, 1] using 20 equally-spaced nodes. The interpolant oscillates wildly near the endpoints. What does switching to Chebyshev nodes fix, and how?"
  type: multiple-choice
  options:
    - "It changes the interpolation algorithm to suppress endpoint oscillations automatically"
    - "It clusters nodes near the endpoints, reducing the maximum of the nodal polynomial there"
    - "It increases the polynomial degree only near the endpoints where errors are large"
    - "It applies a smoothness penalty that damps oscillatory behavior in the interpolant"
  answer: 1
  explanation: "Runge's phenomenon occurs because uniform nodes leave the endpoints undersampled relative to the center, causing the nodal polynomial |ω(x)| to spike near the endpoints. Chebyshev nodes cluster near the endpoints (with density proportional to 1/√(1−x²)), reducing |ω(x)| there. Critically, the interpolation algorithm itself doesn't change — you simply evaluate the function at a different set of x-values. The fix is entirely in the node placement."

- question: "What does it mean that Chebyshev nodes are 'optimal in the minimax sense' for polynomial interpolation?"
  type: multiple-choice
  options:
    - "They minimize the sum of squared errors across all interpolation points"
    - "They guarantee the interpolating polynomial has zero error at the interval midpoint"
    - "Among all choices of n+1 nodes, they produce the monic nodal polynomial with the smallest possible maximum absolute value on the interval"
    - "They minimize the degree of the interpolating polynomial needed to achieve a given accuracy"
  answer: 2
  explanation: "The interpolation error bound is proportional to the maximum of |ω(x)|, where ω is the nodal polynomial. Chebyshev nodes minimize this maximum — no other node placement produces a monic polynomial of the same degree with a smaller sup-norm. The minimal max value is 1/2ⁿ for degree n+1. This is a minimax optimality result, not a least-squares one."

- question: "Chebyshev nodes cluster more densely near the endpoints of the interpolation interval than in the center."
  type: true-false
  answer: true
  explanation: "Yes — the Chebyshev nodes are xₖ = cos((2k+1)π/(2n+2)), which are projections of equally-spaced points on a semicircle down to the x-axis. This packing formula produces density proportional to 1/√(1−x²), which is highest at ±1. This is the opposite of uniform spacing and is precisely what equalizes the nodal polynomial's maximum across the interval."

- question: "Switching from uniform nodes to Chebyshev nodes requires a fundamentally different interpolation algorithm."
  type: true-false
  answer: false
  explanation: "False — the same interpolation algorithm (Lagrange, Newton divided differences, barycentric, etc.) works regardless of node placement. Chebyshev nodes are simply a better choice of x-values at which to evaluate the function. The algorithm takes any set of nodes as input; the optimality is entirely in the selection of those nodes, not in how they are processed."

- question: "Why do uniform nodes cause Runge's phenomenon near the endpoints of an interpolation interval, and how does the distribution of Chebyshev nodes address this?"
  type: short-answer
  answer: "Uniform nodes undersample the endpoint regions relative to the center, causing the nodal polynomial |ω(x)| to grow very large near the endpoints. As the degree increases, this growth dominates the error bound, and the interpolant oscillates wildly. Chebyshev nodes cluster near the endpoints, equalizing |ω(x)| across the interval through the equioscillation property — the nodal polynomial achieves its maximum value at roughly equal heights across multiple points, the signature of a minimax-optimal approximation."
  explanation: "The key insight is that Runge's phenomenon is not a failure of polynomial interpolation in general — it is a failure of uniform node spacing specifically. The error bound involves two factors: the function's derivatives (fixed for a given function) and the nodal polynomial (controlled by node placement). Chebyshev nodes optimize the second factor. This is why they produce geometrically convergent errors for smooth functions."
```

## Explainer

From your study of interpolation error analysis, you know the error bound for polynomial interpolation takes the form |f(x) − P(x)| ≤ (max|f^(n+1)(ξ)|/(n+1)!) · |ω(x)|, where ω(x) = (x − x₀)(x − x₁)···(x − xₙ) is the **nodal polynomial** — the product of all (x − xᵢ) terms. The derivative factor depends only on the function, not on the choice of nodes. But the nodal polynomial depends entirely on where you place your interpolation points. This raises a clean optimization question: which placement of n+1 nodes in [a, b] minimizes the maximum value of |ω(x)| over the interval?

The answer is the **Chebyshev nodes**: xₖ = cos((2k+1)π/(2n+2)) for k = 0, 1, …, n, mapped from [−1, 1] to [a, b] via a simple linear rescaling. These are the roots of the **Chebyshev polynomial of the first kind** Tₙ₊₁(x) = cos((n+1)arccos(x)). The key property is that among all monic polynomials of degree n+1, Tₙ₊₁(x)/2ⁿ has the smallest possible maximum absolute value on [−1, 1], equal to 1/2ⁿ. No other choice of nodes can produce a nodal polynomial with a smaller max — Chebyshev nodes are optimal in the minimax sense.

Looking at where Chebyshev nodes fall on the interval explains their behavior intuitively. They cluster near the endpoints and spread out toward the center, with the density proportional to 1/√(1 − x²). This is precisely the opposite of uniform spacing, which packs more resolution in the middle and leaves the endpoints relatively undersampled. The problem with uniform nodes is **Runge's phenomenon**: even for smooth functions like f(x) = 1/(1 + 25x²), interpolating at equally-spaced points on [−1, 1] produces a polynomial that wildly oscillates near the endpoints as n increases. The maximum of |ω(x)| for uniform nodes grows much faster near the endpoints than near the center, causing the interpolant to diverge there. Chebyshev nodes tame this by equalizing the error across the interval — the **equioscillation** property means |ω(x)| achieves its maximum value at roughly equal heights across multiple points, which is the signature of an optimal approximation.

In practice, switching from uniform to Chebyshev nodes requires no change to your interpolation algorithm — you simply evaluate the function at a different set of x-values. The gains are dramatic for smooth functions: the interpolation error decreases **geometrically** in n (exponential convergence) rather than polynomially. For functions with singularities or limited smoothness, Chebyshev nodes lose their advantage because the derivative bound in the error formula then dominates. This is why Chebyshev nodes are the default choice for high-degree polynomial approximation of smooth functions, forming the basis of spectral methods in scientific computing and the Chebfun numerical system.
