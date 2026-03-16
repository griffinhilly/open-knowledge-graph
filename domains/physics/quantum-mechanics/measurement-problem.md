---
id: measurement-problem
title: The Measurement Problem
domain: physics
course: quantum-mechanics
prerequisites:
- id: born-rule-and-measurement
  type: hard
- id: entanglement
  type: soft
tags:
- measurement
- foundations
stage: abstract-reasoning
status: draft
---

# The Measurement Problem

## Core Idea
The measurement problem is the tension between unitary evolution and probabilistic collapse. If apparatus and system are both quantum, the combined state remains pure and superposed. Why do we observe definite outcomes? Various interpretations (Copenhagen, Many-Worlds, Bohmian, Objective Collapse) offer different resolutions.

## Explainer

You know the Born rule: if a quantum system is in a superposition |ψ⟩ = α|0⟩ + β|1⟩, measurement yields outcome 0 with probability |α|² and outcome 1 with probability |β|², after which the state "collapses" to the corresponding eigenstate. You also know about entanglement — that two systems interacting quantum mechanically can become correlated in a way that cannot be described by separate states. The measurement problem asks: where does collapse come from, and is it even a real physical process?

Here is the puzzle stated sharply. A measuring apparatus is made of atoms — it is, in principle, a quantum system. When apparatus and particle interact, the Schrödinger equation governs the combined system and evolves it unitarily: |ready⟩|ψ⟩ → α|reads-0⟩|0⟩ + β|reads-1⟩|1⟩. The apparatus and particle are now **entangled**: the full system is in a superposition of "apparatus reads 0 and particle is in |0⟩" and "apparatus reads 1 and particle is in |1⟩." According to the Schrödinger equation, no collapse has occurred — the state is still a superposition. But you, looking at the apparatus, see a definite result. This gap between what the mathematics predicts (persistent superposition) and what observers experience (definite outcomes) is the measurement problem.

**Decoherence** partially explains this gap without resolving it completely. The apparatus interacts with trillions of environmental degrees of freedom (air molecules, photons, phonons), entangling the quantum state with the environment. Once this entanglement spreads, the off-diagonal elements of the reduced density matrix — the interference terms — become negligibly small at any accessible scale. The superposition still exists, but measuring interference between the branches requires accessing all environmental degrees of freedom simultaneously, which is thermodynamically impossible. Decoherence explains why we don't observe macroscopic superpositions; it does not explain why *one* outcome occurs rather than another.

The four main interpretations each cut the remaining knot differently. **Copenhagen** treats collapse as a primitive: measurement is a classical act that falls outside the quantum formalism, and asking what happens "during" measurement is meaningless. This is pragmatically powerful but philosophically incomplete. **Many-Worlds** (Everett) eliminates collapse entirely: the superposition is physically real, and the observer also becomes entangled and "branches" — in one branch they see outcome 0, in another they see outcome 1. All outcomes occur, but each branch is internally consistent. **Bohmian mechanics** retains definite particle trajectories guided by the wave function; outcomes are determined by initial conditions we cannot control (hidden variables), and apparent randomness reflects our ignorance. **Objective collapse theories** (GRW, CSL) modify the Schrödinger equation itself with random collapse terms that are negligible for microscopic systems but rapid for macroscopic ones. Each interpretation agrees with every experimental prediction of quantum mechanics — they are empirically equivalent — which is precisely why the problem remains unresolved.
