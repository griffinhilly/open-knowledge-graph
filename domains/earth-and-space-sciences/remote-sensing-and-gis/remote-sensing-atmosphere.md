---
id: remote-sensing-atmosphere
title: Remote Sensing of the Atmosphere
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: hard
- id: passive-vs-active-sensors
  type: hard
builds-toward:
- disaster-monitoring-remote-sensing
tags:
- atmospheric-remote-sensing
- aerosols
- trace-gases
- weather-satellites
stage: advanced
status: validated
---

# Remote Sensing of the Atmosphere

## Core Idea
Atmospheric remote sensing measures the composition, structure, and dynamics of Earth's atmosphere from satellites. While surface remote sensing treats the atmosphere as an obstacle (to be corrected away), atmospheric remote sensing treats it as the target. Key measurements include atmospheric temperature and humidity profiles (from infrared and microwave sounders), cloud properties (from visible, infrared, and radar sensors), aerosol distribution (from multi-angle and polarimetric sensors), trace gas concentrations (from ultraviolet, visible, and infrared spectrometers), and precipitation (from radar and passive microwave). These measurements drive weather forecasting, climate monitoring, and air quality assessment.

## Questions

```yaml
- question: "The TROPOMI instrument on Sentinel-5P measures nitrogen dioxide (NO2) columns by detecting specific absorption features in reflected sunlight. What spectral region does it use for NO2 retrieval?"
  type: multiple-choice
  options:
    - "Thermal infrared (10-12 um)"
    - "Visible blue-violet (400-465 nm), where NO2 has strong absorption bands"
    - "Microwave (10-30 GHz)"
    - "Near-infrared (1.0-1.3 um)"
  answer: 1
  explanation: "NO2 absorbs strongly in the blue-violet portion of the visible spectrum. By measuring the depth of these absorption features in sunlight reflected from the surface and atmosphere, TROPOMI retrieves the total column amount of NO2. This has revealed urban pollution hotspots, shipping lanes, and the dramatic drop in NO2 during COVID-19 lockdowns at unprecedented spatial detail."

- question: "Weather satellites in geostationary orbit can directly measure atmospheric temperature profiles from space."
  type: true-false
  answer: true
  explanation: "Infrared sounders on geostationary satellites measure thermal emission at multiple wavelengths in CO2 absorption bands. Because CO2 is well-mixed and its concentration is known, the emission at different wavelengths originates from different altitudes (stronger absorption = higher altitude of emission). By measuring emission in a series of channels with different CO2 absorption strengths, the instrument retrieves temperature at multiple atmospheric levels -- a technique called thermal sounding."

- question: "Explain how satellite-based lidar (like CALIPSO's CALIOP) provides information that passive atmospheric sensors cannot."
  type: short-answer
  answer: "CALIOP transmits laser pulses and measures the backscattered return as a function of time (altitude), producing vertical cross-sections of the atmosphere. This reveals the vertical distribution of clouds and aerosol layers -- their altitude, thickness, and optical properties. Passive sensors view the atmosphere from above and can measure column-integrated quantities but cannot determine the vertical structure. CALIOP can distinguish high thin cirrus from low thick stratus, identify elevated dust plumes versus boundary-layer pollution, and detect the altitude of volcanic ash layers critical for aviation safety."
  explanation: "Active lidar provides vertical resolution that passive sensors fundamentally lack, resolving the 3D structure of the atmosphere rather than just column-integrated properties."
```

## Explainer

While most remote sensing courses focus on observing Earth's surface, the atmosphere is itself a complex, dynamic target observed by a dedicated constellation of satellites. Atmospheric remote sensing provides the data that drives weather forecasts, tracks air quality, monitors the ozone layer, and measures greenhouse gas concentrations for climate science.

Temperature and humidity profiling uses infrared and microwave sounders that measure thermal emission from the atmosphere at wavelengths where specific gases (primarily CO2 and H2O) absorb and emit. By selecting channels with different absorption strengths, sounders sample different atmospheric layers -- strong absorption channels see only the upper atmosphere, while weak absorption channels see down to the surface. This vertical sounding technique produces temperature and moisture profiles essential for initializing numerical weather prediction models.

Trace gas remote sensing exploits the spectral fingerprints of molecules. Each atmospheric gas absorbs at characteristic wavelengths: ozone in the ultraviolet, NO2 in the visible, CO and CH4 in the shortwave infrared, CO2 at 4.3 um and 15 um. Spectrometers with sufficient spectral resolution can measure the absorption depth and retrieve the column concentration of each gas. Instruments like TROPOMI, OMI, and OCO-2 have mapped air pollution, methane leaks, and carbon dioxide distribution with increasing spatial detail, informing both science and policy.

Precipitation estimation combines multiple sensor types. Passive microwave radiometers detect the scattering signature of ice particles in clouds. Cloud-profiling radar (on CloudSat and GPM) directly measures precipitation structure. Geostationary infrared imagery provides temporal context -- cold cloud tops indicate deep convection and heavy rain. The Global Precipitation Measurement (GPM) mission merges these observations to produce near-real-time global precipitation maps at 0.1-degree resolution every 30 minutes.
