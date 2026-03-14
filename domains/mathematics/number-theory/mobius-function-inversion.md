---
id: mobius-function-inversion
title: Möbius Function and Möbius Inversion
domain: mathematics
course: number-theory
prerequisites:
- id: arithmetic-functions-multiplicativity
  type: hard
tags:
- mobius
- inversion
- combinatorics
stage: advanced
status: draft
---

# Möbius Function and Möbius Inversion

## Core Idea
The Möbius function μ(n) is 0 if n has a squared prime factor, and (-1)^k if n is a product of k distinct primes. Möbius inversion states: if g(n) = Σ_{d|n} f(d), then f(n) = Σ_{d|n} μ(n/d)g(d), enabling inversion of divisor sums.
