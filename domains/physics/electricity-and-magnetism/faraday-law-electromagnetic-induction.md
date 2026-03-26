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
- id: electromagnetic-induction-applications
  type: soft
- id: eddy-currents-and-energy-dissipation
  type: soft
- id: induced-electric-field-non-conservative
  type: soft
builds-toward:
- lenz-law-induced-currents
tags:
- faraday-law
- induction
- emf
stage: advanced
status: validated
---
# Faraday's Law of Electromagnetic Induction

## Core Idea
Faraday's law states ε = −dΦ_B/dt, where ε is induced EMF and Φ_B is magnetic flux through a circuit. Changing magnetic flux induces an electric field that drives current. The negative sign (Lenz's law) indicates the induced field opposes the flux change.

## Questions

```yaml
- question: "A bar magnet is held perfectly stationary inside a coil of wire. What is the induced EMF in the coil?"
  type: multiple-choice
  options:
    - "Maximum — the magnetic flux through the coil is at its highest"
    - "Zero — there is no change in flux, so Faraday's law gives ε = −dΦ/dt = 0"
    - "Proportional to the magnetic field strength of the magnet"
    - "Proportional to the number of turns in the coil"
  answer: 1
  explanation: "Faraday's law states ε = −dΦ_B/dt. A stationary magnet produces constant magnetic flux — dΦ/dt = 0, so EMF = 0 and no current flows. This directly attacks the most common misconception: that the presence of a magnetic field induces current. It is the *change* in flux, not the flux itself, that drives induction. The moment the magnet moves, dΦ/dt becomes nonzero and EMF appears."

- question: "A generator coil rotating at constant speed in a uniform magnetic field produces maximum EMF at the instant when:"
  type: multiple-choice
  options:
    - "The coil face is perpendicular to the field — maximizing flux through the coil"
    - "The coil face is parallel to the field — flux is zero but changing at its fastest rate"
    - "The coil is halfway between the two extreme positions — flux and rate of change are both moderate"
    - "Rotation stops momentarily at the peak position — flux is maximum and stable"
  answer: 1
  explanation: "EMF = −dΦ/dt, not EMF = −Φ. When the coil face is perpendicular to the field (Φ = BA, maximum), the rate of change of flux is actually zero — the coil momentarily isn't changing how much field passes through it. When the coil face is parallel to the field (Φ = 0), the coil crosses the 'equator' of its rotation and flux changes at its fastest rate — dΦ/dt is maximum, giving maximum EMF. This counterintuitive result is fundamental to understanding AC generators."

- question: "Lenz's law, encoded in the negative sign of Faraday's law, is a consequence of energy conservation: you must do work against the induced field to change the magnetic flux."
  type: true-false
  answer: true
  explanation: "Yes. If the induced EMF reinforced rather than opposed the flux change, you could move a magnet into a coil and the resulting current would pull the magnet in even faster, generating electrical energy without any input work — a perpetual motion machine. The opposition expressed by Lenz's law ensures that you must do work to change the flux, satisfying energy conservation. The negative sign is not a mere convention; it encodes a physical constraint."

- question: "The direction of the induced current in a loop is generally the same, regardless of whether the magnetic flux through the loop is increasing or decreasing."
  type: true-false
  answer: false
  explanation: "Lenz's law states that the induced current opposes the *change* in flux, so direction depends entirely on whether flux is increasing or decreasing. If flux is increasing, the induced current creates a magnetic field opposing the increase — one current direction. If flux is decreasing, the induced current tries to maintain it — the opposite direction. A magnet approaching a coil and the same magnet receding produce opposite current directions in the coil."

- question: "Why does a stationary magnet inside a coil produce no current, while a moving magnet produces current? What does this reveal about the true content of Faraday's law?"
  type: short-answer
  answer: "Faraday's law states ε = −dΦ_B/dt: only a *change* in magnetic flux induces EMF. A stationary magnet creates constant flux through the coil — the field is present but not changing, so dΦ/dt = 0 and EMF = 0. When the magnet moves, the amount of magnetic flux passing through the coil changes with time, producing a nonzero dΦ/dt and therefore a nonzero EMF. This reveals that induction is fundamentally about flux changing over time, not about the presence or strength of a field at any moment."
  explanation: "The distinction matters enormously in applications. A transformer works because alternating current continuously changes the magnetic flux in its iron core, inducing EMF in the secondary coil — DC would produce constant flux and no induction. A microphone works because sound waves vibrate a coil in a magnetic field, changing flux and generating a signal proportional to the sound."
```

## Explainer

From Ampère's law you learned that currents produce magnetic fields. Faraday's law is in some sense the reverse: changing magnetic fields produce electric fields — and therefore voltages and currents. The central quantity is **magnetic flux** Φ_B = ∫B⃗·dA⃗ through a surface bounded by your circuit. Flux measures how much magnetic field passes through the loop, weighted by the angle of incidence. If the field is uniform and the loop lies flat in the field, Φ_B = BA cos θ. What matters for induction is not the flux itself, but its rate of change.

Faraday's law states that the **induced EMF** around a closed loop equals the negative rate of change of flux through it: ε = −dΦ_B/dt. Think of EMF as the voltage that would push a current around the loop if a conducting path exists. Crucially, the flux can change in three ways — the field strength can change, the area of the loop can change (as in a generator with a rotating coil), or the angle between the field and the loop can change. All three mechanisms produce EMF, and they are interchangeable in the formula.

The negative sign is the mathematical form of **Lenz's law**: the induced EMF (and therefore the induced current it drives) always acts to oppose the change that caused it. If flux through the loop is increasing, the induced current creates its own magnetic field that opposes the increase — it "fights back." If flux is decreasing, the induced current tries to maintain it. This opposition is a statement of energy conservation: you must do work against the induced field to change the flux. In your prerequisite study of the curl operator and Stokes' theorem, you learned to convert between line integrals around loops and surface integrals. The differential form of Faraday's law, ∇×E = −∂B/∂t, expresses the same physics pointwise: a time-varying magnetic field generates a curling electric field, not just at wires, but throughout all of space.

This law is the operating principle behind every electrical generator, transformer, and inductance-based device. A generator rotates a coil in a steady magnetic field, continuously changing the angle between the loop and the field and therefore continuously changing flux — producing AC voltage. A transformer couples two coils through a shared changing flux: EMF in the primary induces flux change, which induces EMF in the secondary. The ratio of turns in each coil sets the voltage ratio, all traceable to ε = −dΦ_B/dt. When you study Lenz's law applications and then self-inductance, Faraday's law will be the governing equation at each step.
