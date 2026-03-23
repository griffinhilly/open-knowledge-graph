---
id: double-aperture-interference-fringe
title: Young's Double-Slit Experiment and Analysis
domain: physics
course: waves-and-optics
prerequisites:
- id: bright-fringes-dark-fringes-spacing
  type: hard
builds-toward:
- multiple-slit-grating-equation
- single-aperture-diffraction-minima
tags:
- interference
- experiment
- light
stage: advanced
status: validated
---

# Young's Double-Slit Experiment and Analysis

## Core Idea
Two slits act as coherent sources, producing a characteristic pattern of vertical bright and dark fringes on a distant screen. The fringe spacing is λD/d, where D is the distance to the screen and d is the slit separation. This experiment demonstrates the wave nature of light and provides a method to measure wavelength.

## How It's Best Learned
Derive the positions of bright fringes using path difference geometry and the condition for constructive interference.

## Common Misconceptions
The double slit does not create the interference pattern—the two coherent waves created by diffraction at each slit interfere to form the pattern.

## Questions

```yaml
- question: "In a double-slit experiment, you double the slit separation d while keeping the screen distance D and wavelength λ unchanged. What happens to the fringe spacing Δy?"
  type: multiple-choice
  options:
    - "Δy doubles — wider slits spread the light more, creating wider fringes"
    - "Δy stays the same — fringe spacing only depends on wavelength"
    - "Δy halves — slits farther apart produce more tightly packed fringes"
    - "Δy halves — the central maximum broadens but the outer fringes compress"
  answer: 2
  explanation: "Fringe spacing is Δy = λD/d. Doubling d with λ and D held constant halves Δy. The intuition: when slits are farther apart, the path difference grows more rapidly as you move off-center, so constructive and destructive interference conditions occur more frequently — fringes are packed closer together. The common misconception is option A — confusing double-slit interference with diffraction, where wider slits do spread light more. In double-slit interference, d is in the denominator: larger separation → smaller spacing."

- question: "A double-slit experiment is run first with red light (λ = 700 nm) and then with blue light (λ = 450 nm), with all other parameters held constant. Which result is correct?"
  type: multiple-choice
  options:
    - "Blue light produces wider fringe spacing because it has higher energy"
    - "Red light produces wider fringe spacing because longer wavelengths create larger path differences per unit angle"
    - "Both produce identical fringe spacing — wavelength affects brightness but not spacing"
    - "Red light produces narrower fringes because it is closer to infrared and spreads less"
  answer: 1
  explanation: "Δy = λD/d — fringe spacing is directly proportional to wavelength. Red light (700 nm) has a larger λ than blue light (450 nm), so it produces wider-spaced fringes. Longer wavelengths require a larger angular separation between adjacent maxima to accumulate path differences of one full wavelength. Option A is wrong: photon energy (E = hf) is higher for blue light, but energy has no direct effect on fringe spacing. Options C and D reflect confusions between energy, frequency, and wavelength."

- question: "In Young's double-slit experiment, the two slits themselves generate the interference pattern through the specific way they are cut."
  type: true-false
  answer: false
  explanation: "The slits don't 'create' the pattern — they act as two coherent sources of spreading waves through diffraction. It is the superposition of these two wave fronts in the space beyond the slits that produces the interference pattern. Any two coherent sources with the same geometry would produce the same pattern. The slits simply enforce the condition that the two sources have a stable phase relationship (coherence) and a fixed separation d. Without coherence — such as using two independent light bulbs — no stable pattern would form even with two openings."

- question: "At the central bright fringe in a double-slit pattern, the path difference from the two slits to that point is exactly zero."
  type: true-false
  answer: true
  explanation: "The central maximum (m = 0) occurs along the axis of symmetry, exactly equidistant from both slits. Because both waves travel identical distances, the path difference is zero, meaning they arrive perfectly in phase and interfere constructively to produce the brightest fringe. All other bright fringes (m = ±1, ±2, …) occur where the path difference is an integer number of wavelengths, and dark fringes occur where it is a half-integer multiple."

- question: "Explain why shooting classical particles through two slits would not produce a multi-fringe interference pattern, and what the observation of such a pattern in Young's experiment tells us about the nature of light."
  type: short-answer
  answer: "Classical particles follow definite trajectories and do not superpose — a particle passes through one slit or the other. The result would be two bright stripes on the screen, one behind each slit, with no alternating dark bands. The multi-fringe interference pattern requires that waves from both slits overlap and add or cancel depending on path difference. The fact that light produces this pattern demonstrates that light behaves as a wave, not a stream of classical particles — it is direct evidence of the wave nature of light, which is why Young's 1801 experiment was historically decisive in the wave-particle debate."
  explanation: "The key is that interference requires two waves to be present simultaneously at the same point in space, where they can add constructively or destructively. Particles don't do this — they arrive one at a time at specific locations and do not cancel each other. The interference pattern is a collective, wave phenomenon. Historically, this experiment appeared to settle the debate in favor of the wave model, until the 20th century revealed that light has both wave and particle properties (wave-particle duality)."
```

## Explainer

You already know the conditions for bright and dark fringes: **constructive interference** occurs when two waves arrive in phase (path difference = nλ), and **destructive interference** when they arrive out of phase (path difference = (n + ½)λ). Young's double-slit experiment is the classic setup that makes these conditions physically visible as a repeating pattern of light and dark stripes on a distant screen — and it is worth understanding the geometry that produces the formula, not just memorizing the formula itself.

Here is the setup: two narrow, closely spaced slits are illuminated by coherent light (light with a stable phase relationship, so the waves from each slit stay synchronized). Each slit acts as a new source of spreading waves through diffraction. These two coherent wave fronts overlap in the space beyond the slits. At any point on a distant screen, waves from the two slits have traveled slightly different distances. That **path difference** determines whether they arrive in phase or out of phase. Along the central axis — directly in front of the midpoint between the slits — the path difference is zero, giving perfect constructive interference and the **central bright fringe**. Moving up or down from center, the path difference grows. The first bright fringe (order m = 1) appears where path difference equals exactly one wavelength (λ); the first dark fringe appears where it equals half a wavelength (λ/2).

This geometry produces a regular, symmetric ladder of bright and dark bands with a constant spacing. The **fringe spacing** formula Δy = λD/d connects the measurable geometry (screen distance D, slit separation d) to the wavelength λ. Shorter-wavelength (bluer) light produces more tightly packed fringes; longer-wavelength (redder) light produces more widely spaced fringes. By measuring the fringe spacing and the geometry, you can solve for λ — which is how wavelength was measured precisely long before modern instruments existed.

The deepest lesson is historical and conceptual: at the start of the 19th century, this experiment settled the wave-versus-particle debate in favor of the wave model of light. Particles don't interfere — if you shot bullets through two slits, you'd get two stripes on the wall behind them, not a multi-stripe pattern. The fact that light creates many alternating bright and dark fringes is direct evidence of its wave nature. When you observe a double-slit pattern, you are watching wavelengths add and cancel across space, made visible as light and shadow.
