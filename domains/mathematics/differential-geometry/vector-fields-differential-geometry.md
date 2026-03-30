---
id: vector-fields-differential-geometry
title: Vector Fields
domain: mathematics
course: differential-geometry
prerequisites:
  - id: tangent-vectors-and-tangent-spaces
    type: hard
  - id: smooth-manifolds
    type: hard
tags:
  - vector-fields-differential-geometry
  - sections
  - flows
  - tangent-bundle
stage: advanced
status: validated
---

# Vector Fields

## Core Idea
A vector field on a smooth manifold M is a smooth assignment of a tangent vector to each point — formally, a smooth section of the tangent bundle. In local coordinates, a vector field looks like X = Xⁱ(x)∂/∂xⁱ where the coefficient functions Xⁱ are smooth. Vector fields act as derivations on the algebra of smooth functions, generating flows (one-parameter families of diffeomorphisms) that describe how points move along the field.

## Questions

```yaml
- question: "A vector field X on a compact manifold M always generates a complete flow — meaning the integral curves exist for all time t ∈ (-∞, ∞). On a non-compact manifold, this can fail. Why?"
  type: multiple-choice
  options:
    - "On non-compact manifolds, vector fields are not smooth, so integral curves are not defined"
    - "Integral curves on non-compact manifolds can escape to infinity in finite time, preventing extension beyond that time"
    - "Non-compact manifolds do not have tangent bundles, so vector fields cannot be defined"
    - "The flow equations have no solutions on non-compact manifolds because the ODE existence theorem fails"
  answer: 1
  explanation: "On a non-compact manifold, integral curves can leave every compact set in finite time — they 'run off to infinity.' For example, the vector field X = x²∂/∂x on ℝ has the integral curve x(t) = 1/(1-t) starting at x=1, which blows up at t=1. On a compact manifold, integral curves have nowhere to escape to, so the ODE existence/uniqueness theorem guarantees the flow extends for all time. This is a consequence of compactness ensuring that any finite-time limit of the integral curve must converge to a point in M."

- question: "Vector fields on a smooth manifold form a module over the ring of smooth functions C∞(M), not merely a vector space over ℝ."
  type: true-false
  answer: true
  explanation: "You can multiply a vector field X by a smooth function f to get a new vector field fX, defined by (fX)_p = f(p)·X_p. This operation satisfies the module axioms. The set of vector fields is also a vector space over ℝ (you can add fields and scale by constants), but the module structure over C∞(M) is richer and more useful. This distinction matters: for instance, the C∞(M)-linearity (or lack thereof) of various operations on vector fields distinguishes tensorial operations from non-tensorial ones."

- question: "Let X = x∂/∂x + y∂/∂y on ℝ². What does the flow of X look like geometrically, and what is the flow map φt(x₀, y₀)?"
  type: short-answer
  answer: "The flow is radial expansion/contraction: φt(x₀, y₀) = (eᵗx₀, eᵗy₀). Each point moves radially outward from the origin with exponential speed. The integral curves are rays from the origin (excluding the origin itself, which is a fixed point). The flow dilates distances by a factor of eᵗ."
  explanation: "The system of ODEs is dx/dt = x, dy/dt = y, with solutions x(t) = x₀eᵗ, y(t) = y₀eᵗ. This is the flow of the Euler vector field, which generates scaling transformations. Each φt is a diffeomorphism (in fact, a linear map — multiplication by eᵗ). The fixed point at the origin corresponds to the zero of the vector field."

- question: "A smooth function f : M → ℝ is constant along the integral curves of a vector field X if and only if X(f) = 0 everywhere."
  type: true-false
  answer: true
  explanation: "If γ(t) is an integral curve of X, then d/dt f(γ(t)) = X_γ(t)(f). So f is constant along γ if and only if Xf vanishes along γ. If X(f) = 0 everywhere on M, then f is constant on every integral curve. Functions satisfying X(f) = 0 are called first integrals or conservation laws of the vector field. This characterization is fundamental in mechanics: conserved quantities are exactly the functions annihilated by the Hamiltonian vector field."
```

## Explainer

A tangent vector lives at a single point. A **vector field** is the global version: a rule that assigns a tangent vector X_p ∈ TpM to every point p ∈ M, smoothly. In local coordinates (x¹, ..., xⁿ), this means X = Xⁱ(x) ∂/∂xⁱ where the component functions Xⁱ are smooth real-valued functions. You can think of a vector field as an arrow attached to every point of the manifold, varying smoothly from point to point — like a wind map or a velocity field in fluid dynamics.

Vector fields act on smooth functions: given f ∈ C∞(M), the function Xf defined by (Xf)(p) = X_p(f) is again smooth. This makes each vector field a **derivation** of the algebra C∞(M) — a linear map satisfying the Leibniz rule X(fg) = f·X(g) + g·X(f). In fact, derivations of C∞(M) are in bijection with smooth vector fields, so you can equivalently define a vector field as a derivation of the function algebra. This algebraic perspective becomes essential when defining Lie brackets and connections.

The **flow** of a vector field is the family of diffeomorphisms φt : M → M obtained by following integral curves for time t. An integral curve γ(t) satisfies γ'(t) = X_γ(t) — at each moment, its velocity equals the vector field at its current position. The existence and uniqueness theorem for ODEs guarantees that through each point there passes a unique integral curve, at least for short time. On compact manifolds, the flow exists for all time (the vector field is **complete**). The flow satisfies the group property φs ∘ φt = φs+t, making it a one-parameter group of diffeomorphisms.

The space of all smooth vector fields on M, denoted 𝔛(M) or Γ(TM), has a rich algebraic structure. It is an infinite-dimensional real vector space, and more importantly, a module over C∞(M) — you can multiply vector fields by smooth functions. This module structure is what distinguishes tensor operations from non-tensor operations: a map on vector fields is tensorial (defines a tensor) if and only if it is C∞(M)-linear. The Lie bracket, which measures the failure of flows to commute, is a fundamental non-tensorial operation that we encounter next.
