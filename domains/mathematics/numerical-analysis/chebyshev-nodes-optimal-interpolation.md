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
stage: advanced
status: draft
---

# Chebyshev Nodes and Optimal Interpolation

## Core Idea
Chebyshev nodes, the roots of the Chebyshev polynomial of the first kind, minimize the maximum nodal polynomial and are optimal for polynomial interpolation. They cluster near the endpoints of the interval, matching the increasing derivatives of smooth functions there. Using Chebyshev nodes eliminates Runge's phenomenon and provides near-optimal error bounds for smooth functions.

## Explainer

From your study of interpolation error analysis, you know the error bound for polynomial interpolation takes the form |f(x) − P(x)| ≤ (max|f^(n+1)(ξ)|/(n+1)!) · |ω(x)|, where ω(x) = (x − x₀)(x − x₁)···(x − xₙ) is the **nodal polynomial** — the product of all (x − xᵢ) terms. The derivative factor depends only on the function, not on the choice of nodes. But the nodal polynomial depends entirely on where you place your interpolation points. This raises a clean optimization question: which placement of n+1 nodes in [a, b] minimizes the maximum value of |ω(x)| over the interval?

The answer is the **Chebyshev nodes**: xₖ = cos((2k+1)π/(2n+2)) for k = 0, 1, …, n, mapped from [−1, 1] to [a, b] via a simple linear rescaling. These are the roots of the **Chebyshev polynomial of the first kind** Tₙ₊₁(x) = cos((n+1)arccos(x)). The key property is that among all monic polynomials of degree n+1, Tₙ₊₁(x)/2ⁿ has the smallest possible maximum absolute value on [−1, 1], equal to 1/2ⁿ. No other choice of nodes can produce a nodal polynomial with a smaller max — Chebyshev nodes are optimal in the minimax sense.

Looking at where Chebyshev nodes fall on the interval explains their behavior intuitively. They cluster near the endpoints and spread out toward the center, with the density proportional to 1/√(1 − x²). This is precisely the opposite of uniform spacing, which packs more resolution in the middle and leaves the endpoints relatively undersampled. The problem with uniform nodes is **Runge's phenomenon**: even for smooth functions like f(x) = 1/(1 + 25x²), interpolating at equally-spaced points on [−1, 1] produces a polynomial that wildly oscillates near the endpoints as n increases. The maximum of |ω(x)| for uniform nodes grows much faster near the endpoints than near the center, causing the interpolant to diverge there. Chebyshev nodes tame this by equalizing the error across the interval — the **equioscillation** property means |ω(x)| achieves its maximum value at roughly equal heights across multiple points, which is the signature of an optimal approximation.

In practice, switching from uniform to Chebyshev nodes requires no change to your interpolation algorithm — you simply evaluate the function at a different set of x-values. The gains are dramatic for smooth functions: the interpolation error decreases **geometrically** in n (exponential convergence) rather than polynomially. For functions with singularities or limited smoothness, Chebyshev nodes lose their advantage because the derivative bound in the error formula then dominates. This is why Chebyshev nodes are the default choice for high-degree polynomial approximation of smooth functions, forming the basis of spectral methods in scientific computing and the Chebfun numerical system.
