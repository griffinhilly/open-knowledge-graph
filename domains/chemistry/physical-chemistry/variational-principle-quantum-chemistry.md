---
id: variational-principle-quantum-chemistry
title: Variational Principle and Basis Set Methods
domain: chemistry
course: physical-chemistry
prerequisites:
- id: schrodinger-equation-molecular-systems
  type: hard
- id: variational-principle-chemistry
  type: soft
builds-toward:
- density-functional-theory-molecules
- hartree-fock-self-consistent-field
tags:
- quantum
- variational
- approximation
- basis-sets
stage: advanced
status: draft
---

# Variational Principle and Basis Set Methods

## Core Idea
The variational principle states that any trial wavefunction yields an energy expectation value that is greater than or equal to the true ground state energy. By expanding the trial wavefunction as a linear combination of basis functions and minimizing energy with respect to coefficients, we obtain the best approximation within that basis set. This approach underlies all modern quantum chemical calculations.

## Explainer

From your work with the Schrödinger equation for molecular systems, you know that exact solutions are impossible for anything beyond the simplest one-electron systems. The **variational principle** transforms this impossibility into a practical optimization problem: guess a wavefunction, compute its energy, and know with certainty that your answer is an upper bound to the true ground-state energy. Any improvement to the guess can only lower the energy toward the exact value, never below it. This one-way guarantee turns quantum chemistry from an unsolvable differential equation into a minimization problem — and minimization is something we know how to do computationally.

The strategy works as follows. You write a **trial wavefunction** as a linear combination of known functions: ψ_trial = c₁φ₁ + c₂φ₂ + ... + cₙφₙ. The functions φᵢ are your **basis set** — a collection of mathematical building blocks, typically Gaussian functions centered on each atom in the molecule. The coefficients cᵢ are the adjustable parameters. You compute the energy expectation value E = ⟨ψ_trial|Ĥ|ψ_trial⟩/⟨ψ_trial|ψ_trial⟩, take derivatives with respect to each coefficient, set them to zero, and solve the resulting system of equations. This procedure, called the **Rayleigh-Ritz method**, yields the best possible wavefunction within the space spanned by your chosen basis functions.

The quality of the answer depends entirely on the basis set. A minimal basis set — one function per occupied atomic orbital — captures the qualitative shape of molecular orbitals but misses quantitative details. Adding more functions (polarization functions that allow orbitals to distort, diffuse functions for loosely bound electrons) systematically improves the result. Common basis set families like STO-3G, 6-31G*, cc-pVDZ, and cc-pVTZ represent a hierarchy of increasing accuracy and increasing computational cost. The **basis set limit** is the best energy achievable with an infinitely flexible basis; approaching it requires balancing accuracy against the practical constraint that computation time grows steeply with basis set size (roughly as N⁴ for Hartree-Fock).

Understanding the variational principle also clarifies what it cannot do. It guarantees an upper bound only for the ground state — excited-state energies calculated variationally can be above or below the true values unless special orthogonality constraints are enforced. It also guarantees the energy bound only for the exact Hamiltonian; approximate methods that modify the Hamiltonian (like some DFT approaches) do not inherit this property. Despite these limitations, the variational principle plus basis set expansion is the engine that powers virtually every electronic structure calculation in modern chemistry, from drug design to materials science.
