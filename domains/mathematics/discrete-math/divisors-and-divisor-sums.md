---
id: divisors-and-divisor-sums
title: Divisor Functions and Multiplicative Functions
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: modular-arithmetic
  type: soft
tags:
- number-theory
- divisor-functions
- multiplicative
stage: formal-systems
status: draft
---

# Divisor Functions and Multiplicative Functions

## Core Idea
The divisor function τ(n) counts the number of positive divisors of n, and σ(n) sums them. These are multiplicative functions: if gcd(a,b)=1, then f(ab)=f(a)f(b). Understanding these functions is essential for number-theoretic problems and factorization analysis.

## Explainer

From your work on divisibility and GCDs, you know how to factor integers and identify which numbers divide a given n. The divisor functions τ (tau) and σ (sigma) formalize and count this structure, turning divisibility facts into numerical quantities you can compute and compare.

**τ(n)** (sometimes written d(n)) counts how many positive divisors n has. For example, τ(12) = 6 because 1, 2, 3, 4, 6, 12 all divide 12. **σ(n)** sums those divisors: σ(12) = 1 + 2 + 3 + 4 + 6 + 12 = 28. These functions capture different aspects of a number's multiplicative structure — τ measures divisibility width while σ measures divisibility weight. A number n is called **perfect** when σ(n) = 2n (its divisors sum to twice itself), which happens for 6, 28, and 496.

The key property is **multiplicativity**: if gcd(a, b) = 1, then τ(ab) = τ(a)·τ(b) and σ(ab) = σ(a)·σ(b). This lets you compute τ(n) efficiently from the prime factorization. If n = p₁^a₁ · p₂^a₂ · …, then τ(n) = (a₁ + 1)(a₂ + 1)…. Each prime power contributes independently, because the divisors of n factor as products of divisors from each prime component — one from each pᵢ^aᵢ. For n = 12 = 2²·3¹: τ(12) = (2 + 1)(1 + 1) = 6. ✓ Similarly, σ(pᵃ) = 1 + p + p² + … + pᵃ = (pᵃ⁺¹ − 1)/(p − 1), and multiplicativity handles the rest.

Multiplicativity is a powerful structural property: the behavior of the function on all integers is completely determined by its values on prime powers alone. The Möbius function μ(n), Euler's totient φ(n), and many other important number-theoretic functions share this property. Divisor functions are the simplest examples in this family, and mastering them gives you the pattern — prime-by-prime independence — that underlies the general theory of multiplicative functions and Dirichlet series.
