---
id: faraday-induced-emf
title: Faraday's Law and Induced EMF
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-solenoid
  type: soft
builds-toward:
- motional-emf
- lenzs-law
tags:
- faraday-law
- emf
- induction
stage: formal-systems
status: validated
---

# Faraday's Law and Induced EMF

## Core Idea
Faraday's law: ε = −dΦ_B/dt relates induced EMF to the rate of change of magnetic flux. In integral form: ∮ E⃗·d⃗ℓ = −dΦ_B/dt. A changing magnetic flux induces a non-conservative electric field that drives current in a closed loop. This is fundamental to generators, transformers, and induction; the induced field opposes the flux change (Lenz's law).

## Questions

```yaml
- question: "A strong permanent magnet is held perfectly still inside a closed copper loop. A student predicts this will generate a continuous current. What is wrong with this prediction?"
  type: multiple-choice
  options:
    - "Copper is not ferromagnetic, so it cannot respond to a static magnetic field"
    - "A static magnetic field produces zero induced EMF — only a changing flux can drive current"
    - "The loop would need multiple turns of wire for any induction to occur"
    - "The magnet must be oriented so its poles are perpendicular to the loop's plane"
  answer: 1
  explanation: "Faraday's law states ε = −dΦ_B/dt. A stationary magnet produces a constant flux through the loop, so dΦ_B/dt = 0 and therefore ε = 0 — regardless of field strength. It is the rate of change of flux that matters, not the flux itself. This is the central insight of Faraday's law and the most common point of confusion: a powerful static field does nothing."

- question: "What does the negative sign in ε = −dΦ_B/dt encode?"
  type: multiple-choice
  options:
    - "That EMF has a negative value when measured in standard SI units"
    - "That the induced current flows in a direction that opposes the flux change producing it"
    - "That the formula applies only when magnetic flux is decreasing"
    - "That the induced electric field points opposite to the magnetic field direction"
  answer: 1
  explanation: "The negative sign encodes Lenz's law: the induced current creates its own magnetic field that opposes whatever change in flux caused the induction. If flux through a loop is increasing, the induced current creates a field opposing the increase; if flux is decreasing, the induced current tries to sustain it. This 'electromagnetic inertia' is not a curiosity — it is the mechanism behind regenerative braking and transformer operation."

- question: "A very strong but perfectly stationary magnetic field through a loop will induce a larger EMF than a weak but rapidly changing field through the same loop."
  type: true-false
  answer: false
  explanation: "EMF is determined by dΦ_B/dt — the rate of change of flux — not by the magnitude of the flux or field. A strong static field has dΦ_B/dt = 0, so it induces zero EMF. A weak but rapidly oscillating field can produce a large dΦ_B/dt and therefore a large EMF. Field strength matters only insofar as it contributes to how quickly flux changes."

- question: "The electric field induced by Faraday's law is non-conservative — it can do net work on a charge carried around a closed loop."
  type: true-false
  answer: true
  explanation: "Electrostatic fields are conservative: they do zero net work around any closed path (∮E⃗·dℓ⃗ = 0). The induced electric field arising from a changing magnetic flux is fundamentally different: ∮E⃗·dℓ⃗ = −dΦ_B/dt ≠ 0. This circulating field can continuously accelerate charges around a loop — exactly what a battery does with chemical energy, but here achieved through electromagnetic induction."

- question: "Why does a rotating coil in a steady magnetic field produce alternating current rather than direct current?"
  type: short-answer
  answer: "As the coil rotates, the angle between the magnetic field and the coil's normal changes continuously. The flux through the coil is Φ_B = BA cos(θ), where θ = ωt. Differentiating, dΦ_B/dt = −BAω sin(ωt), so the induced EMF ε = BAω sin(ωt) oscillates sinusoidally — positive for half a rotation, negative for the other half. This sign reversal every half-cycle is what makes the output alternating current."
  explanation: "The sinusoidal variation arises because the projection of the coil area onto the field direction varies as cos(ωt). To produce DC, a commutator can be used to flip the external connection every half-cycle, always presenting the positive half of the EMF waveform to the external circuit — this is how DC generators work."
```

## Explainer

You already know from studying solenoids that a current-carrying coil creates a magnetic field and that **magnetic flux** Φ_B = ∫ B⃗·dA⃗ measures how much field threads through a surface. Faraday's discovery was the reverse process: a *changing* flux induces an EMF. The word "changing" is crucial — a static magnetic field through a loop, no matter how strong, produces nothing. Only dΦ_B/dt matters. This EMF drives current in a closed loop exactly as a battery would, even though there is no chemical source of energy.

The induced EMF ε = −dΦ_B/dt has a negative sign encoding **Lenz's law**: the induced current flows in the direction that *opposes* the flux change. If flux is increasing, the induced current creates a field opposing the increase; if flux is decreasing, the induced current tries to maintain it. You can think of it as electromagnetic inertia — the system resists changes to its magnetic state. This opposition is not just a curiosity; it is the mechanism that makes generators and brakes work.

What Faraday's law reveals at a deeper level is that a changing magnetic field creates a **non-conservative electric field**. In electrostatics, electric fields point from high to low potential and do zero work around any closed loop. The induced E⃗ is different — it circulates continuously around the loop, doing net work on charges. Written in integral form, ∮ E⃗·d⃗ℓ = −dΦ_B/dt says that the circulation (the line integral of E⃗ around a closed path) equals the rate of flux change. This is a qualitatively new kind of electric field, one with no static analogue.

The practical power of this law is vast. In a generator, a coil rotates in a magnetic field, causing sinusoidal flux variation and therefore sinusoidal EMF — this is how nearly all electrical power is produced. In a transformer, an oscillating primary current creates an oscillating flux in the iron core, which then induces EMF in the secondary coil; the voltage ratio equals the turns ratio. In wireless charging, a time-varying current in a transmitter coil induces current in a receiver coil placed nearby. Every one of these devices is a direct application of ε = −dΦ_B/dt.
