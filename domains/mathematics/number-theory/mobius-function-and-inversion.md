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

## Questions

```yaml
- question: "What fundamental identity of the Möbius function makes Möbius inversion work — that is, allows f(n) to be recovered from g(n) = Σ_{d|n} f(d)?"
  type: multiple-choice
  options:
    - "μ is completely multiplicative: μ(mn) = μ(m)μ(n) for all m, n"
    - "Σ_{d|n} μ(d) = 1 if n = 1 and 0 otherwise, collapsing all cross-terms in the inversion"
    - "μ(n) only takes the values −1, 0, and 1, keeping the inversion numerically bounded"
    - "μ is the unique arithmetic function satisfying μ(p) = −1 for every prime p"
  answer: 1
  explanation: "The inversion formula works because when you substitute g and rearrange, you get sums of the form Σ_{d|n} μ(d), which equal 1 only when n = 1 and 0 otherwise. This collapses every cross-term and isolates f(n). Knowing that μ only takes values in {−1, 0, 1} (option C) or that it is multiplicative (option A) does not by itself give the cancellation needed for inversion."

- question: "A student computes μ(12) by reasoning: '12 = 2 × 2 × 3 has three prime factors (counting multiplicity), so μ(12) = (−1)³ = −1.' What is the correct value of μ(12), and what flaw is in the student's reasoning?"
  type: multiple-choice
  options:
    - "μ(12) = −1; the student counted prime factors correctly and applied the formula correctly"
    - "μ(12) = 0; since 12 = 2² × 3 contains a squared prime factor, 12 is not squarefree and μ(12) = 0 by definition"
    - "μ(12) = 1; the student should count only distinct primes (2 and 3), giving (−1)² = 1"
    - "μ(12) = −1; but the student's reasoning is flawed because the formula only uses distinct primes"
  answer: 1
  explanation: "The Möbius function assigns μ(n) = 0 whenever n is divisible by any perfect square greater than 1. Since 12 = 2² × 3 is divisible by 4 = 2², μ(12) = 0. The formula μ(n) = (−1)^k applies only to squarefree n — numbers with no repeated prime factor. Option C is also wrong: distinct-prime counting would give μ(12) = (−1)² = 1, but that too is incorrect because the squarefree check comes first."

- question: "The Möbius function μ satisfies μ(mn) = μ(m)μ(n) whenever gcd(m, n) = 1. This means μ is completely multiplicative."
  type: true-false
  answer: false
  explanation: "μ is multiplicative (the weaker condition holding only for coprime inputs) but NOT completely multiplicative. Complete multiplicativity would require μ(mn) = μ(m)μ(n) for ALL m, n without any coprimality restriction. This fails: μ(4) = 0 (since 4 = 2² is not squarefree), but μ(2)·μ(2) = (−1)(−1) = 1. Multiplicativity and complete multiplicativity are distinct properties, and confusing them leads to errors when computing μ on prime powers."

- question: "For every prime p, μ(p) = −1."
  type: true-false
  answer: true
  explanation: "Every prime p is squarefree (it has no squared prime factor) and is the product of exactly k = 1 distinct prime. Therefore μ(p) = (−1)¹ = −1. This is one of the simplest and most consistent facts about μ — it always assigns −1 to primes."

- question: "Explain why Möbius inversion is described as the 'deconvolution' operation for Dirichlet convolution, and give one example of a function relationship it can 'undo.'"
  type: short-answer
  answer: "Dirichlet convolution of two arithmetic functions f and g is (f * g)(n) = Σ_{d|n} f(d)g(n/d). The divisor-sum transform g(n) = Σ_{d|n} f(d) is exactly the Dirichlet convolution of f with the constant function 1: g = f * 1. Möbius inversion recovers f by convolving g with μ, since μ is the Dirichlet inverse of 1 (they satisfy 1 * μ = ε, where ε(n) = [n=1]). A canonical example: since Σ_{d|n} φ(d) = n, Möbius inversion immediately gives φ(n) = Σ_{d|n} μ(n/d)·d."
  explanation: "The key insight is that the divisor-sum g = f * 1 is an operation that loses information about f by averaging over divisors. Möbius inversion reverses this by convolving with μ, the multiplicative inverse of 1 in the Dirichlet ring. Without knowing this algebraic structure, deriving formulas like φ(n) = Σ μ(n/d)·d requires an ad hoc calculation; with it, the formula is immediate."
```

## Explainer

The **Möbius function** μ(n) is a number-theoretic tool that encodes information about the squarefree structure of an integer. Recall from your study of arithmetic functions and multiplicativity that a function is multiplicative if f(mn) = f(m)f(n) whenever gcd(m, n) = 1. The Möbius function is multiplicative, which makes it tractable to compute and work with. Its values are simple: μ(1) = 1; μ(n) = 0 if n has any squared prime factor (i.e., p² | n for some prime p); and if n = p₁p₂⋯pₖ is squarefree, then μ(n) = (−1)ᵏ — positive if k is even, negative if k is odd.

To build intuition, compute a few values. μ(6) = μ(2·3) = (−1)² = 1. μ(30) = μ(2·3·5) = (−1)³ = −1. μ(12) = μ(4·3) = 0 because 4 = 2² is a squared factor. The function oscillates between −1, 0, and 1, with zeroes at numbers divisible by any perfect square greater than 1. A foundational identity is Σ_{d|n} μ(d) = [n = 1], meaning the sum of μ over all divisors of n equals 1 if n = 1 and 0 otherwise. This is the key property that makes Möbius inversion work.

**Möbius inversion** is the technique: if you know that g(n) = Σ_{d|n} f(d) — that is, g is the "summatory" version of f over divisors — then you can recover f from g by f(n) = Σ_{d|n} μ(n/d)·g(d). Think of it as an inverse operation for the divisor-sum transform, analogous to how subtraction inverts addition. The proof uses the identity above: when you substitute the formula for g and rearrange, the μ-weighted sums collapse to [d = 1], isolating f(n).

The canonical application is deriving a formula for **Euler's totient function** φ(n). We know that Σ_{d|n} φ(d) = n — counting integers from 1 to n grouped by their gcd with n. This has the form g(n) = Σ_{d|n} f(d) with g(n) = n and f(n) = φ(n). Möbius inversion immediately gives φ(n) = Σ_{d|n} μ(n/d)·d, a formula that would be tedious to derive otherwise. More broadly, whenever a function in number theory is defined as a sum over divisors, Möbius inversion is the tool that peels it apart — it is the "deconvolution" operation for Dirichlet convolution, the multiplication structure that underlies all multiplicative arithmetic functions.
