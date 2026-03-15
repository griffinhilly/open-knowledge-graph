---
id: adjoint-functors
title: Adjoint Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: hard
- id: universal-properties
  type: soft
- id: representable-functors
  type: soft
- id: comma-categories
  type: soft
- id: initial-and-terminal-objects
  type: soft
- id: products-and-coproducts
  type: soft
- id: pullbacks-and-pushouts
  type: soft
- id: yoneda-lemma
  type: soft
- id: group-homomorphisms
  type: soft
- id: composition-of-functions
  type: soft
builds-toward:
- adjunction-unit-and-counit
- monads-in-category-theory
tags:
- adjunction
- left adjoint
- right adjoint
- hom-set bijection
- universal arrow
stage: advanced
status: validated
---
# Adjoint Functors

## Core Idea
A pair of functors F: C → D and G: D → C form an adjunction (F ⊣ G, F left adjoint to G) if there is a natural bijection Hom_D(F(A), B) ≅ Hom_C(A, G(B)) for all A in C and B in D. Adjunctions are one of the most pervasive structures in mathematics: free–forgetful pairs (free group ⊣ forgetful), product–exponential pairs in Set, left Kan extensions, and many constructions in algebra and topology arise as adjunctions. Right adjoints preserve limits; left adjoints preserve colimits—a powerful tool for computing limits in many categories.

## How It's Best Learned
Verify the free-forgetful adjunction: a function from a set S to the underlying set of a group G corresponds naturally to a group homomorphism from the free group F(S) to G. Draw the natural bijection explicitly and verify naturality in both variables. Internalize the slogan: 'adjoint functors arise naturally and are ubiquitous'.

## Common Misconceptions
- Not every functor has an adjoint; existence of adjoints is a substantive condition (addressed by adjoint functor theorems).
- Left and right adjoints are not symmetric roles: the left adjoint preserves colimits while the right adjoint preserves limits.
- An adjunction is not an equivalence of categories; additional conditions (the unit and counit being isomorphisms) are required for an equivalence.
