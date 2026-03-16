---
id: extinction-and-interstellar-reddening
title: Extinction and Interstellar Reddening
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: stellar-spectra-and-classification-scheme
  type: soft
- id: apparent-magnitude-brightness-measurement
  type: hard
builds-toward:
- galaxy-classification-and-morphology
tags:
- interstellar
- dust
- extinction
- observational
stage: formal-systems
status: draft
---

# Extinction and Interstellar Reddening

## Core Idea
Interstellar dust grains absorb and scatter starlight, preferentially removing blue light more efficiently than red light—a process producing reddening of starlight colors. Extinction is the overall dimming of starlight by dust, measurable as differences in apparent magnitude; reddening is the selective color shift. Both effects depend on the amount of dust along the line of sight and the grain size distribution. Accounting for extinction and reddening is essential for accurate distance and luminosity determinations.

## Explainer

From your study of apparent magnitude, you know that a star's measured brightness depends on its intrinsic luminosity and its distance. But there is a third factor that complicates this clean relationship: **interstellar dust**. The space between stars is not perfectly transparent. Tiny solid particles — typically fractions of a micrometer in size, composed of silicates, graphite, and ices — populate the interstellar medium, and they interact with starlight passing through them. The total effect of this interaction is called **extinction**: the starlight arrives dimmer than it would in a dust-free universe.

Extinction has two physical components: **absorption** (the dust grain absorbs the photon's energy and re-emits it as infrared radiation) and **scattering** (the photon is deflected out of the line of sight). Both reduce the light reaching the observer. The total extinction in magnitudes, denoted A, is added to a star's apparent magnitude: a star behind 1 magnitude of extinction appears 1 magnitude fainter than its true distance would predict. If you ignore extinction when calculating distances from apparent and absolute magnitudes, you will systematically overestimate how far away stars are — they look fainter, so you conclude they must be farther.

The critical detail is that extinction is **wavelength-dependent**. Dust grains interact more strongly with shorter-wavelength (bluer) light than with longer-wavelength (redder) light, because the grains are comparable in size to the wavelengths of blue and ultraviolet light. This selective removal of blue photons is called **reddening** — the star's observed color shifts redward compared to its true spectral type. Astronomers quantify this with the **color excess** E(B−V), the difference between the observed (B−V) color index and the intrinsic color expected from the star's spectral classification. A star classified as a B-type star from its spectral lines but appearing yellowish in broadband photometry is a clear sign of significant reddening.

The relationship between total extinction and reddening is captured by the **ratio of total-to-selective extinction**, R_V = A_V / E(B−V), which averages about 3.1 in the diffuse interstellar medium but can vary in dense molecular clouds where grain properties differ. This means that measuring the color excess — which requires knowing the star's intrinsic color from its spectral type — lets you estimate the total extinction and correct both the brightness and distance. Astronomers construct **extinction maps** of the Milky Way by measuring reddening toward thousands of stars, revealing the dusty structure of the galactic plane. Without these corrections, the entire cosmic distance ladder would be systematically biased, making extinction correction one of the most practically important calibrations in observational astronomy.
