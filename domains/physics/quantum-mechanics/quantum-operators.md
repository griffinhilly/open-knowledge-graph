---
id: quantum-operators
title: Quantum Operators
domain: physics
course: quantum-mechanics
prerequisites:
- id: hilbert-spaces-and-dirac-notation
  type: hard
- id: linear-transformation-definition
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: linear-transformations
  type: hard
builds-toward:
- quantum-observables
- eigenvalues-eigenstates-quantum
- commutation-relations
tags:
- operators
- observables
- linear-algebra
stage: advanced
status: validated
---

# Quantum Operators

## Core Idea
Quantum operators are linear transformations acting on state vectors in Hilbert space. Common operators include position x̂, momentum p̂ = -iℏ(d/dx), and angular momentum L̂. Operators encode dynamical information: applying an operator to a state yields another state, or an eigenstate yields the eigenvalue representing an observable quantity.

## Questions

```yaml
- question: "A quantum state is prepared as |ψ⟩ = (1/√2)|a₁⟩ + (1/√2)|a₂⟩, a superposition of two eigenstates of observable Â with eigenvalues a₁ and a₂. What does a single measurement of Â yield?"
  type: multiple-choice
  options:
    - "The average value (a₁ + a₂)/2, since the state is an equal superposition"
    - "Either a₁ or a₂, each with probability 1/2"
    - "An undefined result, because the state is not an eigenstate of Â"
    - "Both a₁ and a₂ simultaneously, since both components are present"
  answer: 1
  explanation: "A measurement of an observable always yields one of the operator's eigenvalues — never an intermediate average. The probabilities are |c₁|² and |c₂|², which here are both 1/2. Option A is the most common misconception: the expectation value (a₁ + a₂)/2 is the *average over many measurements*, not any single outcome. The operator defines possible outcomes and probabilities; it does not determine which eigenvalue is realized on a given measurement."

- question: "Why must physical observables in quantum mechanics correspond to Hermitian operators rather than arbitrary linear operators?"
  type: multiple-choice
  options:
    - "Hermitian operators are computationally simpler to apply to state vectors"
    - "Hermitian operators guarantee that all eigenvalues are real numbers, and measurement outcomes must be real"
    - "Non-Hermitian operators cannot be expressed in Dirac notation"
    - "Hermitian operators always commute with each other, ensuring consistent measurements"
  answer: 1
  explanation: "Physical measurement outcomes must be real numbers — you cannot measure an imaginary position or momentum. Hermitian operators (Â† = Â) are guaranteed to have real eigenvalues, making them the only valid candidates for physical observables. Option D is false: Hermitian operators generally do *not* commute (in fact, non-commutativity encodes the uncertainty principle). The Hermiticity requirement follows directly from demanding real measurement outcomes, not computational convenience."

- question: "Applying the momentum operator p̂ to any wavefunction returns a real number representing the particle's momentum."
  type: true-false
  answer: false
  explanation: "Applying p̂ = −iℏ(d/dx) to an arbitrary wavefunction returns *another wavefunction*, not a number. Only when the wavefunction is an eigenstate of p̂ — specifically, a plane wave e^(ikx) — does the result equal a number (the eigenvalue ℏk) times the original state. For a general superposition, the operator maps one state vector to another, encoding the probability distribution over momentum outcomes rather than a single definite value."

- question: "A particle in an eigenstate of the position operator x̂ with eigenvalue x₀ will yield x₀ with certainty upon position measurement."
  type: true-false
  answer: true
  explanation: "This is the defining property of eigenstates: Â|ψ⟩ = a|ψ⟩ means measuring observable Â on state |ψ⟩ yields eigenvalue a with probability 1. A position eigenstate (a Dirac delta function in position space) is maximally localized — measuring position returns x₀ every time. The trade-off, embodied in the uncertainty principle, is that such a state is completely delocalized in momentum space."

- question: "Explain why the momentum operator takes the form p̂ = −iℏ(d/dx) rather than simply being multiplication by a position-like variable. What physical reasoning connects differentiation to momentum?"
  type: short-answer
  answer: "The form follows from the de Broglie relation p = ℏk and the structure of plane waves. A state of definite momentum p is a plane wave e^(ikx) with k = p/ℏ. Differentiating: d/dx e^(ikx) = ik · e^(ikx), so −iℏ(d/dx) e^(ikx) = ℏk · e^(ikx) = p · e^(ikx). The plane wave is an eigenstate of −iℏ(d/dx) with eigenvalue p. The differential operator is necessary because momentum in quantum mechanics is linked to spatial frequency (the rate of phase oscillation), not position. Multiplication by x encodes position information; differentiation with respect to x encodes how rapidly the wavefunction oscillates, which encodes momentum."
  explanation: "The momentum operator being differential is not an arbitrary convention — it is forced by the requirement that plane waves (states of definite momentum) be eigenstates of the momentum operator, which follows from de Broglie. This reflects the deep connection between momentum and spatial translation symmetry: in quantum mechanics, the momentum operator is the generator of spatial translations, and generators of continuous symmetries always appear as differential operators."
```

## Explainer

From your linear algebra prerequisites, you know that a linear transformation takes vectors to vectors and satisfies T(αv + βw) = αT(v) + βT(w). In quantum mechanics, the vectors live in Hilbert space — they are quantum states — and the "transformations" are operators representing physical observables. Every measurable quantity (position, momentum, energy, spin) corresponds to a specific **Hermitian operator**, and the possible measurement outcomes are exactly the operator's eigenvalues.

The **position operator** x̂ acts on a wavefunction ψ(x) by multiplication: x̂ψ(x) = xψ(x). This makes sense — the operator "asks" where the particle is by multiplying by the position coordinate. The **momentum operator** p̂ = −iℏ(d/dx) is more surprising: it is a differential operator. This is not arbitrary. From the de Broglie relation p = ℏk and the fact that plane waves e^(ikx) are states of definite momentum, differentiating e^(ikx) brings down ik — so −iℏ(d/dx) applied to e^(ikx) gives ℏk · e^(ikx) = p · e^(ikx). Plane waves are eigenstates of p̂ with eigenvalue p.

The eigenvalue equation Â|ψ⟩ = a|ψ⟩ is the central formula. When a state |ψ⟩ is an eigenstate of operator Â with eigenvalue a, measuring the corresponding observable always yields the value a with certainty. When the state is a superposition of eigenstates — say |ψ⟩ = c₁|a₁⟩ + c₂|a₂⟩ — the measurement yields a₁ with probability |c₁|² or a₂ with probability |c₂|². The operator doesn't tell you which outcome will happen; it tells you what outcomes are possible and (via the state decomposition) with what probabilities. This is the precise sense in which operators "encode observable information."

**Hermitian operators** are the special class required for physical observables because their eigenvalues are always real — measurement outcomes must be real numbers. From Dirac notation you know that the adjoint of an operator is defined by ⟨φ|Â†|ψ⟩ = ⟨ψ|Â|φ⟩*; for Hermitian operators, Â† = Â. You can verify p̂ is Hermitian by integration by parts. The requirement of Hermiticity, combined with the eigenvector structure of linear algebra you already know, determines which mathematical objects can serve as quantum observables — not every linear operator qualifies, only the Hermitian ones.
