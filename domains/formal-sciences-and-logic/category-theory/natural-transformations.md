---
id: natural-transformations
title: Natural Transformations
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
builds-toward:
- functor-categories
- yoneda-lemma
- adjoint-functors
- monads-in-category-theory
tags:
- natural transformation
- naturality square
- morphisms of functors
stage: advanced
status: draft
---

# Natural Transformations

## Core Idea
A natural transformation η: F ⇒ G between functors F, G: C → D assigns to each object A in C a morphism η_A: F(A) → G(A) in D such that for every morphism f: A → B in C, the naturality square commutes: η_B ∘ F(f) = G(f) ∘ η_A. Natural transformations are the morphisms between functors, making them the 2-morphisms of the 2-category Cat. The concept of 'naturality' formalizes the intuition that a construction is canonical or independent of arbitrary choices—the determinant, double dual embedding, and many algebraic maps are natural transformations.

## How It's Best Learned
Verify that the double dual embedding V → V** for vector spaces (sending v to the evaluation map ev_v) is natural by drawing and checking the naturality square for an arbitrary linear map T: V → W. Contrast with the non-natural isomorphism V ≅ V* (which requires choosing a basis).

## Common Misconceptions
- Naturality is not automatic from having the right type signature; many component-wise maps fail the naturality square.
- A natural transformation is not a single morphism but a whole family of morphisms, one per object, satisfying coherence conditions.
- Natural isomorphisms (where every η_A is an isomorphism) are stronger than just having isomorphic functors pointwise.
