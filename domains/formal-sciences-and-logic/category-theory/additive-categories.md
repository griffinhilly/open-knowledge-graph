---
id: additive-categories
title: Additive Categories and Direct Sums
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monomorphisms-epimorphisms
  type: hard
- id: zero-objects-and-morphisms
  type: hard
- id: products-and-coproducts
  type: soft
builds-toward:
- exact-sequences
- abelian-structure-properties
- projective-objects
- injective-objects
tags:
- algebraic-structure
- limits
- homological-algebra
stage: advanced
status: draft
---

# Additive Categories and Direct Sums

## Core Idea
An additive category is an Ab-enriched category where Hom-sets are abelian groups and composition is bilinear. Finite products and coproducts coincide (both are direct sums). Additive categories provide the minimal algebraic structure to define exact sequences and chain complexes, forming the foundation of homological algebra.

## Explainer

From your work on products and coproducts, you know these are dual constructions: a product A × B comes with projections to each factor, while a coproduct A ⊔ B comes with injections from each factor. In a general category these can be very different objects — the product of two sets is their Cartesian product, while the coproduct is their disjoint union. An **additive category** is one where this distinction collapses: every finite product is also a coproduct, and the shared object is called the **direct sum** A ⊕ B. The key extra ingredient that forces this collapse is the enrichment: every Hom-set carries the structure of an **abelian group**, and composition distributes over this group structure (bilinearity).

The abelian group structure on Hom(A, B) means you can add morphisms: given f, g: A → B, you have a sum f + g: A → B, and a zero morphism 0: A → B. This is not available in a general category — in the category of sets, there is no natural way to add two functions. The requirement that composition is bilinear means h ∘ (f + g) = h ∘ f + h ∘ g and (f + g) ∘ k = f ∘ k + g ∘ k. This bilinearity condition, combined with the existence of a **zero object** (the prerequisite you studied), is exactly what makes products and coproducts coincide. You can construct the direct sum A ⊕ B explicitly with both the injection maps (i_A: A → A ⊕ B, i_B: B → A ⊕ B) and the projection maps (π_A: A ⊕ B → A, π_B: A ⊕ B → B) satisfying π_A ∘ i_A = id_A, π_B ∘ i_B = id_B, π_A ∘ i_B = 0, π_B ∘ i_A = 0, and i_A ∘ π_A + i_B ∘ π_B = id_{A⊕B}.

The canonical examples are the category of abelian groups **Ab**, the category of modules over a ring, and the category of vector spaces over a field. In each case, Hom(A, B) is the group of homomorphisms (or linear maps), which forms an abelian group under pointwise addition. The zero morphism sends everything to the zero element of B. The direct sum A ⊕ B is the usual direct sum of abelian groups or modules, with coordinate-wise operations. Categories of sets, topological spaces, or groups (without abelian assumption) are not additive: in the category of groups, for instance, the pointwise sum of two homomorphisms is generally not a homomorphism.

Additive categories are the setting where homological algebra begins. To define **exact sequences** — the sequences 0 → A → B → C → 0 where the image of each map equals the kernel of the next — you need to talk about kernels and cokernels as morphisms, not just as sets. This requires the additional structure of an **abelian category** (which adds the requirement that every monomorphism is a kernel and every epimorphism is a cokernel), but additive categories are the necessary first step: without the ability to add morphisms and form direct sums, neither chain complexes nor the long exact sequences of homology would be well-defined.
