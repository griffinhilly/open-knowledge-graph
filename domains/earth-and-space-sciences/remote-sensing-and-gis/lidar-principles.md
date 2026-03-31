---
id: lidar-principles
title: LiDAR Principles
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: passive-vs-active-sensors
  type: hard
- id: electromagnetic-spectrum-remote-sensing
  type: soft
builds-toward:
- digital-elevation-models
- photogrammetry
tags:
- lidar
- point-cloud
- terrain-mapping
- active-sensors
stage: advanced
status: validated
---

# LiDAR Principles

## Core Idea
LiDAR (Light Detection and Ranging) transmits laser pulses (typically near-infrared, ~1064 nm) and measures the round-trip time to derive precise distances to reflecting surfaces. When mounted on aircraft with GPS and inertial navigation, LiDAR generates dense three-dimensional point clouds with centimeter-level vertical accuracy. Unlike passive imagery (2D), LiDAR directly measures elevation and can record multiple returns per pulse -- first return from tree canopy, intermediate returns from branches, last return from the ground -- enabling separation of vegetation from terrain.

## Questions

```yaml
- question: "A LiDAR survey over dense forest records multiple returns from a single pulse. What do the first and last returns typically represent?"
  type: multiple-choice
  options:
    - "First return: ground surface; Last return: top of canopy"
    - "First return: top of canopy; Last return: ground surface beneath the vegetation"
    - "First return: cloud base; Last return: canopy top"
    - "Both returns represent the same surface at different angles"
  answer: 1
  explanation: "The pulse hits the canopy first (first return from uppermost foliage). Portions penetrate through gaps, reflecting off branches (intermediate returns) and eventually the ground (last return). The difference gives canopy height. This multi-return capability is what makes LiDAR uniquely powerful for forestry."

- question: "LiDAR cannot map the ocean floor because laser light does not penetrate water."
  type: true-false
  answer: false
  explanation: "Bathymetric LiDAR uses green wavelength lasers (~532 nm) that penetrate clear water to approximately 40-70 meters. The system fires both a near-infrared pulse (reflects off the water surface) and a green pulse (penetrates to the bottom), using the time difference to measure depth. This only works in relatively clear water."

- question: "Explain how LiDAR bare-earth DEMs are created from point clouds that include vegetation and buildings."
  type: short-answer
  answer: "Ground classification algorithms identify the lowest points in local neighborhoods and iteratively build a surface model, rejecting points above this surface as vegetation or structures. Last-return points are more likely to represent ground. The classified ground points are then interpolated (via TIN or kriging) to create a continuous bare-earth DEM. The challenge is distinguishing low vegetation from ground, requiring adaptive filtering that accounts for terrain slope and point density."
  explanation: "The multi-return capability is essential: without it, separating ground from above-ground objects would require assumptions rather than direct measurements."
```

## Explainer

While radar uses microwave pulses, LiDAR uses laser pulses -- highly focused beams of light, typically at 1064 nm (near-infrared) for topographic mapping or 532 nm (green) for bathymetric mapping. The fundamental measurement is the precise round-trip travel time of each pulse, giving distance with centimeter-level accuracy.

An airborne LiDAR system integrates three components: the laser scanner (firing 100,000 to 1,000,000 pulses per second), a GPS receiver (providing aircraft position to centimeter accuracy), and an inertial measurement unit (recording aircraft orientation). Together these produce a georeferenced 3D coordinate for every return, generating a point cloud with densities of 1-100+ points per square meter.

The multi-return capability distinguishes LiDAR from other elevation technologies. A single pulse encountering a tree is partly reflected by canopy, branches, and ground. Full-waveform systems record the complete return signal for even finer vertical decomposition. This allows creation of both a Digital Surface Model (including canopy) and a Digital Terrain Model (bare earth) -- the difference being the Canopy Height Model.

Applications span forestry (canopy height, biomass), flood modeling (high-accuracy terrain for hydraulic simulation), archaeology (revealing structures beneath forest canopy), urban modeling (3D city models), and coastal erosion monitoring. Space-based LiDAR (ICESat-2, GEDI) extends these capabilities globally at lower point densities.
