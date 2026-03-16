---
id: thermodynamic-diagram-analysis
title: Thermodynamic Diagrams and Atmospheric Sounding Analysis
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: adiabatic-lapse-rates
  type: hard
- id: saturation-and-dew-point
  type: hard
- id: convective-instability-indices
  type: hard
builds-toward:
- severe-weather-systems
- latent-heating-in-weather-systems
tags:
- skew-T
- sounding
- hodograph
- thermodynamic-diagram
- analysis
stage: abstract-reasoning
status: draft
---

# Thermodynamic Diagrams and Atmospheric Sounding Analysis

## Core Idea
Atmospheric soundings—vertical profiles of temperature, dew point, and wind measured by radiosondes—are plotted on thermodynamic diagrams (like skew-T log-P diagrams) to visualize atmospheric structure. These diagrams allow forecasters to identify stable and unstable layers, estimate parcel lifting levels and heights, calculate CAPE, and analyze wind shear by examining hodographs (wind vectors at different heights). Proper sounding interpretation is essential for severe weather forecasting.

## Explainer

You already understand adiabatic lapse rates (how rising parcels cool), saturation and dew point (when moisture condenses), and convective instability indices (how to quantify the atmosphere's potential for thunderstorms). A **thermodynamic diagram** is the tool that brings all of these concepts together on a single chart, letting you visually read the atmosphere's vertical structure and predict what will happen when air is lifted.

The most widely used diagram is the **skew-T log-P diagram**. The vertical axis is pressure (decreasing upward on a logarithmic scale, so that equal vertical distances represent roughly equal altitude intervals). The horizontal axis is temperature, but the isotherms are tilted — "skewed" — to the right, which spreads out the temperature and dew point lines and makes the diagram easier to read. On this chart, a radiosonde sounding appears as two lines: the **temperature trace** (solid, on the right) and the **dew point trace** (dashed, on the left). Where these two lines are close together, the air is moist; where they diverge, the air is dry. When they touch, the air is saturated — you are inside a cloud.

Overlaid on the diagram are reference lines you already know: dry adiabats (the ~9.8°C/km cooling rate of unsaturated rising air), moist adiabats (the slower cooling rate once condensation begins and releases latent heat), and mixing ratio lines (constant moisture content). To assess stability, you trace a hypothetical parcel upward from the surface: it follows the dry adiabat until it reaches its **Lifted Condensation Level** (where temperature meets dew point and a cloud forms), then follows the moist adiabat above that. Wherever the parcel's traced path is warmer than the environmental temperature line, the parcel is buoyant and will accelerate upward — this is unstable air. The area between the parcel's path and the environment where the parcel is warmer represents **CAPE** (Convective Available Potential Energy), the total energy available to fuel thunderstorm updrafts. The larger that area, the more explosive the convection.

A **hodograph** complements the thermodynamic diagram by plotting wind vectors at different heights as a connected curve. The shape of the hodograph reveals wind shear structure: a straight hodograph indicates unidirectional shear (winds strengthening with height but not turning), while a curved hodograph indicates directional shear — winds turning clockwise with height. Curved hodographs are associated with rotating updrafts and supercell thunderstorms. Together, the skew-T and hodograph give a forecaster a complete picture: the skew-T reveals whether the atmosphere can produce deep convection (instability and moisture), while the hodograph reveals whether that convection can organize into severe, rotating storms. Learning to read these diagrams is the gateway to operational weather forecasting.
