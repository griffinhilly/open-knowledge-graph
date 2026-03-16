---
id: path-difference-phase-difference
title: Path Difference and Phase Difference in Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relationship
  type: hard
- id: wave-superposition
  type: hard
builds-toward:
- constructive-destructive-interference
- two-source-interference-patterns
tags:
- phase
- path-difference
- interference
stage: formal-systems
status: draft
---

# Path Difference and Phase Difference in Waves

## Core Idea
Path difference Δx between two wave sources creates a phase difference Δφ = 2πΔx/λ. Constructive interference occurs when Δx = nλ (phase difference = 2πn), while destructive interference occurs when Δx = (n + ½)λ (phase difference = (2n + 1)π).

## How It's Best Learned
Use phasor diagrams to visualize how phase differences add. Calculate path differences for two-point sources and predict interference patterns.

## Common Misconceptions
- Thinking path difference and phase difference are the same thing; they're related by wavelength.
- Assuming constructive interference always increases amplitude; this is true for coherent waves.

## Explainer

You already know two things: waves have a wavelength λ that defines the periodic scale of the disturbance, and when two waves overlap, they superpose — their displacements add algebraically at every point. **Path difference** and **phase difference** are the tools that connect these two ideas. They let you take a geometric fact (two waves traveled different distances to reach a point) and turn it into a prediction (what does the superposition look like there?).

The key insight is that a wavelength is the distance over which a wave completes one full cycle. If one wave travels exactly one wavelength farther than another before reaching the same point, it arrives shifted by one full cycle — which is no shift at all. The two waves are back in sync, and their peaks align. If one travels exactly half a wavelength farther, it arrives shifted by half a cycle — now peaks align with troughs, and they cancel. **Path difference** Δx is the extra distance one wave travels; **phase difference** Δφ is the resulting phase offset between them. The conversion is Δφ = 2πΔx/λ: each additional wavelength of path difference adds 2π to the phase difference (one full cycle).

The constructive and destructive interference conditions follow directly. Constructive interference requires Δx = nλ for any integer n — the path difference is a whole number of wavelengths, so the phase difference is a multiple of 2π, meaning the waves arrive in phase and their amplitudes add. Destructive interference requires Δx = (n + ½)λ — the path difference is a half-integer number of wavelengths, so the phase difference is an odd multiple of π, meaning the waves arrive perfectly out of phase and cancel.

These two conditions are the foundation for all two-source interference analysis — the double-slit experiment, diffraction gratings, and antenna arrays all reduce to this same path-difference geometry. When you analyze two sources and a point P somewhere in space, you measure the distances r₁ and r₂ from each source to P, compute Δx = |r₁ − r₂|, and ask whether that value is a whole or half-integer multiple of λ. The phase difference formula Δφ = 2πΔx/λ translates spatial geometry into wave behavior. Mastering this translation is what makes interference problems tractable rather than mysterious.
