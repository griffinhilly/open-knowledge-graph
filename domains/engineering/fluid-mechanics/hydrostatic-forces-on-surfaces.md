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
- id: buoyancy-and-archimedes
  type: soft
builds-toward:
- control-volume-momentum
tags:
- hydrostatic force
- center of pressure
- plane surfaces
- curved surfaces
stage: advanced
status: validated
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

## Explainer

From your prerequisite on fluid statics, you know that pressure in a static fluid increases linearly with depth: p = ρgh. That simple fact becomes non-trivial the moment you ask: "What is the net force on a surface submerged in that fluid, and where does it act?" The pressure is not uniform across the surface — it is larger at greater depths — so the force is the integral of a varying load, not just pressure times area. This topic gives you the systematic tools to evaluate that integral for both flat and curved surfaces.

For a **flat (plane) submerged surface**, the total resultant force turns out to be elegantly simple: F = ρg·ȳ·A, where ȳ is the depth of the **centroid** of the surface. In other words, you can compute the magnitude as if the entire area were sitting at the average depth — the centroid depth. This works because pressure is linear with depth, and the centroid is by definition the area-weighted average position. However, a linearly varying load does not act at its average position — it acts closer to the high-pressure end. That is why the **center of pressure** y_cp lies below the centroid. The offset is I_c/(ȳ·A), where I_c is the second moment of area about the centroidal axis. You already know how to calculate I_c for rectangles, circles, and composite areas — that geometry prerequisite is exactly what you need here.

Here is the physical intuition for why the center of pressure is below the centroid: deeper regions of the surface experience higher pressure, so they contribute more to the total moment than their area alone would suggest. The net moment is biased toward the deep end, pulling the effective application point downward. As the surface is submerged deeper (ȳ increases while A and I_c remain constant), the offset I_c/(ȳ·A) shrinks — at very great depth, pressure variation across the surface becomes negligible relative to the mean pressure, and the center of pressure approaches the centroid.

**Curved surfaces** require a different approach because pressure always acts normal to the surface, and the direction of "normal" varies continuously along a curve. You cannot add these vectors directly by scalar integration. Instead, decompose the force into a **horizontal component** F_H and a **vertical component** F_V. The horizontal component equals the hydrostatic force on the vertical projected area of the curved surface — treat the projection as a flat vertical plate and use the plane-surface formula. The vertical component equals the weight of the fluid column directly above the curved surface, up to the free surface. If the curved surface is concave upward (like the bottom of a tank), this fluid column is a real weight pushing down. If the surface is convex upward (like the top of a submerged dome), the vertical force is the weight of the imaginary fluid column that *would* sit above it — and it acts upward, which is precisely the buoyancy concept you already know from Archimedes' principle. The resultant force is then √(F_H² + F_V²) acting at the appropriate angle, located by taking moments of the two components separately.
