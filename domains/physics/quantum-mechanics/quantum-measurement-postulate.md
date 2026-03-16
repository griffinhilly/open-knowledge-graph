---
id: quantum-measurement-postulate
title: Quantum Measurement and Collapse
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
- id: state-vectors-and-wavefunctions
  type: hard
builds-toward:
- quantum-measurement-problem
- interpretations-quantum-mechanics
tags:
- measurement
- collapse
- interpretation
stage: advanced
status: draft
---

# Quantum Measurement and Collapse

## Core Idea
Measurement of an observable forces the quantum state to collapse into an eigenstate of the measurement operator, with outcome equal to the corresponding eigenvalue. The probability of measuring eigenvalue λₙ equals |⟨φₙ|ψ⟩|², where |φₙ⟩ is the corresponding eigenstate. After measurement, the system remains in the collapsed state until further interaction.

## Explainer

From your study of state vectors and wavefunctions, you know that a quantum state |ψ⟩ can be expressed as a superposition of basis states. From the quantum postulates, you know that observable quantities correspond to Hermitian operators whose eigenstates form a complete basis. The measurement postulate tells you what happens when you actually observe a system in superposition — and the answer is discontinuous and irreversible in a way that nothing in classical physics prepares you for.

Suppose the state is |ψ⟩ = Σ cₙ |φₙ⟩, where |φₙ⟩ are the eigenstates of some observable Â with eigenvalues λₙ. Before measurement, the system is genuinely in all states simultaneously — this is not mere ignorance about a pre-existing value. When you measure Â, you get exactly one result: some particular λₙ, with probability |cₙ|² = |⟨φₙ|ψ⟩|². This is the **Born rule**, and it is one of the foundational postulates — it cannot be derived from the Schrödinger equation alone. Immediately after the measurement, the state collapses: |ψ⟩ → |φₙ⟩. All other terms in the superposition disappear, and subsequent measurements of the same observable will yield λₙ with certainty.

Two features make collapse radically different from classical probability. First, the outcome is not just unknown before measurement — it is genuinely indeterminate. An electron approaching a half-silvered mirror is not secretly going either left or right; interference experiments prove the two paths are simultaneously real. Second, **collapse is not Schrödinger evolution**. The Schrödinger equation is linear and unitary — it never collapses a superposition. Measurement introduces a discontinuous jump that sits outside the ordinary dynamics. This mismatch is called the **measurement problem**, and it is the deepest unresolved conceptual issue in quantum foundations.

A useful way to build intuition: think of the inner product ⟨φₙ|ψ⟩ as the "overlap amplitude" between the system state and the eigenstate you're projecting onto. The probability is the square of this amplitude. Orthogonal eigenstates (⟨φₙ|φₘ⟩ = 0 for n ≠ m) mean that if you measure and get λₙ, the probability of immediately getting λₘ in a second measurement is zero. Repeated measurements of the same observable on the same collapsed state always return the same value — because after collapse, the state is already an eigenstate. This repeatability is why measurement collapse is physically essential: it is what makes classical records (pointer positions, detector clicks) possible.
