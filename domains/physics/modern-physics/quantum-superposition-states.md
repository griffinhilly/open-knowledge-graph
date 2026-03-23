---
id: quantum-superposition-states
title: Quantum Superposition and Linear Combinations of States
domain: physics
course: modern-physics
prerequisites:
- id: wavefunction-probability-density
  type: hard
- id: quantum-superposition
  type: soft
- id: vector-spaces-definition
  type: hard
builds-toward:
- expectation-values-quantum
tags:
- quantum
- superposition
- states
stage: advanced
status: validated
---

# Quantum Superposition and Linear Combinations of States

## Core Idea
A quantum system can exist in a superposition of multiple eigenstates simultaneously, with relative amplitudes and phases determining the overall wavefunction ψ = Σ cₙφₙ. Measurement projects the system into one eigenstate with probability |cₙ|². Superposition is fundamentally different from classical uncertainty; it is an ontological feature of quantum reality.

## Questions

```yaml
- question: "A student says: 'Saying an electron is in a superposition of spin-up and spin-down is just like saying a coin is spinning in the air — it's either heads or tails, we just don't know which yet.' What is the key reason this analogy fails?"
  type: multiple-choice
  options:
    - "It fails because quantum objects cannot be compared to classical macroscopic objects"
    - "It fails because quantum superposition enables interference between components — a classical probability mixture cannot produce interference patterns, but a genuine superposition can"
    - "It fails because we can measure which spin-state the electron is in, whereas we cannot observe a coin mid-spin"
    - "It fails because the coin analogy applies only to discrete systems, while quantum states are continuous"
  answer: 1
  explanation: "The critical distinction is interference. A genuine quantum superposition carries relative phases between its components that produce constructive and destructive interference in experiments (double-slit, interferometers). A classical 'we don't know which' probability mixture has no phases and cannot produce interference — the fringe pattern would disappear. The empirical signature of true quantum superposition is these interference effects, which depend on the phases of the coefficients cₙ, not just their magnitudes. Classical ignorance and quantum superposition make different experimental predictions."

- question: "An electron is prepared as an equal superposition of spin-up and spin-down along the z-axis. Physicist A says it is 'in superposition.' Physicist B says it is 'in an eigenstate.' Are they contradicting each other?"
  type: multiple-choice
  options:
    - "Yes — an eigenstate is by definition not a superposition, so both cannot be correct simultaneously"
    - "No — the same state can be an eigenstate of one observable (spin-x) and a superposition of eigenstates of another (spin-z); whether a state 'is in superposition' depends entirely on the measurement basis"
    - "Yes — only one correct decomposition of a quantum state exists at any time"
    - "No — all quantum states are simultaneously eigenstates of every observable"
  answer: 1
  explanation: "An equal superposition of z-spin-up and z-spin-down is exactly the eigenstate of spin along the x-axis. Physicist A is measuring spin along z; physicist B is measuring spin along x. They are both correct, relative to their chosen basis. This is the deep insight: 'being in superposition' is not an intrinsic property of a state but a relationship between the state and a choice of observable. Every state is an eigenstate of some observable and a superposition of eigenstates of every non-commuting observable. Asking 'is this state in superposition?' without specifying the basis is not well-posed."

- question: "Measurement collapses a quantum superposition, projecting the system onto one eigenstate and destroying the superposition."
  type: true-false
  answer: true
  explanation: "Before measurement, the system evolves as a superposition ψ = Σcₙφₙ with each component carrying phase e^{-iEₙt/ℏ}. Measuring the corresponding observable instantaneously projects the system onto a single eigenstate φₙ with probability |cₙ|². The other components disappear — the superposition is destroyed. Subsequent measurements (before re-preparation) always return the same eigenstate, because the collapse has already selected it. To recover the original superposition, the system must be re-prepared from scratch."

- question: "The probability of obtaining eigenstate φₙ when measuring a system in state ψ = Σcₙφₙ is given by the coefficient cₙ itself."
  type: true-false
  answer: false
  explanation: "The probability is |cₙ|² — the squared modulus of the complex amplitude, not cₙ itself. The coefficients cₙ are complex numbers (probability amplitudes) with both magnitude and phase; they cannot directly be probabilities since they can be negative or imaginary. It is squaring the absolute value that yields a real, non-negative probability consistent with the normalization Σ|cₙ|² = 1. This distinction is physically crucial: the phases of cₙ drive quantum interference (which survives before measurement), while |cₙ|² gives the collapse probability (which discards the phase information)."

- question: "What is the key physical evidence that quantum superposition is fundamentally different from classical uncertainty, and what feature of the formalism produces this evidence?"
  type: short-answer
  answer: "The key evidence is quantum interference — constructive and destructive fringe patterns in experiments like the double-slit or Mach-Zehnder interferometer. These patterns depend on the relative phases of the coefficients cₙ in ψ = Σcₙφₙ. A classical probability distribution over definite states has no phase information and cannot produce interference: if you blocked each path and added the resulting distributions, you would get a smooth sum, not fringes. Only a genuine superposition, where both amplitude and phase are present in each term, can cancel in some directions and reinforce in others. The phase is the fingerprint of true quantum superposition; interference is its observable consequence."
  explanation: "This is why physicists say quantum superposition is an ontological claim, not an epistemic one. It is not that we lack information about which state the system is in — the system genuinely is in multiple states simultaneously, and the phases between them have real physical consequences that can be measured. When we measure, those phases are lost (the collapse is irreversible); but before measurement, they are as real as any other physical quantity."
```

## Explainer

From your study of vector spaces, you know that any vector can be written as a linear combination of basis vectors. In quantum mechanics, states work the same way: the wavefunction ψ lives in a Hilbert space, and any complete set of eigenstates {φₙ} forms a basis for that space. Writing ψ = Σ cₙφₙ is not a metaphor — it is a literal vector decomposition. The **coefficients cₙ** are complex numbers called **probability amplitudes**, and the square of each modulus, |cₙ|², gives the probability of finding the system in eigenstate φₙ if you measure the corresponding observable. The normalization condition ⟨ψ|ψ⟩ = 1 requires Σ |cₙ|² = 1, which is just the statement that probabilities sum to one.

The critical conceptual leap is understanding what this superposition *means* before measurement. A classical coin spinning in the air is either heads or tails — you just do not know which. A quantum particle in a superposition of energy eigenstates is genuinely *not* in any single eigenstate; both terms are simultaneously present and physically real. The clearest evidence is **quantum interference**: if you prepare two paths through an interferometer so their probability amplitudes add in one direction and cancel in another, you get bright and dark fringes. This pattern depends on the *phases* of the coefficients cₙ, not just their magnitudes. A classical probability mixture cannot produce interference; only a genuine superposition can.

**Measurement** collapses the superposition. Before you measure, the system evolves as a superposition, with each component φₙ carrying its own time evolution e^{-iEₙt/ℏ}. The relative phases between terms oscillate, driving interference phenomena like the beating between energy levels. When you perform a measurement of the observable whose eigenstates are {φₙ}, the wavefunction instantaneously projects onto one eigenstate φₙ with probability |cₙ|². After measurement, the other terms are gone — the superposition is destroyed. This is why repeated measurements of the same state (before re-preparation) do not yield a distribution: the first measurement collapses the state.

The deeper lesson is that the basis matters. An electron in a superposition of spin-up and spin-down along the z-axis is simultaneously in a definite eigenstate of spin along some other axis. "Is the electron in a superposition?" is not a well-posed question without specifying: superposition of *which* observable's eigenstates? Every quantum state is an eigenstate of some observable and a superposition of eigenstates of every non-commuting observable. Superposition is not a special condition of a state — it is the generic condition, relative to most measurement bases.
