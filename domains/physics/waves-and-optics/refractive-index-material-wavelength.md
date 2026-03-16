---
id: refractive-index-material-wavelength
title: 'Refractive Index: Definition and Wavelength Dependence'
domain: physics
course: waves-and-optics
prerequisites:
- id: snells-law
  type: soft
- id: refractive-index-and-dispersion
  type: soft
builds-toward:
- dispersion-and-prisms
- thin-lenses
tags:
- refractive-index
- dispersion
- optical-properties
stage: formal-systems
status: draft
---

# Refractive Index: Definition and Wavelength Dependence

## Core Idea
The refractive index n = c/v relates the speed of light in vacuum (c) to its speed in the material (v). Refractive index depends on wavelength (dispersion), with shorter wavelengths typically experiencing higher refractive indices. This wavelength dependence causes dispersion and chromatic aberration in optical systems.

## Explainer

From Snell's law, you know that light bends when it crosses between two media, and that the amount of bending depends on the ratio of refractive indices: n₁ sin θ₁ = n₂ sin θ₂. The **refractive index** n of a medium is defined as n = c/v, where c is the speed of light in vacuum (~3 × 10⁸ m/s) and v is the speed of light in that material. Glass has n ≈ 1.5, meaning light travels about two-thirds as fast in glass as in vacuum. Diamond has n ≈ 2.4 — light crawls through it at less than half its vacuum speed. Air has n ≈ 1.0003, close enough to vacuum that we often treat it as 1.

The subtlety that distinguishes this topic from basic Snell's law is that n is not a single fixed number for a given material — it varies with wavelength. This **dispersion** arises from how light interacts with the electron clouds in atoms. Different frequencies of light drive the electrons at different fractions of their natural resonant frequency, and this changes how strongly the material slows them down. The relationship is captured by the Cauchy equation (an empirical approximation): n(λ) ≈ A + B/λ², where A and B are material-specific constants and λ is wavelength. This formula immediately shows that shorter wavelengths (smaller λ) produce larger n — violet light travels more slowly through glass and bends more sharply than red light.

The practical consequence in Snell's law is that if you send white light (a mixture of all visible wavelengths) through a glass interface at an angle, each wavelength bends by a slightly different amount. Red light (λ ≈ 700 nm, n_glass ≈ 1.512) bends less than violet light (λ ≈ 400 nm, n_glass ≈ 1.532). This wavelength-dependent refraction is the physical mechanism behind **dispersion** — the separation of white light into its spectral colors by a prism or raindrop. The fact that n varies by only about 1–2% across the visible spectrum means the color separation is subtle but visually striking when given enough geometry to accumulate.

For optical instruments, this wavelength dependence creates a problem called **chromatic aberration**: a lens focuses different colors at slightly different distances from the lens, because each wavelength is bent by a slightly different amount. In a camera or telescope, this means red and violet components of a scene form their sharpest images at different depths, producing colored fringes around high-contrast edges. Lens designers correct this by combining lenses made from two different glass types — a **doublet** — chosen so that their dispersions partly cancel. The crown glass brings one color to focus, and the flint glass (with steeper dispersion) corrects the remaining spread. Understanding why chromatic aberration exists, and why different glasses have different dispersion curves, depends entirely on the wavelength dependence of n you're learning here.
