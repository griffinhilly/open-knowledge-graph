---
id: tangent-vectors-and-tangent-spaces
title: Tangent Vectors and Tangent Spaces
domain: mathematics
course: differential-geometry
prerequisites:
  - id: smooth-manifolds
    type: hard
  - id: linear-transformations
    type: hard
  - id: partial-derivatives
    type: hard
tags:
  - tangent-vectors
  - tangent-vectors-and-tangent-spaces
  - derivations
  - directional-derivatives
stage: advanced
status: validated
---

# Tangent Vectors and Tangent Spaces

## Core Idea
A tangent vector at a point p on a smooth manifold is a derivation — a linear map from smooth functions to real numbers satisfying the Leibniz (product) rule. The tangent space TpM is the vector space of all tangent vectors at p. This definition avoids embedding the manifold in an ambient space, making it intrinsic. In local coordinates, tangent vectors correspond to directional derivatives ∂/∂xⁱ, and TpM has the same dimension as M.

## Questions

```yaml
- question: "A tangent vector v at a point p on an n-dimensional smooth manifold M is formally defined as a derivation on C∞(M). Which of the following is NOT a property that v must satisfy?"
  type: multiple-choice
  options:
    - "Linearity: v(af + bg) = a·v(f) + b·v(g) for smooth functions f, g and constants a, b"
    - "Leibniz rule: v(fg) = f(p)·v(g) + g(p)·v(f)"
    - "v maps C∞(M) to ℝ"
    - "Chain rule: v(f ∘ g) = v(f) · v(g) for smooth functions f and g"
  answer: 3
  explanation: "Tangent vectors as derivations must satisfy linearity and the Leibniz rule (product rule), and they map smooth functions to real numbers. Option D states a 'multiplicative chain rule' that is not part of the definition and is in fact false — it conflates two different things. The chain rule does apply to tangent vectors, but in the form v(f ∘ φ) = Dφ(v)(f), which involves pushforwards, not a simple product. The three defining properties are: (1) maps C∞(M) → ℝ, (2) linearity, (3) Leibniz rule."

- question: "The tangent space at a point on an n-dimensional manifold is an n-dimensional real vector space."
  type: true-false
  answer: true
  explanation: "This is correct and is a fundamental theorem. In local coordinates (x¹, ..., xⁿ), the partial derivative operators ∂/∂x¹|_p, ..., ∂/∂xⁿ|_p form a basis for TpM. Any derivation at p can be uniquely written as a linear combination of these basis vectors: v = vⁱ ∂/∂xⁱ|_p. The proof uses the Leibniz rule to show that a derivation annihilates constants, and then uses a Taylor expansion argument to show the derivation is determined by its action on coordinate functions."

- question: "In ℝ³ viewed as a smooth manifold, the tangent space at any point p is naturally identified with ℝ³ itself. On the sphere S², the tangent space at the north pole (0,0,1) is the horizontal plane z = 1. Why is the intrinsic (derivation) definition preferred over these extrinsic descriptions?"
  type: short-answer
  answer: "The derivation definition works for any smooth manifold without requiring it to be embedded in an ambient Euclidean space. Many important manifolds (such as abstract Lie groups, quotient manifolds, or spacetime in general relativity) are not naturally presented as subsets of ℝⁿ. The extrinsic definition requires choosing an embedding, and different embeddings give different-looking tangent planes that are abstractly isomorphic. The intrinsic definition captures what tangent vectors actually do — act on functions by differentiation — without reference to any ambient space."
  explanation: "While the extrinsic picture (tangent plane touching a surface in ℝ³) is invaluable for building intuition, it depends on an embedding that may not exist or may not be natural. The derivation approach is coordinate-free and works universally. The Whitney embedding theorem guarantees that every smooth manifold can be embedded in some ℝⁿ, so the extrinsic picture is always available in principle — but the intrinsic definition is more fundamental because it depends only on the smooth structure of M itself."

- question: "If (x, y) are local coordinates on a 2-manifold and v = 3∂/∂x + 2∂/∂y at a point p, then v acts on a function f by computing 3(∂f/∂x)(p) + 2(∂f/∂y)(p)."
  type: true-false
  answer: true
  explanation: "This is the operational meaning of the derivation definition in local coordinates. A tangent vector v = vⁱ∂/∂xⁱ acts on a smooth function f by v(f) = vⁱ(∂f/∂xⁱ)(p), which is just the directional derivative of f in the direction (v¹, ..., vⁿ) expressed in the coordinate basis. The components (3, 2) tell you how fast you are moving in each coordinate direction. This connects the abstract derivation definition to the familiar directional derivative from multivariable calculus."
```

## Explainer

In multivariable calculus, the tangent space at a point on a surface in ℝ³ is a plane that just touches the surface — a linear approximation to the surface near that point. But this picture depends on the surface sitting inside ℝ³. On an abstract smooth manifold, there is no ambient space to host a tangent plane. The derivation definition solves this by defining tangent vectors in terms of what they *do* rather than where they *live*: a tangent vector acts on smooth functions by differentiating them.

Formally, a **derivation** at p ∈ M is a linear map v : C∞(M) → ℝ satisfying the Leibniz rule v(fg) = f(p)v(g) + g(p)v(f). The set of all derivations at p forms a vector space under pointwise addition and scalar multiplication — this is the **tangent space** TpM. Two immediate consequences of the Leibniz rule: derivations kill constants (v(c) = 0 for any constant function c), and derivations depend only on the local behavior of f near p (if f = g on a neighborhood of p, then v(f) = v(g)).

In a coordinate chart (U, φ) with coordinates (x¹, ..., xⁿ), the operators ∂/∂xⁱ|_p are derivations. The operator ∂/∂xⁱ|_p acts on f by computing the iᵗʰ partial derivative of f ∘ φ⁻¹ at φ(p). These n derivations form a **basis** for TpM, so dim(TpM) = dim(M). A general tangent vector is v = vⁱ ∂/∂xⁱ|_p, where the coefficients vⁱ are the **components** of v in this coordinate basis. Under a change of coordinates (x¹, ..., xⁿ) → (y¹, ..., yⁿ), the components transform by the Jacobian matrix: v's components in the y-basis are (∂yʲ/∂xⁱ)vⁱ. This transformation law is the classical definition of a "contravariant vector."

A smooth map F : M → N between manifolds induces a linear map dFp : TpM → TF(p)N called the **differential** (or pushforward). It acts by (dFp(v))(g) = v(g ∘ F) for any smooth function g on N. In coordinates, dFp is represented by the Jacobian matrix of F. The differential is the manifold version of the total derivative from multivariable calculus, and it is the primary tool for relating the geometry of different manifolds. If F is a diffeomorphism, then dFp is an isomorphism of tangent spaces.

The **tangent bundle** TM is the disjoint union of all tangent spaces: TM = ∪_p TpM. It is itself a smooth manifold of dimension 2n (n coordinates for the base point, n for the tangent vector). A smooth assignment of a tangent vector to each point of M — a section of the tangent bundle — is a **vector field**, which is the next major concept in differential geometry. The tangent space construction is the gateway to all the linear algebra that happens "fiberwise" on a manifold.
