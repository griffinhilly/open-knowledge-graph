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
