---
id: change-detection-remote-sensing
title: Change Detection in Remote Sensing
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: image-classification-remote-sensing
  type: hard
- id: image-preprocessing-remote-sensing
  type: hard
builds-toward:
- land-use-land-cover-mapping
- disaster-monitoring-remote-sensing
tags:
- change-detection
- multi-temporal
- time-series
- remote-sensing
stage: advanced
status: validated
---

# Change Detection in Remote Sensing

## Core Idea
Change detection identifies differences in the state of a landscape between two or more dates by comparing remote sensing images acquired at different times. Techniques range from simple image differencing (subtracting one date from another) to post-classification comparison (classifying each date independently and comparing the maps) to advanced time-series analysis that tracks continuous change trajectories. Reliable change detection requires that differences between images reflect actual surface change rather than artifacts from atmospheric conditions, sensor calibration, illumination geometry, or phenological cycles. This makes preprocessing and careful image selection critical.

## Questions

```yaml
- question: "An image difference map (Date2 - Date1) of NDVI values shows large negative values in a forest region. Which interpretation is most likely?"
  type: multiple-choice
  options:
    - "The forest grew significantly between dates"
    - "Vegetation loss occurred (deforestation, fire, disease) causing NDVI to decrease"
    - "Atmospheric conditions improved between the two dates"
    - "The sensor gain was reduced for the second acquisition"
  answer: 1
  explanation: "NDVI decreases when vegetation health or cover declines (reduced NIR reflectance relative to red). Large negative NDVI differences in a forest indicate substantial vegetation loss -- from logging, fire, insect damage, or storm damage. Atmospheric and sensor artifacts should have been removed by preprocessing; seasonal phenology is controlled by selecting anniversary dates."

- question: "Comparing two images acquired in different seasons is sufficient for detecting land cover change because seasonal vegetation differences average out."
  type: true-false
  answer: false
  explanation: "Seasonal differences (phenology) can overwhelm actual land cover change signals. A deciduous forest photographed in summer (leaf-on, high NDVI) and winter (leaf-off, low NDVI) shows dramatic spectral differences that have nothing to do with land cover change. Reliable change detection typically requires anniversary date images (same time of year) or time-series approaches that model and remove the seasonal cycle."

- question: "What advantage does time-series change detection (e.g., LandTrendr, BFAST) offer over simple bi-temporal comparison?"
  type: short-answer
  answer: "Time-series approaches use all available observations (potentially hundreds of images over decades) to model the temporal trajectory of each pixel, distinguishing gradual trends (forest degradation, urban sprawl) from abrupt events (fire, harvest) and from seasonal noise. Bi-temporal comparison can only detect net change between two dates, missing the timing, duration, and nature of change events. Time-series methods are also more robust to individual noisy observations because they fit models through many data points rather than relying on just two."
  explanation: "Dense time-series analysis transforms change detection from 'did it change?' to 'when, how fast, and what type of change occurred?'"
```

## Explainer

Remote sensing's unique power is not just mapping what is on Earth's surface at one moment, but tracking how it changes over time. With archives stretching back to 1972 (Landsat), analysts can reconstruct decades of landscape transformation -- deforestation, urban expansion, glacial retreat, coastal erosion -- at scales from individual parcels to entire continents.

The simplest approach is image differencing: subtract one date's spectral values (or derived index like NDVI) from another. Pixels with large differences are flagged as changed. This is fast and intuitive but sensitive to noise and requires very careful preprocessing to ensure that differences reflect actual change. Post-classification comparison independently classifies each date and compares the resulting maps, producing a from-to change matrix (e.g., forest-to-agriculture, agriculture-to-urban). This provides thematic change information but accumulates classification errors from both dates.

Modern time-series approaches exploit the growing density of satellite observations. Algorithms like LandTrendr fit piecewise linear models to each pixel's spectral trajectory over decades, identifying break points that correspond to disturbance events. BFAST decomposes time series into trend, seasonal, and residual components, detecting both abrupt breaks and gradual trends. Google Earth Engine and similar cloud platforms make it feasible to process thousands of images per pixel, transforming change detection from a bi-temporal exercise into continuous monitoring.

The persistent challenge is separating real change from confounding factors: phenological cycles, atmospheric variability, sensor degradation, and registration errors. Successful change detection demands not just algorithms but careful experimental design -- selecting appropriate dates, ensuring comparable preprocessing, understanding the landscape's natural variability, and validating results against independent data. A change map without accuracy assessment is an assertion, not evidence.
