---
id: chebyshev-nodes
title: Chebyshev Nodes and Optimal Interpolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runges-phenomenon
  type: hard
builds-toward:
- cubic-spline-interpolation
tags:
- chebyshev
- optimal-nodes
- interpolation
stage: abstract-reasoning
status: draft
---

# Chebyshev Nodes and Optimal Interpolation

## Core Idea
Chebyshev nodes, the roots of the Chebyshev polynomial T_n(x) = cos(n·arccos(x)), minimize max|∏(x - x_i)| and are clustered near the interval endpoints [-1,1]. Using Chebyshev nodes for interpolation prevents Runge oscillations and ensures convergence for smooth functions. This choice is optimal among all node sets in the minimax sense.

## Explainer

Runge's phenomenon revealed that equally-spaced interpolation nodes cause polynomial interpolants to wildly oscillate near the endpoints of the interval, even for smooth functions like 1/(1 + 25x²). The source of the problem is the **node error product** ω(x) = (x - x_0)(x - x_1)···(x - x_n): the interpolation error at any point x is bounded by a term involving |ω(x)|, and with equally-spaced nodes, this product becomes very large near x = ±1. To fix the problem, you need to choose nodes that make max|ω(x)| as small as possible.

The answer comes from an unexpected direction: trigonometry. The **Chebyshev nodes** on [-1, 1] are x_k = cos((2k+1)π / (2n+2)) for k = 0, 1, ..., n. These are the projections onto the x-axis of equally-spaced points on the upper semicircle. Near the center x = 0, the points are spread apart; near the endpoints x = ±1, they cluster together. This crowding near the endpoints is precisely what counteracts the natural tendency of the error to blow up there.

The optimality of Chebyshev nodes is not accidental — it follows from a deep minimax property. The **Chebyshev polynomial** T_n(x) = cos(n arccos(x)) is the unique monic polynomial of degree n whose maximum absolute value on [-1, 1] is minimized. Its maximum value is 1/2^{n-1}, and no other monic polynomial of degree n can stay flatter on [-1, 1]. Since the node error product ω(x) is exactly a monic degree-(n+1) polynomial, choosing the roots of T_{n+1}(x) as your nodes makes ω(x) = T_{n+1}(x)/2^n, which achieves the minimum possible maximum.

In practice, transforming any interval [a, b] to [-1, 1] via x = (a + b)/2 + (b - a)/2 · t lets you always use Chebyshev nodes. For smooth functions, using Chebyshev nodes not only prevents the Runge explosion but guarantees that the interpolating polynomial converges to the function as n → ∞ — a guarantee that equally-spaced interpolation cannot provide. This makes Chebyshev nodes the default choice whenever you are doing polynomial interpolation and care about accuracy across the whole interval.
