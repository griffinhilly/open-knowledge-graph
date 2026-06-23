---
id: optical-remote-sensing
title: Optical Remote Sensing
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: hard
- id: passive-vs-active-sensors
  type: hard
- id: satellite-orbits-remote-sensing
  type: soft
builds-toward:
- multispectral-imaging
- hyperspectral-imaging
- image-classification-remote-sensing
tags:
- optical-sensors
- reflectance
- satellite-imagery
- remote-sensing
stage: advanced
status: validated
---

# Optical Remote Sensing

## Core Idea
Optical remote sensing captures reflected solar radiation in the visible and near-infrared wavelengths (roughly 0.4-2.5 micrometers) to create images of Earth's surface. The fundamental measurement is surface reflectance -- the fraction of incoming sunlight reflected by each material at each wavelength. Because different surface materials reflect sunlight differently across wavelengths, optical imagery encodes rich information about land cover, vegetation health, water quality, and mineral composition. Key system parameters include spatial resolution, spectral resolution, temporal resolution, and radiometric resolution.

## Questions

```yaml
- question: "A Sentinel-2 image shows pixels that appear bright in the near-infrared band and dark in the red band. What surface type does this pattern most likely represent?"
  type: multiple-choice
  options:
    - "Open water, which absorbs infrared radiation"
    - "Bare soil, which reflects evenly across visible and infrared"
    - "Healthy green vegetation, which strongly reflects NIR and absorbs red light for photosynthesis"
    - "Snow, which reflects strongly across all visible wavelengths"
  answer: 2
  explanation: "Healthy vegetation has a characteristic spectral signature: chlorophyll absorbs red light for photosynthesis while leaf mesophyll cell structure strongly scatters near-infrared radiation. This dramatic contrast is the basis of vegetation indices like NDVI."

- question: "Higher spatial resolution in optical remote sensing always produces better results for land cover classification."
  type: true-false
  answer: false
  explanation: "Higher spatial resolution increases detail but also increases spectral variability within land cover classes (the salt-and-pepper effect). A 30m pixel averages many trees into a smooth signature, while a 0.5m image shows individual crowns, shadows, and gaps. The optimal resolution depends on the application."

- question: "Explain why optical remote sensing images require atmospheric correction before quantitative analysis."
  type: short-answer
  answer: "The signal includes both surface-reflected radiation and unwanted atmospheric contributions: Rayleigh scattering adds bluish haze, aerosol scattering adds path radiance, and atmospheric gases absorb portions of the signal. Atmospheric correction models estimate and remove these effects to retrieve physically meaningful surface reflectance values comparable across dates and sensors."
  explanation: "Raw satellite digital numbers are contaminated by atmosphere. Atmospheric correction converts them to surface reflectance."
```

## Explainer

With an understanding of the electromagnetic spectrum and sensor types, you can now focus on the most widely used form of remote sensing: optical imaging. Optical sensors are passive instruments that record sunlight reflected from Earth's surface in the visible, near-infrared, and shortwave infrared wavelengths.

The raw measurement is radiance -- the power of electromagnetic radiation reaching the sensor per unit area, per unit solid angle, per unit wavelength. But what scientists actually want is surface reflectance: the fraction of incoming sunlight that the surface reflects at each wavelength. Converting from radiance to reflectance requires accounting for solar illumination geometry, Earth-Sun distance, and atmospheric effects.

Optical remote sensing systems are characterized by four resolutions. Spatial resolution determines the smallest distinguishable feature -- from 0.3 m (commercial) to 1 km (MODIS). Spectral resolution describes how finely the spectrum is sampled. Temporal resolution is the revisit frequency. Radiometric resolution measures sensitivity to brightness differences. No single sensor optimizes all four; mission design involves deliberate trade-offs.

The power of optical remote sensing lies in systematically mapping surface properties across enormous areas. A single Landsat scene covers 185 x 185 km at 30 m resolution in seven spectral bands, every 16 days, free of charge. This combination makes optical remote sensing indispensable for agriculture, forestry, urban growth tracking, water quality, and disaster response.
