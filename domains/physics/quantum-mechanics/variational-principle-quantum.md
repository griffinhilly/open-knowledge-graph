---
id: variational-principle-quantum
title: The Variational Principle in Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: observables-and-operators
  type: hard
builds-toward:
- variational-method-quantum
tags:
- variational-methods
- energy-bounds
stage: formal-systems
status: draft
---

# The Variational Principle in Quantum Mechanics

## Core Idea
For any normalized |ψ⟩, ⟨ψ|Ĥ|ψ⟩ ≥ E₀ (ground state energy). Minimizing over trial wavefunctions estimates E₀ without solving Schrödinger's equation exactly.

## Explainer

From your study of observables and operators, you know that the expectation value of the Hamiltonian in state |ψ⟩ is ⟨ψ|Ĥ|ψ⟩, and that this equals the average energy you would measure. The variational principle adds one crucial theorem: this expectation value is *always* at least as large as the ground state energy E₀, for *any* normalized state |ψ⟩ you choose.

The proof is elegant and short. Expand |ψ⟩ in the energy eigenbasis: |ψ⟩ = Σ_n c_n |n⟩ with Σ_n |c_n|² = 1. Then ⟨ψ|Ĥ|ψ⟩ = Σ_n |c_n|² E_n ≥ Σ_n |c_n|² E₀ = E₀. The inequality holds because every E_n ≥ E₀ by definition of the ground state. Equality holds if and only if |ψ⟩ = |0⟩ (the true ground state). So ⟨Ĥ⟩ is a **rigorous upper bound** on E₀: you can never accidentally compute a value lower than the true ground state energy, no matter what trial state you use.

This turns the problem of finding E₀ into an optimization problem. Choose a family of **trial wavefunctions** |ψ(α)⟩ parameterized by some numbers α (maybe the width of a Gaussian, the exponent in a hydrogen-like orbital, or a set of variational coefficients). Compute E(α) = ⟨ψ(α)|Ĥ|ψ(α)⟩ and minimize over α. The minimum you find is guaranteed to be ≥ E₀, and a good trial family will bring it close. The art of the method is choosing a trial family rich enough to approximate the true ground state without being so complicated that the integrals become intractable. For the hydrogen atom, a trial function ψ(r) ∝ e^{−αr} with one variational parameter α gives the exact ground state — because the true ground state happens to be in that family. For helium, the same form with independent exponents for each electron gives ∼2% error without solving any differential equations.

The variational principle is the foundation of much of computational quantum chemistry and condensed matter physics. **Hartree-Fock theory** parameterizes the wavefunction as a Slater determinant (antisymmetrized product of single-particle orbitals) and minimizes the energy over all such determinants — this is a variational calculation with a structured trial family. **Density functional theory** (Hohenberg-Kohn theorem) rests on the same principle applied to the electron density. Even quantum Monte Carlo methods use variational optimization of explicitly correlated wavefunctions. The principle is powerful precisely because it converts an eigenvalue problem (hard, often impossible exactly) into a minimization problem (tractable, systematically improvable).
