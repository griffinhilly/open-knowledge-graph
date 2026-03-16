---
id: quantum-observables
title: Observables and Hermitian Operators
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-operators
  type: hard
- id: eigenvalues-eigenstates-quantum
  type: hard
builds-toward:
- commutation-relations
- uncertainty-principle-canonical
tags:
- observables
- hermitian
- measurement
stage: advanced
status: draft
---

# Observables and Hermitian Operators

## Core Idea
Observables in quantum mechanics are represented by Hermitian (self-adjoint) operators Â = Â†. Hermitian operators guarantee real eigenvalues consistent with measurement outcomes and orthogonal eigenstates enabling complete descriptions. Examples include the Hamiltonian (energy), momentum, and angular momentum operators.

## Explainer

When you study quantum operators and eigenvalues, you learn that a quantum state can be expressed as a superposition of eigenstates of any operator. But not every operator deserves to represent a physical measurement — only a special class called **Hermitian operators** (also called self-adjoint operators) do. The defining property is Â = Â†, meaning the operator equals its own conjugate transpose. This seemingly abstract condition has concrete physical consequences that make it indispensable.

The first consequence is that Hermitian operators have **real eigenvalues**. This is essential: when you measure a physical quantity, the result must be a real number (you can't get an imaginary position or energy). For a Hermitian operator, if Â|aₙ⟩ = aₙ|aₙ⟩, then aₙ must be real. The proof is a one-line calculation using the Hermitian property: aₙ = ⟨aₙ|Â|aₙ⟩ = ⟨Â†aₙ|aₙ⟩ = aₙ*, which forces aₙ = aₙ*. No other class of operators guarantees this.

The second consequence is **orthogonality of eigenstates**. If two eigenstates |aₙ⟩ and |aₘ⟩ have different eigenvalues (aₙ ≠ aₘ), then ⟨aₙ|aₘ⟩ = 0. This lets you write any state as a complete sum of orthogonal basis states — the eigenstates of the observable form a complete orthonormal basis for the Hilbert space. The Born rule then says that if the system is in state |ψ⟩ and you measure observable Â, the probability of getting result aₙ is |⟨aₙ|ψ⟩|². The measurement collapses |ψ⟩ to |aₙ⟩. Without orthogonality of eigenstates, these probabilities wouldn't sum to 1 and the statistical interpretation would collapse.

The physical examples make the structure concrete. The Hamiltonian Ĥ is Hermitian, so energy eigenvalues are real — no surprise. The momentum operator p̂ = −iℏ∂/∂x is Hermitian on appropriately defined function spaces, with real eigenvalues p. The position operator x̂ is multiplication by x, trivially Hermitian. Non-Hermitian combinations — like the raising operator â† alone — do not represent observables; you can't measure it directly. When you later study commutation relations and the uncertainty principle, you'll see that two observables can be simultaneously measured only when their operators commute, which brings together eigenvalues, eigenstates, and measurement in a unified framework.
