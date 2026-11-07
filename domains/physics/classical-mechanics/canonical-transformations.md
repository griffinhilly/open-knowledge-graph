---
id: canonical-transformations
title: Canonical Transformations and Generating Functions
domain: physics
course: classical-mechanics
prerequisites:
- id: hamiltonian-mechanics-intro
  type: hard
- id: partial-derivatives
  type: hard
- id: legendre-transformations-potentials
  type: soft
- id: phase-space-trajectories
  type: soft
builds-toward:
- hamilton-jacobi-theory
- liouville-theorem-statistical-mechanics
tags:
- hamiltonian
- phase-space
- generating-functions
- poisson-brackets
stage: advanced
status: validated
---

# Canonical Transformations and Generating Functions

## Core Idea
A canonical transformation is a change of phase-space variables (q, p) → (Q, P) that keeps Hamilton's equations in the same form, with some new Hamiltonian K(Q, P, t). Such transformations can be built from a generating function, such as F₂(q, P, t), whose partial derivatives give the old momenta and the new coordinates. A good choice can turn a hard problem into one where the new coordinates are cyclic and the motion is trivial. A one-variable transformation is canonical exactly when the Poisson bracket {Q, P} equals 1.

## How It's Best Learned
Begin with simple examples: the identity, the exchange Q = p, P = −q, and a point transformation of coordinates. Check each with the Poisson bracket test. Then work through the harmonic oscillator transformation that makes the Hamiltonian depend only on P. Emphasize that time evolution itself is a canonical transformation; this is the link to Liouville's theorem.

## Common Misconceptions
- Any invertible change of variables in phase space is canonical. (A canonical transformation must preserve the fundamental Poisson brackets; doubling both q and p gives {Q, P} = 4, so it is not canonical. Hamilton's equations survive it only if the Hamiltonian is also rescaled to 4H, which texts call a scale transformation.)
- The new Q must still be a position and P a momentum. (The exchange Q = p, P = −q is canonical; the labels "coordinate" and "momentum" lose their everyday meaning.)
- The new Hamiltonian is always the old one written in new variables. (K = H + ∂F/∂t, so an explicitly time-dependent generating function changes the Hamiltonian.)

## Questions

```yaml
- question: "For one degree of freedom, which transformation is canonical?"
  type: multiple-choice
  options: ["Q = p, P = q", "Q = p, P = −q", "Q = 2q, P = 2p", "Q = q², P = p"]
  answer: 1
  explanation: "Test {Q, P} = ∂Q/∂q ∂P/∂p − ∂Q/∂p ∂P/∂q. For Q = p, P = −q this is 0·0 − (1)(−1) = 1. The others give −1, 4, and 2q."
- question: "The evolution of a Hamiltonian system from time t to time t + Δt is itself a canonical transformation of phase space."
  type: true-false
  answer: true
  explanation: "Hamilton's equations generate a flow that preserves Poisson brackets. The Hamiltonian acts as the generator of this transformation, which is why phase-space volume is conserved (Liouville's theorem)."
- question: "Use the type-2 generating function F₂(q, P) = qP, with p = ∂F₂/∂q and Q = ∂F₂/∂P. What transformation results?"
  type: short-answer
  answer: "The identity: Q = q and P = p."
  explanation: "∂F₂/∂q = P, so p = P. ∂F₂/∂P = q, so Q = q. This is why qP is the starting point for building transformations close to the identity."
- question: "For the oscillator H = p²/2m + mω²q²/2, the transformation q = √(2P/mω) sin Q, p = √(2mωP) cos Q gives K = ωP. Why does this make the problem easy?"
  type: multiple-choice
  options: ["K no longer depends on Q, so P is constant and Q grows linearly in time", "K no longer depends on P, so Q is constant", "K is zero, so nothing moves", "The transformation removes the mass from the problem"]
  answer: 0
  explanation: "Q is cyclic, so dP/dt = −∂K/∂Q = 0 and P = E/ω is constant. Then dQ/dt = ∂K/∂P = ω, so Q = ωt + φ. Substituting back gives the familiar sinusoidal motion."
```

## Explainer
In Lagrangian mechanics you may choose any generalized coordinates you like. Hamiltonian mechanics allows a wider freedom: you may mix coordinates and momenta, provided the new variables still obey Hamilton's equations. Such a change (q, p) → (Q, P) is called canonical. The new Hamiltonian K(Q, P, t) then satisfies dQ/dt = ∂K/∂P and dP/dt = −∂K/∂Q.

A quick test uses Poisson brackets. For one degree of freedom the transformation is canonical when {Q, P} = 1, computed with respect to q and p. More generally, all the fundamental brackets {Qᵢ, Pⱼ} = δᵢⱼ and {Qᵢ, Qⱼ} = {Pᵢ, Pⱼ} = 0 must hold. The exchange Q = p, P = −q passes this test. Doubling both q and p fails it, because {2q, 2p} = 4.

Generating functions give a way to build canonical transformations. One common type is F₂(q, P, t). It defines the transformation through

p = ∂F₂/∂q,  Q = ∂F₂/∂P,  K = H + ∂F₂/∂t.

The choice F₂ = qP gives the identity. Other types, such as F₁(q, Q, t) with p = ∂F₁/∂q and P = −∂F₁/∂Q, are related to F₂ by Legendre transforms.

The payoff is that a clever transformation can make every new coordinate cyclic. The harmonic oscillator shows this. With q = √(2P/mω) sin Q and p = √(2mωP) cos Q, the Hamiltonian H = p²/2m + mω²q²/2 becomes K = ωP. Since K does not contain Q, P is constant and equals E/ω. Since ∂K/∂P = ω, the new coordinate grows steadily, Q = ωt + φ. Substituting back gives q(t) = √(2E/mω²) sin(ωt + φ). The new variables P and Q are, up to a factor, the action and angle variables of Hamilton-Jacobi theory.

Canonical transformations also clarify the structure of mechanics. An infinitesimal transformation generated by a function G shifts q by ε ∂G/∂p and p by −ε ∂G/∂q. Momentum generates translations, angular momentum generates rotations, and the Hamiltonian generates time evolution. Because time evolution is canonical, it preserves phase-space volume, which is Liouville's theorem. The same pattern carries into quantum mechanics, where unitary operators replace canonical transformations and commutators replace Poisson brackets.
