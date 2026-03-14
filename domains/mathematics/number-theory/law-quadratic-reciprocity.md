---
id: law-quadratic-reciprocity
title: Law of Quadratic Reciprocity
domain: mathematics
course: number-theory
prerequisites:
- id: eulers-criterion
  type: hard
- id: quadratic-residues-legendre-symbol
  type: hard
builds-toward:
- jacobi-symbol
tags:
- reciprocity
- quadratic-residues
- legendre-symbol
stage: advanced
status: draft
---

# Law of Quadratic Reciprocity

## Core Idea
For distinct odd primes p and q: (p/q)(q/p) = (-1)^((p-1)(q-1)/4). Combined with supplementary laws for (-1/p) and (2/p), it enables efficient Legendre symbol computation and is central to number theory.

## How It's Best Learned
Prove a special case (e.g., p=3, q=5) to understand the counting argument. Use it to compute (a/p) without explicit square-root verification.

## Common Misconceptions
Forgetting supplementary laws for (-1/p) and (2/p). Misremembering the sign in the reciprocity formula.
