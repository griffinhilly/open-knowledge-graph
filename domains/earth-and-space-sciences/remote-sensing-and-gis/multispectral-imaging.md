---
id: multispectral-imaging
title: Multispectral Imaging
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: optical-remote-sensing
  type: hard
- id: electromagnetic-spectrum-remote-sensing
  type: hard
builds-toward:
- hyperspectral-imaging
- vegetation-indices-ndvi
- image-classification-remote-sensing
tags:
- multispectral
- spectral-bands
- landsat
- sentinel
stage: advanced
status: validated
---

# Multispectral Imaging

## Core Idea
Multispectral sensors capture images in a discrete number of relatively broad spectral bands (typically 4-12), each covering 20-200 nanometers. Each band targets a specific physical property: blue for water penetration, green for vegetation vigor, red for chlorophyll absorption, near-infrared for vegetation structure, shortwave infrared for moisture and minerals. The result is a multi-layer data cube where each pixel has a reflectance value in every band, enabling band combinations and ratios that discriminate surface materials far beyond what a single band or photograph can achieve.

## Questions

```yaml
- question: "Sentinel-2 includes three bands in the red-edge region (705, 740, and 783 nm). What is the primary purpose of these red-edge bands?"
  type: multiple-choice
  options:
    - "To improve the aesthetic quality of true-color images"
    - "To capture the steep increase in vegetation reflectance between red absorption and NIR reflection, enabling finer discrimination of vegetation health"
    - "To detect thermal emissions from volcanic regions"
    - "To penetrate cloud cover more effectively than standard visible bands"
  answer: 1
  explanation: "The red edge (680-750 nm) is where vegetation reflectance transitions sharply from low (chlorophyll absorption) to high (mesophyll scattering). Three bands sampling this transition enable detection of subtle vegetation condition changes that broad red and NIR bands would miss."

- question: "A multispectral image with 4 bands (blue, green, red, NIR) contains only 4 independent pieces of information per pixel."
  type: true-false
  answer: false
  explanation: "While there are 4 measured values per pixel, band ratios, normalized differences, and other indices create derived information. NDVI isolates vegetation signal from soil background. Band ratios suppress illumination variation. The information content exceeds the raw band count because it includes relationships between bands."

- question: "Why does Landsat include a shortwave infrared (SWIR) band around 1.6 micrometers in addition to visible and NIR bands?"
  type: short-answer
  answer: "The 1.6 um SWIR band is sensitive to moisture content because water strongly absorbs at this wavelength. It also reveals clay mineral absorption features useful for geological mapping. For snow/cloud discrimination, snow absorbs at 1.6 um while clouds reflect, allowing automated separation. These capabilities complement visible/NIR bands, which are insensitive to moisture and mineral composition."
  explanation: "Each spectral band targets specific physical properties. SWIR adds moisture and mineral sensitivity that visible/NIR bands lack."
```

## Explainer

From optical remote sensing fundamentals, you know that surface materials reflect sunlight differently across wavelengths. Multispectral imaging operationalizes this by sampling the reflected spectrum at strategically chosen wavelength bands selected to maximize discrimination of important surface features.

The design philosophy is targeted sampling. Each band exists for a reason. Landsat 8's OLI has 9 bands: coastal/aerosol for atmospheric studies, blue for water penetration, green for peak vegetation reflectance, red for chlorophyll absorption, NIR for vegetation structure, two SWIR bands for moisture and minerals, a panchromatic band for sharpening, and a cirrus band for thin cloud detection.

The analytical power comes from band math. NDVI uses (NIR - Red)/(NIR + Red) to quantify vegetation density while minimizing illumination effects. Similar normalized differences target water (NDWI), snow (NDSI), and built-up areas (NDBI). False-color composites display non-visible bands as visible colors, making invisible patterns immediately apparent.

The trade-off of multispectral imaging is that broad bands average over many spectral features, potentially mixing distinct absorption signatures. Hyperspectral imaging addresses this but at the cost of data volume and complexity. For most applications, multispectral imaging provides the right balance.
