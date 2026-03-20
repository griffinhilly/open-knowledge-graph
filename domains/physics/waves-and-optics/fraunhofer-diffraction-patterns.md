---
id: fraunhofer-diffraction-patterns
title: 'Fraunhofer Diffraction: Far-Field Diffraction Patterns'
domain: physics
course: waves-and-optics
prerequisites:
- id: single-slit-diffraction
  type: hard
- id: diffraction-and-huygen-principle
  type: soft
builds-toward:
- diffraction-gratings
tags:
- fraunhofer-diffraction
- far-field
- diffraction-pattern
stage: advanced
status: draft
---

# Fraunhofer Diffraction: Far-Field Diffraction Patterns

## Core Idea
Fraunhofer diffraction occurs when the source and observation screen are far from the diffracting aperture (parallel incident light), producing diffraction patterns determined by Fourier transform of the aperture. Slit width a produces minima at angles where sin θ = nλ/a (n ≠ 0).

## Explainer

From your study of single-slit diffraction and Huygens' principle, you know that every point on a wavefront acts as a source of secondary wavelets. When a wave passes through a slit, all the points across the slit opening emit wavelets, and the observed intensity at any downstream point is determined by how those wavelets interfere. The challenge is that the geometry of the interference depends on exactly how far the screen is from the slit. **Fraunhofer diffraction** is the simplifying limit where the screen is far enough away that you can treat the rays reaching any single point on the screen as effectively parallel — the **far-field** regime.

In this limit, the math becomes clean. The phase difference between a wavelet from the slit's center and one from a point a distance y from the center is simply φ = (2πy/λ) sin θ. To find the total amplitude at angle θ, you sum the contributions from all points across the slit — which, as the slit width becomes a continuous aperture, is an integral. This integral is precisely the **Fourier transform** of the aperture function (the function describing where the slit is open). For a rectangular slit of width a, the transform gives a sinc-function amplitude, and the intensity pattern is sinc²: a bright central maximum flanked by weaker secondary maxima, with dark minima wherever sin θ = nλ/a (n = 1, 2, 3, ...). Notice that the central bright fringe is twice as wide as each secondary maximum — a distinctive signature of single-slit Fraunhofer diffraction.

The Fourier transform connection is more than mathematical elegance. It reveals a fundamental reciprocal relationship: a **narrow** slit (small a) produces a **wide** diffraction pattern, and a **wide** slit produces a **narrow** pattern. This is a spatial analogue of the Heisenberg uncertainty principle: localizing a wave more tightly in space spreads it more broadly in angle. The same principle explains why a telescope with a larger aperture resolves finer angular detail — a wider aperture produces a narrower diffraction limit — and why radio telescopes must be enormous to achieve angular resolution comparable to optical telescopes operating at much shorter wavelengths.

When light passes through two slits, an array of slits, or any complex aperture, the Fraunhofer pattern is always the magnitude-squared of the Fourier transform of that aperture. This is why diffraction gratings — arrays of many closely-spaced slits — produce extremely sharp maxima: the Fourier transform of a periodic array (a comb function) is another comb function, with energy concentrated into sharp, widely-spaced peaks. Understanding Fraunhofer diffraction is therefore the gateway to understanding both diffraction gratings and how scientists use X-ray diffraction to determine crystal structures, where the atomic lattice acts as the diffracting aperture.
