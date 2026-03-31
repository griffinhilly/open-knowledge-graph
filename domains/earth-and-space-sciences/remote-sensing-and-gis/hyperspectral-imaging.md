---
id: hyperspectral-imaging
title: Hyperspectral Imaging
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: multispectral-imaging
  type: hard
- id: electromagnetic-spectrum-remote-sensing
  type: hard
builds-toward:
- image-classification-remote-sensing
tags:
- hyperspectral
- imaging-spectroscopy
- spectral-unmixing
- remote-sensing
stage: advanced
status: validated
---

# Hyperspectral Imaging

## Core Idea
Hyperspectral sensors (imaging spectrometers) record reflected radiation in hundreds of narrow, contiguous spectral bands (typically 5-10 nm wide), producing a near-continuous reflectance spectrum for every pixel. Where multispectral sensors sample at a few strategic wavelengths, hyperspectral sensors capture the complete spectral shape, enabling identification of specific minerals, chemicals, vegetation species, and materials based on diagnostic absorption features too narrow for broadband sensors to resolve. This comes at the cost of enormous data volume and complex processing requirements.

## Questions

```yaml
- question: "A geologist needs to distinguish kaolinite (absorption at 2.16 um) from montmorillonite (absorption at 2.21 um). Why would a hyperspectral sensor succeed where a Landsat SWIR band (2.11-2.29 um) would fail?"
  type: multiple-choice
  options:
    - "Hyperspectral sensors have higher spatial resolution"
    - "Landsat SWIR integrates across the entire 2.11-2.29 um range, averaging out both narrow absorption features, while hyperspectral bands resolve each absorption separately"
    - "Hyperspectral sensors use active illumination that penetrates rock"
    - "Landsat cannot image in the SWIR due to atmospheric absorption"
  answer: 1
  explanation: "The absorptions are separated by only 50 nm. A Landsat band spanning 180 nm averages both into a single value. A hyperspectral sensor with 10 nm bands resolves each separately, allowing mineral-specific identification based on exact position, depth, and shape of the absorption."

- question: "Hyperspectral imaging is always superior to multispectral imaging for remote sensing applications."
  type: true-false
  answer: false
  explanation: "Hyperspectral data has hundreds of highly correlated bands creating processing challenges (curse of dimensionality), requires sophisticated atmospheric correction, demands large training datasets, and produces enormous data volumes. For many applications, multispectral data with 4-12 well-chosen bands provides sufficient discrimination at lower cost and complexity."

- question: "What is spectral unmixing and why is it particularly important for hyperspectral data?"
  type: short-answer
  answer: "Spectral unmixing decomposes a pixel's spectrum into fractional contributions of constituent materials (endmembers). Because pixels often contain multiple materials, the recorded spectrum is a mixture. With few multispectral bands, unmixing is underdetermined. Hyperspectral data provides enough spectral samples to solve for multiple endmember fractions reliably, yielding sub-pixel abundance maps critical for mineral mapping, fractional vegetation cover, and detecting small targets that do not fill entire pixels."
  explanation: "Spectral unmixing transforms analysis from 'what class is this pixel' to 'what fraction of this pixel is each material' -- enabled by the high spectral dimensionality."
```

## Explainer

Multispectral imaging samples the spectrum at a handful of strategic points. Hyperspectral imaging measures a near-continuous spectrum for every pixel, typically in 100-300 bands each 5-10 nm wide, spanning 0.4-2.5 um. The result is an image cube -- two spatial dimensions plus one spectral dimension -- where each pixel contains a complete reflectance spectrum.

The scientific motivation is material identification through diagnostic spectral features. Many minerals, chemicals, and biological materials have absorption features narrower than 50 nm that multispectral sensors cannot resolve. Iron oxides, carbonates, sulfates, and clay minerals each have characteristic SWIR absorptions. Vegetation species differ in subtle features related to leaf chemistry. Water quality parameters each affect the spectrum in distinct narrow-band ways.

The processing pipeline is substantially more demanding. Atmospheric correction must be accurate for each narrow band. Dimensionality reduction techniques (PCA, minimum noise fraction) compress hundreds of correlated bands into meaningful components. Spectral matching compares each pixel against known material spectra. Spectral unmixing estimates fractional abundance of multiple materials within a single pixel.

Current missions include PRISMA, DESIS, and EnMAP, with NASA's SBG planned for global coverage. The technology is also widely deployed on aircraft for targeted campaigns. The trend is toward making hyperspectral data increasingly accessible, but multispectral imaging remains the backbone of operational remote sensing due to simpler processing and longer archives.
