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
stage: abstract-reasoning
status: draft
---

# Scalar and Vector Potentials in Electromagnetism

## Core Idea
The scalar potential φ and vector potential A satisfy E = -∇φ - ∂A/∂t and B = ∇ × A. These redundant potentials often simplify calculations by replacing Maxwell's equations with wave equations for φ and A. The freedom in choosing potentials reflects gauge freedom.

## Explainer

You already know the scalar electric potential V (or φ) from electrostatics: it is a scalar field whose negative gradient gives the electric field, E⃗ = −∇φ, and it is defined as the potential energy per unit charge. You also know that ∇ × A⃗ = B⃗ — the **vector potential** A⃗ is a vector field whose curl gives the magnetic field. These two potentials, φ and A⃗, are not new physical objects; they are alternative mathematical descriptions of the same E⃗ and B⃗ fields. But they are often dramatically more convenient to work with.

In electrostatics, E⃗ = −∇φ works because the electric field is curl-free (∇ × E⃗ = 0) in the static case — any curl-free vector field can be written as the gradient of a scalar. The magnetic field satisfies ∇ · B⃗ = 0 always (no magnetic monopoles), and any divergence-free vector field can be written as the curl of another vector field, giving B⃗ = ∇ × A⃗. In the full time-dependent case, Faraday's law says ∇ × E⃗ = −∂B⃗/∂t = −∂(∇ × A⃗)/∂t = −∇ × (∂A⃗/∂t). Rearranging: ∇ × (E⃗ + ∂A⃗/∂t) = 0. Since this is curl-free, it can be written as the gradient of a scalar: E⃗ + ∂A⃗/∂t = −∇φ, giving **E⃗ = −∇φ − ∂A⃗/∂t**. This is the general relationship that reduces to E⃗ = −∇φ only in the static case (∂A⃗/∂t = 0).

The real payoff comes when you substitute these into Maxwell's equations. In free space, the four Maxwell equations for E⃗ and B⃗ become two equations for φ and A⃗ — specifically, wave equations coupled by terms involving ∇ · A⃗ + (1/c²)∂φ/∂t. This coupling can be eliminated by choosing a convenient **gauge**: the **Lorenz gauge** sets ∇ · A⃗ + (1/c²)∂φ/∂t = 0, decoupling the equations into two independent wave equations, □²φ = −ρ/ε₀ and □²A⃗ = −μ₀J⃗, where □² is the d'Alembertian (the relativistic wave operator). This is enormously cleaner than working with the six components of E⃗ and B⃗ directly.

**Gauge freedom** is the key insight connecting to the prerequisite on gauge transformations: the physical fields E⃗ and B⃗ are unchanged if you simultaneously transform φ → φ − ∂Λ/∂t and A⃗ → A⃗ + ∇Λ for any scalar function Λ. This means the potentials are not uniquely determined by the physics — there is an infinite family of equivalent (φ, A⃗) pairs all describing the same observable fields. Different gauge choices suit different problems: the **Coulomb gauge** (∇ · A⃗ = 0) simplifies the equation for φ in radiation problems; the Lorenz gauge is relativistically covariant and best for radiation theory. The existence of gauge freedom is not a bug but a profound feature — in quantum mechanics and quantum field theory, gauge invariance becomes a foundational principle that dictates the form of fundamental interactions.
