---
id: lie-group-representations-intro
title: Lie Group Representations (Introduction)
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: matrix-representations
  type: hard
- id: linear-transformations
  type: soft
builds-toward:
- representations-of-sl2
tags:
- lie-group
- compact-group
- exponential-map
- continuous-representation
- peter-weyl
stage: expert
status: validated
---

# Lie Group Representations (Introduction)

## Core Idea
A Lie group is a group that is also a smooth manifold — its elements can vary continuously and the group operations are smooth. Representations of Lie groups are required to be continuous (or smooth) homomorphisms G → GL(V), which is a much stronger constraint than for finite groups. For compact Lie groups (like SO(n), SU(n), U(n)), a complete analogue of finite group theory holds: every representation is completely reducible, characters determine representations, and orthogonality relations hold — with integrals over the group (via Haar measure) replacing finite sums.

## Questions

```yaml
- question: "Which of the following is a compact Lie group?"
  type: multiple-choice
  options:
    - "GL_n(ℝ) — the general linear group"
    - "SL_2(ℝ) — the special linear group"
    - "SO(3) — the rotation group in 3 dimensions"
    - "The additive group (ℝ, +)"
  answer: 2
  explanation: "SO(3) is the group of 3×3 orthogonal matrices with determinant 1. It is compact because the orthogonality condition AᵀA = I constrains the entries (they satisfy Σ aᵢⱼ² = 1 for each column), making it a closed bounded subset of ℝ⁹. GL_n(ℝ) is not compact (matrices can have arbitrarily large entries). SL_2(ℝ) is closed but not bounded. (ℝ, +) is not compact."

- question: "For compact Lie groups, Maschke's theorem generalizes: every continuous finite-dimensional representation is completely reducible. What replaces the averaging sum (1/|G|)Σ_{g∈G}?"
  type: short-answer
  answer: "Integration with respect to the Haar measure: ∫_G f(g) dg. The Haar measure is the unique (up to scale) left-invariant Borel measure on G, and compactness ensures it has finite total mass (normalized to 1)."
  explanation: "For finite groups, averaging is (1/|G|)Σ_{g∈G} f(g). For compact Lie groups, the finite sum becomes an integral over the group with respect to Haar measure. The key properties — left invariance (∫f(hg)dg = ∫f(g)dg) and finite total volume — ensure that the averaging trick from Maschke's proof goes through identically. Non-compact groups lack a finite invariant measure, so complete reducibility can fail."

- question: "The exponential map exp: 𝔤 → G connects the Lie algebra to the Lie group. For matrix groups, exp(X) = Σ_{n=0}^∞ Xⁿ/n!."
  type: true-false
  answer: true
  explanation: "For a matrix Lie group G ⊆ GL_n(ℝ), the Lie algebra 𝔤 consists of matrices X such that exp(tX) ∈ G for all t ∈ ℝ. The exponential map exp: 𝔤 → G defined by the matrix power series is a local diffeomorphism near the identity. It connects infinitesimal (Lie algebra) information to global (Lie group) information. For example, the Lie algebra of SO(3) is the space of 3×3 skew-symmetric matrices, and exp maps them to rotation matrices."

- question: "The Peter-Weyl theorem for compact Lie groups is the analogue of which result for finite groups?"
  type: multiple-choice
  options:
    - "Lagrange's theorem"
    - "The decomposition of the regular representation into irreducibles"
    - "The Sylow theorems"
    - "The Jordan-Hölder theorem"
  answer: 1
  explanation: "For a finite group G, the regular representation decomposes as ℂ[G] ≅ ⊕ᵢ Vᵢ^{dᵢ}, and the matrix coefficients of irreducible representations form an orthogonal basis of L²(G). The Peter-Weyl theorem generalizes this to compact groups: the matrix coefficients of all irreducible unitary representations form a complete orthonormal system in L²(G, dg). This is the representation-theoretic foundation of harmonic analysis on compact groups."
```

## Explainer

**Lie groups** are groups with a manifold structure — they have both algebraic and geometric properties. Examples include GL_n(ℝ) (invertible n×n real matrices), SO(n) (rotations in n dimensions), SU(n) (special unitary matrices), and the circle group U(1) ≅ S¹. A representation of a Lie group is a continuous (equivalently, smooth) homomorphism ρ: G → GL(V). The continuity requirement is the key difference from finite group theory: it eliminates pathological homomorphisms and connects the representation theory to the group's geometry.

The **exponential map** exp: 𝔤 → G connects the Lie algebra 𝔤 (the tangent space at the identity, with Lie bracket [X,Y] = XY − YX for matrix groups) to the Lie group. A representation ρ: G → GL(V) induces a Lie algebra representation dρ: 𝔤 → 𝔤𝔩(V) defined by dρ(X) = (d/dt)|_{t=0} ρ(exp(tX)). For connected, simply connected groups, the representation theories of G and 𝔤 are equivalent — every Lie algebra representation integrates to a group representation. This reduces many questions to linear algebra on the Lie algebra.

For **compact Lie groups**, the theory parallels the finite group case remarkably closely. The Haar measure dg (the unique normalized left-invariant measure) replaces the counting measure (1/|G|)Σ. Maschke's theorem holds: every continuous finite-dimensional representation is completely reducible, via the same averaging argument with integrals replacing sums. Schur's lemma, orthogonality relations, and character theory all carry over. The irreducible representations are finite-dimensional and classified by **highest weights** — a combinatorial datum determined by the group's root system.

The **Peter-Weyl theorem** is the grand generalization. For a compact Lie group G, the matrix coefficients of all irreducible unitary representations form a complete orthonormal system in L²(G). The Hilbert space L²(G) decomposes as a completed direct sum: L²(G) ≅ ⊕̂ᵢ Vᵢ ⊗ Vᵢ*, where the sum runs over all irreducible representations. This is the infinite-dimensional analogue of ℂ[G] ≅ ⊕ Vᵢ^{dᵢ}. For non-compact groups (like SL_2(ℝ)), the theory is vastly more complicated: irreducible representations can be infinite-dimensional, complete reducibility fails, and the decomposition of L²(G) involves both discrete and continuous spectrum — the Plancherel formula replaces the Peter-Weyl theorem.
