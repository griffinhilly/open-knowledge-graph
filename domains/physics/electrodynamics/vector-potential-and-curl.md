---
id: vector-potential-and-curl
title: Vector Potential and Curl Relationships
domain: physics
course: electrodynamics
prerequisites:
- id: magnetic-field-and-lorentz-force
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- scalar-and-vector-potentials
- gauge-transformations
tags:
- vector-calculus
- magnetostatics
- potentials
stage: abstract-reasoning
status: draft
---

# Vector Potential and Curl Relationships

## Core Idea
The vector potential A is defined by B = ∇ × A, automatically satisfying ∇ · B = 0. This reformulation replaces the magnetic constraint with a vector equation, often simplifying calculations. Like scalar potential, A is non-unique under gauge transformations.

## Explainer

In electrostatics you learned that because ∇ × E⃗ = 0 (the curl of the electric field is zero in statics), you can write E⃗ = −∇φ for some scalar potential φ. The potential encodes the field in a simpler object — a single function φ rather than three component functions — and energy bookkeeping becomes clean. Magnetostatics gives you an analogous opportunity, but the relevant constraint is different: ∇ · B⃗ = 0 (no magnetic monopoles). This means B⃗ is **divergence-free**, not curl-free. A different identity from vector calculus saves you: the divergence of any curl is identically zero — ∇ · (∇ × A⃗) = 0 for any vector field A⃗. So if you define B⃗ = ∇ × A⃗, the constraint ∇ · B⃗ = 0 is automatically satisfied, no matter what A⃗ is.

The **vector potential** A⃗ is this auxiliary field. It is not directly measurable in classical physics — B⃗ is the physical quantity, and A⃗ is a computational tool. Its curl is B⃗; its divergence is not yet determined. That freedom to choose ∇ · A⃗ is called **gauge freedom**, and a specific choice (like the Coulomb gauge ∇ · A⃗ = 0 or the Lorenz gauge) is called a gauge condition. Different gauges leave B⃗ unchanged because adding any gradient ∇χ to A⃗ shifts the curl by ∇ × (∇χ) = 0, which is the zero vector. Concretely, A⃗ → A⃗ + ∇χ leaves B⃗ = ∇ × A⃗ untouched. The scalar potential φ you know from electrostatics has the same property: adding a constant to φ leaves E⃗ = −∇φ unchanged. Gauge freedom is the same non-uniqueness, promoted to a vector setting.

Why bother with A⃗ at all? There are several reasons. First, the Biot-Savart law for B⃗ due to a current distribution is a complicated cross-product integral; computing A⃗ first requires only a simpler (non-cross-product) volume integral over current density, and then one curl differentiates it to give B⃗. Second, when you move from magnetostatics to electrodynamics, Faraday's law couples the changing B⃗ to E⃗, and the most natural way to write all four Maxwell equations symmetrically is through the potentials (φ, A⃗). Third — and this becomes central in quantum mechanics — the Schrödinger equation for a charged particle couples to A⃗ directly, not only through B⃗. The **Aharonov-Bohm effect** demonstrates that a quantum particle can be affected by A⃗ in a region where B⃗ = 0, showing that the potential has independent physical significance beyond just being a calculation shortcut.
