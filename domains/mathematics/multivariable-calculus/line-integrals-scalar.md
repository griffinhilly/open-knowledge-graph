---
id: line-integrals-scalar
title: Line Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: arc-length-parametric
  type: hard
builds-toward:
- line-integrals-vector-fields
- work-line-integrals
tags:
- line-integral
- arc-length
stage: formal-systems
status: draft
---

# Line Integrals of Scalar Functions

## Core Idea
The line integral ∫_C f ds integrates a scalar function along a curve, weighted by arc length. Parametrically: ∫_C f ds = ∫_a^b f(r(t)) ||r'(t)|| dt. This generalizes single-variable integration to curves.

## Explainer

From arc length, you know that the length of a curve C parametrized by r(t) for t ∈ [a, b] is ∫ₐᵇ |r'(t)| dt. This integral accumulates the infinitesimal arc-length element ds = |r'(t)| dt along the path. A **scalar line integral** ∫_C f ds does the same accumulation, but instead of adding up ds alone, it weights each piece of arc length by the value of the scalar function f at that point. Intuitively: if f(x, y, z) represents the linear density (mass per unit length) of a wire shaped like the curve C, then ∫_C f ds gives the total mass of the wire.

The parametric formula makes this concrete. Substitute the curve: f is evaluated at each point r(t) on the path, giving f(r(t)), and each infinitesimal bit of arc length is |r'(t)| dt. The integral becomes ∫ₐᵇ f(r(t)) |r'(t)| dt — an ordinary single-variable integral in t. The |r'(t)| factor is essential: it converts from "distance in parameter t" to "actual distance along the curve," which is what makes the result independent of how you choose to parametrize C. If you travel the same wire faster or slower, the mass doesn't change.

This independence from parametrization is a key feature. Unlike vector-field line integrals (which you'll study next and which do depend on the direction of traversal), scalar line integrals are purely geometric: ∫_C f ds depends on the curve as a set of points and on the function f, but not on the direction of travel or the speed of parametrization. Reversing the direction of C leaves ∫_C f ds unchanged, because both f and ds are unaffected by orientation.

The step from arc length to scalar line integrals is the conceptual bridge to all line integrals. Once you accept the idea of "sum up a quantity per unit length along a curve," the scalar line integral is natural. The vector-field line integral ∫_C F · dr comes next, but its formula ∫ₐᵇ F(r(t)) · r'(t) dt has a different character — the dot product with r'(t) (rather than |r'(t)|) incorporates both direction and magnitude, which is why vector line integrals measure work done and do depend on orientation.
