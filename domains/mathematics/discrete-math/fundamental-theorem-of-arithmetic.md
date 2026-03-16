---
id: fundamental-theorem-of-arithmetic
title: The Fundamental Theorem of Arithmetic
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: mathematical-induction
  type: hard
- id: proof-by-contradiction
  type: soft
tags:
- fundamental-theorem-arithmetic
- prime-factorization
- unique-factorization
- euclids-lemma
stage: formal-systems
status: validated
---

# The Fundamental Theorem of Arithmetic

## Core Idea
The Fundamental Theorem of Arithmetic states that every integer greater than 1 can be expressed as a product of prime numbers in exactly one way, up to the order of factors. Existence of the factorization is proved by strong induction. Uniqueness requires Euclid's lemma: if a prime p divides ab, then p divides a or p divides b. The theorem underpins the entire structure of elementary number theory — GCD, LCM, and divisibility results all depend on factorizations being unique.

## How It's Best Learned
Prove existence by strong induction, then prove Euclid's lemma separately using Bezout's identity, and finally assemble the uniqueness proof by contradiction. Contrast with systems where unique factorization fails (e.g., Z[√−5], where 6 = 2×3 = (1+√−5)(1−√−5)) to appreciate why the theorem is non-trivial.

## Common Misconceptions
- Treating unique factorization as self-evident — the proof is non-trivial and the property fails in other algebraic systems.
- Incorrectly classifying 1 as prime; 1 is excluded by convention and has the vacuous empty product as its factorization.

## Explainer

From your work on **divisibility and GCD**, you know that primes are the integers with no divisors except 1 and themselves, and that GCD can be computed using the Euclidean algorithm. The Fundamental Theorem of Arithmetic makes a deeper claim: these primes are the unique "atoms" of multiplication. Every integer greater than 1 breaks into primes in exactly one way (ignoring order). This feels obvious — try to factor 12 any way you like, you always get 2 × 2 × 3. But the theorem is not trivial, and its proof has two distinct parts that require different techniques.

**Existence** of a prime factorization is proved by strong induction, which you've already mastered. The argument is: if n is prime, it's its own factorization. If n is composite, it has a divisor d with 1 < d < n, so both d and n/d are smaller than n. By strong induction, each has a prime factorization, and multiplying them gives a prime factorization of n. Clean and complete.

**Uniqueness** is harder and is where **Euclid's lemma** enters: if a prime p divides a product ab, then p divides a or p divides b (or both). This follows from Bézout's identity — if p doesn't divide a, then gcd(p, a) = 1 (since p is prime), so there exist integers x, y with px + ay = 1, multiply both sides by b to get p(xb) + (ab)y = b, and since p divides ab, p divides the left side, so p divides b. With Euclid's lemma in hand, you can prove uniqueness by contradiction: assume two different prime factorizations exist, use the lemma to show each prime on one side must appear on the other, producing a contradiction.

To appreciate why uniqueness is non-trivial, consider the ring Z[√−5] — integers of the form a + b√−5. In this system, 6 = 2 × 3 = (1 + √−5)(1 − √−5), and all four factors are "irreducible" (can't be factored further) yet the two factorizations are genuinely different. Unique factorization fails because Euclid's lemma fails. In the ordinary integers, the proof works because of the specific structure of the Euclidean algorithm — a reminder that theorems depend on the axioms of their system, not just intuition.
