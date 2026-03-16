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

## Explainer

From your work on quadratic residues and Euler's criterion, you can already decide whether a given integer a is a square mod p: compute a^{(p-1)/2} mod p and check whether the result is 1 or -1. But this requires computing a large modular power, and it gives you no pattern for how the answer changes as p varies. The **Legendre symbol** (a/p) = ±1 packages this answer neatly, and the Law of Quadratic Reciprocity provides a powerful shortcut for computing it by reducing the problem recursively.

The reciprocity law states: for distinct odd primes p and q, **(p/q)(q/p) = (-1)^{(p-1)/2 · (q-1)/2}**. This exponent is 1 — making the product negative — only when *both* p and q are congruent to 3 mod 4; otherwise the product is 1. The practical consequence is that you can flip the symbol: to compute (p/q), replace it with ±(q/p), which may be easier because q < p or because q is a familiar number. Then apply reciprocity again, just like in the Euclidean algorithm. The computation terminates because the numbers decrease.

Two supplementary laws complete the toolkit. The **first supplementary law** says (-1/p) = (-1)^{(p-1)/2}: the symbol equals 1 if p ≡ 1 (mod 4), and -1 if p ≡ 3 (mod 4). The **second supplementary law** says (2/p) = (-1)^{(p²-1)/8}: the symbol equals 1 if p ≡ 1 or 7 (mod 8), and -1 if p ≡ 3 or 5 (mod 8). Together with the main law, these three rules let you reduce any Legendre symbol computation to a chain of flips and small residues, analogous to how the Euclidean algorithm reduces any gcd computation to a chain of divisions.

To see this in action, compute (5/13): flip by reciprocity (both ≡ 1 mod 4, so sign is +1) to get (13/5) = (3/5) since 13 ≡ 3 (mod 5). Now compute (3/5): both are odd primes with 3 ≡ 3 mod 4 and 5 ≡ 1 mod 4, so only one is ≡ 3 mod 4, meaning the exponent is 0 and the product is +1, giving (3/5) = (5/3) = (2/3). Finally (2/3): using the second supplementary law, 3 ≡ 3 (mod 8), so (2/3) = -1. Tracing back: (5/13) = -1, meaning 5 is not a quadratic residue mod 13. At no point did you compute any large powers.
