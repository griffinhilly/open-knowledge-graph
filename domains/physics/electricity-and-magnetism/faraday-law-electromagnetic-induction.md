---
id: faraday-law-electromagnetic-induction
title: Faraday's Law of Electromagnetic Induction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ampere-law-applications
  type: hard
- id: magnetic-flux-and-induction
  type: hard
- id: stokes-theorem
  type: hard
- id: line-integrals-vector-fields
  type: hard
- id: curl-divergence
  type: hard
- id: line-integrals
  type: hard
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- lenz-law-induced-currents
tags:
- faraday-law
- induction
- emf
stage: formal-systems
status: draft
---

# Faraday's Law of Electromagnetic Induction

## Core Idea
Faraday's law states ε = −dΦ_B/dt, where ε is induced EMF and Φ_B is magnetic flux through a circuit. Changing magnetic flux induces an electric field that drives current. The negative sign (Lenz's law) indicates the induced field opposes the flux change.

## Explainer

From Ampère's law you learned that currents produce magnetic fields. Faraday's law is in some sense the reverse: changing magnetic fields produce electric fields — and therefore voltages and currents. The central quantity is **magnetic flux** Φ_B = ∫B⃗·dA⃗ through a surface bounded by your circuit. Flux measures how much magnetic field passes through the loop, weighted by the angle of incidence. If the field is uniform and the loop lies flat in the field, Φ_B = BA cos θ. What matters for induction is not the flux itself, but its rate of change.

Faraday's law states that the **induced EMF** around a closed loop equals the negative rate of change of flux through it: ε = −dΦ_B/dt. Think of EMF as the voltage that would push a current around the loop if a conducting path exists. Crucially, the flux can change in three ways — the field strength can change, the area of the loop can change (as in a generator with a rotating coil), or the angle between the field and the loop can change. All three mechanisms produce EMF, and they are interchangeable in the formula.

The negative sign is the mathematical form of **Lenz's law**: the induced EMF (and therefore the induced current it drives) always acts to oppose the change that caused it. If flux through the loop is increasing, the induced current creates its own magnetic field that opposes the increase — it "fights back." If flux is decreasing, the induced current tries to maintain it. This opposition is a statement of energy conservation: you must do work against the induced field to change the flux. In your prerequisite study of the curl operator and Stokes' theorem, you learned to convert between line integrals around loops and surface integrals. The differential form of Faraday's law, ∇×E = −∂B/∂t, expresses the same physics pointwise: a time-varying magnetic field generates a curling electric field, not just at wires, but throughout all of space.

This law is the operating principle behind every electrical generator, transformer, and inductance-based device. A generator rotates a coil in a steady magnetic field, continuously changing the angle between the loop and the field and therefore continuously changing flux — producing AC voltage. A transformer couples two coils through a shared changing flux: EMF in the primary induces flux change, which induces EMF in the secondary. The ratio of turns in each coil sets the voltage ratio, all traceable to ε = −dΦ_B/dt. When you study Lenz's law applications and then self-inductance, Faraday's law will be the governing equation at each step.
