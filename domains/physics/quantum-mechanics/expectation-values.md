---
id: expectation-values
title: Expectation Values and Averages
domain: physics
course: quantum-mechanics
prerequisites:
- id: observables-and-operators
  type: hard
- id: born-rule-and-measurement
  type: hard
builds-toward:
- variational-method
- time-independent-perturbation-theory
tags:
- observables
- averages
stage: advanced
status: validated
---

# Expectation Values and Averages

## Core Idea
The expectation value ⟨A⟩ = ⟨ψ|A|ψ⟩ gives the average result of measuring observable A. Higher moments characterize the full probability distribution. Expectation values connect quantum mechanics to classical observables.

## Questions

```yaml
- question: "A particle is prepared in an equal superposition of two energy eigenstates |E₁⟩ and |E₂⟩ with E₁ = 1 eV and E₂ = 3 eV. The expectation value ⟨H⟩ = 2 eV. What does this tell you about the result of a single energy measurement?"
  type: multiple-choice
  options:
    - "The measurement will return exactly 2 eV, since that is the expectation value"
    - "The measurement will return either 1 eV or 3 eV with equal probability, averaging to 2 eV over many measurements"
    - "The measurement is indeterminate and could return any value between 1 eV and 3 eV"
    - "The expectation value is only meaningful for eigenstates, so ⟨H⟩ = 2 eV is not physically interpretable here"
  answer: 1
  explanation: "The expectation value is a long-run average, not a prediction for a single measurement. A single energy measurement can only return an eigenvalue of H — here, either 1 eV or 3 eV. Since the superposition is equal-weight, each occurs with probability 1/2, and the average over many measurements is (1 + 3)/2 = 2 eV. The expectation value 2 eV is never actually observed in a single measurement; it is a statistical property of the state."

- question: "For an eigenstate |φₙ⟩ of observable A with eigenvalue aₙ, what is the variance ⟨(ΔA)²⟩ = ⟨A²⟩ − ⟨A⟩²?"
  type: multiple-choice
  options:
    - "aₙ², since squaring the eigenvalue gives the mean-square"
    - "aₙ, since the expectation value equals the eigenvalue"
    - "Zero, because every measurement of A returns aₙ with certainty"
    - "It depends on the specific observable and cannot be determined without knowing the full spectrum"
  answer: 2
  explanation: "For an eigenstate, every measurement returns exactly aₙ — there is no spread. ⟨A⟩ = aₙ and ⟨A²⟩ = aₙ², so the variance is aₙ² − aₙ² = 0. Zero variance means zero uncertainty: ΔA = 0. This is the quantitative expression of the fact that eigenstates are states of definite value for their observable. It also connects to the Heisenberg uncertainty principle: an eigenstate of position would have zero position uncertainty but maximal momentum uncertainty."

- question: "The uncertainty ΔA in observable A reflects the imprecision of the measuring apparatus — a better instrument would reduce ΔA toward zero."
  type: true-false
  answer: false
  explanation: "Quantum mechanical uncertainty is a property of the *state*, not of the measuring apparatus. ΔA = √(⟨A²⟩ − ⟨A⟩²) is computed from the wavefunction and tells you the intrinsic spread in outcomes for that state, even with a perfect measurement device. An eigenstate has ΔA = 0 regardless of the apparatus; a superposition has ΔA > 0 regardless of how good the instrument is. The Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2 is a statement about states, not about experimental limitations."

- question: "Ehrenfest's theorem shows that the expectation values of position and momentum obey Newton's second law, which is why macroscopic objects follow classical trajectories even though they obey quantum mechanics."
  type: true-false
  answer: true
  explanation: "Ehrenfest's theorem states d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∂V/∂x⟩. When a wavepacket is narrow enough that the potential varies slowly across it, ⟨∂V/∂x⟩ ≈ (∂V/∂x)|_{⟨x⟩}, and the quantum equations reduce to the classical F = ma. Macroscopic objects have extremely narrow wavefunctions relative to the scales over which forces vary, so their expectation values track the classical trajectory with negligible spread. This is the quantum-classical correspondence: quantum mechanics reduces to classical mechanics in the appropriate limit."

- question: "What is the physical meaning of the expectation value ⟨A⟩, and why does it not tell you what result any single measurement will return?"
  type: short-answer
  answer: "⟨A⟩ is the long-run average of measurement outcomes: if you prepare many identical copies of the state |ψ⟩ and measure observable A on each, ⟨A⟩ is the mean of the results. It does not predict a single outcome because quantum measurement is inherently probabilistic — each measurement yields one of A's eigenvalues, with probabilities given by the Born rule. Unless |ψ⟩ is already an eigenstate of A, different measurements of the same state return different eigenvalues. The expectation value summarizes the distribution of those outcomes, just as a probability distribution's mean doesn't tell you the result of a single draw."
  explanation: "This distinction — statistical average versus single-event prediction — is fundamental to understanding quantum mechanics. The expectation value connects the quantum formalism to experimental practice: it's what an experimentalist measures when they repeat the same preparation and average many results."
```

## Explainer

You already know from the Born rule that measuring observable A on state |ψ⟩ yields eigenvalue aₙ with probability |⟨φₙ|ψ⟩|², where {|φₙ⟩} are the eigenstates of the operator Â. The **expectation value** ⟨A⟩ is simply the statistical average over all possible measurement outcomes: ⟨A⟩ = Σ aₙ |⟨φₙ|ψ⟩|². It answers the question: if you prepare many identical copies of |ψ⟩ and measure A on each one, what is the mean of your results? It does not tell you what any single measurement will give — only the long-run average.

The compact formula ⟨A⟩ = ⟨ψ|Â|ψ⟩ packages this average elegantly. For position, it becomes ⟨x⟩ = ∫ ψ*(x) · x · ψ(x) dx, which is just the probability-density-weighted average of position — a continuous version of E[X] from probability theory. For momentum, the operator is Âₚ = −iℏ ∂/∂x, so ⟨p⟩ = ∫ ψ*(x) (−iℏ ∂ψ/∂x) dx. The operator acts on the ket before the inner product is evaluated; the order matters whenever the operator involves derivatives. For an eigenstate |φₙ⟩ with eigenvalue aₙ, the expectation value is simply aₙ — no surprise, since every measurement returns the same value.

**Higher moments** extend this: ⟨A²⟩ = ⟨ψ|Â²|ψ⟩ gives the mean-square value, and the **variance** is ⟨(ΔA)²⟩ = ⟨A²⟩ − ⟨A⟩². The standard deviation ΔA = √⟨(ΔA)²⟩ is the **uncertainty** in observable A, the quantity that appears in the Heisenberg uncertainty principle: ΔxΔp ≥ ℏ/2. An eigenstate of A has zero variance in A (ΔA = 0), while a superposition of different eigenstates has nonzero uncertainty. The uncertainty is not a measurement imprecision — it is a property of the state itself.

The deepest connection is to classical mechanics via **Ehrenfest's theorem**: d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∂V/∂x⟩. The expectation values of position and momentum obey Newton's second law, but with the force evaluated as an expectation value of the gradient of the potential. When the wavepacket is narrow enough that ∂V/∂x is approximately constant across it, the quantum equations reduce to the classical equations of motion. This is why macroscopic objects follow classical trajectories even though they are quantum mechanically: their wavefunctions are so sharply peaked that expectation values track the classical path precisely.
