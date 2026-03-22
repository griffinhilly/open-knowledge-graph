---
id: scalar-and-vector-potentials
title: Scalar and Vector Potentials in Electromagnetism
domain: physics
course: electrodynamics
prerequisites:
- id: electric-potential-and-potential-energy
  type: hard
- id: vector-potential-and-curl
  type: hard
builds-toward:
- gauge-transformations
- retarded-potentials
tags:
- potentials
- field-decomposition
stage: advanced
status: draft
---

# Scalar and Vector Potentials in Electromagnetism

## Core Idea
The scalar potential φ and vector potential A satisfy E = -∇φ - ∂A/∂t and B = ∇ × A. These redundant potentials often simplify calculations by replacing Maxwell's equations with wave equations for φ and A. The freedom in choosing potentials reflects gauge freedom.

## Questions

```yaml
- question: "In a time-varying electromagnetic field, which expression correctly relates the electric field to the scalar potential φ and vector potential A?"
  type: multiple-choice
  options:
    - "E = −∇φ (same as the electrostatic case)"
    - "E = −∇φ − ∂A/∂t"
    - "E = ∇φ + ∂A/∂t"
    - "E = −∂A/∂t only, since the static gradient term vanishes when fields vary"
  answer: 1
  explanation: "The general relation is E = −∇φ − ∂A/∂t, derived from Faraday's law in the time-dependent case. The electrostatic relation E = −∇φ is only valid when ∂A/∂t = 0 (static fields). In the time-varying case, the changing vector potential contributes an additional term to the electric field — this is why the potentials are genuinely more powerful than just a notational convenience."

- question: "You add ∇Λ to the vector potential A. How must the scalar potential φ change simultaneously to leave the physical fields E and B unchanged?"
  type: multiple-choice
  options:
    - "φ is unchanged — only A is modified in this gauge transformation"
    - "φ → φ + ∂Λ/∂t"
    - "φ → φ − ∂Λ/∂t"
    - "φ must be set to zero to compensate for the change in A"
  answer: 2
  explanation: "The paired gauge transformation is A → A + ∇Λ and φ → φ − ∂Λ/∂t. These two changes cancel exactly in B = ∇ × A (the curl of ∇Λ is zero) and in E = −∇φ − ∂A/∂t (the −∂(∇Λ)/∂t from A and the −∇(−∂Λ/∂t) from φ cancel). The two transformations must always be applied together — changing only one would alter the physical fields."

- question: "The scalar potential φ and vector potential A are uniquely determined by the physical situation — there is only one correct (φ, A) pair for any given set of E and B fields."
  type: true-false
  answer: false
  explanation: "Gauge freedom means infinitely many (φ, A) pairs all produce the same physical E and B fields. Any gauge transformation A → A + ∇Λ, φ → φ − ∂Λ/∂t (for any scalar function Λ) generates a different but physically equivalent pair. This is not a weakness of the potential formulation — it is a freedom that physicists exploit by choosing whichever gauge simplifies the problem at hand."

- question: "In the Lorenz gauge, Maxwell's equations for φ and A decouple into two independent wave equations."
  type: true-false
  answer: true
  explanation: "The Lorenz gauge condition ∇·A + (1/c²)∂φ/∂t = 0 eliminates the coupling term between the equations for φ and A, yielding □²φ = −ρ/ε₀ and □²A = −μ₀J separately. This is much cleaner than working with all six components of E and B directly, and is particularly powerful for radiation theory because the d'Alembertian □² is manifestly Lorentz-covariant."

- question: "Why are the potentials φ and A described as 'redundant' descriptions of E and B, and what practical advantage does this redundancy give?"
  type: short-answer
  answer: "The potentials are redundant because gauge freedom allows infinitely many different (φ, A) pairs to produce the same physical E and B fields — the fields underdetermine the potentials. The practical advantage is that you can choose the gauge that makes the mathematics simplest for a given problem: the Lorenz gauge decouples the wave equations and is best for radiation theory; the Coulomb gauge simplifies the equation for φ in quasi-static problems. The freedom to choose the gauge is not a complication — it is a tool."
  explanation: "This redundancy has deep consequences beyond computational convenience. In quantum mechanics, the potentials (not E and B directly) appear in the Schrödinger equation, and gauge invariance there becomes a foundational principle. The Aharonov-Bohm effect demonstrates that potentials have physical significance even where fields are zero, showing that the 'redundancy' at the classical level reveals new physics at the quantum level."
```

## Explainer

You already know the scalar electric potential V (or φ) from electrostatics: it is a scalar field whose negative gradient gives the electric field, E⃗ = −∇φ, and it is defined as the potential energy per unit charge. You also know that ∇ × A⃗ = B⃗ — the **vector potential** A⃗ is a vector field whose curl gives the magnetic field. These two potentials, φ and A⃗, are not new physical objects; they are alternative mathematical descriptions of the same E⃗ and B⃗ fields. But they are often dramatically more convenient to work with.

In electrostatics, E⃗ = −∇φ works because the electric field is curl-free (∇ × E⃗ = 0) in the static case — any curl-free vector field can be written as the gradient of a scalar. The magnetic field satisfies ∇ · B⃗ = 0 always (no magnetic monopoles), and any divergence-free vector field can be written as the curl of another vector field, giving B⃗ = ∇ × A⃗. In the full time-dependent case, Faraday's law says ∇ × E⃗ = −∂B⃗/∂t = −∂(∇ × A⃗)/∂t = −∇ × (∂A⃗/∂t). Rearranging: ∇ × (E⃗ + ∂A⃗/∂t) = 0. Since this is curl-free, it can be written as the gradient of a scalar: E⃗ + ∂A⃗/∂t = −∇φ, giving **E⃗ = −∇φ − ∂A⃗/∂t**. This is the general relationship that reduces to E⃗ = −∇φ only in the static case (∂A⃗/∂t = 0).

The real payoff comes when you substitute these into Maxwell's equations. In free space, the four Maxwell equations for E⃗ and B⃗ become two equations for φ and A⃗ — specifically, wave equations coupled by terms involving ∇ · A⃗ + (1/c²)∂φ/∂t. This coupling can be eliminated by choosing a convenient **gauge**: the **Lorenz gauge** sets ∇ · A⃗ + (1/c²)∂φ/∂t = 0, decoupling the equations into two independent wave equations, □²φ = −ρ/ε₀ and □²A⃗ = −μ₀J⃗, where □² is the d'Alembertian (the relativistic wave operator). This is enormously cleaner than working with the six components of E⃗ and B⃗ directly.

**Gauge freedom** is the key insight connecting to the prerequisite on gauge transformations: the physical fields E⃗ and B⃗ are unchanged if you simultaneously transform φ → φ − ∂Λ/∂t and A⃗ → A⃗ + ∇Λ for any scalar function Λ. This means the potentials are not uniquely determined by the physics — there is an infinite family of equivalent (φ, A⃗) pairs all describing the same observable fields. Different gauge choices suit different problems: the **Coulomb gauge** (∇ · A⃗ = 0) simplifies the equation for φ in radiation problems; the Lorenz gauge is relativistically covariant and best for radiation theory. The existence of gauge freedom is not a bug but a profound feature — in quantum mechanics and quantum field theory, gauge invariance becomes a foundational principle that dictates the form of fundamental interactions.
