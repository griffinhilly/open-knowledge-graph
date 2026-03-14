---
id: monoidal-categories
title: Monoidal Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: products-and-coproducts
  type: hard
- id: natural-transformations
  type: soft
- id: isomorphisms-in-categories
  type: soft
builds-toward:
- closed-monoidal-categories
- enriched-categories
tags:
- monoidal category
- tensor product
- unit object
- associator
- coherence theorem
- Mac Lane
stage: advanced
status: draft
---
# Monoidal Categories

## Core Idea
A monoidal category is a category C equipped with a bifunctor ⊗: C × C → C (the tensor product), a unit object I, and natural isomorphisms for associativity (A ⊗ (B ⊗ C) ≅ (A ⊗ B) ⊗ C) and left/right unit laws (I ⊗ A ≅ A ≅ A ⊗ I), all satisfying Mac Lane's coherence conditions (the pentagon and triangle axioms). Examples include (Set, ×, {*}), (Vect, ⊗, k), (Ab, ⊗_Z, Z), and (Cat, ×, 1). Mac Lane's coherence theorem guarantees that every diagram built from the associator and unitors commutes, so one may work as if ⊗ were strictly associative and unital.

## How It's Best Learned
Start with (Set, ×, {*}) and verify the associator and unitor isomorphisms explicitly. Then move to (Vect_k, ⊗_k, k) and confirm the same axioms hold. State the pentagon and triangle axioms and check them for these examples. Appreciate the coherence theorem by constructing a diagram with multiple paths and verifying they agree.

## Common Misconceptions
- A monoidal category need not be symmetric; the braided and symmetric variants require additional structure (a braiding natural isomorphism).
- The tensor product is not the same as the categorical product; in Vect, the tensor product and direct product are different constructions.
- Coherence does not mean the associator is the identity; it means all diagrams built from structural isomorphisms commute, allowing us to suppress them notationally.
