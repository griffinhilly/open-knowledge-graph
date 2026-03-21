---
id: variational-principle-chemistry
title: The Variational Principle and Trial Wavefunctions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hydrogen-atom-wavefunctions
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: schrodinger-equation-intro
  type: soft
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- molecular-orbital-theory-advanced
- huckel-molecular-orbital-theory
tags:
- variational
- ground-state
- approximate-methods
- helium
stage: advanced
status: validated
---

# The Variational Principle and Trial Wavefunctions

## Core Idea
The variational principle states that for any trial wavefunction φ, the expectation value of the energy ⟨φ|Ĥ|φ⟩/⟨φ|φ⟩ is always greater than or equal to the true ground-state energy E₀. This gives a systematic way to improve approximate wavefunctions by minimizing the energy with respect to variational parameters. The secular determinant |H − ES| = 0, obtained by expanding the trial function in a basis set, reduces the problem to matrix diagonalization. This principle underpins Hartree-Fock theory, DFT, and all basis-set electronic structure methods.

## How It's Best Learned
Apply the variational method to helium as a first example, using a screened hydrogenic wavefunction with the screening constant as the variational parameter. Observe how minimizing energy gives the optimal screening constant.

## Common Misconceptions
- Thinking the variational principle gives the exact energy — it gives an upper bound; the true energy is lower or equal.
- Forgetting that the principle applies only to the ground state (with exceptions for excited states of different symmetry).

## Questions

```yaml
- question: "You apply the variational method to helium using two different trial wavefunctions. Trial A gives an energy of −77.5 eV, and Trial B gives −79.0 eV. What can you conclude?"
  type: multiple-choice
  options:
    - "Trial A is a better approximation because it gives a higher energy"
    - "Trial B is a better approximation because it gives a lower energy, closer to the true ground state"
    - "Trial B must give the exact ground-state energy since it is the lower value"
    - "Neither can be a valid approximation because both may be below the exact energy"
  answer: 1
  explanation: "The variational principle guarantees that both trial energies are upper bounds on the true ground-state energy. A lower energy means the trial wavefunction is closer to the true ground state — so Trial B is the better approximation. However, the true energy could still be lower than −79.0 eV, so Trial B need not be exact. Option C confuses 'closer to' with 'equal to' the true energy."

- question: "A chemist introduces an additional variational parameter into a trial wavefunction for a molecule. After re-optimization, the energy is identical to before. What does this indicate?"
  type: multiple-choice
  options:
    - "The variational method has broken down and the result is unreliable"
    - "The additional parameter is redundant — the original trial function already captured everything the new parameter could improve"
    - "The true ground-state energy has been reached exactly"
    - "The new parameter was incorrectly defined and the calculation must be redone"
  answer: 1
  explanation: "The variational principle guarantees energies can only decrease (or stay the same) as you add more flexibility to the trial function. If adding a parameter doesn't change the energy, the original trial function already captured whatever improvement was possible in that direction. It does NOT mean the exact energy has been reached — there may still be a gap to the true energy that this type of parameter cannot bridge."

- question: "The variational principle states that the energy calculated from any trial wavefunction is always less than or equal to the true ground-state energy."
  type: true-false
  answer: false
  explanation: "This reverses the inequality. The variational principle states that the expectation value of the energy for any trial wavefunction is always GREATER THAN OR EQUAL TO the true ground-state energy. The true ground state is a lower bound that no trial function can beat — every approximate wavefunction overshoots. Improving the trial function brings the energy down toward the true value, but always from above."

- question: "Expanding a trial wavefunction as a linear combination of basis functions and minimizing the energy with respect to the coefficients leads to a matrix eigenvalue problem."
  type: true-false
  answer: true
  explanation: "When the trial function is φ = Σ cᵢχᵢ, minimizing the energy with respect to the coefficients leads to the secular equation |H − ES| = 0, where H and S are the Hamiltonian and overlap matrices. Solving this eigenvalue equation gives the variational energies as eigenvalues and the optimal coefficients as eigenvectors. This connection to linear algebra is what makes the variational method computationally tractable for large molecular systems."

- question: "Why can the variational principle transform the problem of solving the many-electron Schrödinger equation into an optimization problem?"
  type: short-answer
  answer: "The variational principle guarantees that the energy expectation value of any trial wavefunction is an upper bound on the true ground-state energy. This means 'lower energy = better wavefunction,' so you can improve your approximation by minimizing the energy with respect to adjustable parameters. The intractable task of solving a multi-body differential equation becomes the tractable task of minimizing a function — and the minimum is always pushing toward, not past, the correct answer."
  explanation: "The key is the one-way guarantee: since trial energies can only be too high, minimization is a reliable guide toward the truth. Without this guarantee, minimizing would have no physical meaning. The principle converts a problem with no known exact solution into a systematic approximation where each step provably improves the result."
```

## Explainer

From solving the Schrödinger equation for the hydrogen atom, you know that exact analytical solutions exist for one-electron systems. But the moment you add a second electron — even for helium, the simplest multi-electron atom — the electron-electron repulsion term makes the equation analytically unsolvable. The variational principle provides a way forward: it turns the problem of solving a differential equation into the more tractable problem of *minimizing a function*. The principle states that for any normalized trial wavefunction φ you can write down, the expectation value of the energy ⟨φ|Ĥ|φ⟩ is guaranteed to be greater than or equal to the true ground-state energy E₀. This means the exact ground-state energy is a **lower bound** that no trial function can beat — every guess overshoots.

This guarantee converts quantum mechanics into an optimization problem. You propose a trial wavefunction with adjustable parameters — say, a hydrogen-like wavefunction for helium but with the nuclear charge Z replaced by an effective charge Z_eff that accounts for electron shielding. Then you compute the energy as a function of Z_eff and minimize. The resulting Z_eff ≈ 1.69 (rather than the bare nuclear charge of 2) captures the physical reality that each electron partially screens the nucleus from the other. The energy you obtain is remarkably close to the experimental value — within about 2% — from a single-parameter optimization. More parameters and more flexible trial functions systematically push the energy closer to the true value, and the variational principle guarantees you are always approaching from above.

The method becomes even more powerful when you expand the trial wavefunction as a **linear combination of basis functions**: φ = c₁χ₁ + c₂χ₂ + ... + c_Nχ_N. Now the variational parameters are the coefficients c_i. Minimizing the energy with respect to all coefficients leads to the **secular equation** |H − ES| = 0, where H is the matrix of Hamiltonian integrals H_ij = ⟨χᵢ|Ĥ|χⱼ⟩ and S is the overlap matrix S_ij = ⟨χᵢ|χⱼ⟩. This is an eigenvalue problem — a connection to the linear algebra you have studied. Diagonalizing the matrix gives you the best approximation to the ground-state energy (the lowest eigenvalue) and its wavefunction (the corresponding eigenvector), plus approximations to excited states as the higher eigenvalues.

This framework is the foundation of essentially all modern computational chemistry. Hartree-Fock theory uses the variational principle to find the best single-determinant wavefunction. Density functional theory, basis-set methods, and configuration interaction all rest on the same idea: propose a flexible functional form, compute the energy, and minimize. The variational principle is what makes these methods trustworthy — because the energy can only go down as you improve the trial function, you always know which direction "better" is. It transforms the intractable many-body Schrödinger equation into a systematic, improvable approximation scheme.
