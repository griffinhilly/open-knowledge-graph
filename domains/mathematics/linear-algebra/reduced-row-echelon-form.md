---
id: reduced-row-echelon-form
title: Reduced Row Echelon Form (RREF)
domain: mathematics
course: linear-algebra
prerequisites:
- id: row-echelon-form
  type: hard
builds-toward:
- matrix-inverses
- rank-and-nullity-theorem
tags:
- rref
- reduced-row-echelon-form
- unique-form
stage: formal-systems
status: draft
---

# Reduced Row Echelon Form (RREF)

## Core Idea
Reduced row echelon form is the unique matrix form where each pivot is 1, each pivot is the only nonzero entry in its column, and pivots move strictly rightward. RREF is obtained by back-substitution after REF. The RREF of [A | I] gives A⁻¹ (when A is invertible), and RREF is the unique row-equivalent form of any matrix.

## How It's Best Learned
Compute RREF for small matrices by hand using Gaussian elimination with back-substitution. Compare RREF forms across different matrices to see the unique structure.
