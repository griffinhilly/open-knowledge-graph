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
stage: formal-systems
status: draft
---

# Diffraction Gratings: Construction, Spectra, and Spectroscopy

## Core Idea
Diffraction gratings have many slits (hundreds to thousands per mm), producing narrow, sharp maxima when path difference equals integer wavelengths: d sin θ = mλ. They disperse light by wavelength, making them essential for spectroscopy. Higher orders give better wavelength resolution but lower intensity.

## Explainer

From your study of two-source interference, you know that when two coherent sources are separated by a distance, they produce a pattern of bright maxima and dark minima based on path difference. A diffraction grating extends this to hundreds or thousands of slits, and the effect on the bright fringes is dramatic: they become extraordinarily narrow and sharp. Here is why. With two slits, a fringe begins to fade gradually as you move off the maximum condition. With N slits, destructive interference from many slit pairs kills the intensity almost immediately on either side of a maximum, leaving an extremely narrow bright line. More slits means sharper peaks.

The **grating equation** d sin θ = mλ is identical in form to the two-slit condition — it just redefines d as the spacing between adjacent slits (the grating spacing, equal to 1 divided by the number of lines per unit length). The integer m is the **diffraction order**: m = 0 is the straight-through beam, m = 1 is the first-order maximum on either side, m = 2 is the second-order, and so on. Higher orders appear at larger angles because a larger path difference is needed to reach the next integer multiple of λ.

The real power of gratings for spectroscopy comes from the wavelength-dependence of θ. Because different wavelengths satisfy d sin θ = mλ at different angles, a grating physically separates white light into its component wavelengths — it disperses the spectrum. This is exactly what a prism does via refraction, but a grating does it by interference and can achieve far higher **angular dispersion** and **resolving power**. The resolving power R = mN tells you how finely a grating can separate two nearby wavelengths: m is the order and N is the total number of illuminated slits. A grating with 1000 slits used in second order can resolve wavelengths differing by as little as 1 part in 2000.

The trade-off in choosing diffraction order is important for practical spectroscopy. Higher orders (larger m) give more angular separation between wavelengths, making them easier to distinguish — but the intensity falls off in higher orders because energy is spread across more maxima. First-order is usually the most intense; many spectrometers use it exclusively. When you see the iridescent colors on a CD or the spectral bands from a diffraction grating card, you are seeing first-order diffraction: each wavelength of white light scattered to a slightly different angle, your eye interpreting the angular spread as a rainbow of colors.
