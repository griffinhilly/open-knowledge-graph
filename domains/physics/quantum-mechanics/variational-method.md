---
id: variational-method
title: Variational Method
domain: physics
course: quantum-mechanics
prerequisites:
- id: expectation-values
  type: hard
- id: calculus-of-variations
  type: hard
tags:
- approximation-methods
- variational
stage: abstract-reasoning
status: draft
---

# Variational Method

## Core Idea
The variational method states that for any trial state |ψ(α)⟩: ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ ≥ E₀. Minimizing over variational parameters α gives an upper bound on ground state energy, useful when exact solutions are impossible.

## Explainer

From your study of expectation values you know that ⟨H⟩ = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ gives the average energy you would find if you measured the energy of a system in state |ψ⟩ many times. The **variational theorem** turns this into a powerful approximation tool: for *any* state |ψ⟩, the expectation value of H is always greater than or equal to the true ground state energy E₀. This follows directly from expanding |ψ⟩ in the energy eigenbasis — every term in the sum is weighted by a coefficient squared (non-negative) multiplied by an energy eigenvalue that is at least E₀. The bound is saturated only if |ψ⟩ is exactly the ground state.

The practical procedure builds on your calculus of variations background. You choose a **trial wavefunction** ψ(r; α, β, ...) that has a physically reasonable shape and contains free parameters. You then compute the energy functional E(α, β, ...) = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ analytically or numerically, and minimize it over the parameters. The minimum you find is guaranteed to be an upper bound on E₀, and if your trial function has good shape, it will be a tight one. The art of the variational method lies in choosing a trial function that captures the essential physics with as few parameters as possible.

A concrete example: for the hydrogen atom ground state you know the exact answer is −13.6 eV. Suppose instead you try a Gaussian trial function ψ(r; α) = e^{−αr²}. Compute ⟨T⟩ and ⟨V⟩, differentiate E(α) with respect to α, set to zero, and you recover an energy only about 15% above the true ground state. Use a better trial function — say, e^{−αr} with the correct exponential decay — and the variational minimum gives the *exact* answer, because the exact ground state is in that family. The method is self-correcting: a better guess never makes the bound worse.

The variational method extends naturally to excited states and multi-particle systems. For excited states, if you restrict your trial function to be orthogonal to all lower eigenstates, the variational bound then applies to the next energy level. For many-electron atoms and molecules, the trial function becomes a multi-parameter construct (e.g., a Slater determinant of single-particle orbitals), and optimizing all parameters simultaneously is the foundation of **Hartree-Fock theory** and modern quantum chemistry. The variational principle is ultimately what makes these methods systematically improvable: more flexible trial functions give lower (better) energy estimates, and you always know you are approaching from above.
