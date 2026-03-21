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

## Questions

```yaml
- question: "A student wants to compute A + B where A is a 2×3 matrix and B is a 3×2 matrix. They transpose B to make it 2×3, then add entry-by-entry, reasoning that both now have the same total number of entries. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Nothing is wrong — addition is defined as long as both matrices have the same number of entries"
    - "The student should transpose A instead of B, since convention requires adding along rows"
    - "Matrix addition requires identical dimensions; transposing B creates a mathematically different matrix, and the result is not a valid sum of A and the original B"
    - "The approach is valid but inefficient — direct addition without transposing would give the same result"
  answer: 2
  explanation: "Matrix addition is defined only for matrices with identical dimensions — same number of rows AND same number of columns. Transposing B changes the matrix: the (i,j) entry of B becomes the (j,i) entry of B^T, a different mathematical object. You cannot add a 2×3 and a 3×2 by reshaping one of them; A + B is simply undefined when their dimensions don't match."

- question: "Which property does matrix addition NOT share with scalar addition?"
  type: multiple-choice
  options:
    - "Commutativity: A + B = B + A"
    - "Associativity: (A + B) + C = A + (B + C)"
    - "Existence of an additive identity: there is a matrix 0 such that A + 0 = A"
    - "Unrestricted operability: A + B is defined even when A and B have different dimensions"
  answer: 3
  explanation: "Scalar addition works for any two numbers regardless of 'dimension,' but matrix addition requires both matrices to have identical dimensions. Commutativity, associativity, and additive identity all hold for matrix addition and follow entry-by-entry from the same properties of scalar addition. The dimension requirement is an additional constraint with no scalar analogue."

- question: "Matrix addition proceeds entry-by-entry: the (i,j) entry of A + B equals a_ij + b_ij."
  type: true-false
  answer: true
  explanation: "This is the definition of matrix addition. For each position (i,j), you simply add the scalar entries at that position. This locality is what makes all algebraic properties inherit directly from scalar addition, and it makes matrix addition fundamentally different from matrix multiplication, which mixes entries across rows and columns."

- question: "Matrix multiplication, like matrix addition, is defined entry-by-entry: (AB)_ij = a_ij · b_ij."
  type: true-false
  answer: false
  explanation: "This is a critical misconception to correct before studying multiplication. Addition IS entry-by-entry, but multiplication is NOT. The (i,j) entry of AB is the dot product of row i of A with column j of B: (AB)_ij = Σ_k a_ik · b_kj. This is why multiplication requires the number of columns of A to equal the number of rows of B, and why multiplication is generally not commutative. Confusing entry-wise with dot-product is one of the most common early errors in linear algebra."

- question: "Why do m×n matrices under addition form a vector space, and what does this tell us about the relationship between matrices and vectors in ℝ^(mn)?"
  type: short-answer
  answer: "Matrix addition satisfies all vector space axioms entry-by-entry: commutativity, associativity, the zero matrix as additive identity, additive inverses (−A), and scalar multiplication by scaling each entry. These axioms hold because they hold for each scalar entry, and matrix operations apply them uniformly. An m×n matrix can be 'unrolled' into a vector of mn entries — M_{m,n} is isomorphic to ℝ^(mn) as a vector space. Matrices are vectors with entries arranged in a grid."
  explanation: "Recognizing M_{m,n} as a vector space is not just an abstraction — it enables results that treat spaces of matrices as geometric objects (measuring distance between matrices, defining linear maps between them, identifying subspaces). The simplicity of entry-wise addition makes this structure transparent, and it sets up the contrast with matrix multiplication: addition is uniform and commutative; multiplication is structural and generally noncommutative."
```

## Explainer

You already know what a matrix is: a rectangular array of entries arranged in rows and columns. Matrix addition simply applies the most natural operation you can imagine — adding the corresponding entries. If A and B are both 2 × 2 matrices, then A + B produces a new 2 × 2 matrix whose (i, j) entry is a_ij + b_ij. Think of it like adding two spreadsheets cell by cell: the value in row 1, column 2 of the result is just the sum of the values in row 1, column 2 of each input. Subtraction works the same way, replacing addition with subtraction at each position. Crucially, this operation only makes sense when both matrices have **the same dimensions** — you cannot add a 2 × 3 matrix to a 3 × 2 matrix because there is no meaningful pairing of entries.

All the familiar algebraic properties of addition carry over directly, because they hold entry by entry. **Commutativity** (A + B = B + A) follows because a_ij + b_ij = b_ij + a_ij for every entry. **Associativity** ((A + B) + C = A + (B + C)) follows for the same reason. The **zero matrix** — every entry equal to zero — acts as the additive identity, just as 0 does for numbers. And every matrix A has an additive inverse −A, formed by negating every entry, with A + (−A) = 0.

These properties are not just convenient facts — they tell you that the set of all m × n matrices forms a **vector space** M_{m,n}. If you scale a matrix by a constant c, you multiply every entry by c, satisfying the scalar multiplication axioms. The zero matrix plays the role of the zero vector. This realization is important: matrix addition is structurally identical to adding vectors in ℝⁿ, just with entries arranged in a grid rather than a column. In fact, you can always "unroll" an m × n matrix into a vector with mn entries and the algebra is the same.

Understanding matrix addition is foundational before matrix multiplication, which is far less intuitive. Multiplication does not proceed entry by entry — it mixes rows and columns in a complex way. But addition does proceed entry by entry, and that simplicity is what makes M_{m,n} a well-behaved vector space. When you encounter results about matrices as vectors later (such as linear maps between spaces of matrices), the vector space structure of M_{m,n} is what makes those results possible.
