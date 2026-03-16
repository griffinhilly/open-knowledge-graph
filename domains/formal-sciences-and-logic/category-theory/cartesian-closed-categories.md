---
id: cartesian-closed-categories
title: Cartesian Closed Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: products-and-coproducts
  type: hard
- id: initial-and-terminal-objects
  type: hard
builds-toward:
- topos-theory-intro
tags:
- cartesian
- closed
- exponential
- internal-hom
- lambda-calculus
stage: advanced
status: draft
---

# Cartesian Closed Categories

## Core Idea
A cartesian closed category has finite products with a terminal object and an exponential object B^A for each pair of objects, satisfying the adjunction Hom(A × B, C) ≅ Hom(A, C^B). Cartesian closed categories are the categorical semantics for typed lambda calculus and higher-order logic. The exponential object represents the set of all morphisms from A to B, generalizing function spaces.

## How It's Best Learned
Study Set (exponential = function space), Top (topological exponential objects and the compact-open topology), and Grp (where exponentials do not always exist). Verify the adjunction explicitly in these examples and practice translating lambda calculus into cartesian closed category language.

## Common Misconceptions
Not every category with finite products is cartesian closed; the exponential object must exist and satisfy the adjunction. In Top, the naive exponential (all continuous functions with pointwise operations) may fail to be in the category unless carefully chosen. Cartesian closed structure depends on the underlying monoidal structure.

## Explainer

You already know that a category with finite products has a monoidal structure where the tensor product is the categorical product A × B and the unit is the terminal object 1. A **cartesian closed category (CCC)** adds one more ingredient: for every pair of objects A and B, there is an **exponential object** B^A (also written [A, B] or A ⇒ B) that internalizes the notion of "the object of morphisms from A to B." In Set, this exponential is literally the set of all functions from A to B. The cartesian closed condition is the requirement that this exponential behaves correctly with respect to products.

The behavioral requirement is an **adjunction**: for every three objects A, B, C, there is a natural isomorphism Hom(A × B, C) ≅ Hom(A, C^B). In plain language: a morphism from the product A × B to C corresponds exactly to a morphism from A to the function-space C^B. This is **currying** — the categorical version of the familiar programming operation. A function of two arguments f(a, b) = c can always be converted to a function that takes one argument and returns a function: curry(f)(a) = (b ↦ c). The adjunction says this conversion is always possible, natural, and invertible in a CCC. The counit of the adjunction is the **evaluation morphism** ev: C^B × B → C, the categorical analog of applying a function to an argument.

In Set, the isomorphism Hom(A × B, C) ≅ Hom(A, C^B) is just the set-theoretic fact that a function on a product bijects with a curried function. But the categorical formulation captures this pattern in any CCC. The category **Grp** of groups is not cartesian closed: there is no group that plays the role of the exponential Hom(A, B) for arbitrary groups, because the set of group homomorphisms from A to B does not carry a natural group structure in general. **Top** (topological spaces and continuous maps) is also not cartesian closed with the naive exponential, but the full subcategory of compactly generated weakly Hausdorff spaces is — and this is why that subcategory is the standard setting for algebraic topology and homotopy theory.

The deep significance of CCCs is their connection to **typed lambda calculus**. The types of a simply-typed lambda calculus correspond to objects of a CCC: base types are objects, the function type A → B is the exponential B^A, and the product type A × B is the categorical product. Lambda abstraction corresponds to the currying bijection; function application corresponds to the evaluation morphism. This correspondence, known as the **Curry-Howard-Lambek correspondence**, is a three-way equivalence between typed lambda calculi, intuitionistic propositional logic, and cartesian closed categories. It means that reasoning in a CCC is exactly the same as computing in a functional programming language and as proving theorems in constructive logic — three apparently different activities that are secretly the same.

When checking whether a category is cartesian closed, the procedure is: verify it has a terminal object (1), verify it has all binary products (A × B), and then for each pair A, B, check whether the functor Hom(- × A, B) is representable — i.e., whether there exists an object B^A with a natural isomorphism Hom(C × A, B) ≅ Hom(C, B^A) for all C. If this representability fails for even one pair, the category is not cartesian closed.
