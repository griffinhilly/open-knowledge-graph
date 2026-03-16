---
id: abelian-categories-homology
title: Abelian Categories and Homological Algebra
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: homology-and-cohomology
  type: hard
builds-toward:
- derived-functors
- triangulated-categories
tags:
- abelian
- homology
- exact-sequence
- kernel
- cokernel
stage: advanced
status: draft
---

# Abelian Categories and Homological Algebra

## Core Idea
An abelian category is an additive category with kernels, cokernels, and images, in which every monomorphism is a kernel and every epimorphism is a cokernel. Abelian categories provide the natural setting for homological algebra: chain complexes, homology, cohomology, and derived functors. Examples include module categories, vector spaces, and abelian groups. The theory of abelian categories abstracts homological algebra to axiomatic foundations.

## How It's Best Learned
Study module categories and vector space categories as canonical abelian examples. Verify the five lemma and snake lemma for abelian categories. Compute derived functors (Ext, Tor) via projective and injective resolutions in abelian categories.

## Common Misconceptions
Abelian categories generalize module categories but are not just 'categorical algebra'—they require specific exactness properties. Not every additive category is abelian; the kernel-cokernel conditions are non-trivial. Abelian category axioms are sufficient for homological algebra but some conclusions require additional structure (e.g., enough projectives).

## Explainer

From your study of abelian categories, you know the axioms: the hom-sets are abelian groups, composition is bilinear, there are finite products, every morphism has a **kernel** and **cokernel**, and every monomorphism is a kernel while every epimorphism is a cokernel. From homology and cohomology you know chain complexes and their homology groups in concrete settings like simplicial homology or singular cohomology. The present topic is the synthesis: abelian categories are precisely the setting in which homological algebra works, not just for one or two examples, but universally.

The core machinery that homological algebra requires is **exactness**: a sequence A → B → C is exact at B if the image of the first map equals the kernel of the second. Exactness captures "no information is lost or invented." In an abelian category, exactness is well-defined because kernels and images exist as objects (not just sets), and the condition that every mono is a kernel ensures that "image = kernel" is a categorical statement, not just a set-theoretic one. **Short exact sequences** 0 → A → B → C → 0 generalize the relationship between a subobject, an object, and its quotient, and they appear everywhere: the long exact sequence in homology, the snake lemma output, extension problems. All of this requires only the abelian category axioms — it applies simultaneously to modules, sheaves of abelian groups, representations of a quiver, and coherent sheaves on a scheme.

**Diagram-chasing** is the technique of chasing elements around commutative diagrams to prove exactness results. In the category of abelian groups or R-modules, this is literal: you pick an element in one group and track it through maps to reach a contradiction or a desired element elsewhere. The remarkable fact is that diagram-chasing proofs in any abelian category can be reduced to the same argument — by the **Freyd-Mitchell embedding theorem**, every small abelian category embeds fully and exactly into a module category. This means: whenever you want to prove a result about an abelian category (the **five lemma**, the **snake lemma**, the **horseshoe lemma**), you may assume without loss of generality that objects have elements. Write the element-chasing proof in R-Mod; it is valid in every abelian category.

**Chain complexes** in an abelian category A are sequences ⋯ → Aₙ₊₁ →^{dₙ₊₁} Aₙ →^{dₙ} Aₙ₋₁ → ⋯ with dₙ ∘ dₙ₊₁ = 0 for all n. The **homology** at position n is Hₙ = ker(dₙ)/im(dₙ₊₁), which is an object of A. In an abelian category this quotient is well-defined (coequalized images and kernels coexist as required). A **morphism of chain complexes** is a collection of morphisms fₙ: Aₙ → Bₙ commuting with differentials; it induces morphisms Hₙ(A) → Hₙ(B) on homology. This is exactly the functorial behavior from your homology prerequisite, now seen to hold in any abelian category, for any chain complexes — not just topological ones.

**Derived functors** are the deepest payoff. Left-exact functors (like Hom(−, N) or the global sections functor Γ on sheaves) fail to preserve short exact sequences exactly: they preserve the left portion but truncate at the right. The **right derived functors** Rⁱ F measure the failure: they detect "hidden" information lost by the inexact portion. To compute Rⁱ F(A), resolve A by an injective resolution 0 → A → I⁰ → I¹ → ⋯, apply F termwise, and take homology. The result is independent of the choice of resolution — a consequence of the comparison theorem for resolutions, which in turn requires that the ambient category be abelian with enough injectives. The canonical examples Ext^i_R(M, N) = Rⁱ Hom_R(M, −)(N) and Tor^R_i(M, N) = L_i(M ⊗_R −)(N) are specific instances; the language of abelian categories reveals them as two faces of the same general construction.
