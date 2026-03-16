---
id: stellar-spectra-and-classification-scheme
title: Stellar Spectra and Spectral Classification
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: inverse-square-law-stellar-radiation
  type: soft
builds-toward:
- stellar-effective-temperature-color
- extinction-and-interstellar-reddening
tags:
- spectroscopy
- classification
- stellar-properties
stage: formal-systems
status: draft
---

# Stellar Spectra and Spectral Classification

## Core Idea
Stellar spectra display absorption lines that reflect composition and physical conditions in stellar atmospheres. The Harvard spectral classification sequence (OBAFGKM, from hottest to coolest) organizes stars by effective temperature, with spectral type determined from line strength patterns: hydrogen Balmer lines, ionized calcium lines, and metal lines. Spectroscopy provides detailed physical diagnostics of stellar atmospheres complementing other classification methods.

## How It's Best Learned
Study actual stellar spectra at different wavelengths. Identify key diagnostic lines and understand how line strength correlates with temperature and gravity. Use modern spectral databases to explore the diversity of real stellar spectra.

## Common Misconceptions
Spectral type does not uniquely determine luminosity; luminosity is determined by temperature and surface area separately. Spectral lines arise from absorption in the photosphere, not from the bulk composition of the star. Metal lines used in spectral classification refer to all elements heavier than helium, not just iron.

## Explainer

From the inverse-square law, you know that a star's apparent brightness decreases with the square of its distance, and that we can recover its intrinsic luminosity if we know how far away it is. But brightness alone tells us very little about what a star actually *is*. To learn a star's temperature, composition, and physical conditions, we need to spread its light into a **spectrum** — a rainbow of wavelengths — and read the patterns encoded in it.

When you disperse starlight through a prism or diffraction grating, you see a continuous rainbow crossed by dark **absorption lines** at specific wavelengths. These lines form because atoms in the star's outer atmosphere (the **photosphere**) absorb photons at the precise energies needed to excite their electrons to higher energy levels. Each chemical element produces a unique fingerprint of lines, so the pattern of absorption immediately reveals which elements are present. But the real power of stellar spectroscopy is that the *strength* of these lines depends not just on which elements exist, but on the temperature and pressure of the gas. Hydrogen is the most abundant element in virtually every star, yet hydrogen absorption lines (the **Balmer series**) are strongest in medium-temperature stars (~10,000 K) and weaker in both hotter and cooler stars — because the lines require hydrogen atoms with electrons already in the first excited state, and the population of those atoms peaks at intermediate temperatures.

This temperature dependence is the foundation of the **Harvard spectral classification**: O, B, A, F, G, K, M — from hottest (~50,000 K) to coolest (~3,000 K). The famous mnemonic "Oh Be A Fine Girl/Guy, Kiss Me" helps remember the sequence. **O-type** stars are blue-white and show lines of highly ionized helium and multiply ionized metals — only extreme temperatures can strip electrons from these atoms. **A-type** stars show the strongest hydrogen Balmer lines. **G-type** stars like our Sun display prominent ionized calcium (Ca II) lines and numerous metal lines, because at ~5,800 K, metals retain enough electrons to produce abundant absorption features. **M-type** stars are cool enough for molecules like titanium oxide (TiO) to survive in their atmospheres, producing broad absorption bands that dominate the spectrum.

Each spectral type is further divided into subtypes 0–9 (e.g., G2 for the Sun, where lower numbers are hotter within the class). Beyond temperature, the width and shape of spectral lines also encode information about **surface gravity** and therefore luminosity class. Giant and supergiant stars have more extended, lower-density atmospheres, producing narrower spectral lines than compact dwarf stars of the same temperature. This led to the **MKK luminosity classification** (I through V), which, combined with spectral type, gives a two-dimensional classification — for example, the Sun is a G2V star (G2 spectral type, luminosity class V for main-sequence dwarf). Together, spectral type and luminosity class allow astronomers to estimate a star's temperature, luminosity, radius, and evolutionary state from its light alone — without ever needing to visit it.
