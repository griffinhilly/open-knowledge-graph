---
id: hydrostatic-pressure-distribution
title: Hydrostatic Pressure Distribution
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pressure-and-forces-in-fluids
  type: hard
- id: fluid-properties-and-continuum
  type: soft
builds-toward:
- forces-on-submerged-surfaces
- floating-body-stability-equilibrium
tags:
- statics
- pressure
- hydrostatics
stage: advanced
status: draft
---

# Hydrostatic Pressure Distribution

## Core Idea
In a static fluid, pressure varies linearly with depth: P = P₀ + ρgh, where ρ is fluid density, g is gravitational acceleration, and h is depth. This hydrostatic pressure distribution results from the weight of fluid above and acts perpendicular to any surface. The distribution is independent of the shape of the container and depends only on the fluid density and vertical height difference.

## How It's Best Learned
Measure water pressure at different depths in a column using pressure gauges or manometers. Observe that pressure increase per unit depth is the same regardless of container shape, demonstrating the principle that pressure depends only on vertical height.

## Common Misconceptions
- Pressure at a depth depends on the shape or total volume of the container (pressure depends only on depth, not on container shape).
- Pressure in a fluid only acts downward (pressure acts in all directions equally).
- Different fluids at the same depth have the same pressure (pressure depends on fluid density; heavier fluids have higher pressure at the same depth).

## Explainer

You already know that pressure is force per unit area, and that in a static fluid, pressure at a point is isotropic — it acts equally in all directions. This follows from Pascal's principle: if it didn't, a tiny fluid element would accelerate in the direction of the pressure imbalance, and the fluid wouldn't be static. The question then is: how does pressure change from point to point in a motionless fluid? The answer follows from a simple force balance on a column of fluid.

Imagine isolating a thin horizontal slab of fluid at depth h below the surface. The fluid above it exerts a downward pressure, and the fluid below exerts an upward pressure. For the slab to remain stationary, the pressure difference between top and bottom must exactly support the weight of the slab. Working this out gives dP/dh = ρg — pressure increases linearly with depth in an incompressible fluid of uniform density. Integrating from the surface gives **P = P₀ + ρgh**, where P₀ is the pressure at the free surface (usually atmospheric), ρ is the fluid density, g is gravitational acceleration, and h is the vertical depth below the surface. Three numbers — density, gravity, and depth — determine everything.

The most surprising implication is the **hydrostatic paradox**: pressure at a given depth is completely independent of the container's shape or total volume of fluid above. A 1-centimeter-diameter pipe filled with water to 10 meters produces the same pressure at the bottom as an Olympic swimming pool of the same depth. This seems counterintuitive — the swimming pool has vastly more water pressing down — but the sidewalls of the wider container support the excess weight. Pressure depends only on the vertical height of fluid, not on how much total fluid is present. This is why manometers can measure pressure using only a small U-shaped tube: the height difference in the fluid column directly encodes the pressure difference.

The omnidirectional nature of pressure means it acts perpendicular to any surface it contacts, regardless of that surface's orientation. A horizontal floor at depth h experiences pressure P₀ + ρgh pushing upward; a vertical wall at that same depth experiences the same pressure pushing horizontally. This matters enormously for engineering design: the net hydrostatic force on a dam wall, for example, must be computed by integrating the linearly varying pressure distribution over the entire submerged face — a calculation that builds directly on the linear P(h) relationship established here.
