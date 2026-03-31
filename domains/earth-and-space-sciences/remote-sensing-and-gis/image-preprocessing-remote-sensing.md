---
id: image-preprocessing-remote-sensing
title: Image Preprocessing for Remote Sensing
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: optical-remote-sensing
  type: hard
- id: coordinate-systems-projections
  type: soft
builds-toward:
- image-classification-remote-sensing
- change-detection-remote-sensing
- vegetation-indices-ndvi
tags:
- image-preprocessing
- atmospheric-correction
- geometric-correction
- radiometric-calibration
stage: advanced
status: validated
---

# Image Preprocessing for Remote Sensing

## Core Idea
Raw satellite imagery contains systematic distortions that must be corrected before meaningful analysis. Preprocessing transforms raw sensor data into scientifically usable products through three main steps: radiometric calibration (converting raw digital numbers to physical units of radiance or reflectance), atmospheric correction (removing the atmosphere's contribution to isolate the surface signal), and geometric correction (aligning image pixels to accurate ground coordinates). Without preprocessing, pixel values do not represent true surface properties, multi-date comparisons are invalid, and data from different sensors cannot be combined.

## Questions

```yaml
- question: "Two Landsat images of the same area acquired in different seasons show different pixel values over an unchanged concrete surface. What preprocessing step would most directly address this inconsistency?"
  type: multiple-choice
  options:
    - "Pan-sharpening to improve spatial resolution"
    - "Atmospheric correction to remove seasonal differences in atmospheric scattering and absorption, converting to surface reflectance"
    - "Edge enhancement to sharpen feature boundaries"
    - "Principal component analysis to reduce data dimensionality"
  answer: 1
  explanation: "Atmospheric conditions (water vapor, aerosol loading) vary between seasons, adding different amounts of path radiance and absorption to each image. Atmospheric correction removes these atmospheric contributions, yielding surface reflectance values that should be consistent for unchanged surfaces across dates. Without this step, apparent changes may be atmospheric artifacts rather than real surface change."

- question: "Geometric correction of satellite imagery only requires knowledge of the satellite orbit and sensor geometry."
  type: true-false
  answer: false
  explanation: "While orbital parameters and sensor models provide the initial geometric model, terrain-induced distortions (relief displacement) require a DEM for orthorectification, and residual systematic errors often require ground control points (GCPs) -- identifiable features with known coordinates -- for refinement. Without DEM-based orthorectification, images of mountainous terrain can have positional errors of tens to hundreds of meters."

- question: "Explain the difference between top-of-atmosphere (TOA) reflectance and surface reflectance, and why the distinction matters for quantitative remote sensing."
  type: short-answer
  answer: "TOA reflectance is computed from sensor-recorded radiance by accounting for solar illumination geometry and Earth-Sun distance, but it still includes atmospheric effects (scattering and absorption). Surface reflectance additionally removes the atmospheric contribution to isolate the signal from the ground. The distinction matters because surface reflectance is the physically meaningful quantity that describes the surface material, while TOA reflectance conflates surface and atmospheric signals. Vegetation indices, spectral matching, and multi-temporal comparisons require surface reflectance for valid results."
  explanation: "TOA reflectance removes sensor and solar geometry effects; surface reflectance additionally removes atmospheric effects. The latter is required for any analysis comparing pixels across space, time, or sensors."
```

## Explainer

Raw satellite data straight from the sensor is not ready for analysis. It contains a mixture of surface information, atmospheric effects, and geometric distortions that must be systematically separated and corrected. This preprocessing chain is the unglamorous but essential foundation of all quantitative remote sensing.

Radiometric calibration converts raw digital numbers (DN) to physical units. Each sensor has calibration coefficients that convert DN to at-sensor radiance (watts per square meter per steradian per micrometer). From radiance, dividing by the solar irradiance at the top of the atmosphere (adjusted for Earth-Sun distance and solar zenith angle) yields top-of-atmosphere (TOA) reflectance -- a standardized quantity that removes sensor-specific and illumination effects but still includes the atmosphere.

Atmospheric correction is the most scientifically important step. The atmosphere scatters incoming sunlight into the sensor's field of view (path radiance), absorbs portions of both downwelling and upwelling radiation, and alters the spectral distribution of light reaching the surface. Physics-based models (6S, MODTRAN, libRadtran) simulate these processes using atmospheric parameters (aerosol optical depth, water vapor column, ozone) to estimate and remove the atmospheric contribution. The result is surface reflectance -- what the surface would look like if there were no atmosphere.

Geometric correction ensures that pixels map to correct geographic locations. Satellite ephemeris data provides an initial geometric model, but systematic and non-systematic errors require correction using ground control points and, for accurate results, orthorectification using a DEM to remove terrain-induced displacement. The result is an image where each pixel has a reliable geographic coordinate, enabling overlay with other geospatial data and precise multi-temporal registration essential for change detection.
