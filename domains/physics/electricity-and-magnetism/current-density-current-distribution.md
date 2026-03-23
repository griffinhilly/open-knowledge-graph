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
status: validated
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

## Questions

```yaml
- question: "A wire carrying current I narrows so that its cross-sectional area halves (from A to A/2). What happens to the current density J in the narrower section?"
  type: multiple-choice
  options:
    - "J halves — less area means less current can flow"
    - "J doubles — the same current passes through half the area"
    - "J stays the same — current is conserved through the wire"
    - "J becomes undefined because the cross-section changed"
  answer: 1
  explanation: "Current I is conserved — the same charge per second must pass through every cross-section of a series conductor (Kirchhoff's current law). Since J = I/A and I is fixed, halving the area doubles the current density. This higher J also means a larger local electric field (via J = σE) and greater power dissipation per unit volume (P/V = J·E = J²/σ), which is why thin wires heat up more than thick ones carrying the same total current."

- question: "In a metal conductor, the direction of the current density vector J points:"
  type: multiple-choice
  options:
    - "In the same direction as the drift velocity of the electrons"
    - "Opposite to the drift velocity of the electrons"
    - "Perpendicular to the drift velocity of the electrons"
    - "J has no direction — it is a scalar quantity"
  answer: 1
  explanation: "J is defined as the direction of positive charge flow (conventional current direction). In a metal, the charge carriers are electrons, which carry negative charge and drift opposite to the electric field. Since conventional current flows in the direction of positive charge flow, J points opposite to the electron drift. The formula J = nqv_d accounts for this: with q = −e (negative) and v_d pointing left (say), the product gives J pointing right. Tracking signs carefully here prevents errors in all subsequent electromagnetic calculations."

- question: "If current I is conserved along a conductor, then the current density J must also be the same at every cross-section."
  type: true-false
  answer: false
  explanation: "Current I is conserved (the same total charge per second passes each cross-section), but current density J = I/A depends on the local cross-sectional area. Where the conductor is narrow, J is large; where it is wide, J is small. This is why current density is a more informative quantity than current alone — it captures the spatial distribution of charge flow and directly governs local effects like heating (P/V = J²/σ) and the driving electric field (J = σE)."

- question: "The continuity equation ∂ρ/∂t + ∇·J = 0 is a mathematical expression of the conservation of electric charge."
  type: true-false
  answer: true
  explanation: "The continuity equation states that any net outflow of current from a region (∇·J > 0) must be accompanied by a decrease in the local charge density (∂ρ/∂t < 0), and vice versa. Charge is neither created nor destroyed — it can only move. In steady-state circuits where charge density doesn't change (∂ρ/∂t = 0), this reduces to ∇·J = 0: as much current enters any volume as leaves it. This is the field-theoretic version of Kirchhoff's current law."

- question: "Explain why current density J, rather than current I, is the more fundamental quantity for describing how current flows through a conductor with varying cross-sectional area."
  type: short-answer
  answer: "I is a scalar giving total charge flow per second through a cross-section, but it says nothing about how that flow is distributed spatially. J is a vector field that captures the local magnitude and direction of current at every point. In a conductor with varying cross-section, I is conserved but J varies inversely with area. J connects directly to local physical effects: J = σE relates current density to the local electric field; P/V = J²/σ gives local heating. I can be recovered from J by surface integration, making J the more complete and fundamental description."
  explanation: "The distinction between I and J mirrors the distinction between total flux and flux density in other areas of physics. Knowing total water flow in a pipe doesn't tell you the local flow speed; that requires dividing by local cross-sectional area. Similarly, J = I/A (for uniform cross-sections) gives the local intensity of charge flow. In inhomogeneous conductors or complex geometries, only J fully describes what's happening — I alone cannot distinguish a thin, hot wire from a thick, cool one carrying the same total current."
```

## Explainer

From your study of electric current and resistance, you know that current I measures the total charge flowing past a cross-section per second. But this scalar description throws away geometric information — it says nothing about *where* the charge is flowing within the conductor. **Current density** J recovers that information by describing the current per unit area at every point in space, making it a vector field rather than a single number. The direction of J at each point is the local direction of positive charge flow; the magnitude tells you how densely the current is packed at that location.

The relation J = nqv_d builds from microscopic ingredients you can picture directly. In a metal wire, n is the number of free electrons per cubic meter, q = e is the elementary charge, and v_d is the **drift velocity** — the slow net motion of electrons through the random thermal jostling. Multiplying these three numbers gives the charge crossing a unit area per second, which is exactly what J measures. The subtlety for electrons is that since they carry negative charge and move opposite to the electric field, the conventional current density J points opposite to the electron drift — a sign convention you must track carefully.

The **continuity equation** ∂ρ/∂t + ∇·J = 0 is the mathematical expression of charge conservation. You encountered divergence when working with Gauss's law: ∇·J measures the net outward current per unit volume at a point. If this is positive, charge is flowing out of that region faster than it flows in, so the local charge density ρ must be decreasing. The equation simply says: whatever leaves as current must reduce the local charge. In steady state (no charge accumulation), ∂ρ/∂t = 0, so ∇·J = 0 everywhere — current flows in closed loops, consistent with Kirchhoff's current law, which is the lumped-circuit version of this same conservation principle.

The most practical consequence of the vectorial description is understanding non-uniform current distribution. When a wire narrows, the same total current I must pass through a smaller area A, so J = I/A increases. The local electric field driving the current — given by **Ohm's law in point form** J = σE, where σ is the conductivity — must also increase, meaning the narrow region has a larger voltage gradient. This is why thin wires heat up more than thick ones carrying the same current: the higher J leads to greater power dissipation per unit volume via P/V = J·E = J²/σ. Integrating J over any cross-sectional surface recovers the total current I, connecting the field picture back to the circuit quantities you already know.
