---
id: linear-systems-notation
title: 'Linear Systems: Notation and Solution Existence'
domain: mathematics
course: linear-algebra
prerequisites:
- id: systems-of-three-variables
  type: hard
- id: matrices-intro
  type: hard
builds-toward:
- gaussian-elimination-method
- rank-nullity-theorem
- linear-systems-consistency
tags:
- systems
- Ax=b
- notation
- existence
stage: formal-systems
status: draft
---

# Linear Systems: Notation and Solution Existence

## Core Idea
A system of m linear equations in n unknowns is written as Ax = b, where A is m×n, x is the unknown vector, and b is the right-hand side. Solutions exist if and only if b is in the column space of A. The solution set is either empty, a single point, or an affine subspace (infinite solutions). Augmented matrices [A | b] encode the system compactly.
