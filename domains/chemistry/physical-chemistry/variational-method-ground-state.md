---
id: variational-method-ground-state
title: Variational Method for Ground State Approximation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: variational-principle-chemistry
  type: hard
- id: quantum-chemistry-foundations
  type: hard
builds-toward:
- hartree-fock-method
- density-functional-theory-intro
tags:
- variational-principle
- approximation-methods
- quantum-chemistry
stage: advanced
status: draft
---

# Variational Method for Ground State Approximation

## Core Idea
The variational principle states that for any trial wave function, the calculated energy is greater than or equal to the true ground state energy. This inequality allows systematic approximation by optimizing parameters in trial functions without solving the Schrödinger equation exactly. The method is rigorous—lower energy guarantees a better approximation.

## How It's Best Learned
Use simple trial functions (e.g., exponential with adjustable decay constant) for hydrogen-like systems; minimize energy with respect to parameters and compare with exact solutions. Understand why this approach always works.

## Explainer

From your quantum chemistry foundations, you know that the Schrödinger equation gives exact solutions only for a handful of simple systems — the hydrogen atom, the harmonic oscillator, the particle in a box. For virtually every real molecule, the equation cannot be solved exactly because electron-electron repulsion makes the mathematics intractable. The variational method provides a rigorous way to get approximate answers that are guaranteed to be useful: you guess a wave function, compute the energy, and know with certainty that your answer is an upper bound to the true ground state energy.

The **variational theorem** states that for any normalized trial wave function |ψ_trial⟩, the expectation value of the Hamiltonian satisfies ⟨ψ_trial|H|ψ_trial⟩ ≥ E₀, where E₀ is the exact ground state energy. The proof is elegant: expand the trial function in the basis of exact eigenstates, and because every eigenstate has energy ≥ E₀, any weighted average of those energies must also be ≥ E₀. This inequality is not an approximation or a hope — it is a mathematical fact. It means that if you try two different trial functions, the one that gives the lower energy is objectively the better approximation. Energy becomes a score function, and minimizing it systematically improves your wave function.

In practice, you construct a **trial wave function** with adjustable parameters — for example, ψ(r) = e^(−αr) for a hydrogen-like atom, where α controls how tightly the electron is held near the nucleus. You then compute the energy as a function of α, take the derivative, set it to zero, and solve for the optimal α. For hydrogen, this procedure recovers the exact answer (α = 1 in atomic units, E = −13.6 eV), confirming the method works. For helium, where the exact solution is unknown, you might try ψ(r₁, r₂) = e^(−α(r₁ + r₂)) and find that the optimal α gives an energy within about 2% of experiment — remarkable for such a simple one-parameter function. Adding more parameters (or more flexible functional forms like linear combinations of Gaussians) systematically drives the energy closer to the true value.

This principle underlies nearly all of computational quantum chemistry. The **Hartree-Fock method** uses the variational principle to optimize a wave function built from one-electron orbitals. **Density functional theory** applies variational ideas to the electron density rather than the wave function. **Configuration interaction** expands the trial function in a basis of many-electron configurations and variationally optimizes the expansion coefficients. In every case, the logic is the same: propose a parameterized form, minimize the energy, and trust that lower energy means a better approximation. The variational method converts the unsolvable differential equation into an optimization problem — something computers handle extremely well.
