---
id: quotient-categories
title: Quotient Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
builds-toward:
- localization-of-categories
tags:
- quotient-construction
- equivalence-relations
- morphism-identification
stage: abstract-reasoning
status: draft
---

# Quotient Categories

## Core Idea
A quotient category is formed by identifying morphisms in a category according to an equivalence relation that respects composition, resulting in a category where some formerly distinct morphisms are identical. Quotient categories generalize the notion of quotient structures in algebra and provide a framework for understanding how categorical information changes under identifications.

## How It's Best Learned
Start with simple examples: quotient of a discrete category by an equivalence relation on objects, and quotient of a category of complexes by homotopy equivalence. Verify that the quotient map is universal and that the quotient respects categorical structure.

## Common Misconceptions
Not every equivalence relation on morphisms descends to a valid quotient category; the relation must be compatible with composition. Additionally, the quotient category may collapse structure in surprising ways.
