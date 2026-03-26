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
- id: eigenvalues-and-eigenvectors
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
status: validated
---

# Solving the Schrödinger Equation for Hydrogen Atom

## Core Idea
The time-independent Schrödinger equation for hydrogen separates in spherical coordinates into radial and angular parts. Solutions are labeled by quantum numbers n (principal), ℓ (orbital angular momentum), and m_ℓ (magnetic). Energy depends only on n: E_n = −13.6 eV / n². Degeneracy increases as n² because different (ℓ, m_ℓ) combinations give the same energy.

## How It's Best Learned
Understand the separation of variables and radial equation with effective potential. Recognize the role of boundary conditions in quantizing energy. Compare predictions (energy levels, wavefunctions) with experimental hydrogen spectrum and atomic properties.

## Common Misconceptions
The wavefunction ψ(r,θ,φ) is not an orbit—it is a probability amplitude whose square gives probability density. Quantum numbers must satisfy 0 ≤ ℓ ≤ n−1 and −ℓ ≤ m_ℓ ≤ ℓ.

## Questions

```yaml
- question: "A hydrogen atom is in the state n=2, ℓ=1, m_ℓ=0. What is its energy?"
  type: multiple-choice
  options:
    - "−3.4 eV, the same as all n=2 states regardless of ℓ or m_ℓ"
    - "−1.51 eV, because ℓ=1 raises the energy compared to ℓ=0"
    - "−13.6 eV, because a p orbital keeps the electron close to the nucleus"
    - "−6.8 eV, determined by the product of n and ℓ"
  answer: 0
  explanation: "Energy in hydrogen depends only on the principal quantum number n: E_n = −13.6 eV/n². For n=2, E = −13.6/4 = −3.4 eV regardless of whether ℓ=0 (s orbital) or ℓ=1 (p orbital). This n²-fold degeneracy — all four n=2 states (2s, 2px, 2py, 2pz) having the same energy — is a special feature of the Coulomb 1/r potential. It breaks down in multi-electron atoms, but is exact for hydrogen."

- question: "Which set of quantum numbers represents a valid hydrogen orbital?"
  type: multiple-choice
  options:
    - "n=2, ℓ=2, m_ℓ=0"
    - "n=3, ℓ=2, m_ℓ=−3"
    - "n=3, ℓ=1, m_ℓ=−1"
    - "n=1, ℓ=1, m_ℓ=0"
  answer: 2
  explanation: "The constraints are 0 ≤ ℓ ≤ n−1 and −ℓ ≤ m_ℓ ≤ ℓ. Option A fails because ℓ=2 requires n≥3. Option B fails because m_ℓ=−3 requires ℓ≥3. Option D fails because ℓ=1 requires n≥2. Only option C satisfies both rules: n=3, ℓ=1 satisfies ℓ ≤ n−1 = 2, and m_ℓ=−1 satisfies |m_ℓ| ≤ ℓ = 1."

- question: "In hydrogen, the 2s and 2p orbitals have the same energy."
  type: true-false
  answer: true
  explanation: "Because the hydrogen atom energy E_n = −13.6 eV/n² depends only on n, all orbitals with n=2 are exactly degenerate: 2s (ℓ=0) and all three 2p orbitals (ℓ=1, m_ℓ=−1,0,+1) all sit at −3.4 eV. This n²-fold degeneracy — four states for n=2, nine for n=3 — is a hidden symmetry specific to the 1/r potential. The degeneracy lifts in multi-electron atoms, which is why 2s and 2p electrons have different energies in carbon but not in hydrogen."

- question: "The wavefunction ψ(r,θ,φ) of a hydrogen orbital describes the trajectory the electron follows as it orbits the nucleus."
  type: true-false
  answer: false
  explanation: "The wavefunction is a probability amplitude, not a trajectory. |ψ(r,θ,φ)|² gives the probability density — the probability of finding the electron in a small volume element at that location. Electrons do not follow classical orbits; the orbital shape (s, p, d) represents a cloud of probability rather than a path. Treating orbitals as orbits was Bohr's model, which quantum mechanics replaced precisely because electrons do not have definite positions and momenta simultaneously."

- question: "Why does the energy of a hydrogen atom depend only on the principal quantum number n, and what does this imply about the number of distinct quantum states at each energy level?"
  type: short-answer
  answer: "Energy depends only on n because the 1/r Coulomb potential has a special hidden symmetry (beyond spherical symmetry) that makes all (ℓ, m_ℓ) combinations at a given n degenerate. For each n, ℓ runs from 0 to n−1, and for each ℓ, m_ℓ runs from −ℓ to +ℓ, giving n² distinct states all at the same energy E_n."
  explanation: "The n² degeneracy is not just a coincidence of the math — it reflects a conserved quantity (the Runge-Lenz vector) that is specific to inverse-square-law forces. For n=1: 1 state; for n=2: 4 states (1s + 3×2p); for n=3: 9 states (1s + 3×2p + 5×3d), all degenerate. This degeneracy has physical consequences: it is why hydrogen's spectral lines appear where they do and why atomic shells fill the way they do in the periodic table."
```

## Explainer

You have learned the Schrödinger equation and quantum numbers, and you know that solving it means finding the eigenvalues and eigenfunctions of the Hamiltonian operator. The hydrogen atom is the most important exactly-solvable problem in quantum mechanics — the Coulomb potential V = −ke²/r has just enough symmetry to allow a complete analytic solution that illuminates the whole structure of atomic physics.

The strategy is **separation of variables**. The wavefunction ψ(r,θ,φ) is written as a product R(r)Y(θ,φ), where R is a purely radial function and Y is purely angular. Substituting into the Schrödinger equation in spherical coordinates, you find that the angular part Y(θ,φ) satisfies an equation whose solutions are the **spherical harmonics** Y_ℓ^m(θ,φ), characterized by two quantum numbers: ℓ (orbital angular momentum, non-negative integer) and m_ℓ (magnetic quantum number, integer with |m_ℓ| ≤ ℓ). The spherical harmonics are eigenfunctions of both the total angular momentum L² and its z-component L_z — they describe the shape and orientation of the wavefunction in angle space. The radial equation, meanwhile, contains an **effective potential** that adds a centrifugal barrier ℏ²ℓ(ℓ+1)/(2mr²) to the Coulomb attraction, depending on ℓ.

Solving the radial equation with the requirement that the wavefunction remain normalizable (decaying to zero as r → ∞) quantizes the energy. The allowed energies are E_n = −13.6 eV/n², where n = 1, 2, 3, ... is the **principal quantum number**. The n = 1 ground state has the electron closest to the nucleus on average and the largest binding energy. The -13.6 eV value matches the experimentally measured ionization energy of hydrogen to high precision — this exact agreement was one of quantum mechanics' earliest triumphs. Importantly, the energy depends only on n, not on ℓ or m_ℓ: for each n, the allowed values of ℓ run from 0 to n−1, and for each ℓ, m_ℓ runs from −ℓ to +ℓ, giving n² distinct (ℓ, m_ℓ) states all at the same energy. This **degeneracy** is larger than what the spherical symmetry alone would require — it is a hidden symmetry of the 1/r potential specific to the Coulomb problem.

The resulting wavefunctions ψ_nlm(r,θ,φ) = R_nl(r)Y_ℓ^m(θ,φ) are called **atomic orbitals**. The label n = 1, ℓ = 0 gives the 1s orbital (spherically symmetric); n = 2, ℓ = 1 gives the three 2p orbitals (dumbbell-shaped, oriented along x, y, z for m_ℓ = ±1, 0). The radial function R_nl tells you where the electron is likely to be found at various distances from the nucleus, and |ψ|² gives the full three-dimensional probability density. These orbitals are the building blocks for multi-electron atoms (via the Pauli principle and orbital filling), molecular bonding, and all of chemistry. The pattern of energy levels directly predicts the hydrogen emission spectrum — each spectral line corresponds to a transition between levels, setting up the photon absorption and emission physics you will study next.
