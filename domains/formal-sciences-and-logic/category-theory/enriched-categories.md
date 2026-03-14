---
id: enriched-categories
title: Enriched Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: functor-categories
  type: soft
- id: categories-and-morphisms
  type: soft
tags:
- enriched category
- V-category
- hom-object
- 2-category
- Ab-enriched
- metric space
stage: advanced
status: draft
---
# Enriched Categories

## Core Idea
A category enriched over a monoidal category (V, ⊗, I) replaces hom-sets with hom-objects in V: for objects A, B in C, the "morphisms from A to B" form an object C(A, B) in V rather than a set. Composition is a morphism C(B, C) ⊗ C(A, B) → C(A, C) in V, and identities are morphisms I → C(A, A), satisfying associativity and unit laws. This framework unifies many structures: Set-enriched categories are ordinary categories, Ab-enriched categories are preadditive categories, Cat-enriched categories are 2-categories, and [0,∞]-enriched categories (with + as tensor, 0 as unit) are generalized metric spaces (Lawvere's insight). Enriched category theory provides a uniform language for studying these diverse structures.

## How It's Best Learned
Start with Ab-enrichment: in R-Mod, the hom-sets are naturally abelian groups and composition is bilinear. Verify the enriched axioms. Then consider Lawvere's metric space example: objects are points, C(A,B) is a non-negative real number (the distance), composition is the triangle inequality d(A,C) ≤ d(A,B) + d(B,C), and the identity axiom is d(A,A) = 0. This surprising reformulation reveals the power of the enriched perspective.

## Common Misconceptions
- Enriched categories are not merely categories with extra structure on morphisms; the entire composition and identity structure is reformulated within V, and there may be no underlying ordinary category if V lacks a suitable forgetful functor.
- The choice of monoidal category V matters: enriching over different V yields genuinely different theories (topology for Top-enrichment, algebra for Ab-enrichment).
- An enriched functor must preserve the V-valued hom structure, which is a stronger condition than merely being a functor on any underlying ordinary category.
