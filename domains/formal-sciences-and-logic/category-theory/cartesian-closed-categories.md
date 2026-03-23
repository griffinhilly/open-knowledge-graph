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
stage: expert
status: draft
---

# Cartesian Closed Categories

## Core Idea
A cartesian closed category has finite products with a terminal object and an exponential object B^A for each pair of objects, satisfying the adjunction Hom(A × B, C) ≅ Hom(A, C^B). Cartesian closed categories are the categorical semantics for typed lambda calculus and higher-order logic. The exponential object represents the set of all morphisms from A to B, generalizing function spaces.

## How It's Best Learned
Study Set (exponential = function space), Top (topological exponential objects and the compact-open topology), and Grp (where exponentials do not always exist). Verify the adjunction explicitly in these examples and practice translating lambda calculus into cartesian closed category language.

## Common Misconceptions
Not every category with finite products is cartesian closed; the exponential object must exist and satisfy the adjunction. In Top, the naive exponential (all continuous functions with pointwise operations) may fail to be in the category unless carefully chosen. Cartesian closed structure depends on the underlying monoidal structure.

## Questions

```yaml
- question: "The adjunction Hom(A × B, C) ≅ Hom(A, C^B) in a cartesian closed category captures which familiar programming concept?"
  type: multiple-choice
  options:
    - "Pattern matching — decomposing a product type into its components"
    - "Currying — converting a function of two arguments into a function that takes one argument and returns a function"
    - "Polymorphism — a single function operating on multiple types"
    - "Memoization — caching function results to avoid recomputation"
  answer: 1
  explanation: "The adjunction says: a morphism from A × B to C (a function taking a pair as input) corresponds naturally and bijectively to a morphism from A to C^B (a function that takes one argument and returns a function from B to C). This is exactly currying. In Haskell, curry :: ((a,b) -> c) -> a -> b -> c; uncurry :: (a -> b -> c) -> (a,b) -> c. The CCC adjunction is the categorical version: the isomorphism is natural (respects composition), invertible (uncurrying exists), and universal (works for all A, B, C). The evaluation morphism ev: C^B × B → C is the categorical analog of function application."

- question: "The category Grp of groups and group homomorphisms is not cartesian closed. What is the core reason?"
  type: multiple-choice
  options:
    - "Groups do not have a terminal object, which is required for cartesian closure"
    - "The binary product of two groups does not exist in Grp"
    - "The set of group homomorphisms from A to B cannot be given a natural group structure, so no exponential object exists"
    - "Grp is a closed category but not a cartesian one because the tensor product is not the categorical product"
  answer: 2
  explanation: "Grp does have a terminal object (the trivial group) and binary products (direct products A × B). What it lacks is exponential objects. The exponential B^A should represent 'the object of all morphisms from A to B' — in Set this is the function set with composition. In Grp, the set of group homomorphisms Hom(A, B) does not carry a natural group structure: the pointwise product of two homomorphisms (f·g)(x) = f(x)·g(x) is only a homomorphism when B is abelian. For non-abelian B, Hom(A, B) cannot be made into a group naturally, so the exponential fails to exist. This shows that cartesian closure is a strong condition that fails even in well-behaved algebraic categories."

- question: "Every cartesian closed category must have all finite products, including a terminal object."
  type: true-false
  answer: true
  explanation: "By definition, a CCC requires: (1) a terminal object 1 (the empty product), (2) all binary products A × B (and hence all finite products by iteration), and (3) exponential objects B^A for every pair A, B satisfying the adjunction Hom(C × A, B) ≅ Hom(C, B^A). The terminal object and binary products give the 'cartesian' part; the exponentials give the 'closed' part. The terminal object plays the role of the unit for the monoidal structure, and the product is the tensor. You cannot have cartesian closed structure without the cartesian structure (products) as its foundation."

- question: "A category that has all finite products automatically also has all exponential objects, making it cartesian closed."
  type: true-false
  answer: false
  explanation: "Having finite products is necessary but not sufficient for cartesian closure. The exponential B^A must exist as a specific object satisfying the adjunction Hom(C × A, B) ≅ Hom(C, B^A) naturally in all three variables. Many categories have products but fail to be cartesian closed because the required exponential objects do not exist. Examples: Grp has products but no exponentials (for non-abelian groups). Top (all topological spaces) has products but is not cartesian closed with the pointwise topology on function spaces — you need to restrict to compactly generated spaces. Checking cartesian closure requires explicitly verifying the representability of Hom(− × A, B) as a functor."

- question: "What is the Curry-Howard-Lambek correspondence, and what three structures does it connect?"
  type: short-answer
  answer: "The Curry-Howard-Lambek correspondence is a three-way equivalence between: (1) types and terms of simply-typed lambda calculus, (2) propositions and proofs in intuitionistic propositional logic, and (3) objects and morphisms in cartesian closed categories. Under this correspondence, function types (A → B) correspond to exponential objects (B^A) and to logical implication (A ⊃ B); lambda abstraction corresponds to currying (the CCC adjunction); function application corresponds to the evaluation morphism; and products correspond to logical conjunction and the type-theoretic product."
  explanation: "The significance is that three apparently different disciplines — programming language theory, proof theory, and abstract algebra — are secretly the same subject, expressed in different notation. A program that type-checks is simultaneously a valid proof and a well-defined morphism in a CCC. This means insights transfer freely: type-theoretic constructions like dependent types correspond to more expressive categories (locally cartesian closed categories, toposes), and categorical constructions suggest new programming language features. The correspondence is the foundation of proof assistants like Coq and Agda, where writing a program and proving a theorem are literally the same activity."
```

## Explainer

You already know that a category with finite products has a monoidal structure where the tensor product is the categorical product A × B and the unit is the terminal object 1. A **cartesian closed category (CCC)** adds one more ingredient: for every pair of objects A and B, there is an **exponential object** B^A (also written [A, B] or A ⇒ B) that internalizes the notion of "the object of morphisms from A to B." In Set, this exponential is literally the set of all functions from A to B. The cartesian closed condition is the requirement that this exponential behaves correctly with respect to products.

The behavioral requirement is an **adjunction**: for every three objects A, B, C, there is a natural isomorphism Hom(A × B, C) ≅ Hom(A, C^B). In plain language: a morphism from the product A × B to C corresponds exactly to a morphism from A to the function-space C^B. This is **currying** — the categorical version of the familiar programming operation. A function of two arguments f(a, b) = c can always be converted to a function that takes one argument and returns a function: curry(f)(a) = (b ↦ c). The adjunction says this conversion is always possible, natural, and invertible in a CCC. The counit of the adjunction is the **evaluation morphism** ev: C^B × B → C, the categorical analog of applying a function to an argument.

In Set, the isomorphism Hom(A × B, C) ≅ Hom(A, C^B) is just the set-theoretic fact that a function on a product bijects with a curried function. But the categorical formulation captures this pattern in any CCC. The category **Grp** of groups is not cartesian closed: there is no group that plays the role of the exponential Hom(A, B) for arbitrary groups, because the set of group homomorphisms from A to B does not carry a natural group structure in general. **Top** (topological spaces and continuous maps) is also not cartesian closed with the naive exponential, but the full subcategory of compactly generated weakly Hausdorff spaces is — and this is why that subcategory is the standard setting for algebraic topology and homotopy theory.

The deep significance of CCCs is their connection to **typed lambda calculus**. The types of a simply-typed lambda calculus correspond to objects of a CCC: base types are objects, the function type A → B is the exponential B^A, and the product type A × B is the categorical product. Lambda abstraction corresponds to the currying bijection; function application corresponds to the evaluation morphism. This correspondence, known as the **Curry-Howard-Lambek correspondence**, is a three-way equivalence between typed lambda calculi, intuitionistic propositional logic, and cartesian closed categories. It means that reasoning in a CCC is exactly the same as computing in a functional programming language and as proving theorems in constructive logic — three apparently different activities that are secretly the same.

When checking whether a category is cartesian closed, the procedure is: verify it has a terminal object (1), verify it has all binary products (A × B), and then for each pair A, B, check whether the functor Hom(- × A, B) is representable — i.e., whether there exists an object B^A with a natural isomorphism Hom(C × A, B) ≅ Hom(C, B^A) for all C. If this representability fails for even one pair, the category is not cartesian closed.
