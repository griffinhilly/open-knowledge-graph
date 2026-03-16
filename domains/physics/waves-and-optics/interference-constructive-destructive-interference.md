---
id: interference-constructive-destructive-interference
title: Constructive and Destructive Interference
domain: physics
course: waves-and-optics
prerequisites:
- id: superposition-principle-waves
  type: hard
- id: phase-and-phase-relationships
  type: hard
- id: trigonometric-identities
  type: soft
builds-toward:
- two-source-interference-patterns
- thin-film-interference
tags:
- interference
- constructive
- destructive
stage: formal-systems
status: draft
---

# Constructive and Destructive Interference

## Core Idea
Constructive interference occurs when waves in phase combine, producing maximum amplitude. Destructive interference occurs when waves are π radians out of phase, producing minimum (or zero) amplitude. The type of interference depends on the path difference: constructive when path difference equals an integer multiple of λ, destructive when it equals (n + ½)λ.

## How It's Best Learned
Use two speakers driven by the same frequency to create regions of loud and quiet sound. Create interference patterns with ripple tanks using two sources. Measure the conditions for constructive vs destructive interference.

## Common Misconceptions
- Destructive interference always produces zero amplitude; it can produce reduced but nonzero amplitude.
- Interference only occurs with identical frequency waves; any coherent waves can interfere.
- Path difference directly equals phase difference; phase difference = (path difference / λ) × 2π.

## Explainer

From the superposition principle, you know that when two waves occupy the same point in space, their displacements simply add. The result at any instant is just the sum of the individual wave amplitudes at that point. Interference is what you observe when this addition produces a stable, predictable pattern — which requires that the waves maintain a fixed **phase relationship** over time. Such waves are called **coherent**. With coherent sources, the interference pattern stays put; with incoherent sources (like two separate lightbulbs), the phase relationship shifts randomly and the pattern averages away.

When two coherent waves arrive at a point in phase — crest meeting crest — their displacements reinforce. The combined amplitude equals the sum of the individual amplitudes. This is **constructive interference**. When they arrive exactly out of phase — crest meeting trough — the displacements partially or fully cancel. If the two amplitudes are equal, the cancellation is complete: zero net displacement. This is **destructive interference**. The phase difference that matters is the difference at the point of observation, not at the source.

The most physically transparent way to track phase is through **path difference** — the difference in distance each wave travels to reach the observation point. If wave A travels 3.5 wavelengths to reach a point and wave B travels 2.0 wavelengths, the path difference is 1.5λ. One full wavelength of extra travel corresponds to one full oscillation cycle, bringing the wave back in phase with itself. So a path difference of exactly nλ (for any integer n) means the waves arrive in phase → constructive interference. A path difference of (n + ½)λ means one wave has traveled an extra half-cycle relative to the other → waves arrive exactly out of phase → destructive interference.

Be careful about the conversion between path difference and phase difference: they are proportional, not equal. A path difference of Δr corresponds to a phase difference of δ = (Δr/λ) × 2π radians. A path difference of λ gives δ = 2π (in phase). A path difference of λ/2 gives δ = π (out of phase). Mixing up path difference in meters with phase difference in radians is the most common computational error in interference problems. The physical condition (integer vs. half-integer wavelengths) is easy to remember; the formula is just the rigorous version of the same idea.
