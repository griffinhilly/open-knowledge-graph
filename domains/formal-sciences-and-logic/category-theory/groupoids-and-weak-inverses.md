---
id: groupoids-and-weak-inverses
title: Groupoids and Weak Inverses
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: isomorphisms-in-categories
  type: hard
builds-toward:
- the-fundamental-groupoid
tags:
- groupoids
- invertible-morphisms
- automorphisms
stage: abstract-reasoning
status: draft
---

# Groupoids and Weak Inverses

## Core Idea
A groupoid is a category in which every morphism is an isomorphism, generalizing both groups and equivalence relations. Groupoids provide a framework for studying 'partial' algebraic structures where not all pairs of elements can be composed, and arise naturally in topology, combinatorics, and analysis. The theory of groupoids captures aspects of both group theory and category theory.

## How It's Best Learned
Study the fundamental groupoid of a topological space, the groupoid of a group action, and abstract groupoids given by presentations. Verify that morphisms are invertible and explore the automorphism groups at each object. Compute groupoid homology and cohomology.

## Common Misconceptions
A groupoid is not just a group with extra structure; it has multiple objects. The identity morphisms at different objects are distinct, and composition is only defined when target and source match appropriately.
