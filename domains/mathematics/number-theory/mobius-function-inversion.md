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

## Explainer

From your study of arithmetic functions and multiplicativity, you know that many number-theoretic quantities — like Euler's totient φ(n), the sum of divisors σ(n), and the number of divisors d(n) — are defined via sums over divisors of n. A natural question arises: if you know the divisor sum g(n) = Σ_{d|n} f(d), can you recover f(n)? Möbius inversion answers yes, and the **Möbius function** μ is the key.

The definition of μ(n) is sharp: μ(1) = 1; μ(n) = 0 if any prime appears squared in n's factorization; μ(n) = (−1)^k if n is a product of k distinct primes. In other words, μ detects squarefreeness and assigns a sign based on the number of prime factors. For example: μ(6) = μ(2·3) = (−1)² = 1, μ(30) = μ(2·3·5) = (−1)³ = −1, μ(12) = μ(2²·3) = 0. The function oscillates, but its local averages are controlled.

The **Möbius inversion formula** says: if g(n) = Σ_{d|n} f(d), then f(n) = Σ_{d|n} μ(n/d) g(d). Think of this as a "Fourier inversion" over the divisibility lattice. The multiplicativity of μ (a consequence of your prerequisite on arithmetic functions) makes this tractable. A key identity underpinning the whole theory is Σ_{d|n} μ(d) = [n=1] — the sum of μ over all divisors equals 1 if n = 1 and 0 otherwise. This is the "orthogonality" that makes inversion possible.

As a concrete application: you can recover φ(n) from the identity n = Σ_{d|n} φ(d) (which sums totient values over divisors). Inverting gives φ(n) = Σ_{d|n} μ(n/d) · d = n Σ_{d|n} μ(d)/d. Similarly, you can invert any multiplicative Dirichlet series using μ as the "inverse" of the constant function 1 in the ring of arithmetic functions under **Dirichlet convolution**. This algebraic structure — where Dirichlet convolution acts as multiplication and μ * 1 = ε (the identity) — unifies dozens of formulas in number theory and is the true reason Möbius inversion works.
