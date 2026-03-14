---
id: fluid-statics-pressure
title: Fluid Statics and Hydrostatic Pressure
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
- id: equilibrium-particles-3d
  type: soft
builds-toward:
- manometry-and-pressure-measurement
- buoyancy-and-archimedes
- hydrostatic-forces-on-surfaces
tags:
- pressure
- hydrostatics
- Pascal's law
- pressure variation
stage: formal-systems
status: validated
---

# Fluid Statics and Hydrostatic Pressure

## Core Idea
In a static fluid, pressure increases with depth according to dP/dz = −ρg, giving the hydrostatic equation P = P₀ + ρgh for an incompressible fluid. Pascal's law states that a pressure change applied at one point is transmitted undiminished throughout a static fluid. Pressure is isotropic — it acts equally in all directions at a point — and is measured as absolute or gauge pressure relative to atmospheric.

## How It's Best Learned
Derive the pressure-depth relationship from a free-body diagram of a fluid element. Practice computing pressures at various depths in tanks with multiple fluid layers. Use U-tube problems to build physical intuition before formalizing with the hydrostatic equation.

## Common Misconceptions
- Pressure depends only on depth and fluid density, not on the shape or total volume of the container (the hydrostatic paradox).
- Gauge pressure is relative to atmosphere; failing to specify absolute vs. gauge leads to sign errors.
- Pressure is a scalar, not a vector, even though forces due to pressure act normal to surfaces.
