---
id: submanifolds
title: Submanifolds
domain: mathematics
course: differential-geometry
prerequisites:
  - id: smooth-manifolds
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
tags:
  - submanifolds
  - immersions
  - embeddings
  - regular-values
stage: advanced
status: validated
---

# Submanifolds

## Core Idea
A submanifold is a subset of a manifold that is itself a manifold in a compatible way. Embedded submanifolds arise as level sets of smooth maps at regular values (the preimage theorem), as images of injective immersions, or as solution sets of constraint equations. The tangent space of a submanifold at a point is a subspace of the ambient tangent space, and the codimension determines how many independent constraints define the submanifold locally.

## Questions

```yaml
- question: "Let F : ℝ³ → ℝ be defined by F(x,y,z) = x² + y² + z² - 1. By the regular value theorem, F⁻¹(0) = S² is a smooth submanifold of ℝ³ because..."
  type: multiple-choice
  options:
    - "F is a smooth function and 0 is in its image"
    - "The derivative dF is surjective (has rank 1) at every point of F⁻¹(0)"
    - "S² is compact and Hausdorff"
    - "F⁻¹(0) is a closed subset of ℝ³"
  answer: 1
  explanation: "The regular value theorem (preimage theorem) states that if c is a regular value of F — meaning dF_p is surjective for every p ∈ F⁻¹(c) — then F⁻¹(c) is a smooth submanifold of codimension equal to the dimension of the codomain. Here dF = (2x, 2y, 2z), which is nonzero (hence surjective as a map to ℝ) at every point of S² (where x²+y²+z² = 1). So 0 is a regular value and S² is a smooth 2-dimensional submanifold of ℝ³."

- question: "An immersion is always an embedding."
  type: true-false
  answer: false
  explanation: "An immersion is a smooth map whose derivative is injective at every point, but it need not be an embedding. An embedding additionally requires the map to be a homeomorphism onto its image (in the subspace topology). The figure-eight curve t ↦ (sin 2t, sin t) is an immersion of ℝ into ℝ² that is not an embedding because it crosses itself. A more subtle example: the irrational-slope line on a torus is an injective immersion that is not an embedding because its image is dense in the torus."

- question: "What is the relationship between the tangent space of a submanifold S ⊂ M at a point p and the tangent space of the ambient manifold M at p?"
  type: short-answer
  answer: "TpS is naturally a linear subspace of TpM. If S has dimension k and M has dimension n, then TpS is a k-dimensional subspace of the n-dimensional space TpM. When S is defined as the level set F⁻¹(c) of a smooth map F : M → N, then TpS = ker(dFp) — the tangent space of S is the kernel of the derivative of the defining map. The normal directions to S at p correspond to the quotient TpM/TpS (or, with a metric, to the orthogonal complement)."
  explanation: "This is the infinitesimal version of the inclusion S ↪ M. The inclusion map i : S → M has derivative di_p : TpS → TpM which is injective, so TpS embeds as a subspace. For level sets, the tangent space consists of all tangent vectors that are 'tangent to the constraint surface' — vectors along which the constraint function F does not change to first order."

- question: "The dimension of a submanifold defined as the level set of a smooth map F : M → ℝᵏ at a regular value is dim(M) - k."
  type: true-false
  answer: true
  explanation: "When c is a regular value of F : Mⁿ → ℝᵏ (so dFp has rank k at every point of F⁻¹(c)), the preimage theorem says F⁻¹(c) is a smooth submanifold of dimension n - k. Each component of F imposes one independent constraint, removing one dimension. For example, one equation F = 0 in ℝ³ gives a surface (3-1=2), two independent equations give a curve (3-2=1), and three independent equations give isolated points (3-3=0)."
```

## Explainer

The simplest way to construct a submanifold is as a **level set**. If F : M → N is a smooth map and c ∈ N is a **regular value** (meaning dF_p is surjective for every p ∈ F⁻¹(c)), then the **preimage theorem** guarantees that F⁻¹(c) is a smooth submanifold of M with dimension dim(M) - dim(N). This is the manifold version of the implicit function theorem from multivariable calculus. The sphere S² = {x² + y² + z² = 1} ⊂ ℝ³, the orthogonal group O(n) = {A : AᵀA = I} ⊂ GL(n), and every smooth curve in the plane defined by an equation f(x,y) = 0 with nonvanishing gradient are examples.

More generally, a smooth map f : S → M is an **immersion** if df_p is injective at every point of S, and an **embedding** if it is additionally a homeomorphism onto its image. An embedded submanifold is the image of an embedding — it inherits a smooth structure from the ambient manifold and sits inside M "without crossing itself." Every compact manifold that immerses in M actually embeds (the Whitney embedding theorem gives quantitative dimension bounds). An immersed submanifold may have self-intersections or may fail to have the subspace topology, as with dense curves on tori.

The tangent space of a submanifold S at a point p is a subspace of the ambient tangent space: TpS ⊆ TpM. For a level set S = F⁻¹(c), the tangent space is the kernel of the derivative: TpS = ker(dFp). The **codimension** of S in M is dim(M) - dim(S), and it equals the number of independent constraints defining S. When M is equipped with a Riemannian metric, the tangent space splits as TpM = TpS ⊕ (TpS)⊥, where the orthogonal complement is the **normal space**. This split is fundamental to the geometry of submanifolds — curvature, the second fundamental form, and the Gauss-Codazzi equations all arise from studying how TpS sits inside TpM.

Submanifolds are ubiquitous in mathematics and physics. Configuration spaces of mechanical systems (the set of positions satisfying constraints) are submanifolds of a product of copies of ℝ³. Lie groups are submanifolds of matrix spaces. Phase spaces in Hamiltonian mechanics are submanifolds defined by energy conservation. The theory of submanifolds connects the intrinsic geometry of S to the extrinsic geometry of how S sits in M — a theme that runs from the Gauss-Bonnet theorem through modern geometric analysis.
