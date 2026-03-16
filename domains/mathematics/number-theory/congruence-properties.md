---
id: congruence-properties
title: Properties of Congruences
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
builds-toward:
- fermats-little-theorem
- eulers-theorem
- quadratic-residues-legendre-symbol
tags:
- congruences
- modular-arithmetic
- properties
stage: advanced
status: draft
---

# Properties of Congruences

## Core Idea
Congruences mod n form an equivalence relation: a ≡ b (mod n) iff n|(a-b). They respect addition, subtraction, and multiplication. If gcd(a,n) = 1, division is possible. These properties make congruences a powerful algebraic tool for number theory.

## Explainer

From your study of modular arithmetic, you know that a ≡ b (mod n) means a and b leave the same remainder when divided by n — equivalently, n divides (a − b). What congruences gain from being an **equivalence relation** is structure: they carve the integers into n disjoint **residue classes** (the classes 0, 1, 2, ..., n−1), and every integer belongs to exactly one. You can think of the integers as being "folded" onto a circle of n positions, and two numbers are congruent precisely when they land on the same position.

The arithmetic rules follow directly from this picture. If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d and a × c ≡ b × d (mod n). To see why multiplication works: a = b + kn and c = d + ln for some integers k, l, so ac = (b + kn)(d + ln) = bd + (bl + dk + kln)n. The extra terms are all multiples of n, so ac and bd land on the same residue class. This means you can reduce intermediate results at any stage of a computation — a powerful shortcut when doing arithmetic mod n.

**Division** is the subtler operation. You cannot always divide both sides of a congruence by a common factor and preserve the modulus. For example, 6 ≡ 2 (mod 4), but dividing by 2 gives 3 ≡ 1 (mod 4), which is false. Division works cleanly only when the divisor is **coprime to n** — that is, gcd(a, n) = 1. In that case, a has a **multiplicative inverse mod n**, a unique number a⁻¹ such that a·a⁻¹ ≡ 1 (mod n). Multiplying both sides by a⁻¹ is valid division. When gcd(a, n) = d > 1, you can still cancel a from ac ≡ ab (mod n), but the modulus shrinks: c ≡ b (mod n/d).

These properties are what make congruences a genuine algebraic system rather than just notation. The set {0, 1, ..., n−1} under addition and multiplication mod n forms a **ring** (written ℤ/nℤ); when n is prime, every nonzero element has a multiplicative inverse and it becomes a **field**. This algebraic lens is what powers everything downstream — Fermat's little theorem, Euler's theorem, and the Legendre symbol all live inside this structure. Whenever you see a proof that "reduces mod p," the congruence properties are the invisible machinery making each step valid.
