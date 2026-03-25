---
id: stellar-effective-temperature-color
title: Stellar Effective Temperature and Color Index
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: inverse-square-law-stellar-radiation
  type: soft
- id: stellar-spectral-classification
  type: hard
builds-toward:
- core-hydrogen-burning-main-sequence
tags:
- stellar-properties
- temperature
- color
- spectroscopy
stage: formal-systems
status: validated
---

# Stellar Effective Temperature and Color Index

## Core Idea
A star's effective temperature is the temperature of an equivalent blackbody that radiates the same total energy per unit surface area. Star color—determined from spectral peaks or photometric color indices—indicates effective temperature: O-type stars are blue and hot (~30,000+ K), while M-type stars are red and cool (~3,000 K). Color provides a direct and rapid classification of stellar temperatures.

## Questions

```yaml
- question: "An astronomer measures two stars: Star A has a B−V color index of −0.3, and Star B has a B−V color index of +1.5. Which star has the higher effective temperature?"
  type: multiple-choice
  options:
    - "Star B — a larger B−V value indicates greater total energy output and therefore higher temperature"
    - "Star A — a more negative B−V means more flux at blue wavelengths relative to visual, indicating a hotter blackbody spectrum"
    - "They are equally hot — color index measures apparent brightness, not temperature"
    - "Star B — red stars burn more slowly and therefore maintain higher core temperatures"
  answer: 1
  explanation: "B−V color index measures the difference in brightness between the blue (B) and visual (V) filter bands. A hot star peaks at shorter wavelengths and emits more flux in B than V, giving a small or negative B−V. A cool star peaks at longer wavelengths, emitting relatively more in V than B, giving a large positive B−V. Star A (B−V = −0.3) is blue and hot; Star B (B−V = +1.5) is red and cool. This is a direct observational implementation of Wien's displacement law."

- question: "Two stars have the same spectral type (both are G2, like the Sun) but one is 100 times more luminous. What explains the luminosity difference?"
  type: multiple-choice
  options:
    - "Nothing — stars of the same spectral type must have the same luminosity by definition"
    - "The more luminous star must have a higher effective temperature, since luminosity depends only on T_eff"
    - "The more luminous star has a larger radius — since L = 4πR²σT_eff⁴, same T_eff with larger R produces higher luminosity"
    - "The more luminous star is closer to Earth, making it appear brighter"
  answer: 2
  explanation: "The Stefan-Boltzmann relation L = 4πR²σT_eff⁴ shows that luminosity depends on both radius and effective temperature. Two stars with identical spectral type have nearly the same T_eff (their spectral classification is based on temperature), so the luminosity difference must come from different radii. This is exactly the distinction between main-sequence stars and giants/supergiants: an A-type supergiant and an A-type main-sequence star have similar colors and T_eff but vastly different luminosities because the supergiant is enormously larger. Spectral type alone does not determine luminosity."

- question: "A star's effective temperature is the actual temperature measured at a specific physical layer of the star, such as the photosphere."
  type: true-false
  answer: false
  explanation: "Effective temperature is a model quantity, not a direct physical measurement. It is defined as the temperature of a hypothetical blackbody that would emit the same total power per unit surface area as the star: L = 4πR²σT_eff⁴. Real stellar photospheres have temperature gradients — they are hotter deeper in and cooler at the top. T_eff is a single representative number capturing the star's overall radiative output, derived from the Stefan-Boltzmann law using the observed luminosity and radius. It is an extremely useful abstraction, but it is not 'the temperature at a layer.'"

- question: "The spectral classification sequence O-B-A-F-G-K-M is fundamentally a temperature sequence, with O stars being the hottest and M stars the coolest."
  type: true-false
  answer: true
  explanation: "The sequence was originally organized by hydrogen line strength, but it was later recognized that hydrogen line intensity peaks at intermediate temperatures (A-type stars) because the lines require a specific balance of excitation and ionization. Reordered by temperature, the sequence runs hot to cool: O (>30,000 K), B (~10,000–30,000 K), A (~7,500–10,000 K), F (~6,000–7,500 K), G (~5,200–6,000 K), K (~3,700–5,200 K), M (~2,400–3,700 K). The different absorption features that define each class arise because temperature controls which atomic states and molecular species exist in stellar atmospheres."

- question: "Why does a star's color indicate its surface temperature? Explain the physical principle connecting them."
  type: short-answer
  answer: "Stars approximate blackbodies, which emit radiation with a spectral peak determined by temperature via Wien's displacement law: λ_peak = b/T (where b ≈ 2.9 × 10⁻³ m·K). Hotter stars peak at shorter (bluer) wavelengths; cooler stars peak at longer (redder) wavelengths. Astronomers measure this through color indices: by comparing a star's brightness in blue (B) versus visual (V) filters, the ratio of fluxes at two wavelengths constrains the shape of the spectral energy distribution and thus the effective temperature. A blue star has most of its flux at short wavelengths (high T_eff); a red star has most at long wavelengths (low T_eff)."
  explanation: "The connection is direct and quantitative: color is a measurement of the spectral peak's location, and Wien's law links the peak location to temperature. Interstellar dust can redden starlight (shifting observed colors toward the red), requiring correction before inferring T_eff — but this is a practical complication of the same underlying physics, not an exception to it."
```

## Explainer

When you look at the night sky, stars are not all the same color. Betelgeuse glows distinctly orange-red, while Rigel shines blue-white. This color difference is not cosmetic — it directly encodes each star's surface temperature. The connection comes from a concept you already know: **blackbody radiation**. A perfect blackbody emits light across all wavelengths, but the peak of its emission shifts with temperature according to Wien's displacement law. Hotter objects peak at shorter (bluer) wavelengths; cooler objects peak at longer (redder) wavelengths. Stars are not perfect blackbodies — their atmospheres absorb specific wavelengths — but they are close enough that the overall color reliably indicates temperature.

The **effective temperature** (T_eff) of a star formalizes this idea. It is defined as the temperature of a hypothetical blackbody that would radiate the same total energy per unit surface area as the star. This connects to the Stefan-Boltzmann law you encountered through the inverse square law of stellar radiation: the luminosity of a star equals 4πR²σT_eff⁴, where R is the stellar radius and σ is the Stefan-Boltzmann constant. Effective temperature is not the temperature at any specific physical layer of the star — the photosphere has a temperature gradient — but it is a single number that captures the star's overall thermal radiation character. It is arguably the most fundamental observable property of a stellar surface.

In practice, astronomers determine effective temperature through two complementary methods. The first is **spectral classification**, which you have already studied. The spectral sequence O-B-A-F-G-K-M is fundamentally a temperature sequence, from the hottest O stars above 30,000 K to cool M stars around 3,000 K. The absorption lines that define each class — ionized helium in O stars, hydrogen Balmer lines peaking in A stars, molecular bands in M stars — change because temperature controls which atoms and molecules exist in which ionization and excitation states. The second method uses **color indices**: by measuring a star's brightness through different wavelength filters (such as B and V), the ratio of fluxes at two wavelengths gives a direct proxy for the spectral energy distribution's shape and hence T_eff. A small or negative B−V index means the star is blue and hot; a large positive B−V means it is red and cool.

The relationship between color and effective temperature is not perfectly linear, and it depends on factors like surface gravity and chemical composition (metallicity), which subtly alter the spectrum. Reddening by interstellar dust also shifts observed colors toward the red, requiring correction before inferring true temperatures. Despite these complications, the color-temperature relationship is one of the most powerful tools in stellar astrophysics: it allows astronomers to estimate temperatures for millions of stars from photometry alone, enabling the construction of the Hertzsprung-Russell diagram and the classification of stellar populations across entire galaxies.
