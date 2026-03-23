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
stage: expert
status: validated
---

# Lorentz Covariance of Maxwell's Equations

## Core Idea
Maxwell's equations have the same form in all inertial reference frames—a fundamental requirement of special relativity. This Lorentz covariance is automatic when expressed in terms of 4-vectors and tensors in spacetime, revealing that electrodynamics is inherently relativistic. The covariant formulation unifies space and time, electric and magnetic fields, and provides the foundation for relativistic quantum field theory.

## Questions

```yaml
- question: "An observer at rest sees a stationary point charge producing a pure electric field with no magnetic field. A second observer moves at constant velocity relative to the first. What does the moving observer measure?"
  type: multiple-choice
  options:
    - "The same pure electric field — the field is a physical object that cannot change based on observer motion"
    - "No fields at all — in the moving frame, the charge is at a different position so its effects cancel"
    - "A combination of electric and magnetic fields — the moving charge appears as a current, and E and B mix under Lorentz boosts"
    - "A pure magnetic field — velocity converts electric fields to magnetic fields completely"
  answer: 2
  explanation: "This is the central physical insight of Lorentz covariance: E⃗ and B⃗ are not separately invariant quantities; they mix under Lorentz boosts just as space and time coordinates mix. The moving observer sees the charge as moving — a moving charge is a current — so a magnetic field appears. Neither observer is wrong; they are both making correct measurements in their own inertial frames. This is precisely why the electromagnetic field tensor F^μν is necessary: it packages all six field components together so the transformation law is clean."

- question: "What does it mean to say that Maxwell's equations are 'Lorentz covariant'?"
  type: multiple-choice
  options:
    - "The speed of light is the same in all inertial frames, so Maxwell's equations must involve c"
    - "Maxwell's equations take the same mathematical form in every inertial reference frame, so no frame is privileged"
    - "Maxwell's equations were derived assuming a stationary ether, and Lorentz showed how to correct them for moving frames"
    - "The electromagnetic fields E⃗ and B⃗ are unchanged (invariant) under Lorentz transformations"
  answer: 1
  explanation: "Covariance means the equations preserve their form under Lorentz transformations — not that the fields themselves are unchanged (they are not invariant; they transform). Option C is historically backwards: Maxwell's equations needed no correction, unlike Newtonian mechanics. Option D confuses covariance (same form) with invariance (same value). The equations ∂_μ F^μν = J^ν and ∂_[μ F_νλ] = 0 are manifestly covariant because every index is contracted according to consistent tensor rules."

- question: "Maxwell's equations required modification when special relativity was developed, just as Newton's laws required modification."
  type: true-false
  answer: false
  explanation: "This is historically and physically backwards. Maxwell's equations were already exactly relativistic — they did not need modification. It was *Newtonian mechanics* that required modification (giving way to relativistic mechanics). Einstein's 1905 paper started from Maxwell's equations as correct and reconstructed kinematics around them. The Lorentz transformations were originally derived to find the symmetry group of Maxwell's equations, not the other way around. This is why the paper was titled 'On the Electrodynamics of Moving Bodies.'"

- question: "Under a Lorentz boost, a pure electric field in one inertial frame becomes a mixture of electric and magnetic field components in another frame."
  type: true-false
  answer: true
  explanation: "This is one of the key physical consequences of Lorentz covariance. E⃗ and B⃗ are not independently Lorentz-invariant; they transform into each other under boosts. This is why the electromagnetic field tensor F^μν, which packages all six field components together, is the natural object in relativistic electrodynamics. Two relativistic invariants — E⃗·B⃗ and E²−c²B² — remain unchanged across frames, but the individual E⃗ and B⃗ vectors generally do not."

- question: "Why does packaging the electric and magnetic fields into the electromagnetic field tensor F^μν make Lorentz covariance manifest, while treating them as separate 3-vectors obscures it?"
  type: short-answer
  answer: "In 3D notation, E⃗ and B⃗ appear as separate objects with separate transformation laws that only mix correctly if you apply the right formulas. In 4D tensor notation, F^μν is a single rank-2 tensor that transforms automatically under Lorentz transformations via the standard tensor rule: F'^μν = Λ^μ_α Λ^ν_β F^αβ. Maxwell's equations written as ∂_μ F^μν = μ₀J^ν have all indices contracted, which by the rules of tensor calculus guarantees the equation holds in all frames simultaneously. No separate frame-by-frame verification is needed. The covariance is 'manifest' because it is built into the notation: a properly contracted tensor equation is automatically Lorentz covariant."
  explanation: "This is the payoff of the 4D formalism. The 3D equations hide the relativistic structure; the 4D equations reveal it. The same logic applies throughout modern physics: gauge theories, general relativity, and quantum field theory all use tensor/spinor notation precisely because it makes symmetry properties manifest rather than requiring case-by-case verification."
```

## Explainer

From your study of special relativity, you know that the laws of physics must take the same form in all inertial reference frames — this is the principle of relativity. From your study of Maxwell's equations in differential form, you have four equations relating E⃗ and B⃗ to their sources. A profound historical question is whether Maxwell's equations obey special relativity, or need correction. The answer is that Maxwell's equations are already exactly relativistic — no modification is needed. In fact, Einstein's 1905 paper was titled "On the Electrodynamics of Moving Bodies" precisely because the tension between classical mechanics and Maxwell's equations forced him to reconcile them through special relativity, not the other way around. **Lorentz covariance** is the precise statement that the equations transform correctly under Lorentz transformations, maintaining the same form in every inertial frame.

To see this concretely, consider what happens when you boost to a different frame. In your original frame, you might see a purely static electric field (say, from a stationary charge). An observer moving relative to you sees the same charge moving — a moving charge is a current, and a current produces a magnetic field. So what you call a pure electric field, the moving observer sees as a combination of electric and magnetic fields. The E⃗ and B⃗ fields are not separately Lorentz-invariant: they **mix** under boosts, exactly as space and time coordinates mix. The deeper structure is the **electromagnetic field tensor** F^μν — a 4×4 antisymmetric tensor that packages all six components of E⃗ and B⃗ together. Under a Lorentz transformation, F^μν transforms as a proper rank-2 tensor, and Maxwell's equations, written as ∂_μ F^μν = J^ν (where J^μ is the 4-current), are manifestly covariant — every index is contracted, making the equation frame-independent.

The covariant formulation also unifies the sources. In 3D, charge density ρ and current density J⃗ appear as separate objects. In 4D spacetime, they combine into a single **4-current** J^μ = (cρ, J⃗), which transforms as a 4-vector under boosts. Similarly, the scalar and vector potentials φ and A⃗ unify into the **4-potential** A^μ = (φ/c, A⃗). The field tensor is then F^μν = ∂^μ A^ν − ∂^ν A^μ, a clean geometric statement. Maxwell's equations reduce to two tensor equations: ∂_μ F^μν = μ₀J^ν and ∂_[μ F_νλ] = 0 (the Bianchi identity), each manifestly Lorentz-covariant.

This covariant framework is not merely aesthetic elegance — it is computationally essential. When you need to find the fields of a moving charge or transform fields between frames, the tensor transformation rules give the answer directly. The relativistic invariants of the field — quantities unchanged by boosts — are E·B and E² − c²B², which appear naturally from tensor contractions. The covariant formulation also provides the foundation for quantum electrodynamics (QED) and all subsequent gauge field theories of particle physics: you promote the 4-potential to a quantum field and the covariance ensures consistency across all observer frames. Electrodynamics is the prototype relativistic field theory.
