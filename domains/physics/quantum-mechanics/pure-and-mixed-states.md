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
status: draft
---

# Pure States and Mixed States

## Core Idea
A pure state |ψ⟩ has ρ = |ψ⟩⟨ψ| with Tr(ρ²) = 1. A mixed state has Tr(ρ²) < 1, representing loss of information due to decoherence or measurement.

## Explainer

From your work with density matrices, you know that ρ is the most general description of a quantum system's state. A **pure state** is the special case where complete quantum information is available: the system is in a definite (though possibly superposed) quantum state |ψ⟩, and the density matrix is just the outer product ρ = |ψ⟩⟨ψ|. The entry ρᵢⱼ = ⟨i|ψ⟩⟨ψ|j⟩ captures not just probabilities (the diagonal) but also phase relationships between basis states (the off-diagonal terms). These off-diagonal elements — the **coherences** — are what make quantum superposition distinct from classical uncertainty.

To see why, consider a spin-1/2 particle prepared in |+x⟩ = (|↑⟩ + |↓⟩)/√2. This is a pure state. Its density matrix has equal diagonal entries (probability 1/2 of finding spin up or spin down in the z-basis) but also equal off-diagonal entries reflecting the definite phase relationship between |↑⟩ and |↓⟩. If you measure in the x-basis, you get a definite result: spin up with certainty. The coherences are the fingerprint of that certainty. For a pure state, ρ² = ρ (it's a projector), and Tr(ρ²) = Tr(ρ) = 1.

A **mixed state** arises when you have classical uncertainty about which pure state the system is in. Suppose you prepare spin-up |↑⟩ half the time and spin-down |↓⟩ the other half, but you don't track which — you just hand the particles over. The density matrix is ρ = (1/2)|↑⟩⟨↑| + (1/2)|↓⟩⟨↓|, which has equal diagonal entries but *zero* off-diagonal entries. Measuring in the z-basis still gives 50/50 results — identical to the |+x⟩ pure state in this basis. But the x-basis measurement now also gives 50/50, unlike the pure state. The coherences are gone. Tr(ρ²) = 1/4 + 1/4 = 1/2 < 1, and the closer Tr(ρ²) is to 1/n (where n is the dimension), the more maximally mixed the state.

The crucial point is that quantum superposition and classical statistical mixture look identical when you only ask the wrong questions, but they are physically different. A pure superposition can exhibit interference; a mixture cannot. When you split a laser beam, recombine it, and see fringes — that's pure-state coherence. When you mix photons from two independent light bulbs, no fringes appear — that's a mixture. The density matrix formalism distinguishes them precisely through the off-diagonal terms.

**Decoherence** is the process by which pure states become mixed in practice. When a quantum system interacts with a large environment (air molecules, photons, phonons), the system and environment become entangled — but you only have access to the system. Tracing out the environment from the joint density matrix eliminates the coherences, converting the system's pure state into a mixture. This is why quantum computers require isolation: every unwanted environmental interaction degrades pure states toward mixtures, destroying the interference that makes quantum computation powerful. The Tr(ρ²) test is the operational measure of how much quantum coherence survives.


