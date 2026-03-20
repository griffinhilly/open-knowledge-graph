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

## Explainer

From your study of electromagnetic waves, you know that light consists of oscillating electric and magnetic fields perpendicular to the direction of travel. In **unpolarized light** — a typical lightbulb or the sun — those fields oscillate in all possible orientations around the propagation axis, randomly and rapidly shifting direction. **Polarization** refers to constraining that oscillation to a single orientation. The distinction is purely geometric: polarized light is light where the electric field vector stays in one plane as the wave propagates.

The simplest way to produce linearly polarized light is with a **polarizer**: a material (like Polaroid film) containing long molecular chains aligned in one direction. These chains absorb electric field oscillations along their length and transmit oscillations perpendicular to them. Only light whose electric field aligns with the transmission axis passes through freely; all other orientations are attenuated. When unpolarized light passes through an ideal polarizer, exactly half the intensity is transmitted — the half carried by oscillations in the pass direction. The other half is absorbed regardless of how you rotate the polarizer, because unpolarized light has equal energy in all orientations.

Once you have linearly polarized light, a second polarizer (used as an **analyzer**) lets you measure its polarization direction. **Malus' law** — I = I₀ cos²θ — tells you how much intensity passes through. The cos²θ factor comes from projecting the polarized electric field onto the analyzer's transmission axis: only the component aligned with the analyzer's axis passes, and intensity scales as the square of the field amplitude. At θ = 0° the analyzer is aligned and all light passes; at θ = 90° (crossed polarizers) no light passes. At 45°, half the intensity passes. Two crossed polarizers create near-total darkness — a result you can verify with any two pairs of polarized sunglasses.

Polarization also arises from reflection. At **Brewster's angle** (tan θ_B = n₂/n₁), reflected light is completely polarized with the electric field parallel to the reflecting surface. This is why polarized sunglasses cut glare: light reflecting off horizontal surfaces like water or roads is predominantly polarized horizontally, and the vertically oriented polarizers in the lenses block it selectively. **Birefringent** crystals like calcite produce polarization by a different mechanism — they have different refractive indices for different oscillation directions, splitting an unpolarized beam into two polarized beams that travel at different speeds and separate spatially. This property is exploited in optical wave plates, which retard one polarization component relative to the other to convert between linear, circular, and elliptical polarization.
