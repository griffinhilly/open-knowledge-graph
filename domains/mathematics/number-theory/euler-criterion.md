---
id: euler-criterion
title: Euler's Criterion for Quadratic Residues
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-and-legendre-symbol
  type: hard
- id: fermat-little-theorem
  type: soft
builds-toward:
- law-of-quadratic-reciprocity
tags:
- quadratic-residues
- legendre-symbol
- fermat-little-theorem
stage: advanced
status: draft
---

# Euler's Criterion for Quadratic Residues

## Core Idea
Euler's criterion states that a^((p−1)/2) ≡ (a/p) (mod p) for odd prime p and integer a. This provides an efficient computational method to evaluate the Legendre symbol and connects Fermat's Little Theorem to quadratic character theory.

## Explainer

Your prerequisites give you two key tools. The **Legendre symbol** (a/p) tells you whether a is a quadratic residue mod p: it equals 1 if a ≡ b² (mod p) for some b, −1 if no such b exists, and 0 if p divides a. **Fermat's Little Theorem** says a^(p−1) ≡ 1 (mod p) whenever gcd(a, p) = 1. Euler's criterion connects these two results through a single computation.

The key observation is that a^((p−1)/2) is a square root of a^(p−1) ≡ 1 (mod p). The only square roots of 1 modulo a prime are 1 and −1 (since x²≡1 means p | (x−1)(x+1), forcing x≡1 or x≡−1). So a^((p−1)/2) must be either 1 or −1 mod p. The criterion asserts the value matches the Legendre symbol exactly: +1 when a is a quadratic residue, −1 when it is a non-residue.

To see why the residue case works: if a ≡ b² (mod p), then a^((p−1)/2) ≡ b^(p−1) ≡ 1 (mod p) by Fermat's Little Theorem. For non-residues, the argument uses the fact that the multiplicative group mod p is cyclic: if g is a primitive root, then non-residues are odd powers of g. An odd power raised to (p−1)/2 gives g^(odd·(p−1)/2), which is an odd multiple of (p−1)/2, necessarily ≡ −1 (mod p).

A concrete example makes this tangible. Take p = 7. Is 2 a quadratic residue mod 7? Check: 1²=1, 2²=4, 3²=2, 4²=2, 5²=4, 6²=1 — yes, 2≡3² (mod 7), so (2/7)=1. Euler's criterion confirms: 2^3 = 8 ≡ 1 (mod 7). Now try a = 3: 3^3 = 27 ≡ 6 ≡ −1 (mod 7), so (3/7) = −1 and 3 is a non-residue. The computational payoff is significant: evaluating (a/p) via a^((p−1)/2) mod p takes O(log p) multiplications using fast exponentiation, far more efficient than checking all squares manually.
