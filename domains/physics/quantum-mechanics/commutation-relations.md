---
id: commutation-relations
title: Commutators and Commutation Relations
domain: physics
course: quantum-mechanics
prerequisites:
- id: observables-and-operators
  type: hard
builds-toward:
- canonical-commutation-relations
- uncertainty-relations
tags:
- operators
- commutators
- algebra
stage: formal-systems
status: draft
---

# Commutators and Commutation Relations

## Core Idea
The commutator [Â, B̂] = ÂB̂ − B̂Â measures how operators fail to commute. Nonzero commutators signal that observables cannot be simultaneously measured with arbitrary precision.

## Questions

```yaml
- question: "Two quantum-mechanical operators Â and B̂ satisfy [Â, B̂] = 0. What can you immediately conclude about the corresponding observables?"
  type: multiple-choice
  options:
    - "Measuring Â always yields the same numerical result as measuring B̂"
    - "They share a complete set of eigenstates — a quantum state can simultaneously have a definite value of both observables, and measuring one does not disturb the other"
    - "Both operators must equal zero"
    - "The observables are physically identical and measure the same thing"
  answer: 1
  explanation: "When [Â, B̂] = 0, the operators commute — they can be simultaneously diagonalized, meaning there exists a basis of states that are eigenstates of both. In such a state, both observables have sharp (definite) values at once. Measuring Â leaves the system in an eigenstate of B̂ as well, so the subsequent measurement of B̂ is not disturbed. This is the direct physical meaning of commutativity: simultaneous knowability."

- question: "The canonical commutation relation [x̂, p̂] = iℏ implies that:"
  type: multiple-choice
  options:
    - "Position and momentum have identical units and can be measured interchangeably"
    - "The position and momentum operators are equal in magnitude but opposite in sign"
    - "Position and momentum share no common eigenstates — no quantum state can simultaneously have a definite position and a definite momentum, which is the mathematical root of the Heisenberg uncertainty principle"
    - "The Hamiltonian commutes with both x̂ and p̂, so both are conserved quantities"
  answer: 2
  explanation: "Because [x̂, p̂] ≠ 0, x̂ and p̂ do not share a common eigenbasis. There is no quantum state that is simultaneously an eigenstate of both — any state with a perfectly definite position (a delta function) has completely indefinite momentum, and vice versa. This non-commutativity is not an artifact of imprecise instruments; it is a structural feature of the operators. The Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2 follows mathematically from this single commutation relation."

- question: "If an operator Ô commutes with the Hamiltonian ([Ĥ, Ô] = 0), then the observable corresponding to Ô is conserved — its expectation value does not change over time."
  type: true-false
  answer: true
  explanation: "This is the quantum version of Noether's theorem. The time evolution of an expectation value is governed by d⟨Ô⟩/dt = (i/ℏ)⟨[Ĥ, Ô]⟩ (plus any explicit time dependence). If [Ĥ, Ô] = 0, this derivative vanishes — the expectation value is constant. For example, if a system has rotational symmetry, the angular momentum operators commute with H, and angular momentum is conserved. Commutativity with the Hamiltonian is the precise characterization of a conserved quantity in quantum mechanics."

- question: "The Heisenberg uncertainty principle is fundamentally a statement about measurement disturbance — sufficiently delicate instruments could measure both position and momentum precisely, but practical limitations prevent this."
  type: true-false
  answer: false
  explanation: "This is the most common and most important misconception about quantum uncertainty. The uncertainty principle is not about measurement clumsiness — it follows mathematically from the non-commutativity [x̂, p̂] = iℏ. Even in principle, there is no quantum state in which both position and momentum have simultaneously definite values, because no such eigenstate exists. This is a structural fact about the Hilbert space and its operators, not a technological limitation. The uncertainty is in the quantum state itself, not in the measuring apparatus."

- question: "What does it mean for two operators to 'commute,' and why does non-commutativity have direct physical consequences for what can be simultaneously known about a quantum system?"
  type: short-answer
  answer: "Two operators commute if ÂB̂ = B̂Â, i.e., [Â, B̂] = ÂB̂ − B̂Â = 0. Physically, commuting operators share a complete set of simultaneous eigenstates — states in which both observables have definite values. Non-commutativity ([Â, B̂] ≠ 0) means no such shared eigenbasis exists: any eigenstate of Â is a superposition of many eigenstates of B̂, so measuring B̂ after a definite-Â state yields a spread of results. The commutator literally quantifies how much the operators' algebraic order matters, and this algebraic fact is why certain pairs of observables cannot simultaneously have sharp values."
  explanation: "The deep point is that commutation relations encode the fundamental structure of a quantum theory — not just as a mathematical technicality but as the source of physical constraints. All the content of the uncertainty principle, the conservation laws (via [Ĥ, Ô] = 0), and the entire structure of angular momentum quantization follow from commutation relations, without solving any differential equations. The commutator is the language in which quantum mechanics writes its physical constraints."
```

## Explainer

The commutator measures something physically fundamental: whether two operations can be performed in either order without affecting the result. In classical mechanics, all observables commute — it doesn't matter whether you measure position or momentum first, the act of measurement doesn't disturb the system. Quantum mechanics is different, and the commutator [Â, B̂] = ÂB̂ − B̂Â is how we quantify the failure of this classical commutativity.

From your study of operators, you know that observables are Hermitian operators acting on state vectors. The commutator is itself an operator. If [Â, B̂] = 0, the operators **commute** — they share a complete set of eigenstates and can be simultaneously diagonalized, meaning a state can be an eigenstate of both at once. Measuring one observable leaves the system in an eigenstate of the other, so both values can be known simultaneously. If [Â, B̂] ≠ 0, the operators **do not commute** — they have no common eigenbasis, and measuring one necessarily disturbs the other. The canonical example is [x̂, p̂] = iℏ: position and momentum operators fail to commute by exactly iℏ, and this single equation is the mathematical root of the Heisenberg uncertainty principle.

Commutators also govern time evolution. If an operator commutes with the Hamiltonian, [Ĥ, Ô] = 0, then the corresponding observable is **conserved** — its expectation value is constant in time. This is the quantum version of Noether's theorem. Angular momentum components illustrate the algebra: L̂x, L̂y, and L̂z satisfy [L̂x, L̂y] = iℏL̂z and cyclic permutations, so no two components can be simultaneously known. But [L̂², L̂z] = 0, which is why quantum states can simultaneously have definite total angular momentum and one definite component — the hydrogen wavefunctions you've encountered are precisely the joint eigenstates of Ĥ, L̂², and L̂z.

The deeper point is that commutation relations encode the algebraic structure of a physical theory. All the physics of angular momentum — the quantization of ℓ and m, the ladder operators, the addition rules for combining spins — follow entirely from [L̂i, L̂j] = iℏεijk L̂k, without ever solving a differential equation. The commutator is not just a computational tool; it is the language in which the constraints of quantum mechanics are written.
