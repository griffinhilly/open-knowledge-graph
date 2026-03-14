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
