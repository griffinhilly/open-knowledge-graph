---
id: entanglement-quantum
title: Quantum Entanglement
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-superposition
  type: hard
builds-toward:
- bell-theorem-inequalities
tags:
- entanglement
- non-locality
- correlations
stage: advanced
status: draft
---

# Quantum Entanglement

## Core Idea
Entangled states cannot be written as products of individual particle states. A classic example is the Bell state |ψ⟩ = 1/√2(|↑↓⟩ + |↓↑⟩), where measuring one particle's spin instantly determines the other's regardless of separation. Entanglement reveals non-local correlations without faster-than-light communication. It cannot be created by local operations alone and is a resource for quantum computing.

## Explainer

From superposition you know that a single quantum system can exist in a combination of multiple states until measured. Entanglement extends this idea to multi-particle systems — and produces something genuinely new. Start with two particles that each independently have some quantum state. A **product state** like |↑⟩₁|↓⟩₂ simply means particle 1 is spin-up and particle 2 is spin-down: you can describe each particle separately. An **entangled state** is one where this is impossible. The Bell state |ψ⟩ = (1/√2)(|↑↓⟩ + |↓↑⟩) cannot be factored into separate descriptions for each particle. There is no definite answer to "what spin does particle 1 have?" — not because we don't know, but because the question has no answer until a measurement is made.

Here is what makes entanglement strange. Before measurement, neither particle has a definite spin. But the moment you measure particle 1 and find it spin-up, particle 2 is instantly in state |↓⟩ — no matter how far away it is. This **non-local correlation** is real and measurable: if you collect many such pairs and compare results (which requires a classical communication channel), the correlations violate the Bell inequalities, ruling out any "hidden variables" explanation where the particles carried pre-determined spins all along. The correlations are stronger than anything classically possible.

Does this allow faster-than-light communication? No, and the reason is subtle. When you measure particle 1, you get a random result — 50% up, 50% down. You cannot control which outcome you get, so you cannot use it to send a message. Only when you compare your result with your distant partner's result (over a normal, slower-than-light channel) does the correlation become visible. The non-locality is real but unleverageable for signaling.

Entanglement also has a production constraint: **local operations and classical communication (LOCC)** cannot create entanglement. If two particles start unentangled and never interact, no amount of local operations on each particle separately can produce an entangled state. Entanglement must be created through physical interaction — typically by letting particles interact in a way that correlates their states, such as scattering events or joint measurements. This is why entanglement is treated as a **resource** in quantum information: it must be manufactured, stored carefully, and consumed when used. Applications like quantum teleportation and superdense coding use pre-shared entangled pairs as the fuel that enables their protocols to outperform anything classically achievable.
