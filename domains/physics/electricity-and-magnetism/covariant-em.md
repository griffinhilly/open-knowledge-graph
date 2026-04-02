---
id: covariant-em
title: Electromagnetic Field Tensor and Special Relativity
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: lorentz-gauge
  type: soft
tags:
- relativity
- four-vectors
- covariance
stage: expert
status: validated
---

# Electromagnetic Field Tensor and Special Relativity

## Core Idea
In special relativity, E and B unify into the electromagnetic field tensor F^μν (rank-2 4-tensor). Lorentz transformations show E and B fields mix: what is purely electric to one observer appears electric plus magnetic to a moving observer. Maxwell's equations take covariant form ∂_μF^μν = J^ν, manifesting relativistic consistency and deep spacetime structure.

## Questions

```yaml
- question: "A positive charge sits at rest in its own reference frame, producing only an electric field. A second observer moves past that charge at high speed. What does the second observer detect?"
  type: multiple-choice
  options:
    - "Only an electric field — the field is the same in all inertial frames"
    - "Both an electric field and a magnetic field"
    - "Only a magnetic field — the moving observer sees the charge as a current"
    - "No field at all — moving observers lose access to static fields"
  answer: 1
  explanation: "Under a Lorentz boost, the components of F^μν mix. The second observer sees the charge as moving — a moving charge is a current — and currents produce magnetic fields. The electric field components also transform. Neither E alone nor B alone is Lorentz-invariant; only the full electromagnetic field tensor F^μν is the genuine relativistic object. Option C is wrong because the electric field does not vanish; option A expresses the pre-relativistic misconception that E and B are separately observer-independent."

- question: "The covariant form of Maxwell's sourced equations is ∂_μF^μν = μ₀J^ν. How many independent scalar equations does this single tensor equation represent?"
  type: multiple-choice
  options:
    - "1 — it is a single equation"
    - "4 — one for each value of the free index ν"
    - "6 — one for each independent component of F^μν"
    - "16 — one for each entry of the 4×4 matrix"
  answer: 1
  explanation: "The free index ν runs over four values (0, 1, 2, 3), so the equation ∂_μF^μν = μ₀J^ν is really four equations. These four equations encode exactly Gauss's law for electricity and Ampère's law with Maxwell's correction — the two sourced Maxwell equations in their vector form. The other two Maxwell equations (Faraday's law and Gauss's law for magnetism) are encoded in the separate Bianchi identity ∂_[μF_νλ] = 0."

- question: "Magnetic forces and electric forces are fundamentally distinct phenomena that can seldom be converted into each other by changing reference frame."
  type: true-false
  answer: false
  explanation: "This is exactly the misconception that covariant electrodynamics refutes. Electric and magnetic fields are frame-dependent components of the same electromagnetic field tensor. A Lorentz boost mixes them: what is purely electric in one frame has both electric and magnetic components in another. The famous example is the magnetic force on a charge moving near a wire — in the wire's rest frame this is a Coulomb force from charge density imbalances due to length contraction. There is one electromagnetic field, viewed from different frames."

- question: "Maxwell published his equations in 1865, and Einstein published special relativity in 1905. This means Maxwell's original equations were inconsistent with special relativity and had to be reformulated."
  type: true-false
  answer: false
  explanation: "Maxwell's equations were already Lorentz-covariant when Maxwell wrote them — they just didn't look obviously covariant in their original vector form. Special relativity was largely motivated by the fact that Newtonian mechanics was inconsistent with Maxwell's equations, not the other way around. The tensor formulation makes the covariance manifest: each side of ∂_μF^μν = μ₀J^ν transforms as the same type of geometric object under Lorentz transformations. Maxwell did not need updating; Newtonian mechanics did."

- question: "The electromagnetic field tensor F^μν is a 4×4 matrix but has only 6 independent components. Why?"
  type: short-answer
  answer: "F^μν is antisymmetric: F^μν = −F^νμ. Antisymmetry forces all diagonal elements to zero (F^μμ = −F^μμ implies F^μμ = 0) and means the lower triangle is just the negative of the upper triangle. A 4×4 antisymmetric matrix therefore has 4×3/2 = 6 independent off-diagonal entries. These 6 components encode exactly the three components of E and the three components of B."
  explanation: "The antisymmetry is not just a mathematical convenience — it encodes the physics that the electromagnetic field has no scalar 'self-interaction' term and that the field strength is purely about differences. Understanding why antisymmetry reduces 16 entries to 6 is key to working fluently with the tensor, and it directly explains why the unified tensor packages the six field components so efficiently."
```

## Explainer

You have mastered Maxwell's equations in differential form and worked with gauge potentials. Now comes the payoff of unification: when you embed electromagnetism in special relativity, the six field components (three for E, three for B) are not independent objects — they are components of a single geometrical object in spacetime. The **electromagnetic field tensor** F^μν is a rank-2 antisymmetric 4-tensor: a 4×4 matrix whose off-diagonal entries encode all six field components. The upper triangle holds the magnetic field components (B_x, B_y, B_z) and the mixed time-space entries hold the electric field components (E_x/c, E_y/c, E_z/c). The antisymmetry F^μν = −F^νμ ensures the diagonal vanishes and reduces the 16 entries to 6 independent ones.

The physical consequence is striking: **E and B are not separately observer-independent quantities**. When you apply a Lorentz boost to F^μν, the transformed tensor mixes E and B components in a precise way. A stationary charge creates a purely electric Coulomb field in its rest frame. To a moving observer, that same charge is moving — it constitutes a current — and a current produces a magnetic field. The "magnetic force" you feel on a test charge moving past a wire is, in the wire's rest frame, a purely electrostatic Coulomb force arising from charge density imbalances due to length contraction. There is no physical distinction between electric and magnetic; there is only the electromagnetic field tensor viewed from different reference frames. This is one of the deepest unifications in physics.

Maxwell's equations also simplify dramatically in this language. The four vector equations collapse into just two tensor equations: ∂_μF^μν = μ₀J^ν encodes Gauss's law and Ampère's law (the equations sourced by charge and current), while ∂_μ(½ε^μναβF_αβ) = 0, or equivalently ∂_[μF_νλ] = 0, encodes Faraday's law and Gauss's law for magnetism (the source-free equations). The Lorentz gauge condition you learned previously takes the manifestly covariant form ∂_μA^μ = 0, and the wave equation for the four-potential becomes simply ∂_μ∂^μ A^ν = μ₀J^ν — a single 4-vector equation replacing four scalar equations.

The deeper lesson is about **covariance**: an equation is Lorentz-covariant if it maintains the same form in all inertial frames. Maxwell's equations in tensor form are manifestly covariant by construction — each side transforms as the same type of tensor object. This is not just aesthetics; it is a proof that electromagnetism is fundamentally relativistic. Maxwell actually published his equations in 1865, forty years before Einstein, yet they were already consistent with special relativity. The formulation you are learning now makes that consistency transparent and provides the geometric language needed for general relativity, quantum field theory, and advanced gravitational physics.
