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
status: validated
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

## Explainer

From your work with universal properties, you know that categorical objects are characterized not by what they *contain* but by the morphisms they participate in. Initial and terminal objects are the simplest application of this principle — they are defined entirely by the structure of arrows between them and every other object in the category.

An **initial object** is one from which there is exactly one morphism to every object in the category. The word "every" makes it powerful; the word "exactly one" makes it a universal property. In **Set**, the empty set ∅ is initial: for any set X, there is exactly one function ∅ → X, namely the empty function (vacuously, it sends no elements anywhere). In the category of rings, the ring of integers ℤ is initial: for any ring R, there is exactly one ring homomorphism ℤ → R, which sends 1 to the multiplicative identity of R. These two examples feel very different concretely, but categorically they are identical in kind.

A **terminal object** reverses all arrows: it is one to which there is exactly one morphism from every object. In **Set**, any singleton {*} is terminal: for any set X, there is exactly one function X → {*}, which sends every element to the single element. In **Vect_k** (the category of vector spaces over a field k), the zero vector space {0} is both initial and terminal — sending every vector to 0 is the unique morphism to the zero space, and the zero space has only the zero morphism to any space. An object that is simultaneously initial and terminal is called a **zero object**.

The **duality** between initial and terminal objects is the simplest instance of categorical duality: an initial object in C is exactly a terminal object in C^op (the opposite category), because reversing all arrows converts "unique morphism from it to everything" into "unique morphism from everything to it." This is why you prove facts about initial objects once and get the corresponding facts about terminal objects for free by dualizing. **Uniqueness up to unique isomorphism** is a theorem, not a definition: if 0 and 0' are both initial, there are unique morphisms 0 → 0' and 0' → 0, and their composites must be the identity morphisms (because there is a unique morphism from an initial object to itself, namely the identity). So any two initial objects are canonically isomorphic — you can speak of "the" initial object without ambiguity.
