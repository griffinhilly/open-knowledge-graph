---
id: prime-number-theorem
title: Prime Number Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: distribution-of-primes
  type: hard
tags:
- prime-number-theorem
- analytic-number-theory
- primes
stage: advanced
status: draft
---

# Prime Number Theorem

## Core Idea
The Prime Number Theorem states that π(x) ~ x/ln(x), where π(x) counts primes up to x. Conjectured by Gauss and Legendre, it was proved in 1896 using complex analysis of the Riemann zeta function. It shows primes have asymptotic density 1/ln(x) near x.

## Explainer

From studying the distribution of primes, you know that primes become less frequent as numbers grow larger. But how much less frequent, exactly? The Prime Number Theorem gives a precise asymptotic answer. Let **π(x)** denote the count of primes up to x. The theorem states that π(x) ~ x / ln(x), meaning the ratio π(x) / (x / ln(x)) approaches 1 as x → ∞. The tilde notation means asymptotic equivalence — the approximation becomes arbitrarily accurate in relative terms as x grows.

To build intuition, think of a random number near x. The theorem says it is prime with approximate probability 1/ln(x). Near 1,000, about 1 in 7 numbers is prime (ln(1000) ≈ 6.9). Near 1,000,000, about 1 in 14. Near 10^100, about 1 in 230. Primes thin out slowly — logarithmically slowly — which is fast enough that the sum of reciprocals of primes diverges, but slow enough that their density approaches zero. Gauss and Legendre conjectured this law in the late 1700s from extensive tables of primes, but the proof had to wait a century for the tools of complex analysis.

The proof, independently achieved by Hadamard and de la Vallée Poussin in 1896, passes through the **Riemann zeta function** ζ(s) = Σ 1/n^s for Re(s) > 1. Euler had already connected this series to primes via the product formula ζ(s) = ∏ (1 - p^{-s})^{-1}, where the product runs over all primes. This identity encodes the fundamental theorem of arithmetic analytically: each prime contributes one factor. The distribution of primes is controlled by the zeros of ζ(s) in the complex plane. The critical step in the proof is showing that ζ(s) has no zeros on the vertical line Re(s) = 1. This non-vanishing, combined with analytic continuation and Fourier-type arguments, yields the asymptotic.

The theorem also has a more precise form: π(x) ~ Li(x) = ∫₂^x dt / ln(t), the **logarithmic integral**, which approximates π(x) far more accurately than x/ln(x). For x = 10^6, the true count is π(x) = 78,498 while Li(x) ≈ 78,628 and x/ln(x) ≈ 72,382 — the logarithmic integral wins by a factor of roughly 10 in absolute error. The **Riemann Hypothesis**, which conjectures that all non-trivial zeros of ζ(s) lie on the critical line Re(s) = 1/2, would give the sharpest possible error bounds on how well Li(x) approximates π(x): the error would be O(√x · ln(x)), a statement about the fine structure of primes that remains unproved after 160 years.
