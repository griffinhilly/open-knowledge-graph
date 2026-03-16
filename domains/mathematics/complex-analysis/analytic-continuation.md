---
id: analytic-continuation
title: Analytic Continuation
domain: mathematics
course: complex-analysis
prerequisites:
- id: taylor-series-complex
  type: hard
tags:
- analytic-continuation
- extension
- identity-theorem
stage: advanced
status: draft
---

# Analytic Continuation

## Core Idea
If two analytic functions agree on a set with a limit point in their common domain, then they are identical on the entire connected component of their domain. This identity theorem implies that an analytic function is completely determined by its values on any small open set, and can be uniquely extended (continued) along paths in the plane — the basis for understanding multi-valued functions and Riemann surfaces.

## Explainer

From your study of Taylor series in the complex plane, you know that a holomorphic function on a disk is completely encoded by its power series, and the power series converges on the largest disk that avoids singularities. This suggests something striking: knowing a function on a small disk might determine it everywhere. The **Identity Theorem** makes this precise and provides the theoretical foundation for analytic continuation.

The Identity Theorem states: if f and g are holomorphic on a connected open domain D, and they agree on any set that has a limit point inside D — even an infinite sequence of distinct points converging to an interior point — then f ≡ g throughout D. This rigidity has no real-analysis counterpart. A smooth real function can be freely modified on any interval without affecting its values elsewhere. A holomorphic complex function has no such freedom: its Taylor coefficients at any point are forced by the function values on any nearby limit-containing set, and matching Taylor coefficients on one disk forces equality on every overlapping disk, propagating throughout the connected domain.

**Analytic continuation** exploits this rigidity to extend functions beyond their original domains. Given f holomorphic on a disk D₁, suppose you find a holomorphic function g on an overlapping disk D₂ that agrees with f on D₁ ∩ D₂. The Identity Theorem guarantees that g is the *unique* analytic extension of f to D₂ — there is no other way to extend f holomorphically to D₂. Repeat the process disk by disk along a path to reach far beyond the original domain. The classic instance is the Riemann zeta function: the series Σ n⁻ˢ converges only for Re(s) > 1, but analytic continuation uniquely extends it to all of ℂ minus a simple pole at s = 1.

A subtlety arises when continuation can travel along loops. If you continue log(z) starting near z = 1, where log(1) = 0, and travel along a path that winds once around the origin, you return to z = 1 with value 2πi instead of 0. The continuation is path-dependent: the value you recover depends on how many times you've encircled the origin. This **monodromy** is the source of multi-valued functions — log z and z^(1/2) are not truly multi-valued but are single-valued functions on a **Riemann surface**, a multi-sheeted domain that unwinds the loop. Analytic continuation reveals this structure: when continuing around a loop fails to return to the starting value, the domain itself must be extended into multiple sheets to accommodate the function globally.
