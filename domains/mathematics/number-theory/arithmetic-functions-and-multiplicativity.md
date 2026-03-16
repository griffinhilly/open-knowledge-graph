---
id: arithmetic-functions-and-multiplicativity
title: Arithmetic Functions and Multiplicativity
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic-rigorous
  type: hard
builds-toward:
- euler-totient-function
- mobius-function-and-inversion
tags:
- arithmetic-functions
- multiplicative
- divisor-functions
stage: advanced
status: draft
---

# Arithmetic Functions and Multiplicativity

## Core Idea
Arithmetic functions map positive integers to complex numbers; examples include the divisor function d(n) and Euler's totient function φ(n). Multiplicative functions satisfy f(mn) = f(m)f(n) for coprime m, n, and their properties are completely determined by their values on prime powers. This structure enables efficient computation.

## Explainer

An **arithmetic function** is any function f: ℕ → ℂ — any assignment of a complex number to each positive integer. Examples include d(n), the number of divisors of n; σ(n), the sum of divisors; and φ(n), Euler's totient. The definition is broad, but the most useful arithmetic functions carry additional structure that makes them tractable to compute and study.

The key property is **multiplicativity**: f is multiplicative if f(1) = 1 and f(mn) = f(m)f(n) whenever gcd(m, n) = 1. The coprimality condition is essential — without it, f would be **completely multiplicative**, a stronger and rarer condition. Multiplicativity is powerful precisely because of your prerequisite: the Fundamental Theorem of Arithmetic guarantees that every positive integer factors uniquely into prime powers. A multiplicative function on n is therefore completely determined by its values on prime powers p^k. To know f everywhere, you only need to know f(p^k) for all primes p and integers k ≥ 1.

To see this concretely, take d(n). If n = p₁^a₁ · p₂^a₂ · · · pₖ^aₖ, then d(n) = (a₁ + 1)(a₂ + 1)···(aₖ + 1). This product formula works because divisors of n are built by independently choosing each prime's exponent from 0 to aᵢ — giving aᵢ + 1 choices per prime. The product formula is exactly what multiplicativity gives: d(p^a · q^b) = d(p^a) · d(q^b) when p ≠ q, and d(p^a) = a + 1 on prime powers. Similarly, the sum-of-divisors function satisfies σ(p^a) = 1 + p + p² + ··· + p^a = (p^{a+1} − 1)/(p − 1), and multiplicativity extends this to all n by taking products over prime power factors.

The pattern is always the same: compute the function on prime powers (usually yielding a geometric-series-type formula), then extend to all integers by multiplication — because the Fundamental Theorem ensures the factorization is unique and the coprimality conditions hold automatically for distinct prime factors. This reduces questions about arbitrary integers to questions about prime powers, which are much more tractable. The functions that build toward this topic — Euler's totient and the Möbius function — both follow this same structure, and Möbius inversion exploits multiplicativity to convert between arithmetic functions in a systematic way.
