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
