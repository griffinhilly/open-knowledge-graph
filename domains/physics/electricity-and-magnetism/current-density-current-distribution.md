---
id: current-density-current-distribution
title: Current Density and Current Distribution
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-and-resistance
  type: hard
builds-toward:
- joule-heating-resistive-power
tags:
- currents
- vector field
- charge flow
stage: formal-systems
status: draft
---

# Current Density and Current Distribution

## Core Idea
Current density J is the current per unit area perpendicular to flow: J = I/A. As a vector field, J = nqv where n is charge carrier density, q is charge per carrier, and v is drift velocity. The continuity equation ∂ρ/∂t + ∇·J = 0 expresses charge conservation. Integrating J over a surface gives total current through that surface.

## How It's Best Learned
Derive the continuity equation from charge conservation. Calculate current density in wires of uniform and varying cross-section.

## Common Misconceptions
- Current and current density have the same units (amperes vs amperes per square meter).
- J direction equals charge carrier motion for all carriers (electrons move opposite to J).
- Current density is always uniform in a conductor (it varies when cross-section or resistivity varies).

## Explainer

From your study of electric current and resistance, you know that current I measures the total charge flowing past a cross-section per second. But this scalar description throws away geometric information — it says nothing about *where* the charge is flowing within the conductor. **Current density** J recovers that information by describing the current per unit area at every point in space, making it a vector field rather than a single number. The direction of J at each point is the local direction of positive charge flow; the magnitude tells you how densely the current is packed at that location.

The relation J = nqv_d builds from microscopic ingredients you can picture directly. In a metal wire, n is the number of free electrons per cubic meter, q = e is the elementary charge, and v_d is the **drift velocity** — the slow net motion of electrons through the random thermal jostling. Multiplying these three numbers gives the charge crossing a unit area per second, which is exactly what J measures. The subtlety for electrons is that since they carry negative charge and move opposite to the electric field, the conventional current density J points opposite to the electron drift — a sign convention you must track carefully.

The **continuity equation** ∂ρ/∂t + ∇·J = 0 is the mathematical expression of charge conservation. You encountered divergence when working with Gauss's law: ∇·J measures the net outward current per unit volume at a point. If this is positive, charge is flowing out of that region faster than it flows in, so the local charge density ρ must be decreasing. The equation simply says: whatever leaves as current must reduce the local charge. In steady state (no charge accumulation), ∂ρ/∂t = 0, so ∇·J = 0 everywhere — current flows in closed loops, consistent with Kirchhoff's current law, which is the lumped-circuit version of this same conservation principle.

The most practical consequence of the vectorial description is understanding non-uniform current distribution. When a wire narrows, the same total current I must pass through a smaller area A, so J = I/A increases. The local electric field driving the current — given by **Ohm's law in point form** J = σE, where σ is the conductivity — must also increase, meaning the narrow region has a larger voltage gradient. This is why thin wires heat up more than thick ones carrying the same current: the higher J leads to greater power dissipation per unit volume via P/V = J·E = J²/σ. Integrating J over any cross-sectional surface recovers the total current I, connecting the field picture back to the circuit quantities you already know.
