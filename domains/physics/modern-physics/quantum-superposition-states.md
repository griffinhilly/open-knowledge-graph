---
id: quantum-superposition-states
title: Quantum Superposition and Linear Combinations of States
domain: physics
course: modern-physics
prerequisites:
- id: wavefunction-probability-density
  type: hard
- id: quantum-superposition
  type: soft
- id: vector-spaces-definition
  type: hard
builds-toward:
- expectation-values-quantum
tags:
- quantum
- superposition
- states
stage: abstract-reasoning
status: draft
---

# Quantum Superposition and Linear Combinations of States

## Core Idea
A quantum system can exist in a superposition of multiple eigenstates simultaneously, with relative amplitudes and phases determining the overall wavefunction ψ = Σ cₙφₙ. Measurement projects the system into one eigenstate with probability |cₙ|². Superposition is fundamentally different from classical uncertainty; it is an ontological feature of quantum reality.

## Explainer

From your study of vector spaces, you know that any vector can be written as a linear combination of basis vectors. In quantum mechanics, states work the same way: the wavefunction ψ lives in a Hilbert space, and any complete set of eigenstates {φₙ} forms a basis for that space. Writing ψ = Σ cₙφₙ is not a metaphor — it is a literal vector decomposition. The **coefficients cₙ** are complex numbers called **probability amplitudes**, and the square of each modulus, |cₙ|², gives the probability of finding the system in eigenstate φₙ if you measure the corresponding observable. The normalization condition ⟨ψ|ψ⟩ = 1 requires Σ |cₙ|² = 1, which is just the statement that probabilities sum to one.

The critical conceptual leap is understanding what this superposition *means* before measurement. A classical coin spinning in the air is either heads or tails — you just do not know which. A quantum particle in a superposition of energy eigenstates is genuinely *not* in any single eigenstate; both terms are simultaneously present and physically real. The clearest evidence is **quantum interference**: if you prepare two paths through an interferometer so their probability amplitudes add in one direction and cancel in another, you get bright and dark fringes. This pattern depends on the *phases* of the coefficients cₙ, not just their magnitudes. A classical probability mixture cannot produce interference; only a genuine superposition can.

**Measurement** collapses the superposition. Before you measure, the system evolves as a superposition, with each component φₙ carrying its own time evolution e^{-iEₙt/ℏ}. The relative phases between terms oscillate, driving interference phenomena like the beating between energy levels. When you perform a measurement of the observable whose eigenstates are {φₙ}, the wavefunction instantaneously projects onto one eigenstate φₙ with probability |cₙ|². After measurement, the other terms are gone — the superposition is destroyed. This is why repeated measurements of the same state (before re-preparation) do not yield a distribution: the first measurement collapses the state.

The deeper lesson is that the basis matters. An electron in a superposition of spin-up and spin-down along the z-axis is simultaneously in a definite eigenstate of spin along some other axis. "Is the electron in a superposition?" is not a well-posed question without specifying: superposition of *which* observable's eigenstates? Every quantum state is an eigenstate of some observable and a superposition of eigenstates of every non-commuting observable. Superposition is not a special condition of a state — it is the generic condition, relative to most measurement bases.
