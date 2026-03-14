---
id: two-categories-and-weak-functors
title: 2-Categories and Weak Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- higher-category-theory-intro
tags:
- higher-categories
- two-categories
- weak-functors
- natural-transformations
stage: abstract-reasoning
status: draft
---

# 2-Categories and Weak Functors

## Core Idea
A 2-category consists of objects, morphisms (1-cells) between objects, and 2-morphisms (2-cells) between morphisms, with composition operations at both levels. Weak (or lax) functors between 2-categories preserve the 2-categorical structure up to invertible 2-morphisms, generalizing both ordinary functors and natural transformations. This framework encompasses categories, functors, and natural transformations as a single 2-categorical structure.

## How It's Best Learned
Study the 2-category Cat of all categories, functors, and natural transformations. Understand how ordinary categories and functors sit inside this structure. Explore other 2-categories: 2-categories arising from partial orders, from rings, and from algebraic structures.

## Common Misconceptions
In a 2-category, 2-morphisms need not have inverses; strict equality of compositions is replaced by isomorphism. Weak functors are less restrictive than strict functors and are often more natural, but this requires care in applications.
