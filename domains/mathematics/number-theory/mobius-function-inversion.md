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
status: validated
---

# Möbius Function and Möbius Inversion

## Core Idea
The Möbius function μ(n) is 0 if n has a squared prime factor, and (-1)^k if n is a product of k distinct primes. Möbius inversion states: if g(n) = Σ_{d|n} f(d), then f(n) = Σ_{d|n} μ(n/d)g(d), enabling inversion of divisor sums.

## Questions

```yaml
- question: "What is μ(12)?"
  type: multiple-choice
  options:
    - "1, because 12 has two distinct prime factors (2 and 3)"
    - "−1, because 12 has three prime factors counting multiplicity (2, 2, and 3)"
    - "0, because 12 = 2² · 3 contains a squared prime factor"
    - "−1, because μ(6) = 1 and 12 = 2·6 so signs alternate"
  answer: 2
  explanation: "The Möbius function is 0 whenever n has any prime factor appearing to a power greater than 1. Since 12 = 2² · 3, the prime 2 appears squared, so μ(12) = 0. The tempting distractor (option A) counts distinct prime factors correctly — there are two, 2 and 3 — but ignores the squarefreeness requirement. The key rule: μ(n) can only be ±1 when n is squarefree."

- question: "The Möbius inversion formula recovers f from g when g(n) = Σ_{d|n} f(d). Which identity is the algebraic engine that makes this inversion work?"
  type: multiple-choice
  options:
    - "μ is a multiplicative arithmetic function"
    - "Σ_{d|n} μ(d) = 1 for all n ≥ 1"
    - "Σ_{d|n} μ(d) = 1 if n = 1 and 0 otherwise"
    - "The Dirichlet series for μ(n) converges for Re(s) > 1"
  answer: 2
  explanation: "The identity Σ_{d|n} μ(d) = [n=1] is the orthogonality condition that makes inversion work. When you substitute g into the inversion formula and expand the double sum, cross terms vanish because Σ_{d|n} μ(d) = 0 for all n > 1, leaving only f(n). In Dirichlet convolution language, μ is the inverse of the constant function 1, so μ * 1 = ε (the multiplicative identity). Option A is true but insufficient: multiplicativity makes μ tractable, but the actual cancellation mechanism is the orthogonality identity."

- question: "If n is a product of exactly three distinct primes, then μ(n) = −1."
  type: true-false
  answer: true
  explanation: "If n = p·q·r for distinct primes p, q, r, then n is squarefree (no prime appears twice), so μ(n) = (−1)³ = −1. This is correct. The key is that 'product of k distinct primes' already implies squarefree — if the primes are distinct, none can appear twice. Compare with μ(12) = 0: 12 has two distinct prime factors but is not squarefree because 2 appears squared."

- question: "Möbius inversion only works when f is a multiplicative function — it fails for arbitrary arithmetic functions."
  type: true-false
  answer: false
  explanation: "The Möbius inversion formula f(n) = Σ_{d|n} μ(n/d)g(d) holds for any arithmetic function f — multiplicativity is not required. It is a general inversion result over the divisibility lattice. The formula follows from the single orthogonality identity Σ_{d|n} μ(d) = [n=1], which holds regardless of what f looks like. What multiplicativity helps with is efficient computation and nice Dirichlet series structure, not the inversion identity itself."

- question: "Explain in your own words why the Möbius function μ can 'undo' a divisor sum. What property of μ makes the inversion formula work?"
  type: short-answer
  answer: "The key property is the orthogonality identity Σ_{d|n} μ(d) = 1 if n = 1 and 0 if n > 1. In Dirichlet convolution language, μ * 1 = ε (where 1 is the constant function and ε is the identity). When g = 1 * f (meaning g(n) = Σ_{d|n} f(d)), convolving both sides with μ gives μ * g = μ * 1 * f = ε * f = f. The cancellation works because all the cross terms in the double sum vanish due to the orthogonality identity, leaving only f(n)."
  explanation: "This is the Dirichlet convolution perspective: μ is the multiplicative inverse of the constant function 1 in the ring of arithmetic functions under Dirichlet convolution. The sign-oscillation of μ (values +1, −1, 0) is precisely calibrated to cancel accumulated contributions across all divisors — an 'orthogonality' analogous to Fourier series over the divisibility lattice."
```

## Explainer

From your study of arithmetic functions and multiplicativity, you know that many number-theoretic quantities — like Euler's totient φ(n), the sum of divisors σ(n), and the number of divisors d(n) — are defined via sums over divisors of n. A natural question arises: if you know the divisor sum g(n) = Σ_{d|n} f(d), can you recover f(n)? Möbius inversion answers yes, and the **Möbius function** μ is the key.

The definition of μ(n) is sharp: μ(1) = 1; μ(n) = 0 if any prime appears squared in n's factorization; μ(n) = (−1)^k if n is a product of k distinct primes. In other words, μ detects squarefreeness and assigns a sign based on the number of prime factors. For example: μ(6) = μ(2·3) = (−1)² = 1, μ(30) = μ(2·3·5) = (−1)³ = −1, μ(12) = μ(2²·3) = 0. The function oscillates, but its local averages are controlled.

The **Möbius inversion formula** says: if g(n) = Σ_{d|n} f(d), then f(n) = Σ_{d|n} μ(n/d) g(d). Think of this as a "Fourier inversion" over the divisibility lattice. The multiplicativity of μ (a consequence of your prerequisite on arithmetic functions) makes this tractable. A key identity underpinning the whole theory is Σ_{d|n} μ(d) = [n=1] — the sum of μ over all divisors equals 1 if n = 1 and 0 otherwise. This is the "orthogonality" that makes inversion possible.

As a concrete application: you can recover φ(n) from the identity n = Σ_{d|n} φ(d) (which sums totient values over divisors). Inverting gives φ(n) = Σ_{d|n} μ(n/d) · d = n Σ_{d|n} μ(d)/d. Similarly, you can invert any multiplicative Dirichlet series using μ as the "inverse" of the constant function 1 in the ring of arithmetic functions under **Dirichlet convolution**. This algebraic structure — where Dirichlet convolution acts as multiplication and μ * 1 = ε (the identity) — unifies dozens of formulas in number theory and is the true reason Möbius inversion works.
