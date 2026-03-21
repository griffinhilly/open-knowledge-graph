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

## Questions

```yaml
- question: "A student computes the energy of trial wave function ψ_A and gets −13.2 eV. A second student uses a different trial function ψ_B and gets −13.8 eV. The true ground state energy is −13.6 eV. What can you conclude?"
  type: multiple-choice
  options:
    - "ψ_B violates the variational principle because its energy is below the true ground state"
    - "ψ_A is the better approximation because it is closer to zero"
    - "ψ_B is the better approximation because it gives a lower energy, even though it is below the true value"
    - "Neither result is valid; both should be recomputed with larger basis sets"
  answer: 2
  explanation: "The variational principle guarantees that for any trial wave function, the calculated energy is ≥ E₀. Here E₀ = −13.6 eV, so any valid result must be at or above −13.6 eV. ψ_A gives −13.2 eV (above E₀, valid upper bound) and ψ_B gives −13.8 eV — which is BELOW the true ground state energy. This means either ψ_B is not properly normalized, or a computational error occurred. Option C would be correct only if both results were valid upper bounds; since −13.8 eV is below the true energy, ψ_B has violated the theorem. The lower result is not automatically better — it signals an error."

- question: "A researcher adds a second adjustable parameter to a trial wave function and re-minimizes the energy. How does this affect the result?"
  type: multiple-choice
  options:
    - "It may raise or lower the energy — adding parameters makes the result less predictable"
    - "It will leave the energy unchanged, since one parameter is already sufficient"
    - "It can only lower (or maintain) the energy, since a more flexible function can always do at least as well"
    - "It will raise the energy, because more parameters introduce additional approximation error"
  answer: 2
  explanation: "A two-parameter trial function includes all one-parameter trial functions as special cases (by setting the new parameter to a fixed value). Therefore, the best two-parameter energy is at least as low as the best one-parameter energy — it can only improve or stay the same. This is the logic behind systematic improvement in computational chemistry: Hartree-Fock → configuration interaction → full CI, each step adding flexibility and driving the energy closer to the exact value. Adding parameters never makes the variational result worse."

- question: "The variational principle guarantees that optimizing a trial wave function will eventually yield the exact ground state energy if enough parameters are added."
  type: true-false
  answer: true
  explanation: "If the trial wave function form is flexible enough — in the limit, a complete basis set of functions — then optimization will converge to the exact ground state energy and wave function. This is the conceptual basis of full configuration interaction (FCI), which uses a complete many-electron basis and gives the exact result within the chosen one-electron basis. In practice, the exact limit is only approached asymptotically, but the principle guarantees that more flexibility always yields a lower (better) energy."

- question: "The variational method can determine the exact energy of excited states just as reliably as it determines the ground state energy."
  type: true-false
  answer: false
  explanation: "The standard variational principle only guarantees an upper bound to the GROUND STATE energy. For excited states, an unconstrained trial function will simply collapse toward the ground state during optimization. Excited states require special treatment: either enforcing orthogonality to all lower states (which is hard in practice) or using variational methods specifically designed for excited states (like the linear variation method applied within a constrained subspace). This limitation is a significant reason why ground-state methods like Hartree-Fock and DFT dominated computational chemistry before excited-state extensions were developed."

- question: "Why does the variational principle transform the quantum mechanical problem from an unsolvable differential equation into an optimization problem, and why is this useful?"
  type: short-answer
  answer: "The variational principle shows that the energy of any trial wave function is always ≥ the true ground state energy, with equality only when the trial function is exact. This means you can parameterize a trial function, compute the energy as a function of those parameters, and minimize it — without ever solving the Schrödinger equation. The minimum energy found is the best approximation available with that functional form. This is useful because optimization problems (find the minimum of E(α, β, ...)) are computationally tractable even when the differential equation is not."
  explanation: "The key insight is that 'lower energy = better approximation' is not just a heuristic — it is a mathematical guarantee. This converts an impossible analytical problem (solving the many-electron Schrödinger equation) into a tractable numerical one (minimizing a function). Virtually all of computational quantum chemistry — Hartree-Fock, DFT, coupled cluster — rests on this foundation."
```

## Explainer

From your quantum chemistry foundations, you know that the Schrödinger equation gives exact solutions only for a handful of simple systems — the hydrogen atom, the harmonic oscillator, the particle in a box. For virtually every real molecule, the equation cannot be solved exactly because electron-electron repulsion makes the mathematics intractable. The variational method provides a rigorous way to get approximate answers that are guaranteed to be useful: you guess a wave function, compute the energy, and know with certainty that your answer is an upper bound to the true ground state energy.

The **variational theorem** states that for any normalized trial wave function |ψ_trial⟩, the expectation value of the Hamiltonian satisfies ⟨ψ_trial|H|ψ_trial⟩ ≥ E₀, where E₀ is the exact ground state energy. The proof is elegant: expand the trial function in the basis of exact eigenstates, and because every eigenstate has energy ≥ E₀, any weighted average of those energies must also be ≥ E₀. This inequality is not an approximation or a hope — it is a mathematical fact. It means that if you try two different trial functions, the one that gives the lower energy is objectively the better approximation. Energy becomes a score function, and minimizing it systematically improves your wave function.

In practice, you construct a **trial wave function** with adjustable parameters — for example, ψ(r) = e^(−αr) for a hydrogen-like atom, where α controls how tightly the electron is held near the nucleus. You then compute the energy as a function of α, take the derivative, set it to zero, and solve for the optimal α. For hydrogen, this procedure recovers the exact answer (α = 1 in atomic units, E = −13.6 eV), confirming the method works. For helium, where the exact solution is unknown, you might try ψ(r₁, r₂) = e^(−α(r₁ + r₂)) and find that the optimal α gives an energy within about 2% of experiment — remarkable for such a simple one-parameter function. Adding more parameters (or more flexible functional forms like linear combinations of Gaussians) systematically drives the energy closer to the true value.

This principle underlies nearly all of computational quantum chemistry. The **Hartree-Fock method** uses the variational principle to optimize a wave function built from one-electron orbitals. **Density functional theory** applies variational ideas to the electron density rather than the wave function. **Configuration interaction** expands the trial function in a basis of many-electron configurations and variationally optimizes the expansion coefficients. In every case, the logic is the same: propose a parameterized form, minimize the energy, and trust that lower energy means a better approximation. The variational method converts the unsolvable differential equation into an optimization problem — something computers handle extremely well.
