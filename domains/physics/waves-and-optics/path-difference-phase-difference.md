---
id: path-difference-phase-difference
title: Path Difference and Phase Difference in Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relation
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
stage: advanced
status: validated
---

# Path Difference and Phase Difference in Waves

## Core Idea
Path difference Δx between two wave sources creates a phase difference Δφ = 2πΔx/λ. Constructive interference occurs when Δx = nλ (phase difference = 2πn), while destructive interference occurs when Δx = (n + ½)λ (phase difference = (2n + 1)π).

## How It's Best Learned
Use phasor diagrams to visualize how phase differences add. Calculate path differences for two-point sources and predict interference patterns.

## Common Misconceptions
- Thinking path difference and phase difference are the same thing; they're related by wavelength.
- Assuming constructive interference always increases amplitude; this is true for coherent waves.

## Questions

```yaml
- question: "Two coherent wave sources reach point P: Wave 1 travels 3.0 m and Wave 2 travels 3.5 m. The wavelength is 0.5 m. What type of interference occurs at P?"
  type: multiple-choice
  options:
    - "Destructive — the path difference of 0.5 m produces a phase difference of π"
    - "Constructive — the path difference equals exactly one wavelength, giving a phase difference of 2π"
    - "Neither — a phase difference of 2π means the waves are out of phase"
    - "Partially constructive — 0.5 m path difference never produces full constructive interference"
  answer: 1
  explanation: "Path difference Δx = 3.5 − 3.0 = 0.5 m = 1 wavelength (since λ = 0.5 m). Phase difference Δφ = 2πΔx/λ = 2π(1) = 2π. A phase difference of 2π means the waves are exactly in phase — their peaks and troughs align — producing constructive interference. The most common error is confusing a phase difference of 2π (full cycle, in phase) with π (half cycle, out of phase)."

- question: "Two coherent sources each produce waves with a path difference of 6 cm to point P. Source A has wavelength 2 cm; Source B has wavelength 4 cm. At which source does the path difference produce constructive interference at P?"
  type: multiple-choice
  options:
    - "Source A only — Δx/λ = 3 (integer), giving full constructive interference; Source B has Δx/λ = 1.5 (half-integer), giving destructive interference"
    - "Source B only — the longer wavelength is less sensitive to path differences"
    - "Both sources — the same path difference always produces the same type of interference"
    - "Neither source — 6 cm is too large a path difference for either wavelength"
  answer: 0
  explanation: "For Source A: Δx/λ = 6/2 = 3 (integer multiple of λ) → constructive. For Source B: Δx/λ = 6/4 = 1.5 (half-integer multiple) → destructive. The same path difference produces different interference outcomes for different wavelengths. This is why 'path difference' and 'type of interference' cannot be connected without knowing the wavelength — the conversion Δφ = 2πΔx/λ is the essential link."

- question: "A path difference of exactly one wavelength always produces constructive interference, regardless of the wavelength's actual value."
  type: true-false
  answer: true
  explanation: "If Δx = λ, then Δφ = 2πΔx/λ = 2π(λ/λ) = 2π. A phase difference of 2π is a full cycle — the two waves arrive perfectly in phase. This is true for any wavelength: what matters is the ratio Δx/λ, not the absolute values. A path difference of one wavelength always means full constructive interference."

- question: "Path difference and phase difference are the same quantity measured in different units — one in meters, one in radians."
  type: true-false
  answer: false
  explanation: "Path difference (Δx, in meters) and phase difference (Δφ, in radians) measure fundamentally different things, and the conversion between them depends on wavelength: Δφ = 2πΔx/λ. The same path difference of 1 meter produces a phase difference of 2π for λ = 1 m, but a phase difference of 4π for λ = 0.5 m. They are not simply different units for the same quantity — wavelength is a necessary factor in the conversion."

- question: "Point P has a path difference of 450 nm from two coherent sources with wavelength λ = 300 nm. Determine whether P is a bright or dark fringe and explain how the path difference–wavelength relationship leads to that conclusion."
  type: short-answer
  answer: "Δx/λ = 450/300 = 1.5, which is a half-integer (n + ½ for n = 1). Therefore Δφ = 2π(1.5) = 3π, an odd multiple of π. This means the waves arrive exactly out of phase — a peak of one aligns with a trough of the other — producing destructive interference. Point P is a dark fringe. The key step is computing Δx/λ: if the result is an integer, it's a bright fringe; if it's a half-integer, it's a dark fringe."
  explanation: "The ratio Δx/λ is the central quantity in interference analysis. It tells you how many wavelengths of path difference exist, which directly determines whether the waves arrive in phase or out of phase. Students who memorize the conditions (nλ for constructive, (n+½)λ for destructive) without computing this ratio often make sign errors or apply the wrong condition."
```

## Explainer

You already know two things: waves have a wavelength λ that defines the periodic scale of the disturbance, and when two waves overlap, they superpose — their displacements add algebraically at every point. **Path difference** and **phase difference** are the tools that connect these two ideas. They let you take a geometric fact (two waves traveled different distances to reach a point) and turn it into a prediction (what does the superposition look like there?).

The key insight is that a wavelength is the distance over which a wave completes one full cycle. If one wave travels exactly one wavelength farther than another before reaching the same point, it arrives shifted by one full cycle — which is no shift at all. The two waves are back in sync, and their peaks align. If one travels exactly half a wavelength farther, it arrives shifted by half a cycle — now peaks align with troughs, and they cancel. **Path difference** Δx is the extra distance one wave travels; **phase difference** Δφ is the resulting phase offset between them. The conversion is Δφ = 2πΔx/λ: each additional wavelength of path difference adds 2π to the phase difference (one full cycle).

The constructive and destructive interference conditions follow directly. Constructive interference requires Δx = nλ for any integer n — the path difference is a whole number of wavelengths, so the phase difference is a multiple of 2π, meaning the waves arrive in phase and their amplitudes add. Destructive interference requires Δx = (n + ½)λ — the path difference is a half-integer number of wavelengths, so the phase difference is an odd multiple of π, meaning the waves arrive perfectly out of phase and cancel.

These two conditions are the foundation for all two-source interference analysis — the double-slit experiment, diffraction gratings, and antenna arrays all reduce to this same path-difference geometry. When you analyze two sources and a point P somewhere in space, you measure the distances r₁ and r₂ from each source to P, compute Δx = |r₁ − r₂|, and ask whether that value is a whole or half-integer multiple of λ. The phase difference formula Δφ = 2πΔx/λ translates spatial geometry into wave behavior. Mastering this translation is what makes interference problems tractable rather than mysterious.
