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
stage: expert
status: validated
---

# Mutual Inductance and Coupled Coils

## Core Idea
Mutual inductance M relates current in one coil to flux in another: Φ₂₁ = MI₁. The mutual-induced EMF is ε₂ = -M(dI₁/dt). Mutual inductance is symmetric: M₁₂ = M₂₁. The coupling coefficient k = M/√(L₁L₂) ranges from 0 (no coupling) to 1 (perfect coupling). Mutual inductance is the principle behind transformers and wireless power transfer.

## Questions

```yaml
- question: "An engineer doubles the current flowing through coil 1, while keeping everything else the same. What happens to the mutual inductance M between the two coils?"
  type: multiple-choice
  options:
    - "M doubles, because flux through coil 2 doubles when current in coil 1 doubles"
    - "M stays the same, because M is determined by geometry, not by the magnitude of the current"
    - "M halves, because the induced EMF in coil 2 must remain constant"
    - "M increases by √2, following the same relationship as self-inductance"
  answer: 1
  explanation: "Mutual inductance M is a purely geometric quantity — it depends on the sizes, shapes, and relative positions of the coils, not on what current happens to be flowing. The Explainer states this explicitly: 'The mutual inductance M is a purely geometric quantity.' When current doubles, the flux Φ₂₁ = MI₁ also doubles, and the induced EMF ε₂ = −M(dI₁/dt) changes as well — but M itself is unchanged. Confusing 'M stays fixed while the flux and EMF change' is one of the most common errors in this topic."

- question: "Two coils are placed far apart in free space, with only a tiny fraction of coil 1's flux threading coil 2. What does this imply about the coupling coefficient k?"
  type: multiple-choice
  options:
    - "k ≈ 1, because the coils are physically separated and experience no interference"
    - "k ≈ 0, because almost none of coil 1's flux links coil 2, indicating very weak coupling"
    - "k depends only on the ratio of self-inductances L₁/L₂, not on the shared flux"
    - "k = M/√(L₁L₂) = 0.5 for coils in free space, by convention"
  answer: 1
  explanation: "The coupling coefficient k = M/√(L₁L₂) measures what fraction of coil 1's flux reaches coil 2. When coils are far apart, very little flux is shared, M is tiny relative to √(L₁L₂), and k approaches 0. Conversely, k ≈ 1 means nearly all the flux links both coils — achieved in a transformer wound on a high-permeability iron core that guides the flux. Option A confuses physical separation with strong coupling; physical separation gives weak coupling (k → 0), not strong."

- question: "The mutual inductance M₁₂ (flux through coil 2 per unit current in coil 1) equals M₂₁ (flux through coil 1 per unit current in coil 2), even if the coils have very different sizes."
  type: true-false
  answer: true
  explanation: "The Explainer calls this 'a non-obvious but powerful result' and attributes it to 'the reciprocity of the magnetic vector potential.' Geometrically, it seems strange: driving current through a small coil near a large coil and driving current through the large coil near the small one seem like different configurations with different amounts of flux threading the other coil. But the symmetry holds rigorously. In practice, it means you can calculate M from whichever configuration is mathematically easier, and the result applies to both directions."

- question: "If you increase the current flowing through coil 1 more rapidly (increase dI₁/dt), the mutual inductance M between the coils increases."
  type: true-false
  answer: false
  explanation: "Increasing dI₁/dt increases the induced EMF in coil 2 (ε₂ = −M·dI₁/dt), but M itself is unchanged. M depends entirely on the geometric configuration of the coils — their sizes, shapes, separation, and orientation. The rate of change of current affects how much EMF is induced, but it does not alter the proportionality constant M. This is analogous to self-inductance: increasing dI/dt in a single coil increases its back-EMF without changing L."

- question: "Why is the symmetry M₁₂ = M₂₁ described as 'non-obvious,' and what makes it true despite the apparent asymmetry between differently sized coils?"
  type: short-answer
  answer: "It is non-obvious because the geometry seems asymmetric: if coil 1 is small and coil 2 is large, driving current through small coil 1 sends a concentrated magnetic field that threads a small area of large coil 2, while driving current through large coil 2 sends a dispersed field over the area of small coil 1. Intuitively, the flux linkages seem different. The symmetry holds because of the reciprocity of the magnetic vector potential — a deep result from electromagnetic theory that shows the mutual flux Φ₂₁/I₁ and Φ₁₂/I₂ are always equal, regardless of size mismatch. This allows engineers to calculate M from whichever direction is easier and trust the result applies both ways."
  explanation: "The practical value of this symmetry is significant in circuit design. It means M is a single number characterizing the coupling between two inductors, not two different numbers depending on which coil is the 'source.' This simplifies transformer analysis, coupled-resonator circuits, and wireless power transfer calculations. The deeper reason — reciprocity of the vector potential — is a consequence of the linearity of Maxwell's equations and is a prototype of broader reciprocity theorems in physics."
```

## Explainer

Self-inductance describes how a coil's own changing current induces a back-EMF in itself. **Mutual inductance** extends this to two coils: when current in coil 1 changes, the changing magnetic flux it creates threads through coil 2 and induces an EMF there. By Faraday's law, ε₂ = −dΦ₂₁/dt, and since Φ₂₁ is proportional to I₁ (the source current), we write Φ₂₁ = MI₁ and get ε₂ = −M dI₁/dt. The mutual inductance M is a purely geometric quantity — it depends on the sizes, shapes, and relative positions of the two coils, not on what currents happen to be flowing.

The **symmetry M₁₂ = M₂₁** is a non-obvious but powerful result: the mutual inductance from coil 1 acting on coil 2 equals the mutual inductance from coil 2 acting on coil 1. This is not geometrically obvious — changing current in a small coil near a large coil and changing current in the large coil near the small one seem like different situations — but the equality follows from the reciprocity of the magnetic vector potential. In practice, it means you can calculate M from whichever direction is easier and the result applies both ways.

The **coupling coefficient** k = M/√(L₁L₂) measures what fraction of coil 1's flux actually reaches coil 2. It ranges from 0 (coils far apart or perpendicular, no shared flux) to 1 (perfect coupling, all flux links both coils). For a transformer wound on an iron core, k ≈ 1 — the core guides essentially all the flux from primary to secondary. For two loosely coupled coils in free space, k might be 0.01 or less. The voltage transformation ratio of a transformer (V₂/V₁ = N₂/N₁) follows from perfect coupling combined with the flux linkage relationship.

Mutual inductance is the physical principle behind a surprising range of technologies: power transformers (voltage conversion in the grid), wireless phone chargers (inductive power transfer over millimeters), MRI machines (RF coils that transmit and receive at the Larmor frequency), and metal detectors (an oscillating primary coil drives eddy currents in a nearby conductor, which alter the signal in a receiver coil). In all these cases, the underlying physics is the same: changing current in one circuit induces EMF in another through shared magnetic flux, quantified by M.
