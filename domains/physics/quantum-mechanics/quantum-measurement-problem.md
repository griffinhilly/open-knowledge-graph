---
id: quantum-measurement-problem
title: The Quantum Measurement Problem
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-measurement-postulate
  type: hard
- id: quantum-superposition
  type: soft
builds-toward:
- interpretations-quantum-mechanics
tags:
- measurement
- problem
- foundations
stage: advanced
status: draft
---

# The Quantum Measurement Problem

## Core Idea
The measurement problem arises from the apparent contradiction between unitary Schrödinger evolution (superposition preserved) and measurement (definite outcome). Why does measurement yield one outcome when the wavefunction represents superposition? Why does the wavefunction 'collapse'? How does the macroscopic measuring apparatus fit into quantum theory? No consensus resolution exists; different interpretations propose different solutions.

## Explainer

From the measurement postulate you know the operational rules: if you measure an observable on a system in state |ψ⟩ = Σcₙ|aₙ⟩, you get outcome aₙ with probability |cₙ|², and the state immediately after becomes |aₙ⟩. This **wavefunction collapse** is an additional postulate layered on top of the Schrödinger equation. The measurement problem is the question of whether this postulate is consistent, fundamental, or derivable — and nobody agrees on the answer.

Here is the tension precisely. The Schrödinger equation is **unitary**: it maps pure states to pure states and preserves superpositions. If the measuring apparatus itself obeys quantum mechanics (which it must, being made of atoms), then when it interacts with a quantum system in superposition, the combined system+apparatus state should evolve into an entangled superposition: |ψ⟩ = α|spin up⟩|meter reads up⟩ + β|spin down⟩|meter reads down⟩. This is sometimes called a **Schrödinger's cat state** — the meter is in superposition of two macroscopically distinct readings. But you never observe a meter in superposition. You always see a definite reading. So where does the superposition go, and why?

The proposed resolutions diverge sharply on what question they are answering. The **Copenhagen interpretation** sidesteps the problem by declaring that quantum mechanics applies to microscopic systems, and that a measurement is by definition an interaction with a classical apparatus that is outside the quantum description. This is pragmatically successful but conceptually unsatisfying — it never defines the boundary. **Many-worlds** (Everett) denies collapse entirely: the superposition persists, and both outcomes occur in branching copies of the universe. There is no collapse because there is no need for one — but the meaning of probability in this picture is contested. **Decoherence** (not itself an interpretation, but a mechanism) shows that entanglement with the environment rapidly destroys interference between macroscopic superposition branches, explaining why you cannot observe quantum interference in a meter — but it produces a mixed state, not a definite outcome, so it dissolves the appearance of the problem without fully solving it.

What makes the measurement problem genuinely hard is that it is not a gap in our ability to calculate. Quantum mechanics predicts experimental outcomes with extraordinary precision. The problem is interpretive: what does the formalism say about reality? The answer depends on whether you think the wavefunction is a complete description of an individual system, a description of ensembles, or merely an agent's knowledge. As you study interpretations of quantum mechanics next, you will see how different starting assumptions about these questions lead to radically different pictures of physical reality — while leaving all predictions unchanged.
