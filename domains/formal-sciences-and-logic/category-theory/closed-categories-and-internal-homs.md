---
id: closed-categories-and-internal-homs
title: Closed Categories and Internal Hom-objects
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: adjoint-functors
  type: hard
- id: cartesian-closed-categories
  type: soft
builds-toward:
- enriched-categories
tags:
- closed-categories
- exponential-objects
- internal-hom
- curry-howard
stage: abstract-reasoning
status: draft
---

# Closed Categories and Internal Hom-objects

## Core Idea
A closed monoidal category is one where the monoidal structure admits an internal hom-object [A, B] such that morphisms A ⊗ C → B correspond bijectively to morphisms C → [A, B], generalizing the adjoint relationship between product and function spaces. Closed categories provide an internalization of the hom-functor and appear in logic through the Curry-Howard correspondence, in topology as function spaces, and throughout higher algebra.

## How It's Best Learned
Study closed structures in the category of vector spaces with tensor product (where [A, B] is Hom(A, B)), in the category of sets with product, and in cartesian closed categories. Verify the universal properties and understand currying as an isomorphism. Explore connections to logic and type theory.

## Common Misconceptions
Not every monoidal category is closed; existence of internal homs requires additional structure or axioms. The exponential [A, B] must behave naturally with respect to the monoidal structure in subtle ways.

## Explainer

From your study of monoidal categories, you know that ⊗ provides a way to "combine" objects — tensor product for vector spaces, Cartesian product for sets, smash product for pointed spaces. From adjoint functors, you know that natural constructions often come in adjoint pairs: F is left adjoint to G when morphisms F(A) → B correspond naturally to morphisms A → G(B). A **closed monoidal category** is one where the functor (−) ⊗ A has a right adjoint for each A. That right adjoint, written [A, B] or A ⊸ B, is the **internal hom-object**.

The defining property is the **tensor-hom adjunction**: morphisms A ⊗ C → B correspond bijectively and naturally to morphisms C → [A, B]. In the category of sets, [A, B] is the set of all functions A → B. The adjunction then says: a function from A × C to B is the same data as a function from C to the set of functions A → B. This is **currying** — the fundamental operation of functional programming, now presented as a categorical universal property. In the category of vector spaces over a field k, [A, B] = Hom_k(A, B) as a k-vector space, and the adjunction says bilinear maps A ⊗ C → B correspond naturally to linear maps C → Hom(A, B). The same pattern recurs throughout algebra and topology.

Why internalize the hom? External hom-sets Hom(A, B) live in **Set** — they are sets of morphisms but not objects of the category. This limits what you can do with them categorically. **Internal hom-objects** [A, B] live inside the category itself, making function spaces first-class objects that can be composed, tensored, and mapped. In **cartesian closed categories** (where ⊗ is the Cartesian product), this is the categorical foundation of **lambda calculus** via the **Curry-Howard correspondence**: types are objects, programs are morphisms, and function types A → B are internal homs [A, B]. Provability in propositional logic corresponds to inhabitation of types, and logical implication A ⊃ B corresponds to the internal hom.

The subtlety is that closure is not automatic. Requiring that (−) ⊗ A has a right adjoint for every A is a genuine constraint — it fails in many monoidal categories. When it does hold, the category supports an internal language rich enough to reason about morphisms as objects. This closed structure is also the foundation of **enriched category theory**: a category enriched in a closed monoidal category 𝒱 replaces hom-sets with hom-objects drawn from 𝒱, enabling categories of modules, sheaves, and spectra to be understood as enriched categories in which the hom-object encodes far more structure than a bare set of morphisms.
