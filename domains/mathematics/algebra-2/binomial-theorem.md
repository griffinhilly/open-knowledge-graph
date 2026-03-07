---
id: binomial-theorem
title: Binomial Theorem
domain: mathematics
course: algebra-2
prerequisites:
  - id: sigma-notation
    type: soft
  - id: combinations
    type: hard
  - id: polynomial-multiplication
    type: hard
builds-toward:
  - probability-with-combinatorics
  - calculus-series
tags: [binomial-theorem, pascal-triangle, combinations, expansion]
stage: abstract-reasoning
status: draft
---

# Binomial Theorem

## Core Idea
The Binomial Theorem gives the expansion of (a + b)^n: the sum from k=0 to n of C(n,k) * a^(n-k) * b^k, where C(n,k) = n!/(k!(n-k)!) is the binomial coefficient. Pascal's Triangle provides these coefficients visually. The theorem generalizes FOIL to any positive integer power. Each term has degree n (the exponents of a and b sum to n), and there are n+1 terms total.

## How It's Best Learned
Start with manual expansion of (a+b)^2, (a+b)^3, (a+b)^4 and observe patterns. Introduce Pascal's Triangle as the coefficient pattern. Formalize with the binomial coefficient formula. Practice expanding specific binomials and finding specific terms (e.g., "the 4th term of (2x - 3)^7"). Connect to combinations.

## Common Misconceptions
- Forgetting that both a and b can be negative or involve variables (e.g., (x - 2)^5 uses b = -2).
- Miscounting terms (there are n+1 terms, not n).
- Errors in computing binomial coefficients.
- Forgetting that the exponents of a decrease while those of b increase.
