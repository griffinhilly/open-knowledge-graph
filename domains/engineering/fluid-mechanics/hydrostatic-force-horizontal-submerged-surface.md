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
stage: advanced
status: draft
---

# Hydrostatic Force on Horizontal Submerged Surfaces

## Core Idea
For horizontal submerged surfaces, the hydrostatic force is uniform across the surface because pressure is constant at a given depth. The total force equals the pressure at that depth times the total area, and the force acts perpendicular to the surface at the geometric centroid. This simplification makes calculations for tank bottoms and horizontal components straightforward.

## Questions

```yaml
- question: "A horizontal rectangular plate (2 m × 3 m) is fixed to the bottom of a tank at a depth of 5 m. Where does the resultant hydrostatic force act on this plate?"
  type: multiple-choice
  options:
    - "Below the geometric centroid, shifted toward the deeper edge of the plate"
    - "At the geometric centroid of the plate, because the pressure is uniform across the surface"
    - "At the geometric centroid only if the plate is perfectly level; any tilt shifts the center of pressure"
    - "At the center of pressure, which is located below the centroid by an amount dependent on depth"
  answer: 1
  explanation: "Because the plate is horizontal, every point is at the same depth (5 m), so the pressure is uniform across the entire surface. A uniform pressure distribution has its resultant acting at the geometric centroid — the center of area. There is no centroid-to-centroid offset as occurs with vertical surfaces. Option D describes the behavior of inclined or vertical surfaces, where pressure increases with depth across the surface, shifting the center of pressure below the centroid."

- question: "A vertical flat gate (1 m × 1 m) and a horizontal flat plate of the same dimensions are both submerged so their centroids are at depth 4 m. Which surface has the larger total hydrostatic force?"
  type: multiple-choice
  options:
    - "The vertical gate, because pressure increases over its depth, creating a larger average pressure"
    - "The horizontal plate, because uniform pressure acts over the entire area simultaneously"
    - "Both surfaces experience the same total force, since both centroids are at the same depth"
    - "The vertical gate, because the center of pressure is shifted deeper, amplifying the moment"
  answer: 2
  explanation: "Total hydrostatic force depends on the average pressure times the area: F = P̄ × A. The average pressure equals ρg × (depth of centroid) regardless of orientation. Since both surfaces have the same area and the same centroid depth (4 m), they have identical average pressure and therefore the same total force. The difference between vertical and horizontal surfaces is NOT the magnitude of total force (which depends only on centroid depth and area) but rather where the force acts — vertical surfaces have the center of pressure below the centroid, horizontal surfaces do not."

- question: "For a horizontal submerged surface, the center of pressure always coincides with the geometric centroid of the surface, regardless of depth."
  type: true-false
  answer: true
  explanation: "Because every point on a horizontal surface lies at the same depth, the pressure is perfectly uniform. A uniform distribution has no differential moment — no region contributes more pressure-force than another — so the resultant acts at the geometric center of the area. Depth affects the magnitude of the force (deeper → higher pressure → larger force) but not the location of the resultant, which always remains at the centroid. This is the key simplification that distinguishes horizontal from vertical surfaces."

- question: "A horizontal plate at a greater depth has its center of pressure shifted further below the geometric centroid compared to a shallower horizontal plate."
  type: true-false
  answer: false
  explanation: "For horizontal surfaces, the center of pressure is always at the geometric centroid regardless of depth. Depth increases the magnitude of the uniform pressure (more force), but pressure remains uniform across the surface, so there is no differential loading that would shift the center of pressure. The 'shift below centroid' behavior occurs on vertical and inclined surfaces, where pressure varies across the depth of the surface, creating an asymmetric distribution. Confusing the two geometries is the most common error in hydrostatics problems."

- question: "Why does the calculation of hydrostatic force on a horizontal surface simplify to F = ρghA, while a vertical surface requires integration? Explain the physical reason for this difference."
  type: short-answer
  answer: "The key is whether pressure varies across the surface. Hydrostatic pressure depends only on depth: P = ρgh. On a horizontal surface, every point lies at the same depth h, so pressure is the same everywhere — uniform. A uniform pressure times the area gives the total force directly: F = ρghA, no integration needed. On a vertical surface, depth increases from top to bottom, so pressure increases continuously from top to bottom. The force must be computed by integrating ρgy over the area, and the resulting non-uniform distribution shifts the center of pressure below the centroid. The horizontal case is special because depth is constant, collapsing the integral to a simple product."
  explanation: "This question targets the core physical insight: the simplification arises from the geometry (constant depth = constant pressure), not from any special properties of the material or the force itself. Students who understand this can correctly categorize any surface as needing integration (varying depth) or not (constant depth), which is the essential skill for fluid statics problems involving complex submerged shapes."
```

## Explainer

From your study of hydrostatic force on vertical surfaces, you know that pressure increases with depth as P = ρgh, and that the pressure at any point depends only on the vertical distance from the free surface — not on horizontal position. This depth-only rule is the key insight that makes horizontal surfaces special: every point on a horizontal surface lies at exactly the same depth, so every point is under exactly the same pressure. The pressure distribution is therefore **uniform**, not trapezoidal as it is on a vertical surface.

Because the pressure is uniform, computing the total hydrostatic force on a horizontal surface is straightforward: F = P × A, where P = ρgh is the pressure at the depth h of the surface and A is the total area. There is no need to integrate a varying pressure distribution or locate a pressure centroid separately from the geometric centroid. The **center of pressure** — the point where the resultant force effectively acts — coincides exactly with the **geometric centroid** of the surface, because every part of the surface contributes equally to the force.

Consider a rectangular tank bottom at depth h. The gauge pressure there is ρgh, acting uniformly downward on the fluid above (by Newton's third law, the tank bottom pushes up on the fluid with this same intensity). The total upward force the bottom must support equals ρghA — the weight of the fluid column above it. This is just the weight of the fluid divided by the bottom area multiplied back by the area, which confirms the result is simply the weight of the overlying fluid. This correspondence between the hydrostatic force calculation and the weight of the fluid column above is a useful sanity check: for a horizontal surface, the force always equals the weight of the fluid directly overhead.

The contrast with inclined and vertical surfaces is instructive. Vertical surfaces require integrating pressure over a varying depth, locating the pressure centroid below the geometric centroid, and accounting for the moment arm. For horizontal surfaces, all that complexity collapses because depth is constant. When analyzing a three-dimensional submerged object — a gate, a hull panel, a pipe cap — decomposing the problem into horizontal and vertical surface components lets you handle each piece with the appropriate (often simpler) formula.
