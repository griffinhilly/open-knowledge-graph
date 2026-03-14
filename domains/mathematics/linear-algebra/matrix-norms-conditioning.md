---
id: matrix-norms-conditioning
title: Matrix Norms and Condition Numbers
domain: mathematics
course: linear-algebra
prerequisites:
- id: singular-value-decomposition
  type: hard
- id: vector-norms
  type: hard
builds-toward:
- iterative-methods-linear-systems
tags:
- matrix-norms
- conditioning
- numerical-stability
stage: formal-systems
status: draft
---

# Matrix Norms and Condition Numbers

## Core Idea
Matrix norms measure matrix size; common ones are the operator norm ||A||₂ = σ_max(A), Frobenius norm ||A||_F = √(Σᵢⱼ Aᵢⱼ²), and max norm ||A||_∞. The condition number κ(A) = ||A|| ||A⁻¹|| quantifies sensitivity of Ax = b to perturbations: small relative errors in b lead to large relative errors in x when κ is large. κ = σ_max/σ_min for SVD.
