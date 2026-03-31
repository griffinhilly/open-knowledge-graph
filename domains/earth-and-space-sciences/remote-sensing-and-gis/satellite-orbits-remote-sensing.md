---
id: satellite-orbits-remote-sensing
title: Satellite Orbits for Remote Sensing
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: electromagnetic-spectrum-remote-sensing
  type: hard
- id: passive-vs-active-sensors
  type: soft
builds-toward:
- optical-remote-sensing
- radar-remote-sensing-sar
tags:
- satellite-orbits
- sun-synchronous
- geostationary
- remote-sensing
stage: advanced
status: validated
---

# Satellite Orbits for Remote Sensing

## Core Idea
The orbit of a remote sensing satellite determines when, where, and how often it observes any point on Earth. Two orbit families dominate: sun-synchronous orbits (SSO) cross every latitude at the same local solar time, providing consistent illumination for comparative studies, with typical altitudes of 600-900 km and revisit periods of days to weeks. Geostationary orbits (GEO) sit at ~35,786 km above the equator, rotating with Earth to continuously monitor the same hemisphere at coarser spatial resolution. Orbit parameters directly control spatial resolution, swath width, temporal revisit, and illumination geometry.

## Questions

```yaml
- question: "Landsat satellites use a sun-synchronous orbit crossing the equator at approximately 10:00 AM local time. What is the primary advantage of maintaining the same local crossing time?"
  type: multiple-choice
  options:
    - "It maximizes the amount of sunlight reaching the sensor"
    - "It ensures consistent solar illumination geometry across dates, making multi-temporal comparisons valid"
    - "It avoids orbital decay caused by atmospheric drag"
    - "It prevents the satellite from passing over the same area twice"
  answer: 1
  explanation: "Consistent local time means consistent sun angle, shadow length, and illumination intensity across repeat passes. This is critical because differences in reflectance between dates should reflect actual surface change, not varying illumination geometry."

- question: "A geostationary weather satellite can image the same hemisphere every 10-15 minutes, but its spatial resolution is typically 0.5-4 km. This coarser resolution compared to low-earth-orbit satellites exists because geostationary orbit altitude is approximately 36,000 km."
  type: true-false
  answer: true
  explanation: "Spatial resolution is inversely related to altitude for a given sensor aperture. At 36,000 km, each detector element covers a much larger ground area than the same detector at 700 km. The trade-off is temporal resolution versus spatial detail."

- question: "Why do most land-observation satellites use near-polar sun-synchronous orbits rather than equatorial orbits?"
  type: short-answer
  answer: "Near-polar orbits allow the satellite to observe nearly every point on Earth as the planet rotates beneath it, providing global coverage. An equatorial orbit would only image a narrow band around the equator. The sun-synchronous variant adds constant local solar time at each latitude, ensuring repeatable illumination conditions. The slight inclination (~98 degrees) causes the orbital plane to precess at exactly the rate Earth orbits the Sun."
  explanation: "Global coverage plus consistent illumination makes sun-synchronous polar orbits the standard for land and environmental monitoring missions."
```

## Explainer

Building on your understanding of sensor types, the next question is how the platform carrying the sensor determines what you can observe. A satellite's orbit dictates its altitude (controlling spatial resolution and swath width), its ground track pattern (determining geographic coverage), and its revisit period (how often you get a new image of the same location).

Sun-synchronous orbits are the workhorse of land remote sensing. Satellites like Landsat, Sentinel-2, and SPOT fly at 600-900 km altitude in near-polar orbits inclined at about 98 degrees. This inclination exploits Earth's equatorial bulge (J2 perturbation) to make the orbital plane precess eastward at exactly the rate Earth orbits the Sun. The satellite crosses every latitude at the same local solar time on every pass, chosen to balance adequate illumination with minimal cloud buildup.

Geostationary orbits serve a fundamentally different purpose. At 35,786 km altitude, the orbital period matches Earth's rotation, so the satellite appears stationary above a fixed equatorial point. GOES, Meteosat, and Himawari provide continuous hemispheric weather imagery at 10-15 minute intervals. The penalty is spatial resolution: each pixel covers 0.5-4 km on the ground.

The choice between orbit families is the first design decision in any remote sensing mission. It determines what science questions the satellite can answer, what applications it enables, and what complementary data sources are needed to fill its gaps.
