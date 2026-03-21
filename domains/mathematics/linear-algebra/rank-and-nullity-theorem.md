---
id: rank-and-nullity-theorem
title: Rank-Nullity Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: basis-and-dimension
  type: hard
builds-toward:
  - column-space
tags:
- rank
- nullity
- rank-nullity
- dimension
stage: formal-systems
status: draft
---
# Rank-Nullity Theorem

## Core Idea
For an m × n matrix A: rank(A) + nullity(A) = n, where rank is the dimension of the column space and nullity is the dimension of the null space. Rank equals the number of pivot columns in RREF. This fundamental theorem connects dimension of the domain, kernel, and image of a linear transformation.

## Questions

```yaml
- question: "A 4 × 7 matrix A has rank 3. What is the nullity of A?"
  type: multiple-choice
  options:
    - "1"
    - "3"
    - "4"
    - "7"
  answer: 2
  explanation: "The rank-nullity theorem states rank + nullity = n, where n is the number of columns. Here n = 7 and rank = 3, so nullity = 7 − 3 = 4. The 4-dimensional null space means there is a 4-dimensional subspace of ℝ⁷ that A maps entirely to zero. Note: it is tempting to use the number of rows (4), but the theorem always refers to the number of columns — the dimension of the domain."

- question: "A 5 × 5 matrix has rank 3. Which statement is true?"
  type: multiple-choice
  options:
    - "The matrix is invertible because it is square"
    - "The system Ax = 0 has only the trivial solution x = 0"
    - "The null space has dimension 2, so Ax = 0 has infinitely many solutions"
    - "The column space spans all of ℝ⁵"
  answer: 2
  explanation: "With rank = 3 and n = 5 columns, nullity = 5 − 3 = 2. A 2-dimensional null space means a whole plane of vectors maps to zero — so Ax = 0 has infinitely many solutions. A square matrix is invertible if and only if rank = n (and equivalently nullity = 0). Since rank < 5 here, the matrix is not invertible, the column space does not span all of ℝ⁵, and Ax = b may have zero or infinitely many solutions."

- question: "For a 3 × 5 matrix with rank 3, the column space spans all of ℝ³."
  type: true-false
  answer: true
  explanation: "The column space has dimension equal to rank. If rank = 3, the column space is a 3-dimensional subspace of ℝ³ — which is all of ℝ³. This means every vector in ℝ³ can be expressed as a linear combination of the matrix's columns, so the system Ax = b has at least one solution for every possible b. The null space meanwhile has dimension 5 − 3 = 2."

- question: "The rank-nullity theorem states that rank + nullity = m, where m is the number of rows of the matrix."
  type: true-false
  answer: false
  explanation: "This is a common confusion. The theorem states rank + nullity = n, where n is the number of columns — the dimension of the domain. The number of rows m is the dimension of the codomain (where outputs live), not of the domain. The columns are what the transformation acts on; the theorem accounts for how that domain dimension splits between the null space and the column space."

- question: "Explain in your own words what the rank-nullity theorem reveals about how a linear transformation handles its inputs."
  type: short-answer
  answer: "A linear transformation T: ℝⁿ → ℝᵐ takes an n-dimensional input space. The rank-nullity theorem says this input space is divided into exactly two non-overlapping parts: the null space (inputs mapped to zero, with dimension = nullity) and the part that 'survives' and contributes to the output (with dimension = rank). These two dimensions sum to exactly n — nothing is left unaccounted for."
  explanation: "The theorem is not just an equation — it reveals the structure of linear transformations. High rank means most of the input survives into the output; low rank means large portions are collapsed to zero. For a square matrix, rank = n (invertible) means nothing is collapsed; any rank deficiency creates a nontrivial null space and signals that the transformation loses information."
```

## Explainer

Every linear transformation T: ℝⁿ → ℝᵐ takes an n-dimensional space as input. The rank-nullity theorem says something elegant: that input space is divided, without overlap, between two parts — the part that collapses to zero (the null space, with dimension called **nullity**) and the part that survives and contributes to the output (the column space, with dimension called **rank**). These two dimensions must sum to exactly n, the number of columns.

Here's a concrete example. Suppose A is a 3 × 5 matrix. It maps ℝ⁵ to ℝ³. That 5-dimensional input space can't all "make it through" into a 3-dimensional output — some dimensions must collapse. If you row-reduce A and find 3 pivot columns, then rank = 3 and nullity = 2. This means the null space is 2-dimensional: there's a whole 2D plane of input vectors that A maps to zero. Conversely, if only 2 pivot columns appear, rank = 2 and nullity = 3, meaning a 3D subspace of inputs gets annihilated. You identified basis and dimension as prerequisites — rank-nullity is precisely the statement that the dimension of the domain splits between "what survives" and "what dies."

The theorem has immediate practical consequences. A square n × n matrix is invertible if and only if rank = n, which means nullity = 0: nothing maps to zero except zero itself. If rank < n for a square matrix, the null space is nontrivial and the system Ax = b has either no solutions or infinitely many. For a non-square system Ax = b with m equations and n unknowns, the theorem governs what's possible: if rank < n, solutions (if they exist) are not unique; if rank < m, some right-hand sides b cannot be achieved at all.

The pivot-counting interpretation ties everything together. Row reducing A to RREF reveals which columns are pivot columns and which are free columns. Pivot columns correspond to rank — they form a basis for the column space. Free columns, and their count equals nullity, correspond to free variables that parameterize the null space. The rank-nullity theorem is not something you verify after the fact; it's built into the structure of row reduction itself. Counting pivots and counting free variables always gives you two numbers that add up to n.
