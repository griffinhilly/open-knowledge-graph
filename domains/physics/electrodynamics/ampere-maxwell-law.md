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
stage: advanced
status: draft
---

# Ampère-Maxwell Law and Displacement Current

## Core Idea
Maxwell's crucial addition to Ampère's law—the displacement current term ε₀∂E/∂t—accounts for magnetic fields produced by time-varying electric fields. Without this term, electromagnetic waves are impossible and charge conservation is violated. This modification unifies electricity and magnetism completely and predicts that light is an electromagnetic wave.

## Explainer

You know Ampère's law: ∮ B⃗·d⃗ℓ = μ₀I_enc. This says a magnetic field circulates around any current. The problem Maxwell discovered in 1865 was that this law is internally inconsistent for time-varying situations. Consider a capacitor charging: current flows in the wires, but no actual charge flows between the plates. Draw an Amperian loop around the wire — one surface cut by the wire gives I_enc = I, predicting a magnetic field. But deform that surface to pass between the capacitor plates — no current crosses it, so I_enc = 0, predicting no magnetic field. The same loop, the same magnetic field, two different answers. Something is missing.

The fix is **displacement current**: even though no real charge flows between the plates, the electric field between them is growing as the capacitor charges. Maxwell recognized that a time-varying electric field must produce a magnetic field just as a real current does. He added the term ε₀∂E/∂t to the right side of Ampère's law: ∮ B⃗·d⃗ℓ = μ₀(I_enc + ε₀ dΦ_E/dt). Now the surface between the capacitor plates contributes via the growing electric flux, and both surfaces give the same answer. The inconsistency disappears. The term is called displacement current because it was historically associated with displacement of charge in dielectrics, but the physics is that a changing E field generates a circulating B field, whether or not physical charge is involved.

The deeper consequence is transformative. You already know from Faraday's law that a changing magnetic field induces an electric field: ∮ E⃗·d⃗ℓ = -dΦ_B/dt. The amended Ampère's law says the reverse is also true: a changing electric field induces a magnetic field. These two laws form a feedback loop. Suppose you create an oscillating electric field in some region of space. It produces an oscillating magnetic field nearby. That oscillating magnetic field produces an oscillating electric field a little further out. And so on — the disturbance propagates outward through empty space as a self-sustaining electromagnetic wave. The wave speed works out to 1/√(ε₀μ₀), which Maxwell computed to be approximately 3 × 10⁸ m/s — the measured speed of light. The conclusion was unavoidable: **light is an electromagnetic wave**.

This one modification, ε₀∂E/∂t, is the linchpin that completes Maxwell's equations and unifies electricity, magnetism, and optics. Without it, charge conservation would be violated and electromagnetic waves could not exist. With it, everything from radio transmitters to fiber-optic cables to the photoelectric effect traces back to this single correction that Maxwell made to reconcile a mathematical inconsistency in Ampère's law.
