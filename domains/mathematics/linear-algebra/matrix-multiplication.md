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
