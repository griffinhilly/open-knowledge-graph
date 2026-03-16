---
id: mutual-inductance-coupled-coils
title: Mutual Inductance and Coupled Coils
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: self-inductance-of-circuits
  type: hard
- id: faraday-law-of-induction
  type: hard
builds-toward:
- electromagnetic-induction-applications
tags:
- inductance
- mutual inductance
- coupling
stage: formal-systems
status: draft
---

# Mutual Inductance and Coupled Coils

## Core Idea
Mutual inductance M relates current in one coil to flux in another: Φ₂₁ = MI₁. The mutual-induced EMF is ε₂ = -M(dI₁/dt). Mutual inductance is symmetric: M₁₂ = M₂₁. The coupling coefficient k = M/√(L₁L₂) ranges from 0 (no coupling) to 1 (perfect coupling). Mutual inductance is the principle behind transformers and wireless power transfer.

## Explainer

Self-inductance describes how a coil's own changing current induces a back-EMF in itself. **Mutual inductance** extends this to two coils: when current in coil 1 changes, the changing magnetic flux it creates threads through coil 2 and induces an EMF there. By Faraday's law, ε₂ = −dΦ₂₁/dt, and since Φ₂₁ is proportional to I₁ (the source current), we write Φ₂₁ = MI₁ and get ε₂ = −M dI₁/dt. The mutual inductance M is a purely geometric quantity — it depends on the sizes, shapes, and relative positions of the two coils, not on what currents happen to be flowing.

The **symmetry M₁₂ = M₂₁** is a non-obvious but powerful result: the mutual inductance from coil 1 acting on coil 2 equals the mutual inductance from coil 2 acting on coil 1. This is not geometrically obvious — changing current in a small coil near a large coil and changing current in the large coil near the small one seem like different situations — but the equality follows from the reciprocity of the magnetic vector potential. In practice, it means you can calculate M from whichever direction is easier and the result applies both ways.

The **coupling coefficient** k = M/√(L₁L₂) measures what fraction of coil 1's flux actually reaches coil 2. It ranges from 0 (coils far apart or perpendicular, no shared flux) to 1 (perfect coupling, all flux links both coils). For a transformer wound on an iron core, k ≈ 1 — the core guides essentially all the flux from primary to secondary. For two loosely coupled coils in free space, k might be 0.01 or less. The voltage transformation ratio of a transformer (V₂/V₁ = N₂/N₁) follows from perfect coupling combined with the flux linkage relationship.

Mutual inductance is the physical principle behind a surprising range of technologies: power transformers (voltage conversion in the grid), wireless phone chargers (inductive power transfer over millimeters), MRI machines (RF coils that transmit and receive at the Larmor frequency), and metal detectors (an oscillating primary coil drives eddy currents in a nearby conductor, which alter the signal in a receiver coil). In all these cases, the underlying physics is the same: changing current in one circuit induces EMF in another through shared magnetic flux, quantified by M.
