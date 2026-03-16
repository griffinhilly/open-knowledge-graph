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

## Explainer

You have studied plane electromagnetic waves and the energy stored in static electric and magnetic fields. Now the question is: as an EM wave propagates, how does the energy travel with it, and how is that energy exchange with matter tracked? The **Poynting vector** S = (1/μ₀)E × B answers the first question — it is the energy flux density of the electromagnetic field, measuring how many watts of electromagnetic power flow through each square meter of area, in the direction perpendicular to both E and B. For a plane wave traveling in the +z direction with E in the x-direction and B in the y-direction, S points in the +z direction, as it must: the energy flows in the same direction as the wave.

The derivation of the Poynting theorem is an exercise in manipulating Maxwell's equations. Starting from the work done per unit volume by the fields on charges (J·E), you use Maxwell's equations to rewrite this in terms of field quantities only, arriving at: ∂u/∂t + ∇·S = −J·E. Here u = (ε₀E²/2 + B²/2μ₀) is the **electromagnetic energy density** you already know from field energy calculations. This equation is a continuity equation — a local conservation law. The rate of change of field energy density plus the divergence of energy flux equals the negative of the work done on charges. If ∇·S > 0 at a point, energy is flowing out of that region; if J·E > 0, the field is doing positive work on the charges and losing energy.

A crucial and counterintuitive application: energy in a DC circuit does not flow through the wires — it flows in the space surrounding them. In a resistive wire carrying current, E points along the wire (driving the current) and B circles the wire (from Ampère's law). The Poynting vector E × B points radially inward toward the wire — electromagnetic energy flows in from the surrounding field and is converted to Joule heat inside the conductor. The battery "pumps" energy into the external electromagnetic field, and that field delivers energy to the resistor, not through the wire but through the empty space around it. This perspective is startling but correct, and it is entirely consistent with the circuit-level energy accounting you already know.

For radiation problems — antennas, light scattering, thermal emission — S is the central quantity. The **intensity** of radiation I is the time-averaged magnitude of S, so I = ⟨|S|⟩. For a plane wave in vacuum, this gives I = E₀²/(2μ₀c). The direction of S tells you the direction of radiation propagation; its spatial variation (via ∇·S) tells you where energy is being deposited. When you study radiation pressure (which builds on this topic), you will find that electromagnetic momentum flux density is S/c², so the Poynting vector contains information not just about energy but also about momentum transfer — the mechanism by which light can push objects.
