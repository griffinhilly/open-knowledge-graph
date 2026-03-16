---
id: vector-subspaces
title: Subspaces and Closure Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces-definition
  type: hard
builds-toward:
- span-spanning-set
- basis-definition
- dimension-vector-space
tags:
- subspaces
- closure
- subsets
stage: formal-systems
status: draft
---

# Subspaces and Closure Properties

## Core Idea
A subspace of a vector space V is a non-empty subset W that is closed under addition and scalar multiplication. Equivalently, W is a subspace if and only if for any u, v in W and scalar c, we have u + v and cu in W. Subspaces inherit all vector space properties from V.

## How It's Best Learned
Start with geometric examples: lines and planes through the origin in R^3 are subspaces. Test the closure conditions explicitly. Practice with null spaces and column spaces of matrices.

## Common Misconceptions
- Forgetting that subspaces must contain the zero vector.
- Thinking lines or planes not through the origin are subspaces; they are affine subsets, not subspaces.

## Explainer

From your study of vector spaces, you know that a vector space comes with two operations — addition and scalar multiplication — and a list of axioms that govern them. A **subspace** is a subset of a vector space that is itself a vector space under the same operations. Instead of checking all eight or ten axioms from scratch, there is a shortcut: a non-empty subset W of a vector space V is a subspace if and only if it is **closed under addition** (u + v ∈ W whenever u, v ∈ W) and **closed under scalar multiplication** (cu ∈ W whenever c is a scalar and u ∈ W). Both conditions together force W to be a vector space in its own right.

The geometric picture in ℝ³ is the most direct way to build intuition. A line through the origin is a subspace: stretch or shrink any vector on the line and you stay on the line; add two vectors on the line and you stay on the line. A plane through the origin is likewise a subspace for the same reasons. But a line or plane that does NOT pass through the origin fails immediately — add the zero vector to any element and you leave the set (unless the set contains the zero vector, which an off-origin line doesn't). This is the key diagnostic: **every subspace must contain the zero vector**. If your candidate set doesn't, it's not a subspace.

Two of the most important subspaces attached to a matrix A are the **column space** and the **null space**. The column space (or image) of A is the set of all vectors of the form Ax — it's a subspace of the output space. The null space (or kernel) of A is the set of all x with Ax = 0 — it's a subspace of the input space. Both are worth checking against the two closure conditions as an exercise; they will become central objects when you study span, basis, and dimension, since a central theorem (the rank-nullity theorem) quantifies how these two subspaces divide up the total space.

When you test whether a given set is a subspace, work methodically: first verify the zero vector is present, then check both closure conditions with arbitrary elements. If any condition fails, you have found a counterexample. If all conditions hold, you have a subspace. This two-condition test is one of the first genuinely efficient theorems in linear algebra — it collapses what could be a ten-axiom verification into two checks.
