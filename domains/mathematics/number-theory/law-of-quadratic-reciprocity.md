---
id: law-of-quadratic-reciprocity
title: Law of Quadratic Reciprocity
domain: mathematics
course: number-theory
prerequisites:
- id: euler-criterion
  type: hard
builds-toward:
- jacobi-symbol
tags:
- quadratic-reciprocity
- legendre-symbol
- number-theory
stage: advanced
status: draft
---

# Law of Quadratic Reciprocity

## Core Idea
For distinct odd primes p and q, (p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2). This elegant and surprising theorem is central to understanding which numbers are quadratic residues and has profound implications throughout number theory, with applications to primality testing and cryptography.

## How It's Best Learned
Study the statement with numerical examples before attempting proofs. Learn at least one proof (Gauss gave multiple). Practice computing Legendre symbols using reciprocity and supplementary laws for (−1/p) and (2/p).

## Common Misconceptions
The law is not symmetric; it gives (p/q)(q/p) = ±1, not individual reciprocity. The supplementary laws (−1/p) = (−1)^((p−1)/2) and (2/p) = (−1)^((p²−1)/8) must be applied separately. The formula does not apply to composite moduli.
