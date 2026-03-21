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
stage: formal-systems
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

## Questions

```yaml
- question: "What is the 4th term (k = 3) in the expansion of (x - 2)^6?"
  type: multiple-choice
  options:
    - "C(6,3) · x³ · 2³ = 160x³"
    - "C(6,3) · x³ · (-2)³ = -160x³"
    - "C(6,3) · x³ · 2³ = 20x³"
    - "C(6,4) · x⁴ · (-2)² = 60x⁴"
  answer: 1
  explanation: "The (k+1)-th term is C(n,k)·a^(n-k)·b^k. Here n=6, k=3, a=x, b=-2. So: C(6,3)·x^(6-3)·(-2)^3 = 20·x³·(-8) = -160x³. The two most common errors are: (1) forgetting that b = -2, not +2, so (-2)^3 = -8, not +8; and (2) computing the wrong binomial coefficient. C(6,3) = 6!/(3!·3!) = 20, not 160. The negative sign is essential — dropping it is the typical mistake."

- question: "How many terms are in the expansion of (a + b)^8?"
  type: multiple-choice
  options:
    - "8 terms — one for each power of b from b¹ to b⁸"
    - "8 terms — matching the exponent"
    - "9 terms — one for each value of k from 0 to 8"
    - "16 terms — each factor of (a + b) contributes two terms"
  answer: 2
  explanation: "The expansion sums over k = 0, 1, 2, ..., n — that is n+1 values, giving n+1 terms. For n=8, there are 9 terms. The k=0 term is a⁸ (no b), and the k=8 term is b⁸ (no a). A very common error is to say 'n terms' because the exponent is n, but the count is always one more than the exponent. Check with (a+b)²: it produces 3 terms (a², 2ab, b²), not 2."

- question: "The expansion of (a + b)^n has exactly n terms."
  type: true-false
  answer: false
  explanation: "The expansion of (a + b)^n has n+1 terms, corresponding to k = 0, 1, 2, ..., n. The off-by-one error is pervasive: students see the exponent n and expect n terms, forgetting that the k=0 term (which is aⁿ, with b absent) is still a term in the expansion. For example, (a+b)³ = a³ + 3a²b + 3ab² + b³ has 4 terms, not 3."

- question: "In the expansion of (a + b)^n, the exponents of a and b in any single term always sum to n."
  type: true-false
  answer: true
  explanation: "Every term has the form C(n,k)·a^(n-k)·b^k. The exponent of a is (n-k) and the exponent of b is k, so their sum is (n-k)+k = n. This reflects the combinatorial structure: each term arises from choosing a or b from each of the n factors of (a+b), and the total count of choices is always n. Every term therefore has total degree n — the expansion is homogeneous of degree n."

- question: "Explain why the coefficient of a^(n-k)b^k in the expansion of (a + b)^n is C(n, k). What combinatorial reasoning justifies this?"
  type: short-answer
  answer: "When (a+b)^n is expanded by multiplying out n copies of (a+b), each term is formed by picking either a or b from each factor. To get the term a^(n-k)b^k, you must choose b from exactly k of the n factors (and a from the remaining n-k). The number of ways to choose which k factors contribute the b is C(n,k) = n!/(k!(n-k)!). Since each such selection produces the same monomial a^(n-k)b^k, that term appears C(n,k) times in the product — giving it coefficient C(n,k)."
  explanation: "The combinatorial interpretation is the heart of the theorem. C(n,k) isn't an arbitrary formula — it counts selections, and each selection corresponds to a distinct way of obtaining the same monomial when multiplying n factors. This also explains the symmetry C(n,k) = C(n,n-k): choosing k positions for b is equivalent to choosing n-k positions for a. Pascal's Triangle organizes these counts visually, and the identity C(n,k) = C(n-1,k-1) + C(n-1,k) mirrors the recursive structure of multiplication."
```

## Explainer

You already know how to expand (a + b)² = a² + 2ab + b² and (a + b)³ = a³ + 3a²b + 3ab² + b³ by multiplying out. But what about (a + b)¹⁰ or (a + b)²⁰? Multiplying out twenty factors by hand is impractical, and the Binomial Theorem gives you a direct formula instead. The key insight is that the coefficients — 1, 2, 1 for (a+b)², and 1, 3, 3, 1 for (a+b)³ — are not arbitrary. They are **binomial coefficients** C(n,k), which you know from combinatorics as the number of ways to choose k items from n.

Here is why: when you expand (a + b)^n by multiplying out n copies of (a + b), each term in the expansion comes from choosing either the a or the b from each factor. To get the term a^(n-k)b^k, you must choose b from exactly k of the n factors and a from the remaining n-k. The number of ways to make that choice is C(n,k) = n!/(k!(n-k)!). So the term containing b^k appears exactly C(n,k) times, and the coefficient of a^(n-k)b^k in the expansion is C(n,k). The full expansion is the sum of all these terms as k runs from 0 to n.

The formula is (a + b)^n = Σ C(n,k) · a^(n-k) · b^k, summing from k=0 to n. Notice that the exponents of a and b always sum to n — every term has total degree n. There are n+1 terms (k = 0, 1, 2, ..., n). Pascal's Triangle arranges the coefficients visually: each row gives the coefficients for the corresponding power, and each entry is the sum of the two above it, which mirrors the identity C(n,k) = C(n-1,k-1) + C(n-1,k).

In practice, the Binomial Theorem is often used to find a specific term without expanding the whole polynomial. The (k+1)-th term of (a+b)^n is C(n,k) · a^(n-k) · b^k. For example, to find the 4th term (k=3) of (2x - 3)^7, plug in a = 2x, b = -3, n = 7, k = 3: C(7,3) · (2x)^4 · (-3)^3 = 35 · 16x⁴ · (-27) = -15,120x⁴. The negative sign comes from b = -3 raised to an odd power — a common place to make errors. The theorem turns what was a tedious multiplication into a single lookup and calculation.
