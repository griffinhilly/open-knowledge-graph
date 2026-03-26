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
stage: expert
status: validated
---

# Closed Categories and Internal Hom-objects

## Core Idea
A closed monoidal category is one where the monoidal structure admits an internal hom-object [A, B] such that morphisms A ⊗ C → B correspond bijectively to morphisms C → [A, B], generalizing the adjoint relationship between product and function spaces. Closed categories provide an internalization of the hom-functor and appear in logic through the Curry-Howard correspondence, in topology as function spaces, and throughout higher algebra.

## How It's Best Learned
Study closed structures in the category of vector spaces with tensor product (where [A, B] is Hom(A, B)), in the category of sets with product, and in cartesian closed categories. Verify the universal properties and understand currying as an isomorphism. Explore connections to logic and type theory.

## Common Misconceptions
Not every monoidal category is closed; existence of internal homs requires additional structure or axioms. The exponential [A, B] must behave naturally with respect to the monoidal structure in subtle ways.

## Questions

```yaml
- question: "In a closed monoidal category, the tensor-hom adjunction states that for all objects A, B, C there is a natural bijection between morphisms. Which pair of hom-sets are in bijection?"
  type: multiple-choice
  options:
    - "Hom(A, B ⊗ C) ≅ Hom(A ⊗ B, C)"
    - "Hom(A ⊗ C, B) ≅ Hom(C, [A, B])"
    - "Hom(A, [B, C]) ≅ Hom(A ⊗ B, A ⊗ C)"
    - "Hom([A, B], C) ≅ Hom(A, B ⊗ C)"
  answer: 1
  explanation: "The defining adjunction of a closed monoidal category is Hom(A ⊗ C, B) ≅ Hom(C, [A, B]), natural in all variables. This is currying: a morphism from A ⊗ C to B (a 'two-argument function') corresponds to a morphism from C into the internal hom [A, B] (a 'curried one-argument function returning a function')."

- question: "A student argues: 'In the category of sets, the internal hom [A, B] is just the set B^A of functions from A to B, so it is the same as the external hom-set Hom(A, B). Therefore internalizing the hom-functor adds nothing new in Set.' What is wrong with this argument?"
  type: multiple-choice
  options:
    - "The argument is correct — internal and external homs coincide in Set and the distinction only matters in non-concrete categories"
    - "The sets B^A and Hom(A, B) are different objects; internal homs always have additional algebraic structure not present in hom-sets"
    - "While they happen to coincide in Set, the value of internal homs is that they live inside the category as objects that can be further composed and mapped — unlike external hom-sets which land in Set regardless of the ambient category"
    - "The argument fails because Hom(A, B) in Set is not a set but a proper class"
  answer: 2
  explanation: "In Set, [A, B] ≅ Hom(A, B) as sets — they coincidentally agree. But the point is categorical: external hom-sets always land in Set, making morphisms second-class citizens. Internal homs make function spaces objects within the original category, available for further categorical operations: you can tensor them, map into them, and use them to define enriched structures. This distinction becomes critical in categories like vector spaces or chain complexes where hom-objects carry more structure than mere sets."

- question: "In any cartesian closed category, the categorical operation of currying is an instance of the tensor-hom adjunction where the monoidal product is the Cartesian product."
  type: true-false
  answer: true
  explanation: "A cartesian closed category is a closed monoidal category where ⊗ = ×. The tensor-hom adjunction then reads: Hom(A × C, B) ≅ Hom(C, [A, B]), which is exactly currying — a function of two arguments is the same as a function returning a function. This is the categorical foundation of lambda calculus and functional programming type theory via Curry-Howard."

- question: "Nearly every monoidal category is automatically closed, because the monoidal product ⊗ generally has a right adjoint given by the opposite monoidal structure."
  type: true-false
  answer: false
  explanation: "Closure is an additional property, not automatic. The monoidal structure gives ⊗ as a functor, but requiring (−) ⊗ A to have a right adjoint [A, −] for each A is a genuine constraint that fails in many monoidal categories. For example, the category of topological spaces with Cartesian product is not cartesian closed (the required function spaces may not exist with the right topology). Closed structure must be verified or assumed separately."

- question: "Why does it matter that internal hom-objects [A, B] live inside the category, rather than always living in Set as external hom-sets do? Give a concrete consequence of this internalization."
  type: short-answer
  answer: "Internal homs are first-class objects that can be tensored, mapped into, and used to define enriched hom-objects — enabling enriched category theory and type-theoretic reasoning within the category itself"
  explanation: "External hom-sets Hom(A, B) always belong to Set — they are sets of morphisms, not objects of the category. This means you cannot compose them with morphisms, tensor them with objects, or treat them as inputs to further categorical constructions. Internal homs [A, B] are objects in the category itself: you can form [[A, B], C], tensor [A, B] ⊗ C, and define categories enriched in 𝒱 by replacing hom-sets with hom-objects drawn from 𝒱. This underpins enriched category theory, module categories, and the Curry-Howard correspondence."
```

## Explainer

From your study of monoidal categories, you know that ⊗ provides a way to "combine" objects — tensor product for vector spaces, Cartesian product for sets, smash product for pointed spaces. From adjoint functors, you know that natural constructions often come in adjoint pairs: F is left adjoint to G when morphisms F(A) → B correspond naturally to morphisms A → G(B). A **closed monoidal category** is one where the functor (−) ⊗ A has a right adjoint for each A. That right adjoint, written [A, B] or A ⊸ B, is the **internal hom-object**.

The defining property is the **tensor-hom adjunction**: morphisms A ⊗ C → B correspond bijectively and naturally to morphisms C → [A, B]. In the category of sets, [A, B] is the set of all functions A → B. The adjunction then says: a function from A × C to B is the same data as a function from C to the set of functions A → B. This is **currying** — the fundamental operation of functional programming, now presented as a categorical universal property. In the category of vector spaces over a field k, [A, B] = Hom_k(A, B) as a k-vector space, and the adjunction says bilinear maps A ⊗ C → B correspond naturally to linear maps C → Hom(A, B). The same pattern recurs throughout algebra and topology.

Why internalize the hom? External hom-sets Hom(A, B) live in **Set** — they are sets of morphisms but not objects of the category. This limits what you can do with them categorically. **Internal hom-objects** [A, B] live inside the category itself, making function spaces first-class objects that can be composed, tensored, and mapped. In **cartesian closed categories** (where ⊗ is the Cartesian product), this is the categorical foundation of **lambda calculus** via the **Curry-Howard correspondence**: types are objects, programs are morphisms, and function types A → B are internal homs [A, B]. Provability in propositional logic corresponds to inhabitation of types, and logical implication A ⊃ B corresponds to the internal hom.

The subtlety is that closure is not automatic. Requiring that (−) ⊗ A has a right adjoint for every A is a genuine constraint — it fails in many monoidal categories. When it does hold, the category supports an internal language rich enough to reason about morphisms as objects. This closed structure is also the foundation of **enriched category theory**: a category enriched in a closed monoidal category 𝒱 replaces hom-sets with hom-objects drawn from 𝒱, enabling categories of modules, sheaves, and spectra to be understood as enriched categories in which the hom-object encodes far more structure than a bare set of morphisms.
