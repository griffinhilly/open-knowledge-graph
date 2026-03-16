---
id: bright-fringes-dark-fringes-spacing
title: Fringe Spacing in Interference Patterns
domain: physics
course: waves-and-optics
prerequisites:
- id: path-length-difference-analysis
  type: hard
builds-toward:
- double-aperture-interference-fringe
tags:
- interference
- patterns
stage: formal-systems
status: draft
---

# Fringe Spacing in Interference Patterns

## Core Idea
The separation between adjacent bright fringes (fringe spacing Δy = λD/d) depends on wavelength, distance to screen (D), and source separation (d). Longer wavelengths and greater distances produce wider fringes; closer sources also widen fringes. This relationship quantifies the diffraction-like spreading of interference patterns.

## Explainer

From your study of path-length difference analysis, you know that two coherent waves produce a bright fringe wherever their path lengths differ by an integer number of wavelengths (Δℓ = mλ), and a dark fringe wherever they differ by a half-integer (Δℓ = (m + ½)λ). Fringe spacing takes the next step: instead of asking *where* a fringe occurs in terms of path difference, it asks *how far apart* adjacent fringes are on the screen in actual distance units.

The geometry connects path difference to screen position. For a double slit with separation *d* and a screen at distance *D*, a point at height *y* on the screen subtends a small angle θ ≈ y/D. The path difference between the two rays at that point is approximately Δℓ ≈ d·sinθ ≈ d·y/D for small angles. Setting successive bright-fringe conditions equal — d·y_m/D = mλ and d·y_(m+1)/D = (m+1)λ — and subtracting gives the **fringe spacing formula**: Δy = λD/d. This single equation captures all the geometry.

Each variable tells an intuitive story. Larger wavelength λ means the path-difference condition is met at wider angular separations, spreading the fringes out. Larger screen distance D amplifies any angular spacing into greater physical distance, again widening fringes. Larger slit separation d means the two slits are farther apart, so a much smaller angle is enough to accumulate a full wavelength of path difference — fringes crowd together. You can remember the pattern as: "spread the waves or spread the screen and fringes widen; spread the sources and fringes narrow."

A practical consequence is that fringe spacing gives a way to measure wavelength. If you set up a double slit of known separation, measure D with a ruler, and measure Δy from the pattern, you can solve λ = Δy·d/D. This is how early experimenters determined the wavelengths of visible light. Conversely, in modern spectroscopy the same relationship is used in reverse: known λ is used to calibrate the geometry of the apparatus. The formula is also the foundation for understanding why different colors in white light produce overlapping but offset fringe patterns — each wavelength has its own spacing.
