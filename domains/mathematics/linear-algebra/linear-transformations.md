---
id: linear-transformations
title: Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
- id: matrices-intro
  type: soft
builds-toward:
- matrix-representation-linear-transformations
- composition-linear-transformations
- eigenvalues-and-eigenvectors
tags:
- linear-transformations
- functions
- preserves-structure
stage: formal-systems
status: draft
---

# Linear Transformations

## Core Idea
A linear transformation T: Rⁿ → Rᵐ satisfies T(cu + v) = cT(u) + T(v) for all scalars c and vectors u, v. Linear transformations preserve vector addition and scalar multiplication, making them algebraic homomorphisms. Every linear transformation is represented by a unique matrix A such that T(x) = Ax.
