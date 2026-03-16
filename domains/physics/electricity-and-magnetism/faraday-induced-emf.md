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
- lenz-law
tags:
- faraday-law
- emf
- induction
stage: formal-systems
status: draft
---

# Faraday's Law and Induced EMF

## Core Idea
Faraday's law: ε = −dΦ_B/dt relates induced EMF to the rate of change of magnetic flux. In integral form: ∮ E⃗·d⃗ℓ = −dΦ_B/dt. A changing magnetic flux induces a non-conservative electric field that drives current in a closed loop. This is fundamental to generators, transformers, and induction; the induced field opposes the flux change (Lenz's law).

## Explainer

You already know from studying solenoids that a current-carrying coil creates a magnetic field and that **magnetic flux** Φ_B = ∫ B⃗·dA⃗ measures how much field threads through a surface. Faraday's discovery was the reverse process: a *changing* flux induces an EMF. The word "changing" is crucial — a static magnetic field through a loop, no matter how strong, produces nothing. Only dΦ_B/dt matters. This EMF drives current in a closed loop exactly as a battery would, even though there is no chemical source of energy.

The induced EMF ε = −dΦ_B/dt has a negative sign encoding **Lenz's law**: the induced current flows in the direction that *opposes* the flux change. If flux is increasing, the induced current creates a field opposing the increase; if flux is decreasing, the induced current tries to maintain it. You can think of it as electromagnetic inertia — the system resists changes to its magnetic state. This opposition is not just a curiosity; it is the mechanism that makes generators and brakes work.

What Faraday's law reveals at a deeper level is that a changing magnetic field creates a **non-conservative electric field**. In electrostatics, electric fields point from high to low potential and do zero work around any closed loop. The induced E⃗ is different — it circulates continuously around the loop, doing net work on charges. Written in integral form, ∮ E⃗·d⃗ℓ = −dΦ_B/dt says that the circulation (the line integral of E⃗ around a closed path) equals the rate of flux change. This is a qualitatively new kind of electric field, one with no static analogue.

The practical power of this law is vast. In a generator, a coil rotates in a magnetic field, causing sinusoidal flux variation and therefore sinusoidal EMF — this is how nearly all electrical power is produced. In a transformer, an oscillating primary current creates an oscillating flux in the iron core, which then induces EMF in the secondary coil; the voltage ratio equals the turns ratio. In wireless charging, a time-varying current in a transmitter coil induces current in a receiver coil placed nearby. Every one of these devices is a direct application of ε = −dΦ_B/dt.
