---
id: interpolation-error-analysis
title: Interpolation Error Analysis
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-divided-differences
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runges-phenomenon
- chebyshev-nodes
tags:
- error-analysis
- interpolation
- bounds
stage: abstract-reasoning
status: draft
---

# Interpolation Error Analysis

## Core Idea
If P(x) interpolates f at n+1 points, the error E(x) = f(x) - P(x) satisfies |E(x)| ≤ (max |f^{(n+1)}|)/(n+1)! |∏(x - x_i)|. This bound reveals that error depends on the (n+1)-th derivative of f and the magnitude of the node product. For smooth functions with well-chosen nodes, interpolation error can be very small; poor node placement causes large errors.

## Explainer

From Taylor series, you know that approximating a function by a polynomial accumulates error controlled by higher derivatives. Specifically, the Taylor remainder after n terms involves f^(n+1) evaluated at some point between x and the expansion center. Interpolation error analysis tells a closely parallel story, but now the polynomial matches f at multiple points rather than matching all derivatives at one point. The structure of the error bound reflects this difference in a precise and instructive way.

When P(x) is the unique degree-n polynomial interpolating f at nodes x₀, x₁, …, xₙ, the error at a point x is exactly E(x) = f^(n+1)(ξ) / (n+1)! · ω(x), where ω(x) = (x − x₀)(x − x₁)···(x − xₙ) is the **node polynomial** and ξ is some point in the interval spanned by x and the nodes. The proof mirrors the Taylor remainder proof: define a helper function that vanishes at all n+2 points (the n+1 nodes plus x itself), then apply Rolle's theorem n+1 times to locate a point ξ where the (n+1)-th derivative of the helper equals zero. The final expression falls out cleanly.

The bound |E(x)| ≤ M/(n+1)! · |ω(x)| separates into two factors that tell distinct stories. The term M = max|f^(n+1)| measures how "curved" f is — how much its (n+1)-th derivative fluctuates. You cannot control this; it is a property of f itself. The term |ω(x)| = |∏(x − xᵢ)| measures how far the evaluation point x is from the interpolation nodes, and this you **can** control by choosing nodes wisely. At the nodes themselves, ω = 0 and the error vanishes exactly (as it must, since P interpolates f there). Between nodes and beyond them, |ω| can vary enormously depending on node placement.

The most striking consequence concerns **equally spaced nodes**. Your intuition might suggest that spacing nodes evenly across [a, b] is natural and good — after all, you're covering the interval uniformly. But |ω(x)| for equally spaced nodes is very small near the center of the interval and very large near the endpoints. For functions like f(x) = 1/(1 + 25x²) on [−1, 1] (Runge's function), this edge amplification is so severe that the interpolating polynomial with equally spaced nodes oscillates wildly near ±1 as n increases — the interpolation actually gets worse, not better, as you add more nodes. This is **Runge's phenomenon**.

The fix is **Chebyshev nodes**: xₖ = cos((2k+1)π/(2n+2)) for k = 0, …, n. These nodes cluster near the endpoints and spread out the node polynomial more evenly. The maximum of |ω(x)| over [−1, 1] for Chebyshev nodes is 1/2ⁿ — exponentially smaller than for equally spaced nodes. The lesson is that error analysis is not just about measuring error after the fact; it is a design tool that tells you where to put your nodes before you even begin the computation. Understanding the error formula is what separates a numerical analyst from someone who just applies a formula and hopes for the best.
