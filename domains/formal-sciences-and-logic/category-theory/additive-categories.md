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
stage: expert
status: draft
---

# Additive Categories and Direct Sums

## Core Idea
An additive category is an Ab-enriched category where Hom-sets are abelian groups and composition is bilinear. Finite products and coproducts coincide (both are direct sums). Additive categories provide the minimal algebraic structure to define exact sequences and chain complexes, forming the foundation of homological algebra.

## Questions

```yaml
- question: "In the category of sets, the product A×B (Cartesian product) and the coproduct A⊔B (disjoint union) are distinct objects with different universal properties. What additional structure in an additive category forces these two constructions to coincide as the direct sum A⊕B?"
  type: multiple-choice
  options:
    - "The existence of a terminal object, which forces all limits to equal colimits."
    - "The requirement that every morphism is invertible, making products and coproducts trivially isomorphic."
    - "Ab-enrichment: Hom-sets carry abelian group structure and composition is bilinear, enabling the identity i_A∘π_A + i_B∘π_B = id_{A⊕B}."
    - "The simultaneous existence of an initial object and a terminal object, whose coincidence defines the direct sum."
  answer: 2
  explanation: "The collapse requires Ab-enrichment. When each Hom(A,B) is an abelian group and composition is bilinear, you can write the identity on A⊕B as a sum i_A∘π_A + i_B∘π_B = id. This identity ties together the injection maps (from the coproduct structure) and the projection maps (from the product structure) in a single object. Without the ability to add morphisms, this identity cannot even be stated, and products and coproducts remain separate constructions."

- question: "Which of the following categories is NOT additive?"
  type: multiple-choice
  options:
    - "The category Ab of abelian groups"
    - "The category of vector spaces over a field k"
    - "The category of R-modules for a commutative ring R"
    - "The category Grp of all groups (including non-abelian groups)"
  answer: 3
  explanation: "In Grp, given two homomorphisms f, g: A → B, the pointwise product (f·g)(a) = f(a)·g(a) is generally not a homomorphism when B is non-abelian: (f·g)(ab) = f(a)f(b)g(a)g(b) equals f(a)g(a)f(b)g(b) = (f·g)(a)(f·g)(b) only when f(b) and g(a) commute. So Hom(A,B) lacks a natural abelian group structure in Grp, and the category fails to be Ab-enriched. Ab, Vect_k, and R-Mod are all standard examples of additive categories."

- question: "In an additive category, the object A⊕B simultaneously satisfies the universal property of the product A×B (equipped with projection maps) and the universal property of the coproduct A⊔B (equipped with injection maps)."
  type: true-false
  answer: true
  explanation: "This is exactly what 'direct sum' means in an additive category — the same object serves both roles. The four maps satisfy π_A∘i_A = id_A, π_B∘i_B = id_B, π_A∘i_B = 0, π_B∘i_A = 0, and i_A∘π_A + i_B∘π_B = id_{A⊕B}. The last identity — which requires adding morphisms — is what ties the product and coproduct structures together into a single object."

- question: "Any category with a zero object automatically has the structure needed to form direct sums, since zero morphisms supply the additive identity required for Ab-enrichment of Hom-sets."
  type: true-false
  answer: false
  explanation: "A zero object provides a distinguished zero morphism between any two objects — the additive identity — but a single element is not a full abelian group structure. Ab-enrichment requires every pair of morphisms to have a well-defined sum that is itself a morphism, plus associativity, commutativity, and inverses. The category of pointed sets has a zero object but is not additive. Zero objects are a necessary but far from sufficient condition for additivity."

- question: "Explain why the category Grp of all groups fails to be additive, even though it has a zero object (the trivial group) and zero morphisms between every pair of objects."
  type: short-answer
  answer: "For Grp to be additive, Hom(A,B) must be an abelian group for every pair A, B — meaning any two homomorphisms f, g: A → B must have a sum f+g that is also a homomorphism. The natural candidate is pointwise multiplication: (f+g)(a) = f(a)·g(a). But for this to be a homomorphism, we need (f+g)(ab) = (f+g)(a)·(f+g)(b), which expands to f(a)f(b)g(a)g(b) = f(a)g(a)f(b)g(b). This holds only when f(b) and g(a) commute for all a, b — precisely when B is abelian. For a non-abelian target B, the pointwise product of two homomorphisms is generally not a homomorphism, so Hom(A,B) has no natural abelian group structure and Grp is not Ab-enriched."
  explanation: "The key insight is that Ab-enrichment is a condition on Hom-sets, not just on objects. The full subcategory Ab ⊂ Grp of abelian groups IS additive for exactly this reason — restricting to abelian targets makes pointwise addition of homomorphisms well-defined."
```

## Explainer

From your work on products and coproducts, you know these are dual constructions: a product A × B comes with projections to each factor, while a coproduct A ⊔ B comes with injections from each factor. In a general category these can be very different objects — the product of two sets is their Cartesian product, while the coproduct is their disjoint union. An **additive category** is one where this distinction collapses: every finite product is also a coproduct, and the shared object is called the **direct sum** A ⊕ B. The key extra ingredient that forces this collapse is the enrichment: every Hom-set carries the structure of an **abelian group**, and composition distributes over this group structure (bilinearity).

The abelian group structure on Hom(A, B) means you can add morphisms: given f, g: A → B, you have a sum f + g: A → B, and a zero morphism 0: A → B. This is not available in a general category — in the category of sets, there is no natural way to add two functions. The requirement that composition is bilinear means h ∘ (f + g) = h ∘ f + h ∘ g and (f + g) ∘ k = f ∘ k + g ∘ k. This bilinearity condition, combined with the existence of a **zero object** (the prerequisite you studied), is exactly what makes products and coproducts coincide. You can construct the direct sum A ⊕ B explicitly with both the injection maps (i_A: A → A ⊕ B, i_B: B → A ⊕ B) and the projection maps (π_A: A ⊕ B → A, π_B: A ⊕ B → B) satisfying π_A ∘ i_A = id_A, π_B ∘ i_B = id_B, π_A ∘ i_B = 0, π_B ∘ i_A = 0, and i_A ∘ π_A + i_B ∘ π_B = id_{A⊕B}.

The canonical examples are the category of abelian groups **Ab**, the category of modules over a ring, and the category of vector spaces over a field. In each case, Hom(A, B) is the group of homomorphisms (or linear maps), which forms an abelian group under pointwise addition. The zero morphism sends everything to the zero element of B. The direct sum A ⊕ B is the usual direct sum of abelian groups or modules, with coordinate-wise operations. Categories of sets, topological spaces, or groups (without abelian assumption) are not additive: in the category of groups, for instance, the pointwise sum of two homomorphisms is generally not a homomorphism.

Additive categories are the setting where homological algebra begins. To define **exact sequences** — the sequences 0 → A → B → C → 0 where the image of each map equals the kernel of the next — you need to talk about kernels and cokernels as morphisms, not just as sets. This requires the additional structure of an **abelian category** (which adds the requirement that every monomorphism is a kernel and every epimorphism is a cokernel), but additive categories are the necessary first step: without the ability to add morphisms and form direct sums, neither chain complexes nor the long exact sequences of homology would be well-defined.
