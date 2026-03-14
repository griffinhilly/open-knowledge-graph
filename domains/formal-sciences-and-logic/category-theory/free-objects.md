---
id: free-objects
title: Free Objects
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: universal-properties
  type: hard
- id: adjoint-functors
  type: soft
- id: concrete-categories
  type: soft
builds-toward:
- monads-in-category-theory
tags:
- free group
- free monoid
- free module
- universal property
- left adjoint
- forgetful functor
stage: advanced
status: draft
---
# Free Objects

## Core Idea
A free object on a set S in a concrete category C is an object F(S) together with a function η: S → U(F(S)) such that every function f: S → U(A) factors uniquely through a morphism F(S) → A in C. This universal property makes the free construction F left adjoint to the forgetful functor U: C → Set. Free groups, free monoids, free modules, and free algebras all arise this way. The adjunction F ⊣ U encapsulates the idea that the free object is the most general or least constrained object built from the generators S, subject only to the axioms of the category.

## How It's Best Learned
Construct the free monoid on a set S (it is just the set of finite words in S with concatenation) and verify the universal property: every function from S to a monoid M extends uniquely to a monoid homomorphism from the free monoid to M. Then repeat for free groups and free vector spaces to see the pattern.

## Common Misconceptions
- Free objects are not always easy to describe concretely; the free group on S requires quotienting by relations, unlike the free monoid which is simply the set of words.
- Not every category has free objects; the forgetful functor must have a left adjoint, which is not guaranteed.
- A free object is not the same as a projective object, though free implies projective in many algebraic categories.
