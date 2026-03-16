---
id: electric-current-definition
title: Electric Current and Current Density
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: elementary-charge-conservation
  type: hard
builds-toward:
- resistance-resistivity-temperature
- ohms-law-circuits
tags:
- current
- charge-flow
- density
stage: formal-systems
status: draft
---

# Electric Current and Current Density

## Core Idea
Electric current I is the charge per unit time flowing through a cross-section: I = dQ/dt, measured in amperes (A). Current density J = I/A is current per unit area; via continuity equation ∂ρ/∂t + ∇⋅J = 0.

## Explainer

You already know from your prerequisite on charge conservation that electric charge is a fixed quantity — it cannot be created or destroyed. Electric current is what happens when charge moves in an organized way. **Electric current** I is defined as the rate at which charge crosses a surface: I = dQ/dt. The unit is the ampere (A), which equals one coulomb per second. The sign of the current follows the direction of positive charge flow by convention — so in a metal wire, where electrons (negative) move right, conventional current points left. This historical convention can be confusing but never leads to wrong answers as long as you apply it consistently.

A single number I is sufficient to describe current in a thin wire, but in a conductor with finite cross-sectional area, charge may flow unevenly — more densely in some regions than others. **Current density** J captures this spatial detail: it is a vector field whose magnitude is current per unit area (A/m²) and whose direction is the local direction of charge flow. For a uniform wire, I = JA, where A is the cross-sectional area. More generally, I through any surface S is I = ∫∫ J⃗·dA⃗ — the flux of the current density through that surface. This is where your understanding of flux from vector calculus connects to electromagnetism.

The **continuity equation** ∂ρ/∂t + ∇⋅J = 0 is the mathematical statement of charge conservation. It says: if current is diverging away from a region (∇⋅J > 0), then the charge density in that region must be decreasing (∂ρ/∂t < 0). Think of it like the conservation of water: if more water flows out of a volume than flows in, the water level inside must drop. In steady-state circuits, ∂ρ/∂t = 0 everywhere, so ∇⋅J = 0 — as much current enters any node as leaves it. This is Kirchhoff's current law expressed as a field equation.

Current and current density are the gateway to everything that follows in circuit theory and electromagnetism. Resistance and resistivity connect J to the driving electric field; Ampère's law connects I to the magnetic field it generates; and the continuity equation underlies every conservation argument in circuit analysis. Developing the habit of distinguishing I (a scalar, associated with a wire or path) from J (a vector field, associated with a region of space) will prevent category errors in virtually every subsequent topic.
