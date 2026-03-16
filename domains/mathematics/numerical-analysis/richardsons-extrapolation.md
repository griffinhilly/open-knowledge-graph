---
id: richardsons-extrapolation
title: Richardson's Extrapolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- romberg-integration
tags:
- richardson-extrapolation
- acceleration
- deferred-correction
stage: advanced
status: draft
---

# Richardson's Extrapolation

## Core Idea
Richardson's extrapolation accelerates convergence by combining approximations at different step sizes to cancel leading error terms. If an approximation has error A(h) = a₀ + a₁h^p + a₂h^{2p} + ..., linear combinations of A(h) and A(h/2) eliminate the a₁h^p term, increasing convergence order. This technique amplifies accuracy without more function evaluations.

## Explainer

Richardson's extrapolation is a clever trick that turns "two mediocre approximations" into "one much better one." To see why it works, start with what you know from Taylor series. Many numerical methods — finite difference derivatives, numerical integration rules, and others — produce approximations whose error can be expanded as a power series in the step size h: A(h) = L + c₁h^p + c₂h^{2p} + ... where L is the true answer, and the c₁h^p term is the dominant error. Halving h reduces this leading error by a factor of 2^p — which is good. But Richardson's idea is more radical: can we *eliminate* that leading error term entirely, rather than just shrinking it?

Yes. Compute A(h) and A(h/2). You have two equations: A(h) ≈ L + c₁h^p and A(h/2) ≈ L + c₁(h/2)^p = L + c₁h^p/2^p. Multiply the second equation by 2^p and subtract the first: 2^p · A(h/2) − A(h) ≈ (2^p − 1)L. Solving for L gives the **Richardson extrapolate**: R = (2^p · A(h/2) − A(h)) / (2^p − 1). The c₁h^p term cancels exactly, and the remaining error is O(h^{2p}) — a full order improvement. For a method that was O(h^2) accurate, Richardson extrapolation makes it O(h^4) with no extra function evaluations beyond computing A at two step sizes.

A concrete example makes this vivid. The centered difference formula approximates f'(x) ≈ (f(x+h) − f(x−h))/(2h) with error O(h²). Suppose h = 0.1 gives error ~0.01, and h = 0.05 gives error ~0.0025. You could just use h = 0.05 and accept the O(h²) accuracy. Or you could take both values, apply Richardson extrapolation with p = 2 (since the error series involves even powers of h), and get an approximation with error O(h⁴) — roughly 0.0000625. Same two function evaluations, dramatically better result.

The deeper reason Richardson extrapolation is so powerful is that it's not specific to any one method. Wherever you have an approximation with a known asymptotic error expansion, you can apply extrapolation. **Romberg integration** — the topic this leads into — applies Richardson extrapolation repeatedly to the trapezoidal rule, building a triangular table of increasingly accurate estimates. At each level, you eliminate one more error term, until floating-point roundoff dominates. This recursive application is the soul of Romberg's method.

One important caution: Richardson extrapolation requires that the error expansion A(h) = L + c₁h^p + c₂h^{2p} + ... actually holds — that the error truly behaves like a power series in h. If this assumption breaks down (for example, near a discontinuity, or when the function is not smooth enough to support a Taylor expansion), the extrapolation can give wildly wrong answers. The method amplifies accuracy when the expansion is valid, and amplifies error when it isn't. Understanding *why* the expansion holds for a given method — which comes from Taylor series analysis — is essential for knowing when to trust the result.
