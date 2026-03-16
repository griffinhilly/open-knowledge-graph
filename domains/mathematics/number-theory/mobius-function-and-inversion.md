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

## Explainer

The **Möbius function** μ(n) is a number-theoretic tool that encodes information about the squarefree structure of an integer. Recall from your study of arithmetic functions and multiplicativity that a function is multiplicative if f(mn) = f(m)f(n) whenever gcd(m, n) = 1. The Möbius function is multiplicative, which makes it tractable to compute and work with. Its values are simple: μ(1) = 1; μ(n) = 0 if n has any squared prime factor (i.e., p² | n for some prime p); and if n = p₁p₂⋯pₖ is squarefree, then μ(n) = (−1)ᵏ — positive if k is even, negative if k is odd.

To build intuition, compute a few values. μ(6) = μ(2·3) = (−1)² = 1. μ(30) = μ(2·3·5) = (−1)³ = −1. μ(12) = μ(4·3) = 0 because 4 = 2² is a squared factor. The function oscillates between −1, 0, and 1, with zeroes at numbers divisible by any perfect square greater than 1. A foundational identity is Σ_{d|n} μ(d) = [n = 1], meaning the sum of μ over all divisors of n equals 1 if n = 1 and 0 otherwise. This is the key property that makes Möbius inversion work.

**Möbius inversion** is the technique: if you know that g(n) = Σ_{d|n} f(d) — that is, g is the "summatory" version of f over divisors — then you can recover f from g by f(n) = Σ_{d|n} μ(n/d)·g(d). Think of it as an inverse operation for the divisor-sum transform, analogous to how subtraction inverts addition. The proof uses the identity above: when you substitute the formula for g and rearrange, the μ-weighted sums collapse to [d = 1], isolating f(n).

The canonical application is deriving a formula for **Euler's totient function** φ(n). We know that Σ_{d|n} φ(d) = n — counting integers from 1 to n grouped by their gcd with n. This has the form g(n) = Σ_{d|n} f(d) with g(n) = n and f(n) = φ(n). Möbius inversion immediately gives φ(n) = Σ_{d|n} μ(n/d)·d, a formula that would be tedious to derive otherwise. More broadly, whenever a function in number theory is defined as a sum over divisors, Möbius inversion is the tool that peels it apart — it is the "deconvolution" operation for Dirichlet convolution, the multiplication structure that underlies all multiplicative arithmetic functions.
