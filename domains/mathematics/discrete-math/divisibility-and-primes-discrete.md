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
