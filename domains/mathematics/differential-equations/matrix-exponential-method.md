---
id: matrix-exponential-method
title: Matrix Exponential Method for Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- stability-classification
tags:
- systems
- method
- matrix-exponential
stage: advanced
status: draft
---

# Matrix Exponential Method for Systems

## Core Idea
For the homogeneous system y' = Ay with constant matrix A, the solution is y(t) = e^{At}y₀, where e^{At} is the matrix exponential. When A is diagonalizable, e^{At} = Pe^{Λt}P⁻¹, making the solution explicit in terms of eigenvalues and eigenvectors.

## How It's Best Learned
Compute matrix exponentials for 2×2 systems with distinct real eigenvalues, then handle complex eigenvalues. Verify solutions by differentiating e^{At}y₀ directly.
