---
id: dispersion-wavelength-dependent-refraction
title: Dispersion and Wavelength-Dependent Refraction
domain: physics
course: waves-and-optics
prerequisites:
- id: refractive-index-material-property
  type: hard
builds-toward:
- dispersion-and-prisms
tags:
- dispersion
- wavelength-dependent
- prism
stage: formal-systems
status: draft
---

# Dispersion and Wavelength-Dependent Refraction

## Core Idea
Dispersion is the wavelength-dependent variation of refractive index in a material: shorter wavelengths (blue light) have higher refractive indices than longer wavelengths (red light) in normal dispersion. This causes white light to separate into its component colors when passing through a prism. Dispersion is the origin of rainbows and explains why different colors refract at different angles.

## Explainer

Dispersion builds directly on what you know about refractive index. You learned that n = c/v, where c is the speed of light in vacuum and v is its speed in the medium. When light enters glass, it slows down, and n captures how much. Dispersion extends this by revealing that n is not a single fixed number for a given material — it depends on the frequency (and therefore wavelength) of the light. The refractive index of glass for blue light is measurably higher than for red light.

The physical reason is that light interacts with the electrons in the material, and this interaction is strongly frequency-dependent. Higher-frequency light (shorter wavelengths, bluer) drives electron oscillations closer to their natural resonance frequency, producing a stronger interaction and more slowing. This is called **normal dispersion** and is the behavior of glass, water, and most transparent solids at visible wavelengths. The relationship between n and wavelength is not linear — it curves steeply toward the ultraviolet end of the spectrum. Empirical formulas like the Cauchy equation (n ≈ A + B/λ²) capture this behavior well for visible light.

The consequence is that Snell's law — n₁ sin θ₁ = n₂ sin θ₂ — produces a different refraction angle for each color. When white light enters a prism, each wavelength bends by a different amount at both the entry and exit surfaces. Blue light, with the highest n, bends the most; red light, with the lowest n, bends the least. The cumulative effect of two refractions (entry and exit) spreads the colors into a continuous spectrum. The angular spread between red and violet across the visible spectrum is the **dispersion** of the material, and it varies widely between glass types — which is why lens designers combine different glass types to cancel dispersion while preserving focusing power.

Rainbows arise from the same physics in spherical water droplets. Sunlight enters a droplet, reflects off the back interior surface, and refracts again on exit. Because each wavelength exits at a slightly different angle (red at ~42°, violet at ~40° from the antisolar point), different colors reach your eye from droplets at different positions in the sky. The result is the colored arc. The key insight in both prisms and rainbows is the same: dispersion is not an imperfection or side effect — it is a fundamental consequence of how electromagnetic waves interact with bound electrons, and it is the mechanism behind spectroscopy, optical fiber chromatic dispersion, and the chromatic aberration that lens designers work to correct.
