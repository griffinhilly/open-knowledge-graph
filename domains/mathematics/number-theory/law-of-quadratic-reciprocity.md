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

## Explainer

From your study of the Euler criterion, you know that an integer a is a **quadratic residue** mod a prime p — meaning x² ≡ a (mod p) has a solution — if and only if a^((p−1)/2) ≡ 1 (mod p). The **Legendre symbol** (a/p) packages this into notation: it equals +1 if a is a nonzero quadratic residue mod p, −1 if it is a non-residue, and 0 if p | a. With this notation, Euler's criterion says (a/p) ≡ a^((p−1)/2) (mod p). The Legendre symbol is completely multiplicative: (ab/p) = (a/p)(b/p), so it behaves like a kind of arithmetic "sign."

The Law of Quadratic Reciprocity addresses a natural question: is p a square mod q, and does knowing whether q is a square mod p help? The remarkable answer is: yes, and in a precise way. For distinct odd primes p and q, the product (p/q)(q/p) equals (−1)^((p−1)/2 · (q−1)/2). Since (p−1)/2 is even when p ≡ 1 (mod 4) and odd when p ≡ 3 (mod 4), the exponent is odd only when both p and q are ≡ 3 (mod 4). In plain English: the two Legendre symbols agree — both +1 or both −1 — unless both primes are 3 mod 4, in which case they are opposite. This is not obvious; there is no elementary reason why the solvability of x² ≡ p (mod q) should have anything to do with x² ≡ q (mod p).

To use reciprocity in practice, work by reduction. Suppose you want to decide whether 137 is a square mod 401 (both prime). Compute (137/401). By reciprocity, since 137 ≡ 1 (mod 4), the product (137/401)(401/137) = 1, so (137/401) = (401/137). Now 401 ≡ 127 (mod 137), so (401/137) = (127/137). Since 127 ≡ 3 (mod 4) and 137 ≡ 1 (mod 4), reciprocity flips again: (127/137) = (137/127) = (10/127). Factor: (10/127) = (2/127)(5/127). Apply the supplementary law for 2: (2/127) = (−1)^((127²−1)/8) = (−1)^(2016) = 1. Continue with (5/127), and so on. Each step reduces the numbers; eventually you reach a trivially evaluated symbol.

This reduction process — resembling the Euclidean algorithm — is why the law is so computationally powerful. It lets you evaluate large Legendre symbols without factoring or computing modular exponentiations step-by-step. The **Jacobi symbol**, which extends the Legendre symbol to composite moduli, preserves the reciprocity law and allows even faster computation, though it no longer directly answers the quadratic residue question (a Jacobi symbol of +1 does not guarantee a solution). Gauss proved the law at least six different ways, and mathematicians continue to find new proofs because it sits at the intersection of so many areas: algebraic number theory, group theory, and later class field theory, where reciprocity generalizes to a sweeping description of abelian extensions of number fields.
