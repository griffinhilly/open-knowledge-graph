---
id: row-echelon-form
title: Row Echelon Form and Back Substitution
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination
  type: hard
builds-toward:
- reduced-row-echelon-form
tags:
- systems
- row echelon form
- matrices
stage: formal-systems
status: draft
---

# Row Echelon Form and Back Substitution

## Core Idea
A matrix is in row echelon form if non-zero rows appear before zero rows and each non-zero row has a leading (pivot) entry to the right of the pivot above. REF allows back-substitution to find solutions. Pivot columns identify basic variables; non-pivot columns identify free variables.
