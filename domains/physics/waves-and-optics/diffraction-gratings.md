---
id: diffraction-gratings
title: Diffraction Gratings
domain: physics
course: waves-and-optics
prerequisites:
- id: youngs-double-slit
  type: hard
- id: single-slit-diffraction
  type: soft
- id: electromagnetic-spectrum
  type: soft
tags:
- diffraction grating
- spectroscopy
- principal maxima
- resolving power
stage: advanced
status: validated
---
# Diffraction Gratings

## Core Idea
A diffraction grating contains thousands of equally spaced slits. The many coherent sources interfere to produce extremely sharp, bright principal maxima at dsinθ = mλ (same condition as double slit). Because maxima are so narrow, different wavelengths are well-separated angularly, making gratings ideal spectrometers. The resolving power R = mN (where N is the number of slits) determines how closely spaced two wavelengths can be and still be distinguished.

## How It's Best Learned
Use a diffraction grating to observe the spectrum of white light and hydrogen discharge tube. Measure the angular positions of spectral lines and back-calculate wavelengths. Compare resolution to a prism spectrometer.

## Common Misconceptions
- A grating does not separate colors by dispersion (like a prism); it works by interference, and different wavelengths have maxima at different angles for the same grating equation.
- Higher grating orders give greater angular separation but also require more grating lines to maintain resolution.

## Explainer

You already know from Young's double-slit experiment that two coherent sources produce an interference pattern with bright fringes wherever the path difference is an integer multiple of the wavelength: d sin θ = mλ. A diffraction grating extends this idea to thousands of slits — a typical grating has 500 to 1,200 slits per millimeter. The grating equation d sin θ = mλ is identical to the double-slit condition, so the bright maxima appear at exactly the same angles. What changes dramatically is the *sharpness* of those maxima.

With only two slits, the bright fringes are broad — intensity falls off gradually on either side of each maximum. With N slits all contributing coherently, the constructive interference peak becomes extraordinarily narrow. Think of it this way: if you are just a fraction of a degree away from the exact maximum angle, a wave from slit 1 and a wave from slit N/2 (halfway across the grating) are slightly out of phase. With two slits this barely matters; with 600 slits per millimeter, these small phase errors accumulate and the combined amplitude drops steeply to zero. The result is that the **principal maxima** are bright and razor-sharp, while everything between them is dark.

That sharpness is what makes gratings ideal for **spectroscopy**. Two wavelengths λ₁ and λ₂ that are close together produce principal maxima at slightly different angles. If the fringes are sharp enough, those two maxima are distinguishable — the wavelengths are *resolved*. The **resolving power** R = mN tells you quantitatively: in diffraction order m with N illuminated slits, you can distinguish two wavelengths separated by as little as Δλ = λ/R. More slits and higher orders both improve resolution, which is why real spectrographs are sized to illuminate as many grating lines as possible.

It is important not to confuse a diffraction grating with a prism. A prism separates colors because its refractive index varies with wavelength (dispersion) — different colors bend by different amounts. A grating separates colors because the grating equation d sin θ = mλ makes the constructive interference angle proportional to wavelength — longer wavelengths diffract at larger angles. The physics is entirely different: dispersion versus interference. In practice, gratings are preferred for precision spectroscopy because their angular dispersion is more uniform and their resolving power scales predictably with N, whereas prism dispersion is nonlinear and harder to calibrate.
