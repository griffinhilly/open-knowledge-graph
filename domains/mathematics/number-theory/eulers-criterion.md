---
id: eulers-criterion
title: Euler's Criterion
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-legendre-symbol
  type: hard
- id: fermats-little-theorem
  type: hard
builds-toward:
- law-quadratic-reciprocity
tags:
- eulers-criterion
- quadratic-residues
- legendre-symbol
stage: advanced
status: draft
---

# Euler's Criterion

## Core Idea
(a/p) ≡ a^((p-1)/2) (mod p). This criterion computes the Legendre symbol via modular exponentiation and reveals that quadratic residuosity is determined by the group structure of (Z/pZ)*.

## Explainer

You already know two things that Euler's Criterion connects: the **Legendre symbol** (a/p), which tells you whether a is a quadratic residue mod p, and **Fermat's Little Theorem**, which tells you a^(p-1) ≡ 1 (mod p) for any a not divisible by p. Euler's Criterion is what happens when you ask: can Fermat's Little Theorem tell us about squares?

The key algebraic step is to factor. Since a^(p-1) ≡ 1 (mod p), we have a^(p-1) - 1 ≡ 0 (mod p), which factors as (a^((p-1)/2) - 1)(a^((p-1)/2) + 1) ≡ 0 (mod p). Because p is prime, one of the factors must be zero mod p — so a^((p-1)/2) is either 1 or -1 (mod p). Euler's Criterion asserts exactly which outcome corresponds to which: a is a quadratic residue mod p if and only if a^((p-1)/2) ≡ 1 (mod p), and a non-residue if and only if a^((p-1)/2) ≡ -1 (mod p).

Why does this work? Consider the **multiplicative group** (ℤ/pℤ)*, which is cyclic of order p-1. Every element can be written as g^k for a fixed generator g. The element g^k is a perfect square in this group if and only if k is even, because g^k = (g^(k/2))² only makes sense when k/2 is an integer. Now compute (g^k)^((p-1)/2) = g^(k(p-1)/2). If k is even, this equals (g^(p-1))^(k/2) = 1^(k/2) = 1 by Fermat. If k is odd, the exponent k(p-1)/2 is not a multiple of p-1, and the result is g^((p-1)/2) — the unique element of order 2 in the group, which equals -1 (mod p). The exponent test perfectly separates squares from non-squares.

In practice, Euler's Criterion turns a question about square roots into a fast modular exponentiation. To decide whether 7 is a quadratic residue mod 11, compute 7^5 mod 11: 7² = 49 ≡ 5, 7⁴ ≡ 25 ≡ 3, 7⁵ ≡ 21 ≡ 10 ≡ -1 (mod 11). So (7/11) = -1, meaning 7 has no square root mod 11 — far more efficient than checking all residue classes individually. This computational power, rooted in the group structure of (ℤ/pℤ)*, is what makes the criterion foundational for the deeper theory of quadratic reciprocity.
