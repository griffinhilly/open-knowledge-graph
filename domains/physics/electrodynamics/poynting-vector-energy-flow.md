---
id: poynting-vector-energy-flow
title: Poynting Vector and Electromagnetic Energy Flow
domain: physics
course: electrodynamics
prerequisites:
- id: plane-electromagnetic-waves
  type: hard
- id: energy-stored-in-fields
  type: soft
builds-toward:
- radiation-pressure
- maxwell-stress-tensor
tags:
- poynting-vector
- energy-flow
- energy-density
stage: advanced
status: draft
---

# Poynting Vector and Electromagnetic Energy Flow

## Core Idea
The Poynting vector S = (1/μ₀)E × B represents the directional electromagnetic energy flux, with units of power per unit area. Its magnitude gives the intensity of electromagnetic radiation, and its direction indicates energy flow. The continuity equation for electromagnetic energy, ∂u/∂t + ∇·S = -J·E, elegantly connects energy density, energy flow, and work done on charges.

## Questions

```yaml
- question: "A resistive wire carries a steady DC current. According to Poynting vector analysis, where does the electromagnetic energy actually flow to deliver power to the resistor?"
  type: multiple-choice
  options:
    - "Through the wire, carried by the conduction electrons moving along it"
    - "Radially inward from the surrounding field into the wire, where it is converted to Joule heat"
    - "Outward from the wire in all directions, dissipating into free space"
    - "Along the surface of the wire in the direction of current flow"
  answer: 1
  explanation: "In a current-carrying wire, E points along the wire (driving the current) and B circles the wire (from Ampère's law). The Poynting vector S = (1/μ₀)E × B therefore points radially inward — energy flows from the surrounding electromagnetic field into the wire, where it is deposited as Joule heat. The wire is the sink, not the channel. Option A is the intuitive but wrong answer: conduction electrons carry charge, not energy. The energy delivery is through the external field."

- question: "A plane electromagnetic wave travels in the +z direction with E pointing in the +x direction and B in the +y direction. What is the direction of the Poynting vector?"
  type: multiple-choice
  options:
    - "+x direction, along the electric field"
    - "+y direction, along the magnetic field"
    - "+z direction, along the wave propagation"
    - "Radially outward from the wave source"
  answer: 2
  explanation: "S = (1/μ₀)E × B = (1/μ₀)(x̂ × ŷ) = (1/μ₀)ẑ. The cross product of x̂ and ŷ is +ẑ, confirming that the Poynting vector points in the direction of wave propagation. This is a consistency check: electromagnetic energy must flow in the direction the wave travels. S is always perpendicular to both E and B, which is why it naturally aligns with propagation."

- question: "The Poynting theorem, ∂u/∂t + ∇·S = −J·E, expresses a local conservation law for electromagnetic energy, analogous to a continuity equation."
  type: true-false
  answer: true
  explanation: "The Poynting theorem has exactly the structure of a continuity equation: the rate of change of energy density (∂u/∂t) plus the divergence of energy flux (∇·S) equals the source/sink term (−J·E, the negative of work done on charges). If ∇·S > 0, energy is flowing out of the region. If J·E > 0, the field is doing work on charges and losing field energy. This is the electromagnetic analog of charge conservation ∂ρ/∂t + ∇·J = 0."

- question: "In a DC circuit, the electric field inside a resistive wire points radially outward from the wire's axis, which is what drives the Poynting vector inward."
  type: true-false
  answer: false
  explanation: "The electric field inside a resistive wire points along the wire in the direction of current flow (from high to low potential), not radially outward. It is this longitudinal E combined with the azimuthal B (which circles the wire per Ampère's law) that produces a cross product pointing radially inward. A radially outward E would give a Poynting vector with no inward component — it would be circumferential, not inward."

- question: "Explain why electromagnetic energy in a DC circuit flows through the empty space surrounding the wire rather than through the wire itself."
  type: short-answer
  answer: "The energy is carried by the electromagnetic field, not by the electrons. The battery establishes an electric field along the circuit and a magnetic field around the current-carrying wires. The Poynting vector S = (1/μ₀)E × B points radially inward toward the wire everywhere along its length, meaning the field delivers energy from the surrounding space into the conductor where it is dissipated as heat. The electrons inside the wire are the mechanism for completing the circuit and maintaining the fields, but the energy transport is in the external field."
  explanation: "This result, though counterintuitive, is required by the Poynting theorem. Circuit theory gives the right answer for total power (P = IV) but says nothing about where the energy travels spatially. Field theory shows the energy flows in the field region, not in the wires. This reconciles with Joule heating: the inward-flowing field energy is converted to thermal energy inside the resistor at exactly the rate P = I²R predicted by circuit analysis."
```

## Explainer

You have studied plane electromagnetic waves and the energy stored in static electric and magnetic fields. Now the question is: as an EM wave propagates, how does the energy travel with it, and how is that energy exchange with matter tracked? The **Poynting vector** S = (1/μ₀)E × B answers the first question — it is the energy flux density of the electromagnetic field, measuring how many watts of electromagnetic power flow through each square meter of area, in the direction perpendicular to both E and B. For a plane wave traveling in the +z direction with E in the x-direction and B in the y-direction, S points in the +z direction, as it must: the energy flows in the same direction as the wave.

The derivation of the Poynting theorem is an exercise in manipulating Maxwell's equations. Starting from the work done per unit volume by the fields on charges (J·E), you use Maxwell's equations to rewrite this in terms of field quantities only, arriving at: ∂u/∂t + ∇·S = −J·E. Here u = (ε₀E²/2 + B²/2μ₀) is the **electromagnetic energy density** you already know from field energy calculations. This equation is a continuity equation — a local conservation law. The rate of change of field energy density plus the divergence of energy flux equals the negative of the work done on charges. If ∇·S > 0 at a point, energy is flowing out of that region; if J·E > 0, the field is doing positive work on the charges and losing energy.

A crucial and counterintuitive application: energy in a DC circuit does not flow through the wires — it flows in the space surrounding them. In a resistive wire carrying current, E points along the wire (driving the current) and B circles the wire (from Ampère's law). The Poynting vector E × B points radially inward toward the wire — electromagnetic energy flows in from the surrounding field and is converted to Joule heat inside the conductor. The battery "pumps" energy into the external electromagnetic field, and that field delivers energy to the resistor, not through the wire but through the empty space around it. This perspective is startling but correct, and it is entirely consistent with the circuit-level energy accounting you already know.

For radiation problems — antennas, light scattering, thermal emission — S is the central quantity. The **intensity** of radiation I is the time-averaged magnitude of S, so I = ⟨|S|⟩. For a plane wave in vacuum, this gives I = E₀²/(2μ₀c). The direction of S tells you the direction of radiation propagation; its spatial variation (via ∇·S) tells you where energy is being deposited. When you study radiation pressure (which builds on this topic), you will find that electromagnetic momentum flux density is S/c², so the Poynting vector contains information not just about energy but also about momentum transfer — the mechanism by which light can push objects.
