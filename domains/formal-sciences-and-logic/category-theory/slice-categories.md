---
id: slice-categories
title: Slice and Coslice Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- universal-properties
- kan-extensions
tags:
- slice
- coslice
- comma
- relative
- over
stage: advanced
status: draft
---

# Slice and Coslice Categories

## Core Idea
The slice category C/X has objects as morphisms f: Y → X and morphisms as commutative triangles. The coslice category X/C has objects as morphisms X → Y with the same commutative structure. Slice categories formalize 'relative' categorical properties and are essential for defining limits and colimits in a relative sense. They appear naturally in studying fibrations and in defining universal properties with a fixed reference object.

## How It's Best Learned
Study slice categories of Set over a set S (equivalent to S-indexed families of sets). Examine slice categories of a poset over an element, and verify that limits in the slice category correspond to special limits in the original category.

## Common Misconceptions
A slice category is not a full subcategory—morphisms in C/X are defined relative to X. Not every limit in C/X lifts to a limit in C. The universal properties in slice categories are weaker than absolute universal properties because they depend on the choice of X.
