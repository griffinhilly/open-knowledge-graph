---
id: pure-and-mixed-states
title: Pure States and Mixed States
domain: physics
course: quantum-mechanics
prerequisites:
- id: density-matrices
  type: hard
tags:
- pure-states
- mixed-states
stage: formal-systems
status: validated
---

# Pure States and Mixed States

## Core Idea
A pure state |ψ⟩ has ρ = |ψ⟩⟨ψ| with Tr(ρ²) = 1. A mixed state has Tr(ρ²) < 1, representing loss of information due to decoherence or measurement.

## Questions

```yaml
- question: "A spin-1/2 particle is prepared in |+x⟩ = (|↑⟩ + |↓⟩)/√2. A second particle is in a statistical mixture: spin up 50% of the time and spin down 50%, with no tracking of which. Both give identical measurement statistics in the z-basis. What physically distinguishes these two states?"
  type: multiple-choice
  options:
    - "They are physically identical — different preparations of the same quantum state"
    - "The pure state has off-diagonal coherences in its density matrix; the mixed state does not"
    - "The mixed state has Tr(ρ²) = 1; the pure state has Tr(ρ²) < 1"
    - "The pure state has equal diagonal elements; the mixed state has unequal diagonal elements"
  answer: 1
  explanation: "Both states show identical 50/50 z-measurement statistics — the diagonal elements are the same. The distinction lives in the off-diagonal coherences: the pure state has them (reflecting the definite phase relationship between |↑⟩ and |↓⟩), the mixed state does not. This difference becomes visible when measuring in a different basis: the pure state gives a definite outcome in the x-basis, while the mixture gives 50/50 in every basis. Option C reverses the Tr(ρ²) relationship — pure states have Tr(ρ²) = 1, mixed states have Tr(ρ²) < 1."

- question: "A quantum computer qubit begins in a pure superposition state with Tr(ρ²) = 1.0. After interacting with its environment, Tr(ρ²) drops to 0.52. What has happened?"
  type: multiple-choice
  options:
    - "The qubit was measured, collapsing it to a definite computational basis state"
    - "The qubit entangled with environmental degrees of freedom; tracing out the environment leaves a mixed reduced state"
    - "The qubit is now more stable because decoherence has suppressed quantum noise"
    - "Tr(ρ²) decreasing means the qubit has gained quantum information from the environment"
  answer: 1
  explanation: "Decoherence occurs when a quantum system entangles with its environment. Even though the joint system+environment state may remain pure, tracing out the environment from the joint density matrix eliminates the off-diagonal coherences, leaving a mixed reduced state for the qubit. Tr(ρ²) < 1 confirms the state is mixed — quantum coherence has been lost. Option A describes projective measurement, which would yield a new pure state with Tr(ρ²) = 1 after collapse. Decoherence is a gradual degradation, not a discrete event."

- question: "A quantum state that shows 50/50 probabilities for spin-up and spin-down should be a mixed state."
  type: true-false
  answer: false
  explanation: "The pure state |+x⟩ = (|↑⟩ + |↓⟩)/√2 gives exactly 50/50 probabilities in the z-basis while being a pure state with Tr(ρ²) = 1 and nonzero off-diagonal coherences. Equal measurement probabilities in one basis say nothing about purity — purity is determined by whether coherences exist, not by the diagonal probabilities. The distinction requires probing a different measurement basis, where the pure state gives a definite outcome and the mixture gives 50/50."

- question: "For a pure state, the density matrix ρ satisfies ρ² = ρ."
  type: true-false
  answer: true
  explanation: "A pure state has ρ = |ψ⟩⟨ψ|, so ρ² = |ψ⟩⟨ψ|ψ⟩⟨ψ| = |ψ⟩⟨ψ| = ρ since ⟨ψ|ψ⟩ = 1. This means ρ is a projector onto the pure state, and Tr(ρ²) = Tr(ρ) = 1. For a mixed state, ρ² ≠ ρ and Tr(ρ²) < 1. The identity ρ² = ρ is the precise algebraic signature that distinguishes pure states from mixtures."

- question: "Explain why a pure quantum superposition and a classical statistical mixture can give identical measurement statistics in one basis but differ in another. What does this reveal about quantum coherence?"
  type: short-answer
  answer: "A pure superposition encodes definite phase relationships between basis states through off-diagonal coherences in the density matrix. A classical mixture has the same diagonal entries (same probabilities for a given basis measurement) but zero off-diagonal terms — it represents classical uncertainty about which pure state the system is in. Measuring in the original basis only probes the diagonal and cannot distinguish them. Measuring in a rotated basis probes the off-diagonal coherences and reveals the difference: the pure state gives a definite outcome in the rotated basis, the mixture gives 50/50. Coherences are the operational signature of quantum superposition — they enable interference. Their presence or absence, not the diagonal probabilities, is what separates quantum from classical uncertainty."
  explanation: "This is the conceptual core of the density matrix formalism. Tr(ρ²) = 1 iff the state is pure (coherences intact); Tr(ρ²) < 1 means some quantum information has been lost to the environment. Decoherence is precisely the process of losing these off-diagonal terms through entanglement with the environment."
```

## Explainer

From your work with density matrices, you know that ρ is the most general description of a quantum system's state. A **pure state** is the special case where complete quantum information is available: the system is in a definite (though possibly superposed) quantum state |ψ⟩, and the density matrix is just the outer product ρ = |ψ⟩⟨ψ|. The entry ρᵢⱼ = ⟨i|ψ⟩⟨ψ|j⟩ captures not just probabilities (the diagonal) but also phase relationships between basis states (the off-diagonal terms). These off-diagonal elements — the **coherences** — are what make quantum superposition distinct from classical uncertainty.

To see why, consider a spin-1/2 particle prepared in |+x⟩ = (|↑⟩ + |↓⟩)/√2. This is a pure state. Its density matrix has equal diagonal entries (probability 1/2 of finding spin up or spin down in the z-basis) but also equal off-diagonal entries reflecting the definite phase relationship between |↑⟩ and |↓⟩. If you measure in the x-basis, you get a definite result: spin up with certainty. The coherences are the fingerprint of that certainty. For a pure state, ρ² = ρ (it's a projector), and Tr(ρ²) = Tr(ρ) = 1.

A **mixed state** arises when you have classical uncertainty about which pure state the system is in. Suppose you prepare spin-up |↑⟩ half the time and spin-down |↓⟩ the other half, but you don't track which — you just hand the particles over. The density matrix is ρ = (1/2)|↑⟩⟨↑| + (1/2)|↓⟩⟨↓|, which has equal diagonal entries but *zero* off-diagonal entries. Measuring in the z-basis still gives 50/50 results — identical to the |+x⟩ pure state in this basis. But the x-basis measurement now also gives 50/50, unlike the pure state. The coherences are gone. Tr(ρ²) = 1/4 + 1/4 = 1/2 < 1, and the closer Tr(ρ²) is to 1/n (where n is the dimension), the more maximally mixed the state.

The crucial point is that quantum superposition and classical statistical mixture look identical when you only ask the wrong questions, but they are physically different. A pure superposition can exhibit interference; a mixture cannot. When you split a laser beam, recombine it, and see fringes — that's pure-state coherence. When you mix photons from two independent light bulbs, no fringes appear — that's a mixture. The density matrix formalism distinguishes them precisely through the off-diagonal terms.

**Decoherence** is the process by which pure states become mixed in practice. When a quantum system interacts with a large environment (air molecules, photons, phonons), the system and environment become entangled — but you only have access to the system. Tracing out the environment from the joint density matrix eliminates the coherences, converting the system's pure state into a mixture. This is why quantum computers require isolation: every unwanted environmental interaction degrades pure states toward mixtures, destroying the interference that makes quantum computation powerful. The Tr(ρ²) test is the operational measure of how much quantum coherence survives.


