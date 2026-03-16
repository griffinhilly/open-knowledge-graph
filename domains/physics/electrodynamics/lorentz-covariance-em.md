---
id: lorentz-covariance-em
title: Lorentz Covariance of Maxwell's Equations
domain: physics
course: electrodynamics
prerequisites:
- id: special-relativity-postulates
  type: hard
- id: maxwell-equations-differential-form
  type: hard
builds-toward:
- electromagnetic-field-tensor
- lorentz-transformations-em-fields
tags:
- covariance
- lorentz-invariance
- relativity
stage: advanced
status: draft
---

# Lorentz Covariance of Maxwell's Equations

## Core Idea
Maxwell's equations have the same form in all inertial reference frames—a fundamental requirement of special relativity. This Lorentz covariance is automatic when expressed in terms of 4-vectors and tensors in spacetime, revealing that electrodynamics is inherently relativistic. The covariant formulation unifies space and time, electric and magnetic fields, and provides the foundation for relativistic quantum field theory.

## Explainer

From your study of special relativity, you know that the laws of physics must take the same form in all inertial reference frames — this is the principle of relativity. From your study of Maxwell's equations in differential form, you have four equations relating E⃗ and B⃗ to their sources. A profound historical question is whether Maxwell's equations obey special relativity, or need correction. The answer is that Maxwell's equations are already exactly relativistic — no modification is needed. In fact, Einstein's 1905 paper was titled "On the Electrodynamics of Moving Bodies" precisely because the tension between classical mechanics and Maxwell's equations forced him to reconcile them through special relativity, not the other way around. **Lorentz covariance** is the precise statement that the equations transform correctly under Lorentz transformations, maintaining the same form in every inertial frame.

To see this concretely, consider what happens when you boost to a different frame. In your original frame, you might see a purely static electric field (say, from a stationary charge). An observer moving relative to you sees the same charge moving — a moving charge is a current, and a current produces a magnetic field. So what you call a pure electric field, the moving observer sees as a combination of electric and magnetic fields. The E⃗ and B⃗ fields are not separately Lorentz-invariant: they **mix** under boosts, exactly as space and time coordinates mix. The deeper structure is the **electromagnetic field tensor** F^μν — a 4×4 antisymmetric tensor that packages all six components of E⃗ and B⃗ together. Under a Lorentz transformation, F^μν transforms as a proper rank-2 tensor, and Maxwell's equations, written as ∂_μ F^μν = J^ν (where J^μ is the 4-current), are manifestly covariant — every index is contracted, making the equation frame-independent.

The covariant formulation also unifies the sources. In 3D, charge density ρ and current density J⃗ appear as separate objects. In 4D spacetime, they combine into a single **4-current** J^μ = (cρ, J⃗), which transforms as a 4-vector under boosts. Similarly, the scalar and vector potentials φ and A⃗ unify into the **4-potential** A^μ = (φ/c, A⃗). The field tensor is then F^μν = ∂^μ A^ν − ∂^ν A^μ, a clean geometric statement. Maxwell's equations reduce to two tensor equations: ∂_μ F^μν = μ₀J^ν and ∂_[μ F_νλ] = 0 (the Bianchi identity), each manifestly Lorentz-covariant.

This covariant framework is not merely aesthetic elegance — it is computationally essential. When you need to find the fields of a moving charge or transform fields between frames, the tensor transformation rules give the answer directly. The relativistic invariants of the field — quantities unchanged by boosts — are E·B and E² − c²B², which appear naturally from tensor contractions. The covariant formulation also provides the foundation for quantum electrodynamics (QED) and all subsequent gauge field theories of particle physics: you promote the 4-potential to a quantum field and the covariance ensures consistency across all observer frames. Electrodynamics is the prototype relativistic field theory.
