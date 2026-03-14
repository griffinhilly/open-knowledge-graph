---
id: jacobi-symbol
title: The Jacobi Symbol
domain: mathematics
course: number-theory
prerequisites:
- id: law-quadratic-reciprocity
  type: hard
tags:
- jacobi-symbol
- quadratic-reciprocity
- composite-moduli
stage: advanced
status: draft
---

# The Jacobi Symbol

## Core Idea
The Jacobi symbol (a/n) extends the Legendre symbol to composite odd n via the Chinese Remainder Theorem: (a/n) = ∏(a/p_i)^(e_i) for n = ∏p_i^(e_i). While not a direct residuosity test, it satisfies quadratic reciprocity and is efficient to compute.
