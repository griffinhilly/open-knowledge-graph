---
id: arithmetic-functions-multiplicativity
title: Arithmetic Functions and Multiplicativity
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
builds-toward:
- eulers-totient-function
- mobius-function-inversion
tags:
- arithmetic-functions
- multiplicative
stage: advanced
status: validated
---

# Arithmetic Functions and Multiplicativity

## Core Idea
An arithmetic function maps positive integers to complex numbers. A function f is multiplicative if f(mn) = f(m)f(n) whenever gcd(m, n) = 1, and completely multiplicative if this holds for all m and n regardless of their gcd. Because every positive integer factors uniquely into prime powers, a multiplicative function is entirely determined by its values on prime powers. Key examples include Euler's totient φ(n), the divisor function σ(n), and the Möbius function μ(n). Multiplicativity enables efficient computation and is the foundation for techniques like Möbius inversion and Dirichlet series manipulation.

## How It's Best Learned
Verify multiplicativity by hand for small examples: compute φ(12) via φ(4)·φ(3) and confirm it matches the direct count. Then see how knowing φ(pᵏ) = pᵏ − pᵏ⁻¹ lets you compute φ for any n from its prime factorization.

## Common Misconceptions
Multiplicative does not mean f(mn) = f(m)f(n) for all m, n—that is completely multiplicative. The coprimality condition is essential. Also, f(1) = 1 is a consequence of multiplicativity, not an extra assumption.

## Explainer

An **arithmetic function** is any function f : ℕ → ℂ — it assigns a complex number to each positive integer. Some famous examples include the divisor-counting function d(n) (how many divisors n has), the sum-of-divisors function σ(n), and Euler's totient φ(n) (how many integers less than n are coprime to n). What makes these functions tractable is a structural property rooted in the Fundamental Theorem of Arithmetic: they are all **multiplicative**. A function f is multiplicative if f(mn) = f(m)f(n) whenever gcd(m, n) = 1. This condition means that the value of f at any integer is entirely determined by its values on prime powers, because the Fundamental Theorem writes every n uniquely as a product of coprime prime powers p₁^{a₁} · p₂^{a₂} · ⋯ · pₖ^{aₖ}, and multiplicativity then gives f(n) = f(p₁^{a₁}) · f(p₂^{a₂}) · ⋯ · f(pₖ^{aₖ}).

The coprimality requirement gcd(m, n) = 1 is not a technicality — it is the entire substance of the definition. Multiplicativity does not say f(mn) = f(m)f(n) for all m and n; that stronger condition defines a **completely multiplicative** function. The distinction matters: Euler's totient is multiplicative but not completely multiplicative. You can verify this directly: φ(4) = 2 and φ(2) = 1, but φ(4) ≠ φ(2)·φ(2) = 1, because gcd(2, 2) = 2 ≠ 1. In contrast, the identity function f(n) = n is completely multiplicative since f(mn) = mn = f(m)f(n) for all m and n, with no coprimality restriction needed.

The power of multiplicativity is computational. To compute φ(360), you do not enumerate the integers coprime to 360. Instead, factor 360 = 2³ · 3² · 5, compute φ(2³) = 4, φ(3²) = 6, φ(5) = 4, and multiply: φ(360) = 4 · 6 · 4 = 96. This works because the prime-power factors are pairwise coprime, so multiplicativity applies directly. The reduction from a problem about the full integer to a product of independent problems on prime powers is what makes multiplicative functions computationally efficient and theoretically clean.

Multiplicativity also has deep algebraic consequences. The **Dirichlet convolution** of two arithmetic functions, defined by (f * g)(n) = Σ_{d|n} f(d)g(n/d), preserves multiplicativity: if f and g are both multiplicative, so is f * g. This algebraic structure is the foundation for Möbius inversion — the technique that lets you recover f from its summatory function F(n) = Σ_{d|n} f(d). The Möbius function μ(n) is itself multiplicative, and its role as the inverse of the constant function 1 under Dirichlet convolution is what makes the inversion formula work. From the factorization-based viewpoint you have built here, Möbius inversion becomes a natural consequence of the ring structure of multiplicative functions under Dirichlet convolution.

## Questions

```yaml
- question: "A multiplicative function f satisfies f(4) = 3 and f(9) = 5. What is f(36)?"
  type: multiple-choice
  options:
    - "15, because gcd(4, 9) = 1 and f(36) = f(4) · f(9)"
    - "8, because f(36) = f(4) + f(9)"
    - "Cannot be determined without knowing f on all prime powers"
    - "15, but only if f is also completely multiplicative"
  answer: 0
  explanation: "Since 36 = 4 · 9 and gcd(4, 9) = 1 (they share no prime factors: 4 = 2² and 9 = 3²), multiplicativity directly gives f(36) = f(4) · f(9) = 3 · 5 = 15. The coprimality condition is satisfied, so the standard definition applies. No additional condition is needed — multiplicativity suffices here because the inputs are coprime."

- question: "A function f satisfies f(p²) = f(p)² for every prime p. Does this follow from multiplicativity alone?"
  type: multiple-choice
  options:
    - "Yes — multiplicativity gives f(p · p) = f(p) · f(p) for all primes p"
    - "No — multiplicativity only applies when gcd(m, n) = 1, but gcd(p, p) = p ≠ 1"
    - "Yes — prime powers are a special case where the coprimality condition is waived"
    - "No — this property requires knowing f on all integers, not just primes"
  answer: 1
  explanation: "Multiplicativity requires gcd(m, n) = 1. For p · p, gcd(p, p) = p ≠ 1, so the rule does not apply. Therefore f(p²) ≠ f(p)² in general for a merely multiplicative function. Euler's totient illustrates this: φ(p²) = p² − p, but φ(p)² = (p−1)², and these are different. For p = 5: φ(25) = 20 but φ(5)² = 16. Complete multiplicativity would give f(p²) = f(p)², but multiplicativity alone does not."

- question: "A multiplicative function is entirely determined by its values on prime powers p^k."
  type: true-false
  answer: true
  explanation: "By the Fundamental Theorem of Arithmetic, every positive integer n factors uniquely as n = p₁^{a₁} · p₂^{a₂} · ... · pₖ^{aₖ} where the prime power factors are pairwise coprime. Multiplicativity then gives f(n) = f(p₁^{a₁}) · f(p₂^{a₂}) · ... · f(pₖ^{aₖ}). Knowing f(p^k) for every prime p and every exponent k therefore determines f everywhere. This is what makes multiplicative functions computationally tractable."

- question: "A substantially multiplicative function satisfies f(mn) = f(m)f(n) primarily when gcd(m, n) = 1."
  type: true-false
  answer: false
  explanation: "This describes merely multiplicative, not completely multiplicative. A completely multiplicative function satisfies f(mn) = f(m)f(n) for ALL positive integers m and n, with no coprimality restriction. Complete multiplicativity is strictly stronger: every completely multiplicative function is multiplicative, but not vice versa. The identity function f(n) = n is completely multiplicative; Euler's totient φ is only multiplicative."

- question: "Explain why the coprimality condition in the definition of multiplicativity is mathematically essential. What goes wrong if you naively apply f(p²) = f(p)·f(p) for a merely multiplicative function?"
  type: short-answer
  answer: "The coprimality condition ensures that when we write n = m · k with gcd(m, k) = 1, the prime factorizations of m and k are completely disjoint — no prime is shared. Multiplicativity factors f over this disjoint union. If m and k share a prime factor, their product 'double-counts' that prime, and the multiplicativity rule is invalid. For f(p²) = f(p · p), gcd(p, p) = p ≠ 1, so the rule cannot be applied. Concretely, for Euler's totient: φ(p²) = p² − p (direct computation), but φ(p) · φ(p) = (p−1)². These are equal only when p−1 = p, which never happens."
  explanation: "This is why the values f(p^k) on prime powers must be established separately (via their own formulas or definitions), and only then can multiplicativity be used to compute f at composite numbers from coprime prime-power building blocks. The function factors over coprime pairs, not arbitrary pairs."
```

