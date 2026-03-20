---
id: observables-and-operators
title: Observables and Quantum Operators
domain: physics
course: quantum-mechanics
prerequisites:
- id: dirac-notation
  type: hard
- id: linear-transformations
  type: hard
builds-toward:
- commutation-relations
tags:
- operators
- observables
- hermitian
stage: formal-systems
status: draft
---

# Observables and Quantum Operators

## Core Idea
Each physical observable is represented by a Hermitian operator; eigenvalues are possible measurement outcomes, eigenstates have definite values. The expectation value ⟨ψ|Ô|ψ⟩ predicts the average of repeated measurements.

## Explainer

In classical mechanics, an observable is just a number — a particle's position, momentum, or energy at any instant. Quantum mechanics replaces these numbers with **operators**: mathematical objects that act on state vectors (kets) to produce new state vectors. The position of a particle is not a fixed number but an operator X̂; its momentum is an operator P̂. This isn't a notational whim — it is forced by the experimental fact that quantum systems don't have definite values until measured, and the act of measurement disturbs the system.

The central constraint is that operators representing physical observables must be **Hermitian** (or self-adjoint): Â = Â†, meaning ⟨φ|Â|ψ⟩ = ⟨ψ|Â|φ⟩*. You need Hermitian operators for two reasons, both rooted in physics. First, Hermitian operators have real eigenvalues — and measurement outcomes must be real numbers, not complex ones. Second, their eigenstates form a complete orthonormal set, so any quantum state can be expanded in them. This is the spectral theorem from linear algebra, now doing real physical work: it guarantees that the eigenstates of any observable form a valid basis for the Hilbert space.

The **eigenvalue equation** Â|aₙ⟩ = aₙ|aₙ⟩ encodes the measurement postulate directly. If the system is in eigenstate |aₙ⟩, a measurement of A yields the definite value aₙ with certainty. If the system is in a superposition |ψ⟩ = Σ cₙ|aₙ⟩, a measurement yields outcome aₙ with probability |cₙ|² = |⟨aₙ|ψ⟩|², and the state collapses to |aₙ⟩ afterward. The **expectation value** ⟨ψ|Â|ψ⟩ = Σ aₙ|cₙ|² is simply the probability-weighted average of all possible outcomes — the quantum analog of a classical average.

Two observables can be simultaneously well-defined only if their operators **commute**: [Â, B̂] = ÂB̂ − B̂Â = 0. When this commutator is zero, the operators share a common eigenbasis — you can simultaneously know definite values of both A and B. When the commutator is nonzero (as it is for position and momentum: [X̂, P̂] = iℏ), no state can have definite values of both simultaneously, and the uncertainty principle follows. The operator structure is therefore not just a bookkeeping device: it encodes which pairs of quantities are compatible and which are fundamentally in tension.
