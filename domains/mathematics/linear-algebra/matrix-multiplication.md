---
id: matrix-multiplication
title: Matrix Multiplication
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-addition-subtraction
  type: hard
- id: dot-product
  type: hard
builds-toward:
- matrix-transpose
- linear-transformations
- matrix-representation-linear-transformations
- determinants-2x2-3x3
tags:
- matrix-multiplication
- composition
- linear-transformations
stage: formal-systems
status: draft
---

# Matrix Multiplication

## Core Idea
The product of an m × p matrix A and a p × n matrix B is an m × n matrix C where cᵢⱼ = Σₖ aᵢₖ bₖⱼ (row of A dotted with column of B). Matrix multiplication is associative but not commutative. It represents composition of linear transformations and has deep geometric meaning.
