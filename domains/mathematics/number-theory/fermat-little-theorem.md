---
id: fermat-little-theorem
title: Fermat's Little Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- euler-theorem
- rsa-cryptography
tags:
- modular-arithmetic
- group-theory
- primes
- fermat
stage: advanced
status: draft
---

# Fermat's Little Theorem

## Core Idea
If p is prime and gcd(a, p) = 1, then a^(p−1) ≡ 1 (mod p). This theorem follows from Lagrange's theorem applied to the multiplicative group (ℤ/pℤ)* and forms the basis for Fermat primality tests and many cryptographic algorithms.

## How It's Best Learned
Derive it from group theory using the multiplicative group mod p. Verify with numerical examples (e.g., 2^4 ≡ 1 (mod 5)). Apply it to compute large powers modulo p efficiently.

## Common Misconceptions
The converse is false: a^(n−1) ≡ 1 (mod n) does not imply n is prime (Carmichael numbers counterexample: 561 = 3·11·17). The condition gcd(a, p) = 1 is essential; the theorem fails when a is divisible by p.
