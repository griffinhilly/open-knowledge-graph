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
status: validated
---

# Arithmetic Functions and Multiplicativity

## Core Idea
Arithmetic functions map positive integers to complex numbers; examples include the divisor function d(n) and Euler's totient function φ(n). Multiplicative functions satisfy f(mn) = f(m)f(n) for coprime m, n, and their properties are completely determined by their values on prime powers. This structure enables efficient computation.

## Questions

```yaml
- question: "What is d(72), the number of divisors of 72?"
  type: multiple-choice
  options:
    - "8"
    - "9"
    - "12"
    - "18"
  answer: 2
  explanation: "72 = 2³ × 3². By the product formula for the divisor function, d(72) = (3+1)(2+1) = 4 × 3 = 12. Each divisor is formed by independently choosing an exponent for 2 (0, 1, 2, or 3: four choices) and an exponent for 3 (0, 1, or 2: three choices). Multiplicativity lets you multiply these counts because 2³ and 3² are coprime. Trying to list divisors directly (1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72) confirms the answer."

- question: "Suppose f is multiplicative and you know f(2) = 3, f(4) = 5, f(3) = 7. Which additional piece of information lets you compute f(12) without any further assumptions?"
  type: multiple-choice
  options:
    - "f(2) alone, because multiplicativity means f(12) = f(2)⁴ / f(3)"
    - "f(4) and f(3), because 12 = 4 × 3 and gcd(4, 3) = 1, so f(12) = f(4)·f(3) = 35"
    - "f(2) and f(3), because 12 = 2² × 3 and f(12) = f(2)·f(2)·f(3) = 63"
    - "All three values are needed and the answer is f(2)·f(4)·f(3)"
  answer: 1
  explanation: "Since 12 = 4 × 3 and gcd(4, 3) = 1, multiplicativity gives f(12) = f(4)·f(3) = 5 × 7 = 35. You need f(4) = f(2²), not just f(2), because a multiplicative function's values on prime powers are independent data — f(p²) is not determined by f(p) alone (only completely multiplicative functions satisfy f(p²) = f(p)²). Option C incorrectly applies complete multiplicativity, which is a stronger condition."

- question: "Knowing f(p) for every prime p is sufficient to compute f(n) for every positive integer n, as long as f is multiplicative."
  type: true-false
  answer: false
  explanation: "Multiplicativity requires knowing f on all prime *powers*, not just primes. For a prime power p^k with k ≥ 2, f(p^k) is independent data — it cannot be derived from f(p) unless f happens to be completely multiplicative (f(mn) = f(m)f(n) for ALL m, n, not just coprime pairs). For example, d(p) = 2 for every prime p, but d(p²) = 3, not 2² = 4. You need the value at each prime power separately."

- question: "A multiplicative function on n is completely determined by its values on prime powers because the Fundamental Theorem of Arithmetic guarantees a unique factorization of every integer into coprime prime-power factors."
  type: true-false
  answer: true
  explanation: "This is the structural reason multiplicativity is so powerful. Every n > 1 factors uniquely as p₁^a₁ · p₂^a₂ · … · pₖ^aₖ with distinct primes, and the factors are pairwise coprime. Applying f(mn) = f(m)f(n) repeatedly (valid since all factors are coprime) gives f(n) = f(p₁^a₁)·f(p₂^a₂)·…·f(pₖ^aₖ). Without unique factorization, this argument would fail — there would be multiple ways to factor n, potentially giving different values of f(n)."

- question: "Why does multiplicativity reduce the problem of computing an arithmetic function on all positive integers to computing it only on prime powers?"
  type: short-answer
  answer: "The Fundamental Theorem of Arithmetic guarantees that every integer n > 1 factors uniquely into prime powers: n = p₁^a₁ · p₂^a₂ · … · pₖ^aₖ. These prime-power factors are pairwise coprime (gcd(pᵢ^aᵢ, pⱼ^aⱼ) = 1 for i ≠ j). Multiplicativity then gives f(n) = f(p₁^a₁)·f(p₂^a₂)·…·f(pₖ^aₖ) — a product of prime-power values. Since prime powers are much simpler objects than arbitrary integers (their structure is just p^k), the value of f there is usually given by a simple formula like a geometric series. Once those prime-power values are known, the function is determined everywhere."
  explanation: "This reduction is the core utility of multiplicativity. Computing d(n) for a random 20-digit number would be intractable by listing divisors, but factoring n and applying d(p^k) = k+1 at each prime power gives the answer immediately. The same pattern applies to σ(n), φ(n), and the Möbius function — multiplicativity is the lever that makes number-theoretic computation tractable."
```

## Explainer

An **arithmetic function** is any function f: ℕ → ℂ — any assignment of a complex number to each positive integer. Examples include d(n), the number of divisors of n; σ(n), the sum of divisors; and φ(n), Euler's totient. The definition is broad, but the most useful arithmetic functions carry additional structure that makes them tractable to compute and study.

The key property is **multiplicativity**: f is multiplicative if f(1) = 1 and f(mn) = f(m)f(n) whenever gcd(m, n) = 1. The coprimality condition is essential — without it, f would be **completely multiplicative**, a stronger and rarer condition. Multiplicativity is powerful precisely because of your prerequisite: the Fundamental Theorem of Arithmetic guarantees that every positive integer factors uniquely into prime powers. A multiplicative function on n is therefore completely determined by its values on prime powers p^k. To know f everywhere, you only need to know f(p^k) for all primes p and integers k ≥ 1.

To see this concretely, take d(n). If n = p₁^a₁ · p₂^a₂ · · · pₖ^aₖ, then d(n) = (a₁ + 1)(a₂ + 1)···(aₖ + 1). This product formula works because divisors of n are built by independently choosing each prime's exponent from 0 to aᵢ — giving aᵢ + 1 choices per prime. The product formula is exactly what multiplicativity gives: d(p^a · q^b) = d(p^a) · d(q^b) when p ≠ q, and d(p^a) = a + 1 on prime powers. Similarly, the sum-of-divisors function satisfies σ(p^a) = 1 + p + p² + ··· + p^a = (p^{a+1} − 1)/(p − 1), and multiplicativity extends this to all n by taking products over prime power factors.

The pattern is always the same: compute the function on prime powers (usually yielding a geometric-series-type formula), then extend to all integers by multiplication — because the Fundamental Theorem ensures the factorization is unique and the coprimality conditions hold automatically for distinct prime factors. This reduces questions about arbitrary integers to questions about prime powers, which are much more tractable. The functions that build toward this topic — Euler's totient and the Möbius function — both follow this same structure, and Möbius inversion exploits multiplicativity to convert between arithmetic functions in a systematic way.
