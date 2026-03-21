---
id: diffraction-gratings-applications
title: 'Diffraction Gratings: Construction, Spectra, and Spectroscopy'
domain: physics
course: waves-and-optics
prerequisites:
- id: diffraction-gratings
  type: soft
- id: two-source-interference-patterns
  type: hard
builds-toward:
- spectroscopy-applications
tags:
- diffraction-grating
- spectroscopy
- grating-equation
stage: advanced
status: draft
---

# Diffraction Gratings: Construction, Spectra, and Spectroscopy

## Core Idea
Diffraction gratings have many slits (hundreds to thousands per mm), producing narrow, sharp maxima when path difference equals integer wavelengths: d sin θ = mλ. They disperse light by wavelength, making them essential for spectroscopy. Higher orders give better wavelength resolution but lower intensity.

## Questions

```yaml
- question: "You replace a diffraction grating with 500 slits with one having 1000 slits, keeping the slit spacing d the same. What changes in the diffraction pattern?"
  type: multiple-choice
  options:
    - "New bright maxima appear at new angles, and the peaks get sharper"
    - "The angles of the bright maxima are unchanged, but the peaks become sharper and more intense per unit angle"
    - "The grating equation changes, so the bright maxima shift to new angles"
    - "The pattern becomes dimmer overall because more slits divide the light into more beams"
  answer: 1
  explanation: "The positions of bright maxima are determined by d sin θ = mλ. Since d and λ are unchanged, the angles of the maxima don't change. What changes is the sharpness: with more slits, destructive interference from the many slit pairs eliminates intensity almost immediately on either side of each maximum, producing much narrower peaks. The resolving power R = mN also doubles (from 500N to 1000N for order m), meaning the grating can now separate wavelengths twice as close together. More slits = sharper peaks at the same locations, not new peaks."

- question: "A diffraction grating with N = 800 slits is used in the third diffraction order. What is its resolving power?"
  type: multiple-choice
  options:
    - "800"
    - "2400"
    - "267"
    - "It depends on the wavelength being resolved"
  answer: 1
  explanation: "Resolving power R = mN = 3 × 800 = 2400. This means the grating can just resolve two wavelengths λ and λ + Δλ when λ/Δλ = 2400 — it can distinguish wavelengths differing by as little as 1 part in 2400. Resolving power depends on the order m and total number of slits N, not directly on the wavelength. Higher order and more slits both increase resolving power, which is why spectrometers are designed to use many slits and sometimes higher orders."

- question: "Using a diffraction grating in a higher diffraction order (m = 2 rather than m = 1) increases angular dispersion between wavelengths, but the intensity of the maxima decreases."
  type: true-false
  answer: true
  explanation: "Both statements are correct. The grating equation d sin θ = mλ shows that at higher order m, the same wavelength difference Δλ produces a larger angle difference Δθ — better angular separation. Resolving power R = mN also increases with m. However, the intensity falls off in higher orders because the total energy is being distributed across more maxima, and single-slit diffraction envelope effects reduce intensity at larger angles. First-order is typically the most intense; spectrometers often use it exclusively, accepting lower resolving power in exchange for intensity."

- question: "A diffraction grating with more slits produces more bright maxima at more angles than a grating with fewer slits."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The positions of the bright maxima are determined solely by d sin θ = mλ — only the slit spacing d and wavelength λ matter, not the number of slits. More slits produce the same maxima at the same angles, but sharper. The effect of adding more slits is to increase destructive interference between the maxima, narrowing each peak without adding new ones. The number of possible orders is limited by the condition sin θ ≤ 1, not by the number of slits."

- question: "Why do more slits in a diffraction grating produce sharper peaks rather than more peaks?"
  type: short-answer
  answer: "Each additional slit adds a new source of destructive interference between the bright maxima. With N slits, there are N-1 zeros between consecutive orders. A small deviation from the maximum angle causes waves from pairs of slits to be slightly out of phase, and with many slits, these partial cancellations sum to nearly complete destructive interference very quickly on either side of the maximum. With only 2 slits, the cancellation is gradual; with 1000 slits, it is rapid, leaving a very narrow bright line at each maximum. Peak positions (from d sin θ = mλ) are unchanged; only peak width narrows."
  explanation: "The mathematical reason is that the intensity pattern for N slits is proportional to sin²(Nδ/2)/sin²(δ/2), where δ is the phase difference between adjacent slits. At the bright maximum δ = 2πm, this expression equals N². Just off the maximum, sin(Nδ/2) oscillates rapidly through zero as N increases, producing the sharp destructive minima. The width of the central peak scales as 1/N — exactly why resolving power R = mN grows with N. More slits narrow the peaks without shifting them."
```

## Explainer

From your study of two-source interference, you know that when two coherent sources are separated by a distance, they produce a pattern of bright maxima and dark minima based on path difference. A diffraction grating extends this to hundreds or thousands of slits, and the effect on the bright fringes is dramatic: they become extraordinarily narrow and sharp. Here is why. With two slits, a fringe begins to fade gradually as you move off the maximum condition. With N slits, destructive interference from many slit pairs kills the intensity almost immediately on either side of a maximum, leaving an extremely narrow bright line. More slits means sharper peaks.

The **grating equation** d sin θ = mλ is identical in form to the two-slit condition — it just redefines d as the spacing between adjacent slits (the grating spacing, equal to 1 divided by the number of lines per unit length). The integer m is the **diffraction order**: m = 0 is the straight-through beam, m = 1 is the first-order maximum on either side, m = 2 is the second-order, and so on. Higher orders appear at larger angles because a larger path difference is needed to reach the next integer multiple of λ.

The real power of gratings for spectroscopy comes from the wavelength-dependence of θ. Because different wavelengths satisfy d sin θ = mλ at different angles, a grating physically separates white light into its component wavelengths — it disperses the spectrum. This is exactly what a prism does via refraction, but a grating does it by interference and can achieve far higher **angular dispersion** and **resolving power**. The resolving power R = mN tells you how finely a grating can separate two nearby wavelengths: m is the order and N is the total number of illuminated slits. A grating with 1000 slits used in second order can resolve wavelengths differing by as little as 1 part in 2000.

The trade-off in choosing diffraction order is important for practical spectroscopy. Higher orders (larger m) give more angular separation between wavelengths, making them easier to distinguish — but the intensity falls off in higher orders because energy is spread across more maxima. First-order is usually the most intense; many spectrometers use it exclusively. When you see the iridescent colors on a CD or the spectral bands from a diffraction grating card, you are seeing first-order diffraction: each wavelength of white light scattered to a slightly different angle, your eye interpreting the angular spread as a rainbow of colors.
