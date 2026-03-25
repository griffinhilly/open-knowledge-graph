---
id: bright-fringes-dark-fringes-spacing
title: Fringe Spacing in Interference Patterns
domain: physics
course: waves-and-optics
prerequisites:
- id: path-length-difference-analysis
  type: hard
- id: beats-and-beat-frequency
  type: soft
builds-toward:
- double-aperture-interference-fringe
tags:
- interference
- patterns
stage: advanced
status: validated
---
# Fringe Spacing in Interference Patterns

## Core Idea
The separation between adjacent bright fringes (fringe spacing Δy = λD/d) depends on wavelength, distance to screen (D), and source separation (d). Longer wavelengths and greater distances produce wider fringes; closer sources also widen fringes. This relationship quantifies the diffraction-like spreading of interference patterns.

## Questions

```yaml
- question: "In a double-slit experiment, the slit separation d is doubled while wavelength and screen distance are held constant. What happens to the fringe spacing?"
  type: multiple-choice
  options:
    - "It doubles — wider slits spread the pattern out"
    - "It halves — fringes crowd together when slits are farther apart"
    - "It stays the same — slit separation does not affect fringe spacing"
    - "It quadruples — fringe spacing scales with d²"
  answer: 1
  explanation: "From Δy = λD/d, doubling d halves the fringe spacing. This surprises many students who expect wider-apart slits to spread the fringes out (by analogy with a wider spray). The logic runs the other way: when slits are farther apart, only a tiny angle is needed for the path difference to reach one full wavelength, so fringes are compressed. The key insight is that d is in the denominator."

- question: "A double-slit experiment uses slits separated by d = 0.50 mm and a screen at D = 1.5 m. The observed fringe spacing is Δy = 1.5 mm. What wavelength does this imply?"
  type: multiple-choice
  options:
    - "250 nm — visible violet"
    - "500 nm — visible green"
    - "750 nm — near infrared"
    - "1500 nm — infrared, outside visible range"
  answer: 1
  explanation: "Rearranging Δy = λD/d gives λ = Δy·d/D = (1.5×10⁻³ m × 0.50×10⁻³ m) / 1.5 m = 5.0×10⁻⁷ m = 500 nm — green light. This calculation shows how early experimenters used fringe measurements to determine wavelengths of visible light from purely geometric measurements."

- question: "Increasing the distance D between the double-slit and the screen makes the fringes wider."
  type: true-false
  answer: true
  explanation: "Yes — from Δy = λD/d, fringe spacing is directly proportional to D. Moving the screen farther away amplifies any angular spacing into greater physical separation. The fringes get broader without the pattern itself changing; you are just projecting it onto a more distant surface."

- question: "Using a longer-wavelength (red) light source instead of a shorter-wavelength (blue) source will make the fringes closer together in a double-slit experiment."
  type: true-false
  answer: false
  explanation: "Longer wavelength produces wider fringe spacing — λ is in the numerator of Δy = λD/d. Red light (λ ≈ 700 nm) produces broader fringes than blue light (λ ≈ 450 nm) under the same geometry. This is why white-light double-slit patterns show different colors offset from each other: each wavelength has its own spacing."

- question: "How can the fringe-spacing formula Δy = λD/d be used to measure an unknown wavelength of light, and which quantities must be measured experimentally?"
  type: short-answer
  answer: "Rearranging gives λ = Δy·d/D. The experimentally measured quantities are the fringe spacing Δy (measured on the screen), the slit separation d (known from the apparatus), and the slit-to-screen distance D (measured with a ruler). Plugging these in yields the wavelength."
  explanation: "This is how early experimenters determined visible light wavelengths well before quantum theory — purely from geometry and a measured fringe pattern. The same relationship runs in reverse in modern spectroscopy: known wavelengths calibrate the geometry of the apparatus."
```

## Explainer

From your study of path-length difference analysis, you know that two coherent waves produce a bright fringe wherever their path lengths differ by an integer number of wavelengths (Δℓ = mλ), and a dark fringe wherever they differ by a half-integer (Δℓ = (m + ½)λ). Fringe spacing takes the next step: instead of asking *where* a fringe occurs in terms of path difference, it asks *how far apart* adjacent fringes are on the screen in actual distance units.

The geometry connects path difference to screen position. For a double slit with separation *d* and a screen at distance *D*, a point at height *y* on the screen subtends a small angle θ ≈ y/D. The path difference between the two rays at that point is approximately Δℓ ≈ d·sinθ ≈ d·y/D for small angles. Setting successive bright-fringe conditions equal — d·y_m/D = mλ and d·y_(m+1)/D = (m+1)λ — and subtracting gives the **fringe spacing formula**: Δy = λD/d. This single equation captures all the geometry.

Each variable tells an intuitive story. Larger wavelength λ means the path-difference condition is met at wider angular separations, spreading the fringes out. Larger screen distance D amplifies any angular spacing into greater physical distance, again widening fringes. Larger slit separation d means the two slits are farther apart, so a much smaller angle is enough to accumulate a full wavelength of path difference — fringes crowd together. You can remember the pattern as: "spread the waves or spread the screen and fringes widen; spread the sources and fringes narrow."

A practical consequence is that fringe spacing gives a way to measure wavelength. If you set up a double slit of known separation, measure D with a ruler, and measure Δy from the pattern, you can solve λ = Δy·d/D. This is how early experimenters determined the wavelengths of visible light. Conversely, in modern spectroscopy the same relationship is used in reverse: known λ is used to calibrate the geometry of the apparatus. The formula is also the foundation for understanding why different colors in white light produce overlapping but offset fringe patterns — each wavelength has its own spacing.
