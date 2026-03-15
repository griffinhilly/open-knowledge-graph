---
id: functors
title: Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: composition-of-functions
  type: soft
- id: functions-and-function-properties
  type: soft
- id: function-composition
  type: hard
builds-toward:
- natural-transformations
- functor-categories
- representable-functors
- full-and-faithful-functors
tags:
- functors
- structure-preserving maps
- covariant
- contravariant
stage: advanced
status: validated
---

# Functors

## Core Idea
A functor F: C → D between categories assigns to each object A in C an object F(A) in D, and to each morphism f: A → B a morphism F(f): F(A) → F(B), preserving composition and identities: F(g∘f) = F(g)∘F(f) and F(id_A) = id_{F(A)}. Functors are the morphisms of the category of categories; they include familiar constructions like the forgetful functor from Grp to Set, the free group functor, and the fundamental group functor in topology. A contravariant functor reverses the direction of morphisms and can be viewed as a covariant functor from C^op.

## How It's Best Learned
Work through at least three concrete functors: the forgetful functor from groups to sets, the power set functor on Set, and the hom-functor Hom(A, -). Verify functoriality axioms explicitly for each. Then identify where contravariance arises naturally (e.g., Hom(-, B) reverses arrows).

## Common Misconceptions
- Functors need not be injective or surjective on objects or morphisms; they can collapse structure.
- A contravariant functor is not a functor 'going backward'—it is a covariant functor from the opposite category.
- Functors do not require the categories to have the same size or type.
