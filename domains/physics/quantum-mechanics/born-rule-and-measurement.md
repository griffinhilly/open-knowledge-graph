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
stage: advanced
status: validated
---

# Born Rule and Quantum Measurement

## Core Idea
The Born rule states that the probability of measuring eigenvalue aₙ of observable A in state |ψ⟩ is |⟨aₙ|ψ⟩|². Upon measurement, the state collapses to the corresponding eigenstate. This rule connects the wavefunction to experimental predictions.

## Questions

```yaml
- question: "A particle is in state |ψ⟩ = (3/5)|a₁⟩ + (4/5)|a₂⟩. What is the probability of measuring eigenvalue a₁?"
  type: multiple-choice
  options:
    - "3/5, because that is the coefficient of the eigenstate |a₁⟩"
    - "9/25, because the Born rule gives the modulus squared of the amplitude"
    - "1/2, because there are only two possible outcomes and they must be equally likely"
    - "4/5, because the larger coefficient dominates the measurement outcome"
  answer: 1
  explanation: "The Born rule states P(aₙ) = |⟨aₙ|ψ⟩|². The amplitude for a₁ is 3/5, so the probability is |3/5|² = 9/25. The amplitude itself (3/5) is not the probability — this is the most common error. Note that P(a₂) = |4/5|² = 16/25, and 9/25 + 16/25 = 1, confirming completeness. The amplitude is a complex number that carries phase information; the probability discards the phase by taking the modulus squared."

- question: "After measuring a particle's spin and finding it to be spin-up, a student argues that the Schrödinger equation will now evolve the state back into a superposition of spin-up and spin-down over time. What is correct about this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — the Schrödinger equation always eventually restores a superposition"
    - "The Schrödinger equation governs unitary evolution between measurements; state collapse upon measurement is a separate postulate that instantly projects the state into the measured eigenstate"
    - "The student is correct only if the spin-up state is not an energy eigenstate"
    - "The student is wrong because superpositions only arise for particles with many degrees of freedom"
  answer: 1
  explanation: "This gets at a deep feature of quantum measurement. The Schrödinger equation describes smooth, continuous, unitary evolution of the wavefunction between measurements — it never produces collapse. State collapse is a separate postulate: upon measurement yielding aₙ, the state instantly becomes |aₙ⟩. This discontinuity is not derived from the Schrödinger equation; it is an additional rule. The post-measurement state |↑⟩ will then evolve unitarily under Schrödinger — but that evolution will only produce a superposition again if the Hamiltonian mixes spin states (e.g., in a magnetic field in a different direction)."

- question: "If a system is already in an eigenstate of the observable being measured, the Born rule predicts that measurement yields the corresponding eigenvalue with probability 1."
  type: true-false
  answer: true
  explanation: "If |ψ⟩ = |aₙ⟩, then ⟨aₙ|ψ⟩ = ⟨aₙ|aₙ⟩ = 1, and for all m ≠ n, ⟨aₘ|ψ⟩ = ⟨aₘ|aₙ⟩ = 0 by orthogonality. So P(aₙ) = 1 and P(aₘ) = 0 for all other eigenvalues. This is consistent with the collapse postulate: if you measure a system already in an eigenstate, you get that eigenvalue with certainty, and the state after measurement is unchanged."

- question: "The probability amplitude ⟨aₙ|ψ⟩ directly gives the probability of measuring eigenvalue aₙ."
  type: true-false
  answer: false
  explanation: "The probability amplitude ⟨aₙ|ψ⟩ is a complex number, not a probability. Probabilities must be real and between 0 and 1. The Born rule takes the modulus squared: P(aₙ) = |⟨aₙ|ψ⟩|². Taking the modulus squared discards phase information and produces a real non-negative number. The amplitude itself carries phase, which is physically meaningful for interference phenomena — but it is not directly observable. Confusing amplitude with probability is one of the most common errors in introductory quantum mechanics."

- question: "Why is state collapse described as a separate postulate from the Schrödinger equation, and what experimental consequence demonstrates that collapse actually occurs?"
  type: short-answer
  answer: "The Schrödinger equation describes unitary, continuous, deterministic evolution — it never causes a state to jump discontinuously into a single eigenstate. Collapse is a separate, non-unitary postulate. The experimental consequence: if you immediately repeat the same measurement after obtaining eigenvalue aₙ, you always get aₙ again. This is consistent with the collapsed state being |aₙ⟩, which yields aₙ with probability 1."
  explanation: "If there were no collapse — if the state continued to evolve unitarily after measurement — then a second identical measurement would generally not give the same result, because the state would have evolved away from the eigenstate. The fact that repeated measurements give the same result (immediately after the first) is direct experimental evidence for collapse. This is also why measuring in a different basis after the first measurement generally gives random results: the collapse into |aₙ⟩ creates a definite state in the original basis, but that state is typically a superposition in other bases."
```

## Explainer

Quantum mechanics describes physical systems with wavefunctions — mathematical objects that encode all knowable information about a system. But wavefunctions don't directly tell you what you'll observe when you make a measurement. The **Born rule** is the bridge: it converts the abstract wavefunction into concrete probability predictions.

From your study of quantum postulates, you know that observables are represented by Hermitian operators, each with a set of eigenvalues (possible measurement results) and eigenstates. The Born rule states: if a system is in state |ψ⟩ and you measure observable A, the probability of obtaining eigenvalue aₙ is P(aₙ) = |⟨aₙ|ψ⟩|². The inner product ⟨aₙ|ψ⟩ is the **probability amplitude** — a complex number. Its modulus squared gives the probability. If the state is already an eigenstate, the probability is 1 for that eigenvalue and 0 for all others. If the state is a superposition, probabilities spread across multiple outcomes. Note that the probabilities sum to 1 by completeness: Σₙ |⟨aₙ|ψ⟩|² = 1.

The second part of the rule is **state collapse**: after a measurement yields aₙ, the state instantaneously becomes the eigenstate |aₙ⟩. This is not described by the Schrödinger equation — it is a separate postulate. Before measurement, the system is in a superposition; measurement forces it into a definite state. This is philosophically contentious (it underlies the "measurement problem" this topic builds toward) but experimentally confirmed: if you immediately repeat the same measurement, you get the same result with certainty, consistent with the system now being in eigenstate |aₙ⟩.

Consider a spin-1/2 particle prepared in the state |ψ⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩. The Born rule gives P(↑) = |⟨↑|ψ⟩|² = |1/√2|² = 1/2 and similarly P(↓) = 1/2. After measuring spin-up, the state collapses to |↑⟩. A follow-up spin-z measurement gives ↑ with certainty. But if instead you measure spin-x after the first measurement, the probabilities are again 50/50 — because the collapsed state |↑⟩ is an equal superposition in the x-eigenbasis. Repeated measurements in different bases reveal the full structure of the wavefunction. The Born rule is the most experimentally tested postulate in all of physics; no experiment has ever contradicted it.
