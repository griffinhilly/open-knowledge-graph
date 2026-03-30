---
id: principal-bundles
title: Principal Bundles
domain: mathematics
course: differential-geometry
prerequisites:
  - id: fiber-bundles
    type: hard
  - id: lie-groups-and-lie-algebras
    type: hard
tags:
  - principal-bundles
  - gauge-theory
  - frame-bundle
  - associated-bundles
stage: expert
status: validated
---

# Principal Bundles

## Core Idea
A principal G-bundle is a fiber bundle whose fiber is a Lie group G, acting freely and transitively on each fiber by right multiplication. Unlike vector bundles (where fibers are vector spaces), principal bundles have no preferred "zero" in each fiber — every point is equivalent. The frame bundle of a manifold is a principal GL(n)-bundle, and connections on principal bundles (gauge fields) are the mathematical foundation of gauge theory in physics. Every vector bundle arises from a principal bundle via the associated bundle construction.

## Questions

```yaml
- question: "The frame bundle F(M) of an n-manifold M has as its fiber over p the set of all ordered bases (frames) for TpM. What is its structure group?"
  type: multiple-choice
  options:
    - "O(n), the orthogonal group"
    - "GL(n, ℝ), the general linear group"
    - "SL(n, ℝ), the special linear group"
    - "SO(n), the special orthogonal group"
  answer: 1
  explanation: "The frame bundle F(M) is a principal GL(n, ℝ)-bundle. GL(n) acts on frames by changing basis: if (e₁,...,eₙ) is a frame and A ∈ GL(n), then (e₁,...,eₙ)·A = (Aⁱ₁eᵢ,...,Aⁱₙeᵢ) gives another frame. This action is free and transitive on each fiber (any two frames are related by a unique invertible matrix). Choosing a Riemannian metric reduces the structure group to O(n) — the orthonormal frame bundle is a principal O(n)-bundle. An orientation further reduces to SO(n)."

- question: "A connection on a principal G-bundle is a g-valued 1-form on the total space (where g is the Lie algebra of G). This is equivalent to specifying a horizontal distribution in the total space."
  type: true-false
  answer: true
  explanation: "A connection 1-form ω on a principal bundle P assigns to each tangent vector of P an element of the Lie algebra g. The kernel of ω at each point defines a horizontal subspace complementary to the vertical subspace (the tangent to the fiber). The horizontal distribution tells you how to lift curves from the base to the total space — this is parallel transport. The curvature 2-form Ω = dω + ½[ω, ω] measures the failure of the horizontal distribution to be integrable (the Frobenius condition)."

- question: "How does the associated bundle construction relate principal bundles to vector bundles?"
  type: short-answer
  answer: "Given a principal G-bundle P → M and a representation ρ : G → GL(V) of G on a vector space V, the associated bundle P ×_G V = (P × V)/G is a vector bundle over M with fiber V. The equivalence relation is (pg, v) ~ (p, ρ(g)v). Every vector bundle arises this way from its frame bundle. Conversely, given a vector bundle E, its frame bundle F(E) is a principal GL(n)-bundle, and E ≅ F(E) ×_{GL(n)} ℝⁿ via the standard representation. This correspondence makes principal bundles the universal framework for vector bundles."
  explanation: "The associated bundle construction is the bridge between principal bundles (where the group acts freely on fibers with no preferred point) and vector bundles (where fibers have linear structure). Different representations of the same group produce different vector bundles from the same principal bundle — this is how tensor bundles arise from the frame bundle via tensor representations of GL(n)."
```

## Explainer

A **principal G-bundle** P → M is a fiber bundle where the Lie group G acts freely and transitively on each fiber by right multiplication. "Free" means no group element except the identity fixes any point; "transitive" means any two points in the same fiber are related by a group element. This makes each fiber a copy of G, but with no preferred identity element — the fibers are "G-torsors." The frame bundle F(M), whose fiber over p is the set of all ordered bases of TpM, is the canonical example: GL(n) acts by change of basis, freely and transitively.

A **connection** on a principal bundle is specified by a Lie-algebra-valued 1-form ω on the total space P satisfying compatibility conditions with the G-action. Equivalently, it is a smooth choice of horizontal subspace at each point of P, complementary to the vertical (fiber) direction. The horizontal subspace tells you how to "lift" a curve in the base M to a curve in P — this is the generalization of parallel transport. The **curvature** of the connection is the 2-form Ω = dω + ½[ω ∧ ω], measuring the failure of the horizontal distribution to be integrable. Zero curvature means the horizontal subspaces fit together into a foliation — the bundle is "flat."

The **associated bundle construction** converts a principal bundle into a vector bundle (or any other fiber bundle). Given a principal G-bundle P → M and a left action of G on a space F (e.g., a representation G → GL(V)), the associated bundle P ×_G F is the quotient (P × F)/G where (pg, f) ~ (p, g·f). For F = ℝⁿ with the standard representation of GL(n), the associated bundle of the frame bundle is the tangent bundle: F(M) ×_{GL(n)} ℝⁿ ≅ TM. For the dual representation, you get T*M. For tensor representations, you get tensor bundles. This is why the frame bundle is "universal" — all natural vector bundles on M come from it.

In physics, **gauge theory** is the theory of connections on principal bundles. The electromagnetic field is a connection on a principal U(1)-bundle; the weak and strong nuclear forces are connections on SU(2) and SU(3) bundles. The curvature of the connection is the field strength, and the Yang-Mills equations (generalizing Maxwell's equations) are the Euler-Lagrange equations for the curvature. Gauge transformations — changes of local trivialization — are sections of the associated bundle of automorphisms, and physical observables are gauge-invariant quantities. The principal bundle framework unifies all fundamental forces into a single geometric language.
