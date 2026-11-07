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
Measurement of an observable forces the quantum state to collapse into an eigenstate of the measurement operator, with outcome equal to the corresponding eigenvalue. The probability of measuring eigenvalue λₙ equals |⟨φₙ|ψ⟩|², where |φₙ⟩ is the corresponding eigenstate. Immediately after measurement, the system is in the collapsed state; it then evolves under the Hamiltonian as usual, so it stays in that eigenstate only if the eigenstate is also stationary.

## How It's Best Learned
Run a three-step sequence on a spin-½ state with the matrices in hand. Measure S_z, then S_x, then S_z again, writing the state and the outcome probabilities after each step. The final S_z result is random again, even though the first one was definite. Then repeat with a second S_z measurement in place of S_x and compare the two runs.

## Common Misconceptions
- Once A has been measured, any later measurement of A gives the same value, whatever happens in between. (A measurement of an observable that does not commute with A puts the system in a superposition of A-eigenstates again. A later measurement of A can then give a different value.)
- When an eigenvalue is degenerate, the state collapses onto one particular eigenvector. (The state is projected onto the whole eigenspace for that eigenvalue. The probability is the sum of |⟨φ|ψ⟩|² over an orthonormal basis of that eigenspace.)
- The phases of the coefficients cₙ change the probabilities of measuring A. (Those probabilities depend only on |cₙ|². The relative phases do change the probabilities for other observables that do not commute with A.)

## Questions

```yaml
- question: "An electron is prepared in the spin state |ψ⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩. A student says: 'The spin is already either up or down before we measure — we just don't know which.' What does quantum mechanics actually claim?"
  type: multiple-choice
  options:
    - "The student is correct; the probabilistic description reflects our ignorance of a pre-existing hidden variable"
    - "The state is not an unknown choice between up and down: it is a definite superposition (spin-up along x), and measuring S_x gives +ℏ/2 every time, which no 50/50 mixture of up and down could do"
    - "The statement is meaningless; quantum mechanics only predicts measurement outcomes and makes no claim about pre-measurement reality"
    - "The electron has both up and down spin simultaneously, meaning the measured spin is always zero"
  answer: 1
  explanation: "This is the central conceptual break between quantum mechanics and classical probability. The student describes a 50/50 mixture of |↑⟩ and |↓⟩, like a coin whose face we haven't seen. The given state is different: it equals |+x⟩, spin-up along x. On it, an S_x measurement gives +ℏ/2 with certainty; on the mixture, S_x gives +ℏ/2 and −ℏ/2 half the time each. Interference shows the same difference: with both arms of a balanced Mach-Zehnder interferometer open, every photon reaches one detector, whereas a mixture of 'went one way' and 'went the other way' would split them 50/50. Bell's theorem and experiment also rule out local hidden variables carrying predetermined values. Whether the pre-measurement value is ontologically indeterminate is interpretation-dependent: standard accounts say there is no definite value, while nonlocal hidden-variable theories such as Bohmian mechanics, which are not ruled out, describe things differently. None of them supports the student's simple mixture picture."

- question: "After measuring the energy of a quantum system and obtaining eigenvalue Eₙ (eigenstate |φₙ⟩), the system is immediately measured for energy again. What result do you expect?"
  type: multiple-choice
  options:
    - "A random outcome with the same probability distribution as the first measurement, since collapse is a one-time event"
    - "Definitely Eₙ, because after collapse the system is in eigenstate |φₙ⟩ and measuring an eigenstate always returns its eigenvalue with certainty"
    - "A superposition of all possible energies, since the second measurement triggers a new collapse from a fresh superposition"
    - "An uncertain result that depends on the time elapsed since the first measurement, as the state evolves under the Schrödinger equation between measurements"
  answer: 1
  explanation: "After collapse to eigenstate |φₙ⟩, the system is no longer in superposition — it is in a definite eigenstate. Measuring an observable on an eigenstate of that observable always returns the corresponding eigenvalue with probability 1. This repeatability is physically essential: it is what makes classical records possible. A detector click, a pointer position, a photographic trace — all are stable because after measurement collapses the state, subsequent measurements confirm the same result. Option D is wrong here even for a delayed remeasurement: an energy eigenstate of an isolated system evolves only by a phase factor e^(−iEₙt/ℏ), so its energy stays Eₙ. (Elapsed time does matter when remeasuring an observable that does not commute with the Hamiltonian.)"

- question: "The Born rule — that measuring observable  on state |ψ⟩ yields eigenvalue λₙ with probability |⟨φₙ|ψ⟩|² — cannot be derived from the Schrödinger equation and is a fundamental postulate of quantum mechanics."
  type: true-false
  answer: true
  explanation: "This is a foundational fact about quantum mechanics. The Schrödinger equation is deterministic and linear — it evolves superpositions smoothly and never collapses them. The Born rule is separately postulated to connect the wavefunction (a mathematical object) to probabilities of measurement outcomes (physically observable quantities). Attempts to derive the Born rule from the Schrödinger equation alone (e.g., in Many-Worlds interpretations) remain controversial. The fact that the Born rule cannot be derived from unitary evolution is part of what makes the measurement problem so conceptually deep."

- question: "Wavefunction collapse is exactly like updating a classical probability distribution over pre-existing definite values: the superposition only expressed our ignorance of which value the system already had."
  type: true-false
  answer: false
  explanation: "Whether collapse is a physical process or an update of the observer's information is interpretation-dependent: Copenhagen-style and information-based views treat it as an update of the description, while objective collapse theories make it physical. What is not open is the classical picture in the statement. A superposition is not ignorance of a pre-existing value, and the difference is empirical: with both arms of a balanced interferometer open, every photon reaches one detector, whereas a mixture of 'went one way' and 'went the other way' would split them 50/50. A knowledge update about a definite hidden value of which-path would not produce that interference. So even on informational views, collapse is not a classical Bayesian update over pre-existing values."

- question: "The Schrödinger equation is linear and unitary, meaning it preserves superpositions and never produces collapse. But measurement appears to collapse superpositions discontinuously. Why does this mismatch constitute 'the measurement problem,' and why can't it be resolved by simply treating collapse as an approximation?"
  type: short-answer
  answer: "The measurement problem is that quantum mechanics has two apparently incompatible dynamics: the Schrödinger equation (linear, unitary, continuous, deterministic) and measurement collapse (nonlinear, non-unitary, discontinuous, probabilistic). The Schrödinger equation predicts that when a quantum system interacts with a measuring device, the combined system evolves into a superposition of device-states (pointer pointing left AND pointer pointing right). But we never observe superposed pointers — we observe definite outcomes. Calling collapse an 'approximation' doesn't work because it would require specifying when and why the Schrödinger equation stops applying. Any rule for when collapse happens must break the linearity that is central to quantum mechanics. The problem is not about precision but about fundamental consistency: the theory contains two incompatible dynamical rules and no principled criterion for when each applies."
  explanation: "Different interpretations resolve this differently: Copenhagen says collapse is not a physical process but a transition in our description; Many-Worlds says collapse never happens and all branches are real; spontaneous collapse theories (GRW) modify the Schrödinger equation to include collapse dynamically. All are consistent with known experiments, and none is universally accepted."
```

## Explainer

From your study of state vectors and wavefunctions, you know that a quantum state |ψ⟩ can be expressed as a superposition of basis states. From the quantum postulates, you know that observable quantities correspond to Hermitian operators whose eigenstates form a complete basis. The measurement postulate tells you what happens when you actually observe a system in superposition — and the answer is discontinuous and irreversible in a way that nothing in classical physics prepares you for.

Suppose the state is |ψ⟩ = Σ cₙ |φₙ⟩, where |φₙ⟩ are the eigenstates of some observable Â with eigenvalues λₙ. Before measurement, the system is in a superposition — and a superposition is not mere ignorance about a pre-existing value. When you measure Â, you get exactly one result: some particular λₙ, with probability |cₙ|² = |⟨φₙ|ψ⟩|². This is the **Born rule**, and it is one of the foundational postulates — it cannot be derived from the Schrödinger equation alone. Immediately after the measurement, the state collapses: |ψ⟩ → |φₙ⟩. All other terms in the superposition disappear, and an immediate second measurement of the same observable will yield λₙ with certainty.

Two features make collapse radically different from classical probability. First, the outcome is not just an unknown pre-existing value. A particle approaching a half-silvered mirror is not simply going left or right with 50/50 odds; interference experiments show that both paths contribute to what is observed. (In standard accounts the outcome is genuinely indeterminate; nonlocal hidden-variable theories such as Bohmian mechanics instead give the particle one definite path, guided by a wave that takes both.) Second, **collapse is not Schrödinger evolution**. The Schrödinger equation is linear and unitary — it never collapses a superposition. Measurement introduces a discontinuous jump that sits outside the ordinary dynamics. This mismatch is called the **measurement problem**, and it is the deepest unresolved conceptual issue in quantum foundations.

A useful way to build intuition: think of the inner product ⟨φₙ|ψ⟩ as the "overlap amplitude" between the system state and the eigenstate you're projecting onto. The probability is the square of this amplitude. Orthogonal eigenstates (⟨φₙ|φₘ⟩ = 0 for n ≠ m) mean that if you measure and get λₙ, the probability of immediately getting λₘ in a second measurement is zero. Immediately repeated measurements of the same observable on the same collapsed state always return the same value — because after collapse, the state is already an eigenstate. This repeatability is why measurement collapse is physically essential: it is what makes classical records (pointer positions, detector clicks) possible.
