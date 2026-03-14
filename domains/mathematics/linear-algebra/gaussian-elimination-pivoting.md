---
id: gaussian-elimination-pivoting
title: Gaussian Elimination with Partial Pivoting
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination-method
  type: hard
builds-toward:
- lu-decomposition-numerical
- matrix-norms-conditioning
tags:
- numerical-stability
- pivoting
- gaussian-elimination
stage: formal-systems
status: draft
---

# Gaussian Elimination with Partial Pivoting

## Core Idea
Partial pivoting swaps rows to place the largest entry in the pivot position before elimination, reducing rounding errors in floating-point arithmetic. Without pivoting, small pivots can amplify errors in subsequent operations. Pivoting is essential for numerical stability and is standard in computational practice.
