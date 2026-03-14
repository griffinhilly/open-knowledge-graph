---
id: derived-categories
title: Derived Categories and Derived Equivalences
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: derived-functors
  type: hard
- id: triangulated-categories
  type: soft
builds-toward:
- spectral-sequences-introduction
tags:
- derived-category
- homotopy-category
- localization
- derived-equivalence
stage: abstract-reasoning
status: draft
---

# Derived Categories and Derived Equivalences

## Core Idea
The derived category of an abelian category is obtained by localizing the category of chain complexes at quasi-isomorphisms, so that objects related by homotopy-equivalent chain maps become isomorphic. Derived categories package homological invariants into a single triangulated category and are fundamental to homological algebra. Derived equivalences between algebras capture deep relationships between their module categories.

## How It's Best Learned
Begin with the derived category of an abelian category (e.g., modules over a ring or sheaves of abelian groups). Understand quasi-isomorphisms and homotopy equivalences. Compute the derived category in concrete examples. Study derived functors and how they arise naturally in this setting.

## Common Misconceptions
The derived category is not the homotopy category; localization at quasi-isomorphisms adds new isomorphisms beyond homotopy equivalences. Also, derived categories are triangulated but not necessarily abelian.
