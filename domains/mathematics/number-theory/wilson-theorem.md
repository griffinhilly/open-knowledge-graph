---
id: wilson-theorem
title: Wilson's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
tags:
- modular-arithmetic
- primes
- factorials
- wilson
stage: advanced
status: draft
---

# Wilson's Theorem

## Core Idea
For a prime p, we have (p−1)! ≡ −1 (mod p). While elegant and providing a primality test, Wilson's theorem is computationally impractical for large primes compared to probabilistic tests. It exemplifies the beauty of elementary number theory and connects factorials to modular arithmetic.

## How It's Best Learned
Prove using the pairing of elements with their modular inverses in (ℤ/pℤ)*. Understand why non-primes violate this: for composite n > 4, n/2 pairs with itself.

## Common Misconceptions
Wilson's theorem only characterizes primes; (n−1)! ≡ −1 (mod n) fails for all composite n > 4. It is inefficient for primality testing compared to Fermat or Miller-Rabin tests.
