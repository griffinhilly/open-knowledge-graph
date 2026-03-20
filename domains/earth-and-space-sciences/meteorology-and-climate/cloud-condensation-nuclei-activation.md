---
id: cloud-condensation-nuclei-activation
title: Cloud Condensation Nuclei and Activation Theory
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: cloud-formation-and-types
  type: hard
- id: relative-humidity-saturation-indices
  type: hard
builds-toward:
- bergeron-process-ice-precipitation
- cloud-microphysics-initiation
tags:
- microphysics
- nucleation
- aerosol
stage: advanced
status: draft
---

# Cloud Condensation Nuclei and Activation Theory

## Core Idea
Cloud droplets form on hygroscopic aerosol particles (CCN) when supersaturation exceeds critical thresholds determined by particle size and composition. Larger particles and more soluble materials activate at lower supersaturation. The number and type of available CCN influence cloud droplet size distribution and affect cloud properties, precipitation efficiency, and climate impacts of aerosols.

## How It's Best Learned
Study the Köhler equation for critical supersaturation; examine how different aerosol types (sea salt, dust, sulfate) affect cloud formation; connect to cloud microphysics measurements.

## Common Misconceptions
- Thinking clouds form simply when air reaches 100% relative humidity (requires specific aerosol particles).
- Assuming more aerosol particles always lead to more and heavier precipitation (higher CCN actually produces smaller droplets).

## Explainer

From your study of cloud formation, you know that clouds appear when air cools to its dew point and water vapor condenses into droplets. But there is a hidden problem: pure water vapor strongly resists condensing into tiny droplets. The curved surface of a newly formed droplet has higher vapor pressure than a flat water surface (the **Kelvin effect**), meaning a microscopic droplet evaporates faster than it grows unless the surrounding air is extremely supersaturated — far beyond the modest supersaturations of 0.1–1% that actually occur in clouds. Without help, cloud droplets would almost never form.

The help comes from **cloud condensation nuclei (CCN)** — tiny aerosol particles suspended in the atmosphere. These particles, which include sea salt, sulfate from pollution, dust, and organic compounds, are **hygroscopic**: they attract and dissolve in water. When water vapor condenses onto a CCN, the dissolved material lowers the vapor pressure of the solution surface (the **solute effect**, described by Raoult's law). This reduction in vapor pressure counteracts the Kelvin effect's tendency to evaporate small droplets. The competition between these two effects is captured by the **Köhler equation**, which predicts a critical supersaturation for each particle. Once the ambient supersaturation exceeds this critical value, the particle **activates** — it begins growing spontaneously into a cloud droplet that will not evaporate back.

Larger particles and more soluble materials activate at lower supersaturations because the solute effect is stronger (more dissolved material, lower vapor pressure). A large sea salt particle might activate at just 0.05% supersaturation, while a small, less soluble dust grain might require 0.5% or more. In a rising air parcel, supersaturation builds gradually as cooling outpaces condensation. The most favorable CCN activate first, and as supersaturation peaks (usually within the first few hundred meters above cloud base), a characteristic population of droplets is established.

This activation process has profound consequences for cloud properties and climate. In clean marine air with few CCN, the available water condenses onto a small number of particles, producing relatively few but large droplets — clouds that are optically thin and rain efficiently. In polluted continental air with abundant CCN, the same amount of water is distributed across many more particles, producing numerous small droplets — clouds that are brighter (reflecting more sunlight) but less likely to produce rain because the droplets are too small to coalesce efficiently. This is the **Twomey effect**, and it represents one of the largest uncertainties in understanding how human aerosol emissions influence Earth's climate.
