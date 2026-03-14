---
id: derived-equivalences-categories
title: Derived Equivalences of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: triangulated-categories
  type: hard
- id: equivalence-of-categories
  type: hard
builds-toward:
- topos-theory-intro
tags:
- derived-equivalence
- derived-category
- Morita
- homological
stage: advanced
status: draft
---

# Derived Equivalences of Categories

## Core Idea
Two categories are derived equivalent if their derived categories are equivalent as triangulated categories. Derived equivalence is coarser than ordinary equivalence but preserves homological invariants. Morita equivalence (between module categories) is an instance of derived equivalence. Derived equivalent categories need not be equivalent as ordinary categories but share the same derived categorical structure, making derived equivalence a fundamental invariant in representation theory.

## How It's Best Learned
Study Morita equivalence for rings and modules as the canonical example. Verify that derived equivalent categories have isomorphic Hochschild homology and K-theory. Explore how tilting complexes induce derived equivalences between module categories.

## Common Misconceptions
Derived equivalence is weaker than ordinary equivalence; two derived equivalent categories may have very different ordinary categorical properties. The notion depends on the choice of derived category (unbounded, bounded, etc.). Not every equivalence of derived categories lifts to an equivalence of underlying categories.
