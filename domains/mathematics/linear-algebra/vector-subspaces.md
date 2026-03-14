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
