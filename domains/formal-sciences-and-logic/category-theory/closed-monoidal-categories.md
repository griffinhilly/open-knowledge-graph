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
stage: advanced
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

## Explainer

You know that a monoidal category equips objects with a tensor product ⊗ and a unit object I, satisfying associativity and unit laws up to coherent isomorphism. The monoidal structure lets you "multiply" objects together. A **closed monoidal category** adds the ability to "divide" — or more precisely, to form function objects. For every pair of objects B and C, the **internal hom** [B, C] is an object of the category that represents morphisms from B to C, living *inside* the category rather than just as an external set.

The definition is an adjunction: the functor (−) ⊗ B (which tensors any object with B on the right) has a right adjoint [B, −]. In symbols: Hom(A ⊗ B, C) ≅ Hom(A, [B, C]), naturally in A and C. This is the categorical abstraction of **currying** — a fact you may recognize from functional programming. A function of two arguments f: A × B → C corresponds exactly to a function g: A → (B → C), where g(a) is the function that takes b and returns f(a, b). Set with the cartesian product is the canonical example: [B, C] is the set of all functions B → C, and the adjunction is the familiar bijection between functions of two variables and functions returning functions.

The internal hom [B, C] is more than just a notational convenience — it is an *object* of the category with its own morphisms, structure, and properties. In **Vect_k**, the internal hom [V, W] = Hom_k(V, W) is a vector space, and morphisms in [V, W] are linear maps. In a category of types in a programming language, [B, C] is the function type B → C, and the currying adjunction is the semantic content of lambda abstraction. The evaluation morphism **ev: [B, C] ⊗ B → C** (the counit of the adjunction) is function application; the coevaluation **coev: A → [B, A ⊗ B]** (the unit) is currying.

Closed monoidal structure is what makes a category suitable for an **internal language**: you can interpret type-theoretic constructs — function types, substitution, beta-reduction — directly as morphisms in the category. This is the foundation of the Curry-Howard-Lambek correspondence linking intuitionistic logic, typed lambda calculus, and cartesian closed categories (the special case where ⊗ is the cartesian product). In the non-cartesian symmetric monoidal closed case, the internal language becomes **linear type theory**, where resources are used exactly once — a direct model for quantum mechanics, where quantum states cannot be duplicated (no-cloning theorem), and for resource-sensitive computation in programming languages like Rust.
