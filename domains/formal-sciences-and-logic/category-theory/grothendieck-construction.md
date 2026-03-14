---
id: grothendieck-construction
title: The Grothendieck Construction
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: fibered-categories
  type: hard
- id: natural-transformations
  type: hard
- id: functor-categories
  type: soft
- id: comma-categories
  type: soft
tags:
- Grothendieck construction
- pseudofunctor
- total category
- fibration equivalence
- category of elements
- lax colimit
stage: advanced
status: draft
---
# The Grothendieck Construction

## Core Idea
The Grothendieck construction transforms a (pseudo)functor F: B → Cat into a single fibered category ∫F (the total category) equipped with a projection p: ∫F → B. Objects of ∫F are pairs (b, x) where b is an object of B and x is an object of F(b); a morphism (b, x) → (b', x') is a pair (f, φ) where f: b → b' in B and φ: F(f)(x) → x' in F(b'). This construction establishes an equivalence between pseudofunctors B → Cat and fibered categories over B, providing a bridge between "indexed" and "fibered" perspectives on families of categories. For set-valued functors F: C → Set, the Grothendieck construction yields the category of elements ∫F, and the Yoneda lemma can be rephrased as a statement about this category.

## How It's Best Learned
Start with a functor F: C → Set for a small category C (e.g., a presheaf on a poset). Build the category of elements ∫F explicitly: list all pairs (c, x ∈ F(c)) as objects and all morphisms induced by arrows in C. Verify this gives a category fibered over C. Then generalize to a pseudofunctor to Cat and understand how the morphism definition accounts for the pseudofunctorial coherence data.

## Common Misconceptions
- The Grothendieck construction for Set-valued functors (category of elements) and the general Cat-valued version are related but not identical; the Set version is a special case where each fiber is a discrete category.
- The equivalence between pseudofunctors and fibrations is an equivalence of 2-categories, not merely a bijection; the 2-categorical structure (with pseudonatural transformations and modifications) is essential.
- The total category ∫F is not the disjoint union of the fibers; the morphisms in ∫F encode how the fibers are connected via the action of F on morphisms in the base.
