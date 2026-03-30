---
id: lie-groups-and-lie-algebras
title: Lie Groups and Lie Algebras
domain: mathematics
course: differential-geometry
prerequisites:
  - id: smooth-manifolds
    type: hard
  - id: vector-fields-differential-geometry
    type: hard
  - id: lie-brackets
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
tags:
  - lie-groups
  - lie-algebras
  - matrix-groups
  - symmetry
stage: expert
status: validated
---

# Lie Groups and Lie Algebras

## Core Idea
A Lie group is a smooth manifold that is also a group, with smooth multiplication and inversion. Its Lie algebra — the tangent space at the identity equipped with the Lie bracket — captures the infinitesimal structure of the group. The exponential map connects the Lie algebra to the group, converting algebra problems to geometry and vice versa. Lie groups are the mathematical language of continuous symmetry, appearing as isometry groups of Riemannian manifolds, structure groups of bundles, and gauge groups in physics.

## Questions

```yaml
- question: "The Lie algebra of the rotation group SO(3) consists of 3×3 skew-symmetric matrices. What is the dimension of this Lie algebra, and what does it represent geometrically?"
  type: multiple-choice
  options:
    - "Dimension 3 — each element represents an infinitesimal rotation about some axis in ℝ³"
    - "Dimension 9 — each element is an arbitrary 3×3 matrix"
    - "Dimension 6 — each element represents a rotation and a translation"
    - "Dimension 1 — each element represents a rotation angle"
  answer: 0
  explanation: "The space of 3×3 skew-symmetric matrices (Aᵀ = -A) has dimension 3, with basis elements corresponding to infinitesimal rotations about the x, y, and z axes. The Lie bracket [A,B] = AB - BA is the commutator of matrices, and it captures how infinitesimal rotations interact — the fact that [A,B] ≠ 0 in general reflects the non-commutativity of rotations. The exponential map exp : so(3) → SO(3) sends a skew-symmetric matrix to the rotation it generates: exp(tA) is rotation about the axis of A by angle t|A|."

- question: "The exponential map of a Lie group is always surjective (every group element is the exponential of some Lie algebra element)."
  type: true-false
  answer: false
  explanation: "Surjectivity holds for compact connected Lie groups (like SO(n), SU(n), and any compact group) but fails in general. The classic counterexample is SL(2, ℝ): the matrix diag(-e, -1/e) for e > 0 is in SL(2, ℝ) but is not the exponential of any element of sl(2, ℝ). For connected Lie groups, every element is a product of exponentials (by the Lie group-Lie algebra correspondence), but it may not be a single exponential."

- question: "A Lie group homomorphism φ : G → H induces a Lie algebra homomorphism dφ_e : 𝔤 → 𝔥 at the identity. What key property does dφ_e preserve?"
  type: short-answer
  answer: "The Lie bracket: dφ_e([X, Y]) = [dφ_e(X), dφ_e(Y)] for all X, Y ∈ 𝔤. A Lie algebra homomorphism is a linear map that preserves the bracket. This is because the Lie bracket of left-invariant vector fields is compatible with group homomorphisms — pushing forward by φ commutes with the bracket. The correspondence between Lie group homomorphisms and Lie algebra homomorphisms is one of the central results of Lie theory."
  explanation: "For simply connected Lie groups, the correspondence is a bijection: every Lie algebra homomorphism 𝔤 → 𝔥 lifts uniquely to a Lie group homomorphism G → H. This means the Lie algebra completely determines the simply connected Lie group — a remarkable linearization of a nonlinear object."

- question: "Every compact Lie group admits a bi-invariant Riemannian metric — a metric invariant under both left and right multiplication."
  type: true-false
  answer: true
  explanation: "The construction uses averaging (integration over the group with respect to the Haar measure). Start with any left-invariant metric (obtained by choosing an inner product on the Lie algebra and left-translating). Average it over right translations using the Haar measure of the compact group. The result is bi-invariant. For bi-invariant metrics, the Levi-Civita connection has a beautiful formula: ∇_X Y = ½[X,Y] for left-invariant fields. Geodesics through the identity are one-parameter subgroups, and the Riemannian exponential equals the Lie group exponential."
```

## Explainer

A **Lie group** is a group that is simultaneously a smooth manifold, with the group operations (multiplication μ : G × G → G and inversion ι : G → G) being smooth maps. The classical examples are matrix groups: GL(n, ℝ) (invertible matrices), O(n) (orthogonal matrices), SO(n) (rotations), SL(n) (determinant-1 matrices), U(n) and SU(n) (unitary matrices). These are all smooth submanifolds of the space of matrices, and the group operations are restrictions of polynomial (hence smooth) maps.

The **Lie algebra** 𝔤 of G is the tangent space at the identity TeG, equipped with the Lie bracket inherited from left-invariant vector fields. A vector X ∈ TeG extends uniquely to a left-invariant vector field X̃ on G (by left-translating: X̃_g = dL_g(X)). The bracket [X, Y] is defined as the bracket of the corresponding left-invariant fields: [X, Y] = [X̃, Ỹ]_e. For matrix groups, this bracket is the matrix commutator [A, B] = AB - BA. The Lie algebra is a finite-dimensional vector space with a bilinear, antisymmetric bracket satisfying the Jacobi identity.

The **exponential map** exp : 𝔤 → G sends X to the time-1 flow of the left-invariant vector field X̃. Equivalently, exp(X) = γ_X(1) where γ_X is the unique one-parameter subgroup with γ_X'(0) = X. For matrix groups, this is the matrix exponential exp(A) = I + A + A²/2! + .... The exponential map is a local diffeomorphism near 0 ∈ 𝔤 (by the inverse function theorem), providing coordinates on a neighborhood of the identity. The Baker-Campbell-Hausdorff formula exp(X)exp(Y) = exp(X + Y + ½[X,Y] + ...) shows how the Lie bracket controls the group multiplication to higher order.

Lie groups pervade differential geometry as **symmetry groups**. The isometry group of a Riemannian manifold is a Lie group (the Myers-Steenrod theorem). The structure group of a vector bundle or principal bundle is a Lie group. Gauge theories in physics are built on Lie groups. The representation theory of Lie groups — studying homomorphisms from G to GL(V) — is the mathematical backbone of quantum mechanics and particle physics. The classification of simple Lie algebras (Killing, Cartan) is one of the great achievements of 19th-century mathematics, organizing all possible continuous symmetries into families (A_n, B_n, C_n, D_n) and exceptional cases (G₂, F₄, E₆, E₇, E₈).
