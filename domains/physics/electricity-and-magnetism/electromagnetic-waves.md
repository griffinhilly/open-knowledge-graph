---
id: electromagnetic-waves
title: Electromagnetic Waves
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: maxwells-equations-overview
  type: hard
- id: energy-stored-in-fields
  type: soft
- id: ac-power-and-resonance
  type: soft
- id: wave-equation-one-dimensional
  type: hard
- id: wave-equation-pde
  type: hard
tags:
- EM-waves
- speed-of-light
- Poynting-vector
- spectrum
- radiation
stage: formal-systems
status: validated
---
# Electromagnetic Waves

## Core Idea
Maxwell's equations in vacuum predict transverse electromagnetic waves in which oscillating electric and magnetic fields sustain each other, propagating at speed c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s — the speed of light. In an EM wave, E and B are perpendicular to each other and to the direction of propagation, with magnitudes related by E = cB. The Poynting vector S = (1/μ₀) E × B gives the direction and power per unit area (intensity) of the wave. The EM spectrum spans radio waves through gamma rays, all traveling at c in vacuum.

## How It's Best Learned
Derive the wave equation from Maxwell's equations by taking the curl of Faraday's law and substituting Ampère's law. Identify c = 1/√(μ₀ε₀) as the wave speed. Then work problems computing intensity, energy density, and radiation pressure.

## Common Misconceptions
- EM waves require no medium — they propagate in vacuum, unlike mechanical waves.
- E and B are exactly in phase in a traveling EM wave, not 90° out of phase as in a circuit.
- The speed c = 3 × 10⁸ m/s applies in vacuum; in a medium, the wave slows to c/n where n is the refractive index.

## Questions

```yaml
- question: "In a plane electromagnetic wave traveling in the +x direction in vacuum, which of the following correctly describes the orientation of E and B?"
  type: multiple-choice
  options: ["E and B are parallel to each other, both perpendicular to x", "E and B are perpendicular to each other and both perpendicular to x", "E points along x; B is perpendicular to x", "E and B are perpendicular to each other but oscillate 90° out of phase in time"]
  answer: 1
  explanation: "EM waves are transverse: both E and B lie in the plane perpendicular to the propagation direction. They are also perpendicular to each other (their cross product E×B must point along +x, the direction of energy flow). Critically, they oscillate exactly in phase in time — both reach their maxima simultaneously. The 90° out-of-phase option confuses traveling EM waves with inductor behavior in AC circuits."

- question: "In a traveling electromagnetic wave, the electric and magnetic fields are 90° out of phase with each other in time, similar to how voltage and current behave in an AC inductor."
  type: true-false
  answer: false
  explanation: "In a traveling EM wave, E and B are exactly in phase — they reach their maxima, minima, and zero crossings at the same instant and location. The 90° phase relationship applies to inductors in circuits, not to propagating waves. In a standing wave (superposition of two opposing traveling waves), E and B are 90° out of phase in time, which may be the source of this confusion."

- question: "The speed of light is c = 1/√(μ₀ε₀). Explain conceptually why the electric and magnetic constants of free space determine the propagation speed."
  type: short-answer
  answer: "Maxwell's equations couple a changing E field to a B field and vice versa. ε₀ and μ₀ set the strength of these couplings. The wave speed is determined by how quickly each field can drive the other, which is set by these two constants."
  explanation: "ε₀ (permittivity) governs how strongly an electric field responds to its sources; μ₀ (permeability) governs how strongly a magnetic field responds to current. When the curl equations are combined to derive the wave equation, these constants appear together: ∂²E/∂t² = (1/μ₀ε₀)∂²E/∂x². The coefficient 1/μ₀ε₀ is the square of the wave speed, just as in any wave equation of the form ∂²u/∂t² = v²∂²u/∂x². Plugging in the measured values gives c ≈ 3×10⁸ m/s — matching the measured speed of light."
```

## Explainer

From Maxwell's equations you know two key coupling laws: Faraday's law (a changing B field induces an E field) and Ampère's law with displacement current (a changing E field produces a B field). Individually these describe how static or slowly varying fields behave near sources. Together, they create a self-sustaining feedback loop that needs no source at all: a changing E drives a changing B, which drives a changing E, which drives a changing B — propagating outward as a wave. Maxwell realized this in 1865 and predicted the existence of electromagnetic radiation before it was observed.

To derive the wave equation, take the curl of Faraday's law: ∇ × (∇ × E) = −∂(∇ × B)/∂t. Using the vector identity ∇ × (∇ × E) = ∇(∇ · E) − ∇²E and noting ∇ · E = 0 in vacuum (no free charges), the left side simplifies to −∇²E. Substituting Ampère's law on the right gives ∂²E/∂t² = (1/μ₀ε₀)∇²E. You recognize this from wave-equation-pde as a wave equation with speed c = 1/√(μ₀ε₀). When Maxwell computed 1/√(μ₀ε₀) from known electromagnetic constants, he got ≈ 3 × 10⁸ m/s — the measured speed of light. This was his stunning prediction: light itself is an electromagnetic wave.

In a plane wave traveling in the +x direction, both E and B lie in the yz-plane (the wave is transverse), are perpendicular to each other, and oscillate exactly in phase. If E oscillates along ŷ, then B oscillates along ẑ with magnitude B = E/c at every point. The Poynting vector S = (1/μ₀)(E × B) then points along +x with magnitude S = E²/(μ₀c) — the intensity, or power per unit area. Because S is proportional to E², doubling the field amplitude quadruples the intensity. This quadratic relationship between amplitude and power is a general feature of waves.

A persistent confusion comes from circuit analysis: in an inductor, voltage leads current by 90°, which might suggest E and B are 90° out of phase in a wave. They are not — that phase relationship belongs to circuits, not traveling waves. In a standing wave (created by two equal and opposite traveling waves), E and B are 90° out of phase in time, but a standing wave is a superposition of traveling waves, not the fundamental solution. For traveling waves, in phase is the correct description.

The electromagnetic spectrum — radio, microwave, infrared, visible light, ultraviolet, X-ray, gamma ray — represents different frequency (and thus wavelength) ranges of exactly the same phenomenon. All travel at c in vacuum; all have E ⊥ B ⊥ propagation direction; all carry energy via the Poynting vector. In a material with refractive index n, the wave slows to c/n because the oscillating fields interact with bound electrons, effectively reducing the coupling speed. The factor n encodes all the material physics in a single number.
