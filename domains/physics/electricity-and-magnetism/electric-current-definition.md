---
id: electric-current-definition
title: Electric Current and Current Density
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: elementary-charge-conservation
  type: hard
- id: energy-density-electric-field
  type: soft
builds-toward:
- resistance-resistivity-temperature
- ohms-law-circuits
tags:
- current
- charge-flow
- density
stage: formal-systems
status: validated
---
# Electric Current and Current Density

## Core Idea
Electric current I is the charge per unit time flowing through a cross-section: I = dQ/dt, measured in amperes (A). Current density J = I/A is current per unit area; via continuity equation ∂ρ/∂t + ∇⋅J = 0.

## Questions

```yaml
- question: "In a metal wire, electrons are drifting to the right. What is the direction of conventional current?"
  type: multiple-choice
  options:
    - "To the right, following the electron motion"
    - "To the left, opposite to the electron motion"
    - "There is no conventional current when only electrons move"
    - "Perpendicular to the wire axis"
  answer: 1
  explanation: "Conventional current is defined as the direction positive charges would flow to produce the same effect. Since electrons carry negative charge and drift to the right, conventional current points to the left. This historical convention (established before the electron was discovered) never leads to wrong answers as long as you apply it consistently — the physics is identical either way, since a rightward negative charge flow and a leftward positive charge flow produce the same electromagnetic effects."

- question: "At a point in a conductor, ∇·J > 0. What is happening to the local charge density ρ at that point?"
  type: multiple-choice
  options:
    - "ρ is increasing — current is converging and depositing charge"
    - "ρ is decreasing — more current is leaving than arriving"
    - "ρ is zero — the conductor is charge-neutral"
    - "ρ is constant — the divergence of J doesn't affect charge density"
  answer: 1
  explanation: "The continuity equation ∂ρ/∂t + ∇·J = 0 directly links these quantities. If ∇·J > 0, more current is flowing out of the region than flowing in (net outflow). By charge conservation, this outflow must deplete the local charge, so ∂ρ/∂t = −∇·J < 0 — charge density is decreasing. Think of it as water: if more leaves a tank than enters, the level drops."

- question: "In a metal wire carrying current, the drift velocity of electrons is in the same direction as the conventional current."
  type: true-false
  answer: false
  explanation: "Electrons carry negative charge, so their drift is opposite to conventional current direction. Conventional current flows from high to low potential (positive terminal to negative terminal outside a battery), while electrons — driven by the electric field in the wire — move in the opposite direction, from low to high potential. The sign convention for current was established long before electrons were identified, and it defines current as the direction of positive charge flow."

- question: "Electric current I = dQ/dt measures the rate at which charge flows through a cross-section of a conductor."
  type: true-false
  answer: true
  explanation: "This is the definition of current: the instantaneous rate of charge transfer through a surface, measured in coulombs per second (amperes). It is a scalar — it tells you how much charge crosses the cross-section per unit time, but says nothing about where within the cross-section the charge is flowing. That spatial detail requires the current density vector J."

- question: "Why is current density J a more fundamental description of current than the current I alone, and what information does I lose that J preserves?"
  type: short-answer
  answer: "J is a vector field that describes the magnitude and direction of current flow at every point in space. I is a scalar that gives the total charge crossing a surface per second but discards all spatial detail about how that charge is distributed across the cross-section. When a conductor has a non-uniform cross-section, varying resistivity, or complicated geometry, J captures the local variation — including regions of higher or lower current density. I can always be recovered from J by integrating over a surface: I = ∬ J·dA."
  explanation: "A single wire can be described by I because the geometry is simple and current distributes uniformly. But in a complex conductor — like a semiconductor device, a plasma, or a wire that narrows — different regions carry different current densities. J = σE (Ohm's law in point form) connects the local field to the local current, which is the relationship that explains why narrow sections heat up more (higher J → higher power dissipation per volume). I alone can't give you that spatial picture."
```

## Explainer

You already know from your prerequisite on charge conservation that electric charge is a fixed quantity — it cannot be created or destroyed. Electric current is what happens when charge moves in an organized way. **Electric current** I is defined as the rate at which charge crosses a surface: I = dQ/dt. The unit is the ampere (A), which equals one coulomb per second. The sign of the current follows the direction of positive charge flow by convention — so in a metal wire, where electrons (negative) move right, conventional current points left. This historical convention can be confusing but never leads to wrong answers as long as you apply it consistently.

A single number I is sufficient to describe current in a thin wire, but in a conductor with finite cross-sectional area, charge may flow unevenly — more densely in some regions than others. **Current density** J captures this spatial detail: it is a vector field whose magnitude is current per unit area (A/m²) and whose direction is the local direction of charge flow. For a uniform wire, I = JA, where A is the cross-sectional area. More generally, I through any surface S is I = ∫∫ J⃗·dA⃗ — the flux of the current density through that surface. This is where your understanding of flux from vector calculus connects to electromagnetism.

The **continuity equation** ∂ρ/∂t + ∇⋅J = 0 is the mathematical statement of charge conservation. It says: if current is diverging away from a region (∇⋅J > 0), then the charge density in that region must be decreasing (∂ρ/∂t < 0). Think of it like the conservation of water: if more water flows out of a volume than flows in, the water level inside must drop. In steady-state circuits, ∂ρ/∂t = 0 everywhere, so ∇⋅J = 0 — as much current enters any node as leaves it. This is Kirchhoff's current law expressed as a field equation.

Current and current density are the gateway to everything that follows in circuit theory and electromagnetism. Resistance and resistivity connect J to the driving electric field; Ampère's law connects I to the magnetic field it generates; and the continuity equation underlies every conservation argument in circuit analysis. Developing the habit of distinguishing I (a scalar, associated with a wire or path) from J (a vector field, associated with a region of space) will prevent category errors in virtually every subsequent topic.
