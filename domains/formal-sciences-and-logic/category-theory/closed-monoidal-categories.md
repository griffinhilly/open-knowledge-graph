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
