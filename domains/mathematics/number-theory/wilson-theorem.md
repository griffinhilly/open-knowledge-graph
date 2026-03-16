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

## Explainer

From your work with modular arithmetic, you know that the integers mod p form a field when p is prime, which means every nonzero element has a unique multiplicative inverse mod p. Wilson's theorem exploits this structure to evaluate (p−1)! mod p in one elegant step. The key observation is that most elements in {1, 2, ..., p−1} can be paired with their distinct modular inverse. If a ≢ a⁻¹ (mod p), then a and a⁻¹ are two different elements that contribute a product of 1 to the factorial. So most of the product cancels in pairs, leaving only the **self-inverse** elements: those where a² ≡ 1 (mod p), i.e., a ≡ ±1 (mod p).

Since p is prime, the equation a² ≡ 1 (mod p) has exactly two solutions: a ≡ 1 and a ≡ −1 (mod p), which are 1 and p−1 respectively. Every other element in {2, 3, ..., p−2} pairs with a distinct inverse, and those pairs multiply to 1. So (p−1)! ≡ 1 · (paired terms all giving 1) · (p−1) ≡ p−1 ≡ −1 (mod p). The theorem is proved. For small primes, verify directly: 4! = 24 ≡ −1 (mod 5) ✓, and 6! = 720 ≡ −1 (mod 7) ✓.

Why does this fail for composite n? If n is composite, n has a factor d with 1 < d < n, so d appears in the list {1, 2, ..., n−1}. Since d | n and d | d, we get d | gcd(d, n) = d, but more importantly, n divides (n−1)! because the prime factors of n appear among {1, ..., n−1} (except when n = p² for a prime p, which is a minor special case). This means (n−1)! ≡ 0 (mod n) for most composite n, not −1. The theorem thus provides an exact characterization of primes: n is prime if and only if (n−1)! ≡ −1 (mod n).

The practical limitation is computational. Computing (p−1)! requires multiplying together (p−1) numbers, each of size up to p — an exponential number of operations in the bit length of p. A 1000-digit prime has roughly 10^{1000} in its factorial, making Wilson's test laughably slow compared to **Fermat's little test** (which needs only a modular exponentiation, polynomial in the bit length) or the Miller-Rabin test. Wilson's theorem is best appreciated as a theoretical gem: a perfect characterization of primeness that is simultaneously useless for practical computation. It illustrates a broader theme in number theory — elegant exact characterizations and efficient algorithms are often different things.
