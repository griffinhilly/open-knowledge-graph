---
id: quantum-superposition
title: Quantum Superposition
domain: physics
course: quantum-mechanics
prerequisites:
- id: state-vectors-and-wavefunctions
  type: hard
- id: vector-spaces-definition
  type: hard
builds-toward:
- entanglement-quantum
- quantum-measurement-problem
tags:
- superposition
- quantum-state
- wave-nature
stage: advanced
status: draft
---

# Quantum Superposition

## Core Idea
A quantum system can exist in a superposition of multiple states simultaneously, written as |ψ⟩ = Σ cₙ|φₙ⟩ where |cₙ|² are probabilities. Unlike classical systems where the system definitely is in one state, a superposed quantum state genuinely exhibits properties of all constituent states until measured. Superposition is fundamental to quantum mechanics and has no classical analogue.

## Explainer

You already know that quantum states live in a vector space, and that a state |ψ⟩ can be expanded in any complete basis {|φₙ⟩} as |ψ⟩ = Σ cₙ|φₙ⟩. **Superposition** is what this expansion means physically: the system is not "secretly" in one of the basis states while we remain ignorant — it genuinely occupies all states simultaneously, weighted by the coefficients cₙ. This is the sharpest departure from classical physics, and it demands a careful re-examination of what "state" means.

A classical coin lying flat is definitely heads or definitely tails — we might not know which, but one of those descriptions is true. A quantum coin in superposition is different: before measurement it is neither heads nor tails, and the description |ψ⟩ = c₀|heads⟩ + c₁|tails⟩ is complete — there is nothing more to say. The evidence for this is **interference**. If the system were merely in a classical mixture (heads with probability |c₀|², tails with probability |c₁|²), probabilities for overlapping paths would simply add. But quantum amplitudes add before squaring, producing interference fringes that only appear when both terms are simultaneously "present." The double-slit experiment is the iconic demonstration: each particle goes through both slits simultaneously, and the wave-like interference pattern cannot be explained unless the particle was in a superposition of both paths.

The coefficients cₙ are **probability amplitudes** — complex numbers whose squared magnitudes |cₙ|² give the probability of finding the system in state |φₙ⟩ upon measurement. The normalization condition Σ|cₙ|² = 1 ensures probabilities sum to one. Before measurement, the superposition is the complete description. Upon measurement, the state **collapses** to a single eigenstate: the system is now definitely in some |φₖ⟩ with probability |cₖ|², and all other amplitudes vanish. This collapse is instantaneous and irreversible, and it is the source of the quantum measurement problem you will study next.

A crucial subtlety: superposition is basis-dependent. A state that is a superposition in the energy eigenbasis may be an eigenstate in the position basis, and vice versa. The Schrödinger equation governs how superpositions evolve in time — deterministically, linearly, and coherently, preserving the full superposition — until measurement disrupts it. This tension between deterministic evolution and probabilistic collapse is at the heart of quantum foundations. But the computational power of superposition is already clear: a quantum system of n two-level particles lives in a 2ⁿ-dimensional Hilbert space, and superposition allows it to occupy all 2ⁿ directions simultaneously — the basis of quantum computing.
