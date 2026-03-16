---
id: conductors-in-electrostatics
title: Conductors in Electrostatic Equilibrium
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law
  type: hard
- id: electric-field
  type: hard
- id: electric-potential
  type: soft
builds-toward:
- capacitance
tags:
- conductors
- electrostatics
- shielding
- induced-charge
stage: formal-systems
status: validated
---
# Conductors in Electrostatic Equilibrium

## Core Idea
In a conductor at electrostatic equilibrium, the electric field inside the bulk material is exactly zero; any excess charge resides entirely on the surface. Consequently, the interior is an equipotential region, and the field just outside the surface is perpendicular to it with magnitude σ/ε₀, where σ is the local surface charge density. These properties follow directly from Gauss's law applied to a Gaussian surface just inside the conductor surface.

## How It's Best Learned
Apply Gauss's law with a pillbox Gaussian surface at the conductor surface to derive the boundary condition E = σ/ε₀. Then analyze scenarios like a conductor with a cavity, a grounded conductor, and induced charges.

## Common Misconceptions
- Charge does not distribute uniformly on an irregular conductor; it concentrates at sharp points.
- A hollow conductor shields its interior from external fields — Faraday cage effect.
- Equilibrium is reached on timescales of ~10⁻¹⁹ s for metals, essentially instantaneous.

## Explainer

You already know from Gauss's law that the flux through any closed surface equals the enclosed charge divided by ε₀. Now consider a Gaussian surface drawn just inside the bulk of a conductor — infinitesimally inside the surface. In static equilibrium, there is no current flowing, so free electrons have already repositioned themselves until there is no net force on them. If any internal electric field existed, it would push electrons, contradicting equilibrium. Therefore, **E = 0 everywhere inside a conductor in electrostatic equilibrium**. By Gauss's law, zero field through every interior Gaussian surface means zero net enclosed charge — any excess charge must therefore reside entirely on the surface.

Because E = 0 throughout the interior, the work done moving a charge between any two interior points is zero. That means all interior points are at the same potential — the conductor's interior (and surface) is an **equipotential region**. This is why conductors are used as shielding: any potential difference established outside produces no field inside, regardless of the conductor's shape or the complexity of the external configuration.

At the conductor surface itself, the field is not zero — it must support the surface charge density. Using a flat pillbox Gaussian surface that straddles the surface (part inside, part outside), Gauss's law gives E = σ/ε₀ directed perpendicular to the surface, where σ is the local surface charge density. The field is always perpendicular because a tangential component would drive currents along the surface, again contradicting equilibrium.

The distribution of charge on an irregular conductor is not uniform — it concentrates where the surface curves most sharply. At a pointed tip, the surface charge density and the external field are much stronger than at a flat region. This explains lightning rods: a sharp point creates a strong local field that ionizes air and allows charge to bleed off safely. Finally, a hollow conductor provides a **Faraday cage**: external electric fields induce surface charges on the outer surface that precisely cancel the external field inside the cavity. Any object placed inside the cavity is completely shielded from external electrostatic disturbances.
