---
id: row-echelon-form
title: Row Echelon Form (REF)
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination
  type: hard
builds-toward:
- reduced-row-echelon-form
- rank-and-nullity-theorem
tags:
- row-echelon-form
- ref
- matrix-form
stage: formal-systems
status: draft
---

# Row Echelon Form (REF)

## Core Idea
Row echelon form is a matrix structure where all nonzero rows are above zero rows, and the leading entry (pivot) in each nonzero row is to the right of the pivot above it. REF is obtained by Gaussian elimination and reveals the rank of a matrix and the solution structure of Ax = b.
