---
id: two-categories
title: 2-Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: functor-categories
  type: hard
- id: categories-and-morphisms
  type: soft
builds-toward:
- fibered-categories
tags:
- 2-category
- 2-morphism
- horizontal composition
- vertical composition
- interchange law
- Cat
- bicategory
stage: advanced
status: draft
---
# 2-Categories

## Core Idea
A 2-category is a category enriched over Cat: it has objects (0-cells), morphisms between objects (1-cells), and morphisms between morphisms (2-cells or 2-morphisms). The 2-cells can be composed in two ways: vertically (composing 2-cells along shared 1-cells, like composing natural transformations) and horizontally (composing 2-cells along shared 0-cells, like whiskering). These two compositions must satisfy the interchange law. The primary example is Cat itself, where objects are categories, 1-cells are functors, and 2-cells are natural transformations. Strict 2-categories require associativity and unit laws to hold on the nose; the weaker notion of bicategory allows them to hold only up to coherent isomorphism.

## How It's Best Learned
Take Cat as the running example. Identify the 0-cells (small categories), 1-cells (functors), and 2-cells (natural transformations). Practice vertical composition (composing two natural transformations α: F ⇒ G and β: G ⇒ H) and horizontal composition (whiskering a natural transformation with a functor). Verify the interchange law on a concrete example. Then consider the bicategory of spans as a non-strict example.

## Common Misconceptions
- A 2-category is not the same as a double category; 2-categories have one type of 1-cell, while double categories have two (horizontal and vertical).
- Strict and weak (bi)categories are genuinely different notions; not every bicategory is equivalent to a strict 2-category in the naive sense, though the coherence theorem for bicategories provides a strictification result.
- The interchange law is not a consequence of the other axioms; it is an independent condition that constrains how vertical and horizontal composition interact.
