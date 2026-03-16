---
id: born-rule-and-measurement
title: Born Rule and Quantum Measurement
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
builds-toward:
- measurement-problem
- entanglement
- density-matrices
tags:
- measurement
- probability
stage: abstract-reasoning
status: draft
---

# Born Rule and Quantum Measurement

## Core Idea
The Born rule states that the probability of measuring eigenvalue aₙ of observable A in state |ψ⟩ is |⟨aₙ|ψ⟩|². Upon measurement, the state collapses to the corresponding eigenstate. This rule connects the wavefunction to experimental predictions.

## Explainer

Quantum mechanics describes physical systems with wavefunctions — mathematical objects that encode all knowable information about a system. But wavefunctions don't directly tell you what you'll observe when you make a measurement. The **Born rule** is the bridge: it converts the abstract wavefunction into concrete probability predictions.

From your study of quantum postulates, you know that observables are represented by Hermitian operators, each with a set of eigenvalues (possible measurement results) and eigenstates. The Born rule states: if a system is in state |ψ⟩ and you measure observable A, the probability of obtaining eigenvalue aₙ is P(aₙ) = |⟨aₙ|ψ⟩|². The inner product ⟨aₙ|ψ⟩ is the **probability amplitude** — a complex number. Its modulus squared gives the probability. If the state is already an eigenstate, the probability is 1 for that eigenvalue and 0 for all others. If the state is a superposition, probabilities spread across multiple outcomes. Note that the probabilities sum to 1 by completeness: Σₙ |⟨aₙ|ψ⟩|² = 1.

The second part of the rule is **state collapse**: after a measurement yields aₙ, the state instantaneously becomes the eigenstate |aₙ⟩. This is not described by the Schrödinger equation — it is a separate postulate. Before measurement, the system is in a superposition; measurement forces it into a definite state. This is philosophically contentious (it underlies the "measurement problem" this topic builds toward) but experimentally confirmed: if you immediately repeat the same measurement, you get the same result with certainty, consistent with the system now being in eigenstate |aₙ⟩.

Consider a spin-1/2 particle prepared in the state |ψ⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩. The Born rule gives P(↑) = |⟨↑|ψ⟩|² = |1/√2|² = 1/2 and similarly P(↓) = 1/2. After measuring spin-up, the state collapses to |↑⟩. A follow-up spin-z measurement gives ↑ with certainty. But if instead you measure spin-x after the first measurement, the probabilities are again 50/50 — because the collapsed state |↑⟩ is an equal superposition in the x-eigenbasis. Repeated measurements in different bases reveal the full structure of the wavefunction. The Born rule is the most experimentally tested postulate in all of physics; no experiment has ever contradicted it.
