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
status: validated
---

# Hydrostatic Force on Vertical Submerged Surfaces

## Core Idea
The total hydrostatic force on a vertical submerged surface equals the pressure at the geometric centroid multiplied by the surface area, but the force acts at a point below the centroid called the center of pressure. This location shift is critical for structural design of dams, gates, and underwater vessels because it creates a moment that must be resisted.

## How It's Best Learned
Derive the center of pressure location using integration of pressure distribution over a submerged area. Compare results for simple shapes (rectangular gates) with complex shapes (parabolic weirs).

## Common Misconceptions
The force acts at the centroid. The total force is simply pressure at the surface times area. The center of pressure doesn't move with changing water depth.

## Questions

```yaml
- question: "A rectangular gate 2 m tall and 1 m wide is submerged vertically with its top edge exactly at the water surface. Where does the resultant hydrostatic force act on the gate?"
  type: multiple-choice
  options:
    - "At the centroid of the gate — 1 m from the top"
    - "At the water surface, since that is where pressure acts first"
    - "At 4/3 m from the top (2/3 of the gate height from the top)"
    - "At the bottom of the gate, since that is where pressure is highest"
  answer: 2
  explanation: "For a rectangular gate with its top at the free surface, the center of pressure is located at 2/3 of the total gate height from the top — here, 2/3 × 2 m = 4/3 m from the top. This follows from y_cp = ȳ + I_c/(ȳ·A): with top at surface, ȳ = 1 m (centroid depth), I_c = wd³/12 = (1)(2³)/12 = 2/3 m⁴, A = 2 m², so the shift is (2/3)/(1×2) = 1/3 m below the centroid, placing the center of pressure at 1 + 1/3 = 4/3 m from the top. The force acts below the centroid because deeper portions carry more pressure."

- question: "A dam engineer computes the total hydrostatic force on a vertical gate correctly using F = ρg·h̄·A but then assumes the force acts at the centroid to determine the moment on the gate hinge. What error will result?"
  type: multiple-choice
  options:
    - "The engineer will overestimate the moment, leading to an over-designed (but safe) hinge"
    - "The engineer will underestimate the overturning moment, potentially under-designing the structural support"
    - "No error — for practical engineering purposes, the centroid and center of pressure are close enough to treat as equivalent"
    - "The engineer will compute the wrong total force, not just the wrong moment"
  answer: 1
  explanation: "The center of pressure is always below the centroid, so the force arm from any reference point near the gate top is larger than the centroid location implies. Placing the force at the centroid underestimates the moment arm and therefore underestimates the overturning moment the hinge must resist. This is a potentially dangerous unconservative error: the hinge or structural support would be under-designed for the actual load. The center of pressure can be significantly below the centroid for tall gates with their top near the surface."

- question: "The total hydrostatic force on a vertical submerged surface equals the pressure at the geometric centroid of the surface multiplied by the surface area."
  type: true-false
  answer: true
  explanation: "Correct. Integrating the linearly varying pressure p(h) = ρgh over the surface area gives F = ρg·h̄·A, where h̄ is the depth of the centroid. This is equivalent to using the average pressure over the surface, and for a linearly varying distribution the average equals the value at the midpoint — the centroid. The result is sometimes surprising because students expect to need the full pressure distribution, but the integration simplifies to centroid pressure times area."

- question: "As the water depth above a submerged vertical gate increases, the center of pressure moves further below the centroid of the gate."
  type: true-false
  answer: false
  explanation: "The opposite is true. The shift below the centroid is given by I_c/(ȳ·A). As water depth above the gate increases, ȳ (the centroid depth) grows, making the denominator larger and the shift smaller. The center of pressure migrates toward the centroid as submersion depth increases, but never reaches it for a fully submerged surface. For a gate deeply submerged, the pressure variation across the gate is small relative to the mean pressure, so the resultant acts close to — but always below — the centroid."

- question: "Why does the resultant hydrostatic force on a vertical surface act below the centroid rather than at it, and why does this distinction matter for structural engineering?"
  type: short-answer
  answer: "Hydrostatic pressure increases linearly with depth (p = ρgh), so the lower portions of a vertical surface experience higher pressure per unit area than the upper portions. When the pressure distribution is integrated to find the resultant, the deeper (higher-pressure) regions contribute disproportionately more force, pulling the effective point of action downward from the geometric center. The center of pressure is located at y_cp = ȳ + I_c/(ȳA), always below the centroid by the term I_c/(ȳA). For structural design, this matters because the force creates a moment about any support point; placing the force at the wrong location underestimates that moment, potentially causing structural failure in dams, lock gates, or tank walls."
  explanation: "The key structural insight is that knowing only the magnitude of the hydrostatic force is insufficient for design — you must also know where it acts. A gate hinge, a dam buttress, or an underwater seal must be sized for the actual moment the force creates. Treating the force as acting at the centroid systematically underestimates this moment because the true location is always further from the top of the structure."
```

## Explainer

From fluid statics, you know that pressure in a static fluid increases linearly with depth: p = ρgh, where h is measured downward from the free surface. When a vertical surface is submerged — a dam gate, a lock wall, a tank side panel — this increasing pressure means the force per unit area is not uniform. The bottom of the gate experiences higher pressure than the top, and you need to account for this variation to find both the total force and where it acts.

The total hydrostatic force on a vertical surface is F = p̄·A, where p̄ is the pressure at the **centroid** of the surface (its geometric center). For a rectangular gate of width w with its top edge at depth h₁ and bottom at depth h₂, the centroid is at depth h̄ = (h₁ + h₂)/2, giving F = ρg·h̄·A. This follows from integrating the pressure distribution p(h) = ρgh over the area — the integral of a linearly varying quantity equals the value at the midpoint times the total area. The result is sometimes surprising to students because it seems like you could just use the average pressure, and that is precisely correct — but average pressure means pressure at the centroid, not at the midpoint between the surface and the free surface.

The crucial subtlety is where the resultant force acts. Because pressure increases with depth, the lower portion of the surface carries more force per unit area than the upper portion, and the resultant must act below the centroid. This location, called the **center of pressure** y_cp, is found by computing the moment of the pressure distribution about a reference axis: y_cp = ȳ + I_c/(ȳ·A), where ȳ is the centroid depth measured along the surface and I_c is the second moment of area of the surface shape about its own centroidal axis. For a rectangle of height d and width w, I_c = wd³/12. The term I_c/(ȳ·A) is always positive, confirming that the center of pressure is always below the centroid.

This shift in force location has direct structural consequences. Consider a dam gate hinged at its midpoint — the moment the hydrostatic force creates about the hinge depends on where the force acts, not just its magnitude. A designer who places the resultant at the centroid will underestimate the overturning moment and undersize the hinge or support structure. As water depth increases, ȳ grows while I_c/(ȳ·A) shrinks, so the center of pressure migrates toward the centroid but never reaches it for a fully submerged surface. For a rectangular gate with its top edge at the free surface, the center of pressure is always at two-thirds of the total gate height from the top — a result worth remembering for quick structural checks.
