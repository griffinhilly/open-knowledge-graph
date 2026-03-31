---
id: vegetation-indices-ndvi
title: Vegetation Indices and NDVI
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: multispectral-imaging
  type: hard
- id: image-preprocessing-remote-sensing
  type: soft
builds-toward:
- land-use-land-cover-mapping
- change-detection-remote-sensing
tags:
- NDVI
- vegetation-indices
- vegetation-monitoring
- spectral-indices
stage: advanced
status: validated
---

# Vegetation Indices and NDVI

## Core Idea
Vegetation indices are mathematical combinations of spectral bands designed to enhance the vegetation signal while minimizing confounding factors like soil background, illumination variation, and atmospheric effects. The Normalized Difference Vegetation Index (NDVI) -- calculated as (NIR - Red)/(NIR + Red) -- is the most widely used, exploiting the contrast between chlorophyll absorption in the red band and strong scattering in the near-infrared by leaf mesophyll. NDVI ranges from -1 to +1, with dense healthy vegetation near 0.8-0.9, sparse vegetation around 0.2-0.4, bare soil near 0.1, and water typically negative. Other indices address specific limitations: EVI reduces atmospheric and soil effects, SAVI adjusts for varying soil brightness, and NDWI targets water content.

## Questions

```yaml
- question: "A farmer notices that NDVI values in one section of a wheat field dropped from 0.75 to 0.45 over two weeks while the rest of the field remained stable. What is the most likely interpretation?"
  type: multiple-choice
  options:
    - "The satellite sensor malfunctioned during the second acquisition"
    - "That section experienced vegetation stress (disease, drought, pest damage, or nutrient deficiency) reducing chlorophyll and/or leaf area"
    - "Cloud shadow fell on that section during the second image"
    - "The soil in that section changed color due to rainfall"
  answer: 1
  explanation: "A localized NDVI drop of 0.3 units while surrounding areas remain stable indicates real vegetation change, not sensor or atmospheric artifacts (which would affect broader areas). Reduced chlorophyll decreases red absorption (raising red reflectance), while reduced leaf area decreases NIR reflectance, both lowering NDVI. This spatial pattern points to a localized stress factor."

- question: "NDVI saturates (becomes insensitive to further increases) at high vegetation densities because the NIR and red reflectance values both plateau once leaf area index exceeds approximately 3-4."
  type: true-false
  answer: true
  explanation: "As vegetation density increases, red reflectance approaches its minimum (nearly complete absorption) and NIR reflectance approaches its maximum. Beyond LAI ~3-4, additional leaves do not significantly change the spectrum visible from above because the canopy is already optically thick. NDVI therefore cannot distinguish between moderately dense and very dense vegetation. The Enhanced Vegetation Index (EVI) partially addresses this by incorporating blue band correction and remaining more sensitive at high biomass."

- question: "Why is the normalization in NDVI (dividing by NIR + Red) important compared to a simple difference (NIR - Red)?"
  type: short-answer
  answer: "Normalization reduces sensitivity to illumination intensity variations caused by different sun angles, topographic shadows, and thin clouds. A simple difference would produce larger values on brightly illuminated slopes and smaller values in shadows, even for the same vegetation. Normalization produces a ratio that is more consistent across illumination conditions because both numerator and denominator scale proportionally with illumination intensity. This makes NDVI more comparable across dates, sensors, and terrain."
  explanation: "The ratio format creates a dimensionless index that emphasizes the spectral contrast between bands rather than absolute brightness, improving comparability."
```

## Explainer

The spectral signature of vegetation -- low red reflectance from chlorophyll absorption, high NIR reflectance from leaf structure scattering -- is arguably the single most important pattern in remote sensing. Vegetation indices distill this pattern into a single number that can be mapped, tracked over time, and correlated with biophysical variables like leaf area index, biomass, fractional cover, and productivity.

NDVI's elegance lies in its simplicity and interpretability. By normalizing the NIR-Red contrast, it creates a dimensionless index that suppresses much of the illumination variability while amplifying the vegetation signal. Global NDVI time series from AVHRR (1981-present) and MODIS (2000-present) have revealed planetary-scale patterns: the seasonal green wave sweeping poleward each spring, drought-induced vegetation decline across the Sahel, and the global greening trend driven by CO2 fertilization and warming temperatures.

However, NDVI has well-documented limitations. It saturates over dense vegetation (LAI > 3-4), is sensitive to soil brightness in sparse canopies, and is affected by atmospheric aerosols. The Enhanced Vegetation Index (EVI) addresses these issues by incorporating a blue band for atmospheric correction and soil adjustment factors, maintaining sensitivity in high-biomass regions like tropical forests. The Soil-Adjusted Vegetation Index (SAVI) adds a soil brightness correction factor useful in arid environments. Water-related indices (NDWI, NDMI) replace the red band with SWIR to target canopy moisture content.

The practical value of vegetation indices extends far beyond ecological research. Precision agriculture uses NDVI maps to guide variable-rate fertilizer and irrigation application. Crop insurance programs use satellite NDVI to verify claims. Rangeland managers track forage production. Carbon cycle models assimilate NDVI as a proxy for photosynthetic activity. In each case, the vegetation index translates complex spectral data into actionable information.
