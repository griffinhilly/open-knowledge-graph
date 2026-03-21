---
id: matrix-addition-multiplication
title: Matrix Addition, Multiplication, and Transpose
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-intro
  type: hard
builds-toward:
- linear-transformations-definition
- matrix-inverses-computation
- determinant-computation
tags:
- matrices
- operations
- algebra
stage: formal-systems
status: draft
---

# Matrix Addition, Multiplication, and Transpose

## Core Idea
Matrices are rectangular arrays of numbers. Matrix addition/subtraction works entry-wise, while multiplication of an (m×p) matrix A by a (p×n) matrix B produces an (m×n) matrix with entries (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ. The transpose Aᵀ swaps rows and columns. These operations do not all commute, and matrix algebra is noncommutative.

## How It's Best Learned
Practice small 2×2 and 2×3 multiplications by hand to develop intuition. Verify that AB ≠ BA with numerical examples. Connect matrix multiplication to composition of linear transformations.

## Common Misconceptions
Matrix multiplication is not entry-wise. (AB)ᵢⱼ is a dot product of row i of A with column j of B, not a simple product. AB and BA are different and both may not even be defined.

## Questions

```yaml
- question: "A student computes AB for A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]] by multiplying entry-by-entry, getting [[5, 12], [21, 32]]. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Nothing — entry-wise multiplication is correct for square matrices of the same size"
    - "The student should have transposed B before multiplying"
    - "Matrix multiplication is NOT entry-wise: (AB)₁₁ = row 1 of A · column 1 of B = 1·5 + 2·7 = 19, not 5. Each entry is a dot product, not a simple product."
    - "The student used the wrong indices — they should start with row 2"
  answer: 2
  explanation: "Matrix multiplication uses dot products: (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ. For the (1,1) entry: 1·5 + 2·7 = 19. Entry-wise multiplication is only defined for the Hadamard product, which is a separate operation not usually called 'matrix multiplication.' The correct product AB = [[19, 22], [43, 50]]. Confusing entry-wise multiplication with matrix multiplication is the most common error in linear algebra."

- question: "Matrix A is 2×3 and matrix B is 3×4. A student claims both AB and BA are defined. Are they correct?"
  type: multiple-choice
  options:
    - "Yes — whenever one product is defined, the reverse product is always defined too"
    - "No — AB is 2×4 (inner dimensions match: 3=3), but BA would require a 4×3 times a 2×3, and 3 ≠ 2, so BA is undefined"
    - "Yes — matrix multiplication is always defined for any two rectangular matrices"
    - "No — neither product is defined unless both matrices are square"
  answer: 1
  explanation: "For AB, the inner dimensions must match: A is (2×3) and B is (3×4), so the '3' inner dimensions agree and AB is defined as a (2×4) matrix. For BA, we need B (3×4) times A (2×3): B has 4 columns and A has 2 rows — 4 ≠ 2, so BA is undefined. This illustrates both the dimension rule and non-commutativity: even when AB is defined, BA may not be."

- question: "For any two matrices A and B where both AB and BA are defined and have the same dimensions, it is generally the case that AB ≠ BA."
  type: true-false
  answer: true
  explanation: "Matrix multiplication is non-commutative. Even for square matrices of the same size where both products are always defined, AB and BA are typically different. A simple 2×2 example: A = [[1,1],[0,1]], B = [[1,0],[1,1]]; AB = [[2,1],[1,1]], BA = [[1,1],[1,2]]. Commutativity is the exception (e.g., A and its inverse, or diagonal matrices), not the rule. This non-commutativity is physically meaningful: the order in which transformations are applied generally matters."

- question: "The transpose of a matrix product satisfies (AB)ᵀ = AᵀBᵀ."
  type: true-false
  answer: false
  explanation: "The correct rule is (AB)ᵀ = BᵀAᵀ — the order is *reversed*. This is analogous to reversing operations: if you first apply A then B, the transpose operation inverts both and reverses the order. Using AᵀBᵀ is a common error. A quick check with 2×2 matrices confirms the reversal. The same reversal applies to larger chains: (ABC)ᵀ = CᵀBᵀAᵀ."

- question: "Why is the non-commutativity of matrix multiplication not a mathematical defect but a meaningful and necessary property? What kind of real-world operation does it reflect?"
  type: short-answer
  answer: "Non-commutativity reflects the fact that many sequential actions depend on order. Rotating an object 90° clockwise then flipping it produces a different result than flipping first then rotating — the final orientations differ. Matrix multiplication models the composition of linear transformations, and composing transformations in different orders generally produces different outcomes. If AB always equaled BA, matrix multiplication could not correctly model this order-dependence and would be useless for describing sequential operations in geometry, physics, and computation."
  explanation: "The deeper point is that commutativity would be a special property, not the default. Groups of transformations in physics (rotation groups, symmetry groups) are generally non-abelian — non-commutativity is the norm in the mathematics that describes physical symmetry. Matrix multiplication is the right tool precisely because it inherits this non-commutativity."
```

## Explainer

You already know that a matrix is a rectangular array of numbers. Now consider that you might want to combine two matrices — perhaps to represent two transformations applied in sequence, or simply to add quantities organized in tabular form. **Matrix addition** is the straightforward case: if A and B have the same dimensions, you add them entry-by-entry. (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ. Think of adding two spreadsheets cell by cell. The same-dimension requirement is the only constraint, and the operation inherits all the familiar arithmetic properties — commutativity, associativity — from ordinary addition.

**Matrix multiplication** is the consequential operation, and it works nothing like addition. The product AB multiplies the i-th row of A by the j-th column of B using a **dot product**: (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ. For this to be defined, the number of columns in A must equal the number of rows in B. An (m × p) matrix times a (p × n) matrix produces an (m × n) matrix — the inner dimensions p must match and the outer dimensions m, n survive. The reason for this rule becomes clear when you think about what multiplication will later be shown to represent: applying one linear transformation followed by another. Composing a transformation from ℝᵖ → ℝᵐ with one from ℝⁿ → ℝᵖ produces a transformation from ℝⁿ → ℝᵐ.

The most important property to internalize is **non-commutativity**: in general, AB ≠ BA. Sometimes one product is defined and the other is not (if A is 2×3 and B is 3×4, then AB is 2×4, but BA requires a 4×3 times a 2×3 — impossible). Even when both are defined and square, the results typically differ. Think of the physical analogy: rotating an object and then flipping it produces a different orientation than flipping first and then rotating. Matrix multiplication encodes this kind of ordered sequential action.

The **transpose** operation Aᵀ swaps rows and columns: (Aᵀ)ᵢⱼ = Aⱼᵢ. It converts an m×n matrix into an n×m matrix. A key identity is that transposing a product reverses the order: (AB)ᵀ = BᵀAᵀ. This reversal matters — it is not AᵀBᵀ. Symmetric matrices, where Aᵀ = A, play a special role throughout linear algebra, and the transpose appears constantly in formulas for projections, least squares, and quadratic forms. Mastering these three operations — addition, multiplication, and transpose — is the prerequisite for every matrix computation that follows.
