---
id: fermi-dirac-distribution-statistics
title: Fermi-Dirac Distribution and Fermi Energy
domain: physics
course: statistical-mechanics
prerequisites:
- id: quantum-statistics-intro
  type: hard
- id: grand-partition-function
  type: hard
builds-toward:
- fermi-gas-ideal-quantum
- ideal-fermi-gas
tags:
- fermi-dirac
- occupation-number
- fermi-energy
stage: advanced
status: draft
---

# Fermi-Dirac Distribution and Fermi Energy

## Core Idea
The Fermi-Dirac distribution n_F(E) = 1/(exp((E-μ)/kT) + 1) gives the average occupation number of a quantum state with energy E. At T=0, it is a step function: filled states below the Fermi energy E_F and empty states above. The Fermi energy is the chemical potential at absolute zero and determines the ground-state properties of degenerate fermion gases.

## Explainer

From the grand canonical ensemble, you know that the average occupation number of a single quantum state is determined by maximizing the grand partition function. For fermions — particles obeying the Pauli exclusion principle — each state can hold at most one particle: occupation number 0 or 1. Working out the grand canonical average gives the **Fermi-Dirac distribution**: n_F(E) = 1/(exp((E−μ)/kT) + 1). The +1 in the denominator is the signature of fermionic statistics. It enforces the ceiling of 1 on the occupation number — no matter how large the exponential factor, n_F never exceeds 1.

The behavior at T = 0 is the clearest starting point. When T → 0, (E−μ)/kT → −∞ for all states with E < μ, making exp((E−μ)/kT) → 0, so n_F → 1. For E > μ, the exponential → +∞ and n_F → 0. The distribution becomes a perfect step function: all states below the **chemical potential μ(T=0) ≡ E_F** are exactly filled; all states above are exactly empty. This is the **Fermi energy** — the energy of the highest occupied state at absolute zero. Unlike a classical gas which would collapse to zero kinetic energy at T = 0, a Fermi gas has substantial zero-point kinetic energy because the Pauli principle forces electrons to stack up into progressively higher energy states.

At finite temperature, the sharp step smears out over a width of order kT centered at μ. States within ~kT below E_F have some probability of being empty; states within ~kT above E_F have some probability of being occupied. The thermal excitations responsible for electronic heat capacity and electrical conductivity come entirely from this narrow band of thermally active states. For metals at room temperature, kT ≈ 0.025 eV while E_F ≈ 5–10 eV, so the smearing is only about 0.5% of E_F. The vast majority of conduction electrons are effectively frozen in their ground-state configuration — deeply **degenerate**. Only the tiny fraction near the Fermi surface responds to thermal or electrical perturbations, which is why the classical prediction for electronic heat capacity (3/2 Nk per electron) overestimates the actual value by a factor of ~100.

The chemical potential μ(T) drifts slightly downward from E_F as temperature increases, maintaining constant particle number as the distribution smears. This drift is small for metals (the **Sommerfeld expansion** gives μ ≈ E_F[1 − (π²/12)(kT/E_F)²]) but matters for semiconductor physics, where μ can shift dramatically between the valence and conduction bands. The Fermi energy is therefore not just a number — it is the pivot point around which all fermionic thermal physics is organized.
