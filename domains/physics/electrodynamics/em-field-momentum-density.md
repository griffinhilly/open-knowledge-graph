---
id: em-field-momentum-density
title: Momentum Density in Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: em-field-energy-conservation
  type: hard
- id: poynting-vector-and-energy-flux
  type: hard
builds-toward:
- em-angular-momentum-density
- maxwell-stress-tensor-forces
tags:
- momentum-density
- radiation-pressure
- field-momentum
stage: advanced
status: draft
---

# Momentum Density in Electromagnetic Fields

## Core Idea
Electromagnetic fields carry momentum density g = S/c² = (ε₀/c²)(E × B), where S is the Poynting vector. This momentum transfers to matter in the form of radiation pressure, with magnitude equal to energy density divided by c².

## Explainer

You've already established from the Poynting vector that electromagnetic fields carry energy, with energy flux S = (1/μ₀)(E × B) measured in watts per square meter. The deeper and perhaps more surprising result is that fields also carry **momentum**. This isn't obvious classically — momentum seems like a property of matter — but it follows inescapably from the requirement that momentum be conserved when light interacts with matter.

Here's the argument: when an electromagnetic wave hits an absorbing surface and the charges in the surface begin to move, the Lorentz force F = q(E + v×B) has two parts. The electric field accelerates the charges, and then the magnetic field exerts a force on those moving charges. This secondary magnetic force is directed along the propagation direction of the wave — it pushes the surface forward. Something must be carrying that momentum before the wave is absorbed, and that something is the field itself. The **momentum density** is g = S/c² = ε₀(E × B), pointing in the same direction as the energy flow, with magnitude equal to the energy density divided by c.

The transfer of field momentum to matter is called **radiation pressure**. For a plane wave with energy density u, the radiation pressure on a perfect absorber is P = u (in SI units of N/m²), and on a perfect reflector it's P = 2u (because the momentum reverses). These are tiny forces in everyday life — the radiation pressure of sunlight on Earth is about 5 μPa — but they become significant in astrophysics (stellar winds blow material away from stars), in optical trapping (laser tweezers grip microscopic beads), and in proposed solar sail spacecraft.

The relationship g = S/c² has a profound implication: energy and momentum in electromagnetic fields are not independent, but tied by g = u/c = energy/(c·volume). This is exactly the relationship for massless particles, and it foreshadows the photon picture in quantum mechanics — photons carry energy E = hf and momentum p = h/λ = E/c. The classical result for field momentum per unit volume matches the quantum mechanical count of photon momenta, confirming that even the classical field theory anticipates the quantum nature of light.
