---
id: gravity-data-reduction
title: 'Gravity Data Reduction: Bouguer, Free-Air, and Terrain Corrections'
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
- id: gravity-potential-theory-earths-field
  type: hard
builds-toward:
- gravity-forward-modeling-inversion
tags:
- gravity
- data-reduction
- corrections
- bouguer
stage: advanced
status: draft
---

# Gravity Data Reduction: Bouguer, Free-Air, and Terrain Corrections

## Core Idea
Observed gravity must be corrected for latitude (normal gravity), elevation (free-air correction), topographic masses (terrain correction), and bathymetry to isolate subsurface anomalies. The Bouguer anomaly (with assumed density slab) reveals density variations with depth.

## Explainer

From your study of gravity surveys and potential theory, you know that a gravimeter measures the total gravitational acceleration at a station. But that raw measurement is a composite of many effects — the station's latitude, its elevation above sea level, the mass of rock and topography surrounding it, and the subsurface density anomalies you actually want to find. **Gravity data reduction** is the systematic process of stripping away the known, predictable contributions so that only the geologically interesting signal remains.

The first correction accounts for latitude. Earth is an oblate spheroid, so gravity varies from about 9.78 m/s² at the equator to 9.83 m/s² at the poles. The **normal gravity** formula (based on the reference ellipsoid) predicts what gravity should be at any latitude on a hypothetical smooth Earth with no topography. Subtracting this removes the largest source of variation and gives you the **gravity anomaly** — the difference between observed and predicted values.

Next comes the **free-air correction**, which accounts for elevation. A station at 1,000 m elevation is farther from Earth's center than one at sea level, so it experiences weaker gravity — roughly 0.3086 mGal per meter of elevation. The free-air correction adds this back, effectively projecting all measurements down to a common reference surface (the geoid). The result is the **free-air anomaly**, which is useful for studying large-scale isostatic balance but still contains the gravitational effect of the rock mass between the station and sea level.

The **Bouguer correction** removes that rock mass by modeling it as an infinite horizontal slab of assumed density (typically 2,670 kg/m³ for continental crust). This subtraction eliminates the gravitational pull of the topographic mass itself. In mountainous terrain, the infinite slab approximation is too crude — nearby peaks and valleys produce gravitational effects that the slab model misses. The **terrain correction** fixes this by calculating the gravitational influence of the actual topography around each station and adding it to the Bouguer anomaly. The fully corrected result — the **complete Bouguer anomaly** — isolates lateral density variations beneath the surface: exactly what you need to detect buried structures like ore bodies, sedimentary basins, or the depth to the Moho.
