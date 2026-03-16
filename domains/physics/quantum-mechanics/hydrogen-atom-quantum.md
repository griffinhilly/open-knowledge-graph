---
id: hydrogen-atom-quantum
title: Quantum Mechanical Treatment of Hydrogen
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
- id: angular-momentum-quantum
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- hydrogen-atom-spectrum
- fine-structure-splitting
tags:
- hydrogen-atom
- coulomb-potential
- solvable-systems
stage: advanced
status: draft
---

# Quantum Mechanical Treatment of Hydrogen

## Core Idea
The hydrogen atom with Coulomb potential V(r) = -ke²/r is solved in spherical coordinates. Energy levels depend only on principal quantum number n: En = -13.6 eV / n². Wavefunctions ψ_{nlm}(r,θ,φ) are products of radial functions R_{nl}(r) and spherical harmonics Y_l^m(θ,φ). This exactly solvable system marks the triumph of quantum mechanics over classical theory.

## Explainer

The hydrogen atom is the first and most important exactly solvable system in quantum mechanics. It serves as the foundation for atomic physics, spectroscopy, and ultimately the periodic table. The goal is to find the energy levels and wavefunctions of a single electron bound to a proton by the Coulomb potential V(r) = −ke²/r — attractive, spherically symmetric, and falling off as 1/r.

From your study of eigenvalues and eigenvectors, you know that the time-independent Schrödinger equation is an eigenvalue equation: Ĥψ = Eψ. Because the potential depends only on distance r (spherically symmetric), it is natural to work in **spherical coordinates** (r, θ, φ). From your study of quantum angular momentum, you know the eigenfunctions of L² and Lz are the **spherical harmonics** Y_l^m(θ, φ). The spherical symmetry allows the full wavefunction to separate: ψ_{nlm}(r, θ, φ) = R_{nl}(r) × Y_l^m(θ, φ). The angular part is fully determined by angular momentum theory; what remains is solving for the radial functions R_{nl}(r) subject to the boundary conditions that ψ be normalizable (finite at r = 0 and decaying to zero as r → ∞).

The energy eigenvalues emerge from the normalizability requirement, which forces a quantization condition on the radial solution. This gives **E_n = −13.6 eV / n²**, where n = 1, 2, 3, … is the **principal quantum number**. Three quantum numbers label each state: n (principal, sets the energy), l (orbital angular momentum, 0 to n−1), and m (magnetic, −l to l). The ground state (n=1, l=0, m=0) has energy −13.6 eV — the ionization energy of hydrogen. Excited states have higher (less negative) energy, and the degeneracy grows as n²: for a given n, there are n² distinct states with the same energy because E depends only on n, not on l or m.

The physical picture built by the wavefunctions is rich. For the ground state, the probability density is a simple exponential decay characterized by the **Bohr radius** a₀ ≈ 0.053 nm. For higher n, the radial probability density spreads outward and develops n−l−1 radial nodes. The angular parts give the familiar "orbital shapes" — s orbitals (l=0) are spherically symmetric, p orbitals (l=1) have lobes along the coordinate axes. This is not a circular orbit in any classical sense; it is a genuine probability distribution for where the electron will be found. The true triumph is quantitative: the energy differences E_n − E_{n'} exactly predict the frequencies of hydrogen's spectral lines — the Balmer, Lyman, and Paschen series — explaining with a single formula what decades of empirical spectroscopy had catalogued but not understood.
