---
id: hydrostatic-forces-on-surfaces
title: Hydrostatic Forces on Submerged Surfaces
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-statics-pressure
  type: hard
- id: area-moment-of-inertia-engineering
  type: soft
- id: centroid-areas-composite
  type: soft
builds-toward:
- control-volume-momentum
tags:
- hydrostatic force
- center of pressure
- plane surfaces
- curved surfaces
stage: formal-systems
status: draft
---

# Hydrostatic Forces on Submerged Surfaces

## Core Idea
The resultant hydrostatic force on a submerged plane surface equals the pressure at the centroid times the surface area: F = ρg·ȳ·A. However, the resultant acts at the center of pressure, which lies below the centroid by an amount proportional to the second moment of area about the centroidal axis divided by (ȳ·A). For curved surfaces, horizontal and vertical components are found separately using projected areas and displaced volumes.

## How It's Best Learned
First solve flat gate and dam problems analytically, locating both magnitude and center of pressure. Then use the principle that the vertical force on a curved surface equals the weight of fluid above it to handle gates, domes, and tanks.

## Common Misconceptions
- The center of pressure is always below the centroid for a submerged surface, never above it.
- The resultant force does not act at the centroid unless the surface is under uniform pressure.
- For curved surfaces, you cannot directly integrate a vector pressure; decompose into horizontal and vertical components.
