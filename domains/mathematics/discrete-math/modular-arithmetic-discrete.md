---
id: modular-arithmetic-discrete
title: Modular Arithmetic and Congruences
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic
  type: hard
- id: divisibility-and-primes-discrete
  type: hard
builds-toward:
- congruences-and-crt
tags:
- modular-arithmetic
- congruence
- modulus
- arithmetic-mod-n
stage: formal-systems
status: draft
---

# Modular Arithmetic and Congruences

## Core Idea
a ≡ b (mod n) means n divides a − b. Congruences behave like equality: if a ≡ b and c ≡ d (mod n), then a + c ≡ b + d and ac ≡ bd (mod n). Modular arithmetic is arithmetic in ℤₙ = {0, 1, ..., n−1} with operations mod n.

## How It's Best Learned
Compute modular arithmetic examples: 7 ≡ 2 (mod 5), so 7 + 3 ≡ 2 + 3 ≡ 0 (mod 5). Recognize that ℤₙ is a ring (closed under + and ×). Practice properties and solve congruences.

## Common Misconceptions
a ≡ b (mod n) is not the same as a = b; it's a relation. Division in modular arithmetic requires multiplicative inverses, which don't always exist.

## Explainer

You already know modular arithmetic as clock arithmetic: on a 12-hour clock, 10 + 4 = 2 because you wrap around at 12. The discrete math formalization gives this intuition a rigorous foundation. The **congruence relation** a ≡ b (mod n) is defined precisely: it holds if and only if n divides a − b. So 17 ≡ 2 (mod 5) because 5 divides 17 − 2 = 15. This is different from equality — 17 and 2 are different integers, but they are congruent modulo 5. Congruence is an equivalence relation: it is reflexive (a ≡ a), symmetric, and transitive. These three properties mean it carves the integers into **equivalence classes**, called **residue classes**: all integers that leave the same remainder when divided by n form one class.

The key algebraic fact is that congruences are compatible with addition and multiplication. If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n) and a · c ≡ b · d (mod n). This means you can reduce numbers at any point in a computation. To compute 47 · 83 (mod 5), note 47 ≡ 2 and 83 ≡ 3, so the product ≡ 2 · 3 = 6 ≡ 1 (mod 5). You never needed to compute 3,901. This **reduction principle** is what makes modular arithmetic so useful in cryptography and number theory — you can keep numbers small throughout long computations.

The set of residue classes {0, 1, 2, ..., n−1} under addition and multiplication mod n forms the ring **ℤₙ**. In ℤₙ, addition always works exactly as expected. Multiplication usually works. The tricky operation is division. Dividing by a in ℤₙ requires a **multiplicative inverse**: some element b such that a · b ≡ 1 (mod n). From your divisibility prerequisite, you know the key fact: a has a multiplicative inverse in ℤₙ if and only if gcd(a, n) = 1. So in ℤ₆, the element 2 has no inverse because gcd(2, 6) = 2 ≠ 1 — the equation 2x ≡ 1 (mod 6) has no solution. But in ℤ₇ (where 7 is prime), every nonzero element has an inverse because gcd(a, 7) = 1 for all a ≢ 0. When n is prime, ℤₙ is not just a ring but a **field** — division by nonzero elements always works.
