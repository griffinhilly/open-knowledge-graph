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
stage: advanced
status: validated
---

# Variational Method

## Core Idea
The variational method states that for any trial state |ψ(α)⟩: ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ ≥ E₀. Minimizing over variational parameters α gives an upper bound on ground state energy, useful when exact solutions are impossible.

## Questions

```yaml
- question: "You apply the variational method with a Gaussian trial function to the hydrogen atom and obtain an energy estimate of −11.5 eV. The true ground state energy is −13.6 eV. What does this tell you?"
  type: multiple-choice
  options:
    - "You made a computational error — a correctly applied variational method should give the exact ground state energy"
    - "The result is a valid upper bound: −11.5 eV > −13.6 eV, consistent with the variational theorem"
    - "The variational method underestimated the true energy, which is expected since it approaches from below"
    - "The Gaussian is a poor trial function and you should use a lower energy estimate from a different method"
  answer: 1
  explanation: "The variational theorem guarantees ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ ≥ E₀ for any trial state. −11.5 eV > −13.6 eV is exactly what the theorem predicts — an upper bound that is above (less negative than) the true ground state. Option C reverses the direction: the variational method always approaches the ground state from ABOVE. A more flexible trial function would give a tighter (more negative) upper bound, but it can never go below E₀."

- question: "Why can't the variational method ever yield an energy estimate below the true ground state energy?"
  type: multiple-choice
  options:
    - "Because trial wavefunctions are always normalized, and normalization constrains the energy to be positive"
    - "Because any state expanded in energy eigenstates has all eigenvalue contributions ≥ E₀, so the expectation value — a weighted average of eigenvalues — must also be ≥ E₀"
    - "Because the minimization procedure always converges to the global minimum, which is E₀"
    - "Because the calculus of variations guarantees stationary points are minima, not maxima or saddle points"
  answer: 1
  explanation: "Write |ψ⟩ = Σcₙ|Eₙ⟩. Then ⟨H⟩ = Σ|cₙ|²Eₙ. Since each Eₙ ≥ E₀ and Σ|cₙ|² = 1, this is a weighted average of quantities each at least E₀ — so ⟨H⟩ ≥ E₀. The bound is saturated only when cₙ = 0 for all n > 0, i.e., when |ψ⟩ is exactly the ground state. No choice of parameters in the trial function can make this weighted average go below E₀."

- question: "Adding more variational parameters to a trial function can only lower or preserve the variational energy estimate — it can never raise it."
  type: true-false
  answer: true
  explanation: "True. A trial function with more parameters spans a larger family of states. The minimum over a larger family is always less than or equal to the minimum over a smaller subfamily (since the smaller family is a subset). So adding parameters gives access to states that were previously unavailable, potentially achieving a lower ⟨H⟩, but never forcing ⟨H⟩ to be higher than it was with fewer parameters. This is why the variational method is systematically improvable."

- question: "The variational method can give an energy estimate below the true ground state energy if the trial wavefunction is chosen to have the correct symmetry and nodal structure."
  type: true-false
  answer: false
  explanation: "False. The variational theorem holds for any trial state, regardless of its symmetry or nodal structure. ⟨H⟩ ≥ E₀ always. Symmetry and nodal structure matter for the quality of the upper bound (how close it is to E₀) and for targeting excited states, but they cannot cause the bound to be violated. No cleverness in choosing the trial function can push the estimate below the true ground state energy."

- question: "Explain why minimizing the energy expectation value over variational parameters always gives an upper bound on the ground state energy. Why is this one-sided guarantee useful in practice?"
  type: short-answer
  answer: "The proof follows from expanding the trial state in energy eigenstates: |ψ⟩ = Σcₙ|Eₙ⟩, so ⟨H⟩ = Σ|cₙ|²Eₙ. This is a weighted average of eigenvalues, all of which are ≥ E₀ (the ground state energy is by definition the minimum eigenvalue). A weighted average of quantities each ≥ E₀ is itself ≥ E₀. The bound is tight only when |ψ⟩ = |E₀⟩ exactly. The one-sided guarantee is useful because it makes the method systematically improvable: a better trial function gives a lower (tighter) upper bound, and you always know you are approaching the true answer from above. You can therefore compare competing trial functions by their variational energies — lower is always better — and you know you have not accidentally gone below the true answer."
  explanation: "The practical power is that for systems where exact solutions are impossible (most multi-electron atoms, all molecules beyond H₂⁺), the variational principle gives a controlled approximation: you know the sign of your error and can reduce it by increasing the flexibility of the trial function. This is the foundation of Hartree-Fock theory and all of modern quantum chemistry: larger basis sets lower the variational energy toward the exact answer."
```

## Explainer

From your study of expectation values you know that ⟨H⟩ = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ gives the average energy you would find if you measured the energy of a system in state |ψ⟩ many times. The **variational theorem** turns this into a powerful approximation tool: for *any* state |ψ⟩, the expectation value of H is always greater than or equal to the true ground state energy E₀. This follows directly from expanding |ψ⟩ in the energy eigenbasis — every term in the sum is weighted by a coefficient squared (non-negative) multiplied by an energy eigenvalue that is at least E₀. The bound is saturated only if |ψ⟩ is exactly the ground state.

The practical procedure builds on your calculus of variations background. You choose a **trial wavefunction** ψ(r; α, β, ...) that has a physically reasonable shape and contains free parameters. You then compute the energy functional E(α, β, ...) = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ analytically or numerically, and minimize it over the parameters. The minimum you find is guaranteed to be an upper bound on E₀, and if your trial function has good shape, it will be a tight one. The art of the variational method lies in choosing a trial function that captures the essential physics with as few parameters as possible.

A concrete example: for the hydrogen atom ground state you know the exact answer is −13.6 eV. Suppose instead you try a Gaussian trial function ψ(r; α) = e^{−αr²}. Compute ⟨T⟩ and ⟨V⟩, differentiate E(α) with respect to α, set to zero, and you recover an energy only about 15% above the true ground state. Use a better trial function — say, e^{−αr} with the correct exponential decay — and the variational minimum gives the *exact* answer, because the exact ground state is in that family. The method is self-correcting: a better guess never makes the bound worse.

The variational method extends naturally to excited states and multi-particle systems. For excited states, if you restrict your trial function to be orthogonal to all lower eigenstates, the variational bound then applies to the next energy level. For many-electron atoms and molecules, the trial function becomes a multi-parameter construct (e.g., a Slater determinant of single-particle orbitals), and optimizing all parameters simultaneously is the foundation of **Hartree-Fock theory** and modern quantum chemistry. The variational principle is ultimately what makes these methods systematically improvable: more flexible trial functions give lower (better) energy estimates, and you always know you are approaching from above.
