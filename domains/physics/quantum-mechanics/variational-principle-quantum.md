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
stage: advanced
status: validated
---

# The Variational Principle in Quantum Mechanics

## Core Idea
For any normalized |ψ⟩, ⟨ψ|Ĥ|ψ⟩ ≥ E₀ (ground state energy). Minimizing over trial wavefunctions estimates E₀ without solving Schrödinger's equation exactly.

## Questions

```yaml
- question: "A physicist uses a trial wavefunction to estimate the ground state energy of helium and obtains E_trial = −77.5 eV. The true ground state energy is E₀ = −79.0 eV. What does the variational principle say about this result?"
  type: multiple-choice
  options:
    - "The result is invalid because it differs from the true answer by more than 1%."
    - "E_trial > E₀, which is consistent with the variational principle — the trial wavefunction gives an upper bound, not the exact answer."
    - "The variational principle has been violated because the true energy is lower than the computed value."
    - "The trial wavefunction is close enough that further optimization is unnecessary."
  answer: 1
  explanation: "The variational principle states ⟨ψ|Ĥ|ψ⟩ ≥ E₀ for any normalized ψ. Here E_trial = −77.5 eV > −79.0 eV = E₀, which is exactly what the principle requires. The result is a valid upper bound — the true ground state energy is lower (more negative) than the trial estimate. This is not a violation; it is the expected behavior. The physicist should try to improve the trial wavefunction to bring E_trial closer to E₀ from above."

- question: "Why is the variational method particularly powerful for many-electron systems like molecules, where exact solutions are impossible?"
  type: multiple-choice
  options:
    - "It provides exact analytic solutions to the Schrödinger equation for any system with more than two electrons."
    - "It replaces the eigenvalue problem (finding E₀ exactly, which is often intractable) with an optimization problem that can be systematically improved by enriching the trial wavefunction family."
    - "It works only for ground states and is not applicable to excited states or molecular systems."
    - "It requires knowing the true ground state energy E₀ first, using it as a reference for the optimization."
  answer: 1
  explanation: "The Schrödinger equation for many-electron systems cannot be solved exactly because of electron-electron interactions. The variational method bypasses this: instead of solving an eigenvalue problem, parameterize trial wavefunctions and minimize ⟨Ĥ⟩ over the parameter space. The resulting minimum is a rigorous upper bound on E₀. By choosing richer trial families (more parameters, more flexible forms), you get tighter bounds — systematically improvable without ever solving the full problem exactly."

- question: "For any normalized quantum state |ψ⟩ that is not the true ground state, the expectation value ⟨ψ|Ĥ|ψ⟩ is strictly greater than the ground state energy E₀."
  type: true-false
  answer: true
  explanation: "The proof shows ⟨ψ|Ĥ|ψ⟩ = Σ_n |c_n|² E_n ≥ Σ_n |c_n|² E₀ = E₀, with equality only when all weight is on the ground state (c_n = 0 for all n ≠ 0). If |ψ⟩ is not the ground state, it has nonzero weight on at least one excited state with E_n > E₀, which raises the expectation value strictly above E₀. This strict inequality is what makes the variational method useful: you know the minimum you find is above E₀, and equality means you've found it exactly."

- question: "A variational calculation that produces a lower energy than a previous trial wavefunction has necessarily found a better approximation to the ground state."
  type: true-false
  answer: false
  explanation: "Lower is better — up to a point. A lower E_trial is a tighter upper bound on E₀, which means the new trial wavefunction has higher overlap with the true ground state. However, if E_trial somehow came out *lower* than the true E₀, that would indicate a normalization error or a bug in the calculation, since the variational principle guarantees E_trial ≥ E₀. So 'lower' is only better within the allowed range — any result below E₀ is physically impossible and signals an error, not an improvement. The statement is false because it ignores this crucial floor."

- question: "Why does the variational principle guarantee an upper bound — rather than a lower bound — on the ground state energy?"
  type: short-answer
  answer: "Because the expectation value ⟨ψ|Ĥ|ψ⟩ is a weighted average of energy eigenvalues, with weights |c_n|² summing to 1. Since E₀ is the *minimum* energy eigenvalue, every term in the sum is ≥ E₀, and the weighted average is therefore ≥ E₀. You can never accidentally compute a weighted average that falls below the smallest value being averaged. Equality holds only when all weight is on the ground state eigenfunction itself."
  explanation: "The upper-bound property is what makes the method constructive: you can minimize over trial states knowing your minimum is above the truth. This lets you rank trial wavefunctions by quality (lower energy = better approximation) and systematically improve. A lower-bound principle would require knowing the true answer first, which defeats the purpose. The variational principle's one-sidedness — you can only approach E₀ from above — is both a constraint and a feature."
```

## Explainer

From your study of observables and operators, you know that the expectation value of the Hamiltonian in state |ψ⟩ is ⟨ψ|Ĥ|ψ⟩, and that this equals the average energy you would measure. The variational principle adds one crucial theorem: this expectation value is *always* at least as large as the ground state energy E₀, for *any* normalized state |ψ⟩ you choose.

The proof is elegant and short. Expand |ψ⟩ in the energy eigenbasis: |ψ⟩ = Σ_n c_n |n⟩ with Σ_n |c_n|² = 1. Then ⟨ψ|Ĥ|ψ⟩ = Σ_n |c_n|² E_n ≥ Σ_n |c_n|² E₀ = E₀. The inequality holds because every E_n ≥ E₀ by definition of the ground state. Equality holds if and only if |ψ⟩ = |0⟩ (the true ground state). So ⟨Ĥ⟩ is a **rigorous upper bound** on E₀: you can never accidentally compute a value lower than the true ground state energy, no matter what trial state you use.

This turns the problem of finding E₀ into an optimization problem. Choose a family of **trial wavefunctions** |ψ(α)⟩ parameterized by some numbers α (maybe the width of a Gaussian, the exponent in a hydrogen-like orbital, or a set of variational coefficients). Compute E(α) = ⟨ψ(α)|Ĥ|ψ(α)⟩ and minimize over α. The minimum you find is guaranteed to be ≥ E₀, and a good trial family will bring it close. The art of the method is choosing a trial family rich enough to approximate the true ground state without being so complicated that the integrals become intractable. For the hydrogen atom, a trial function ψ(r) ∝ e^{−αr} with one variational parameter α gives the exact ground state — because the true ground state happens to be in that family. For helium, the same form with independent exponents for each electron gives ∼2% error without solving any differential equations.

The variational principle is the foundation of much of computational quantum chemistry and condensed matter physics. **Hartree-Fock theory** parameterizes the wavefunction as a Slater determinant (antisymmetrized product of single-particle orbitals) and minimizes the energy over all such determinants — this is a variational calculation with a structured trial family. **Density functional theory** (Hohenberg-Kohn theorem) rests on the same principle applied to the electron density. Even quantum Monte Carlo methods use variational optimization of explicitly correlated wavefunctions. The principle is powerful precisely because it converts an eigenvalue problem (hard, often impossible exactly) into a minimization problem (tractable, systematically improvable).
