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
stage: advanced
status: validated
---

# Path Difference and Constructive/Destructive Interference

## Core Idea
The path difference (Δ) between rays from two sources determines whether interference is constructive (Δ = nλ) or destructive (Δ = (n+½)λ). This geometric relationship lets us predict bright and dark locations without calculating phase explicitly and applies to all wave types—sound, water, light.

## How It's Best Learned
Draw two sources and a screen; measure path differences to different points on the screen and mark which give bright vs dark fringes.

## Common Misconceptions
Path difference is NOT the same as distance from one source; it is the difference between distances to the two sources.

## Questions

```yaml
- question: "A listener is 3.0 m from one speaker and 4.0 m from a second speaker. Both emit sound with a wavelength of 1.0 m. What type of interference does the listener experience?"
  type: multiple-choice
  options:
    - "Constructive, because the path difference is 1.0 m, which equals one full wavelength"
    - "Destructive, because the average distance of 3.5 m is not a whole-number multiple of λ"
    - "Constructive, because the nearest speaker is only 3.0 m away, which is 3λ"
    - "Destructive, because the path difference of 1.0 m is less than the distance to either source"
  answer: 0
  explanation: "Path difference Δ = 4.0 − 3.0 = 1.0 m = 1λ. Since Δ = nλ (with n = 1), constructive interference occurs. The critical mistake in options B–D is using individual distances or averages instead of the difference. Only the difference between the two path lengths determines whether waves arrive in phase or out of phase."

- question: "Two coherent wave sources produce waves with wavelength 0.4 m. At a detector, the path difference is 0.6 m. What is the interference condition?"
  type: multiple-choice
  options:
    - "Destructive, because 0.6 m = 1.5λ, satisfying Δ = (n + ½)λ with n = 1"
    - "Constructive, because 0.6 m is less than one full wavelength"
    - "Constructive, because 0.6 m ≈ 1.5λ, which is 'close enough' to a whole-number multiple"
    - "Indeterminate — only Δ = 0 guarantees a predictable interference condition"
  answer: 0
  explanation: "0.6 m / 0.4 m = 1.5, so Δ = 1.5λ = (1 + ½)λ, the destructive interference condition. Option B confuses magnitude with the interference criterion — what matters is not how large Δ is, but whether it equals nλ or (n + ½)λ. Option C is wrong because 'close enough' has no meaning here; the condition must be satisfied exactly for perfect cancellation."

- question: "Constructive interference can occur at a point equidistant from both sources."
  type: true-false
  answer: true
  explanation: "At any point equidistant from both sources, the path difference Δ = 0, which satisfies Δ = nλ with n = 0. This is the zeroth-order constructive maximum — the central bright fringe in a double-slit experiment. Zero path difference means the two waves are perfectly in phase because neither has traveled any extra distance."

- question: "The path difference at any given point equals the distance from the nearer source to that point."
  type: true-false
  answer: false
  explanation: "Path difference is the *difference* between the two path lengths, not either path length alone. If one source is 3 m away and the other is 5 m away, the path difference is 2 m — not 3 m or 5 m. Confusing path difference with a single distance is the most common error in interference problems, and it leads to completely wrong predictions about which points are bright or dark."

- question: "Why is it the *difference* in path lengths — rather than the individual path lengths themselves — that determines whether interference is constructive or destructive?"
  type: short-answer
  answer: "Two coherent sources start in phase. Any extra distance one wave travels corresponds to extra cycles it completes before reaching the detector. If the extra distance (the path difference) is a whole number of wavelengths, the wave arrives having completed full extra cycles and is back in phase — constructive. If the extra distance is a half-plus-integer number of wavelengths, it arrives exactly half a cycle off — destructive. The absolute distance from either source doesn't matter because it contributes equally to both waves' phase; only the *difference* shifts one wave relative to the other."
  explanation: "Phase is set by how many wavelengths fit into the path. Since both waves start in phase, what matters is whether the extra path of the farther wave corresponds to a whole number of wavelengths (back in phase) or a half-integer number (inverted). The individual distances only matter insofar as their difference reveals this extra cycle count."
```

## Explainer

You've already worked with **phase** — the idea that a wave oscillates between peaks and troughs, and that two waves can be aligned (in phase) or offset (out of phase) depending on where they are in their cycles. You've also seen that when two sources emit waves, the interference pattern at a point depends on how the waves from those two sources overlap there. Path-length difference analysis is the geometric tool that connects the *spatial arrangement* of sources and observers to the *phase relationship* at any point — without needing to track phases explicitly.

The central idea is direct: if two coherent sources emit identical waves, and a detector is closer to one source than the other, the wave from the farther source has been traveling longer and has gone through more cycles. The **path length difference** Δ = d₁ − d₂ is the extra distance the farther wave travels compared to the nearer one. If that extra distance is exactly one full wavelength (Δ = λ), the farther wave has completed one extra full cycle — arriving perfectly back in phase with the nearer wave. The waves reinforce: **constructive interference**. If the extra distance is half a wavelength (Δ = λ/2), the farther wave arrives exactly one half-cycle out of phase — crest meets trough — and the waves cancel: **destructive interference**.

The general rules are clean. Constructive interference occurs when Δ = nλ, where n is any integer (0, 1, 2, 3, ...) — meaning the path difference is zero, one wavelength, two wavelengths, and so on. Destructive interference occurs when Δ = (n + ½)λ — half a wavelength, one and a half, two and a half, and so on. This gives you a purely geometric way to predict interference: measure two distances, take their difference, compare to the wavelength. No phase arithmetic required.

The key error to avoid is conflating path difference with distance to a single source. If you're standing 3 m from one speaker and 4 m from another, your path difference is 1 m — not 3 m or 4 m. It's the *difference* that drives interference. This analysis works identically for sound waves in air, water waves in a tank, and light from two slits — the wavelength changes dramatically across these systems, but the principle is the same. Path-difference geometry becomes the foundation of all two-source and multi-source interference problems that follow, including double-slit bright and dark fringe locations.
