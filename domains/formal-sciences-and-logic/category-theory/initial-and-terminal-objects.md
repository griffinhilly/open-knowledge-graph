---
id: initial-and-terminal-objects
title: Initial and Terminal Objects
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: universal-properties
  type: hard
- id: opposite-categories-and-duality
  type: soft
builds-toward:
- products-and-coproducts
- limits-and-colimits
- adjoint-functors
tags:
- initial object
- terminal object
- zero object
- duality
stage: advanced
status: draft
---

# Initial and Terminal Objects

## Core Idea
An initial object 0 in a category is one from which there exists a unique morphism to every object; a terminal object 1 is one to which there exists a unique morphism from every object. These are dual concepts: initial in C is terminal in C^op. Initial and terminal objects, when they exist, are unique up to unique isomorphism. In Set, the empty set is initial (unique function to each set) and any singleton is terminal; in Grp, the trivial group is both initial and terminal (a zero object).

## How It's Best Learned
Identify initial and terminal objects in several categories: Set, Vect_k, Top, partially ordered sets (viewed as categories), and the category of rings. Notice that in posets, initial = minimum element and terminal = maximum element when they exist.

## Common Misconceptions
- Initial objects need not exist in every category; their existence is a property of the specific category.
- The uniqueness of morphisms is part of the definition, not a consequence—it distinguishes initial/terminal objects from objects that merely have morphisms to everything.
- A zero object (both initial and terminal) does not exist in every category; Set has no zero object.
