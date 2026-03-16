---
id: exoplanet-transmission-spectroscopy
title: Exoplanet Transmission Spectroscopy
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: exoplanet-characterization-spectroscopy
  type: hard
- id: electromagnetic-spectrum-astronomy
  type: soft
- id: beers-law
  type: soft
- id: spectroscopy-fundamentals
  type: hard
- id: spectroscopic-instrumentation
  type: soft
- id: ultraviolet-visible-spectroscopy-quantitative
  type: soft
- id: ir-spectroscopy-basics
  type: soft
builds-toward:
- biosignatures-exoplanet-atmospheres
tags:
- transmission
- spectroscopy
- atmosphere
stage: advanced
status: draft
---

# Exoplanet Transmission Spectroscopy

## Core Idea
Transmission spectroscopy measures wavelength-dependent absorption of starlight by exoplanet atmospheres during transit; opacity variations reveal atmospheric composition (H₂O, CO₂, CH₄, molecular features), cloud altitude, and aerosol properties. The technique is sensitive to biosignatures and constraints habitability indicators.

## Explainer

From your prerequisites in spectroscopy and exoplanet characterization, you know that atoms and molecules absorb light at specific wavelengths, and that exoplanets can be studied by analyzing the light from their host stars. Transmission spectroscopy is the technique that connects these ideas: it uses the thin ring of atmosphere visible at a planet's edge during a transit to identify what that atmosphere is made of, without ever directly imaging the planet itself.

The geometry is straightforward. When an exoplanet passes in front of its star (a **transit**), it blocks a small fraction of the starlight — typically around 1% for a Jupiter-sized planet orbiting a Sun-like star, and much less for an Earth-sized planet. But the planet is not a solid opaque disk. It has an atmosphere, and that atmosphere is more opaque at some wavelengths than others. At wavelengths where atmospheric molecules absorb strongly — say, a water vapor absorption band near 1.4 micrometers — the atmosphere is effectively thicker, the planet blocks slightly more starlight, and the transit appears deeper. At wavelengths where the atmosphere is transparent, the transit is shallower. By measuring the transit depth as a function of wavelength, you build a **transmission spectrum**: a plot showing how the apparent size of the planet varies with wavelength, which directly encodes the absorption features of the atmospheric gases along the limb.

The connection to Beer's Law is direct. Starlight passing through the planet's atmospheric limb travels a long path through gas at grazing angles — an extremely long optical path length. Even trace species can produce detectable absorption features because the path length amplifies their signal. The absorption cross-sections of molecules like H₂O, CO₂, CH₄, Na, and K at specific wavelengths create the spectral features that transmission spectroscopy detects. The amplitude of these features depends on the **atmospheric scale height** — how rapidly pressure and density decrease with altitude — which in turn depends on temperature, mean molecular weight, and surface gravity. A hot, low-gravity planet with a hydrogen-rich atmosphere (like a hot Jupiter) has a puffy atmosphere with large, easily detectable features. A cold, rocky planet with a nitrogen-dominated atmosphere has a compact atmosphere with tiny features, pushing the technique to its limits.

Clouds and hazes are the principal complication. High-altitude aerosol layers can act as an opaque floor, blocking the view of deeper atmospheric layers and muting or erasing molecular absorption features. A perfectly cloudy planet would show a featureless, flat transmission spectrum regardless of its atmospheric composition. This is why some early observations of super-Earths and sub-Neptunes returned frustratingly bland spectra — not because those planets lacked atmospheres, but because clouds obscured the molecular signatures. Distinguishing between "no atmosphere" and "cloudy atmosphere" requires observations across a wide wavelength range, since clouds tend to produce wavelength-dependent slopes (from scattering) that differ from molecular absorption patterns.

The James Webb Space Telescope (JWST) has transformed this field by providing unprecedented sensitivity in the infrared, where key molecules like CO₂ (4.3 μm), CH₄ (3.3 μm), and H₂O (multiple bands) have their strongest features. JWST's first transmission spectrum of the rocky exoplanet TRAPPIST-1b and its detection of CO₂ in the atmosphere of the gas giant WASP-39b demonstrated the technique's power. The ultimate goal — detecting **biosignatures** like the simultaneous presence of O₂ and CH₄ in a rocky planet's atmosphere, a thermodynamic disequilibrium that would be difficult to explain without biology — remains a frontier challenge, but transmission spectroscopy is currently the most viable path toward answering whether life exists beyond our solar system.
