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
status: draft
---

# Young's Double-Slit Experiment and Analysis

## Core Idea
Two slits act as coherent sources, producing a characteristic pattern of vertical bright and dark fringes on a distant screen. The fringe spacing is λD/d, where D is the distance to the screen and d is the slit separation. This experiment demonstrates the wave nature of light and provides a method to measure wavelength.

## How It's Best Learned
Derive the positions of bright fringes using path difference geometry and the condition for constructive interference.

## Common Misconceptions
The double slit does not create the interference pattern—the two coherent waves created by diffraction at each slit interfere to form the pattern.

## Explainer

You already know the conditions for bright and dark fringes: **constructive interference** occurs when two waves arrive in phase (path difference = nλ), and **destructive interference** when they arrive out of phase (path difference = (n + ½)λ). Young's double-slit experiment is the classic setup that makes these conditions physically visible as a repeating pattern of light and dark stripes on a distant screen — and it is worth understanding the geometry that produces the formula, not just memorizing the formula itself.

Here is the setup: two narrow, closely spaced slits are illuminated by coherent light (light with a stable phase relationship, so the waves from each slit stay synchronized). Each slit acts as a new source of spreading waves through diffraction. These two coherent wave fronts overlap in the space beyond the slits. At any point on a distant screen, waves from the two slits have traveled slightly different distances. That **path difference** determines whether they arrive in phase or out of phase. Along the central axis — directly in front of the midpoint between the slits — the path difference is zero, giving perfect constructive interference and the **central bright fringe**. Moving up or down from center, the path difference grows. The first bright fringe (order m = 1) appears where path difference equals exactly one wavelength (λ); the first dark fringe appears where it equals half a wavelength (λ/2).

This geometry produces a regular, symmetric ladder of bright and dark bands with a constant spacing. The **fringe spacing** formula Δy = λD/d connects the measurable geometry (screen distance D, slit separation d) to the wavelength λ. Shorter-wavelength (bluer) light produces more tightly packed fringes; longer-wavelength (redder) light produces more widely spaced fringes. By measuring the fringe spacing and the geometry, you can solve for λ — which is how wavelength was measured precisely long before modern instruments existed.

The deepest lesson is historical and conceptual: at the start of the 19th century, this experiment settled the wave-versus-particle debate in favor of the wave model of light. Particles don't interfere — if you shot bullets through two slits, you'd get two stripes on the wall behind them, not a multi-stripe pattern. The fact that light creates many alternating bright and dark fringes is direct evidence of its wave nature. When you observe a double-slit pattern, you are watching wavelengths add and cancel across space, made visible as light and shadow.
