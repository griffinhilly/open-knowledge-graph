---
id: statistical-thermodynamics-applications
title: 'Statistical Thermodynamics: Properties from Partition Functions'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-partition-functions
  type: hard
- id: thermochemistry-enthalpy
  type: soft
builds-toward:
- transition-state-theory
tags:
- Helmholtz
- internal-energy
- heat-capacity
- entropy
- equilibrium-constant
- standard-state
stage: advanced
status: draft
---

# Statistical Thermodynamics: Properties from Partition Functions

## Core Idea
All thermodynamic functions can be derived from the partition function through standard relations: U = kT²(∂ln Q/∂T)_V, A = −kT ln Q (Helmholtz free energy), S = (U−A)/T, and G = A + pV. The heat capacity at constant volume is C_V = (∂U/∂T)_V. Equilibrium constants can be computed from the standard Gibbs energies of reactants and products, which in turn come from partition functions — enabling ab initio predictions of chemical equilibria. This framework explains why vibrational modes are 'frozen out' at low temperatures (contributing R to C_V only above their characteristic temperature θ_vib = hν/k) and provides a molecular interpretation of the third law of thermodynamics.

## How It's Best Learned
Calculate C_V as a function of temperature for a diatomic gas, showing the stepwise activation of translation (3/2 R), rotation (+R), and vibration (+R). Reconcile with the classical equipartition theorem at high temperature.

## Common Misconceptions
- Assuming equipartition always holds; it is only valid when kT >> level spacing.
- Forgetting that electronic contributions to thermodynamic functions are usually negligible unless the ground state is degenerate or excited states are low-lying.
