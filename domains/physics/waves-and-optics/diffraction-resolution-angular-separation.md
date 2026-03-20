---
id: diffraction-resolution-angular-separation
title: Diffraction Limit and the Rayleigh Criterion
domain: physics
course: waves-and-optics
prerequisites:
- id: single-aperture-diffraction-minima
  type: hard
builds-toward:
- optical-system-magnification
tags:
- resolution
- diffraction
- optics
stage: advanced
status: draft
---

# Diffraction Limit and the Rayleigh Criterion

## Core Idea
The Rayleigh criterion states that two point sources are just resolvable if the central diffraction maximum of one coincides with the first dark fringe of the other. For a circular aperture of diameter D, the minimum resolvable angular separation is θ ≈ 1.22 λ/D. This fundamental limit applies to all optical instruments.

## Explainer

From your study of single-aperture diffraction, you know that a circular opening doesn't produce a point image of a point source — it produces a circular **Airy disk**, a bright central maximum surrounded by alternating dark and bright rings. Every lens, mirror, or aperture in an optical system does this. When two nearby point sources are imaged through the same aperture, each produces its own Airy disk on the detector. If the sources are far apart, the two Airy disks are clearly separated and easily resolved. As they move closer together, the disks begin to overlap. The question becomes: at what point does the combined intensity pattern stop showing two distinct peaks and blur into one?

The **Rayleigh criterion** provides a practical, widely-adopted answer: two sources are just resolvable when the central maximum of one Airy disk falls exactly on the first minimum (dark ring) of the other. At this separation, a small but visible dip appears between the two intensity peaks — a trained observer can still tell there are two sources, but just barely. For a circular aperture of diameter D, the angle at which this occurs is θ ≈ 1.22 λ/D. The factor of 1.22 comes from the mathematics of diffraction through a circular aperture (specifically from the first zero of the Bessel function J₁). For a slit rather than a circle, the equivalent formula is θ ≈ λ/D without the 1.22.

The formula θ ≈ 1.22 λ/D contains a complete design recipe: to resolve finer angular detail, either use shorter wavelength light or use a larger aperture. This explains why radio telescopes must be enormous — radio waves have wavelengths thousands of times longer than visible light, so the aperture must be proportionally larger to achieve comparable resolution. It explains why the Hubble Space Telescope works in space (no atmospheric blurring, diffraction-limited by its mirror diameter) and why electron microscopes can resolve atomic structures (electron de Broglie wavelengths are far shorter than visible light). In medical imaging, the same principle governs ultrasound resolution: higher-frequency ultrasound has shorter wavelengths and thus finer resolution, but shorter wavelengths are also absorbed more quickly, limiting penetration depth.

The diffraction limit is not a limitation of instrument quality — it is a fundamental physical limit imposed by wave optics. A perfect, aberration-free lens still cannot beat the Rayleigh criterion. The only ways around it are to use shorter wavelengths (UV microscopy, X-ray crystallography) or to use interference-based techniques like **aperture synthesis** in radio astronomy, where many small telescopes are combined to simulate a single large aperture, or **super-resolution microscopy** in biology, which exploits molecular properties rather than aperture physics to localize sources more precisely than λ/D.
