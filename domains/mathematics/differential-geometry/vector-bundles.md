---
id: vector-bundles
title: Vector Bundles
domain: mathematics
course: differential-geometry
prerequisites:
  - id: fiber-bundles
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
  - id: linear-transformations
    type: hard
tags:
  - vector-bundles
  - sections
  - tangent-bundle
  - cotangent-bundle
stage: expert
status: validated
---

# Vector Bundles

## Core Idea
A vector bundle is a fiber bundle whose fibers are vector spaces and whose transition functions are linear maps (elements of GL(n)). The tangent bundle, cotangent bundle, and their tensor products are the fundamental vector bundles in differential geometry. Sections of vector bundles generalize vector fields and differential forms. Connections on vector bundles extend covariant differentiation beyond the tangent bundle, enabling the study of curvature for any geometric vector bundle.

## Questions

```yaml
- question: "The tangent bundle TM, cotangent bundle T*M, and the bundle of k-forms Λᵏ(T*M) are all examples of vector bundles over M. What distinguishes a vector bundle from a general fiber bundle?"
  type: multiple-choice
  options:
    - "Vector bundles have fibers that are vector spaces and transition functions in GL(n)"
    - "Vector bundles are always trivial (isomorphic to a product)"
    - "Vector bundles must have one-dimensional fibers"
    - "Vector bundles require a Riemannian metric on the base"
  answer: 0
  explanation: "A vector bundle has vector space fibers and linear transition functions. The GL(n) structure group preserves the vector space structure of fibers, so operations like addition of sections and scalar multiplication are well-defined globally. General fiber bundles have arbitrary fibers (circles, Lie groups, homogeneous spaces) with arbitrary structure groups. Not all vector bundles are trivial (TS² is not), fibers can have any dimension, and no metric is needed."

- question: "A global section of the tangent bundle TM is a vector field. A vector bundle E → M admits a nowhere-zero global section if and only if..."
  type: multiple-choice
  options:
    - "E is trivial"
    - "The Euler class of E vanishes (when defined)"
    - "E has a connection"
    - "M is compact"
  answer: 1
  explanation: "A nowhere-zero section exists if and only if the Euler class e(E) ∈ Hⁿ(M) vanishes (for oriented rank-n bundles). The Euler class is the primary obstruction to finding a nowhere-zero section. For the tangent bundle TM, e(TM) = χ(M) (the Euler characteristic), which is why S² (χ=2) has no nowhere-vanishing vector field but the torus (χ=0) does. A bundle admitting a nowhere-zero section can split off a trivial line bundle: E ≅ E' ⊕ ε¹. But having a nowhere-zero section does not make E fully trivial."

- question: "The Whitney sum E ⊕ F and tensor product E ⊗ F of vector bundles over M are again vector bundles. How are their fibers related to the fibers of E and F?"
  type: short-answer
  answer: "The fiber of E ⊕ F at a point p is the direct sum Ep ⊕ Fp (as vector spaces), with dimension rank(E) + rank(F). The fiber of E ⊗ F at p is the tensor product Ep ⊗ Fp, with dimension rank(E) · rank(F). The transition functions of E ⊕ F are block diagonal (g_E ⊕ g_F), and those of E ⊗ F are the tensor product (g_E ⊗ g_F) of the transition functions. These operations make vector bundles over M into a semiring (the Grothendieck group completion gives K-theory)."
  explanation: "These algebraic operations on vector bundles parallel operations on vector spaces. The dual bundle E* has fibers (Ep)*, the determinant bundle det(E) = Λʳᵃⁿᵏ⁽ᴱ⁾(E) has one-dimensional fibers, and the endomorphism bundle End(E) = E* ⊗ E has fibers GL(Ep). The rich algebraic structure of vector bundles is the foundation of K-theory, a generalized cohomology theory that captures bundle topology."
```

## Explainer

A **vector bundle** of rank k over a manifold M is a fiber bundle π : E → M where each fiber Ep = π⁻¹(p) is a k-dimensional real vector space, and the transition functions g_αβ : U_α ∩ U_β → GL(k, ℝ) act linearly on the fibers. The vector space structure of fibers means you can add sections and multiply them by smooth functions — the space of sections Γ(E) is a module over C∞(M), just like the space of vector fields.

The **tangent bundle** TM (fibers are tangent spaces TpM) and the **cotangent bundle** T*M (fibers are cotangent spaces T*pM) are the primary examples. Their tensor products give all tensor bundles: T^{r,s}M = TM⊗r ⊗ (T*M)⊗s, whose sections are (r,s)-tensor fields. The bundle of k-forms Λᵏ(T*M) is a sub-bundle of T^{0,k}M. Riemannian metrics are sections of the symmetric part of T*M ⊗ T*M. Connections, curvature tensors, and all the objects of Riemannian geometry are sections of various vector bundles.

A **connection** on a vector bundle E is a generalization of the covariant derivative: ∇ : 𝔛(M) × Γ(E) → Γ(E) satisfying C∞(M)-linearity in the first argument and the Leibniz rule ∇_X(f·s) = X(f)·s + f·∇_X s in the second. Connections on E need not come from any metric — they are additional structure. The **curvature** of a bundle connection is F(X,Y) = ∇_X ∇_Y - ∇_Y ∇_X - ∇_{[X,Y]}, now an endomorphism-valued 2-form (a section of Λ²(T*M) ⊗ End(E)). This generalizes the Riemann curvature tensor, which is the curvature of the Levi-Civita connection on TM.

**Characteristic classes** are topological invariants of vector bundles computed from the curvature of any connection. The **Chern-Weil theory** produces closed differential forms from invariant polynomials applied to the curvature form, and their de Rham cohomology classes are independent of the connection chosen. Chern classes (for complex bundles), Pontryagin classes (for real bundles), the Euler class (for oriented bundles), and Stiefel-Whitney classes (mod 2) measure the topological twisting of the bundle. The nontriviality of TS² is detected by its Euler class e(TS²) = 2 ∈ H²(S²). These invariants are the primary tools in the topological study of manifolds and are central to modern mathematical physics (gauge theory, string theory, topological quantum field theory).
