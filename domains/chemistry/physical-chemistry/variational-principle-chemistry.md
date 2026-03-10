---
id: variational-principle-chemistry
title: The Variational Principle and Trial Wavefunctions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hydrogen-atom-wavefunctions
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- molecular-orbital-theory-advanced
- huckel-molecular-orbital-theory
tags:
- variational
- ground-state
- approximate-methods
- helium
stage: advanced
status: draft
---

# The Variational Principle and Trial Wavefunctions

## Core Idea
The variational principle states that for any trial wavefunction φ, the expectation value of the energy ⟨φ|Ĥ|φ⟩/⟨φ|φ⟩ is always greater than or equal to the true ground-state energy E₀. This gives a systematic way to improve approximate wavefunctions by minimizing the energy with respect to variational parameters. The secular determinant |H − ES| = 0, obtained by expanding the trial function in a basis set, reduces the problem to matrix diagonalization. This principle underpins Hartree-Fock theory, DFT, and all basis-set electronic structure methods.

## How It's Best Learned
Apply the variational method to helium as a first example, using a screened hydrogenic wavefunction with the screening constant as the variational parameter. Observe how minimizing energy gives the optimal screening constant.

## Common Misconceptions
- Thinking the variational principle gives the exact energy — it gives an upper bound; the true energy is lower or equal.
- Forgetting that the principle applies only to the ground state (with exceptions for excited states of different symmetry).
