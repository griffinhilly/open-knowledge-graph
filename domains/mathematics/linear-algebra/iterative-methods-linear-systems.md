---
id: iterative-methods-linear-systems
title: Iterative Methods for Linear Systems
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-norms-conditioning
  type: soft
builds-toward:
- applications-linear-algebra-modeling
tags:
- iterative-methods
- jacobi
- gauss-seidel
stage: formal-systems
status: draft
---

# Iterative Methods for Linear Systems

## Core Idea
Iterative methods like Jacobi and Gauss-Seidel solve Ax = b as a fixed-point iteration x^(k+1) = (I − D⁻¹A)x^(k) + D⁻¹b. They converge when ||I − D⁻¹A|| < 1 and are useful for sparse or large systems. Convergence rate depends on spectral radius. Conjugate gradient (CG) converges faster for symmetric positive definite matrices.
