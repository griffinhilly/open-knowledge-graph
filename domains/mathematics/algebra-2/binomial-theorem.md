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
- id: multiplying-polynomials
  type: hard
builds-toward:
- probability-with-combinatorics
tags:
- binomial-theorem
- pascal-triangle
- combinations
- expansion
stage: abstract-reasoning
status: validated
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

## Explainer

You already know how to expand (a + b)² = a² + 2ab + b² and (a + b)³ = a³ + 3a²b + 3ab² + b³ by multiplying out. But what about (a + b)¹⁰ or (a + b)²⁰? Multiplying out twenty factors by hand is impractical, and the Binomial Theorem gives you a direct formula instead. The key insight is that the coefficients — 1, 2, 1 for (a+b)², and 1, 3, 3, 1 for (a+b)³ — are not arbitrary. They are **binomial coefficients** C(n,k), which you know from combinatorics as the number of ways to choose k items from n.

Here is why: when you expand (a + b)^n by multiplying out n copies of (a + b), each term in the expansion comes from choosing either the a or the b from each factor. To get the term a^(n-k)b^k, you must choose b from exactly k of the n factors and a from the remaining n-k. The number of ways to make that choice is C(n,k) = n!/(k!(n-k)!). So the term containing b^k appears exactly C(n,k) times, and the coefficient of a^(n-k)b^k in the expansion is C(n,k). The full expansion is the sum of all these terms as k runs from 0 to n.

The formula is (a + b)^n = Σ C(n,k) · a^(n-k) · b^k, summing from k=0 to n. Notice that the exponents of a and b always sum to n — every term has total degree n. There are n+1 terms (k = 0, 1, 2, ..., n). Pascal's Triangle arranges the coefficients visually: each row gives the coefficients for the corresponding power, and each entry is the sum of the two above it, which mirrors the identity C(n,k) = C(n-1,k-1) + C(n-1,k).

In practice, the Binomial Theorem is often used to find a specific term without expanding the whole polynomial. The (k+1)-th term of (a+b)^n is C(n,k) · a^(n-k) · b^k. For example, to find the 4th term (k=3) of (2x - 3)^7, plug in a = 2x, b = -3, n = 7, k = 3: C(7,3) · (2x)^4 · (-3)^3 = 35 · 16x⁴ · (-27) = -15,120x⁴. The negative sign comes from b = -3 raised to an odd power — a common place to make errors. The theorem turns what was a tedious multiplication into a single lookup and calculation.
