---
id: free-and-forgetful-functors
title: Free and Forgetful Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: free-objects
  type: hard
builds-toward:
- left-right-adjoints
tags:
- free
- forgetful
- adjoint
- universal-property
stage: advanced
status: draft
---

# Free and Forgetful Functors

## Core Idea
The forgetful functor U: D → C 'forgets' structure by mapping objects to their underlying sets or simpler structures. The free functor F: C → D is left adjoint to U, and sends generators to the 'freest' objects in D built from them. The adjunction F ⊣ U encodes the universal property of free objects: every function from a generating set extends uniquely to a D-morphism.

## How It's Best Learned
Study free-forgetful adjunctions for groups, rings, and modules. Compute free groups on generators and verify the universal property by constructing unique homomorphic extensions. Explore the relationship between free objects and presentable objects.

## Common Misconceptions
Free objects are not trivial or empty; they are the 'largest' objects with minimal structural constraints. Not every forgetful functor has a left adjoint; existence requires sufficient colimits or a generating set. The forgetful functor must be well-defined on both objects and morphisms, not just on objects.
