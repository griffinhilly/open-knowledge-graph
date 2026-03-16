---
id: quantum-operators
title: Quantum Operators
domain: physics
course: quantum-mechanics
prerequisites:
- id: hilbert-spaces-and-dirac-notation
  type: hard
- id: linear-transformation-definition
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
- id: linear-transformations
  type: hard
builds-toward:
- quantum-observables
- eigenvalues-eigenstates-quantum
- commutation-relations
tags:
- operators
- observables
- linear-algebra
stage: advanced
status: draft
---

# Quantum Operators

## Core Idea
Quantum operators are linear transformations acting on state vectors in Hilbert space. Common operators include position x̂, momentum p̂ = -iℏ(d/dx), and angular momentum L̂. Operators encode dynamical information: applying an operator to a state yields another state, or an eigenstate yields the eigenvalue representing an observable quantity.

## Explainer

From your linear algebra prerequisites, you know that a linear transformation takes vectors to vectors and satisfies T(αv + βw) = αT(v) + βT(w). In quantum mechanics, the vectors live in Hilbert space — they are quantum states — and the "transformations" are operators representing physical observables. Every measurable quantity (position, momentum, energy, spin) corresponds to a specific **Hermitian operator**, and the possible measurement outcomes are exactly the operator's eigenvalues.

The **position operator** x̂ acts on a wavefunction ψ(x) by multiplication: x̂ψ(x) = xψ(x). This makes sense — the operator "asks" where the particle is by multiplying by the position coordinate. The **momentum operator** p̂ = −iℏ(d/dx) is more surprising: it is a differential operator. This is not arbitrary. From the de Broglie relation p = ℏk and the fact that plane waves e^(ikx) are states of definite momentum, differentiating e^(ikx) brings down ik — so −iℏ(d/dx) applied to e^(ikx) gives ℏk · e^(ikx) = p · e^(ikx). Plane waves are eigenstates of p̂ with eigenvalue p.

The eigenvalue equation Â|ψ⟩ = a|ψ⟩ is the central formula. When a state |ψ⟩ is an eigenstate of operator Â with eigenvalue a, measuring the corresponding observable always yields the value a with certainty. When the state is a superposition of eigenstates — say |ψ⟩ = c₁|a₁⟩ + c₂|a₂⟩ — the measurement yields a₁ with probability |c₁|² or a₂ with probability |c₂|². The operator doesn't tell you which outcome will happen; it tells you what outcomes are possible and (via the state decomposition) with what probabilities. This is the precise sense in which operators "encode observable information."

**Hermitian operators** are the special class required for physical observables because their eigenvalues are always real — measurement outcomes must be real numbers. From Dirac notation you know that the adjoint of an operator is defined by ⟨φ|Â†|ψ⟩ = ⟨ψ|Â|φ⟩*; for Hermitian operators, Â† = Â. You can verify p̂ is Hermitian by integration by parts. The requirement of Hermiticity, combined with the eigenvector structure of linear algebra you already know, determines which mathematical objects can serve as quantum observables — not every linear operator qualifies, only the Hermitian ones.
