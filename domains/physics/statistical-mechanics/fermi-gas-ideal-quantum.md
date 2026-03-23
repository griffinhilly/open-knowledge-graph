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
stage: expert
status: draft
---

# The Ideal Fermi Gas: Ground State and Excitations

## Core Idea
An ideal Fermi gas at T=0 has all states filled up to the Fermi energy E_F, which depends on particle density as E_F ∝ (n)^(2/3). At finite T, excitations near the Fermi surface contribute to heat capacity as C_V ∝ T, much smaller than the classical equipartition value. Pressure and other thermodynamic quantities follow from the density of states.

## Questions

```yaml
- question: "A physics student applies classical equipartition to electrons in a metal at room temperature, predicting each electron contributes (3/2)k to the heat capacity. The measured value is about 200 times smaller. What explains the discrepancy?"
  type: multiple-choice
  options:
    - "Electrons in metals are bound to atomic sites and cannot move freely enough to contribute to heat capacity"
    - "Only electrons within approximately kT of the Fermi surface can be thermally excited — electrons deep in the Fermi sea are blocked because all nearby states are already occupied"
    - "Electron-electron repulsion cancels out the thermal contribution, reducing the effective heat capacity"
    - "Heat capacity measurements at room temperature are not precise enough to detect electronic contributions"
  answer: 1
  explanation: "The Pauli exclusion principle is responsible. At room temperature, thermal energy kT (~0.026 eV) is tiny compared to the Fermi energy (~5 eV for typical metals). Only electrons within approximately kT of the Fermi surface can find empty states to be excited into — electrons deep in the Fermi sea are completely blocked because all adjacent states are filled. The fraction that can participate is roughly kT/E_F ≈ 0.005, reducing the heat capacity by the same factor. This is a purely quantum effect with no classical analog."

- question: "The Fermi energy of electrons in a typical metal is approximately 5 eV (~60,000 K equivalent) even at absolute zero. What is the physical origin of this large energy?"
  type: multiple-choice
  options:
    - "Thermal energy stored during the metal's formation that has not yet dissipated"
    - "Electrostatic potential energy from the surrounding ionic lattice, which elevates electron energies"
    - "The Pauli exclusion principle forces electrons to occupy successively higher energy states rather than all settling to the lowest energy"
    - "Zero-point motion of the electrons in the quantum harmonic oscillator potential of the lattice"
  answer: 2
  explanation: "The Fermi energy arises entirely from quantum statistics. If electrons were classical particles, they would all settle into the lowest energy state at T = 0. But the Pauli exclusion principle forbids two fermions from occupying the same quantum state. So filling N electrons forces each into successively higher energy levels (two electrons per state accounting for spin). For typical metallic densities, filling all N electrons forces the last one to approximately 5 eV. This enormous 'zero-temperature kinetic energy' is a direct consequence of fermionic statistics, not of any classical force."

- question: "At absolute zero (T = 0), an ideal Fermi gas has zero total kinetic energy because there is no thermal energy available to excite the particles."
  type: true-false
  answer: false
  explanation: "This is the classical intuition that quantum mechanics overturns. Classical particles would all occupy the lowest energy state at T = 0, giving zero kinetic energy. Fermions cannot do this — the Pauli exclusion principle requires each quantum state to hold at most one fermion. At T = 0, the ground state is the Fermi sea: all states filled up to E_F, giving particles an average kinetic energy of (3/5)E_F. This zero-temperature energy produces degeneracy pressure that supports white dwarf stars against gravitational collapse."

- question: "The degeneracy pressure of a Fermi gas arises from electrostatic repulsion between the electrons."
  type: true-false
  answer: false
  explanation: "Degeneracy pressure is a purely quantum mechanical effect arising from the Pauli exclusion principle, not from any force between particles. In an ideal Fermi gas, particles are non-interacting by definition — there is no Coulomb repulsion included. The pressure exists because compressing the gas into a smaller volume forces particles into higher energy states (the minimum energies required increase with density). This quantum pressure operates even for hypothetically uncharged fermions, and it is what prevents white dwarf stars and neutron stars from collapsing under gravity."

- question: "Why does the heat capacity of an ideal Fermi gas at low temperature scale as C_V ∝ T rather than being constant, as classical equipartition predicts? Explain in terms of which electrons can and cannot contribute."
  type: short-answer
  answer: "Classical equipartition predicts each electron contributes (3/2)k regardless of temperature, giving a constant C_V. In a Fermi gas, the Pauli exclusion principle means all states up to E_F are filled at T = 0. When temperature rises to T, only electrons within approximately kT of the Fermi surface can be excited into available empty states above E_F — electrons deep in the Fermi sea are blocked because all nearby states are already occupied. The fraction of thermally active electrons is roughly kT/E_F, so the heat capacity is reduced by that factor: C_V ≈ (π²/2)(kT/E_F) · Nk, which is linear in T. For metals at room temperature, kT/E_F ≈ 0.005, giving a heat capacity about 200 times smaller than the classical prediction."
  explanation: "The T-linear electronic heat capacity is one of the key experimental signatures of Fermi-Dirac statistics in metals. At very low temperatures, it dominates over the Debye T³ phonon contribution, and careful measurements of the combined C_V = γT + βT³ allow the Fermi energy to be extracted — a direct confirmation that conduction electrons form a degenerate quantum gas."
```

## Explainer

From Fermi-Dirac statistics, you know the average occupation of a single-particle state with energy ε is ⟨n_ε⟩ = 1/(e^{(ε − μ)/kT} + 1). At T = 0, this step function is exactly 1 for ε < μ and exactly 0 for ε > μ. The ideal Fermi gas applies this to N non-interacting fermions confined to a box, asking: what is the ground state, and how does the system behave at low temperature?

At T = 0, the ground state is the **Fermi sea**: fill every single-particle state in increasing energy order, one fermion per state (respecting the Pauli exclusion principle), until all N fermions are placed. The energy of the last filled state is the **Fermi energy**, E_F = (ℏ²/2m)(3π²n)^{2/3}, where n = N/V is the number density. For electrons in a typical metal, n ~ 10²⁸ m⁻³, giving E_F ~ 5 eV — equivalent to a temperature of roughly 60,000 K. Even at absolute zero, the electrons have enormous kinetic energy, and the zero-temperature pressure (the **degeneracy pressure**) does not vanish. This quantum pressure supports white dwarf stars against gravitational collapse.

The low-temperature behavior reveals another dramatic departure from classical intuition. Classically, each gas particle contributes (3/2)k to the heat capacity, giving C_V = (3/2)Nk = (3/2)R per mole. But in a Fermi gas at temperature T, only electrons within approximately kT of the Fermi surface can be thermally excited — those deep in the Fermi sea cannot jump upward because all nearby states are already occupied. The fraction of electrons that participate is roughly kT/E_F, so the heat capacity is reduced by this factor: **C_V ≈ (π²/2)(kT/E_F)Nk ∝ T**, linear in temperature rather than constant. For typical metals at room temperature, kT/E_F ~ 300 K / 60,000 K ~ 0.005, so the electronic heat capacity is about 200 times smaller than the classical prediction. This explains why the heat capacity of metals is dominated by lattice vibrations (phonons ∝ T³) at low T and rises only weakly, with electronic contributions showing up as the linear term in careful measurements at very low temperatures — a key confirmation that conduction electrons behave as a degenerate Fermi gas.
