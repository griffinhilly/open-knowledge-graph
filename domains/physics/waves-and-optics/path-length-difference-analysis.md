---
id: path-length-difference-analysis
title: Path Difference and Constructive/Destructive Interference
domain: physics
course: waves-and-optics
prerequisites:
- id: phase-of-oscillation-initial
  type: hard
- id: two-sources-interference-pattern
  type: hard
builds-toward:
- bright-fringes-dark-fringes-spacing
tags:
- interference
- geometry
- waves
stage: formal-systems
status: draft
---

# Path Difference and Constructive/Destructive Interference

## Core Idea
The path difference (Δ) between rays from two sources determines whether interference is constructive (Δ = nλ) or destructive (Δ = (n+½)λ). This geometric relationship lets us predict bright and dark locations without calculating phase explicitly and applies to all wave types—sound, water, light.

## How It's Best Learned
Draw two sources and a screen; measure path differences to different points on the screen and mark which give bright vs dark fringes.

## Common Misconceptions
Path difference is NOT the same as distance from one source; it is the difference between distances to the two sources.

## Explainer

You've already worked with **phase** — the idea that a wave oscillates between peaks and troughs, and that two waves can be aligned (in phase) or offset (out of phase) depending on where they are in their cycles. You've also seen that when two sources emit waves, the interference pattern at a point depends on how the waves from those two sources overlap there. Path-length difference analysis is the geometric tool that connects the *spatial arrangement* of sources and observers to the *phase relationship* at any point — without needing to track phases explicitly.

The central idea is direct: if two coherent sources emit identical waves, and a detector is closer to one source than the other, the wave from the farther source has been traveling longer and has gone through more cycles. The **path length difference** Δ = d₁ − d₂ is the extra distance the farther wave travels compared to the nearer one. If that extra distance is exactly one full wavelength (Δ = λ), the farther wave has completed one extra full cycle — arriving perfectly back in phase with the nearer wave. The waves reinforce: **constructive interference**. If the extra distance is half a wavelength (Δ = λ/2), the farther wave arrives exactly one half-cycle out of phase — crest meets trough — and the waves cancel: **destructive interference**.

The general rules are clean. Constructive interference occurs when Δ = nλ, where n is any integer (0, 1, 2, 3, ...) — meaning the path difference is zero, one wavelength, two wavelengths, and so on. Destructive interference occurs when Δ = (n + ½)λ — half a wavelength, one and a half, two and a half, and so on. This gives you a purely geometric way to predict interference: measure two distances, take their difference, compare to the wavelength. No phase arithmetic required.

The key error to avoid is conflating path difference with distance to a single source. If you're standing 3 m from one speaker and 4 m from another, your path difference is 1 m — not 3 m or 4 m. It's the *difference* that drives interference. This analysis works identically for sound waves in air, water waves in a tank, and light from two slits — the wavelength changes dramatically across these systems, but the principle is the same. Path-difference geometry becomes the foundation of all two-source and multi-source interference problems that follow, including double-slit bright and dark fringe locations.
