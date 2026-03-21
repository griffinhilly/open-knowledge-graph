---
id: expectation-values-quantum
title: Expectation Values and Quantum Averages
domain: physics
course: modern-physics
prerequisites:
- id: quantum-superposition-states
  type: hard
- id: quantum-operators-observables
  type: hard
builds-toward:
- canonical-commutation-relations
tags:
- quantum
- observables
- measurement
stage: advanced
status: draft
---

# Expectation Values and Quantum Averages

## Core Idea
The expectation value of an observable is ⟨A⟩ = ∫ψ* Â ψ dx, giving the average result of many measurements on identically prepared systems. For an eigenstate of Â, the expectation value equals the eigenvalue. Expectation values obey classical equations of motion (Ehrenfest theorem), bridging quantum and classical mechanics.

## Questions

```yaml
- question: "A particle is prepared in a superposition of two momentum eigenstates with eigenvalues p₁ and p₂. The expectation value is ⟨p⟩ = |c₁|²p₁ + |c₂|²p₂. Which statement best interprets this?"
  type: multiple-choice
  options:
    - "Every measurement of momentum gives exactly ⟨p⟩, since this is the 'actual' momentum of the particle"
    - "The particle's momentum oscillates between p₁ and p₂ at a frequency related to ⟨p⟩"
    - "⟨p⟩ is the average momentum obtained over many measurements on identically prepared copies of the state"
    - "The particle simultaneously has momenta p₁ and p₂, and ⟨p⟩ is simply their arithmetic mean"
  answer: 2
  explanation: "The expectation value is a statistical prediction about an ensemble, not a property of any single measurement. A single momentum measurement always yields an eigenvalue — either p₁ or p₂, with probabilities |c₁|² and |c₂|² respectively. No measurement ever gives ⟨p⟩ unless ⟨p⟩ happens to equal an eigenvalue. Option A is the most common misconception — treating the expectation value as the 'true' momentum. It is the average, just as the expected value of a die roll is 3.5, which never appears on any face."

- question: "A particle is in an eigenstate of the Hamiltonian with eigenvalue E₀. What does a measurement of energy yield, and what is the expectation value ⟨E⟩?"
  type: multiple-choice
  options:
    - "The measurement yields a random eigenvalue near E₀, and ⟨E⟩ is the average of nearby energy levels"
    - "The measurement yields E₀ with certainty, and ⟨E⟩ = E₀ with zero spread"
    - "The measurement yields zero, since eigenstates are stationary and contain no energy fluctuations"
    - "The expectation value is undefined for eigenstates because the wavefunction doesn't spread over energy values"
  answer: 1
  explanation: "In an eigenstate of Â with eigenvalue a, applying the operator gives Âψ = aψ, so ⟨A⟩ = ∫ψ*(aψ)dx = a∫|ψ|²dx = a. Every measurement yields a with certainty — there is no spread. This is the special case that clarifies the general formula: the expectation value is the average, and for an eigenstate the distribution is a delta function at the eigenvalue. The particle is not 'stationary' in the sense of having zero energy; it has definite energy E₀."

- question: "The expectation value of position ⟨x⟩ gives the most probable location where the particle will be found upon measurement."
  type: true-false
  answer: false
  explanation: "⟨x⟩ is the average position over many measurements — the probability-weighted mean of all possible positions. The most probable position is the peak of |ψ|², the probability density. These can differ significantly: for a symmetric double-well potential, ⟨x⟩ might be at the midpoint (where probability is actually low) while the most probable positions are at the two wells. Confusing average with most-probable is a common error; they coincide only for symmetric, unimodal distributions."

- question: "Ehrenfest's theorem shows that the expectation values of position and momentum obey equations analogous to Newton's second law, explaining why large objects behave classically."
  type: true-false
  answer: true
  explanation: "Ehrenfest's theorem states d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∂V/∂x⟩. These are Newton's equations for averages. For a narrow wave packet (large object), ⟨∂V/∂x⟩ ≈ (∂V/∂x)|_{⟨x⟩}, so the expectation values trace the classical trajectory. Quantum mechanics does not violate Newton's laws for averages; it predicts classical motion as the appropriate limit. This is not a coincidence — it is the mathematical mechanism of the quantum-to-classical correspondence."

- question: "What is the physical meaning of the expectation value in quantum mechanics, and why doesn't a single measurement necessarily yield ⟨A⟩?"
  type: short-answer
  answer: "The expectation value ⟨A⟩ is the average result of measuring observable A across an ensemble of identically prepared quantum systems. It is not a property of any individual particle or measurement. A single measurement always yields an eigenvalue of the operator — one of the sharp values allowed by the spectrum. The expectation value is the probability-weighted average of those eigenvalues. Individual outcomes are inherently probabilistic; only the average over many measurements converges to ⟨A⟩. This reflects quantum mechanics' fundamental probabilism: even perfect knowledge of the state does not determine individual outcomes."
  explanation: "This is the key conceptual break from classical mechanics, where a particle's properties are definite and measurement reveals them. In quantum mechanics, the state is definite but measurement outcomes are probabilistic. The expectation value is the bridge between the quantum description (the state) and what you actually observe statistically (averages over measurements). Ehrenfest's theorem shows these averages obey classical equations, recovering classical mechanics as a limit."
```

## Explainer

In classical mechanics, a particle has a definite position, momentum, and energy at every moment. In quantum mechanics, a particle in a superposition state has no definite value for an observable — until measurement, the system is genuinely in multiple states simultaneously. What you *can* compute is the **expectation value**: the average outcome you would obtain if you prepared many identical copies of the system and measured each one. This is not a statement about uncertainty in preparation — the state is precisely known — it is a statement about the irreducibly probabilistic nature of quantum measurement.

The formula **⟨A⟩ = ∫ψ* Â ψ dx** computes this average using the operator Â corresponding to observable A. The structure ψ* Â ψ is a weighted average: Â ψ applies the operator to the wavefunction, and then ψ* "samples" the result with the probability amplitude at each point. For position, Â = x, and ⟨x⟩ = ∫ψ* x ψ dx = ∫x|ψ|² dx — literally the average of position weighted by the probability density |ψ|². For momentum, Â = −iℏ∂/∂x, and the integral picks up the average momentum encoded in how rapidly the wavefunction oscillates.

A special case clarifies the structure. If ψ is an **eigenstate** of Â with eigenvalue a — meaning Âψ = aψ — then ⟨A⟩ = ∫ψ* (aψ) dx = a ∫|ψ|² dx = a. Every measurement gives exactly a; the expectation value equals the eigenvalue and there is no spread. By contrast, in a superposition ψ = c₁ψ₁ + c₂ψ₂ where Âψ₁ = a₁ψ₁ and Âψ₂ = a₂ψ₂, you get ⟨A⟩ = |c₁|²a₁ + |c₂|²a₂ — a weighted average of eigenvalues, weighted by the squared amplitudes, exactly like a classical probability-weighted average.

The **Ehrenfest theorem** shows that expectation values obey classical equations of motion: d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∂V/∂x⟩. These are Newton's laws for averages. When the quantum state is a narrow wave packet (well-localized in space), ⟨∂V/∂x⟩ ≈ ∂V/∂x evaluated at ⟨x⟩, and the expectation values trace out the classical trajectory. This is why large objects behave classically — their wave packets are so narrow that the expectation values and the eigenvalues are indistinguishable. Ehrenfest's theorem is not a coincidence; it is the mathematical explanation of why quantum mechanics reduces to classical mechanics in the appropriate limit.
