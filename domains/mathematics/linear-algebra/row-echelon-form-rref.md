---
id: row-echelon-form-rref
title: Row Echelon Form and Reduced Row Echelon Form
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination-method
  type: hard
builds-toward:
- rank-nullity-theorem
- basis-and-dimension
- vector-subspaces
tags:
- RREF
- row-reduction
- normal-form
stage: formal-systems
status: draft
---

# Row Echelon Form and Reduced Row Echelon Form

## Core Idea
Row echelon form (REF) has leading entries (pivots) forming a staircase pattern with zeros below. Reduced row echelon form (RREF) refines this: each pivot is 1, and zeros appear above and below pivots. RREF is unique for a given matrix and reveals rank, pivot columns (basis for column space), free variables (basis for null space), and solutions directly.
