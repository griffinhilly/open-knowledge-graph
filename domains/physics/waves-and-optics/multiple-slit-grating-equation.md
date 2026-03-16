---
id: multiple-slit-grating-equation
title: Diffraction Gratings and the Grating Equation
domain: physics
course: waves-and-optics
prerequisites:
- id: double-aperture-interference-fringe
  type: hard
builds-toward:
- diffraction-resolution-angular-separation
tags:
- diffraction
- gratings
- spectroscopy
stage: formal-systems
status: draft
---

# Diffraction Gratings and the Grating Equation

## Core Idea
A diffraction grating with spacing d between slits produces sharp bright fringes at angles satisfying d sin(θ) = nλ (grating equation). Each order n shows a different color for white light (spectrum), making gratings powerful tools for spectroscopy. Gratings achieve higher resolution than double slits because many slits interfere simultaneously.

## Explainer

From your study of double-slit interference, you know that two slits produce bright fringes wherever the path length difference from the two slits equals a whole number of wavelengths: Δ = nλ. With only two sources, those fringes are broad and relatively dim, because only two waves are reinforcing each other. A **diffraction grating** extends this idea to hundreds or thousands of equally spaced parallel slits, each separated from its neighbors by the same distance d. The bright fringe condition is still Δ = nλ, which gives the grating equation d sin(θ) = nλ — mathematically identical to the double-slit condition, but with a radically different outcome.

The transformative effect of many slits is **sharpness**. When N slits all constructively interfere at angle θ, the resulting fringe is roughly N times narrower and N² times more intense than with two slits. Why? Because any slight deviation from the constructive-interference angle introduces a small phase error in each slit. With two slits, a small error produces only partial destructive interference — the fringe fades gradually. With 1,000 slits, the same small error puts each slit slightly out of phase with the next, and when you sum 1,000 waves with accumulating phase errors, they cancel almost completely. The result is that the bright maxima become narrow spikes separated by nearly dark regions. This is the power of the grating.

The integer n in the equation is the **diffraction order**: n = 0 is straight-through (all wavelengths at the same angle, so no spectral separation), n = ±1 are the first-order maxima, n = ±2 second-order, and so on. Each order fans out white light into a spectrum because d sin(θ) = nλ at different angles for different λ: blue light (shorter λ) bends less than red light (longer λ) at each order. This spectral spread makes gratings the core element of spectrometers — instruments that identify the wavelengths in a light source and hence the chemical composition of the emitting or absorbing material. Every emission spectrum you've seen — the lines of hydrogen, the glow of neon signs — is measured with a diffraction grating.

In solving grating problems, start by identifying d. It may be given as "600 lines per millimeter," meaning d = 1/600 mm ≈ 1.67 μm. Then apply d sin(θ) = nλ for each order of interest. Remember that sin(θ) cannot exceed 1, so the maximum observable order is n_max = floor(d/λ): higher orders would require the diffracted beam to travel at angles beyond 90°, which is physically impossible. For a grating with d = 1.67 μm and red light at λ = 633 nm, n_max = floor(1670/633) = floor(2.64) = 2 — only orders 0, ±1, and ±2 exist.
