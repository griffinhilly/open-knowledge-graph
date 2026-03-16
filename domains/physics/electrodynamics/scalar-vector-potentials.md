---
id: scalar-vector-potentials
title: Scalar and Vector Potentials
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: curl-and-divergence
  type: hard
builds-toward:
- retarded-potentials
- gauge-transformations
tags:
- potentials
- alternative-formulation
stage: advanced
status: draft
---

# Scalar and Vector Potentials

## Core Idea
Instead of working directly with E and B fields, one can use the scalar potential φ and vector potential A such that E = -∇φ - ∂A/∂t and B = ∇ × A. These potentials automatically satisfy the two Maxwell equations with no sources (∇·B = 0 and ∇ × E = -∂B/∂t). Potentials are mathematically more convenient and form the foundation for quantum mechanics and quantum field theory.

## Explainer

In electrostatics, you already use the scalar potential φ: the electric field is E = -∇φ, and φ is much easier to work with than E directly because it is a scalar. But in electrodynamics, with time-varying fields, E = -∇φ is no longer valid — Faraday's law says ∇ × E = -∂B/∂t ≠ 0, and a gradient always has zero curl, so a pure scalar potential cannot represent a general electric field. The scalar and vector potentials together resolve this problem by representing all four of Maxwell's equations in a more compact and mathematically tractable way.

The starting point is the two source-free Maxwell equations. Since ∇·B = 0 everywhere and always, B must be the curl of something — a theorem from vector calculus says that any divergence-free field can be written as the curl of another field. So define the **vector potential** A⃗ such that B = ∇ × A⃗. Now substitute into Faraday's law: ∇ × E = -∂(∇ × A⃗)/∂t = -∇ × (∂A⃗/∂t), which means ∇ × (E + ∂A⃗/∂t) = 0. A field with zero curl can be written as a gradient, so E + ∂A⃗/∂t = -∇φ, giving E = -∇φ - ∂A⃗/∂t. These two equations for B and E in terms of φ and A⃗ automatically satisfy both source-free Maxwell equations, reducing the problem from four equations to two (the ones involving sources: ∇·E = ρ/ε₀ and ∇ × B = μ₀J + μ₀ε₀∂E/∂t).

A crucial and initially disorienting feature is **gauge freedom**: φ and A⃗ are not uniquely determined by E and B. You can transform φ → φ - ∂Λ/∂t and A⃗ → A⃗ + ∇Λ for any scalar function Λ(r,t), and the resulting E and B fields are identical to before. This means infinitely many different potential pairs describe the same physics. This freedom can be exploited to simplify the equations: the **Lorenz gauge** (∇·A⃗ + μ₀ε₀∂φ/∂t = 0) makes the wave equations for φ and A⃗ symmetric and elegant; the **Coulomb gauge** (∇·A⃗ = 0) simplifies static problems and is preferred in quantum mechanics. The choice of gauge is a computational strategy, not a physical decision.

The potentials are not merely a mathematical convenience — they are physically fundamental in quantum mechanics. The **Aharonov-Bohm effect** demonstrates that a charged particle acquires a measurable phase shift when traveling around a region of nonzero A⃗, even if B = 0 throughout the particle's path. The particle never experiences a magnetic force, yet its quantum state is affected by A⃗. This effect — experimentally confirmed — shows that the vector potential is not just a bookkeeping device; it is the object that directly couples to quantum matter. In quantum field theory, the vector potential becomes the photon field, and gauge invariance becomes the principle that dictates the form of all electromagnetic interactions.
