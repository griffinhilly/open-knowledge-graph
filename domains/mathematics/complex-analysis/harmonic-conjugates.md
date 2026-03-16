---
id: harmonic-conjugates
title: Harmonic Conjugates
domain: mathematics
course: complex-analysis
prerequisites:
- id: harmonic-functions-complex-analysis
  type: hard
tags:
- harmonic
- conjugate-pairs
- reconstruction
stage: advanced
status: draft
---

# Harmonic Conjugates

## Core Idea
If u is a harmonic function on a simply connected domain D, a harmonic conjugate v is a harmonic function such that f = u + iv is holomorphic on D. The Cauchy-Riemann equations tell us how to find v from u: v is obtained by integration using ∂v/∂x = -∂u/∂y and ∂v/∂y = ∂u/∂x. Every harmonic function has a unique harmonic conjugate up to an additive constant.

## Explainer

From your study of harmonic functions, you know that u(x, y) is harmonic if it satisfies Laplace's equation ∂²u/∂x² + ∂²u/∂y² = 0. You also know the Cauchy-Riemann equations: if f = u + iv is holomorphic, then ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. A **harmonic conjugate** of u is a function v satisfying exactly these two equations — it is the imaginary part of a holomorphic function whose real part is u. The relationship is symmetric: u and v are each other's harmonic conjugates, and both are individually harmonic.

The construction of v from u is concrete and computational. Since ∂v/∂y = ∂u/∂x, integrate with respect to y to obtain v up to an unknown function of x alone. Then use the second Cauchy-Riemann equation ∂v/∂x = −∂u/∂y to determine that function. For example, if u = x² − y², then ∂u/∂x = 2x and ∂u/∂y = −2y. Integrating ∂v/∂y = 2x with respect to y gives v = 2xy + g(x). Then ∂v/∂x = 2y + g'(x) must equal −∂u/∂y = 2y, so g'(x) = 0 and g is a constant. The harmonic conjugate is v = 2xy + C, and the corresponding holomorphic function is f = (x² − y²) + i(2xy) = (x + iy)² = z².

The requirement that the domain be **simply connected** is essential. On a domain with holes, a line integral used to construct v may give different values along paths that wind around the hole — the function would be multivalued. The canonical example is u = (1/2) ln(x² + y²) on ℝ² \ {0}, which is harmonic on the punctured plane but has no harmonic conjugate there. The "natural" conjugate would be arctan(y/x), which is multivalued — its value changes by 2π when you loop around the origin. On a simply connected domain, every harmonic function has a harmonic conjugate, unique up to an additive constant.

Harmonic conjugates connect the real and complex worlds cleanly: every harmonic function on a simply connected domain is the real part of some holomorphic function, and finding the conjugate reconstructs that holomorphic function. This is why harmonic functions in complex analysis are far more constrained than harmonic functions in purely real analysis — they come in conjugate pairs, bound together by the Cauchy-Riemann equations and the rigid structure of holomorphic functions.
