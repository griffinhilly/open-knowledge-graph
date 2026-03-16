---
id: stellar-effective-temperature-color
title: Stellar Effective Temperature and Color Index
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: inverse-square-law-stellar-radiation
  type: soft
- id: stellar-spectra-and-classification-scheme
  type: hard
builds-toward:
- core-hydrogen-burning-main-sequence
tags:
- stellar-properties
- temperature
- color
- spectroscopy
stage: formal-systems
status: draft
---

# Stellar Effective Temperature and Color Index

## Core Idea
A star's effective temperature is the temperature of an equivalent blackbody that radiates the same total energy per unit surface area. Star color—determined from spectral peaks or photometric color indices—indicates effective temperature: O-type stars are blue and hot (~30,000+ K), while M-type stars are red and cool (~3,000 K). Color provides a direct and rapid classification of stellar temperatures.

## Explainer

When you look at the night sky, stars are not all the same color. Betelgeuse glows distinctly orange-red, while Rigel shines blue-white. This color difference is not cosmetic — it directly encodes each star's surface temperature. The connection comes from a concept you already know: **blackbody radiation**. A perfect blackbody emits light across all wavelengths, but the peak of its emission shifts with temperature according to Wien's displacement law. Hotter objects peak at shorter (bluer) wavelengths; cooler objects peak at longer (redder) wavelengths. Stars are not perfect blackbodies — their atmospheres absorb specific wavelengths — but they are close enough that the overall color reliably indicates temperature.

The **effective temperature** (T_eff) of a star formalizes this idea. It is defined as the temperature of a hypothetical blackbody that would radiate the same total energy per unit surface area as the star. This connects to the Stefan-Boltzmann law you encountered through the inverse square law of stellar radiation: the luminosity of a star equals 4πR²σT_eff⁴, where R is the stellar radius and σ is the Stefan-Boltzmann constant. Effective temperature is not the temperature at any specific physical layer of the star — the photosphere has a temperature gradient — but it is a single number that captures the star's overall thermal radiation character. It is arguably the most fundamental observable property of a stellar surface.

In practice, astronomers determine effective temperature through two complementary methods. The first is **spectral classification**, which you have already studied. The spectral sequence O-B-A-F-G-K-M is fundamentally a temperature sequence, from the hottest O stars above 30,000 K to cool M stars around 3,000 K. The absorption lines that define each class — ionized helium in O stars, hydrogen Balmer lines peaking in A stars, molecular bands in M stars — change because temperature controls which atoms and molecules exist in which ionization and excitation states. The second method uses **color indices**: by measuring a star's brightness through different wavelength filters (such as B and V), the ratio of fluxes at two wavelengths gives a direct proxy for the spectral energy distribution's shape and hence T_eff. A small or negative B−V index means the star is blue and hot; a large positive B−V means it is red and cool.

The relationship between color and effective temperature is not perfectly linear, and it depends on factors like surface gravity and chemical composition (metallicity), which subtly alter the spectrum. Reddening by interstellar dust also shifts observed colors toward the red, requiring correction before inferring true temperatures. Despite these complications, the color-temperature relationship is one of the most powerful tools in stellar astrophysics: it allows astronomers to estimate temperatures for millions of stars from photometry alone, enabling the construction of the Hertzsprung-Russell diagram and the classification of stellar populations across entire galaxies.
