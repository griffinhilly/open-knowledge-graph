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
stage: abstract-reasoning
status: draft
---

# Canonical Commutation Relations

## Core Idea
The fundamental canonical commutation relation [x̂, p̂] = iℏ quantifies position-momentum uncertainty and is the cornerstone of quantum mechanics.

## Explainer

From your study of commutation relations, you know that when two operators fail to commute, there is a fundamental measurement trade-off: the more precisely you pin down one observable, the less precisely the other is defined. The canonical commutation relation **[x̂, p̂] = iℏ** is the most important instance of this principle. It says that position and momentum are not simultaneously definable to arbitrary precision — not because of any practical limitation, but because they represent incompatible ways of describing a quantum state. This single equation is in many ways the seed from which all of quantum mechanics grows.

To see where it comes from, work in the position representation. Here x̂ acts as multiplication by x, and p̂ acts as the differential operator −iℏ d/dx. Applying [x̂, p̂] to a test function f(x) gives: x̂(p̂f) − p̂(x̂f) = x(−iℏ f') − (−iℏ)(xf)' = −iℏxf' + iℏ(f + xf') = iℏf. The operators do not commute because differentiating a product xf(x) introduces an extra term — that extra term is exactly iℏ times the identity. The **Robertson uncertainty relation** then follows as a theorem: for any two operators  Â and B̂, σ_A · σ_B ≥ |⟨[Â,B̂]⟩|/2. Applied to x and p, this gives σ_x σ_p ≥ ℏ/2, the Heisenberg uncertainty principle.

The canonical commutation relation is not just a constraint on measurement — it encodes the dynamical structure of quantum theory. In the Heisenberg picture, the equation of motion for any operator O is dO/dt = [O, H]/iℏ. For a free particle, applying this to x̂ and p̂ recovers p = m(dx/dt) and dp/dt = 0, the quantum analogs of Newton's laws. The commutator is the quantum mechanical counterpart of the classical **Poisson bracket** {x, p} = 1. The correspondence {A, B} → [Â, B̂]/iℏ is how classical mechanics is quantized: replace Poisson brackets with commutators scaled by iℏ.

Why does this generalize? The same structure applies to any pair of conjugate observables: energy E and time t, angle φ and angular momentum L_z, and so on. Each conjugate pair satisfies a canonical commutation relation, and each generates an uncertainty principle. You will meet this again immediately in the quantum harmonic oscillator, where the algebraic structure of [x̂, p̂] = iℏ is exploited to define ladder operators â and â†, turning the energy eigenvalue problem into an elegant algebraic one. The canonical commutation relation is not a formula to memorize — it is the bedrock structure from which all of quantum dynamics is derived.


