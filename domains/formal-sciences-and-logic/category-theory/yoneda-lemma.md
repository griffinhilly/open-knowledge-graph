---
id: yoneda-lemma
title: The Yoneda Lemma
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: representable-functors
  type: hard
- id: natural-transformations
  type: hard
- id: functor-categories
  type: soft
- id: full-and-faithful-functors
  type: soft
- id: limits-and-colimits
  type: soft
- id: functions-and-function-properties
  type: soft
- id: composition-of-functions
  type: soft
- id: function-composition
  type: soft
- id: set-operations
  type: soft
- id: functions-and-mappings-formal
  type: soft
- id: equivalence-relations
  type: soft
- id: function-composition-and-inverses
  type: soft
builds-toward:
- adjoint-functors
- equivalence-of-categories
tags:
- Yoneda lemma
- Yoneda embedding
- natural transformations
- presheaf
- representability
stage: advanced
status: validated
---
# The Yoneda Lemma

## Core Idea
The Yoneda lemma states that for any functor F: C → Set and any object A in C, there is a bijection Nat(Hom(A,-), F) ≅ F(A) that is natural in both A and F. This means natural transformations from a representable functor to any functor F are completely determined by a single element of F(A). The Yoneda embedding A ↦ Hom(A,-) is a fully faithful functor from C to [C^op, Set], showing every category embeds into a presheaf category and that an object is completely determined by how morphisms map into it from all other objects.

## How It's Best Learned
Work through the proof step by step: given a natural transformation η: Hom(A,-) ⇒ F, evaluate at A and apply to id_A to get an element of F(A). Verify this map is an inverse to the map F(A) → Nat(Hom(A,-), F) given by the Yoneda construction. Appreciate the slogan 'an object is determined by its relationships with all other objects'.

## Common Misconceptions
- The Yoneda lemma is not merely a technical result; it is a fundamental philosophical principle of category theory—objects are determined by their morphisms.
- The bijection Nat(Hom(A,-), F) ≅ F(A) is not a set isomorphism requiring special conditions; it holds for all locally small categories.
- The Yoneda embedding is contravariant when using Hom(-,A); be careful about which version (covariant vs. contravariant) is being used.
