---
id: polarization-production-and-analysis
title: 'Polarization: Production and Analysis'
domain: physics
course: waves-and-optics
prerequisites:
- id: electromagnetic-waves
  type: hard
builds-toward:
- polarization-of-light
tags:
- polarization
- polarizer
- analyzer
stage: advanced
status: draft
---

# Polarization: Production and Analysis

## Core Idea
Polarization restricts oscillation to a single plane perpendicular to propagation. Unpolarized light (random oscillation planes) becomes linearly polarized by passing through a polarizer. A second polarizer (analyzer) transmits intensity I = I₀ cos²θ (Malus' law), where θ is the angle between polarization axes. Polarization can be produced by selective absorption, reflection (Brewster's angle), or birefringent crystals.

## Questions

```yaml
- question: "Three polarizers are stacked: the first produces linearly polarized light, the second is at 45° to the first, and the third is at 90° to the first (crossed). Without the middle polarizer, no light passes. With it, light passes through. Why?"
  type: multiple-choice
  options:
    - "The middle polarizer amplifies the light intensity, allowing enough to overcome the crossed configuration"
    - "The middle polarizer creates a new 45° polarization axis; by Malus' law each stage passes cos²(45°) = 50% of the light it receives, so light reaches the third polarizer with non-zero intensity at an angle that is no longer 90°"
    - "The middle polarizer rotates the polarization direction of individual photons, gradually steering them parallel to the third polarizer's axis"
    - "The middle polarizer scatters some light into the transmission direction of the third polarizer"
  answer: 1
  explanation: "This is the classic three-polarizer paradox. Without the middle polarizer, the first and third are crossed at 90° and block all light. With the middle polarizer at 45°: stage 1→2 passes I₀ cos²(45°) = I₀/2; stage 2→3 passes (I₀/2) cos²(45°) = I₀/4. The key is that after the second polarizer, the light is polarized at 45° — which is only 45° from the third polarizer's axis, not 90°. Each polarizer resets the polarization direction, and the 90° relationship between first and third no longer matters. The middle polarizer does not amplify; it reorients."

- question: "Unpolarized light of intensity I₀ passes through an ideal linear polarizer. What intensity emerges, and does the answer depend on the polarizer's orientation?"
  type: multiple-choice
  options:
    - "I₀ — an ideal polarizer transmits all light without absorption"
    - "I₀/2, regardless of the polarizer's orientation, because unpolarized light carries equal energy in all oscillation planes"
    - "I₀ cos²θ, where θ is the angle between the polarizer axis and the dominant oscillation direction of the incident light"
    - "It depends on the polarizer's orientation — rotating it changes how much unpolarized light is absorbed"
  answer: 1
  explanation: "Unpolarized light is, by definition, light with equal intensity distributed uniformly across all oscillation planes. No matter which direction you orient the polarizer's transmission axis, it passes the component of electric field along that axis and blocks the rest. For a uniform distribution, exactly half the total intensity is carried by oscillations in any one direction. So an ideal polarizer always transmits I₀/2 from unpolarized light, regardless of orientation. This is why Malus' law I = I₀ cos²θ only applies when the incident light is already linearly polarized — for unpolarized light, the input is always I₀/2."

- question: "Two ideal polarizers with their transmission axes crossed at exactly 90° will transmit essentially no light, because the polarization direction of the light from the first polarizer is perpendicular to the transmission axis of the second."
  type: true-false
  answer: true
  explanation: "Malus' law gives I = I₀ cos²(90°) = I₀ · 0 = 0. The electric field component along the second polarizer's axis is exactly zero: the first polarizer produces light oscillating in one plane, and the second polarizer's transmission axis is perpendicular to that plane. There is no component to transmit. In practice, with real polarizers, a tiny amount of light leaks through due to imperfections in alignment and absorption, but an ideal crossed-polarizer configuration produces zero transmission."

- question: "When linearly polarized light passes through an analyzer at angle θ, the transmitted electric field amplitude is reduced by the factor cos²θ."
  type: true-false
  answer: false
  explanation: "The electric field amplitude is reduced by cosθ, not cos²θ. Malus' law states that the transmitted intensity I = I₀ cos²θ. Since intensity is proportional to amplitude squared (I ∝ E²), we have E_transmitted = E₀ cosθ. The cos²θ factor applies to intensity, not amplitude. This distinction matters for understanding interference phenomena, where electric field amplitudes add (not intensities), and for calculating what happens when polarized light passes through multiple optical elements."

- question: "Why does inserting a polarizer at 45° between two crossed polarizers allow light to pass through the system, when the two crossed polarizers alone block all light?"
  type: short-answer
  answer: "The middle polarizer resets the polarization direction to 45°. After the first polarizer, light is polarized in one direction (call it 0°). The middle polarizer at 45° transmits the component of this light along its 45° axis — I₀/2 passes, now polarized at 45°. The third polarizer at 90° then receives light polarized at 45°, which is only 45° away from its transmission axis (not 90°). It transmits I₀/2 · cos²(45°) = I₀/4. Without the middle polarizer, the light from the first polarizer (0°) hits the third polarizer (90°) at 90° — zero transmission. The middle polarizer breaks the perpendicularity relationship by introducing an intermediate polarization state."
  explanation: "This result is counterintuitive because adding an element that blocks half the light at each stage somehow produces more light out the other end than the system without it. The resolution is that it is not the light that passes through the first two polarizers that matters — it is the polarization direction of the light arriving at the third polarizer. The middle polarizer changes that direction from 0° to 45°, and 45° has a non-zero projection onto the 90° axis. More generally, any polarizer inserted between crossed polarizers at an angle other than 0° or 90° will transmit some light."
```

## Explainer

From your study of electromagnetic waves, you know that light consists of oscillating electric and magnetic fields perpendicular to the direction of travel. In **unpolarized light** — a typical lightbulb or the sun — those fields oscillate in all possible orientations around the propagation axis, randomly and rapidly shifting direction. **Polarization** refers to constraining that oscillation to a single orientation. The distinction is purely geometric: polarized light is light where the electric field vector stays in one plane as the wave propagates.

The simplest way to produce linearly polarized light is with a **polarizer**: a material (like Polaroid film) containing long molecular chains aligned in one direction. These chains absorb electric field oscillations along their length and transmit oscillations perpendicular to them. Only light whose electric field aligns with the transmission axis passes through freely; all other orientations are attenuated. When unpolarized light passes through an ideal polarizer, exactly half the intensity is transmitted — the half carried by oscillations in the pass direction. The other half is absorbed regardless of how you rotate the polarizer, because unpolarized light has equal energy in all orientations.

Once you have linearly polarized light, a second polarizer (used as an **analyzer**) lets you measure its polarization direction. **Malus' law** — I = I₀ cos²θ — tells you how much intensity passes through. The cos²θ factor comes from projecting the polarized electric field onto the analyzer's transmission axis: only the component aligned with the analyzer's axis passes, and intensity scales as the square of the field amplitude. At θ = 0° the analyzer is aligned and all light passes; at θ = 90° (crossed polarizers) no light passes. At 45°, half the intensity passes. Two crossed polarizers create near-total darkness — a result you can verify with any two pairs of polarized sunglasses.

Polarization also arises from reflection. At **Brewster's angle** (tan θ_B = n₂/n₁), reflected light is completely polarized with the electric field parallel to the reflecting surface. This is why polarized sunglasses cut glare: light reflecting off horizontal surfaces like water or roads is predominantly polarized horizontally, and the vertically oriented polarizers in the lenses block it selectively. **Birefringent** crystals like calcite produce polarization by a different mechanism — they have different refractive indices for different oscillation directions, splitting an unpolarized beam into two polarized beams that travel at different speeds and separate spatially. This property is exploited in optical wave plates, which retard one polarization component relative to the other to convert between linear, circular, and elliptical polarization.
