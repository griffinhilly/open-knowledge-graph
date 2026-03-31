---
id: thermal-remote-sensing
title: Thermal Remote Sensing
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: hard
- id: passive-vs-active-sensors
  type: hard
builds-toward:
- change-detection-remote-sensing
- land-use-land-cover-mapping
tags:
- thermal-infrared
- land-surface-temperature
- emissivity
- remote-sensing
stage: advanced
status: validated
---

# Thermal Remote Sensing

## Core Idea
Thermal remote sensing measures electromagnetic radiation emitted by Earth's surface in the thermal infrared bands (3-14 um) rather than reflected sunlight. Every object above absolute zero emits thermal radiation governed by its temperature and emissivity (Planck's law). By measuring this emission in atmospheric windows around 3-5 um and 8-14 um, thermal sensors derive land surface temperature (LST) and sea surface temperature (SST). Because thermal emission occurs continuously, thermal sensors operate day and night. Applications span urban heat island mapping, volcanic monitoring, fire detection, and evapotranspiration estimation.

## Questions

```yaml
- question: "Two adjacent surfaces in a thermal image have the same temperature, but one (a lake) appears warmer than the other (a metal roof). What physical property explains this?"
  type: multiple-choice
  options:
    - "The lake is actually warmer due to thermal inertia"
    - "Emissivity -- water has high emissivity (~0.98) and emits nearly as a blackbody, while polished metal has low emissivity (~0.2-0.5) and emits less radiation at the same temperature"
    - "The metal roof reflects thermal radiation from the sky, making it appear cooler"
    - "Atmospheric absorption is stronger over metal surfaces"
  answer: 1
  explanation: "A thermal sensor measures radiance, not temperature directly. Radiance depends on both temperature AND emissivity. At the same temperature, a high-emissivity surface emits more radiation than a low-emissivity surface. If emissivity is not accounted for, the sensor-derived temperature will be wrong. This temperature-emissivity separation problem is central to thermal remote sensing."

- question: "Thermal remote sensing is an active sensing technique because the sensor detects energy emitted by the surface."
  type: true-false
  answer: false
  explanation: "Active sensing requires the sensor to transmit its own energy. Thermal remote sensing is passive -- it detects radiation naturally emitted by the surface due to its temperature. The surface itself is the energy source, not the sensor."

- question: "Explain why urban areas typically appear warmer than surrounding rural areas in nighttime thermal imagery."
  type: short-answer
  answer: "The urban heat island effect results from several factors: (1) Urban materials like concrete and asphalt have high thermal inertia -- they absorb solar energy during the day and release it slowly at night. (2) Urban geometry traps longwave radiation, reducing radiative cooling. (3) Reduced vegetation means less evapotranspiration. (4) Waste heat from buildings and vehicles adds energy. Nighttime thermal imagery isolates heat retention because reflected solar radiation is absent."
  explanation: "Nighttime thermal imagery is particularly diagnostic of urban heat islands because it reveals differential heat storage."
```

## Explainer

While optical remote sensing measures reflected sunlight, thermal remote sensing measures radiation that the surface itself emits. Reflected energy tells you about surface composition; emitted energy tells you about surface temperature and thermal properties.

The physics is governed by Planck's radiation law: every object above absolute zero emits electromagnetic radiation with a spectral distribution that depends on its temperature and emissivity. Earth's surface, at roughly 288 K, has peak emission near 10 um. Thermal sensors measure this emission in atmospheric windows and convert measured radiance to temperature, provided surface emissivity is known or estimated.

The temperature-emissivity separation problem is the central challenge. Emissivity varies with surface material -- natural surfaces have high emissivity (0.95-0.99), while metals can be much lower. With a single thermal band, you cannot independently determine both temperature and emissivity. Multi-band thermal sensors (like ASTER with 5 thermal bands) use spectral differences to solve for both simultaneously.

Applications exploit the fact that surface temperature responds to physical processes. Urban heat island studies map temperature variations across cities. Fire detection relies on extreme thermal contrast between active fires (800-1200 K) and background (300 K). Sea surface temperature drives ocean circulation models. Evapotranspiration models use LST to estimate water loss -- cooler surfaces are evaporating more. In each case, thermal remote sensing provides information that optical imagery cannot.
