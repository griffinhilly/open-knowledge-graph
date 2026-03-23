---
id: ampere-maxwell-law
title: Ampère-Maxwell Law and Displacement Current
domain: physics
course: electrodynamics
prerequisites:
- id: amperes-law
  type: hard
- id: electric-field
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- maxwell-equations-differential-form
- electromagnetic-wave-equation
tags:
- ampere-law
- maxwell-correction
- displacement-current
stage: expert
status: validated
---

# Ampère-Maxwell Law and Displacement Current

## Core Idea
Maxwell's crucial addition to Ampère's law—the displacement current term ε₀∂E/∂t—accounts for magnetic fields produced by time-varying electric fields. Without this term, electromagnetic waves are impossible and charge conservation is violated. This modification unifies electricity and magnetism completely and predicts that light is an electromagnetic wave.

## Questions

```yaml
- question: "A capacitor is being charged by a wire carrying current I. An Amperian loop encircles the wire. A flat surface through the wire gives ∮B⃗·dℓ⃗ = μ₀I. The same loop evaluated with a surface passing between the capacitor plates (where no charge flows) gives 0 using the original Ampère's law. What does this inconsistency reveal?"
  type: multiple-choice
  options:
    - "Ampère's law is only valid for steady DC circuits, not transient situations"
    - "The Amperian loop must always be chosen so the surface cuts through a physical current"
    - "The original Ampère's law is incomplete — it is missing a term that accounts for the contribution of the changing electric flux between the plates"
    - "The magnetic field depends on which surface you choose, so the line integral is genuinely ambiguous"
  answer: 2
  explanation: "Ampère's law must give the same result for any surface bounded by the same loop — that is a mathematical requirement (Stokes' theorem). The inconsistency (I vs. 0 for the same loop) reveals that the original law is missing a term. Maxwell's fix: the growing electric field between the plates contributes a 'displacement current' ε₀(dΦ_E/dt) equivalent to the wire current. When this term is added, both surfaces give the same answer. Options A and B describe workarounds that obscure the real issue; option D is mathematically wrong — the same loop must give the same B-field regardless of surface choice."

- question: "Maxwell calculated the speed of electromagnetic waves in vacuum to be 1/√(ε₀μ₀). Why was this result historically decisive?"
  type: multiple-choice
  options:
    - "It proved that electric and magnetic fields propagate at different speeds depending on frequency"
    - "It matched the experimentally measured speed of light, strongly implying that light itself is an electromagnetic wave"
    - "It showed Maxwell's equations were inconsistent with Newtonian mechanics, motivating special relativity"
    - "It provided the first theoretical evidence that a vacuum can support any physical disturbance"
  answer: 1
  explanation: "The numerical coincidence was not a coincidence: 1/√(ε₀μ₀) ≈ 3 × 10⁸ m/s, exactly the measured speed of light. Maxwell concluded that light *is* an electromagnetic wave — a prediction that unified optics with electricity and magnetism. This was one of the most profound unifications in physics. Option C is true historically (Maxwell's equations are Lorentz-covariant, not Galilean-invariant) but was not the *reason* the result was decisive at the time. Option A is wrong; all electromagnetic waves in vacuum propagate at c regardless of frequency."

- question: "Without Maxwell's displacement current correction, applying the original Ampère's law to the same Amperian loop with two different surfaces can yield two different values for the magnetic field — violating the mathematical consistency of Stokes' theorem."
  type: true-false
  answer: true
  explanation: "This was the actual inconsistency Maxwell discovered. Stokes' theorem guarantees that if Ampère's law is valid, then ∮B⃗·dℓ⃗ must equal μ₀ times whatever passes through *any* surface bounded by the loop — the result cannot depend on which surface you choose. In the charging capacitor scenario, one valid surface gives μ₀I and another gives 0. The mathematical inconsistency (not just physical vagueness) is what demanded a correction. The displacement current term ε₀(dΦ_E/dt) restores consistency: it evaluates to I on the surface between the plates, making both surfaces agree."

- question: "Displacement current requires the physical flow of electric charge between the capacitor plates."
  type: true-false
  answer: false
  explanation: "This is a persistent misconception, partly due to the name 'displacement current,' which was historical and somewhat misleading. No actual charge flows between the capacitor plates in a standard dielectric capacitor — that is the whole point of the capacitor gap. What *does* change is the electric flux (ε₀dΦ_E/dt) as the electric field between the plates grows. Maxwell's insight is that this changing electric flux acts magnetically *just as* a real current would — generating a circulating magnetic field — even though no charge is moving. The 'displacement' refers historically to the displacement of polarization charges in a dielectric, but the effect is general."

- question: "Explain why the displacement current term ε₀∂E/∂t was necessary to complete Ampère's law. What physical phenomenon does this term represent, and what would be impossible without it?"
  type: short-answer
  answer: "The original Ampère's law was mathematically inconsistent for time-varying situations: the same Amperian loop could yield different magnetic field values depending on which bounding surface you used. Maxwell's fix adds ε₀(dΦ_E/dt) to represent the fact that a time-varying electric field generates a magnetic field, even without physical charge flow. Physically, this term says that the growing E field between capacitor plates is magnetically equivalent to the current in the wire. Without it: (1) the law is mathematically inconsistent, and (2) the feedback loop with Faraday's law (changing B generates E; changing E generates B) cannot form — so electromagnetic waves cannot exist, and light cannot be identified as an electromagnetic phenomenon."
  explanation: "The displacement current is the lynchpin of classical electrodynamics. It completes the symmetry between E and B: Faraday says dB/dt → E; the amended Ampère says dE/dt → B. This mutual induction is what allows electromagnetic disturbances to propagate as self-sustaining waves through empty space. Without displacement current, Maxwell's equations would be incomplete and inconsistent, the wave equation for light could not be derived, and the unification of electricity, magnetism, and optics would not exist."
```

## Explainer

You know Ampère's law: ∮ B⃗·d⃗ℓ = μ₀I_enc. This says a magnetic field circulates around any current. The problem Maxwell discovered in 1865 was that this law is internally inconsistent for time-varying situations. Consider a capacitor charging: current flows in the wires, but no actual charge flows between the plates. Draw an Amperian loop around the wire — one surface cut by the wire gives I_enc = I, predicting a magnetic field. But deform that surface to pass between the capacitor plates — no current crosses it, so I_enc = 0, predicting no magnetic field. The same loop, the same magnetic field, two different answers. Something is missing.

The fix is **displacement current**: even though no real charge flows between the plates, the electric field between them is growing as the capacitor charges. Maxwell recognized that a time-varying electric field must produce a magnetic field just as a real current does. He added the term ε₀∂E/∂t to the right side of Ampère's law: ∮ B⃗·d⃗ℓ = μ₀(I_enc + ε₀ dΦ_E/dt). Now the surface between the capacitor plates contributes via the growing electric flux, and both surfaces give the same answer. The inconsistency disappears. The term is called displacement current because it was historically associated with displacement of charge in dielectrics, but the physics is that a changing E field generates a circulating B field, whether or not physical charge is involved.

The deeper consequence is transformative. You already know from Faraday's law that a changing magnetic field induces an electric field: ∮ E⃗·d⃗ℓ = -dΦ_B/dt. The amended Ampère's law says the reverse is also true: a changing electric field induces a magnetic field. These two laws form a feedback loop. Suppose you create an oscillating electric field in some region of space. It produces an oscillating magnetic field nearby. That oscillating magnetic field produces an oscillating electric field a little further out. And so on — the disturbance propagates outward through empty space as a self-sustaining electromagnetic wave. The wave speed works out to 1/√(ε₀μ₀), which Maxwell computed to be approximately 3 × 10⁸ m/s — the measured speed of light. The conclusion was unavoidable: **light is an electromagnetic wave**.

This one modification, ε₀∂E/∂t, is the linchpin that completes Maxwell's equations and unifies electricity, magnetism, and optics. Without it, charge conservation would be violated and electromagnetic waves could not exist. With it, everything from radio transmitters to fiber-optic cables to the photoelectric effect traces back to this single correction that Maxwell made to reconcile a mathematical inconsistency in Ampère's law.
