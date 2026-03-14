---
id: representable-functors
title: Representable Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: soft
- id: opposite-categories-and-duality
  type: soft
- id: full-and-faithful-functors
  type: soft
- id: functor-categories
  type: soft
builds-toward:
- yoneda-lemma
- adjoint-functors
tags:
- representable functor
- hom-functor
- Yoneda
- presheaf
stage: advanced
status: validated
---
# Representable Functors

## Core Idea
For each object A in a locally small category C, the hom-functor Hom(A, -): C → Set sends each object B to the set of morphisms Hom(A, B) and each morphism f: B → C to post-composition with f. A functor F: C → Set is representable if it is naturally isomorphic to Hom(A, -) for some object A, called the representing object. Representability is a powerful concept: many construction functors (tensor product, free algebras, cohomology groups) are representable, and their representing objects carry universal properties.

## How It's Best Learned
Show that the forgetful functor from Grp to Set is representable by the free group on one generator ℤ: a group homomorphism ℤ → G is uniquely determined by where 1 goes, so Grp(ℤ, G) ≅ G as sets, naturally in G. Identify the representing objects for other familiar functors.

## Common Misconceptions
- Not every functor C → Set is representable; representability is a non-trivial condition checked via the Yoneda lemma.
- The representing object is unique up to unique isomorphism, not unique as a set-theoretic construction.
- The contravariant hom-functor Hom(-, A) is representable in C^op, not in C.
