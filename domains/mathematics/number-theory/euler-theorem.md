---
id: euler-theorem
title: Euler's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fermat-little-theorem
  type: soft
- id: euler-totient-function
  type: hard
builds-toward:
- rsa-cryptography
tags:
- modular-arithmetic
- euler-phi
- group-theory
stage: advanced
status: draft
---

# Euler's Theorem

## Core Idea
If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n), where φ is Euler's totient function. This generalizes Fermat's Little Theorem (where n = p gives φ(p) = p−1) and is essential for understanding RSA cryptography and computing modular exponentiation.
