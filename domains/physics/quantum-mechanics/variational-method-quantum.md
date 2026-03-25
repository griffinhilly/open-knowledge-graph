---
id: variational-method-quantum
title: 'The Variational Method: Application'
domain: physics
course: quantum-mechanics
prerequisites:
- id: variational-principle-quantum
  type: hard
tags:
- variational-methods
- approximations
stage: advanced
status: validated
---

# The Variational Method: Application

## Core Idea
Parameterize trial wavefunction ψ(α, β, ...) and compute ⟨H⟩; minimize by ∂⟨H⟩/∂α = 0. Widely used in quantum chemistry (Hartree-Fock) and condensed matter.

## Questions

```yaml
- question: "A physicist uses a Gaussian trial wavefunction for the hydrogen atom and obtains E_trial = −11.5 eV. The exact ground-state energy is −13.6 eV. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The calculation must contain an error — variational energies should converge to the exact answer"
    - "The Gaussian family does not contain the true ground state; −11.5 eV is the best approximation within that family, and the variational bound guarantees the true energy is at or below −11.5 eV"
    - "The true ground-state energy lies between −11.5 eV and −13.6 eV"
    - "The variational method has failed because the estimate is wrong by 15%"
  answer: 1
  explanation: "The variational principle guarantees ⟨H⟩ ≥ E₀ for any trial state. Getting −11.5 eV > −13.6 eV is not an error — it is the expected behavior when your trial family doesn't include the true ground state. The 15% error reflects the price of the wrong functional form (Gaussian vs. the true exponential). The bound tells us the exact energy is somewhere at or below −11.5 eV — and indeed, −13.6 eV < −11.5 eV, consistent with the bound. Option C confuses 'between' with 'below': the true energy is below the estimate, not between it and some other value."

- question: "What happens to the variational energy estimate when you add more free parameters to your trial wavefunction?"
  type: multiple-choice
  options:
    - "It can increase or decrease unpredictably, depending on how the parameters interact with the Hamiltonian"
    - "It increases — more parameters introduce more uncertainty in the approximation"
    - "It stays the same — variational energy depends only on the Hamiltonian, not the parameterization"
    - "It decreases (or stays the same) — a more flexible trial family includes more candidate states, so the minimum over parameters can only be at most as high as the previous best"
  answer: 3
  explanation: "Adding parameters expands the trial family. The new minimum is taken over a strictly larger set of states than before, so it can only be equal to or lower than the previous minimum — never higher. This is why 'more flexible trial function → tighter upper bound on E₀' is a reliable rule. A one-parameter family sits inside every two-parameter generalization of it (just fix one parameter at its previous optimal value). Therefore expanding the family never raises the variational energy."

- question: "If the true ground-state wavefunction is a member of the parameterized trial family, the variational method will recover the exact ground-state energy."
  type: true-false
  answer: true
  explanation: "The variational energy E(α, β, ...) = ⟨ψ(α,β,...)|Ĥ|ψ(α,β,...)⟩ achieves its minimum at E₀ when the minimization reaches the true ground state. If ψ_true is in the family (i.e., there exist parameter values that reproduce it exactly), then the minimum over parameters will find those values and return E₀. This is demonstrated by the hydrogen atom example: using exp(−αr) as the trial function includes the true ground state at α = 1/a₀, and the variational minimum recovers −13.6 eV exactly."

- question: "The variational method can yield an energy estimate lower than the true ground-state energy if the trial wavefunction is a poor approximation."
  type: true-false
  answer: false
  explanation: "This is categorically forbidden by the variational principle. For any normalized trial state |ψ_trial⟩, ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀. The proof: expand ψ_trial in the exact energy eigenbasis — the resulting expectation value is a weighted average of energies, all ≥ E₀, so the sum is ≥ E₀. No matter how bad the trial wavefunction is, ⟨H⟩ can never go below the true ground-state energy. This guarantee is the entire foundation of the variational method's reliability."

- question: "Why does the variational principle guarantee that ⟨H⟩ ≥ E₀ for any trial wavefunction? What does this guarantee imply about how to improve your estimate?"
  type: short-answer
  answer: "Expand the trial wavefunction in the exact energy eigenbasis: |ψ_trial⟩ = Σcₙ|n⟩. Then ⟨H⟩ = Σ|cₙ|²Eₙ. Since E₀ ≤ Eₙ for all n, and the |cₙ|² form a probability distribution summing to 1, ⟨H⟩ = Σ|cₙ|²Eₙ ≥ E₀Σ|cₙ|² = E₀. To improve: expand the trial family (add parameters or use more flexible functional forms) — the minimum over a larger family can only be lower, tightening the bound on E₀."
  explanation: "The guarantee means: (1) you can never accidentally undershoot the true ground-state energy, making the method safe from false negatives, and (2) 'lower variational energy is always better' is a rigorous statement, not just a heuristic. This turns the quantum mechanical problem (find the lowest eigenvalue of a complicated Hamiltonian) into an optimization problem (minimize a functional over a parameterized family), which computers are very good at."
```

## Explainer

The variational principle established in your prerequisite tells you something profound: the expectation value of the Hamiltonian in any trial state is always an upper bound on the true ground-state energy E₀. Formally, ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀ for any normalized |ψ_trial⟩. The variational method turns this bound into a practical algorithm: introduce free parameters into your trial wavefunction, compute ⟨H⟩ as a function of those parameters, and minimize over them. The resulting minimum is the best approximation to E₀ achievable within your chosen functional family — and you are guaranteed never to overshoot below the true ground state.

The procedure is systematic. Choose a **trial wavefunction** ψ(r; α, β, ...) parameterized by one or more variational parameters. Compute the variational energy E(α, β, ...) = ⟨ψ|Ĥ|ψ⟩/⟨ψ|ψ⟩ (the denominator normalizes ψ if it is not already normalized). Then solve ∂E/∂α = 0, ∂E/∂β = 0, ... simultaneously. The solution parameters minimize ⟨H⟩ and yield the best approximate ground-state energy within the trial family. The quality of the answer depends entirely on the trial family: if the true ground state is in it, you find it exactly; if not, you find the closest approach the family allows.

A worked example illustrates both the power and the limits. For the hydrogen atom, the true ground state is ψ(r) ∝ exp(−r/a₀). Using a one-parameter Gaussian trial ψ(r; α) = exp(−αr²) — which is not in the true family — computing ⟨T⟩ + ⟨V⟩, minimizing over α, and evaluating gives E ≈ −11.5 eV compared to the exact −13.6 eV. The 15% error is the price of the wrong functional form. If instead you try ψ(r; α) = exp(−αr), the true ground state is in this family (at α = 1/a₀), and minimizing recovers the exact answer. The lesson: expanding your trial family — more parameters, more flexible functions — always lowers the variational energy toward E₀.

The variational method is indispensable in quantum chemistry and condensed matter precisely because exact solutions are unavailable for multi-electron systems. The **Hartree-Fock method** is variational: it optimizes a Slater determinant (antisymmetric product of single-particle orbitals) and returns the best mean-field ground-state energy. Modern **density functional theory** (DFT) is variational in spirit — it minimizes an energy functional over electron densities. In both cases, the guarantee that ⟨H⟩ ≥ E₀ provides a systematic quality check: lower variational energy is always better, and comparing results from different trial families is a reliable way to rank approximation quality. The variational method thus transforms an intractable eigenvalue problem into an optimization problem — and optimization is something both humans and computers are very good at.
