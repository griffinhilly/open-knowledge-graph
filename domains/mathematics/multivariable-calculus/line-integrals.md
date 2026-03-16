---
id: line-integrals
title: Line Integrals of Scalar and Vector Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-fields
  type: hard
- id: arc-length-parametric
  type: hard
builds-toward:
- fundamental-theorem-line-integrals
- conservative-fields-potential
tags:
- line-integrals
- work
- circulation
stage: formal-systems
status: draft
---

# Line Integrals of Scalar and Vector Functions

## Core Idea
Line integrals ∫_C f ds (scalar) or ∫_C F · dr (vector) integrate along curves. The scalar version sums f weighted by arc length; the vector version computes work done by F along a path C. Both depend on the parametrization's orientation.

## Explainer

Ordinary integrals accumulate a quantity along a straight line segment (the x-axis). Line integrals do the same thing along an arbitrary curve in space. The curve is the domain of integration, and you need a way to measure "how much" of that curve passes through each point. That is the role of **arc length** from your prerequisites: the scalar ds is an infinitesimal piece of arc length, telling you how long a tiny piece of the curve is.

The **scalar line integral** ∫_C f ds answers: if f(x,y,z) is a density or weight at each point, what is the total accumulated quantity along the curve? Imagine a wire whose linear density (mass per unit length) varies from point to point. The total mass is ∫_C ρ ds — sum up density times length element at each point along the wire. To compute this, you parametrize the curve: let r(t) for t ∈ [a,b] trace out C, then ds = |r′(t)| dt, and the integral becomes ∫_a^b f(r(t)) |r′(t)| dt — a standard single-variable integral. The factor |r′(t)| is the speed of the parametrization, which converts the parameter increment dt into actual arc length.

The **vector line integral** ∫_C F · dr asks a different question: how much does the vector field F push the path forward? The integrand F · dr picks up the component of F in the direction of motion along C. This is the **work** done by a force field F on a particle traveling along C. Using the parametrization, dr = r′(t) dt, so the integral becomes ∫_a^b F(r(t)) · r′(t) dt. The dot product F · r′(t) extracts how much F aligns with the direction of travel at each moment; integrating it gives cumulative work. When F is perpendicular to the path everywhere, this integral is zero — a force perpendicular to motion does no work.

**Orientation matters** for vector line integrals but not for scalar ones. Reversing the direction of traversal negates the vector line integral (since r′(t) reverses), but leaves the scalar integral unchanged (since |r′(t)| is always positive). This asymmetry reflects the underlying physics: a force field that aids your journey one way opposes it the other way. For conservative vector fields — those with a potential function — the vector line integral depends only on the endpoints, not the path taken. That is the content of the Fundamental Theorem for Line Integrals, which you will explore next.
