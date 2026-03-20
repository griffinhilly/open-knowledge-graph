---
id: polarization-linear-production
title: 'Linear Polarization: Production and Analysis Methods'
domain: physics
course: waves-and-optics
prerequisites:
- id: polarization-of-light
  type: hard
builds-toward:
- polarization-production-and-analysis
tags:
- polarization
- linear-polarization
- polarizers
stage: advanced
status: draft
---

# Linear Polarization: Production and Analysis Methods

## Core Idea
Unpolarized light becomes linearly polarized through selective absorption (polarizers), reflection at Brewster's angle, or birefringence. Malus's law describes intensity transmission through crossed polarizers: I = I₀cos²θ. Polarization analysis is critical for optical communications and materials characterization.

## Explainer

You already know that polarization describes the orientation of the electric field oscillation in light. Natural light from the sun or a lightbulb is **unpolarized** — the electric field points in all transverse directions at random, with no preferred orientation over time. To produce linearly polarized light, you need a mechanism that either selects one direction or eliminates all others. Three distinct physical mechanisms accomplish this, each exploiting a different property of matter and light.

The most common method is **selective absorption**, used in sheet polarizers found in sunglasses, camera filters, and LCD screens. A polarizing sheet contains long polymer chains aligned in one direction. These chains preferentially absorb the component of the electric field parallel to them, while transmitting the perpendicular component. The direction that passes through is the **transmission axis**. When unpolarized light strikes a polarizer, roughly half the intensity is transmitted — the half whose field is aligned with the transmission axis. What emerges is fully linearly polarized in that direction.

**Brewster's angle** is a subtler effect arising from the way electromagnetic waves reflect at interfaces. When unpolarized light strikes a surface at a specific angle θ_B = arctan(n₂/n₁), the reflected beam is completely polarized with its electric field parallel to the surface (s-polarized). The transmitted beam is partially polarized in the perpendicular direction. This is exactly why polarized sunglasses reduce glare from roads and water: reflected sunlight at near-Brewster's angle is strongly horizontally polarized, and the vertically oriented transmission axis of the glasses blocks it selectively.

**Birefringence** occurs in crystals (like calcite or quartz) that have different refractive indices for the two perpendicular polarization orientations. A ray entering the crystal is effectively split into two components that travel at different speeds, accumulating a phase difference that grows with crystal thickness. By choosing the right thickness, one component can be selectively blocked, or a controlled phase shift can be introduced — the operating principle behind wave plates, which convert between linear, circular, and elliptical polarization.

Once linearly polarized light is produced, **Malus's law** I = I₀cos²θ predicts how much intensity survives a second polarizer. At θ = 0° the polarizers are aligned and all light passes. At θ = 90° (crossed polarizers) no light passes — a combination that appears completely opaque. Strikingly, inserting a third polarizer between them at 45° restores some transmission: Malus's law applied twice (cos²45° × cos²45° = 0.25) gives 25% of I₀. This apparent paradox — adding an obstruction increases transmission — is a direct consequence of the projection nature of the cosine-squared law.
