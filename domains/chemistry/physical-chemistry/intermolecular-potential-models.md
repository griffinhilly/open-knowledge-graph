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

## Explainer

From intermolecular forces, you know qualitatively that molecules attract at long range (London dispersion, dipole-dipole) and repel at short range (electron cloud overlap). **Intermolecular potential models** translate these qualitative ideas into mathematical functions that predict the exact energy of interaction at any separation distance r. Having an equation instead of a hand-waving description is what makes it possible to calculate real physical properties — gas viscosities, boiling points, crystal structures — from molecular parameters.

The workhorse model is the **Lennard-Jones (LJ) 12-6 potential**: u(r) = 4ε[(σ/r)¹² − (σ/r)⁶]. The (σ/r)⁶ term captures the attractive London dispersion interaction, which has a solid theoretical basis in quantum mechanics (induced-dipole/induced-dipole interactions fall off as r⁻⁶). The (σ/r)¹² repulsive term models the sharp increase in energy when electron clouds overlap, though the exponent 12 is chosen for mathematical convenience (it is simply the square of 6, making computation efficient) rather than physical rigor. The two parameters have intuitive meanings: **ε** is the depth of the energy well — how strongly the molecules attract at their optimal separation — and **σ** is the collision diameter — the distance at which the potential crosses zero, meaning repulsion and attraction exactly balance. The minimum energy occurs at r_min = 2^(1/6)σ ≈ 1.12σ, just slightly beyond the collision diameter.

For molecules with permanent dipoles, the LJ potential alone is insufficient. You must add **electrostatic terms** that depend on molecular orientation: the dipole-dipole interaction (∝ r⁻³), the dipole-induced dipole interaction (∝ r⁻⁶), and for ions, Coulombic terms (∝ r⁻¹). These orientation-dependent contributions explain why polar molecules like water have much stronger intermolecular interactions than nonpolar molecules of similar size. More sophisticated models like the Stockmayer potential combine the LJ function with a point dipole, while modern force fields used in molecular simulations assign partial charges to individual atoms and sum pairwise Coulombic and LJ interactions across all atom pairs.

The bridge between these microscopic pair potentials and macroscopic behavior runs through the **second virial coefficient** B(T), which describes the first correction to ideal gas behavior in the equation PV = nRT(1 + B/V + ...). The integral B(T) = −2πN_A∫₀^∞[exp(−u(r)/kT) − 1]r²dr connects the pair potential directly to measurable PV data. At low temperatures, attractions dominate and B is negative (gas is more compressible than ideal); at high temperatures, repulsions dominate and B is positive. Fitting experimental B(T) data across a range of temperatures determines ε and σ for a given molecule, turning the abstract potential into a calibrated, predictive tool.
