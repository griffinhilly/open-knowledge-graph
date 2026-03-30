---
id: integration-on-manifolds
title: Integration on Manifolds
domain: mathematics
course: differential-geometry
prerequisites:
  - id: differential-forms-introduction
    type: hard
  - id: orientation
    type: hard
  - id: partition-of-unity
    type: hard
tags:
  - integration
  - volume-forms
  - change-of-variables
  - manifolds
stage: advanced
status: validated
---

# Integration on Manifolds

## Core Idea
Integration of differential forms on oriented manifolds generalizes multiple integrals from ℝⁿ to curved spaces. An n-form on an oriented n-manifold is integrated by pulling back to coordinate charts via a partition of unity — the transformation law for forms automatically handles the Jacobian determinant from the change of variables formula. This framework unifies line integrals, surface integrals, and volume integrals into a single coordinate-free theory.

## Questions

```yaml
- question: "To define ∫_M ω for an n-form ω on an oriented n-manifold M, you need a partition of unity {ρα} and write ∫_M ω = Σα ∫_M ρα ω. Each term ∫_M ρα ω is computed by..."
  type: multiple-choice
  options:
    - "Evaluating ρα ω at a single point and multiplying by the volume of M"
    - "Pulling back ρα ω to ℝⁿ via the coordinate chart φα and computing a standard Riemann/Lebesgue integral"
    - "Using the metric to convert ω to a function and integrating that function"
    - "Approximating M by a simplicial complex and summing over simplices"
  answer: 1
  explanation: "Since supp(ρα ω) ⊂ Uα, we pull back to the coordinate chart: ∫_M ρα ω = ∫_{φα(Uα)} (φα⁻¹)*(ρα ω), which is an integral of an n-form on an open subset of ℝⁿ — a standard multivariable integral. In coordinates, if ρα ω = f dx¹ ∧ ... ∧ dxⁿ, this becomes ∫ f dx¹...dxⁿ. No metric is needed — the form itself provides the 'volume element.' The partition of unity ensures independence of the chosen cover and partition."

- question: "Reversing the orientation of M multiplies ∫_M ω by -1."
  type: true-false
  answer: true
  explanation: "An orientation determines which coordinate charts are 'positively oriented' — those with positive Jacobian determinant transitions. Reversing orientation flips the sign of the Jacobian determinant in the change-of-variables formula, which flips the sign of the integral. Equivalently, if -M denotes M with the opposite orientation, then ∫_{-M} ω = -∫_M ω. This is why oriented manifolds are essential: without orientation, the integral of a form is not well-defined (it could be either sign)."

- question: "Integration on manifolds does not require a Riemannian metric. What, then, determines the 'volume element' for integration?"
  type: short-answer
  answer: "The differential form itself serves as the volume element. An n-form ω on an n-manifold assigns to each infinitesimal parallelepiped (spanned by n tangent vectors) a signed volume. No metric is needed to define this — the form evaluates on tangent vectors directly. What is needed is an orientation (to fix the sign) and the form to integrate. A Riemannian metric becomes necessary only when you want a canonical volume form (the Riemannian volume form dVg = √det(gij) dx¹∧...∧dxⁿ) or when you want to integrate functions rather than forms."
  explanation: "This is a key conceptual point. In vector calculus, the volume element dV = dx dy dz seems to require knowing what 'volume' means, which suggests a metric. But differential forms carry their own notion of volume. The metric enters only when you want to measure lengths, angles, or integrate scalar functions (in which case you multiply the function by the metric volume form). The metric-free nature of form integration is what makes Stokes' theorem work in full generality."
```

## Explainer

In multivariable calculus on ℝⁿ, you integrate functions f by computing ∫ f dx¹...dxⁿ. Under a change of variables x = φ(u), this becomes ∫ f(φ(u)) |det Dφ| du¹...duⁿ — the Jacobian determinant appears. On a manifold, there are no preferred coordinates, so you need an object whose transformation law automatically includes the Jacobian. Differential n-forms are exactly that object: under a coordinate change, an n-form transforms by det(Jacobian) — without the absolute value, which is why you need an orientation to fix the sign.

The construction of ∫_M ω proceeds in three steps. First, choose an atlas {(Uα, φα)} of positively oriented charts and a subordinate partition of unity {ρα}. Second, write ω = Σα ρα ω, where each term is supported in a single chart. Third, compute each ∫_M ρα ω by pulling back to ℝⁿ: in coordinates, (φα⁻¹)*(ρα ω) = fα dx¹ ∧ ... ∧ dxⁿ, and ∫_M ρα ω = ∫ fα dx¹...dxⁿ as an ordinary integral. The sum of these integrals is ∫_M ω. A crucial verification: this is independent of the choice of atlas and partition of unity (because the transformation law for forms handles the change-of-variables automatically).

When a manifold has a Riemannian metric g, there is a canonical **volume form** dVg: in positively oriented coordinates, dVg = √det(gij) dx¹ ∧ ... ∧ dxⁿ. To integrate a function f : M → ℝ, you integrate the n-form f · dVg. The factor √det(gij) accounts for the "stretching" of the coordinate grid relative to the intrinsic geometry — on a sphere in spherical coordinates, this gives the familiar sin θ factor. But forms of degree less than n (like 1-forms on surfaces) can be integrated over appropriate submanifolds without any metric at all.

Integration on manifolds is the essential link between local differential data and global geometric/topological invariants. The total curvature of a surface (the Gauss-Bonnet integral), the de Rham cohomology pairing, characteristic classes of vector bundles, and the action functional in physics are all integrals of differential forms over manifolds. Stokes' theorem — the next topic — provides the fundamental relationship between integrals over a manifold and integrals over its boundary, completing the framework that unifies Green's theorem, the divergence theorem, and the classical Stokes theorem into a single statement.
