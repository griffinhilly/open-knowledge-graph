---
id: cramers-rule
title: Cramer's Rule for Solving Systems
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-properties
  type: hard
- id: systems-of-linear-equations
  type: hard
tags:
- systems
- cramers rule
- determinants
stage: formal-systems
status: draft
---

# Cramer's Rule for Solving Systems

## Core Idea
For a square system Ax = b with det(A) ≠ 0, Cramer's rule gives x_i = det(A_i) / det(A), where A_i is A with column i replaced by b. This provides an explicit formula for solutions but is computationally inefficient compared to Gaussian elimination.
