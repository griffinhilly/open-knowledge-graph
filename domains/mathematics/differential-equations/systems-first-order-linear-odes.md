---
id: systems-first-order-linear-odes
title: Systems of First-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: matrix-operations
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- matrix-exponential-method
- phase-portraits-linear-systems
tags:
- systems
- matrix-form
- fundamental
stage: advanced
status: draft
---

# Systems of First-Order Linear Differential Equations

## Core Idea
A system dx/dt = Ax + f(t) in matrix form unifies high-order and coupled equations. The homogeneous solution x_h uses eigenvalues λ and eigenvectors v of A: x_h = Σ cᵢe^(λᵢt)vᵢ. Complex eigenvalues give oscillatory components; repeated eigenvalues require generalized eigenvectors. Systems are more general than high-order equations but reveal structure through linear algebra.
