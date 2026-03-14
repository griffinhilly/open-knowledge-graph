---
id: categories-and-morphisms
title: Categories and Morphisms
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: naive-set-theory
  type: hard
- id: binary-relations
  type: soft
- id: composition-of-functions
  type: soft
- id: set-theory-basics
  type: soft
- id: injective-surjective-bijective
  type: soft
builds-toward:
- functors
- isomorphisms-in-categories
- opposite-categories-and-duality
tags:
- categories
- morphisms
- objects
- composition
- identity
stage: advanced
status: validated
---

# Categories and Morphisms

## Core Idea
A category consists of a collection of objects and a collection of morphisms (arrows) between them, together with a composition operation that is associative and has identity morphisms for each object. Categories abstract the essential structure of mathematical systems: sets with functions, groups with homomorphisms, vector spaces with linear maps, and topological spaces with continuous maps all form categories. The morphisms, not the objects, carry most of the structural content—category theory studies what can be said about mathematical structures purely from the arrows between them.

## How It's Best Learned
Start by recognizing familiar mathematical structures as categories: Set (sets and functions), Grp (groups and homomorphisms), Vect (vector spaces and linear maps). Verify the axioms—associativity of composition and existence of identities—in each case. Then work through small finite categories drawn as directed graphs to build intuition before abstract definitions.

## Common Misconceptions
- Objects need not have internal structure; in some categories, objects are just placeholders and all information is in the morphisms.
- A morphism is not necessarily a function—in a poset category, each morphism represents a ≤ relation, not a map.
- Identity morphisms are required for every object, not just for some.
