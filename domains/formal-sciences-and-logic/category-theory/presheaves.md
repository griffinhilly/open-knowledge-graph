---
id: presheaves
title: Presheaves
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: functor-categories
  type: hard
- id: opposite-categories-and-duality
  type: soft
builds-toward:
- sheaves-and-sheafification
- topos-theory-intro
tags:
- presheaf
- functor category
- representable presheaf
- Yoneda embedding
- Set-valued functor
stage: advanced
status: draft
---
# Presheaves

## Core Idea
A presheaf on a category C is a functor F: C^op → Set. The category of presheaves [C^op, Set] is a fundamental construction: it is complete, cocomplete, and cartesian closed, making it a topos. Every object A of C determines a representable presheaf Hom(−, A), and the Yoneda embedding y: C → [C^op, Set] sending A to Hom(−, A) is full and faithful, so C embeds as a full subcategory of its presheaf category. The presheaf category can be thought of as the free cocompletion of C—it freely adds all colimits.

## How It's Best Learned
Take a small concrete category such as a poset (P, ≤) and write out several presheaves as contravariant functors to Set. Compute the representable presheaves and verify that the Yoneda embedding is injective on objects and morphisms. Then explore a non-representable presheaf and understand why it cannot arise as Hom(−, A) for any A.

## Common Misconceptions
- A presheaf is a functor from C^op to Set, not from C to Set; the contravariance is essential and reflects the restriction maps in geometric examples.
- Not every presheaf is representable; representability is a strong condition equivalent to the presheaf preserving all limits that exist in C.
- The presheaf category [C^op, Set] is not the same as the functor category [C, Set]; the two are related by the opposite category construction.
