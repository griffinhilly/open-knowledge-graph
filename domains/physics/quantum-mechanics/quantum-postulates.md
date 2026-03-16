---
id: quantum-postulates
title: Postulates of Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: wavefunction-and-probability
  type: hard
- id: hilbert-space-formalism
  type: hard
builds-toward:
- born-rule-and-measurement
- operators-and-observables
- identical-particles-exchange
tags:
- foundations
- postulates
stage: abstract-reasoning
status: draft
---

# Postulates of Quantum Mechanics

## Core Idea
The postulates specify that states live in Hilbert space, observables are Hermitian operators, measurement outcomes are eigenvalues, and time evolution follows the Schrödinger equation. Together these form the axiomatic foundation distinguishing quantum from classical mechanics.

## Explainer

You already know that quantum states are wavefunctions with probabilistic interpretations — from your study of the wavefunction and the Born rule — and that the mathematical arena for quantum mechanics is a Hilbert space of square-integrable functions, with inner products and orthonormal bases. The postulates of quantum mechanics assemble these ingredients into a complete logical framework that tells you exactly how to predict measurement outcomes and how systems evolve. They are not derived from anything deeper (at least within standard quantum mechanics); they are the axioms from which everything else follows.

**Postulate 1: State representation.** The complete description of a quantum system at any time is a normalized vector |ψ⟩ in a Hilbert space. This is already familiar to you — it is the wavefunction recast in Dirac notation. The key word is "complete": the state contains everything that can in principle be known about the system. There are no hidden variables, no additional information that a more complete theory would supply (within this framework). Two states that differ only by a global phase factor e^{iθ}|ψ⟩ represent the same physical state.

**Postulate 2: Observables as operators.** Every measurable physical quantity — position, momentum, energy, spin — is represented by a **Hermitian operator** acting on the Hilbert space. The requirement that the operator be Hermitian (equal to its own conjugate transpose) guarantees that its eigenvalues are real numbers, which is necessary since measurement outcomes must be real. From your Hilbert space work, you know that Hermitian operators have a complete set of orthonormal eigenvectors that span the space. **Postulate 3: Measurement.** When you measure an observable Â, the only possible outcomes are its eigenvalues aₙ. If the system is in state |ψ⟩ = Σcₙ|aₙ⟩, the probability of obtaining aₙ is |cₙ|² — the Born rule you already know. After the measurement, the state **collapses** to the corresponding eigenstate |aₙ⟩. This is the most philosophically contested postulate, but operationally it is the one that connects the mathematical formalism to experimental results.

**Postulate 4: Time evolution.** Between measurements, a closed quantum system evolves deterministically according to the **Schrödinger equation**: iℏ d|ψ⟩/dt = Ĥ|ψ⟩, where Ĥ is the Hamiltonian operator. This is the quantum analogue of Newton's second law — it specifies how the state changes in time. The evolution is **unitary** (it preserves the norm of the state and hence total probability), reflecting the fact that probability is conserved when no measurement occurs. Together, these four postulates define the rules of the game: state preparation sets |ψ⟩, Schrödinger evolution propagates it, and measurement extracts real numbers from it while collapsing the state. The tension between the deterministic evolution between measurements and the probabilistic collapse during measurement is the heart of the quantum measurement problem — and the starting point for every interpretation of quantum mechanics you will encounter later.
