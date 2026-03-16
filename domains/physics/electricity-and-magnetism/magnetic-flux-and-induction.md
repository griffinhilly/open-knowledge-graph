---
id: magnetic-flux-and-induction
title: Magnetic Flux and Electromagnetic Induction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: electric-flux
  type: soft
- id: flux-integrals
  type: soft
- id: amperes-law
  type: soft
- id: biot-savart-law
  type: soft
builds-toward:
- faradays-law
tags:
- magnetic-flux
- induction
- Faraday
- EMF
stage: formal-systems
status: validated
---
# Magnetic Flux and Electromagnetic Induction

## Core Idea
Magnetic flux Φ_B through a surface is Φ_B = ∫ B · dA, measured in webers (Wb = T·m²). Electromagnetic induction is the phenomenon by which a changing magnetic flux through a conductor induces an electromotive force (EMF) and, if the circuit is closed, an electric current. Faraday discovered that changing B, changing area, or changing the angle between B and the surface all produce an induced EMF. This is the foundation of generators, transformers, and induction motors.

## How It's Best Learned
Build intuition through qualitative experiments: pushing a bar magnet into a coil and observing the induced current direction. Then quantify using Faraday's law. Distinguish clearly between the motional EMF from a moving conductor and the induced EMF from a time-varying B field.

## Common Misconceptions
- It is the change in flux, not flux itself, that induces an EMF.
- A stationary coil in a static magnetic field produces no EMF, even if B is very large.
- The induced EMF drives current around a loop; the EMF itself is not a force but an energy per unit charge.

## Explainer

You already know **magnetic field** lines — curves that show the direction and relative strength of B through a region of space. **Magnetic flux** Φ_B = ∫ B · dA is the precise measure of "how much field passes through a surface": the integral of the component of B perpendicular to the surface, summed over its area. If you've worked with electric flux, the definition is identical — the dot product selects the normal component, so flux depends on both field strength and the orientation of the surface. A loop tilted parallel to B has zero flux through it; tilted perpendicular, it captures the maximum. Flux is measured in webers: 1 Wb = 1 T·m².

The discovery Faraday made — and that makes flux important — is that a **changing** flux through a conducting loop drives an **electromotive force** (EMF) around that loop. If the loop is closed, this EMF pushes current around the circuit; if it's open, a voltage appears across the gap. The key word is *changing*. A steady magnetic field, no matter how large, does nothing to the loop if B isn't changing. You can have a 10-tesla MRI magnet sitting next to a copper ring forever with no current — but the instant you change B (or move the ring, or rotate it), flux changes and current flows.

There are three geometrically distinct ways to change flux: change the magnitude of B (time-varying field), change the area enclosed by the loop (a moving conductor), or change the angle between B and the loop (rotation, as in an electric generator). All three cases produce an EMF, and all are captured by the single formula ε = −dΦ_B/dt (Faraday's law). The negative sign reflects Lenz's law: the induced EMF always opposes the change that created it — the induced current creates a magnetic field that tries to maintain the original flux. Lenz's law is a consequence of energy conservation; if the induced current reinforced the change instead of opposing it, you'd have a perpetual motion machine.

This phenomenon is the working principle of every generator, transformer, and induction motor. In a generator, mechanical rotation changes the angle of the loop in B, producing a sinusoidally oscillating EMF — alternating current. In a transformer, an oscillating current in the primary coil creates an oscillating B, which drives an oscillating flux through the secondary coil, inducing a voltage proportional to the turns ratio. Understanding magnetic flux and induction is the bridge between static magnetism and the time-varying electromagnetic phenomena at the heart of the power grid.
