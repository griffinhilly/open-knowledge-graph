---
id: displacement-current-and-maxwell
title: Displacement Current and Maxwell's Equations
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faraday-law-of-induction
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- maxwells-equations-differential-form
- electromagnetic-wave-equation
tags:
- maxwell-equations
- displacement-current
- symmetry
stage: formal-systems
status: validated
---

# Displacement Current and Maxwell's Equations

## Core Idea
Maxwell added the displacement current term ε₀∂E/∂t to Ampère's law, creating beautiful symmetry where changing E produces B just as changing B produces E. This correction was essential for predicting electromagnetic waves and ensuring current continuity.

## Questions

```yaml
- question: "Maxwell added the displacement current term ε₀∂E/∂t to Ampère's law primarily because:"
  type: multiple-choice
  options:
    - "Experiments had directly measured this new form of current flowing through capacitor gaps"
    - "Applying Ampère's original law to a charging capacitor produced a mathematical inconsistency — different surfaces bounded by the same loop gave different results"
    - "Faraday's law required a symmetric partner to conserve electromagnetic energy"
    - "He needed an additional term to correctly calculate the force on a moving charge"
  answer: 1
  explanation: "The problem was mathematical consistency, not experimental discovery. Applying Ampère's law ∮B·dl = μ₀I_enc to a loop around a wire feeding a capacitor: if you choose a surface cutting the wire, I_enc is nonzero; if you choose a surface through the gap between plates, no charge crosses it, giving I_enc = 0. The same integral cannot equal two different things. Maxwell's displacement current resolves this: ε₀∂E/∂t in the gap acts as an effective current density, making the result consistent for any surface choice. The experimental confirmation came later through electromagnetic wave predictions."

- question: "The displacement current in a charging capacitor gap is best described as:"
  type: multiple-choice
  options:
    - "A real flow of electrons tunneling through the dielectric between the plates"
    - "An effective current arising from the changing electric field, with no actual charge motion through the gap"
    - "A magnetic field that mimics the effect of conventional current in Ampère's law"
    - "A polarization current in the dielectric material that stores energy"
  answer: 1
  explanation: "No charge crosses the gap between capacitor plates — the displacement current is not a flow of electrons. It is the term ε₀∂E/∂t, which has the units of current density and produces a magnetic field exactly as if a real current were present. Maxwell postulated it to maintain mathematical consistency in Ampère's law. This is a conceptual distinction with deep implications: the 'current' is the rate of change of electric flux, not charge transport."

- question: "Maxwell's addition of the displacement current created a symmetric relationship: just as Faraday showed that a changing B field produces a circulating E field, the displacement current shows that a changing E field produces a circulating B field."
  type: true-false
  answer: true
  explanation: "This symmetry is the deep insight. Faraday's law: ∇ × E⃗ = −∂B⃗/∂t. Modified Ampère's law: ∇ × B⃗ = μ₀J⃗ + μ₀ε₀∂E⃗/∂t. In free space (J⃗ = 0), the two laws are mirrors: changing B drives circulating E, and changing E drives circulating B. This mutual induction between the two fields is what produces self-sustaining electromagnetic waves."

- question: "The displacement current was confirmed by direct experimental measurement before Maxwell included it in his equations."
  type: true-false
  answer: false
  explanation: "Maxwell added the displacement current term purely for reasons of mathematical consistency — it was a theoretical postulate, not an experimental discovery. The experimental confirmation came indirectly: the modified equations predicted electromagnetic waves traveling at speed 1/√(μ₀ε₀) ≈ 3×10⁸ m/s, matching the known speed of light. Hertz's experiments (1887) directly confirmed electromagnetic waves. The displacement current was justified after the fact by the enormous predictive success of the complete Maxwell equations."

- question: "Why did Maxwell's addition of the displacement current term lead to the prediction that light is an electromagnetic wave?"
  type: short-answer
  answer: "With both Faraday's law (∇ × E⃗ = −∂B⃗/∂t) and the modified Ampère's law (∇ × B⃗ = μ₀ε₀∂E⃗/∂t in free space), you can take the curl of one equation and substitute the other. This produces the wave equation ∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t², whose solutions are waves traveling at speed v = 1/√(μ₀ε₀). Plugging in the known electromagnetic constants gives v ≈ 3×10⁸ m/s — exactly the measured speed of light, revealing that light is an electromagnetic wave."
  explanation: "Without the displacement current term, no such wave equation emerges — the system is inconsistent and the fields cannot propagate in vacuum. The displacement current is what 'closes the loop': E changing drives B, B changing drives E, and the result is a self-reinforcing wave that can travel through empty space at the speed of light."
```

## Explainer

By the 1860s, three of Maxwell's four equations were established: Gauss's laws for electric and magnetic fields, and Faraday's law linking a changing B⃗ to a circulating E⃗. Ampère's law linked a circulating B⃗ to steady currents. The problem: when you apply Ampère's law to the gap between the plates of a charging capacitor, no conventional current crosses that gap — yet a magnetic field clearly exists there by continuity arguments. The law was inconsistent.

Maxwell's solution was to notice that while no charge crosses the gap, the electric field in the gap is changing as the capacitor charges. He postulated that a **displacement current** ε₀∂E/∂t should generate a magnetic field just as a real current does. Adding this term to Ampère's law — ∇ × B⃗ = μ₀J⃗ + μ₀ε₀∂E⃗/∂t — fixed the inconsistency. The modification created a profound symmetry: Faraday had shown that ∂B/∂t drives circulating E⃗; now Maxwell showed that ∂E/∂t drives circulating B⃗. The two laws became mirrors of each other.

The consequences were revolutionary. Taking the curl of the modified Faraday and Ampère laws and substituting one into the other produces the **electromagnetic wave equation**: ∇²E⃗ = μ₀ε₀∂²E⃗/∂t². This is a wave equation with speed v = 1/√(μ₀ε₀). Plugging in the known constants gives v ≈ 3×10⁸ m/s — exactly the measured speed of light. Maxwell concluded that light itself is an electromagnetic wave. This was arguably the greatest unification in 19th-century physics: optics, electricity, and magnetism were revealed as one.

The displacement current also resolves the capacitor paradox completely. In the gap between capacitor plates, ε₀∂E/∂t acts as an effective current density equal to the conduction current density in the wires feeding the plates. Ampère's law, applied to any surface bounded by the same loop around the wire, gives the same B⃗ regardless of whether you choose a surface that intersects the wire (where J⃗ is nonzero) or one that passes through the gap (where ∂E/∂t is nonzero). The physics is consistent, and a crucial lesson about mathematical self-consistency in physics is illustrated: when a law breaks down at a boundary case, the violation points toward a deeper truth.
