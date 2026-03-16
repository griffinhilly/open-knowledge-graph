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

## Explainer

The Binomial Theorem answers a question you have probably approached by hand: what is (a + b)³, or (a + b)⁵? When you expand (a + b)(a + b)(a + b) by distributing, you pick one term from each factor — either a or b — and multiply. The final sum collects all possible products of n such choices. The **binomial coefficient** C(n, k) = n!/(k!(n-k)!) counts the number of ways to pick exactly k b's (and therefore n-k a's) from n factors. That count is the coefficient of a^(n-k)·b^k in the expansion.

The full theorem states: **(a + b)ⁿ = Σ_{k=0}^{n} C(n,k) · a^(n-k) · b^k**. Reading term by term: k=0 gives C(n,0)·aⁿ = aⁿ (you chose a every time); k=1 gives C(n,1)·a^(n-1)·b = n·a^(n-1)·b (you chose b exactly once, n ways to do that); and so on to k=n, giving bⁿ. **Pascal's triangle** arranges these coefficients visually — each row n gives the coefficients for (a+b)ⁿ, and each entry is the sum of the two above it. This recursive structure matches the identity C(n,k) = C(n-1,k-1) + C(n-1,k), which says "either the new item is included (k-1 remaining choices from n-1) or it is not (k choices from n-1)."

A critical skill is finding a **specific term** without expanding the whole expression. The term with b^k is C(n,k)·a^(n-k)·b^k. For example, in (2x - 3)^8, the term with x^5 means n-k = 5, so k = 3. That term is C(8,3)·(2x)^5·(-3)^3 = 56·32x^5·(-27) = -48,384x^5. Notice two things: you must apply the coefficients inside the parentheses (2 and -3) to the appropriate powers, and the sign alternates because (-3)^k is negative for odd k. These are the two most common error sources.

The Binomial Theorem generalizes significantly. Replacing n with a non-integer or negative number gives the **binomial series** (a + b)^α = Σ C(α,k)·a^(α-k)·b^k, where C(α,k) = α(α-1)···(α-k+1)/k! and the sum runs to infinity. This is the foundation of Taylor expansions you will encounter next — for instance, (1+x)^(1/2) ≈ 1 + x/2 - x²/8 + ... near x = 0. The finite binomial theorem you are learning is the polynomial-degree case of this more general expansion, making it one of the most important identities in all of analysis.
