---
id: atomic-orbitals-quantum
title: Quantum Atomic Orbitals
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-solution
  type: hard
tags:
- atoms
- orbitals
- wavefunctions
stage: advanced
status: draft
---

# Quantum Atomic Orbitals

## Core Idea
Atomic orbitals ψ_{nlm}(r,θ,φ) = R_{nl}(r)Y_l^m(θ,φ) are labeled by quantum numbers n (energy), ℓ (angular momentum), and m (z-component). The probability density |ψ|² gives the charge cloud picture; orbitals represent probability distributions, not electron trajectories.

## Explainer

From solving the hydrogen atom, you already know that the Schrödinger equation in spherical coordinates separates into a radial part and an angular part. The angular solutions are the **spherical harmonics** Y_l^m(θ,φ), which encode the shape and orientation of the orbital. The radial solutions R_{nl}(r) encode how the probability density varies with distance from the nucleus. Together, their product ψ_{nlm} is an atomic orbital — a complete description of one possible stationary state of an electron in the hydrogen potential.

The three **quantum numbers** each tell you something distinct. The principal quantum number **n** (n = 1, 2, 3, ...) determines the energy: E_n = -13.6 eV / n². The **ℓ** quantum number (0 ≤ ℓ ≤ n−1) determines the magnitude of orbital angular momentum and the shape of the orbital — ℓ = 0 gives s orbitals (spherically symmetric), ℓ = 1 gives p orbitals (dumbbell-shaped), ℓ = 2 gives d orbitals, and so on. The magnetic quantum number **m** (−ℓ ≤ m ≤ ℓ) determines the z-component of angular momentum and the spatial orientation. A given energy level n has n² degenerate states corresponding to all allowed (ℓ, m) combinations.

The critical conceptual break from classical mechanics is that |ψ_{nlm}(r,θ,φ)|² is a **probability density** — it tells you the probability per unit volume of finding the electron near position (r,θ,φ). There is no well-defined orbit or trajectory. The familiar picture of an "electron cloud" or "charge cloud" is just this probability density visualized, with denser regions indicating higher probability. An electron in a 1s orbital is not circling the nucleus; it simply has a highest probability of being found near the Bohr radius a₀, with probability spread over a spherical shell.

Because orbitals are derived from a separable differential equation with specific boundary conditions, they form a complete orthonormal basis for the electron's Hilbert space. Any single-electron state can be written as a superposition of orbitals. For multi-electron atoms, the same orbital shapes apply approximately (via the central field approximation), with the important addition of spin and the Pauli exclusion principle, which explains the periodic table's structure. The quantum numbers n, ℓ, m were not invented — they emerged from the mathematics of the hydrogen solution as the only values for which normalizable wavefunctions exist.
