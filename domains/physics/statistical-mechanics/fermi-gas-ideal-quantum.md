---
id: fermi-gas-ideal-quantum
title: 'The Ideal Fermi Gas: Ground State and Excitations'
domain: physics
course: statistical-mechanics
prerequisites:
- id: fermi-dirac-distribution-statistics
  type: hard
- id: grand-canonical-ensemble
  type: soft
builds-toward:
- debye-model-lattice-dynamics
- critical-phenomena-statmech
tags:
- fermi-gas
- degenerate-fermions
- density-of-states
stage: advanced
status: draft
---

# The Ideal Fermi Gas: Ground State and Excitations

## Core Idea
An ideal Fermi gas at T=0 has all states filled up to the Fermi energy E_F, which depends on particle density as E_F ∝ (n)^(2/3). At finite T, excitations near the Fermi surface contribute to heat capacity as C_V ∝ T, much smaller than the classical equipartition value. Pressure and other thermodynamic quantities follow from the density of states.

## Explainer

From Fermi-Dirac statistics, you know the average occupation of a single-particle state with energy ε is ⟨n_ε⟩ = 1/(e^{(ε − μ)/kT} + 1). At T = 0, this step function is exactly 1 for ε < μ and exactly 0 for ε > μ. The ideal Fermi gas applies this to N non-interacting fermions confined to a box, asking: what is the ground state, and how does the system behave at low temperature?

At T = 0, the ground state is the **Fermi sea**: fill every single-particle state in increasing energy order, one fermion per state (respecting the Pauli exclusion principle), until all N fermions are placed. The energy of the last filled state is the **Fermi energy**, E_F = (ℏ²/2m)(3π²n)^{2/3}, where n = N/V is the number density. For electrons in a typical metal, n ~ 10²⁸ m⁻³, giving E_F ~ 5 eV — equivalent to a temperature of roughly 60,000 K. Even at absolute zero, the electrons have enormous kinetic energy, and the zero-temperature pressure (the **degeneracy pressure**) does not vanish. This quantum pressure supports white dwarf stars against gravitational collapse.

The low-temperature behavior reveals another dramatic departure from classical intuition. Classically, each gas particle contributes (3/2)k to the heat capacity, giving C_V = (3/2)Nk = (3/2)R per mole. But in a Fermi gas at temperature T, only electrons within approximately kT of the Fermi surface can be thermally excited — those deep in the Fermi sea cannot jump upward because all nearby states are already occupied. The fraction of electrons that participate is roughly kT/E_F, so the heat capacity is reduced by this factor: **C_V ≈ (π²/2)(kT/E_F)Nk ∝ T**, linear in temperature rather than constant. For typical metals at room temperature, kT/E_F ~ 300 K / 60,000 K ~ 0.005, so the electronic heat capacity is about 200 times smaller than the classical prediction. This explains why the heat capacity of metals is dominated by lattice vibrations (phonons ∝ T³) at low T and rises only weakly, with electronic contributions showing up as the linear term in careful measurements at very low temperatures — a key confirmation that conduction electrons behave as a degenerate Fermi gas.
