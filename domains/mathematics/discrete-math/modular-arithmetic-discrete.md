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
