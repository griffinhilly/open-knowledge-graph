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
