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
stage: advanced
status: draft
---

# Poynting Theorem and Energy Conservation

## Core Idea
The Poynting theorem ∂u/∂t + ∇·S = -J·E expresses conservation of electromagnetic energy: the sum of field energy change, energy flow out, and work done on charges equals zero. This is a fundamental conservation law following from Maxwell's equations.

## Explainer

You already know that electromagnetic fields carry energy — the energy density stored in electric and magnetic fields is u = ½ε₀E² + B²/(2μ₀). The Poynting theorem answers the next natural question: how does this energy move and transform? The starting point is the work done per unit volume on charges: J·E (current density dot electric field). This is the rate at which field energy is converted into mechanical or thermal energy in matter. The theorem derives an accounting identity directly from Maxwell's equations for where that energy comes from.

Taking E·(Ampère-Maxwell equation) − B·(Faraday equation) and rearranging using the vector identity ∇·(E×B) = B·(∇×E) − E·(∇×B), you obtain: −J·E = ∂u/∂t + ∇·S, where **S = (1/μ₀)(E×B)** is the **Poynting vector**. This can be rewritten as ∂u/∂t + ∇·S = −J·E. Read term by term: ∂u/∂t is the rate of change of field energy density; ∇·S is the divergence of the energy flux (positive divergence means energy is flowing outward); J·E is the power delivered to charges per unit volume. The equation says: rate of field energy decrease = energy flowing out + energy delivered to matter. This is energy conservation, local and exact.

Integrating over a volume V and applying the divergence theorem transforms ∫∇·S dV into a surface integral ∮S·dA. This gives: d/dt(field energy in V) = −∮S·dA − ∫J·E dV. The surface integral is the net power flowing out through the bounding surface. The **Poynting vector S** therefore represents the directional flow of electromagnetic power per unit area, in watts per square meter — it points in the direction energy is traveling, like a current of electromagnetic energy through space.

An instructive example: consider a resistor connected to a battery. You might expect the energy to flow along the wire — but the Poynting vector tells a different story. Outside the resistor, E points from the battery terminal, B curls around the current-carrying wire, and E×B points radially inward toward the wire's axis. The electromagnetic energy actually flows from the surrounding space into the resistor, not along the wire itself. The wire guides the fields; the fields carry the energy. This picture, deeply counterintuitive but correct, reveals that power transmission in circuits is fundamentally an electromagnetic phenomenon occurring in the fields surrounding the conductors, not a flow of kinetic energy of charges in the wire.
