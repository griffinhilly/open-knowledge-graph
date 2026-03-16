---
id: measurement-problem-quantum
title: The Measurement Problem
domain: physics
course: quantum-mechanics
prerequisites:
- id: wavefunction-and-probability
  type: hard
builds-toward:
- interpretations-quantum-mechanics
tags:
- measurement-problem
- collapse
stage: abstract-reasoning
status: draft
---

# The Measurement Problem

## Core Idea
Why does |ψ⟩ collapse to an eigenstate upon measurement? This discontinuity is not from Schrödinger's equation. Different interpretations propose different resolutions.

## Explainer

From your study of the wavefunction, you know that |ψ⟩ encodes a probability distribution: before measurement, a particle can have a superposition of many outcomes with definite probabilities for each. But the moment you measure, you get one specific result, and the wavefunction "collapses" to the corresponding eigenstate. This jarring jump is the **measurement problem**: quantum mechanics gives no mechanism for it. Schrödinger's equation is smooth, deterministic, and linear — it does not produce sudden collapses on its own.

The problem has two layers. First, there is the **discontinuity**: unitary evolution under the Schrödinger equation preserves superpositions, yet measurement appears to destroy them. If the measuring device is also a quantum system (as it must be), then coupling the system to the device should produce an entangled superposition of (system state + device state) — not a definite outcome. Second, there is the **preferred basis** problem: why does a measurement of spin force a collapse into spin-up or spin-down, rather than some other basis? The formalism doesn't say which observable is "being measured" — you have to add that by hand.

Different interpretations give radically different answers. The **Copenhagen interpretation** declares that collapse is a primitive rule of quantum theory, not something to be derived — measurement is simply outside the theory's scope. The **many-worlds interpretation** denies that collapse happens at all: the entangled superposition of system and device really does persist, but the observer becomes entangled with one branch and cannot perceive the others. The **pilot wave (Bohmian) interpretation** posits hidden variables — the particle always has a definite position guided by the wavefunction, and "collapse" is just updating your knowledge. **Objective collapse theories** (like GRW) modify the Schrödinger equation to include stochastic terms that occasionally collapse the wavefunction spontaneously.

What makes this a deep problem rather than a philosophical quibble is that these interpretations make different empirical predictions in principle, even if they agree on all currently testable cases. The measurement problem also underlies practical challenges in quantum computing: decoherence (entanglement with the environment) effectively behaves like continuous measurement, destroying the superpositions that make quantum algorithms powerful. Understanding why and when quantum systems "collapse" is thus both a foundational question and an engineering one.
