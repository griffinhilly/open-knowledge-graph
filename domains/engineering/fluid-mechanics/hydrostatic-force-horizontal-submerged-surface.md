---
id: hydrostatic-force-horizontal-submerged-surface
title: Hydrostatic Force on Horizontal Submerged Surfaces
domain: engineering
course: fluid-mechanics
prerequisites:
- id: hydrostatic-force-vertical-surfaces
  type: hard
builds-toward:
- floating-body-stability-metacentric-height
tags:
- hydrostatics
- forces
- horizontal-surfaces
- tanks
stage: formal-systems
status: draft
---

# Hydrostatic Force on Horizontal Submerged Surfaces

## Core Idea
For horizontal submerged surfaces, the hydrostatic force is uniform across the surface because pressure is constant at a given depth. The total force equals the pressure at that depth times the total area, and the force acts perpendicular to the surface at the geometric centroid. This simplification makes calculations for tank bottoms and horizontal components straightforward.

## Explainer

From your study of hydrostatic force on vertical surfaces, you know that pressure increases with depth as P = ρgh, and that the pressure at any point depends only on the vertical distance from the free surface — not on horizontal position. This depth-only rule is the key insight that makes horizontal surfaces special: every point on a horizontal surface lies at exactly the same depth, so every point is under exactly the same pressure. The pressure distribution is therefore **uniform**, not trapezoidal as it is on a vertical surface.

Because the pressure is uniform, computing the total hydrostatic force on a horizontal surface is straightforward: F = P × A, where P = ρgh is the pressure at the depth h of the surface and A is the total area. There is no need to integrate a varying pressure distribution or locate a pressure centroid separately from the geometric centroid. The **center of pressure** — the point where the resultant force effectively acts — coincides exactly with the **geometric centroid** of the surface, because every part of the surface contributes equally to the force.

Consider a rectangular tank bottom at depth h. The gauge pressure there is ρgh, acting uniformly downward on the fluid above (by Newton's third law, the tank bottom pushes up on the fluid with this same intensity). The total upward force the bottom must support equals ρghA — the weight of the fluid column above it. This is just the weight of the fluid divided by the bottom area multiplied back by the area, which confirms the result is simply the weight of the overlying fluid. This correspondence between the hydrostatic force calculation and the weight of the fluid column above is a useful sanity check: for a horizontal surface, the force always equals the weight of the fluid directly overhead.

The contrast with inclined and vertical surfaces is instructive. Vertical surfaces require integrating pressure over a varying depth, locating the pressure centroid below the geometric centroid, and accounting for the moment arm. For horizontal surfaces, all that complexity collapses because depth is constant. When analyzing a three-dimensional submerged object — a gate, a hull panel, a pipe cap — decomposing the problem into horizontal and vertical surface components lets you handle each piece with the appropriate (often simpler) formula.
