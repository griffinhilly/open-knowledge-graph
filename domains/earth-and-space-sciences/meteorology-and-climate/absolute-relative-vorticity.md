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
stage: advanced
status: draft
---

# Absolute and Relative Vorticity

## Core Idea
Absolute vorticity is the sum of the planet's rotation (planetary vorticity, 2Ω) and the wind's rotation relative to the Earth (relative vorticity). In the Northern Hemisphere, planetary vorticity is always positive, meaning even still air has vorticity due to Earth's rotation. Cyclones have large positive relative vorticity, while anticyclones have negative relative vorticity that can partially cancel planetary vorticity.

## How It's Best Learned
Calculate relative vorticity from wind field divergence using finite differences. Trace how total absolute vorticity changes along a parcel trajectory.

## Explainer

You already know from studying the Coriolis effect that Earth's rotation deflects moving air, and from wind shear and vorticity that spinning motion in the atmosphere can be measured as vorticity — the tendency of air to rotate about a vertical axis. The next step is recognizing that the atmosphere always has two sources of rotation happening simultaneously, and separating them is essential for understanding how weather systems develop and move.

**Relative vorticity** is the spin of the wind as seen by someone standing on Earth's surface. A counterclockwise-rotating low-pressure system in the Northern Hemisphere has positive relative vorticity; a clockwise-spinning anticyclone has negative relative vorticity. You can estimate it by looking at how wind speed and direction change across a region — if the winds curve cyclonically or if there is strong speed shear across the flow, relative vorticity is large. Think of it as the local spin the atmosphere has generated through its own dynamics — pressure gradients, friction, and convergence.

**Planetary vorticity** is the spin that Earth's rotation contributes, even to perfectly still air. At the poles, a stationary air parcel completes one full rotation per day relative to the stars, so planetary vorticity is at its maximum. At the equator, a parcel sitting on the surface has no vertical-axis rotation from Earth's spin, so planetary vorticity is zero. The quantity varies smoothly with latitude and equals 2Ω sin(φ), where Ω is Earth's angular velocity and φ is latitude. This is the same Coriolis parameter f you encountered earlier.

**Absolute vorticity** is simply the sum of these two: relative vorticity plus planetary vorticity (ζ + f). It represents the total spin of an air parcel as viewed from space. This quantity matters because it is approximately conserved as air parcels move — a principle that leads directly to potential vorticity conservation. When a parcel moves poleward, f increases, so ζ must decrease to compensate: the flow becomes more anticyclonic. When a parcel moves equatorward, f decreases and ζ increases, promoting cyclonic curvature. This trade-off between planetary and relative vorticity explains why upper-level troughs and ridges develop wavelike patterns — the atmosphere is constantly adjusting its spin budget as parcels shift latitude, producing the Rossby waves that steer weather systems across the mid-latitudes.
