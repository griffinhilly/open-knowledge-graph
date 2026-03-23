---
id: poynting-theorem-conservation-law
title: Poynting Theorem and Energy Conservation
domain: physics
course: electrodynamics
prerequisites:
- id: em-field-energy-conservation
  type: hard
- id: maxwell-equations-differential-form
  type: hard
builds-toward:
- maxwell-stress-tensor-forces
tags:
- energy-conservation
- poynting-vector
- power-flow
stage: expert
status: draft
---

# Poynting Theorem and Energy Conservation

## Core Idea
The Poynting theorem ∂u/∂t + ∇·S = -J·E expresses conservation of electromagnetic energy: the sum of field energy change, energy flow out, and work done on charges equals zero. This is a fundamental conservation law following from Maxwell's equations.

## Questions

```yaml
- question: "A battery is connected to a resistor by copper wires. According to Poynting's theorem, how does energy actually travel from the battery to the resistor?"
  type: multiple-choice
  options:
    - "Along the wire, carried by the directed drift of conduction electrons"
    - "Through the electromagnetic fields surrounding the wire, flowing radially inward toward the resistor"
    - "Entirely within the resistor, where electrical potential energy converts to heat"
    - "Along the surface of the wire in the direction of conventional current"
  answer: 1
  explanation: "This is the most counterintuitive result of Poynting's theorem. Outside a current-carrying wire connected to a battery, the electric field E points along the wire (from high to low potential) while the magnetic field B curls around the wire. Their cross product E×B — the Poynting vector S — points radially inward, toward the wire axis. Energy flows from the surrounding space into the resistor, not along the wire itself. The wire guides the electromagnetic fields; the fields carry the energy through the space around the wire."

- question: "In the Poynting theorem ∂u/∂t + ∇·S = −J·E, what physical quantity does the term J·E represent?"
  type: multiple-choice
  options:
    - "The rate of electromagnetic energy flowing across the boundary of a volume"
    - "The rate of change of stored electromagnetic field energy density"
    - "The power delivered per unit volume to charges — the rate at which field energy converts to mechanical or thermal energy"
    - "The net electromagnetic energy stored in a bounded region"
  answer: 2
  explanation: "J·E is current density dotted with electric field, which has units of W/m³ — power per unit volume. It represents the rate at which the electromagnetic field does work on charges, converting field energy into kinetic or thermal energy in matter (e.g., Ohmic heating). The negative sign on the right side means that when J·E is positive (field doing work on matter), the field energy in the region must be decreasing or flowing outward. The other terms account for storage (∂u/∂t) and transport (∇·S)."

- question: "The Poynting vector S = (1/μ₀)(E×B) can be derived directly from Maxwell's equations using only algebra, without postulating any additional assumptions about energy."
  type: true-false
  answer: true
  explanation: "This is a crucial feature of Poynting's theorem — it is not an independent postulate but a mathematical consequence of Maxwell's equations. The derivation proceeds by taking E·(Ampère-Maxwell) − B·(Faraday), applying the vector identity ∇·(E×B) = B·(∇×E) − E·(∇×B), and rearranging. No new physics is introduced; the energy conservation law is already encoded within Maxwell's equations, and the theorem makes it explicit."

- question: "In a resistor carrying a steady current, the Poynting vector inside the resistor points in the direction of current flow."
  type: true-false
  answer: false
  explanation: "Inside a resistor with steady current, E points in the direction of current (along the wire axis) and B curls around the current. Their cross product E×B — the Poynting vector — therefore points radially inward, perpendicular to the current direction. This inward-pointing energy flux is exactly what delivers power to the resistor: electromagnetic energy flows in from the surrounding space and is converted to heat. A Poynting vector aligned with current flow would represent energy moving along the wire, which is not what happens."

- question: "Why does the Poynting vector show that electromagnetic energy flows through the space surrounding a wire rather than through the wire itself? Describe the geometry of E and B outside a current-carrying wire and what their cross product implies."
  type: short-answer
  answer: "Outside a straight wire carrying current in a circuit with a battery, two fields coexist: an electric field E pointing along the wire (from higher to lower potential, in the direction of conventional current) and a magnetic field B that circles around the wire (by Ampère's law). The Poynting vector S = (1/μ₀)(E×B) is perpendicular to both — which means it points radially inward toward the wire axis. This inward energy flux is what delivers electromagnetic energy from the fields to the wire and ultimately to the resistor. The wire is not a pipe for energy; it is a guide for the fields that carry energy through the surrounding space."
  explanation: "This result challenges the intuitive 'pipe' picture of circuits where current carries energy along the wire. In reality the conduction electrons have very little kinetic energy; almost all the energy being transferred is in the electromagnetic field configuration outside the conductor. Poynting's theorem makes this precise and quantitative: integrate the inward Poynting flux over the surface of any segment of wire or resistor and you get exactly the power being delivered to that segment."
```

## Explainer

You already know that electromagnetic fields carry energy — the energy density stored in electric and magnetic fields is u = ½ε₀E² + B²/(2μ₀). The Poynting theorem answers the next natural question: how does this energy move and transform? The starting point is the work done per unit volume on charges: J·E (current density dot electric field). This is the rate at which field energy is converted into mechanical or thermal energy in matter. The theorem derives an accounting identity directly from Maxwell's equations for where that energy comes from.

Taking E·(Ampère-Maxwell equation) − B·(Faraday equation) and rearranging using the vector identity ∇·(E×B) = B·(∇×E) − E·(∇×B), you obtain: −J·E = ∂u/∂t + ∇·S, where **S = (1/μ₀)(E×B)** is the **Poynting vector**. This can be rewritten as ∂u/∂t + ∇·S = −J·E. Read term by term: ∂u/∂t is the rate of change of field energy density; ∇·S is the divergence of the energy flux (positive divergence means energy is flowing outward); J·E is the power delivered to charges per unit volume. The equation says: rate of field energy decrease = energy flowing out + energy delivered to matter. This is energy conservation, local and exact.

Integrating over a volume V and applying the divergence theorem transforms ∫∇·S dV into a surface integral ∮S·dA. This gives: d/dt(field energy in V) = −∮S·dA − ∫J·E dV. The surface integral is the net power flowing out through the bounding surface. The **Poynting vector S** therefore represents the directional flow of electromagnetic power per unit area, in watts per square meter — it points in the direction energy is traveling, like a current of electromagnetic energy through space.

An instructive example: consider a resistor connected to a battery. You might expect the energy to flow along the wire — but the Poynting vector tells a different story. Outside the resistor, E points from the battery terminal, B curls around the current-carrying wire, and E×B points radially inward toward the wire's axis. The electromagnetic energy actually flows from the surrounding space into the resistor, not along the wire itself. The wire guides the fields; the fields carry the energy. This picture, deeply counterintuitive but correct, reveals that power transmission in circuits is fundamentally an electromagnetic phenomenon occurring in the fields surrounding the conductors, not a flow of kinetic energy of charges in the wire.
