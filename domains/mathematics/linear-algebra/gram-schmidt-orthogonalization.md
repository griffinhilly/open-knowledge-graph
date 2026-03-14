---
id: gram-schmidt-orthogonalization
title: Gram-Schmidt Process and QR Decomposition
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonality-and-orthonormal-sets
  type: hard
builds-toward:
- orthogonal-projections-least-squares
- least-squares-approximation
tags:
- gram-schmidt
- orthogonalization
- qr-decomposition
stage: formal-systems
status: draft
---

# Gram-Schmidt Process and QR Decomposition

## Core Idea
The Gram-Schmidt process converts a linearly independent set {v₁, ..., vₖ} into an orthonormal set by iteratively projecting out previously computed directions. It produces vectors u₁, u₂, ... where uᵢ is perpendicular to all u₁, ..., uᵢ₋₁. QR decomposition writes A = QR where Q has orthonormal columns and R is upper triangular, computed via Gram-Schmidt. This is numerically superior to solving normal equations.
