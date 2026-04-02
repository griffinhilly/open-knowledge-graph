---
id: faraday-law-of-induction
title: Faraday's Law of Electromagnetic Induction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-and-lorentz-force
  type: hard
- id: partial-derivatives
  type: hard
- id: line-integrals
  type: hard
builds-toward:
- displacement-current-and-maxwell
- electromagnetic-wave-equation
tags:
- induction
- time-varying-fields
- maxwell-equations
stage: expert
status: validated
---

# Faraday's Law of Electromagnetic Induction

## Core Idea
Faraday's law states that a changing magnetic flux induces an electric field: ∮ E·dl = -dΦ_B/dt or ∇ × E = -∂B/∂t. This fundamental asymmetry reveals that time-varying B creates E, anticipating Maxwell's symmetrization.

## Questions

```yaml
- question: "A circular wire loop sits in a uniform magnetic field. An EMF is induced in the loop when..."
  type: multiple-choice
  options: ["The field is very strong", "The magnetic flux through the loop is changing", "The loop is oriented parallel to the field", "Current is already flowing in the loop"]
  answer: 1
  explanation: "Faraday's law states EMF = −dΦ_B/dt — only a changing flux induces an EMF. A strong but constant field produces no EMF at all. Flux can change because B changes in magnitude, because the loop's area changes, or because the angle between B and the loop's normal changes."

- question: "A strong, steady magnetic field passing through a conducting loop induces a large EMF in that loop."
  type: true-false
  answer: false
  explanation: "EMF = −dΦ_B/dt — it is the rate of change of flux that matters, not the magnitude. A constant field, however strong, produces dΦ_B/dt = 0 and therefore zero EMF. This is why transformers require alternating current: a DC source produces a static field that induces nothing in the secondary coil."

- question: "The negative sign in Faraday's law (EMF = −dΦ_B/dt) is associated with Lenz's law. What does this sign physically mean?"
  type: short-answer
  answer: "The induced EMF drives a current whose own magnetic field opposes the change in flux that caused the induction — the induced effect resists the change."
  explanation: "Lenz's law is energy conservation in disguise. If the induced EMF reinforced the change in flux instead of opposing it, the growing EMF would increase the flux, which would increase the EMF further — a runaway process requiring no energy input. The negative sign prevents this by ensuring external work must be done to maintain the changing flux, consistent with conservation of energy."
```

## Explainer

You already know that a magnetic field exerts a force on moving charges (the Lorentz force, F = qv × B). Faraday's law reveals something deeper: a *changing* magnetic field creates an electric field, even in regions of empty space where no charges are present. The integral form ∮ E·dl = −dΦ_B/dt says that the line integral of the electric field around any closed loop equals the negative rate of change of magnetic flux through that loop. This is one of Maxwell's four equations and a cornerstone of all electrical technology.

The central word is *changing*. A steady magnetic field — however powerful — induces nothing. What drives induction is dΦ_B/dt, the time derivative of the flux Φ_B = ∫B·dA. Flux can change in three ways: B itself can vary in time, the area of the loop can change, or the angle between B and the surface can change. These three mechanisms correspond to three major technologies: transformers (time-varying B), electric generators (rotating loop — changing angle), and speakers and microphones (moving coil — changing position and effective area). All three are manifestations of the same law.

The negative sign encodes Lenz's law: the induced EMF drives a current whose magnetic field *opposes* the change in flux. Pull a magnet toward a loop and the loop develops a current that creates a field repelling the approaching magnet — trying to prevent the flux from increasing. Push the magnet away and the induced current reverses to attract it, trying to prevent the flux from decreasing. This opposition is not coincidental; it is a consequence of energy conservation. If the induced current reinforced the change in flux, the EMF would amplify the flux, which would amplify the EMF, creating energy from nothing. The negative sign prevents this runaway.

The differential form ∇ × E = −∂B/∂t is the local, point-by-point version of the same law. Where the integral form describes what happens around a loop, the differential form applies at every individual point in space. Stokes' theorem — which converts a line integral around a closed curve into a surface integral of the curl — connects the two forms and shows they are equivalent. Your prerequisite in line integrals is precisely what makes this connection available to you.

Understanding Faraday's law is the gateway to the full theory of electromagnetism. Maxwell completed the theory by adding the displacement current term to Ampere's law, creating a symmetric pair: a changing E produces B (modified Ampere's law), and a changing B produces E (Faraday's law). This symmetry means a disturbance in the electromagnetic field can sustain itself as it propagates through empty space — a self-reinforcing oscillation of E and B fields. That is light. Every electromagnetic wave, from radio to gamma rays, is a consequence of the relationship you have just learned.
