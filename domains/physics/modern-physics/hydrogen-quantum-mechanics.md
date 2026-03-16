---
id: hydrogen-quantum-mechanics
title: Hydrogen Atom in Quantum Mechanics
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-eigenvalue-problem
  type: hard
- id: bohr-model
  type: soft
builds-toward:
- spectral-lines-transitions-wavelength
tags:
- quantum
- atoms
- hydrogen
stage: abstract-reasoning
status: draft
---

# Hydrogen Atom in Quantum Mechanics

## Core Idea
The quantum mechanical hydrogen atom reproduces Bohr's energy levels En = −13.6 eV/n² without assuming circular orbits. Solutions yield three quantum numbers: n (principal, determines energy), ℓ (orbital angular momentum), and mℓ (z-component of angular momentum). Wavefunctions describe probability clouds (orbitals), not trajectories. This approach extends naturally to multi-electron atoms and molecules.

## Explainer

Your prerequisite — the Schrödinger eigenvalue problem — taught you to find quantum states as solutions to Ĥψ = Eψ. For hydrogen, the Hamiltonian is Ĥ = −(ℏ²/2m)∇² − e²/(4πε₀r), combining kinetic energy with the Coulomb attraction between electron and proton. Because the potential depends only on r (it is spherically symmetric), the solutions separate: ψ(r,θ,φ) = R(r)·Y_ℓ^m(θ,φ), where R(r) satisfies a radial equation and Y_ℓ^m are the spherical harmonics governing the angular dependence. This separation is what makes hydrogen exactly solvable, and the three quantum numbers emerge naturally — one from each separated equation.

The **principal quantum number** n = 1, 2, 3, ... determines the energy: E_n = −13.6 eV/n². This is Bohr's formula, recovered without assuming circular orbits. The **orbital angular momentum quantum number** ℓ = 0, 1, ..., n−1 quantifies the magnitude of angular momentum: |L⃗| = ℏ√(ℓ(ℓ+1)). The **magnetic quantum number** m_ℓ = −ℓ, ..., 0, ..., +ℓ quantifies the z-component: L_z = m_ℓℏ. Notice how n constrains ℓ, which constrains m_ℓ — the three quantum numbers are linked because they come from three nested separation equations. For a given n, there are n² distinct states (one for ℓ = 0, three for ℓ = 1, five for ℓ = 2, and so on), all sharing the same energy. This **degeneracy** is a special property of the 1/r Coulomb potential.

The Bohr model gave correct energies by assuming electrons travel on circular orbits of radius a₀n². The quantum mechanical picture replaces orbits with **probability clouds** (orbitals). The quantity |ψ(r,θ,φ)|² gives the probability density for finding the electron at position (r,θ,φ). For the 1s ground state (n=1, ℓ=0, m_ℓ=0), this is spherically symmetric and peaks at the nucleus, decaying exponentially outward. The most probable radius — the peak of the radial probability distribution r²|R(r)|² — is exactly the Bohr radius a₀ ≈ 0.053 nm. Bohr got the right radius but for the wrong reason; quantum mechanics justifies it rigorously.

The n²-fold degeneracy of each energy level is deeper than spherical symmetry alone would predict. A merely spherically symmetric problem would have only a (2ℓ+1)-fold degeneracy in m_ℓ for each ℓ; the additional degeneracy across different ℓ values sharing the same n reflects a hidden SO(4) symmetry of the Coulomb potential — an extra conserved quantity called the Laplace-Runge-Lenz vector. This degeneracy is lifted by perturbations: spin-orbit coupling, relativistic corrections, and external fields all split the n-levels into distinct sub-levels, producing the **fine structure** and **hyperfine structure** observed in high-resolution hydrogen spectra and predicted by the deeper theory.
