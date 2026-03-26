---
id: quantum-measurement-postulate
title: Quantum Measurement and Collapse
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
- id: state-vectors-and-wavefunctions
  type: hard
builds-toward:
- measurement-problem-quantum
- interpretations-quantum-mechanics
tags:
- measurement
- collapse
- interpretation
stage: advanced
status: validated
---

# Quantum Measurement and Collapse

## Core Idea
Measurement of an observable forces the quantum state to collapse into an eigenstate of the measurement operator, with outcome equal to the corresponding eigenvalue. The probability of measuring eigenvalue λₙ equals |⟨φₙ|ψ⟩|², where |φₙ⟩ is the corresponding eigenstate. After measurement, the system remains in the collapsed state until further interaction.

## Questions

```yaml
- question: "An electron is prepared in the spin state |ψ⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩. A student says: 'The spin is already either up or down before we measure — we just don't know which.' What does quantum mechanics actually claim?"
  type: multiple-choice
  options:
    - "The student is correct; the probabilistic description reflects our ignorance of a pre-existing hidden variable"
    - "The spin is genuinely indeterminate before measurement — not unknown but pre-existing — as demonstrated by interference experiments showing both components are simultaneously real"
    - "The statement is meaningless; quantum mechanics only predicts measurement outcomes and makes no claim about pre-measurement reality"
    - "The electron has both up and down spin simultaneously, meaning the measured spin is always zero"
  answer: 1
  explanation: "This is the central conceptual break between quantum mechanics and classical probability. In classical probability, a coin flip has a definite outcome we don't know; in quantum mechanics, the spin state before measurement is genuinely indeterminate. The experimental evidence is interference: in a Mach-Zehnder interferometer, a photon takes 'both paths' simultaneously, and closing one path changes the interference pattern — proving both paths were physically real, not just unknown. A hidden-variable theory would require the outcomes to be predetermined, but Bell's theorem and experiment rule out local hidden variables. The indeterminacy is not epistemic (ignorance) but ontological (there is no definite value)."

- question: "After measuring the energy of a quantum system and obtaining eigenvalue Eₙ (eigenstate |φₙ⟩), the system is immediately measured for energy again. What result do you expect?"
  type: multiple-choice
  options:
    - "A random outcome with the same probability distribution as the first measurement, since collapse is a one-time event"
    - "Definitely Eₙ, because after collapse the system is in eigenstate |φₙ⟩ and measuring an eigenstate always returns its eigenvalue with certainty"
    - "A superposition of all possible energies, since the second measurement triggers a new collapse from a fresh superposition"
    - "An uncertain result that depends on the time elapsed since the first measurement, as the state evolves under the Schrödinger equation between measurements"
  answer: 1
  explanation: "After collapse to eigenstate |φₙ⟩, the system is no longer in superposition — it is in a definite eigenstate. Measuring an observable on an eigenstate of that observable always returns the corresponding eigenvalue with probability 1. This repeatability is physically essential: it is what makes classical records possible. A detector click, a pointer position, a photographic trace — all are stable because after measurement collapses the state, subsequent measurements confirm the same result. Option D would be relevant if significant time passes and the state evolves under the Hamiltonian between measurements, but for immediate remeasurement the evolved state is still effectively |φₙ⟩."

- question: "The Born rule — that measuring observable  on state |ψ⟩ yields eigenvalue λₙ with probability |⟨φₙ|ψ⟩|² — cannot be derived from the Schrödinger equation and is a fundamental postulate of quantum mechanics."
  type: true-false
  answer: true
  explanation: "This is a foundational fact about quantum mechanics. The Schrödinger equation is deterministic and linear — it evolves superpositions smoothly and never collapses them. The Born rule is separately postulated to connect the wavefunction (a mathematical object) to probabilities of measurement outcomes (physically observable quantities). Attempts to derive the Born rule from the Schrödinger equation alone (e.g., in Many-Worlds interpretations) remain controversial. The fact that the Born rule cannot be derived from unitary evolution is part of what makes the measurement problem so conceptually deep."

- question: "Wavefunction collapse is just the quantum mechanical version of updating a classical probability distribution upon learning new information — both are knowledge updates with no additional physical significance."
  type: true-false
  answer: false
  explanation: "This is the most seductive wrong interpretation of collapse. In classical probability, updating reflects a change in knowledge about a pre-existing definite state. In quantum mechanics, before measurement there is no pre-existing definite value — the superposed states are physically real, as demonstrated by interference. Collapse is not a knowledge update but a physical transition from a superposition of genuinely real possibilities to a single definite outcome. The difference is empirical: closing one arm of an interferometer destroys the interference pattern, proving the 'unchosen' path was physically present. A mere knowledge update about a definite hidden state would not produce or destroy interference."

- question: "The Schrödinger equation is linear and unitary, meaning it preserves superpositions and never produces collapse. But measurement appears to collapse superpositions discontinuously. Why does this mismatch constitute 'the measurement problem,' and why can't it be resolved by simply treating collapse as an approximation?"
  type: short-answer
  answer: "The measurement problem is that quantum mechanics has two apparently incompatible dynamics: the Schrödinger equation (linear, unitary, continuous, deterministic) and measurement collapse (nonlinear, non-unitary, discontinuous, probabilistic). The Schrödinger equation predicts that when a quantum system interacts with a measuring device, the combined system evolves into a superposition of device-states (pointer pointing left AND pointer pointing right). But we never observe superposed pointers — we observe definite outcomes. Calling collapse an 'approximation' doesn't work because it would require specifying when and why the Schrödinger equation stops applying. Any rule for when collapse happens must break the linearity that is central to quantum mechanics. The problem is not about precision but about fundamental consistency: the theory contains two incompatible dynamical rules and no principled criterion for when each applies."
  explanation: "Different interpretations resolve this differently: Copenhagen says collapse is not a physical process but a transition in our description; Many-Worlds says collapse never happens and all branches are real; spontaneous collapse theories (GRW) modify the Schrödinger equation to include collapse dynamically. All are consistent with known experiments, and none is universally accepted."
```

## Explainer

From your study of state vectors and wavefunctions, you know that a quantum state |ψ⟩ can be expressed as a superposition of basis states. From the quantum postulates, you know that observable quantities correspond to Hermitian operators whose eigenstates form a complete basis. The measurement postulate tells you what happens when you actually observe a system in superposition — and the answer is discontinuous and irreversible in a way that nothing in classical physics prepares you for.

Suppose the state is |ψ⟩ = Σ cₙ |φₙ⟩, where |φₙ⟩ are the eigenstates of some observable Â with eigenvalues λₙ. Before measurement, the system is genuinely in all states simultaneously — this is not mere ignorance about a pre-existing value. When you measure Â, you get exactly one result: some particular λₙ, with probability |cₙ|² = |⟨φₙ|ψ⟩|². This is the **Born rule**, and it is one of the foundational postulates — it cannot be derived from the Schrödinger equation alone. Immediately after the measurement, the state collapses: |ψ⟩ → |φₙ⟩. All other terms in the superposition disappear, and subsequent measurements of the same observable will yield λₙ with certainty.

Two features make collapse radically different from classical probability. First, the outcome is not just unknown before measurement — it is genuinely indeterminate. An electron approaching a half-silvered mirror is not secretly going either left or right; interference experiments prove the two paths are simultaneously real. Second, **collapse is not Schrödinger evolution**. The Schrödinger equation is linear and unitary — it never collapses a superposition. Measurement introduces a discontinuous jump that sits outside the ordinary dynamics. This mismatch is called the **measurement problem**, and it is the deepest unresolved conceptual issue in quantum foundations.

A useful way to build intuition: think of the inner product ⟨φₙ|ψ⟩ as the "overlap amplitude" between the system state and the eigenstate you're projecting onto. The probability is the square of this amplitude. Orthogonal eigenstates (⟨φₙ|φₘ⟩ = 0 for n ≠ m) mean that if you measure and get λₙ, the probability of immediately getting λₘ in a second measurement is zero. Repeated measurements of the same observable on the same collapsed state always return the same value — because after collapse, the state is already an eigenstate. This repeatability is why measurement collapse is physically essential: it is what makes classical records (pointer positions, detector clicks) possible.
