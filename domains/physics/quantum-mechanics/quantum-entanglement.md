---
id: quantum-entanglement
title: Quantum Entanglement
domain: physics
course: quantum-mechanics
prerequisites:
- id: kets-and-bras
  type: hard
builds-toward:
- bell-theorem
tags:
- entanglement
- correlations
stage: formal-systems
status: draft
---

# Quantum Entanglement

## Core Idea
An entangled state cannot be written as |ψ₁⟩⊗|ψ₂⟩. The Bell state |Φ⁺⟩ = (|↑↓⟩ + |↓↑⟩)/√2 is entangled: measuring one spin constrains the other regardless of distance.

## Explainer

You already know from kets and bras how to write a quantum state as a vector in Hilbert space. A single spin-½ particle has states |↑⟩ and |↓⟩ as a basis, and a general state is a superposition α|↑⟩ + β|↓⟩. For two particles that are **independent** — no interactions, no correlations — the combined system lives in the tensor product space, and the combined state factorizes: |Ψ⟩ = |ψ₁⟩ ⊗ |ψ₂⟩ = (α|↑⟩ + β|↓⟩) ⊗ (γ|↑⟩ + δ|↓⟩). In this case, measuring particle 1 tells you nothing new about particle 2 beyond what you already knew.

**Entanglement** arises when the two-particle state cannot be written as such a product. The canonical example is the **Bell state** |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2. Try to factor it: |Φ⁺⟩ = (a|↑⟩ + b|↓⟩) ⊗ (c|↑⟩ + d|↓⟩) would require ac = 1/√2, ad = 0, bc = 0, bd = 1/√2. The equations ad = 0 and bc = 0 force either a or d to be zero, and either b or c to be zero — but then ac or bd would also be zero, contradicting ac = bd = 1/√2. The state genuinely cannot be factored. Neither particle has an individual quantum state. They only have a joint state.

The physical consequence is striking. Before any measurement, each particle individually is in a completely mixed state — a 50/50 mixture of spin-up and spin-down. But the two particles are perfectly correlated: if you measure particle 1 and find ↑, the entire two-particle state collapses to |↑↑⟩, and particle 2 is now definitely ↑ as well, no matter how far away particle 2 is. This instantaneous correlation is not a signal — you cannot use it to send information faster than light, because the individual measurement outcomes are still random. But the correlations themselves exceed anything explainable by pre-existing ("hidden") properties of the individual particles, as Bell's theorem (the next topic) makes mathematically precise. Entanglement is the resource behind quantum teleportation, quantum cryptography, and quantum computing's potential for exponential speedup.
