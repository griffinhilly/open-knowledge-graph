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
- id: hydrostatic-force-horizontal-submerged-surface
  type: soft
builds-toward:
- control-volume-momentum
tags:
- hydrostatic force
- center of pressure
- plane surfaces
- curved surfaces
stage: formal-systems
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

## Questions

```yaml
- question: "A rectangular gate has its centroid at depth ȳ = 4 m below the free surface. The hydrostatic resultant force equals ρg × 4 m × A. At what depth does this resultant force actually act?"
  type: multiple-choice
  options:
    - "At exactly 4 m depth — the force acts at the centroid"
    - "At a depth greater than 4 m — the center of pressure lies below the centroid"
    - "At a depth less than 4 m — the lower pressure near the top shifts the action point upward"
    - "At the free surface, because that is where the pressure gradient originates"
  answer: 1
  explanation: "The magnitude formula F = ρg·ȳ·A uses the centroid depth to compute the force, but the resultant acts at the center of pressure, which is always below the centroid. The offset is I_c/(ȳ·A), where I_c is the second moment of area about the centroidal axis. The deeper parts of the gate experience higher pressure, biasing the net moment toward the deep end. Using the centroid depth for magnitude is a shortcut that works because pressure varies linearly and the centroid is the area-weighted mean; it does not mean the force acts there."

- question: "A submerged gate is initially at shallow depth (ȳ = 2 m). It is then lowered to ȳ = 20 m, with area and orientation unchanged. How does the location of the center of pressure change relative to the centroid?"
  type: multiple-choice
  options:
    - "The offset grows larger because higher absolute pressure increases the moment imbalance"
    - "The offset shrinks because at great depth, pressure variation across the gate is small compared to the mean pressure, so the load is nearly uniform"
    - "The center of pressure moves above the centroid at great depth"
    - "The offset remains constant because I_c and A are unchanged"
  answer: 1
  explanation: "The offset of the center of pressure below the centroid is I_c/(ȳ·A). As ȳ increases with I_c and A fixed, the offset decreases. Physically: at shallow depth, pressure changes significantly from top to bottom of the gate (relative to the mean pressure), strongly biasing the moment. At great depth, the same absolute pressure change across the gate is a tiny fraction of the mean pressure, so the loading is nearly uniform — and a nearly uniform load acts at its centroid. The center of pressure converges toward the centroid as depth increases."

- question: "The resultant hydrostatic force on a submerged flat surface acts at the centroid of the surface."
  type: true-false
  answer: false
  explanation: "The resultant acts at the center of pressure, which lies below the centroid (for any surface that is not under perfectly uniform pressure, i.e., any surface with finite vertical extent). The centroid depth is used only to compute the magnitude of the resultant force, not its point of application. Applying the force at the centroid rather than the center of pressure would give the wrong moment — a critical error in designing gates, dams, and retaining walls where the moment arm determines structural loads."

- question: "For a curved submerged surface, the horizontal component of the hydrostatic resultant equals the hydrostatic force on the vertical projection of that curved surface."
  type: true-false
  answer: true
  explanation: "Because pressure is a scalar acting normal to the surface, integrating pressure vectors over a curved surface requires decomposition. Horizontal equilibrium on the fluid volume bounded by the curved surface and a vertical projection plane shows that the net horizontal force on the curve must equal the force on its vertical projection — a flat vertical plate at the same depth. This projected-area approach lets you use the familiar plane-surface formula (F = ρg·ȳ·A_projected) for the horizontal component without doing a curved surface integral."

- question: "Explain physically why the center of pressure on a submerged inclined plane lies below the centroid, and describe what happens to this offset as the surface is submerged to greater and greater depth."
  type: short-answer
  answer: "Hydrostatic pressure increases linearly with depth, so deeper parts of a submerged surface experience greater pressure than shallower parts. The pressure distribution is non-uniform: the load per unit area is larger at the bottom than at the top. When computing the moment of this distributed load about the centroid axis, the high-pressure deep region contributes a larger moment than the low-pressure shallow region, pulling the effective point of action (center of pressure) downward, below the centroid. As depth increases, the mean pressure ρg·ȳ grows large relative to the pressure variation across the surface (which depends only on surface height, not ȳ). The variation becomes an increasingly small fraction of the mean, making the load nearly uniform — and a uniform load acts at the centroid. The offset I_c/(ȳ·A) therefore shrinks toward zero as ȳ increases."
  explanation: "This depth-dependence has an important engineering implication: deep submerged gates and hull sections can be analyzed with less concern about center-of-pressure offset than shallow ones, where the pressure gradient across the surface is a large fraction of the mean pressure."
```

## Explainer

From your prerequisite on fluid statics, you know that pressure in a static fluid increases linearly with depth: p = ρgh. That simple fact becomes non-trivial the moment you ask: "What is the net force on a surface submerged in that fluid, and where does it act?" The pressure is not uniform across the surface — it is larger at greater depths — so the force is the integral of a varying load, not just pressure times area. This topic gives you the systematic tools to evaluate that integral for both flat and curved surfaces.

For a **flat (plane) submerged surface**, the total resultant force turns out to be elegantly simple: F = ρg·ȳ·A, where ȳ is the depth of the **centroid** of the surface. In other words, you can compute the magnitude as if the entire area were sitting at the average depth — the centroid depth. This works because pressure is linear with depth, and the centroid is by definition the area-weighted average position. However, a linearly varying load does not act at its average position — it acts closer to the high-pressure end. That is why the **center of pressure** y_cp lies below the centroid. The offset is I_c/(ȳ·A), where I_c is the second moment of area about the centroidal axis. You already know how to calculate I_c for rectangles, circles, and composite areas — that geometry prerequisite is exactly what you need here.

Here is the physical intuition for why the center of pressure is below the centroid: deeper regions of the surface experience higher pressure, so they contribute more to the total moment than their area alone would suggest. The net moment is biased toward the deep end, pulling the effective application point downward. As the surface is submerged deeper (ȳ increases while A and I_c remain constant), the offset I_c/(ȳ·A) shrinks — at very great depth, pressure variation across the surface becomes negligible relative to the mean pressure, and the center of pressure approaches the centroid.

**Curved surfaces** require a different approach because pressure always acts normal to the surface, and the direction of "normal" varies continuously along a curve. You cannot add these vectors directly by scalar integration. Instead, decompose the force into a **horizontal component** F_H and a **vertical component** F_V. The horizontal component equals the hydrostatic force on the vertical projected area of the curved surface — treat the projection as a flat vertical plate and use the plane-surface formula. The vertical component equals the weight of the fluid column directly above the curved surface, up to the free surface. If the curved surface is concave upward (like the bottom of a tank), this fluid column is a real weight pushing down. If the surface is convex upward (like the top of a submerged dome), the vertical force is the weight of the imaginary fluid column that *would* sit above it — and it acts upward, which is precisely the buoyancy concept you already know from Archimedes' principle. The resultant force is then √(F_H² + F_V²) acting at the appropriate angle, located by taking moments of the two components separately.
