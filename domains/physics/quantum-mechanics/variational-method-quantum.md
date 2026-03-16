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
stage: formal-systems
status: draft
---

# The Variational Method: Application

## Core Idea
Parameterize trial wavefunction ψ(α, β, ...) and compute ⟨H⟩; minimize by ∂⟨H⟩/∂α = 0. Widely used in quantum chemistry (Hartree-Fock) and condensed matter.

## Explainer

The variational principle established in your prerequisite tells you something profound: the expectation value of the Hamiltonian in any trial state is always an upper bound on the true ground-state energy E₀. Formally, ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀ for any normalized |ψ_trial⟩. The variational method turns this bound into a practical algorithm: introduce free parameters into your trial wavefunction, compute ⟨H⟩ as a function of those parameters, and minimize over them. The resulting minimum is the best approximation to E₀ achievable within your chosen functional family — and you are guaranteed never to overshoot below the true ground state.

The procedure is systematic. Choose a **trial wavefunction** ψ(r; α, β, ...) parameterized by one or more variational parameters. Compute the variational energy E(α, β, ...) = ⟨ψ|Ĥ|ψ⟩/⟨ψ|ψ⟩ (the denominator normalizes ψ if it is not already normalized). Then solve ∂E/∂α = 0, ∂E/∂β = 0, ... simultaneously. The solution parameters minimize ⟨H⟩ and yield the best approximate ground-state energy within the trial family. The quality of the answer depends entirely on the trial family: if the true ground state is in it, you find it exactly; if not, you find the closest approach the family allows.

A worked example illustrates both the power and the limits. For the hydrogen atom, the true ground state is ψ(r) ∝ exp(−r/a₀). Using a one-parameter Gaussian trial ψ(r; α) = exp(−αr²) — which is not in the true family — computing ⟨T⟩ + ⟨V⟩, minimizing over α, and evaluating gives E ≈ −11.5 eV compared to the exact −13.6 eV. The 15% error is the price of the wrong functional form. If instead you try ψ(r; α) = exp(−αr), the true ground state is in this family (at α = 1/a₀), and minimizing recovers the exact answer. The lesson: expanding your trial family — more parameters, more flexible functions — always lowers the variational energy toward E₀.

The variational method is indispensable in quantum chemistry and condensed matter precisely because exact solutions are unavailable for multi-electron systems. The **Hartree-Fock method** is variational: it optimizes a Slater determinant (antisymmetric product of single-particle orbitals) and returns the best mean-field ground-state energy. Modern **density functional theory** (DFT) is variational in spirit — it minimizes an energy functional over electron densities. In both cases, the guarantee that ⟨H⟩ ≥ E₀ provides a systematic quality check: lower variational energy is always better, and comparing results from different trial families is a reliable way to rank approximation quality. The variational method thus transforms an intractable eigenvalue problem into an optimization problem — and optimization is something both humans and computers are very good at.
