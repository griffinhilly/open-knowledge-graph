---
id: absolute-relative-vorticity
title: Absolute and Relative Vorticity
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: coriolis-effect
  type: hard
- id: wind-shear-and-vorticity
  type: hard
builds-toward:
- potential-vorticity-conservation
tags:
- rotation
- vorticity
- wind
- shear
stage: abstract-reasoning
status: draft
---

# Absolute and Relative Vorticity

## Core Idea
Absolute vorticity is the sum of the planet's rotation (planetary vorticity, 2Ω) and the wind's rotation relative to the Earth (relative vorticity). In the Northern Hemisphere, planetary vorticity is always positive, meaning even still air has vorticity due to Earth's rotation. Cyclones have large positive relative vorticity, while anticyclones have negative relative vorticity that can partially cancel planetary vorticity.

## How It's Best Learned
Calculate relative vorticity from wind field divergence using finite differences. Trace how total absolute vorticity changes along a parcel trajectory.
