---
id: buoyancy-and-archimedes
title: Buoyancy and Archimedes' Principle
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-statics-pressure
  type: hard
builds-toward:
- hydrostatic-forces-on-surfaces
tags:
- buoyancy
- Archimedes
- flotation
- submerged bodies
stage: formal-systems
status: draft
---

# Buoyancy and Archimedes' Principle

## Core Idea
Archimedes' principle states that a body submerged or floating in a fluid experiences an upward buoyant force equal to the weight of fluid displaced. The buoyant force acts through the center of buoyancy, which is the centroid of the displaced fluid volume. For flotation, the weight of the object equals the weight of fluid displaced, setting the draft depth.

## How It's Best Learned
Derive the buoyant force by integrating hydrostatic pressure over the submerged surface, then verify it equals ρ_fluid × g × V_displaced. Apply to objects of varying density to predict sinking, floating, or neutral buoyancy before checking with physical experiments.

## Common Misconceptions
- Buoyancy depends on the displaced fluid volume, not the object's volume if only partially submerged.
- A denser object can float if shaped to displace enough fluid (e.g., a steel ship).
- The buoyant force is unchanged whether the object is at different depths, as long as it remains fully submerged in an incompressible fluid.
