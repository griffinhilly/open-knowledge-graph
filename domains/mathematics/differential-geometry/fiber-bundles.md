---
id: fiber-bundles
title: Fiber Bundles
domain: mathematics
course: differential-geometry
prerequisites:
  - id: smooth-manifolds
    type: hard
  - id: submanifolds
    type: soft
  - id: quotient-spaces
    type: soft
tags:
  - fiber-bundles
  - local-trivialization
  - transition-functions
  - structure-group
stage: expert
status: validated
---

# Fiber Bundles

## Core Idea
A fiber bundle is a space E that locally looks like a product B × F (base × fiber) but may be globally twisted. The projection π : E → B maps each fiber π⁻¹(b) homeomorphically to the standard fiber F, but the fibers may be "glued together" nontrivially across the base. Transition functions encode this twisting and take values in the structure group G ⊂ Aut(F). Fiber bundles unify tangent bundles, vector bundles, principal bundles, and covering spaces into a single framework, and their topology (measured by characteristic classes) is central to differential geometry and physics.

## Questions

```yaml
- question: "The Mobius band is a fiber bundle over the circle S¹ with fiber the interval [-1, 1]. What is its structure group?"
  type: multiple-choice
  options:
    - "The trivial group {id}"
    - "ℤ₂ = {id, reflection} acting on [-1,1] by x ↦ -x"
    - "SO(2), the rotation group"
    - "GL(1, ℝ), the group of nonzero scalars"
  answer: 1
  explanation: "Cover S¹ by two overlapping arcs U₁, U₂. Over each arc, the bundle is a product U_i × [-1,1]. On one component of U₁ ∩ U₂, the transition function is the identity; on the other, it is the reflection x ↦ -x. The transition functions take values in ℤ₂ = {id, reflection}. The Mobius band is nontrivial (not a product) because this transition function is not the identity — the twist encoded by the ℤ₂ element is the essential feature."

- question: "A fiber bundle π : E → B is called trivial if E is diffeomorphic to B × F (as a bundle). The tangent bundle of the sphere S² is trivial."
  type: true-false
  answer: false
  explanation: "The tangent bundle TS² is nontrivial. By the hairy ball theorem, there is no nowhere-vanishing vector field on S² — but if TS² were trivial (isomorphic to S² × ℝ²), then the constant section (p, e₁) would give a nowhere-vanishing vector field. The nontriviality of TS² is detected by the Euler class (which equals χ(S²) = 2 ≠ 0). By contrast, the tangent bundle of S¹ is trivial (S¹ has a nowhere-vanishing vector field — the angular direction), and the tangent bundle of any Lie group is trivial."

- question: "What role do transition functions play in defining a fiber bundle, and why are they valued in a group?"
  type: short-answer
  answer: "Transition functions describe how to glue local trivializations together over overlaps. On U_α ∩ U_β, the two trivializations give two different identifications of the fiber with F, and the transition function g_αβ : U_α ∩ U_β → G ⊂ Aut(F) is the change-of-identification map. They must be group-valued because: (1) g_αα = id (trivially compatible with itself), (2) g_βα = g_αβ⁻¹ (changing identification order inverts the map), and (3) g_αβ g_βγ g_γα = id on triple overlaps (the cocycle condition ensures consistency). The transition functions, up to equivalence, classify the bundle."
  explanation: "This is exactly analogous to how transition maps of coordinate charts define a smooth structure on a manifold. The base space is the same in both cases; what differs is the structure of the fibers and the group acting on them. The cocycle condition is what ensures the local pieces patch together into a well-defined global object."
```

## Explainer

The simplest example of a fiber bundle is a **product** B × F, where the projection π(b, f) = b maps each "fiber" {b} × F to the base point b. But many natural geometric objects have this local product structure without being globally a product. The **Mobius band** is locally a product of an interval with a line segment, but globally it has a twist. The **tangent bundle** TM of a manifold is locally a product U × ℝⁿ (via coordinate charts), but the global structure may be twisted (as for TS²).

A **fiber bundle** π : E → B with fiber F and structure group G consists of: a total space E, a base space B, a projection π, a typical fiber F, and an open cover {U_α} of B with local trivializations φ_α : π⁻¹(U_α) → U_α × F. On overlaps U_α ∩ U_β, the change of trivialization φ_α ∘ φ_β⁻¹ acts as (b, f) ↦ (b, g_αβ(b) · f) for smooth functions g_αβ : U_α ∩ U_β → G. These **transition functions** satisfy the cocycle condition g_αβ g_βγ = g_αγ and encode the global twisting of the bundle.

The **structure group** G is the group of symmetries of the fiber that appears in the transition functions. For vector bundles (fibers are vector spaces), G ⊂ GL(n) acts by linear transformations. For principal bundles (fibers are copies of G itself), the group acts by left or right multiplication. For frame bundles, G = GL(n) or O(n). The structure group encodes what kind of geometry the fibers carry. Reducing the structure group (e.g., from GL(n) to O(n)) corresponds to adding geometric structure (e.g., a metric on the fibers).

Fiber bundles are classified by their transition functions up to equivalence. Two bundles with cohomologous transition functions (related by a coboundary) are isomorphic. This leads to the classification of bundles by **Čech cohomology** H¹(B; G) — a topological invariant of the base. For more refined invariants, **characteristic classes** (Chern classes, Pontryagin classes, Euler class, Stiefel-Whitney classes) are cohomology classes of B computed from the curvature of connections on the bundle. These are the primary tools for distinguishing non-isomorphic bundles and for understanding the global topology of geometric structures.
