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
status: validated
---

# Quantum Entanglement

## Core Idea
A two-particle state is entangled if it cannot be written as |ψ⟩₁ ⊗ |φ⟩₂. Entangled states exhibit correlations stronger than any classical correlation. Bell states (maximally entangled pairs) are fundamental resources for quantum communication and computation.

## Questions

```yaml
- question: "Alice and Bob share the Bell state |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2. Alice measures her particle and finds spin-up. What is the state of Bob's particle immediately after Alice's measurement, and can Alice use this to send Bob a message?"
  type: multiple-choice
  options:
    - "Bob's particle is still in superposition (|↑⟩ + |↓⟩)/√2, unaffected by Alice's distant measurement"
    - "Bob's particle is spin-up, and this was predetermined by a hidden variable set at the moment of entanglement"
    - "Bob's particle is spin-up, but Alice cannot use this to send a message because her own outcome was random and uncontrollable"
    - "Bob's particle is spin-down, since particles in a Bell state must have opposite spins"
  answer: 2
  explanation: "Measuring Alice's particle as spin-up projects |Φ⁺⟩ onto |↑↑⟩, instantly placing Bob's particle in |↑⟩. The correlation is real and nonlocal. But Alice cannot use this to send information: she got +½ randomly with 50% probability and had no control over the outcome — she cannot choose to send a '1' by getting spin-up. Option B (hidden variables) is what Einstein proposed but Bell's theorem rules out for local theories. Option D confuses |Φ⁺⟩ with the singlet state |Ψ⁻⟩ = (|↑↓⟩ − |↓↑⟩)/√2, which does have anti-correlated spins."

- question: "Alice and Bob share a maximally entangled pair. Alice measures spin-up. She immediately texts Bob: 'I got spin-up, so you must have spin-up too — I just transmitted information faster than light!' What is fundamentally wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — she did transmit one bit of information faster than light, but only probabilistically"
    - "Bob's individual outcomes are random and indistinguishable from a world where no entanglement exists; the correlation only appears when they compare results through a classical channel"
    - "The claim fails only because text messages travel slower than light; quantum signaling itself would be instantaneous"
    - "Alice cannot know Bob's result without measuring her particle first, introducing a delay"
  answer: 1
  explanation: "Bob's marginal distribution (the probabilities he observes for his own measurements) is exactly 50/50 regardless of whether Alice has measured, hasn't measured, or doesn't exist. There is no observable difference for Bob. The correlation between their outcomes — that they always agree — only becomes visible when they *compare* results via a classical channel, which is bounded by the speed of light. Information transfer requires the sender to control what the receiver observes; Alice cannot choose her outcome, so no message can be encoded."

- question: "Bell's theorem demonstrates that no theory based on local hidden variables can reproduce all the statistical predictions of quantum mechanics for entangled states."
  type: true-false
  answer: true
  explanation: "Bell's theorem (1964) derives an inequality that any local hidden variable theory must satisfy, but which quantum mechanics violates. The key insight is that the correlations in entangled states are too strong — they exceed what is possible if each particle carried predetermined values set at the moment of entanglement. Loophole-free experiments have confirmed quantum mechanics' predictions with overwhelming statistical confidence. Any explanation of entanglement via 'the particles agreed in advance' must therefore be either nonlocal (signaling faster than light) or non-realist (outcomes don't exist before measurement) — both abandoning core classical intuitions."

- question: "Quantum entanglement enables faster-than-light communication because measuring one particle of an entangled pair instantaneously determines the state of the other particle, regardless of the distance between them."
  type: true-false
  answer: false
  explanation: "While the correlation between measurement outcomes is instantaneous (nonlocal), it cannot be used to transmit information. Each particle's individual outcome is fundamentally random — Alice gets +½ or −½ with equal probability, regardless of Bob's situation, and cannot control which outcome she gets. Bob's outcomes are likewise random. Neither party can distinguish their situation from a world without entanglement by looking only at their own results. The correlation only emerges when both parties compare results through a classical (light-speed-limited) channel. No superluminal signal is transmitted."

- question: "Why can't Alice and Bob use quantum entanglement to send information faster than light, even though measuring Alice's particle instantaneously determines the state of Bob's particle?"
  type: short-answer
  answer: "Entanglement produces correlations between measurement outcomes, but each individual outcome is fundamentally random and uncontrollable. Alice cannot choose to get spin-up; she gets a random result with 50% probability. Bob similarly gets a random result with 50/50 distribution — the same distribution he would see whether or not Alice has measured, and whether or not they share entanglement. There is no observable difference for Bob. The correlation between their outcomes — only visible when they compare results — requires a classical channel, which is bounded by the speed of light. Since information transfer requires the sender to control what the receiver observes, and entanglement provides no such control, no FTL signaling is possible."
  explanation: "This is why entanglement is useful for quantum key distribution (sharing random bits securely) and quantum teleportation (transmitting quantum states, not classical information), but never for faster-than-light communication. The randomness of individual outcomes is not a limitation to overcome — it is fundamental to why quantum mechanics remains consistent with special relativity."
```

## Explainer

From the quantum postulates you already know, combining two quantum systems means forming their **tensor product**: the joint state space is H₁ ⊗ H₂, and if each particle is independently in a definite state, the two-particle state is a product |ψ⟩₁ ⊗ |φ⟩₂. Entanglement is simply the existence of two-particle states that *cannot* be factored this way. The canonical example is the **Bell state** |Φ⁺⟩ = (|↑↑⟩ + |↓↓⟩)/√2. There is no way to write this as (a|↑⟩ + b|↓⟩) ⊗ (c|↑⟩ + d|↓⟩) for any complex numbers a, b, c, d. The two particles are correlated at the level of the wavefunction itself, not merely through shared classical information.

The striking consequence is what happens at measurement. Before measurement, neither particle has a definite spin — that is standard superposition. But when you measure particle 1 and find it spin-up, particle 2 is *instantly* in the state |↑⟩, no matter how far away it is. Einstein called this "spooky action at a distance" and argued it proved quantum mechanics was incomplete — that the particles must have had hidden definite values all along. Bell's theorem (the topic this builds toward) proves that argument wrong: no local hidden variable theory can reproduce all the correlations that entangled states predict, and experiments confirm quantum mechanics wins. The correlations are real, nonlocal, and cannot be explained by any pre-assigned values.

It is essential to distinguish entanglement from signaling. Although the correlation is instantaneous, you cannot use it to send information faster than light. When you measure particle 1, you get a random outcome (+½ or −½ with equal probability). You learn your result, but you cannot *choose* which outcome you get, so you cannot encode a message that particle 2's owner reads from their measurement. The nonlocality is in the correlations — only visible when the two parties later *compare* their results — not in any individual outcome. This is why entanglement is useful for quantum key distribution (shared randomness) and quantum teleportation (transmitting quantum states), but never for faster-than-light communication.

**Entanglement entropy** quantifies how entangled a state is. For a bipartite pure state, trace out one subsystem to get a reduced density matrix ρ₁, then compute S = −Tr(ρ₁ log ρ₁). For a product state, ρ₁ is a pure state and S = 0. For a maximally entangled Bell state, ρ₁ = I/2 (the maximally mixed state) and S = log 2 — one full qubit of entanglement. This measure connects entanglement theory to quantum information, condensed matter (entanglement in many-body ground states), and even quantum gravity (the holographic principle). Entanglement is not a curiosity; it is one of the central resources distinguishing quantum from classical computation and communication.
