---
id: polarization-linear-production
title: 'Linear Polarization: Production and Analysis Methods'
domain: physics
course: waves-and-optics
prerequisites:
- id: polarization-of-light
  type: hard
- id: polarization-production-and-analysis
  type: soft
- id: circular-elliptical-polarization
  type: soft
builds-toward:
- polarization-production-and-analysis
tags:
- polarization
- linear-polarization
- polarizers
stage: advanced
status: validated
---
# Linear Polarization: Production and Analysis Methods

## Core Idea
Unpolarized light becomes linearly polarized through selective absorption (polarizers), reflection at Brewster's angle, or birefringence. Malus's law describes intensity transmission through crossed polarizers: I = I₀cos²θ. Polarization analysis is critical for optical communications and materials characterization.

## Questions

```yaml
- question: "Linearly polarized light with intensity I₀ passes through a polarizer whose transmission axis is oriented at 60° to the polarization direction. What is the transmitted intensity?"
  type: multiple-choice
  options:
    - "0.75 I₀"
    - "0.25 I₀"
    - "0.50 I₀"
    - "0 — only perpendicular orientations transmit light"
  answer: 1
  explanation: "Malus's law: I = I₀cos²θ. At θ = 60°, cos²60° = (0.5)² = 0.25, so 25% of I₀ is transmitted. Option A (0.75) is cos²30°, a common error from using the complementary angle. Option C (0.5) is often guessed because 60° is 'most of the way' to 90°, but the cosine-squared relationship falls off faster than intuition suggests."

- question: "Two polarizing sheets are crossed (transmission axes 90° apart), blocking all light. A third sheet is inserted between them at 45° to each. What fraction of the intensity emerging from the first polarizer is transmitted through the entire stack?"
  type: multiple-choice
  options:
    - "0% — an obstruction cannot restore blocked transmission"
    - "50% — the intermediate polarizer halves the intensity once"
    - "25% — Malus's law applied twice: cos²45° × cos²45° = 0.25"
    - "75% — the intermediate polarizer rotates most of the polarization toward the final axis"
  answer: 2
  explanation: "Each stage applies Malus's law independently. After the first polarizer the beam is polarized at 0°. The middle polarizer at 45° transmits cos²45° = 0.5 of what reaches it. The final polarizer at 90° transmits cos²45° = 0.5 of that. Product: 0.5 × 0.5 = 0.25. Option A captures the intuitive but incorrect argument — that an extra absorber can only reduce transmission. The key insight is that the intermediate polarizer *changes the polarization direction*, making the angle between polarization and the final axis 45° instead of 90°, enabling partial transmission."

- question: "When unpolarized light reflects from a glass surface at Brewster's angle, the reflected beam is completely polarized with its electric field parallel to the surface (perpendicular to the plane of incidence)."
  type: true-false
  answer: true
  explanation: "At Brewster's angle θ_B = arctan(n₂/n₁), the reflected and refracted rays are 90° apart. Under this condition, the p-polarized component (field in the plane of incidence) is not reflected at all, leaving the reflected beam entirely s-polarized (field perpendicular to the plane of incidence, i.e., parallel to the surface). This is exactly why polarized sunglasses oriented with a vertical transmission axis block horizontally polarized glare from roads and water."

- question: "Adding a third polarizer between two crossed polarizers always reduces the total transmitted intensity compared to having only the two crossed polarizers."
  type: true-false
  answer: false
  explanation: "Two perfectly crossed polarizers transmit 0% — they already block everything. Inserting a third polarizer at 45° between them allows 25% of the post-first-polarizer intensity to pass through. Going from 0% to 25% is an increase, not a decrease. This apparent paradox — adding an absorbing element increases transmission — arises because the intermediate polarizer changes the polarization direction of the light reaching the final polarizer, reducing the angle from 90° to 45°."

- question: "Why does inserting a polarizer at 45° between two crossed polarizers increase the transmitted intensity, even though the inserted polarizer itself absorbs light?"
  type: short-answer
  answer: "The two crossed polarizers block all light because the angle between them is 90° and cos²90° = 0. The inserted polarizer does not simply 'add' transmission — it changes the problem. It projects the linearly polarized light from the first polarizer onto the 45° direction, producing a less intense beam polarized at 45°. Now the angle between this new polarization direction and the final polarizer's axis is only 45°, not 90°. Applying Malus's law at each step: cos²45° × cos²45° = 0.25, giving non-zero transmission. Without the intermediate, the direct 90° crossing guarantees zero regardless of intensity."
  explanation: "The core insight is that Malus's law is a projection relationship — it describes how much of the polarization vector aligns with the transmission axis. The crossed-polarizer system fails because the full 90° angle makes the projection zero. The intermediate polarizer resets the polarization direction to an intermediate angle, enabling partial projection at each subsequent stage."
```

## Explainer

You already know that polarization describes the orientation of the electric field oscillation in light. Natural light from the sun or a lightbulb is **unpolarized** — the electric field points in all transverse directions at random, with no preferred orientation over time. To produce linearly polarized light, you need a mechanism that either selects one direction or eliminates all others. Three distinct physical mechanisms accomplish this, each exploiting a different property of matter and light.

The most common method is **selective absorption**, used in sheet polarizers found in sunglasses, camera filters, and LCD screens. A polarizing sheet contains long polymer chains aligned in one direction. These chains preferentially absorb the component of the electric field parallel to them, while transmitting the perpendicular component. The direction that passes through is the **transmission axis**. When unpolarized light strikes a polarizer, roughly half the intensity is transmitted — the half whose field is aligned with the transmission axis. What emerges is fully linearly polarized in that direction.

**Brewster's angle** is a subtler effect arising from the way electromagnetic waves reflect at interfaces. When unpolarized light strikes a surface at a specific angle θ_B = arctan(n₂/n₁), the reflected beam is completely polarized with its electric field parallel to the surface (s-polarized). The transmitted beam is partially polarized in the perpendicular direction. This is exactly why polarized sunglasses reduce glare from roads and water: reflected sunlight at near-Brewster's angle is strongly horizontally polarized, and the vertically oriented transmission axis of the glasses blocks it selectively.

**Birefringence** occurs in crystals (like calcite or quartz) that have different refractive indices for the two perpendicular polarization orientations. A ray entering the crystal is effectively split into two components that travel at different speeds, accumulating a phase difference that grows with crystal thickness. By choosing the right thickness, one component can be selectively blocked, or a controlled phase shift can be introduced — the operating principle behind wave plates, which convert between linear, circular, and elliptical polarization.

Once linearly polarized light is produced, **Malus's law** I = I₀cos²θ predicts how much intensity survives a second polarizer. At θ = 0° the polarizers are aligned and all light passes. At θ = 90° (crossed polarizers) no light passes — a combination that appears completely opaque. Strikingly, inserting a third polarizer between them at 45° restores some transmission: Malus's law applied twice (cos²45° × cos²45° = 0.25) gives 25% of I₀. This apparent paradox — adding an obstruction increases transmission — is a direct consequence of the projection nature of the cosine-squared law.
