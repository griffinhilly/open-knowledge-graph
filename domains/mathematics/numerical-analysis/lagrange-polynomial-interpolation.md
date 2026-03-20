---
id: lagrange-polynomial-interpolation
title: Lagrange Polynomial Interpolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: polynomial-rings
  type: soft
builds-toward:
- newton-divided-differences
- interpolation-error-analysis
tags:
- interpolation
- polynomials
- lagrange
stage: advanced
status: draft
---

# Lagrange Polynomial Interpolation

## Core Idea
Given n+1 distinct points (x_i, y_i), Lagrange interpolation constructs the unique polynomial of degree ≤n passing through all points using L_i(x) = ∏_{j≠i} (x - x_j)/(x_i - x_j). The Lagrange form P(x) = Σ y_i L_i(x) is elegant and explicit but becomes numerically unstable when adding new points since all basis functions must be recomputed.
