---
id: complex-line-integrals
title: Complex Line Integrals
domain: mathematics
course: complex-analysis
prerequisites:
- id: holomorphic-functions
  type: hard
- id: line-integrals-scalar
  type: hard
builds-toward:
- contour-integration
- cauchys-theorem
tags:
- line-integrals
- contour-integrals
- path-dependence
stage: advanced
status: draft
---

# Complex Line Integrals

## Core Idea
The integral of f(z) along a path γ from a to b is ∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt. For a general continuous f, this integral depends on the path. But for holomorphic f on simply connected domains, the integral is path-independent and depends only on the endpoints, a fact made rigorous by Cauchy's theorem.

## How It's Best Learned
Compute ∫_γ z dz along two different paths from 0 to 1+i; verify that they give the same result. Then try f(z) = 1/z along paths that wind around the origin; observe the path-dependence.

## Common Misconceptions
Assuming all line integrals are path-independent; this is true only for holomorphic functions on simply connected domains. Forgetting to parametrize the contour when computing the integral.
