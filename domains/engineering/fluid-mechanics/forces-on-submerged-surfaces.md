---
id: forces-on-submerged-surfaces
title: Forces on Submerged Surfaces
domain: engineering
course: fluid-mechanics
prerequisites:
- id: hydrostatic-pressure-distribution
  type: hard
- id: hydrostatic-force-horizontal-submerged-surface
  type: soft
builds-toward:
- floating-body-stability-equilibrium
tags:
- statics
- forces
- applications
stage: formal-systems
status: validated
---
# Forces on Submerged Surfaces

## Core Idea
The total hydrostatic force on a submerged surface equals the pressure at the centroid of the area multiplied by that area (F = P_c × A). The center of pressure, where the resultant force acts, differs from the geometric centroid and shifts with depth and orientation. These calculations are essential for designing dams, gates, and other structures retaining fluids.

## Explainer

From your study of hydrostatic pressure distribution, you know that pressure in a static fluid increases linearly with depth: P = P_0 + ρgh. Now the engineering question becomes: what is the *net force* that a body of water exerts on a flat surface like a dam face, a floodgate, or the side of a tank? The answer requires two things — the magnitude of the resultant force and where it acts — because both matter for structural design.

**Magnitude of the resultant force.** Imagine a vertical rectangular gate of area A whose centroid sits at depth h_c below the free surface. The pressure at the centroid is P_c = ρg·h_c (taking atmospheric as the gauge reference). Integrating the varying pressure over the entire surface gives a total hydrostatic force F = P_c × A. Intuitively, this says the total force equals what you would get if the *average* pressure — which happens to be the centroidal pressure for a linear distribution — acted uniformly over the entire area. This result holds for any plane surface regardless of shape or orientation, as long as h_c is measured to the centroid perpendicular to gravity.

**Center of pressure.** Here is the key insight that trips up new learners: the resultant force does not act at the centroid. Because pressure increases with depth, the lower parts of the gate experience higher force per unit area than the upper parts, so the resultant is pulled *below* the centroid. The **center of pressure** y_cp = y_c + I_c/(y_c · A), where I_c is the second moment of area of the surface about its centroidal axis and y_c is the slant depth to the centroid. The term I_c/(y_c · A) is always positive (assuming the surface is not infinitely deep), meaning the center of pressure always lies below the geometric centroid. As depth increases, this offset shrinks: deep surfaces have nearly uniform pressure distributions, so the resultant acts close to the centroid.

The engineering consequence is significant. A sluice gate pinned at its top edge must resist not just the total force F but a moment equal to F times the distance between the pin and the center of pressure. A gate designer who mistakenly places the resultant at the centroid will underestimate the overturning moment, potentially designing a pivot point or hinge that is too weak. Similarly, for a dam, the overturning moment about the toe depends on the location of the resultant — which is why the center-of-pressure calculation is always part of the stability check.

For **curved surfaces**, the approach is to resolve the hydrostatic force into horizontal and vertical components. The horizontal component equals the force on the projected vertical plane, computed as above. The vertical component equals the weight of the fluid column directly above the curved surface (real or imaginary). The resultant of these two perpendicular components gives the total force on the curved surface, directed toward the center of curvature for circular arcs — a useful property for designing curved dam faces and circular tanks.

## Questions

```yaml
- question: "A 2 m × 3 m rectangular gate is vertical with its top edge at a depth of 1 m. What is the total hydrostatic force on the gate? (ρ = 1000 kg/m³, g = 9.81 m/s²)"
  type: short-answer
  answer: "The centroid depth h_c = 1 + 1.5 = 2.5 m. F = ρg·h_c·A = 1000 × 9.81 × 2.5 × 6 = 147,150 N ≈ 147 kN."
  explanation: "The centroid of the gate is at the midpoint of its 3 m height, so 1.5 m below the top edge, giving h_c = 2.5 m. Multiplying centroidal pressure by area gives the resultant. Note that A = 2 × 3 = 6 m²."

- question: "Why does the center of pressure always lie below the centroid for a submerged surface?"
  type: short-answer
  answer: "Because hydrostatic pressure increases linearly with depth, the lower portion of the surface experiences greater pressure than the upper portion. The resultant force is therefore weighted toward the bottom of the surface, placing the center of pressure below the geometric centroid."
  explanation: "Only if pressure were uniform (infinite depth approximation) would the two points coincide. The offset I_c/(y_c·A) quantifies this shift; it decreases as depth increases because at great depth the pressure variation across the surface becomes a smaller fraction of the total pressure."
```
