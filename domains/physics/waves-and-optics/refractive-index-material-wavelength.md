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
stage: advanced
status: validated
---

# Refractive Index: Definition and Wavelength Dependence

## Core Idea
The refractive index n = c/v relates the speed of light in vacuum (c) to its speed in the material (v). Refractive index depends on wavelength (dispersion), with shorter wavelengths typically experiencing higher refractive indices. This wavelength dependence causes dispersion and chromatic aberration in optical systems.

## Questions

```yaml
- question: "A glass prism is illuminated with white light. Which color is refracted (bent) the most as it enters the glass?"
  type: multiple-choice
  options:
    - "Red, because it has the longest wavelength and the most energy to push through the material"
    - "Violet, because it has the shortest wavelength and therefore the highest refractive index in glass"
    - "Green, because it is in the middle of the visible spectrum where glass absorbs least"
    - "All colors are refracted equally because the prism is made of uniform glass throughout"
  answer: 1
  explanation: "The Cauchy equation n(λ) ≈ A + B/λ² shows that shorter wavelengths produce higher refractive indices. Violet light (λ ≈ 400 nm) has a higher n in glass than red light (λ ≈ 700 nm), so by Snell's law (n₁ sin θ₁ = n₂ sin θ₂) violet bends more sharply at the interface. Option A is the common misconception — wavelength and energy don't directly control bending; the refractive index does. Option D is wrong because n varies with wavelength even in homogeneous glass, which is the entire point of dispersion."

- question: "A camera produces colored fringes around bright edges in its images. An optical engineer wants to eliminate this chromatic aberration. Which approach addresses the root cause?"
  type: multiple-choice
  options:
    - "Using a lens made from a single glass type with the highest possible refractive index"
    - "Adding an anti-reflective coating to all lens surfaces"
    - "Using a doublet: combining two glass types with different dispersion curves so their wavelength-dependent bending partially cancels"
    - "Reducing the lens aperture to block wavelengths at the spectrum edges"
  answer: 2
  explanation: "Chromatic aberration exists because n varies with wavelength — different colors focus at slightly different distances. The fix must address this wavelength dependence directly. A doublet uses crown glass (lower dispersion) and flint glass (higher dispersion) whose dispersion curves run in opposite directions for the same wavelengths, so their combined effect is nearly the same bending for all visible wavelengths. Option A makes aberration worse (higher n doesn't help if dispersion remains). Options B and D address reflections and intensity, not wavelength-dependent focusing."

- question: "In most transparent optical materials, red light travels faster through the material than violet light."
  type: true-false
  answer: true
  explanation: "Speed in a medium is v = c/n. Red light has a longer wavelength, so the Cauchy equation gives it a lower refractive index than violet light. Lower n means higher speed (v = c/n), so red light travels faster through glass or water than violet light. This is directly related to why violet bends more: higher n means slower speed at the interface, which corresponds to more bending via Snell's law."

- question: "The refractive index of a material is a single fixed constant that characterizes the material's optical properties, independent of the color of light used."
  type: true-false
  answer: false
  explanation: "This is the central misconception this topic corrects. The refractive index depends on wavelength — this wavelength dependence is called dispersion. The Cauchy equation n(λ) ≈ A + B/λ² shows n changes with λ. Glass has n ≈ 1.512 for red light and n ≈ 1.532 for violet light — a ~1% difference that is small but physically significant, producing the rainbow pattern from a prism and chromatic aberration in lenses. Textbooks sometimes give a single n value for a material only as an approximation for a specific wavelength (usually the sodium D line at 589 nm)."

- question: "Explain why a glass prism separates white light into its component colors, using the definition of refractive index and its relationship to wavelength."
  type: short-answer
  answer: "White light is a mixture of all visible wavelengths. The refractive index n of glass is higher for shorter wavelengths (violet, ~400 nm) than for longer wavelengths (red, ~700 nm) — captured by n(λ) ≈ A + B/λ². Since Snell's law n₁ sin θ₁ = n₂ sin θ₂ determines bending angle, and n differs for each wavelength, each color bends by a different amount when entering the prism. Violet bends most, red bends least, and the intermediate wavelengths spread between them. This wavelength-dependent refraction physically separates the originally overlapping colors into a spatial spectrum."
```

## Explainer

From Snell's law, you know that light bends when it crosses between two media, and that the amount of bending depends on the ratio of refractive indices: n₁ sin θ₁ = n₂ sin θ₂. The **refractive index** n of a medium is defined as n = c/v, where c is the speed of light in vacuum (~3 × 10⁸ m/s) and v is the speed of light in that material. Glass has n ≈ 1.5, meaning light travels about two-thirds as fast in glass as in vacuum. Diamond has n ≈ 2.4 — light crawls through it at less than half its vacuum speed. Air has n ≈ 1.0003, close enough to vacuum that we often treat it as 1.

The subtlety that distinguishes this topic from basic Snell's law is that n is not a single fixed number for a given material — it varies with wavelength. This **dispersion** arises from how light interacts with the electron clouds in atoms. Different frequencies of light drive the electrons at different fractions of their natural resonant frequency, and this changes how strongly the material slows them down. The relationship is captured by the Cauchy equation (an empirical approximation): n(λ) ≈ A + B/λ², where A and B are material-specific constants and λ is wavelength. This formula immediately shows that shorter wavelengths (smaller λ) produce larger n — violet light travels more slowly through glass and bends more sharply than red light.

The practical consequence in Snell's law is that if you send white light (a mixture of all visible wavelengths) through a glass interface at an angle, each wavelength bends by a slightly different amount. Red light (λ ≈ 700 nm, n_glass ≈ 1.512) bends less than violet light (λ ≈ 400 nm, n_glass ≈ 1.532). This wavelength-dependent refraction is the physical mechanism behind **dispersion** — the separation of white light into its spectral colors by a prism or raindrop. The fact that n varies by only about 1–2% across the visible spectrum means the color separation is subtle but visually striking when given enough geometry to accumulate.

For optical instruments, this wavelength dependence creates a problem called **chromatic aberration**: a lens focuses different colors at slightly different distances from the lens, because each wavelength is bent by a slightly different amount. In a camera or telescope, this means red and violet components of a scene form their sharpest images at different depths, producing colored fringes around high-contrast edges. Lens designers correct this by combining lenses made from two different glass types — a **doublet** — chosen so that their dispersions partly cancel. The crown glass brings one color to focus, and the flint glass (with steeper dispersion) corrects the remaining spread. Understanding why chromatic aberration exists, and why different glasses have different dispersion curves, depends entirely on the wavelength dependence of n you're learning here.
