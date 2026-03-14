---
id: singular-value-decomposition
title: Singular Value Decomposition (SVD)
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices-properties
  type: hard
builds-toward:
- least-squares-approximation
- matrix-norms-conditioning
tags:
- SVD
- singular-values
- decomposition
stage: formal-systems
status: draft
---

# Singular Value Decomposition (SVD)

## Core Idea
Every m×n matrix A can be written as A = UΣVᵀ where U and V are orthogonal and Σ is diagonal with singular values σ₁ ≥ σ₂ ≥ ... ≥ 0. Singular values are square roots of eigenvalues of AᵀA or AAᵀ. SVD reveals the rank, condition number, and principal directions of A. It is the most general and numerically stable decomposition.
