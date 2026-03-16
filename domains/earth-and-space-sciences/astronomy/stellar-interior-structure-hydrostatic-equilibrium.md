---
id: stellar-interior-structure-hydrostatic-equilibrium
title: Stellar Interior Structure and Hydrostatic Equilibrium
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: stellar-effective-temperature-color
  type: soft
- id: inverse-square-law-stellar-radiation
  type: soft
- id: hydrostatic-balance-pressure-profile
  type: soft
builds-toward:
- core-hydrogen-burning-main-sequence
tags:
- stellar-structure
- physics
- hydrostatic-equilibrium
stage: formal-systems
status: draft
---

# Stellar Interior Structure and Hydrostatic Equilibrium

## Core Idea
Stars maintain constant radius through hydrostatic equilibrium, where the outward pressure gradient balances the inward gravitational force. Pressure support comes primarily from thermal energy produced by nuclear fusion in the core. Interior temperature, density, and pressure increase monotonically toward the core; these profiles depend on stellar mass and composition. Different energy transport mechanisms (radiation vs. convection) characterize different regions of the stellar interior.

## How It's Best Learned
Understand the balance between pressure and gravity. Use stellar models to explore how changing stellar mass or composition affects interior structure. Connect interior conditions to observable properties like luminosity and spectrum.

## Explainer

You already know that a star's surface reveals its effective temperature and that luminosity follows the inverse-square law as radiation streams outward. But what maintains the star itself — what keeps a million-Earth-mass ball of plasma from collapsing under its own gravity? The answer is **hydrostatic equilibrium**: at every point inside the star, the outward push of pressure exactly balances the inward pull of gravity. This is not a delicate coincidence but a self-regulating condition. If gravity momentarily wins, the layer compresses, heating up and increasing pressure until balance is restored. If pressure wins, the layer expands and cools. The star continuously adjusts on a timescale of minutes (the dynamical timescale), maintaining this equilibrium throughout its life.

The equation governing this balance is deceptively simple: the pressure change across a thin shell equals the weight of that shell per unit area (dP/dr = −ρg, where ρ is density and g is local gravitational acceleration). Integrating from the surface inward, pressure increases monotonically toward the center. For the Sun, surface pressure is negligible, but core pressure reaches about 250 billion atmospheres. Temperature follows a similar gradient — from ~5,800 K at the surface to ~15 million K at the core — because higher temperatures are needed to sustain the pressure that supports the overlying weight. **Density** also increases inward, from the tenuous photosphere to a core density roughly 150 times that of water.

The source of the thermal energy maintaining this pressure is **nuclear fusion** in the core, where temperatures and densities are high enough for hydrogen nuclei to overcome their electrostatic repulsion and fuse into helium. The energy released by fusion replaces the energy radiated from the surface, maintaining the temperature gradient that supports the pressure gradient. This is why a star's luminosity is so tightly coupled to its mass: more massive stars need higher core temperatures to support their greater weight, which drives faster fusion reactions and produces dramatically higher luminosity. A star ten times the Sun's mass is roughly 10,000 times more luminous.

How does energy travel from core to surface? Two mechanisms dominate, and which one operates depends on the local temperature gradient. In **radiative zones**, photons carry energy outward through a slow random walk, absorbed and re-emitted countless times (a photon takes ~170,000 years to diffuse from the Sun's core to the surface). In **convective zones**, the temperature gradient becomes steep enough that hot blobs of gas physically rise, carrying energy like boiling water. In Sun-like stars, the core is radiative and the outer ~30% is convective. In more massive stars, the pattern reverses: a convective core (driven by the intense, centralized energy production of the CNO cycle) surrounded by a radiative envelope. This internal structure — the layering of radiative and convective zones — determines how elements mix, how the star evolves, and ultimately what we observe at the surface.
