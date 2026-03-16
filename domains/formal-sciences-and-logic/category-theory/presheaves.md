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
- id: set-operations
  type: soft
- id: indexed-families-of-sets
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

## Explainer

The Yoneda lemma you've already mastered tells you that each object A in a category C determines a contravariant functor Hom(−, A): C^op → Set, sending each object X to the set of morphisms X → A, and sending each morphism f: X → Y to the precomposition map (− ∘ f): Hom(Y, A) → Hom(X, A). The Yoneda embedding y: C → [C^op, Set] shows that this assignment is full and faithful — so C embeds into a larger category whose objects are *all* contravariant functors from C to Set. A **presheaf** on C is simply any such functor: F: C^op → Set. The presheaves include the representable ones (Hom(−, A) for each A) but also many others that don't correspond to any single object of C.

The geometric motivation makes the contravariance feel natural. Take C to be the category **Open(X)** of open sets of a topological space X, with morphisms being inclusions U ↪ V whenever U ⊆ V. A presheaf F on this category assigns a set F(U) to each open set U — think of it as "local data over U" (functions, sections, observations). When U ⊆ V, the morphism V → U in C^op (remember, morphisms reverse in the opposite category) corresponds to a **restriction map** F(V) → F(U): data defined on a larger open set can be restricted to a smaller one. This is exactly the covariant direction for data flow — data restricts to smaller sets, which is why the functor must be contravariant on the original category. Every presheaf you encounter in geometry, topology, or algebra has this restriction-map flavor.

The presheaf category [C^op, Set] has remarkable categorical properties: it has all small limits and colimits (computed pointwise), it is cartesian closed (you can form "function presheaves"), and it is a **topos** — a category with enough structure to do logic and set theory internally. None of this requires C itself to be well-behaved; the presheaf construction freely adds whatever C lacks. The slogan is that [C^op, Set] is the **free cocompletion** of C: every functor from C into a cocomplete category extends uniquely (up to unique natural isomorphism) through the Yoneda embedding. This makes presheaves the universal device for "adding formal colimits" to C.

Not all presheaves are representable, and this non-representability is important rather than a deficiency. A representable presheaf Hom(−, A) knows exactly where every morphism in C points; a non-representable presheaf can encode "generalized objects" that C doesn't contain. In algebraic geometry, for instance, moduli problems (classify all curves of genus g, all elliptic curves with a level structure) often have no representing object in the category of schemes, but they do define perfectly good presheaves — and the project of sheafification and algebraic spaces is essentially about deciding which of these presheaves are "geometric enough" to count as spaces. Understanding presheaves is thus the entry point not just to sheaf theory but to the modern approach to geometry where spaces are defined by what you can map *into* them.

