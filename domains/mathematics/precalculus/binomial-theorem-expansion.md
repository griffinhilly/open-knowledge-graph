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

## Questions

```yaml
- question: "What is the coefficient of x^3 in the expansion of (x + 2)^5?"
  type: multiple-choice
  options:
    - "10"
    - "40"
    - "80"
    - "20"
  answer: 1
  explanation: "The term with x^3 requires n - k = 3, so k = 2. The term is C(5,2)·x^3·2^2 = 10·4 = 40. Option A (10) is the error of using only C(5,2) and forgetting to raise the coefficient 2 to the power k. Option C (80) comes from incorrectly setting k = 3 — as if 'x^3 means k = 3' — which actually gives the x^2 term. Always solve for k from n - k = desired exponent."

- question: "What is the coefficient of y^3 in the expansion of (1 − y)^4?"
  type: multiple-choice
  options:
    - "4"
    - "−4"
    - "6"
    - "−6"
  answer: 1
  explanation: "Here a = 1, b = −y, n = 4, and k = 3. The term is C(4,3)·1^1·(−y)^3 = 4·(−1)^3·y^3 = −4y^3. The coefficient is −4. Option A (4) is the classic sign error — forgetting that (−y)^3 = −y^3. Option C and D involve using k = 2 by mistake. In any expansion of (a − b)^n, you must treat the full (−b) as the second term, so (−b)^k carries a sign of (−1)^k."

- question: "In the expansion of (a − b)^n, the terms alternate in sign because (−b)^k is negative for odd k and positive for even k."
  type: true-false
  answer: true
  explanation: "This is exactly correct. When you substitute −b for the second term, each term becomes C(n,k)·a^(n−k)·(−b)^k = C(n,k)·(−1)^k·a^(n−k)·b^k. Since (−1)^k = +1 for even k and −1 for odd k, the signs alternate: the k=0 term is positive, k=1 negative, k=2 positive, and so on."

- question: "The binomial coefficient C(n,k) equals the permutation P(n,k) = n!/(n−k)!, since both count the number of ways to choose k items from n."
  type: true-false
  answer: false
  explanation: "P(n,k) counts ordered selections; C(n,k) = n!/(k!(n−k)!) counts unordered selections. C(n,k) = P(n,k) / k! because each unordered group of k items can be arranged in k! different orders. In the binomial expansion, we want to count how many factors we pick b from — the order of the factors doesn't matter — so combinations C(n,k) are correct, not permutations."

- question: "Explain, in terms of multiplying out the n factors of (a + b)^n, why the coefficient of a^(n−k)·b^k is C(n,k)."
  type: short-answer
  answer: "When you distribute (a + b)^n, you choose one term — either a or b — from each of the n factors. To produce the monomial a^(n−k)·b^k, you must choose b from exactly k of the n factors (and a from the rest). The number of ways to choose which k factors contribute a b is C(n,k) = n!/(k!(n−k)!). Every such selection yields the same product, so C(n,k) identical terms combine into the coefficient C(n,k)·a^(n−k)·b^k."
  explanation: "This combinatorial argument is the conceptual heart of the theorem — the algebra is just collecting these choices. It also explains why C(n,k) appears in Pascal's triangle: the recursive identity C(n,k) = C(n−1,k−1) + C(n−1,k) says either the last factor contributes a b (C(n−1,k−1) ways to fill the rest) or it contributes an a (C(n−1,k) ways to fill the rest)."
```

## Explainer

The Binomial Theorem answers a question you have probably approached by hand: what is (a + b)³, or (a + b)⁵? When you expand (a + b)(a + b)(a + b) by distributing, you pick one term from each factor — either a or b — and multiply. The final sum collects all possible products of n such choices. The **binomial coefficient** C(n, k) = n!/(k!(n-k)!) counts the number of ways to pick exactly k b's (and therefore n-k a's) from n factors. That count is the coefficient of a^(n-k)·b^k in the expansion.

The full theorem states: **(a + b)ⁿ = Σ_{k=0}^{n} C(n,k) · a^(n-k) · b^k**. Reading term by term: k=0 gives C(n,0)·aⁿ = aⁿ (you chose a every time); k=1 gives C(n,1)·a^(n-1)·b = n·a^(n-1)·b (you chose b exactly once, n ways to do that); and so on to k=n, giving bⁿ. **Pascal's triangle** arranges these coefficients visually — each row n gives the coefficients for (a+b)ⁿ, and each entry is the sum of the two above it. This recursive structure matches the identity C(n,k) = C(n-1,k-1) + C(n-1,k), which says "either the new item is included (k-1 remaining choices from n-1) or it is not (k choices from n-1)."

A critical skill is finding a **specific term** without expanding the whole expression. The term with b^k is C(n,k)·a^(n-k)·b^k. For example, in (2x - 3)^8, the term with x^5 means n-k = 5, so k = 3. That term is C(8,3)·(2x)^5·(-3)^3 = 56·32x^5·(-27) = -48,384x^5. Notice two things: you must apply the coefficients inside the parentheses (2 and -3) to the appropriate powers, and the sign alternates because (-3)^k is negative for odd k. These are the two most common error sources.

The Binomial Theorem generalizes significantly. Replacing n with a non-integer or negative number gives the **binomial series** (a + b)^α = Σ C(α,k)·a^(α-k)·b^k, where C(α,k) = α(α-1)···(α-k+1)/k! and the sum runs to infinity. This is the foundation of Taylor expansions you will encounter next — for instance, (1+x)^(1/2) ≈ 1 + x/2 - x²/8 + ... near x = 0. The finite binomial theorem you are learning is the polynomial-degree case of this more general expansion, making it one of the most important identities in all of analysis.
