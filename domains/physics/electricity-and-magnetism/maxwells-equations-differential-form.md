---
id: maxwells-equations-differential-form
title: Maxwell's Equations in Differential Form
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: displacement-current-and-maxwell
  type: hard
- id: partial-derivatives
  type: hard
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- electromagnetic-wave-equation
- conservation-laws-em
- maxwells-equations-integral-form
tags:
- maxwell-equations
- field-theory
- divergence-curl
stage: formal-systems
status: validated
---

# Maxwell's Equations in Differential Form

## Core Idea
Maxwell's four equations in differential form are: ∇·E = ρ/ε₀, ∇·B = 0, ∇×E = -∂B/∂t, and ∇×B = μ₀J + μ₀ε₀∂E/∂t. These are the fundamental equations governing all classical electromagnetic phenomena.

## Questions

```yaml
- question: "The equation ∇·B = 0 holds everywhere in space. What does this imply about magnetic fields?"
  type: multiple-choice
  options:
    - "Magnetic fields are zero in a vacuum with no current sources"
    - "Magnetic monopoles do not exist — magnetic field lines never begin or end at any point, so they always form closed loops"
    - "Magnetic fields only exist near electric currents or permanent magnets"
    - "The divergence of B is zero only far from any current source, approaching zero asymptotically"
  answer: 1
  explanation: "∇·B = 0 holds everywhere — this is what makes it a fundamental local equation of electromagnetism. Divergence measures whether field lines begin or end at a point. ∇·B = 0 means B field lines never start or terminate anywhere, which forces them to always form closed loops. This is the mathematical statement of the absence of magnetic monopoles — there are no isolated magnetic charges analogous to electric charges. No magnetic monopole has ever been observed, consistent with this equation."

- question: "Before Maxwell added the displacement current term μ₀ε₀∂E/∂t to Ampère's law, Ampère's law was inconsistent for time-varying fields. The displacement current was needed to:"
  type: multiple-choice
  options:
    - "Ensure Ampère's law gives the same result as Gauss's law in electrostatic situations"
    - "Mathematically resolve the inconsistency and enable prediction of electromagnetic waves propagating at the speed of light"
    - "Account for the polarization of dielectric materials in the presence of electric fields"
    - "Describe how changing magnetic fields drive currents in conductors, as in Faraday's law"
  answer: 1
  explanation: "Maxwell's displacement current was a theoretical insight, not an empirical discovery. Without it, taking the divergence of ∇×B = μ₀J yields a contradiction in time-varying situations. With it, the equations become self-consistent, and combining Faraday's law and the modified Ampère's law in vacuum yields a wave equation with speed c = 1/√(μ₀ε₀). When Maxwell found this equaled the measured speed of light, it demonstrated that light is an electromagnetic wave — unifying electricity, magnetism, and optics in a single framework."

- question: "The differential form of Maxwell's equations and their integral form describe the same physical content — they are mathematically equivalent via the divergence theorem and Stokes' theorem."
  type: true-false
  answer: true
  explanation: "The integral and differential forms encode identical physics. The divergence theorem converts ∇·E = ρ/ε₀ to Gauss's law in integral form (surface integrals of E equal enclosed charge); Stokes' theorem converts the curl equations to their integral loop forms. The differential form is often more useful because it holds pointwise at every location in space, avoiding the need to choose specific surfaces or loops. The integral form is convenient when symmetry simplifies the integrals. Neither contains information absent from the other."

- question: "In Faraday's law ∇×E = −∂B/∂t, the negative sign is a convention with no physical consequence — the sign could be positive without changing observable predictions."
  type: true-false
  answer: false
  explanation: "The negative sign encodes Lenz's law, which has direct and observable physical significance. It means the induced electric field circulates in a direction that opposes the change in magnetic flux. If B is increasing in a given direction, the induced E curls so that if it drove current in a conducting loop, that current would produce a magnetic field opposing the increase. Remove the negative sign and electromagnetic feedback becomes destabilizing rather than self-limiting — generators, transformers, and virtually all electromagnetic induction devices depend on this sign for their correct behavior."

- question: "What is the physical significance of the displacement current term μ₀ε₀∂E/∂t in Ampère's law, and why was its addition a landmark in physics?"
  type: short-answer
  answer: "The displacement current says that a time-varying electric field generates a circulating magnetic field, even in the absence of any actual moving charges. Physically, this completes the symmetry between E and B: Faraday's law says changing B creates circulating E; Maxwell's addition says changing E creates circulating B. This mutual generation allows each field to sustain the other, enabling self-propagating electromagnetic waves. When Maxwell combined Faraday and the modified Ampère in vacuum to derive a wave equation, its speed c = 1/√(μ₀ε₀) matched the measured speed of light — proving light is an electromagnetic wave and unifying three previously separate fields of physics."
  explanation: "The displacement current is invisible (no real charges move through a capacitor gap, yet a magnetic field circulates around it), which is why it required theoretical rather than experimental discovery. It exemplifies how mathematical self-consistency requirements can lead to genuine physical insight. Without it, Maxwell's equations are internally inconsistent for time-varying fields; with it, they predict the entire spectrum of electromagnetic radiation."
```

## Explainer

You already know the divergence and curl operators from multivariable calculus, and you've seen **Maxwell's equations** assembled with the displacement current term. The differential form is the most powerful version because it holds at every point in space, not just in integral form over chosen surfaces and loops. Understanding what each equation says locally is the key to reading the physics directly from the mathematics.

**∇·E = ρ/ε₀** is Gauss's law in differential form. The divergence of E at a point equals the local charge density divided by ε₀. Wherever charge density is zero, field lines don't begin or end — they pass through. Wherever ρ ≠ 0, field lines either emanate outward (positive charge) or converge inward (negative charge). **∇·B = 0** says the divergence of B is always zero: magnetic field lines never begin or end anywhere. There are no magnetic monopoles; every field line forms a closed loop. These two divergence equations describe the *sources* of the fields.

The two curl equations describe how changing fields generate each other. **∇×E = −∂B/∂t** is Faraday's law: a time-varying magnetic field creates a circulating electric field. The negative sign (Lenz's law) means the induced E opposes the change in B — if B is increasing into the page, the induced E curls counterclockwise when viewed from the front. **∇×B = μ₀J + μ₀ε₀∂E/∂t** is Ampère's law with Maxwell's displacement current correction: both real current density J and a time-varying electric field ∂E/∂t produce circulating magnetic fields. The displacement current term μ₀ε₀∂E/∂t was Maxwell's crucial insight — without it, Ampère's law is inconsistent for time-varying fields, and electromagnetic waves cannot exist.

Together, the four equations unify electricity and magnetism completely. In vacuum (ρ = 0, J = 0), combining Faraday and Ampère gives ∇×(∇×E) = −μ₀ε₀∂²E/∂t², which simplifies using ∇·E = 0 to ∇²E = μ₀ε₀∂²E/∂t². This is a wave equation with propagation speed c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s — the speed of light. The fact that this constant equaled the measured speed of light was, to Maxwell, definitive proof that light is an electromagnetic wave. All of classical electrodynamics, optics, and radio propagation follows from these four compact equations.
