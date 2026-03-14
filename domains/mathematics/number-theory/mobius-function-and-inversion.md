---
id: mobius-function-and-inversion
title: Möbius Function and Möbius Inversion
domain: mathematics
course: number-theory
prerequisites:
- id: arithmetic-functions-and-multiplicativity
  type: hard
tags:
- möbius-function
- möbius-inversion
- number-theoretic-functions
stage: advanced
status: draft
---

# Möbius Function and Möbius Inversion

## Core Idea
The Möbius function μ(n) is defined via prime factorization: μ(n) = 0 if n has a squared prime factor, 1 if n is a product of an even number of distinct primes, and −1 for an odd number. Möbius inversion is a powerful technique: if g(n) = Σ_{d|n} f(d), then f(n) = Σ_{d|n} μ(n/d)g(d).

## How It's Best Learned
Study the Möbius function through examples and its multiplicativity. Apply Möbius inversion to derive φ(n) = Σ_{d|n} μ(n/d)·d.

## Common Misconceptions
The Möbius function depends crucially on prime factorization; μ(p) = −1 only for primes. Möbius inversion requires a summing function; it doesn't apply to all function relationships.
