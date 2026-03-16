---
id: divisibility-and-primes-discrete
title: Divisibility, Primes, and Fundamental Theorem of Arithmetic
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: prime-and-composite-numbers
  type: hard
builds-toward:
- modular-arithmetic-discrete
tags:
- divisibility
- primes
- factorization
- fundamental-theorem
stage: formal-systems
status: draft
---

# Divisibility, Primes, and Fundamental Theorem of Arithmetic

## Core Idea
An integer a divides b (a | b) if b = ka for some integer k. Prime numbers have exactly two divisors (1 and themselves). The Fundamental Theorem of Arithmetic: every integer > 1 has a unique prime factorization. The proof relies on the Euclidean algorithm and mathematical induction.

## How It's Best Learned
Factor numbers into primes by trial division. Understand gcd via prime factorization: gcd(a, b) is the product of common prime factors to their minimum powers. Use the Euclidean algorithm for large numbers.

## Common Misconceptions
1 is not prime. Uniqueness of factorization requires using primes specifically, not other structures. Division by 0 is undefined; divisibility is defined only for nonzero divisors.

## Explainer

You've already worked with divisibility and GCD, and you know what prime and composite numbers are. This topic formalizes those ideas with precise notation and a powerful theorem. **Divisibility** is written a | b (read "a divides b") and means there exists an integer k such that b = ka. This notation is precise: it's a relationship between integers, not a fraction, and it is defined only when a ≠ 0. Saying 4 | 12 is a true statement (k = 3); saying 4 | 13 is false.

**Prime numbers** are integers greater than 1 whose only positive divisors are 1 and themselves. The number 1 is not prime — this is a definition choice, but a critical one. If 1 were prime, prime factorization would not be unique (12 could be written as 2² × 3 or as 1 × 2² × 3 or 1² × 2² × 3, and so on indefinitely). **Composite numbers** are those with at least one divisor other than 1 and themselves, meaning they factor into smaller positive integers. Every integer greater than 1 is either prime or composite — there is no third option.

The **Fundamental Theorem of Arithmetic** states that every integer greater than 1 can be written as a product of primes in exactly one way, up to the order of the factors. For example, 360 = 2³ × 3² × 5, and no other prime factorization produces 360. The theorem has two parts: existence (every such integer has at least one factorization) and uniqueness (it has exactly one). Uniqueness is the deep and surprising part — it fails in some other algebraic systems, which is why arithmetic in the integers is special.

From your prerequisite on GCD, you can now see it through prime factorizations: gcd(a, b) is the product of primes common to both factorizations, each taken to the minimum power. For example, gcd(360, 504) = gcd(2³·3²·5, 2³·3²·7) = 2³·3² = 72. The **Euclidean algorithm** computes this without factoring at all — useful because factoring large numbers is computationally hard, while the Euclidean algorithm is fast. Together, divisibility, primes, the FTA, GCD, and the Euclidean algorithm form the foundation of number theory and underpin modern cryptographic systems like RSA.
