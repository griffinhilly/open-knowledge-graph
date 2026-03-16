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
stage: abstract-reasoning
status: draft
---

# Commutators and Commutation Relations

## Core Idea
The commutator [Â, B̂] = ÂB̂ − B̂Â measures how operators fail to commute. Nonzero commutators signal that observables cannot be simultaneously measured with arbitrary precision.

## Explainer

The commutator measures something physically fundamental: whether two operations can be performed in either order without affecting the result. In classical mechanics, all observables commute — it doesn't matter whether you measure position or momentum first, the act of measurement doesn't disturb the system. Quantum mechanics is different, and the commutator [Â, B̂] = ÂB̂ − B̂Â is how we quantify the failure of this classical commutativity.

From your study of operators, you know that observables are Hermitian operators acting on state vectors. The commutator is itself an operator. If [Â, B̂] = 0, the operators **commute** — they share a complete set of eigenstates and can be simultaneously diagonalized, meaning a state can be an eigenstate of both at once. Measuring one observable leaves the system in an eigenstate of the other, so both values can be known simultaneously. If [Â, B̂] ≠ 0, the operators **do not commute** — they have no common eigenbasis, and measuring one necessarily disturbs the other. The canonical example is [x̂, p̂] = iℏ: position and momentum operators fail to commute by exactly iℏ, and this single equation is the mathematical root of the Heisenberg uncertainty principle.

Commutators also govern time evolution. If an operator commutes with the Hamiltonian, [Ĥ, Ô] = 0, then the corresponding observable is **conserved** — its expectation value is constant in time. This is the quantum version of Noether's theorem. Angular momentum components illustrate the algebra: L̂x, L̂y, and L̂z satisfy [L̂x, L̂y] = iℏL̂z and cyclic permutations, so no two components can be simultaneously known. But [L̂², L̂z] = 0, which is why quantum states can simultaneously have definite total angular momentum and one definite component — the hydrogen wavefunctions you've encountered are precisely the joint eigenstates of Ĥ, L̂², and L̂z.

The deeper point is that commutation relations encode the algebraic structure of a physical theory. All the physics of angular momentum — the quantization of ℓ and m, the ladder operators, the addition rules for combining spins — follow entirely from [L̂i, L̂j] = iℏεijk L̂k, without ever solving a differential equation. The commutator is not just a computational tool; it is the language in which the constraints of quantum mechanics are written.
