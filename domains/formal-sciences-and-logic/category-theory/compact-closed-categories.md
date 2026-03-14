---
id: compact-closed-categories
title: Compact Closed Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: symmetric-monoidal-categories
  type: hard
builds-toward:
- dagger-categories
tags:
- compact-closed
- dual
- trace
- finite-dimensionality
- linear-logic
stage: advanced
status: draft
---

# Compact Closed Categories

## Core Idea
A compact closed category is a monoidal category where every object X has a dual object X* with evaluation and coevaluation morphisms satisfying triangle identities. This categorical structure captures finite-dimensionality and enables a notion of categorical trace. Compact closed categories are the setting for categorical quantum mechanics and linear logic, providing semantics where the internal logic mirrors the monoidal structure.

## How It's Best Learned
Study FinVect (finite-dimensional vector spaces) with the standard dual construction. Verify triangle identities explicitly and compute traces via the dimension. Explore tangle diagrams and see how string diagrams encode morphisms in compact closed categories.

## Common Misconceptions
Compactness here refers to algebraic finite-dimensionality, not topological compactness. Duals are not unique—different dual constructions can coexist on the same category. The condition requires very specific adjoint-like relationships; failure of triangle identities indicates absence of the compact closed structure.
