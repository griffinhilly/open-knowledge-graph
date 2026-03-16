---
id: reduced-row-echelon-form
title: Reduced Row Echelon Form
domain: mathematics
course: linear-algebra
prerequisites:
- id: row-echelon-form
  type: hard
builds-toward:
- rank-nullity-theorem
tags:
- systems
- rref
- normal form
stage: formal-systems
status: draft
---

# Reduced Row Echelon Form

## Core Idea
Reduced row echelon form (RREF) is the unique simplest form where: matrix is in REF, all pivots equal 1, and all entries above and below pivots are zero. RREF reveals solutions directly with no back-substitution. Every matrix has a unique RREF, which determines rank and solution structure.

## Explainer

You already know row echelon form (REF): zeros below each pivot, with each pivot to the right of the one above it. REF simplified your system enough that you could use back-substitution to read off the solution. **Reduced row echelon form (RREF)** takes the same process one step further by also eliminating all entries *above* each pivot, then scaling each pivot to 1. The result is a form so simple that you can read solutions off directly, with no back-substitution required.

In RREF, each pivot column has exactly one nonzero entry: the pivot itself, which equals 1. All other entries in that column are 0. This means each **free variable** (corresponding to a non-pivot column) can be assigned any value, while each **basic variable** (corresponding to a pivot column) is then determined uniquely in terms of those free variables. The solution structure is fully exposed: the number of pivots is the rank, the number of non-pivot columns (free variables) is the nullity, and the relationship rank + nullity = n is manifest in the RREF.

The most important property of RREF is uniqueness: every matrix has exactly one RREF, regardless of which row operations you used to reach it. This is not true of REF — you can produce many different REFs for the same matrix depending on the sequence of operations. This uniqueness makes RREF a **canonical form**: two matrices have the same RREF if and only if they represent equivalent systems (the same solution set). In practice, RREF is the final state you are aiming for in Gauss-Jordan elimination, and it makes the solution structure completely transparent.
