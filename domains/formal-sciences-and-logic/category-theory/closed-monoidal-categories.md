---
id: closed-monoidal-categories
title: Closed Monoidal Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: functor-categories
  type: soft
- id: adjoint-functors
  type: soft
builds-toward:
- cartesian-closed-categories
tags:
- closed monoidal category
- internal hom
- currying
- exponential
- symmetric monoidal closed
stage: expert
status: draft
---
# Closed Monoidal Categories

## Core Idea
A closed monoidal category is a monoidal category (C, ⊗, I) in which for every object B, the functor (−) ⊗ B has a right adjoint [B, −], called the internal hom. The adjunction Hom(A ⊗ B, C) ≅ Hom(A, [B, C]) is the categorical generalization of currying: a morphism from A ⊗ B to C corresponds naturally to a morphism from A to the function object [B, C]. In the symmetric case, (Set, ×) is closed with [B, C] = the set of functions B → C, and (Vect_k, ⊗_k) is closed with [V, W] = Hom_k(V, W). Closed monoidal structure provides the foundation for internal languages and type-theoretic interpretations of categories.

## How It's Best Learned
Verify the currying adjunction in Set: a function f: A × B → C corresponds to a function g: A → C^B where g(a)(b) = f(a,b). Then check the same pattern in Vect: a bilinear map V ⊗ W → U corresponds to a linear map V → Hom(W, U). Identify the unit and counit of the adjunction (evaluation and coevaluation maps).

## Common Misconceptions
- Not every monoidal category is closed; the existence of internal hom is an additional condition requiring a right adjoint to tensoring.
- The internal hom [B, C] is an object of C, not a set; it internalizes the notion of morphism space within the category itself.
- Closed monoidal need not be symmetric; non-symmetric closed monoidal categories exist (e.g., categories of bimodules), though the symmetric case is most common.

## Questions

```yaml
- question: "In the category Set with the cartesian product ×, the internal hom [B, C] is defined by the natural bijection Hom(A × B, C) ≅ Hom(A, [B, C]). What object plays the role of [B, C] in Set?"
  type: multiple-choice
  options:
    - "The set of all subsets of B × C"
    - "The set of all functions from B to C"
    - "The cartesian product B × C itself"
    - "The set of all functions from C to B"
  answer: 1
  explanation: "In Set, the internal hom [B, C] is the set of all functions B → C, often written C^B. The adjunction Hom(A × B, C) ≅ Hom(A, C^B) is precisely currying: a function f(a, b) of two arguments is in bijection with a function g(a) that returns a function of b. This is the canonical example grounding the abstract definition."

- question: "In Vect_k with the tensor product ⊗_k, a student describes the internal hom [V, W] as 'just the set of linear maps from V to W, which exists outside the category.' What is wrong with this description?"
  type: multiple-choice
  options:
    - "The internal hom in Vect_k is not the set of linear maps — it is the tensor product V ⊗ W"
    - "The internal hom [V, W] = Hom_k(V, W) is itself a k-vector space and an object inside Vect_k, not merely an external set"
    - "The description is correct; internal homs in concrete categories are always external sets"
    - "Vect_k is not a closed monoidal category, so no internal hom exists"
  answer: 1
  explanation: "This is the central distinction of closed monoidal structure. While morphisms from V to W do form a set, the internal hom [V, W] = Hom_k(V, W) is additionally a k-vector space — it has its own linear structure, and it lives as an object inside Vect_k. Morphisms from U to [V, W] are linear maps U → Hom_k(V, W), which correspond via the adjunction to bilinear maps from U ⊗ V to W. The internal hom internalizes the function space within the category, making it available for further categorical operations."

- question: "In a closed monoidal category, the internal hom [B, C] is characterized up to isomorphism by a natural bijection between morphism sets — specifically, the currying adjunction Hom(A ⊗ B, C) ≅ Hom(A, [B, C])."
  type: true-false
  answer: true
  explanation: "The internal hom is defined as the right adjoint to (−) ⊗ B, and right adjoints are unique up to natural isomorphism. The adjunction provides a natural bijection in both A and C, which completely determines [B, C] up to isomorphism. The evaluation morphism ev: [B, C] ⊗ B → C (the counit) and coevaluation coev: A → [B, A ⊗ B] (the unit) are the structural maps witnessing this adjunction."

- question: "Every monoidal category is automatically closed, because morphisms between any two objects always form a set, and this set can serve as the internal hom."
  type: true-false
  answer: false
  explanation: "Closedness is an additional structure, not a consequence of being monoidal. The internal hom requires the functor (−) ⊗ B to have a right adjoint [B, −] for each object B — this adjoint may not exist. Many important monoidal categories lack internal homs. For example, the category of finite sets with cartesian product has a well-defined internal hom (function sets are finite), but the category of finite-dimensional vector spaces with a tensor product ⊗_k satisfies closedness only because Hom(V, W) is again finite-dimensional. In general, the existence of a right adjoint must be verified, not assumed."

- question: "Explain the significance of the internal hom [B, C] being an object *inside* the category, rather than just an external set of morphisms. What does this internalization make possible?"
  type: short-answer
  answer: "When [B, C] is an object of the category, it can appear as a source or target of morphisms within the category itself, enabling constructions like composition (a morphism [B, C] ⊗ [A, B] → [A, C]), currying (a morphism f: A ⊗ B → C corresponds to a morphism f̃: A → [B, C] inside the category), and higher-order functions. This makes the category suitable for interpreting type theories with function types: the internal hom models the function type B → C, and the currying adjunction models lambda abstraction. In the symmetric monoidal closed case, the internal language is linear type theory, directly modeling resource-sensitive systems where values are used exactly once — as in quantum mechanics (no-cloning) or Rust's ownership types."
  explanation: "The key contrast is between Hom_Set(B, C), which is external bookkeeping about the category, and [B, C], which is an entity inside the category that participates in its algebra. Internalization is what enables the Curry-Howard-Lambek correspondence and makes closed monoidal categories the semantic setting for functional programming languages and linear logic."
```

## Explainer

You know that a monoidal category equips objects with a tensor product ⊗ and a unit object I, satisfying associativity and unit laws up to coherent isomorphism. The monoidal structure lets you "multiply" objects together. A **closed monoidal category** adds the ability to "divide" — or more precisely, to form function objects. For every pair of objects B and C, the **internal hom** [B, C] is an object of the category that represents morphisms from B to C, living *inside* the category rather than just as an external set.

The definition is an adjunction: the functor (−) ⊗ B (which tensors any object with B on the right) has a right adjoint [B, −]. In symbols: Hom(A ⊗ B, C) ≅ Hom(A, [B, C]), naturally in A and C. This is the categorical abstraction of **currying** — a fact you may recognize from functional programming. A function of two arguments f: A × B → C corresponds exactly to a function g: A → (B → C), where g(a) is the function that takes b and returns f(a, b). Set with the cartesian product is the canonical example: [B, C] is the set of all functions B → C, and the adjunction is the familiar bijection between functions of two variables and functions returning functions.

The internal hom [B, C] is more than just a notational convenience — it is an *object* of the category with its own morphisms, structure, and properties. In **Vect_k**, the internal hom [V, W] = Hom_k(V, W) is a vector space, and morphisms in [V, W] are linear maps. In a category of types in a programming language, [B, C] is the function type B → C, and the currying adjunction is the semantic content of lambda abstraction. The evaluation morphism **ev: [B, C] ⊗ B → C** (the counit of the adjunction) is function application; the coevaluation **coev: A → [B, A ⊗ B]** (the unit) is currying.

Closed monoidal structure is what makes a category suitable for an **internal language**: you can interpret type-theoretic constructs — function types, substitution, beta-reduction — directly as morphisms in the category. This is the foundation of the Curry-Howard-Lambek correspondence linking intuitionistic logic, typed lambda calculus, and cartesian closed categories (the special case where ⊗ is the cartesian product). In the non-cartesian symmetric monoidal closed case, the internal language becomes **linear type theory**, where resources are used exactly once — a direct model for quantum mechanics, where quantum states cannot be duplicated (no-cloning theorem), and for resource-sensitive computation in programming languages like Rust.
