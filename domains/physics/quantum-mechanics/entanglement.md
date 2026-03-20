---
id: entanglement
title: Quantum Entanglement
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
builds-toward:
- bell-inequalities
- measurement-problem
tags:
- entanglement
- correlations
stage: advanced
status: draft
---

# Quantum Entanglement

## Core Idea
A two-particle state is entangled if it cannot be written as |ψ⟩₁ ⊗ |φ⟩₂. Entangled states exhibit correlations stronger than any classical correlation. Bell states (maximally entangled pairs) are fundamental resources for quantum communication and computation.

## Explainer

From the quantum postulates you already know, combining two quantum systems means forming their **tensor product**: the joint state space is H₁ ⊗ H₂, and if each particle is independently in a definite state, the two-particle state is a product |ψ⟩₁ ⊗ |φ⟩₂. Entanglement is simply the existence of two-particle states that *cannot* be factored this way. The canonical example is the **Bell state** |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2. There is no way to write this as (a|↑⟩ + b|↓⟩) ⊗ (c|↑⟩ + d|↓⟩) for any complex numbers a, b, c, d. The two particles are correlated at the level of the wavefunction itself, not merely through shared classical information.

The striking consequence is what happens at measurement. Before measurement, neither particle has a definite spin — that is standard superposition. But when you measure particle 1 and find it spin-up, particle 2 is *instantly* in the state |↑⟩, no matter how far away it is. Einstein called this "spooky action at a distance" and argued it proved quantum mechanics was incomplete — that the particles must have had hidden definite values all along. Bell's theorem (the topic this builds toward) proves that argument wrong: no local hidden variable theory can reproduce all the correlations that entangled states predict, and experiments confirm quantum mechanics wins. The correlations are real, nonlocal, and cannot be explained by any pre-assigned values.

It is essential to distinguish entanglement from signaling. Although the correlation is instantaneous, you cannot use it to send information faster than light. When you measure particle 1, you get a random outcome (+½ or −½ with equal probability). You learn your result, but you cannot *choose* which outcome you get, so you cannot encode a message that particle 2's owner reads from their measurement. The nonlocality is in the correlations — only visible when the two parties later *compare* their results — not in any individual outcome. This is why entanglement is useful for quantum key distribution (shared randomness) and quantum teleportation (transmitting quantum states), but never for faster-than-light communication.

**Entanglement entropy** quantifies how entangled a state is. For a bipartite pure state, trace out one subsystem to get a reduced density matrix ρ₁, then compute S = −Tr(ρ₁ log ρ₁). For a product state, ρ₁ is a pure state and S = 0. For a maximally entangled Bell state, ρ₁ = I/2 (the maximally mixed state) and S = log 2 — one full qubit of entanglement. This measure connects entanglement theory to quantum information, condensed matter (entanglement in many-body ground states), and even quantum gravity (the holographic principle). Entanglement is not a curiosity; it is one of the central resources distinguishing quantum from classical computation and communication.
