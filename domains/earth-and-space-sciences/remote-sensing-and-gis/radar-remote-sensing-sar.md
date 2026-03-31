---
id: radar-remote-sensing-sar
title: Radar Remote Sensing and SAR
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: hard
- id: passive-vs-active-sensors
  type: hard
builds-toward:
- change-detection-remote-sensing
- digital-elevation-models
- disaster-monitoring-remote-sensing
tags:
- radar
- synthetic-aperture-radar
- SAR
- microwave
- remote-sensing
stage: advanced
status: validated
---

# Radar Remote Sensing and SAR

## Core Idea
Radar remote sensing transmits microwave pulses (wavelengths 1 cm to 1 m) toward Earth's surface and measures the returned signal (backscatter). Synthetic Aperture Radar (SAR) uses the satellite's motion to synthesize a much larger antenna, achieving fine spatial resolution despite long wavelengths. Because the sensor provides its own illumination and microwaves penetrate clouds, rain, and smoke, SAR operates day and night in all weather. Backscatter intensity depends on surface roughness, moisture content, and dielectric properties. SAR also records signal phase, enabling interferometric SAR (InSAR) to measure surface deformation with millimeter precision.

## Questions

```yaml
- question: "InSAR measurements show a section of a city is subsiding at 2 cm per year. What physical principle allows SAR to measure such small ground movements from 700 km away?"
  type: multiple-choice
  options:
    - "The SAR measures changes in backscatter intensity caused by surface compression"
    - "Interferometry compares the phase of radar signals from two passes; the phase difference encodes the change in sensor-to-surface distance with sub-wavelength precision"
    - "The SAR detects changes in surface roughness caused by subsidence"
    - "Doppler frequency shifts from the moving ground surface are measured directly"
  answer: 1
  explanation: "InSAR compares the phase of radar returns from two or more passes. If the ground moved between passes, the path length changes, producing a measurable phase difference. Since phase can be measured to a fraction of the wavelength (e.g., 5.6 cm for C-band), displacements of millimeters to centimeters are detectable."

- question: "SAR images appear similar to photographs and can be interpreted using the same visual principles."
  type: true-false
  answer: false
  explanation: "SAR imagery looks fundamentally different from optical imagery. Backscatter depends on surface roughness, not color. Smooth surfaces (calm water) appear dark. Urban areas show extreme brightness from corner reflectors. Layover, foreshortening, and shadow artifacts distort terrain geometry. Speckle noise creates a granular texture absent from optical images."

- question: "Why does C-band SAR (~5.6 cm) interact primarily with leaves and small branches, while L-band SAR (~23 cm) penetrates the canopy to interact with trunks?"
  type: short-answer
  answer: "Radar backscatter is strongest when scattering elements are comparable in size to the wavelength. C-band interacts with canopy elements of similar dimensions -- leaves and twigs -- and is largely scattered by the upper canopy. L-band wavelengths pass through small elements and interact with larger structures (trunks, major branches) and the ground beneath. This wavelength-dependent penetration is why L-band is preferred for forest biomass estimation."
  explanation: "Short-wavelength radar scatters off small canopy elements while longer wavelengths penetrate to interact with larger structures below."
```

## Explainer

From the passive-vs-active distinction, you understand that active sensors provide their own illumination. Radar remote sensing is the most important active technique, and Synthetic Aperture Radar was the breakthrough that made high-resolution imaging possible from space.

A real antenna's resolution is proportional to wavelength divided by antenna length. At microwave wavelengths, achieving 10-meter resolution from 700 km would require a kilometers-long antenna. SAR solves this by exploiting satellite motion: as it moves along orbit, it records echoes at many positions, then computationally combines them as if from a single enormous antenna. The synthetic aperture is the distance traveled during data collection.

Backscatter intensity depends on surface roughness (relative to wavelength), moisture content (water increases the dielectric constant), incidence angle, and polarization. SAR can transmit and receive in horizontal (H) and vertical (V) polarizations, producing combinations (HH, VV, HV, VH) that respond differently to surface structure. Fully polarimetric SAR enables decomposition into surface, volume, and double-bounce scattering.

Interferometric SAR exploits phase information. By comparing phase from two acquisitions, InSAR measures topography (generating DEMs) and surface deformation (detecting millimeter-scale ground movement). This capability is transformative for monitoring tectonic strain, volcanic inflation, glacial flow, and urban subsidence at continental scales.
