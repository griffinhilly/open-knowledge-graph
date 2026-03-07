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
status: draft
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
