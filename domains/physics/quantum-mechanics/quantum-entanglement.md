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
status: validated
---

# Quantum Entanglement

## Core Idea
An entangled state cannot be written as |ψ₁⟩⊗|ψ₂⟩. The Bell state |Φ⁺⟩ = (|↑↓⟩ + |↓↑⟩)/√2 is entangled: measuring one spin constrains the other regardless of distance.

## Questions

```yaml
- question: "Alice and Bob share a pair of particles in the Bell state |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2. Alice measures her particle and finds spin-up. She immediately knows Bob's particle will be spin-up too. Can Alice use this to send Bob a message faster than light?"
  type: multiple-choice
  options:
    - "Yes — Alice's measurement instantly determines Bob's outcome, transmitting a bit of information"
    - "No — because Alice cannot control which outcome she gets, she cannot encode a message in her measurement results"
    - "Yes — but only if Alice measures along the same axis Bob is measuring"
    - "No — because the correlation only holds statistically, not for individual measurements"
  answer: 1
  explanation: "Alice cannot control whether she gets spin-up or spin-down — her outcome is random. Because she cannot choose the bit she sends, she cannot encode information. Bob's side sees a random sequence of spin-up and spin-down outcomes regardless of whether Alice has measured or not. The correlation (that their results agree) is only visible when they compare notes afterward through a classical channel. Entanglement enables correlations, not signaling. Option D is wrong: the correlation holds for each individual measurement pair, not just statistically."

- question: "Which of the following correctly explains why the Bell state |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2 is entangled rather than separable?"
  type: multiple-choice
  options:
    - "It contains two particles, and any two-particle state is entangled by definition"
    - "It cannot be written as a product (a|↑⟩ + b|↓⟩)⊗(c|↑⟩ + d|↓⟩) because no values of a,b,c,d satisfy all required coefficient equations simultaneously"
    - "The two particles are correlated, and correlation always implies entanglement"
    - "The state contains only |↑↑⟩ and |↓↓⟩ terms, not |↑↓⟩ or |↓↑⟩, which creates an imbalance that prevents factoring"
  answer: 1
  explanation: "Entanglement is defined precisely as the inability to write the state as a tensor product of individual states. For |Φ⁺⟩, a product state (a|↑⟩ + b|↓⟩)⊗(c|↑⟩ + d|↓⟩) expands to ac|↑↑⟩ + ad|↑↓⟩ + bc|↓↑⟩ + bd|↓↓⟩. Matching |Φ⁺⟩ requires ac = bd = 1/√2 and ad = bc = 0. But ad = 0 forces a=0 or d=0, and bc = 0 forces b=0 or c=0 — either way, ac or bd becomes 0, contradiction. The algebra literally fails, proving no product state exists."

- question: "In an entangled two-particle state, neither particle individually has a definite quantum state — they only have a joint state."
  type: true-false
  answer: true
  explanation: "This is the deepest feature of entanglement. For an entangled pair, if you ask 'what is particle 1's quantum state?' the only honest answer is that it doesn't have one. Particle 1 is in a maximally mixed state (50/50 spin-up/spin-down), which is not a pure quantum state at all. The pure quantum state lives at the level of the pair: |Φ⁺⟩ is a well-defined state of the two-particle system, even though neither particle individually has a well-defined state. This is what makes entanglement so different from classical correlation."

- question: "Quantum entanglement allows information to be transmitted faster than light, because measuring one particle instantly affects the other particle's state regardless of distance."
  type: true-false
  answer: false
  explanation: "Measuring one entangled particle does instantly constrain the other's outcome — but no information is transmitted. Alice's measurement result is random and outside her control. Bob's results are also random. The correlations between their results (which can only be checked by comparing notes via a classical channel) are non-classical, but no bit of information travels between them. This is why the no-communication theorem holds: entanglement is a resource for correlations, not a channel for signals."

- question: "Why does the impossibility of factoring |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2 into a product of individual particle states mean that neither particle has its own individual quantum state?"
  type: short-answer
  answer: "A particle has an individual quantum state only if the two-particle system's state can be written as |ψ₁⟩⊗|ψ₂⟩ — a specific state for each particle independently. If that factorization is impossible, there is no |ψ₁⟩ to assign to particle 1 and no |ψ₂⟩ to assign to particle 2. The quantum information is encoded in correlations between the particles, not in the individual particles. All the physics — measurement outcomes, probabilities — is determined by the joint state, which cannot be decomposed into separate descriptions of the two parts."
  explanation: "This is what makes entanglement genuinely novel, not just strong classical correlation. Classical correlation (like a pair of gloves where finding one tells you about the other) is compatible with each object having its own definite properties. Quantum entanglement is not: the particles don't have definite individual properties; they have a joint state that predetermines their correlations without pre-assigning individual values. Bell's theorem (the next topic) makes this distinction mathematically precise."
```

## Explainer

You already know from kets and bras how to write a quantum state as a vector in Hilbert space. A single spin-½ particle has states |↑⟩ and |↓⟩ as a basis, and a general state is a superposition α|↑⟩ + β|↓⟩. For two particles that are **independent** — no interactions, no correlations — the combined system lives in the tensor product space, and the combined state factorizes: |Ψ⟩ = |ψ₁⟩ ⊗ |ψ₂⟩ = (α|↑⟩ + β|↓⟩) ⊗ (γ|↑⟩ + δ|↓⟩). In this case, measuring particle 1 tells you nothing new about particle 2 beyond what you already knew.

**Entanglement** arises when the two-particle state cannot be written as such a product. The canonical example is the **Bell state** |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2. Try to factor it: |Φ⁺⟩ = (a|↑⟩ + b|↓⟩) ⊗ (c|↑⟩ + d|↓⟩) would require ac = 1/√2, ad = 0, bc = 0, bd = 1/√2. The equations ad = 0 and bc = 0 force either a or d to be zero, and either b or c to be zero — but then ac or bd would also be zero, contradicting ac = bd = 1/√2. The state genuinely cannot be factored. Neither particle has an individual quantum state. They only have a joint state.

The physical consequence is striking. Before any measurement, each particle individually is in a completely mixed state — a 50/50 mixture of spin-up and spin-down. But the two particles are perfectly correlated: if you measure particle 1 and find ↑, the entire two-particle state collapses to |↑↑⟩, and particle 2 is now definitely ↑ as well, no matter how far away particle 2 is. This instantaneous correlation is not a signal — you cannot use it to send information faster than light, because the individual measurement outcomes are still random. But the correlations themselves exceed anything explainable by pre-existing ("hidden") properties of the individual particles, as Bell's theorem (the next topic) makes mathematically precise. Entanglement is the resource behind quantum teleportation, quantum cryptography, and quantum computing's potential for exponential speedup.
