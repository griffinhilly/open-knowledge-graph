---
id: natural-isomorphisms
title: Natural Isomorphisms Between Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: functors
  type: hard
builds-toward:
- equivalence-of-categories
- adjoint-functors
tags:
- functors
- equivalence
- natural-transformations
stage: advanced
status: draft
---

# Natural Isomorphisms Between Functors

## Core Idea
A natural isomorphism between functors F, G: C → D is a natural transformation α: F ⇒ G where each component α_c: F(c) → G(c) is an isomorphism. Natural isomorphisms express that two functors are 'the same up to isomorphism' in a way respecting naturality. They form the 2-morphisms in the 2-category Cat.
