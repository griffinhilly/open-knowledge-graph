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
