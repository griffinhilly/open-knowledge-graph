---
id: matrix-addition-subtraction
title: Matrix Addition and Subtraction
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
builds-toward:
- matrix-multiplication
- matrix-transpose
tags:
- matrices
- operations
- addition
stage: formal-systems
status: draft
---

# Matrix Addition and Subtraction

## Core Idea
Two matrices of the same size are added/subtracted entry-wise: (A + B)_ij = a_ij + b_ij. Matrix addition is commutative, associative, and has an identity (the zero matrix). These operations make m × n matrices into a vector space themselves, denoted M_{m,n}.

## Explainer

You already know what a matrix is: a rectangular array of entries arranged in rows and columns. Matrix addition simply applies the most natural operation you can imagine — adding the corresponding entries. If A and B are both 2 × 2 matrices, then A + B produces a new 2 × 2 matrix whose (i, j) entry is a_ij + b_ij. Think of it like adding two spreadsheets cell by cell: the value in row 1, column 2 of the result is just the sum of the values in row 1, column 2 of each input. Subtraction works the same way, replacing addition with subtraction at each position. Crucially, this operation only makes sense when both matrices have **the same dimensions** — you cannot add a 2 × 3 matrix to a 3 × 2 matrix because there is no meaningful pairing of entries.

All the familiar algebraic properties of addition carry over directly, because they hold entry by entry. **Commutativity** (A + B = B + A) follows because a_ij + b_ij = b_ij + a_ij for every entry. **Associativity** ((A + B) + C = A + (B + C)) follows for the same reason. The **zero matrix** — every entry equal to zero — acts as the additive identity, just as 0 does for numbers. And every matrix A has an additive inverse −A, formed by negating every entry, with A + (−A) = 0.

These properties are not just convenient facts — they tell you that the set of all m × n matrices forms a **vector space** M_{m,n}. If you scale a matrix by a constant c, you multiply every entry by c, satisfying the scalar multiplication axioms. The zero matrix plays the role of the zero vector. This realization is important: matrix addition is structurally identical to adding vectors in ℝⁿ, just with entries arranged in a grid rather than a column. In fact, you can always "unroll" an m × n matrix into a vector with mn entries and the algebra is the same.

Understanding matrix addition is foundational before matrix multiplication, which is far less intuitive. Multiplication does not proceed entry by entry — it mixes rows and columns in a complex way. But addition does proceed entry by entry, and that simplicity is what makes M_{m,n} a well-behaved vector space. When you encounter results about matrices as vectors later (such as linear maps between spaces of matrices), the vector space structure of M_{m,n} is what makes those results possible.
