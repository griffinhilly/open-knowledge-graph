---
id: hydrogen-atom-schrodinger-solution
title: Solving the Schrödinger Equation for Hydrogen Atom
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
- id: quantum-numbers
  type: hard
- id: hydrogen-atom-quantum
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
- id: differential-equations-intro
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- hydrogen-radial-wavefunction
- principal-angular-magnetic-quantum-numbers
tags:
- quantum-mechanics
- hydrogen
- atomic-physics
stage: advanced
status: draft
---

# Solving the Schrödinger Equation for Hydrogen Atom

## Core Idea
The time-independent Schrödinger equation for hydrogen separates in spherical coordinates into radial and angular parts. Solutions are labeled by quantum numbers n (principal), ℓ (orbital angular momentum), and m_ℓ (magnetic). Energy depends only on n: E_n = −13.6 eV / n². Degeneracy increases as n² because different (ℓ, m_ℓ) combinations give the same energy.

## How It's Best Learned
Understand the separation of variables and radial equation with effective potential. Recognize the role of boundary conditions in quantizing energy. Compare predictions (energy levels, wavefunctions) with experimental hydrogen spectrum and atomic properties.

## Common Misconceptions
The wavefunction ψ(r,θ,φ) is not an orbit—it is a probability amplitude whose square gives probability density. Quantum numbers must satisfy 0 ≤ ℓ ≤ n−1 and −ℓ ≤ m_ℓ ≤ ℓ.

## Explainer

You have learned the Schrödinger equation and quantum numbers, and you know that solving it means finding the eigenvalues and eigenfunctions of the Hamiltonian operator. The hydrogen atom is the most important exactly-solvable problem in quantum mechanics — the Coulomb potential V = −ke²/r has just enough symmetry to allow a complete analytic solution that illuminates the whole structure of atomic physics.

The strategy is **separation of variables**. The wavefunction ψ(r,θ,φ) is written as a product R(r)Y(θ,φ), where R is a purely radial function and Y is purely angular. Substituting into the Schrödinger equation in spherical coordinates, you find that the angular part Y(θ,φ) satisfies an equation whose solutions are the **spherical harmonics** Y_ℓ^m(θ,φ), characterized by two quantum numbers: ℓ (orbital angular momentum, non-negative integer) and m_ℓ (magnetic quantum number, integer with |m_ℓ| ≤ ℓ). The spherical harmonics are eigenfunctions of both the total angular momentum L² and its z-component L_z — they describe the shape and orientation of the wavefunction in angle space. The radial equation, meanwhile, contains an **effective potential** that adds a centrifugal barrier ℏ²ℓ(ℓ+1)/(2mr²) to the Coulomb attraction, depending on ℓ.

Solving the radial equation with the requirement that the wavefunction remain normalizable (decaying to zero as r → ∞) quantizes the energy. The allowed energies are E_n = −13.6 eV/n², where n = 1, 2, 3, ... is the **principal quantum number**. The n = 1 ground state has the electron closest to the nucleus on average and the largest binding energy. The -13.6 eV value matches the experimentally measured ionization energy of hydrogen to high precision — this exact agreement was one of quantum mechanics' earliest triumphs. Importantly, the energy depends only on n, not on ℓ or m_ℓ: for each n, the allowed values of ℓ run from 0 to n−1, and for each ℓ, m_ℓ runs from −ℓ to +ℓ, giving n² distinct (ℓ, m_ℓ) states all at the same energy. This **degeneracy** is larger than what the spherical symmetry alone would require — it is a hidden symmetry of the 1/r potential specific to the Coulomb problem.

The resulting wavefunctions ψ_nlm(r,θ,φ) = R_nl(r)Y_ℓ^m(θ,φ) are called **atomic orbitals**. The label n = 1, ℓ = 0 gives the 1s orbital (spherically symmetric); n = 2, ℓ = 1 gives the three 2p orbitals (dumbbell-shaped, oriented along x, y, z for m_ℓ = ±1, 0). The radial function R_nl tells you where the electron is likely to be found at various distances from the nucleus, and |ψ|² gives the full three-dimensional probability density. These orbitals are the building blocks for multi-electron atoms (via the Pauli principle and orbital filling), molecular bonding, and all of chemistry. The pattern of energy levels directly predicts the hydrogen emission spectrum — each spectral line corresponds to a transition between levels, setting up the photon absorption and emission physics you will study next.
