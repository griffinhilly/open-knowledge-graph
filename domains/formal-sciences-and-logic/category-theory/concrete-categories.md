---
id: concrete-categories
title: Concrete Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
- id: full-and-faithful-functors
  type: soft
builds-toward:
- free-objects
tags:
- concrete category
- forgetful functor
- faithful functor
- Set
- Grp
- Top
stage: advanced
status: draft
---
# Concrete Categories

## Core Idea
A concrete category is a category C equipped with a faithful functor U: C → Set, called the forgetful functor, that assigns to each object its underlying set and to each morphism the underlying function. Most familiar algebraic and topological categories are concrete: Grp (groups with homomorphisms), Top (topological spaces with continuous maps), Vect_k (vector spaces with linear maps), and Ring (rings with ring homomorphisms). The faithfulness of U means that morphisms in C are completely determined by their action on underlying sets, but the functor need not be full—not every set function is a group homomorphism, for instance.

## How It's Best Learned
Pick three concrete categories (Grp, Top, Vect) and for each one explicitly identify the forgetful functor, verify it is faithful, and determine whether it is full. Then find an example of a non-concrete category (the homotopy category of topological spaces) and understand why no faithful functor to Set exists.

## Common Misconceptions
- Not every category is concrete; the homotopy category hoTop is a standard counterexample, shown by Freyd's theorem.
- The forgetful functor is part of the structure of a concrete category, not a property—the same category may be concretized in different ways.
- Faithfulness does not imply fullness: the forgetful functor Grp → Set is faithful but not full, since not every set function is a homomorphism.

## Explainer

Most categories you've encountered — groups with homomorphisms, vector spaces with linear maps, topological spaces with continuous maps — come with an implicit understanding that their objects "have elements" and their morphisms "are functions" that preserve some structure. **Concrete categories** make this intuition precise in categorical language, using the functor machinery you've already developed.

A concrete category is not just a category C; it is a pair (C, U) where **U: C → Set** is a **faithful functor**, called the **forgetful functor**. "Forgetful" because U forgets the structure: it sends a group (G, ·) to its underlying set G, a topological space (X, τ) to the set X, a vector space V to the set of its elements — the algebraic or topological structure is discarded. Faithfulness (which you know means U is injective on each hom-set) captures the idea that the morphisms of C are completely determined by their underlying set-functions. Two distinct group homomorphisms must induce two distinct set functions; there are no "phantom morphisms" that look the same on elements but differ categorically.

The crucial asymmetry is that faithfulness does not imply fullness. **Fullness** of U: C → Set would mean every set function between underlying sets is a morphism in C — that every function between groups is a homomorphism, that every function between topological spaces is continuous. That is obviously false. Faithful-but-not-full is the generic situation for forgetful functors: morphisms in C must be structure-preserving functions, but not every function preserves the structure. The forgetful functor "sees" the morphisms correctly but sees more set functions than actually exist in C.

Concreteness is **structure on** a category, not an intrinsic property of the abstract category. The same abstract category can be concretized in multiple genuinely different ways: the category of groups can be concretized via U: Grp → Set (the standard forgetful functor), but also by sending each group to its set of subgroups, or to the set of its automorphisms. Different concretizations give different notions of "elements." Conversely, some categories cannot be made concrete at all. The homotopy category **hoTop** — whose morphisms are homotopy classes of continuous maps rather than the maps themselves — is a standard example: Freyd's theorem proves no faithful functor hoTop → Set exists, because the morphism sets are too "large" in a structurally inconsistent way. This non-concreteness reflects that homotopy classes are not faithfully represented by their action on points.
