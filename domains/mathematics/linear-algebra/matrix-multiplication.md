---
id: matrix-multiplication
title: Matrix Multiplication
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
- id: dot-product
  type: soft
builds-toward:
- linear-transformations
- systems-of-linear-equations
- matrix-inverses
tags:
- matrices
- multiplication
- operations
stage: formal-systems
status: validated
---

# Matrix Multiplication

## Core Idea
If A is m × n and B is n × p, their product AB is m × p where (AB)_ij = Σ_k a_ik b_kj. Matrix multiplication is associative and distributes over addition but is NOT commutative. It represents function composition for linear transformations. Multiplication is possible only when inner dimensions match.

## Questions

```yaml
- question: "Matrix A is 3×4 and matrix B is 4×2. Which of the following is correct?"
  type: multiple-choice
  options:
    - "Both AB and BA are defined, and both produce 3×2 matrices"
    - "AB is defined and produces a 3×2 matrix; BA is not defined"
    - "AB is defined and produces a 4×4 matrix; BA produces a 2×3 matrix"
    - "Neither AB nor BA is defined because the outer dimensions don't match"
  answer: 1
  explanation: "AB requires A's columns to equal B's rows: A is 3×4 and B is 4×2, so the inner dimensions both equal 4 — AB is defined and produces a 3×2 matrix. For BA, B is 4×2 and A is 3×4: B's columns (2) must equal A's rows (3), which they don't — BA is undefined. This illustrates non-commutativity concretely: even the question of whether a product is defined depends on order."

- question: "You apply transformation B to a vector, then apply transformation A to the result. Which matrix product encodes this composition?"
  type: multiple-choice
  options:
    - "The product BA, because you apply B first and A second, so B comes first in the expression"
    - "The product AB, because matrix multiplication is commutative and order doesn't matter"
    - "The product AB, because in function composition notation the rightmost matrix is applied first"
    - "You need two separate matrices; a single product cannot encode a two-step transformation"
  answer: 2
  explanation: "In matrix multiplication, the rightmost matrix is applied first — this is function composition notation. If you first apply B then A, the composition is written AB (read right-to-left: B acts first, A acts second). This is why order matters: AB and BA represent different sequences of transformations. Option A is the classic confusion — it reads left-to-right rather than following the composition convention."

- question: "Matrix multiplication is commutative: for any two square matrices A and B of the same size, AB = BA."
  type: true-false
  answer: false
  explanation: "Matrix multiplication is NOT commutative — even for square matrices of the same size, AB and BA are generally not equal. The geometric reason: applying transformation B then A typically gives a different result than applying A then B. For example, rotating then reflecting a shape is different from reflecting then rotating. This is one of the most important ways matrices differ from ordinary numbers."

- question: "If AB is defined, then BA is expected to also be defined."
  type: true-false
  answer: false
  explanation: "AB is defined when A's column count equals B's row count. If A is m×n and B is n×p, then AB is m×p. For BA to be defined, B's columns (p) must equal A's rows (m) — only guaranteed when m = p. For instance, a 2×3 matrix times a 3×5 matrix is defined (giving 2×5), but the reverse product (3×5)(2×3) requires 5 = 2, which is false — undefined."

- question: "Explain why matrix multiplication is not commutative, using the connection between matrices and linear transformations."
  type: short-answer
  answer: "Matrix multiplication represents function composition of linear transformations. Composing transformations in different orders generally produces different results — rotating an object 90° then reflecting it gives a different final orientation than reflecting first then rotating. Since AB means 'apply B first, then A,' and BA means 'apply A first, then B,' the results are generally different. The non-commutativity of matrix multiplication is simply the non-commutativity of function composition made algebraic."
  explanation: "Students often expect multiplication to commute because ordinary number multiplication does. But matrices represent operations on space, not quantities, and the order in which operations are applied changes the outcome. This is why AB = BA almost never holds unless A and B have a special relationship."
```

## Explainer

Think of matrix multiplication as a machine that transforms input vectors step by step. When you compute AB, you are asking: "first apply transformation B, then apply transformation A." The result AB is a single matrix encoding the composition of both transformations — just as composing two functions f(g(x)) gives a single combined function. This is the deepest reason matrix multiplication exists: it is function composition made computational.

The **row-column rule** — (AB)ᵢⱼ equals the dot product of row i of A with column j of B — follows directly from this composition logic. Each column of B tells you where a basis vector lands after B's transformation. Multiplying A into that column then applies A's transformation to the result. The inner dimensions must match because B's output must be a valid input for A: if B produces n-dimensional vectors, A must accept n-dimensional inputs, which means A must have n columns.

Non-commutativity is the most striking property. For numbers, ab = ba always. For matrices, AB and BA are often not equal — and often one doesn't even have defined dimensions while the other does. The geometric reason: rotating then reflecting a shape generally gives a different result than reflecting then rotating. Order matters with transformations, so order matters with matrix multiplication.

Associativity, by contrast, holds: (AB)C = A(BC). This corresponds to the fact that when you compose three transformations, it doesn't matter whether you first combine the first two or the last two — you get the same overall transformation either way. This makes long chains of matrix products unambiguous without parentheses. Combined with the dimension-matching requirement, it means you can think of a sequence of matrix multiplications as a pipeline: each matrix passes its output as input to the next, and the final product encodes the full pipeline as a single matrix.
