---
id: intermolecular-potential-models
title: Intermolecular Potential Energy Models
domain: chemistry
course: physical-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: statistical-mechanics-foundations
  type: soft
- id: molecular-polarity
  type: soft
builds-toward:
- transport-phenomena-gases
tags:
- Lennard-Jones
- van-der-Waals
- dispersion
- pair-potential
- virial-equation
- second-virial-coefficient
stage: advanced
status: validated
---

# Intermolecular Potential Energy Models

## Core Idea
Intermolecular potential models quantify the energy of interaction between molecules as a function of separation distance r. The Lennard-Jones 12-6 potential u(r) = 4ε[(σ/r)¹² − (σ/r)⁶] captures short-range repulsion (Pauli exclusion, r⁻¹²) and long-range London dispersion attraction (r⁻⁶) with two parameters: well depth ε and collision diameter σ. Electrostatic contributions (dipole-dipole, dipole-induced-dipole) add orientation-dependent terms. The second virial coefficient B(T) = −2πN_A∫[exp(−u(r)/kT)−1]r²dr connects the pair potential to deviations from ideal gas behavior, providing a direct experimental route to determining ε and σ from equation-of-state measurements.

## How It's Best Learned
Plot the LJ potential and identify the equilibrium separation (r_min = 2^(1/6)σ), well depth ε, and where the potential crosses zero (r = σ). Calculate B(T) numerically for argon and compare to experimental data across a range of temperatures.

## Common Misconceptions
- Thinking the r⁻¹² repulsion term has a physical origin; it is chosen for computational convenience, not because repulsion follows a 12th-power law (e.g., exponential functions are more accurate).
- Confusing ε (well depth, positive) with the total interaction energy (which is negative at the minimum of the potential).
