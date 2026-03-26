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
status: validated
---

# Observables and Hermitian Operators

## Core Idea
Observables in quantum mechanics are represented by Hermitian (self-adjoint) operators Â = Â†. Hermitian operators guarantee real eigenvalues consistent with measurement outcomes and orthogonal eigenstates enabling complete descriptions. Examples include the Hamiltonian (energy), momentum, and angular momentum operators.

## Questions

```yaml
- question: "A student proposes using the operator (p̂ + ix̂) to represent a measurable physical quantity, where p̂ and x̂ are both Hermitian. Why is this operator unsuitable as an observable?"
  type: multiple-choice
  options:
    - "The combination of position and momentum operators violates the uncertainty principle by construction"
    - "(p̂ + ix̂) is not Hermitian — its conjugate transpose is (p̂ − ix̂) ≠ (p̂ + ix̂) — so its eigenvalues may be complex and cannot represent real measurement outcomes"
    - "Hermitian operators cannot be added or combined in quantum mechanics"
    - "The operator has no physical interpretation, so it fails on interpretive rather than mathematical grounds"
  answer: 1
  explanation: "The Hermitian condition Â = Â† is required for real eigenvalues. (p̂ + ix̂)† = p̂† + (ix̂)† = p̂ − ix̂ ≠ p̂ + ix̂. Since (p̂ + ix̂) ≠ (p̂ + ix̂)†, it is not Hermitian. Its eigenvalues can be complex numbers, which cannot represent physical measurement results. Note that p̂ alone and x̂ alone are individually Hermitian and valid observables — but forming the combination with a factor of i breaks the Hermitian property."

- question: "Why must the eigenstates of a Hermitian observable form an orthonormal basis for the Hilbert space?"
  type: multiple-choice
  options:
    - "Because quantum measurements must be repeatable, and repeatability requires eigenstates to be stable solutions"
    - "Because orthogonality ensures the Born-rule probabilities |⟨aₙ|ψ⟩|² sum to 1 for any normalized state |ψ⟩, preserving the probabilistic interpretation"
    - "Because the Schrödinger equation requires that energy eigenstates be mutually perpendicular"
    - "Because non-orthogonal eigenstates would violate the Heisenberg uncertainty principle"
  answer: 1
  explanation: "The probabilistic interpretation of quantum mechanics requires that measurement probabilities sum to 1. If the eigenstates of an observable form an orthonormal basis {|aₙ⟩}, then any state |ψ⟩ = Σ cₙ|aₙ⟩ with Σ|cₙ|² = 1, and the probabilities |⟨aₙ|ψ⟩|² = |cₙ|² sum to 1 automatically. If the eigenstates were not orthogonal, overlapping expansion coefficients would double-count probability, the sum could exceed 1, and the Born rule would be inconsistent. Hermitian operators guarantee orthogonality of eigenstates with distinct eigenvalues, which is exactly why they — and only they — can represent observables."

- question: "For a Hermitian operator Â, the calculation aₙ = ⟨aₙ|Â|aₙ⟩ = ⟨Â†aₙ|aₙ⟩ = aₙ* forces each eigenvalue aₙ to be real — this follows directly from the condition Â = Â†."
  type: true-false
  answer: true
  explanation: "This is the standard one-line proof. Starting with Â|aₙ⟩ = aₙ|aₙ⟩ and taking the inner product with ⟨aₙ|: aₙ = ⟨aₙ|Â|aₙ⟩. Using Â = Â†: ⟨aₙ|Â|aₙ⟩ = ⟨Â†aₙ|aₙ⟩ = ⟨aₙ|aₙ⟩* · aₙ* = aₙ*. So aₙ = aₙ*, which means aₙ is real. This proof works for any Hermitian operator on any Hilbert space — it is a consequence purely of Â = Â†, not of any particular physical system or operator."

- question: "The raising operator â† is a valid quantum mechanical observable for the harmonic oscillator, because it has well-defined, predictable action on nearly every energy eigenstate."
  type: true-false
  answer: false
  explanation: "â† is not Hermitian: (â†)† = â ≠ â†. Therefore it is not an observable — you cannot measure it directly. Although â† has well-defined action on energy eigenstates (â†|n⟩ = √(n+1)|n+1⟩), its eigenvalues are complex numbers (it belongs to the family of operators with coherent state eigenstates, but these form an overcomplete non-orthogonal set). Observable operators are exactly the Hermitian ones; non-Hermitian operators like â, â†, and their combinations appear in calculations and in defining Hamiltonians, but do not themselves represent measurable quantities."

- question: "Why can't any linear operator on a Hilbert space represent a physical observable? What does the Hermitian property guarantee, and why are both guarantees necessary for the Born rule to work?"
  type: short-answer
  answer: "Two guarantees are needed: (1) real eigenvalues, so that measurement outcomes are real numbers, and (2) orthogonal eigenstates, so that the Born-rule probabilities sum to 1. The Hermitian condition Â = Â† delivers both. Real eigenvalues ensure the measured value is physically meaningful. Orthogonality ensures the probability of each outcome — |⟨aₙ|ψ⟩|² — sums to 1 across all possible outcomes when the eigenstates form a complete orthonormal basis. Without either condition, the probability interpretation breaks down: imaginary eigenvalues are uninterpretable as measurement results, and non-orthogonal eigenstates cause probabilities to exceed 1."
  explanation: "This is why the Hermitian condition is not arbitrary mathematical convention — it is the precise condition that makes the Born rule self-consistent. A non-Hermitian operator might have complex eigenvalues (failing condition 1) or non-orthogonal eigenstates (failing condition 2) or both. Either failure makes the statistical interpretation incoherent. The mathematical elegance of Hermitian operators is that a single algebraic condition (Â = Â†) simultaneously guarantees both physical requirements."
```

## Explainer

When you study quantum operators and eigenvalues, you learn that a quantum state can be expressed as a superposition of eigenstates of any operator. But not every operator deserves to represent a physical measurement — only a special class called **Hermitian operators** (also called self-adjoint operators) do. The defining property is Â = Â†, meaning the operator equals its own conjugate transpose. This seemingly abstract condition has concrete physical consequences that make it indispensable.

The first consequence is that Hermitian operators have **real eigenvalues**. This is essential: when you measure a physical quantity, the result must be a real number (you can't get an imaginary position or energy). For a Hermitian operator, if Â|aₙ⟩ = aₙ|aₙ⟩, then aₙ must be real. The proof is a one-line calculation using the Hermitian property: aₙ = ⟨aₙ|Â|aₙ⟩ = ⟨Â†aₙ|aₙ⟩ = aₙ*, which forces aₙ = aₙ*. No other class of operators guarantees this.

The second consequence is **orthogonality of eigenstates**. If two eigenstates |aₙ⟩ and |aₘ⟩ have different eigenvalues (aₙ ≠ aₘ), then ⟨aₙ|aₘ⟩ = 0. This lets you write any state as a complete sum of orthogonal basis states — the eigenstates of the observable form a complete orthonormal basis for the Hilbert space. The Born rule then says that if the system is in state |ψ⟩ and you measure observable Â, the probability of getting result aₙ is |⟨aₙ|ψ⟩|². The measurement collapses |ψ⟩ to |aₙ⟩. Without orthogonality of eigenstates, these probabilities wouldn't sum to 1 and the statistical interpretation would collapse.

The physical examples make the structure concrete. The Hamiltonian Ĥ is Hermitian, so energy eigenvalues are real — no surprise. The momentum operator p̂ = −iℏ∂/∂x is Hermitian on appropriately defined function spaces, with real eigenvalues p. The position operator x̂ is multiplication by x, trivially Hermitian. Non-Hermitian combinations — like the raising operator â† alone — do not represent observables; you can't measure it directly. When you later study commutation relations and the uncertainty principle, you'll see that two observables can be simultaneously measured only when their operators commute, which brings together eigenvalues, eigenstates, and measurement in a unified framework.
