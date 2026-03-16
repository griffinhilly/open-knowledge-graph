---
id: line-integrals-definition-properties
title: Line Integrals of Scalar and Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions-curves
  type: hard
builds-toward:
- conservative-vector-fields-potential
- greens-theorem-applications
tags:
- line-integrals
- scalar
- vector-fields
stage: formal-systems
status: draft
---

# Line Integrals of Scalar and Vector Fields

## Core Idea
For a curve C parametrized by r(t), the line integral of scalar f is ∫_C f ds = ∫_a^b f(r(t)) |r'(t)| dt. For vector field F, ∫_C F · dr = ∫_a^b F(r(t)) · r'(t) dt represents work done by F along C.

## Explainer

From your work with vector-valued functions and curves, you know that r(t) = (x(t), y(t), z(t)) parametrizes a path through space and that r'(t) is the tangent vector with magnitude |r'(t)| equal to the speed along the curve. A **line integral** generalizes ordinary integration to functions defined along a curve — instead of integrating f(x) over an interval on the x-axis, you integrate f over an arbitrary path in 2D or 3D space.

The **scalar line integral** ∫_C f ds answers: "If f(x, y, z) is a quantity defined at every point in space (say, temperature, or the linear density of a wire), what is the total accumulated value along the curve?" The arc-length element ds = |r'(t)| dt converts the parameter t back into actual distance along the curve, ensuring the answer doesn't depend on how fast you traverse the path. The result ∫_a^b f(r(t)) |r'(t)| dt evaluates f at each point on the curve, weights it by the arc-length element, and sums. If f = 1, you recover the arc length of C — a special case confirming the formula's meaning.

The **vector line integral** ∫_C F · dr has a fundamentally different structure and interpretation. Here F is a vector field — a vector attached to every point in space — and dr = r'(t) dt is the infinitesimal displacement along the curve. The dot product F · dr picks out the component of F *parallel to the curve's direction* at each point, then multiplies by the arc length element. Summing these up gives the total **work** done by the field F on a particle moving along C. If F is a force field (gravity, electromagnetism), this integral gives the physical work. Notice: the |r'(t)| factor that appeared in the scalar case cancels here because dr already carries direction and magnitude. The result ∫_a^b F(r(t)) · r'(t) dt *does* depend on the direction of traversal — reversing the path negates the integral, reflecting the fact that work against a force is negative.

Both integrals share a common structure: evaluate the integrand at each point of the curve (using the parametrization), multiply by the appropriate measure of "how much curve" you've accumulated, and integrate over the parameter. The scalar version uses |r'(t)| to measure arc length; the vector version uses r'(t) to capture both length and direction. This distinction between the two types of line integrals is the conceptual foundation for everything that follows — conservative fields, the gradient theorem, Green's theorem, and Stokes' theorem all hinge on properties of vector line integrals.
