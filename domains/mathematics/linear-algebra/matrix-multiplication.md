---
id: matrix-multiplication
title: Matrix Multiplication
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
- id: dot-product-definition
  type: soft
builds-toward:
- linear-transformation-definition
- systems-of-linear-equations
- matrix-inverses
tags:
- matrices
- multiplication
- operations
stage: formal-systems
status: draft
---

# Matrix Multiplication

## Core Idea
If A is m × n and B is n × p, their product AB is m × p where (AB)_ij = Σ_k a_ik b_kj. Matrix multiplication is associative and distributes over addition but is NOT commutative. It represents function composition for linear transformations. Multiplication is possible only when inner dimensions match.

## Explainer

Think of matrix multiplication as a machine that transforms input vectors step by step. When you compute AB, you are asking: "first apply transformation B, then apply transformation A." The result AB is a single matrix encoding the composition of both transformations — just as composing two functions f(g(x)) gives a single combined function. This is the deepest reason matrix multiplication exists: it is function composition made computational.

The **row-column rule** — (AB)ᵢⱼ equals the dot product of row i of A with column j of B — follows directly from this composition logic. Each column of B tells you where a basis vector lands after B's transformation. Multiplying A into that column then applies A's transformation to the result. The inner dimensions must match because B's output must be a valid input for A: if B produces n-dimensional vectors, A must accept n-dimensional inputs, which means A must have n columns.

Non-commutativity is the most striking property. For numbers, ab = ba always. For matrices, AB and BA are often not equal — and often one doesn't even have defined dimensions while the other does. The geometric reason: rotating then reflecting a shape generally gives a different result than reflecting then rotating. Order matters with transformations, so order matters with matrix multiplication.

Associativity, by contrast, holds: (AB)C = A(BC). This corresponds to the fact that when you compose three transformations, it doesn't matter whether you first combine the first two or the last two — you get the same overall transformation either way. This makes long chains of matrix products unambiguous without parentheses. Combined with the dimension-matching requirement, it means you can think of a sequence of matrix multiplications as a pipeline: each matrix passes its output as input to the next, and the final product encodes the full pipeline as a single matrix.
