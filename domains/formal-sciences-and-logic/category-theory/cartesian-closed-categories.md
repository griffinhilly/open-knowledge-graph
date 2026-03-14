---
id: cartesian-closed-categories
title: Cartesian Closed Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: closed-monoidal-categories
  type: hard
- id: products-and-coproducts
  type: hard
- id: initial-and-terminal-objects
  type: soft
builds-toward:
- topos-theory-intro
tags:
- cartesian closed category
- CCC
- exponential object
- lambda calculus
- simply typed lambda calculus
- Curry-Howard-Lambek
stage: advanced
status: draft
---
# Cartesian Closed Categories

## Core Idea
A cartesian closed category (CCC) is a category with finite products (including a terminal object) in which the product functor (−) × B has a right adjoint B^(−), giving exponential objects. The defining adjunction Hom(A × B, C) ≅ Hom(A, C^B) generalizes the set-theoretic fact that functions from A × B to C correspond to curried functions from A to C^B. CCCs provide the categorical semantics for the simply typed lambda calculus: types are objects, terms are morphisms, and beta-reduction corresponds to the evaluation map. Key examples include Set, the category of small categories Cat, and any elementary topos.

## How It's Best Learned
Start with Set: verify that C^B = {functions B → C} with the evaluation map ev: C^B × B → C satisfies the universal property. Then construct exponentials in a poset category (a Heyting algebra) where C^B = (B ⇒ C). Connect to lambda calculus by translating lambda abstraction as the transpose of a morphism and application as composition with evaluation.

## Common Misconceptions
- Not every category with products is cartesian closed; Top (topological spaces) has products but is not cartesian closed without restricting to a convenient subcategory.
- Cartesian closed is a special case of closed monoidal where the monoidal product is the categorical product; replacing products with a general tensor gives a different notion.
- The exponential object C^B is not merely the hom-set Hom(B,C); it is an internal object in the category representing that hom-set.
