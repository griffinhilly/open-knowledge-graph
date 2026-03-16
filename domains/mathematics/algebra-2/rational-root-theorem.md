---
id: rational-root-theorem
title: Rational Root Theorem
domain: mathematics
course: algebra-2
prerequisites:
  - id: factor-theorem
    type: hard
  - id: synthetic-division
    type: hard
builds-toward:
  - fundamental-theorem-of-algebra
tags: [polynomials, rational-roots, factoring, candidates]
stage: abstract-reasoning
status: validated
---

# Rational Root Theorem

## Core Idea
The Rational Root Theorem states that if a polynomial with integer coefficients has a rational root p/q (in lowest terms), then p divides the constant term and q divides the leading coefficient. This narrows the search for rational roots to a finite list of candidates, which can then be tested using synthetic division. Combined with the factor theorem, it provides a systematic method for factoring polynomials.

## How It's Best Learned
State the theorem and practice listing all possible rational roots for given polynomials. Test candidates systematically using synthetic division. Once one root is found, reduce the polynomial degree and repeat. Discuss limitations: the theorem only finds rational roots; irrational and complex roots require other methods.

## Common Misconceptions
- Listing candidates incorrectly (p divides the constant, q divides the leading coefficient, not vice versa).
- Forgetting negative candidates.
- Thinking every candidate in the list is actually a root (most are not; they must be tested).
- Assuming all polynomials have rational roots (many do not).

## Explainer

Factoring polynomials of degree 3 and higher requires a place to start. You know from the **Factor Theorem** that if r is a root of a polynomial f, then (x − r) is a factor. The challenge is finding r when you can't guess it. For polynomials with integer coefficients, the **Rational Root Theorem** provides a finite candidate list — transforming a search over all of ℝ into a manageable checklist.

The theorem states: if f(x) = aₙxⁿ + ... + a₀ has integer coefficients and p/q is a rational root in lowest terms, then p divides a₀ (the constant term) and q divides aₙ (the leading coefficient). For f(x) = 2x³ − 3x² − 11x + 6, the constant term is 6 with divisors ±1, ±2, ±3, ±6, and the leading coefficient is 2 with divisors ±1, ±2. Every possible rational root has the form (divisor of 6)/(divisor of 2), giving candidates: ±1, ±2, ±3, ±6, ±1/2, ±3/2. That's 12 values to test instead of infinitely many.

To test candidates, use **synthetic division**: divide f(x) by (x − r) and check whether the remainder is zero. If it is, r is a root and the quotient is the reduced polynomial. Testing x = 3 on the example above: synthetic division gives remainder 0 and quotient 2x² + 3x − 2, which factors as (2x − 1)(x + 2). Full factorization: (x − 3)(2x − 1)(x + 2). The strategy is systematic: work through candidates in order, and once you find one root, use the reduced polynomial to search for others (it has lower degree, so fewer candidates).

The theorem's limitations are as important as its power. It only finds **rational** roots. The polynomial x² − 2 has candidates ±1, neither of which works — its roots ±√2 are irrational, beyond the theorem's reach. Many degree-3 and higher polynomials have no rational roots at all. When every candidate fails, you've proven the polynomial has no rational factors — a conclusive result, not a failure. The theorem is a filter: it efficiently rules out rational roots and confirms them when they exist, but irrational and complex roots require other methods entirely.
