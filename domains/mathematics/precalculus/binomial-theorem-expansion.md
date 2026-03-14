---
id: binomial-theorem-expansion
title: Binomial Theorem Expansion
domain: mathematics
course: precalculus
prerequisites:
  - id: sequences-and-series-review
    type: soft
builds-toward:
  - taylor-polynomials
  - power-series
tags: [algebra, binomial, combinatorics]
stage: formal-systems
status: validated
---

# Binomial Theorem

## Core Idea
The Binomial Theorem gives the expansion of (a + b)^n as a sum of terms involving binomial coefficients: (a + b)^n = sum from k=0 to n of C(n,k) * a^(n-k) * b^k. The coefficients C(n,k) = n!/(k!(n-k)!) appear in Pascal's triangle. This result generalizes FOIL to any power and provides the foundation for the binomial series and Taylor expansions.

## How It's Best Learned
Start with small cases (n = 2, 3, 4) by hand to see the pattern. Introduce Pascal's triangle as a computation shortcut. Practice finding specific terms in an expansion (e.g., the x^5 term in (2x - 3)^8). Connect to combinatorics: C(n,k) counts the number of ways to choose k items from n.

## Common Misconceptions
- Forgetting to apply the exponents to both the coefficient and the variable in each term.
- Sign errors when b is negative: (-b)^k alternates sign.
- Confusing C(n,k) with permutations P(n,k).
