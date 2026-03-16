---
id: hydrostatic-force-vertical-surfaces
title: Hydrostatic Force on Vertical Submerged Surfaces
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-statics-pressure
  type: hard
builds-toward:
- hydrostatic-force-horizontal-submerged-surface
- floating-body-stability-metacentric-height
tags:
- hydrostatics
- forces
- submerged-surfaces
- dams
stage: formal-systems
status: draft
---

# Hydrostatic Force on Vertical Submerged Surfaces

## Core Idea
The total hydrostatic force on a vertical submerged surface equals the pressure at the geometric centroid multiplied by the surface area, but the force acts at a point below the centroid called the center of pressure. This location shift is critical for structural design of dams, gates, and underwater vessels because it creates a moment that must be resisted.

## How It's Best Learned
Derive the center of pressure location using integration of pressure distribution over a submerged area. Compare results for simple shapes (rectangular gates) with complex shapes (parabolic weirs).

## Common Misconceptions
The force acts at the centroid. The total force is simply pressure at the surface times area. The center of pressure doesn't move with changing water depth.

## Explainer

From fluid statics, you know that pressure in a static fluid increases linearly with depth: p = ρgh, where h is measured downward from the free surface. When a vertical surface is submerged — a dam gate, a lock wall, a tank side panel — this increasing pressure means the force per unit area is not uniform. The bottom of the gate experiences higher pressure than the top, and you need to account for this variation to find both the total force and where it acts.

The total hydrostatic force on a vertical surface is F = p̄·A, where p̄ is the pressure at the **centroid** of the surface (its geometric center). For a rectangular gate of width w with its top edge at depth h₁ and bottom at depth h₂, the centroid is at depth h̄ = (h₁ + h₂)/2, giving F = ρg·h̄·A. This follows from integrating the pressure distribution p(h) = ρgh over the area — the integral of a linearly varying quantity equals the value at the midpoint times the total area. The result is sometimes surprising to students because it seems like you could just use the average pressure, and that is precisely correct — but average pressure means pressure at the centroid, not at the midpoint between the surface and the free surface.

The crucial subtlety is where the resultant force acts. Because pressure increases with depth, the lower portion of the surface carries more force per unit area than the upper portion, and the resultant must act below the centroid. This location, called the **center of pressure** y_cp, is found by computing the moment of the pressure distribution about a reference axis: y_cp = ȳ + I_c/(ȳ·A), where ȳ is the centroid depth measured along the surface and I_c is the second moment of area of the surface shape about its own centroidal axis. For a rectangle of height d and width w, I_c = wd³/12. The term I_c/(ȳ·A) is always positive, confirming that the center of pressure is always below the centroid.

This shift in force location has direct structural consequences. Consider a dam gate hinged at its midpoint — the moment the hydrostatic force creates about the hinge depends on where the force acts, not just its magnitude. A designer who places the resultant at the centroid will underestimate the overturning moment and undersize the hinge or support structure. As water depth increases, ȳ grows while I_c/(ȳ·A) shrinks, so the center of pressure migrates toward the centroid but never reaches it for a fully submerged surface. For a rectangular gate with its top edge at the free surface, the center of pressure is always at two-thirds of the total gate height from the top — a result worth remembering for quick structural checks.
