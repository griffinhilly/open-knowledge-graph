---
id: canonical-commutation-relations-quantum-mechanics
title: Canonical Commutation Relations
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
builds-toward:
- quantum-harmonic-oscillator
tags:
- commutation-relations
- position-momentum
- foundations
stage: formal-systems
status: validated
---

# Canonical Commutation Relations

## Core Idea
The fundamental canonical commutation relation [x̂, p̂] = iℏ quantifies position-momentum uncertainty and is the cornerstone of quantum mechanics.

## Questions

```yaml
- question: "In the position representation, p̂ = −iℏ d/dx. When computing [x̂, p̂]f(x) for a test function f(x), what produces the nonzero result iℏf(x)?"
  type: multiple-choice
  options:
    - "The product rule of differentiation: d(xf)/dx = f + xf', so the extra f term does not cancel between the two parts of the commutator"
    - "A relativistic correction that becomes significant at quantum scales"
    - "A normalization convention added to ensure dimensional consistency"
    - "The imaginary unit i, which appears because quantum operators must be Hermitian"
  answer: 0
  explanation: "The commutator [x̂, p̂]f = x(−iℏf') − (−iℏ)(xf)' = −iℏxf' + iℏ(f + xf') = iℏf. The product rule applied to d(xf)/dx gives f + xf'. The xf' terms cancel, leaving iℏ × f — the identity operator scaled by iℏ. This is a purely mathematical consequence of differentiation, not a physical assumption."

- question: "A physicist applies the Heisenberg equation of motion dÔ/dt = [Ô, H]/iℏ to position x̂ for a free particle and recovers p̂ = m(dx̂/dt). What does this demonstrate about [x̂, p̂] = iℏ?"
  type: multiple-choice
  options:
    - "The relation encodes the full dynamical structure of quantum mechanics — not just measurement limits, but equations of motion that reproduce classical mechanics in the appropriate limit"
    - "The commutation relation is valid only for free particles without external potentials"
    - "Quantum mechanics and classical mechanics are equivalent for all practical purposes"
    - "The commutation relation is derived from Newton's second law rather than being a foundational statement"
  answer: 0
  explanation: "Applying [x̂, H]/iℏ with H = p̂²/2m recovers dx̂/dt = p̂/m — the quantum analog of classical momentum. This shows [x̂, p̂] = iℏ governs dynamical time evolution, not just measurement uncertainty. The commutation relation is connected to classical mechanics through the Poisson bracket correspondence {x, p} = 1 → [x̂, p̂]/iℏ = 1, making it the bedrock from which quantum dynamics is derived."

- question: "The Heisenberg uncertainty principle (σ_x σ_p ≥ ℏ/2) is a postulate of quantum mechanics — a foundational axiom that must be assumed independently."
  type: true-false
  answer: false
  explanation: "The uncertainty principle is not a postulate — it is a theorem derived from the canonical commutation relation [x̂, p̂] = iℏ via the Robertson relation: for any operators Â and B̂, σ_A σ_B ≥ |⟨[Â,B̂]⟩|/2. Applied to x and p, this yields σ_x σ_p ≥ ℏ/2. The commutation relation is the fundamental input; the uncertainty principle is a consequence. This also means it is not about measurement disturbance — it is a structural property of the mathematical framework."

- question: "The classical Poisson bracket {x, p} = 1 and the quantum commutator [x̂, p̂] = iℏ are structurally analogous, related by {A, B} → [Â, B̂]/iℏ."
  type: true-false
  answer: true
  explanation: "This correspondence is the quantization rule connecting classical and quantum mechanics. Replacing classical Poisson brackets with commutators scaled by iℏ is how any classical system with conjugate variables is quantized. The structural analogy explains why conjugate pairs (energy-time, angle-angular momentum, etc.) each satisfy their own canonical commutation relation, and why the commutation relation encodes the same dynamical content as classical conjugacy."

- question: "Why does [x̂, p̂] = iℏ imply that no quantum state can simultaneously have a perfectly definite position and a perfectly definite momentum, even in principle?"
  type: short-answer
  answer: "If a state had definite position (σ_x = 0) and definite momentum (σ_p = 0), their product would be zero, violating σ_x σ_p ≥ ℏ/2. More fundamentally, [x̂, p̂] ≠ 0 means x̂ and p̂ share no common eigenstates: a position eigenstate (delta function in position space) is a uniform superposition of all momentum eigenstates, giving completely undefined momentum — and vice versa. This is not a limitation of measurement apparatus but a structural feature of how quantum states are defined."
  explanation: "The non-commutativity of x̂ and p̂ is mathematically equivalent to the absence of simultaneous eigenstates. In the Fourier relationship between position and momentum representations, a sharply localized position state (narrow wavepacket) has a broad momentum distribution, and a definite momentum state (plane wave) is completely delocalized in position. This trade-off is built into the mathematics of conjugate variables, independent of any measurement process."
```

## Explainer

From your study of commutation relations, you know that when two operators fail to commute, there is a fundamental measurement trade-off: the more precisely you pin down one observable, the less precisely the other is defined. The canonical commutation relation **[x̂, p̂] = iℏ** is the most important instance of this principle. It says that position and momentum are not simultaneously definable to arbitrary precision — not because of any practical limitation, but because they represent incompatible ways of describing a quantum state. This single equation is in many ways the seed from which all of quantum mechanics grows.

To see where it comes from, work in the position representation. Here x̂ acts as multiplication by x, and p̂ acts as the differential operator −iℏ d/dx. Applying [x̂, p̂] to a test function f(x) gives: x̂(p̂f) − p̂(x̂f) = x(−iℏ f') − (−iℏ)(xf)' = −iℏxf' + iℏ(f + xf') = iℏf. The operators do not commute because differentiating a product xf(x) introduces an extra term — that extra term is exactly iℏ times the identity. The **Robertson uncertainty relation** then follows as a theorem: for any two operators  Â and B̂, σ_A · σ_B ≥ |⟨[Â,B̂]⟩|/2. Applied to x and p, this gives σ_x σ_p ≥ ℏ/2, the Heisenberg uncertainty principle.

The canonical commutation relation is not just a constraint on measurement — it encodes the dynamical structure of quantum theory. In the Heisenberg picture, the equation of motion for any operator O is dO/dt = [O, H]/iℏ. For a free particle, applying this to x̂ and p̂ recovers p = m(dx/dt) and dp/dt = 0, the quantum analogs of Newton's laws. The commutator is the quantum mechanical counterpart of the classical **Poisson bracket** {x, p} = 1. The correspondence {A, B} → [Â, B̂]/iℏ is how classical mechanics is quantized: replace Poisson brackets with commutators scaled by iℏ.

Why does this generalize? The same structure applies to any pair of conjugate observables: energy E and time t, angle φ and angular momentum L_z, and so on. Each conjugate pair satisfies a canonical commutation relation, and each generates an uncertainty principle. You will meet this again immediately in the quantum harmonic oscillator, where the algebraic structure of [x̂, p̂] = iℏ is exploited to define ladder operators â and â†, turning the energy eigenvalue problem into an elegant algebraic one. The canonical commutation relation is not a formula to memorize — it is the bedrock structure from which all of quantum dynamics is derived.


