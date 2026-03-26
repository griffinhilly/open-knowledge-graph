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
status: validated
---

# Divisor Functions and Multiplicative Functions

## Core Idea
The divisor function τ(n) counts the number of positive divisors of n, and σ(n) sums them. These are multiplicative functions: if gcd(a,b)=1, then f(ab)=f(a)f(b). Understanding these functions is essential for number-theoretic problems and factorization analysis.

## Questions

```yaml
- question: "What is τ(360)? (Note: 360 = 2³ × 3² × 5)"
  type: multiple-choice
  options:
    - "10 — sum of the exponents plus one"
    - "12 — product of the exponents"
    - "24 — product of each exponent plus one"
    - "15 — number of distinct prime factors times 5"
  answer: 2
  explanation: "Multiplicativity gives τ(n) = (a₁ + 1)(a₂ + 1)... for n = p₁^a₁ · p₂^a₂ ·... So τ(360) = τ(2³ · 3² · 5¹) = (3+1)(2+1)(1+1) = 4 · 3 · 2 = 24. Each prime power contributes an independent factor because the divisors of n are formed by independently choosing one divisor from each prime component. Option A confusingly adds exponents instead of multiplying; option B multiplies them without adding 1."

- question: "You know τ(m) = 6 and τ(n) = 4. Under what condition can you conclude τ(mn) = 24?"
  type: multiple-choice
  options:
    - "Always — multiplication of divisor counts is always valid"
    - "Only when m and n are both prime powers"
    - "Only when gcd(m, n) = 1"
    - "Only when m and n share no prime factors that appear in the key factorization"
  answer: 2
  explanation: "Multiplicativity states: if gcd(a, b) = 1, then τ(ab) = τ(a)τ(b). The coprimality condition is essential — without it, shared prime factors cause divisors to be counted multiple times. For example, τ(4) = 3 and τ(6) = 4, but τ(24) = 8, not 12, because gcd(4, 6) = 2 ≠ 1. Option A is the classic error — blindly multiplying divisor counts without checking coprimality."

- question: "τ(mn) = τ(m) × τ(n) is true for most positive integers m and n."
  type: true-false
  answer: false
  explanation: "This holds only when gcd(m, n) = 1. When m and n share common prime factors, their divisors interact and τ(mn) < τ(m)τ(n). Counterexample: τ(4) = 3 and τ(6) = 4, but τ(24) = 8, not 12. The multiplicativity property is powerful precisely because it applies across coprime factors — which is why the prime factorization (whose prime power components are always pairwise coprime) is the right framework for computing τ."

- question: "A number n is called perfect when σ(n) = 2n — its positive divisors (including itself) sum to twice n."
  type: true-false
  answer: true
  explanation: "This is the classical definition of a perfect number. For n = 6: divisors are 1, 2, 3, 6, so σ(6) = 12 = 2 × 6. For n = 28: σ(28) = 1+2+4+7+14+28 = 56 = 2 × 28. The connection to σ is immediate: σ(n) sums ALL positive divisors of n including n itself, so σ(n) = 2n means the sum of proper divisors (all divisors except n itself) equals n."

- question: "Explain why multiplicativity means τ(n) is completely determined by the prime factorization of n, and give the resulting formula."
  type: short-answer
  answer: "Because prime powers in the factorization are pairwise coprime, multiplicativity applies at every step: τ(p₁^a₁ · p₂^a₂ · ...) = τ(p₁^a₁) · τ(p₂^a₂) · .... And τ(p^a) = a + 1 for any prime p, since the divisors of p^a are exactly 1, p, p², ..., p^a. So τ(n) = (a₁ + 1)(a₂ + 1)... — the entire function is determined by the exponents in the prime factorization."
  explanation: "Multiplicativity means a function on all integers is determined by its values on prime powers, because every integer factors into coprime prime powers. For τ, the value at each prime power p^a is easy to count directly (a+1 divisors). The formula τ(n) = (a₁+1)(a₂+1)... chains multiplicativity across all prime factors. This prime-by-prime independence is the structural pattern shared by σ, Euler's totient φ, the Möbius function μ, and all multiplicative functions in number theory."
```

## Explainer

From your work on divisibility and GCDs, you know how to factor integers and identify which numbers divide a given n. The divisor functions τ (tau) and σ (sigma) formalize and count this structure, turning divisibility facts into numerical quantities you can compute and compare.

**τ(n)** (sometimes written d(n)) counts how many positive divisors n has. For example, τ(12) = 6 because 1, 2, 3, 4, 6, 12 all divide 12. **σ(n)** sums those divisors: σ(12) = 1 + 2 + 3 + 4 + 6 + 12 = 28. These functions capture different aspects of a number's multiplicative structure — τ measures divisibility width while σ measures divisibility weight. A number n is called **perfect** when σ(n) = 2n (its divisors sum to twice itself), which happens for 6, 28, and 496.

The key property is **multiplicativity**: if gcd(a, b) = 1, then τ(ab) = τ(a)·τ(b) and σ(ab) = σ(a)·σ(b). This lets you compute τ(n) efficiently from the prime factorization. If n = p₁^a₁ · p₂^a₂ · …, then τ(n) = (a₁ + 1)(a₂ + 1)…. Each prime power contributes independently, because the divisors of n factor as products of divisors from each prime component — one from each pᵢ^aᵢ. For n = 12 = 2²·3¹: τ(12) = (2 + 1)(1 + 1) = 6. ✓ Similarly, σ(pᵃ) = 1 + p + p² + … + pᵃ = (pᵃ⁺¹ − 1)/(p − 1), and multiplicativity handles the rest.

Multiplicativity is a powerful structural property: the behavior of the function on all integers is completely determined by its values on prime powers alone. The Möbius function μ(n), Euler's totient φ(n), and many other important number-theoretic functions share this property. Divisor functions are the simplest examples in this family, and mastering them gives you the pattern — prime-by-prime independence — that underlies the general theory of multiplicative functions and Dirichlet series.
