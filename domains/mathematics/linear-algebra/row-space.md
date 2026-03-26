---
id: row-space
title: The Row Space of a Matrix
domain: mathematics
course: linear-algebra
prerequisites:
- id: column-space
  type: hard
- id: matrix-transpose
  type: soft
builds-toward:
- rank-nullity-theorem
tags:
- row space
- row operations
- RREF rows
- orthogonal complement
- rank
stage: formal-systems
status: validated
---

# The Row Space of a Matrix

## Core Idea
The row space of an m×n matrix A is the span of its row vectors, forming a subspace of Rⁿ. Unlike the column space, the row space IS preserved by elementary row operations, so a basis for the row space can be read directly as the nonzero rows of any row echelon form of A. The dimension of the row space equals the rank of A, confirming that row rank equals column rank — a foundational theorem. The row space and null space of A are orthogonal complements in Rⁿ: every vector in Rⁿ can be uniquely written as the sum of a row-space component and a null-space component.

## How It's Best Learned
Row-reduce A to REF and identify the nonzero rows as a row-space basis. Then verify the rank matches the column rank found from Col(A). Use the orthogonality relationship Nul(A) ⊥ Row(A) to geometrically motivate least squares.

## Common Misconceptions
- Row operations DO preserve the row space (unlike the column space, which row operations change).
- Students assume the row space of A equals the column space of A — they are subspaces of different spaces (Rⁿ vs Rᵐ) and equal only when m = n and A is symmetric.
- The row space basis comes from the RREF rows of A, while the column space basis comes from pivot columns of the ORIGINAL A.

## Questions

```yaml
- question: "After row-reducing a matrix A to RREF, a student uses the pivot columns of RREF as her column-space basis and the nonzero rows of RREF as her row-space basis. What is wrong with this procedure?"
  type: multiple-choice
  options:
    - "Both procedures are wrong — you must use the original matrix A for both bases"
    - "The column-space basis must come from the pivot columns of the ORIGINAL A, not the RREF; the row-space basis from the nonzero rows of RREF is correct"
    - "Both procedures are correct"
    - "The row-space basis must also come from the original matrix A, not the RREF"
  answer: 1
  explanation: "Row operations preserve the row space but change the column space. This creates an asymmetry: the nonzero rows of any row echelon form directly give a basis for the row space (because row operations produce only linear combinations of the original rows). But row operations alter the column directions, so you must identify pivot columns in the RREF to find which columns of the ORIGINAL A form a column-space basis. Using RREF columns for the column space is the classic error."

- question: "A vector x satisfies Ax = 0 (i.e., x is in the null space of A). What is the geometric relationship between x and every vector in the row space of A?"
  type: multiple-choice
  options:
    - "x is parallel to every vector in the row space"
    - "x is orthogonal to every vector in the row space"
    - "x has the same dimension as the row space"
    - "x must be the zero vector"
  answer: 1
  explanation: "If Ax = 0, then every row of A dotted with x equals zero (since Ax computes exactly those dot products). This means x is perpendicular to every row vector of A, and therefore perpendicular to every linear combination of rows — i.e., every vector in the row space. The null space Nul(A) and the row space Row(A) are orthogonal complements in Rⁿ, with their dimensions summing to n by the rank-nullity theorem."

- question: "Elementary row operations preserve the row space of a matrix but generally change its column space."
  type: true-false
  answer: true
  explanation: "Each row operation (swap, scale, add a multiple of one row to another) produces rows that are linear combinations of the original rows. So the span of the rows — the row space — is unchanged. The column directions, however, are typically altered: adding a multiple of one row to another changes the entries in each column, so the column vectors in the RREF are generally different from those in the original A. This asymmetry is why the two bases are found by different procedures."

- question: "For an m×n matrix A, the row space and the column space are subspaces of the same vector space."
  type: true-false
  answer: false
  explanation: "The row space Row(A) is a subspace of Rⁿ (since each row has n entries), while the column space Col(A) is a subspace of Rᵐ (since each column has m entries). They live in different ambient spaces unless m = n. Despite this, they always have the same dimension — the rank of A — which is the surprising content of the theorem that row rank equals column rank."

- question: "Explain why row rank equals column rank, and why this equality is surprising."
  type: short-answer
  answer: "The rank of A counts the number of nonzero rows in any echelon form, which equals the number of pivot positions. But the number of pivot positions also equals the number of pivot columns — hence the number of linearly independent columns. So row rank (dimension of the row space) and column rank (dimension of the column space) both equal the number of pivots. The surprise is that these two spaces live in different ambient spaces — Rⁿ and Rᵐ respectively — yet always have the same dimension. There is no obvious geometric reason why compressing m-dimensional column information and n-dimensional row information should yield the same count."
  explanation: "The proof goes through the fact that row reduction counts the same thing from both perspectives: the pivots mark both the independent rows and the independent columns simultaneously. The equality breaks symmetry in a deep way — it says that no matter how rectangular A is, its 'row complexity' and 'column complexity' are identical numbers, reflecting the same underlying rank."
```

## Explainer

You already know that the column space Col(A) is the span of the columns of A — the set of all vectors Ax as x ranges over Rⁿ. The **row space** Row(A) is the analogous object for rows: the span of the row vectors of A, which lives in Rⁿ since each row has n entries. Where the column space asks "which vectors in Rᵐ can A produce?", the row space asks "what linear combinations of the rows of A form this subspace of Rⁿ?" Both are subspaces associated with A, but they live in different ambient spaces and are found by different procedures.

The critical asymmetry is one you need to internalize carefully. From your work with column space, you know that elementary row operations change the column space — you must find pivot columns in the original A, not in the reduced form. The row space is the opposite: **row operations preserve the row space**. This is because each row operation (swap two rows, scale a row, add a multiple of one row to another) produces rows that are still linear combinations of the original rows — no new row directions are created or destroyed. So after row reducing A to echelon form, the nonzero rows directly give a basis for the row space. The rule is: row-space basis from the reduced form, column-space basis from the original.

There is a deep geometric relationship between the row space and the null space. Every vector x in Nul(A) satisfies Ax = 0, which means every row of A is orthogonal to x — each row dotted with x equals zero. Consequently, **Nul(A) ⊥ Row(A)**: the null space and row space are orthogonal complements in Rⁿ. Their dimensions add to n (by the rank-nullity theorem), and every vector in Rⁿ decomposes uniquely into a row-space component and a null-space component. This decomposition is the foundation for least squares: the "best" solution to Ax = b lives in the row space of A, and the error is in the null space.

Finally, consider what these two subspaces reveal about rank. The number of nonzero rows in the echelon form counts the dimension of Row(A). The number of pivot columns counts the dimension of Col(A). These are the same number — the rank of A. This means **row rank equals column rank**, despite the two spaces living in different ambient spaces (Rⁿ and Rᵐ respectively). Both count the same thing: the number of truly independent constraints or directions in A. The equality of row and column rank is one of the more surprising theorems of linear algebra, and the row space is essential for understanding why it holds.
