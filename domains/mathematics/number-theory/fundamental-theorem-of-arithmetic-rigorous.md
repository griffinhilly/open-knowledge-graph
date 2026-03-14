---
id: fundamental-theorem-of-arithmetic-rigorous
title: Fundamental Theorem of Arithmetic (Rigorous)
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic
  type: hard
- id: euclidean-algorithm
  type: soft
builds-toward:
- arithmetic-functions-and-multiplicativity
- failure-of-unique-factorization
tags:
- unique-factorization
- prime-factorization
- integers
stage: advanced
status: draft
---

# Fundamental Theorem of Arithmetic (Rigorous)

## Core Idea
Every integer greater than 1 either is prime or is uniquely expressible as a product of primes, up to order. This rigorous treatment proves both existence (by strong induction) and uniqueness (via Euclid's lemma) and explores why it holds in ℤ but fails in other number systems.

## How It's Best Learned
Prove existence and uniqueness separately using strong induction and Euclid's lemma. Compare with domains where unique factorization fails, such as ℤ[√5] where 6 = 2·3 = (1+√5)(1−√5).

## Common Misconceptions
Unique factorization is not universal across all algebraic structures; it requires special conditions. The unit 1 is not prime and must be handled separately in the uniqueness statement.
