---
id: remainder-theorem
title: Remainder Theorem
domain: mathematics
course: algebra-2
prerequisites:
  - id: synthetic-division
    type: hard
  - id: polynomial-long-division
    type: hard
builds-toward:
  - factor-theorem
tags: [polynomials, remainder-theorem, evaluation]
stage: abstract-reasoning
status: validated
---

# Remainder Theorem

## Core Idea
The Remainder Theorem states that when a polynomial f(x) is divided by (x - c), the remainder equals f(c). This provides a quick way to evaluate polynomials: instead of substituting c into f(x), perform synthetic division and read the remainder. It also connects polynomial division to polynomial evaluation and lays the groundwork for the Factor Theorem.

## How It's Best Learned
Verify the theorem with examples: divide f(x) by (x - c) using synthetic division, then compute f(c) directly, and confirm they match. Practice using the theorem to evaluate polynomials efficiently. Give problems where the remainder is given and students must find unknown coefficients.

## Common Misconceptions
- Confusing the remainder theorem with the factor theorem (the factor theorem is the special case where the remainder is 0).
- Evaluating f(-c) instead of f(c) when dividing by (x - c).
- Thinking the theorem applies to non-polynomial functions.

## Questions

```yaml
- question: "What is the remainder when f(x) = x³ + 3x² − 2x + 5 is divided by (x − 2)?"
  type: multiple-choice
  options:
    - "21"
    - "13"
    - "5"
    - "0"
  answer: 0
  explanation: "By the Remainder Theorem, the remainder equals f(2) = 8 + 12 − 4 + 5 = 21. The most common error is using c = −2 instead of c = 2 when dividing by (x − 2), which gives f(−2) = −8 + 12 + 4 + 5 = 13 — the tempting wrong answer. The divisor (x − c) means c is positive when the sign in the factor is minus."

- question: "When f(x) = x³ + kx² − 4 is divided by (x + 1), the remainder is −7. What is k?"
  type: multiple-choice
  options:
    - "−2"
    - "2"
    - "−7"
    - "3"
  answer: 0
  explanation: "Dividing by (x + 1) means c = −1, so the Remainder Theorem gives f(−1) = −7. Substituting: (−1)³ + k(−1)² − 4 = −7 → −1 + k − 4 = −7 → k − 5 = −7 → k = −2. This demonstrates one of the most powerful uses of the theorem: turning remainder information into an equation for unknown coefficients."

- question: "The value of f(3) for any polynomial f(x) can be found by performing synthetic division of f(x) by (x − 3) and reading the remainder."
  type: true-false
  answer: true
  explanation: "This is exactly what the Remainder Theorem guarantees: the remainder when f(x) is divided by (x − c) equals f(c). Synthetic division with c = 3 and reading the final remainder is mathematically identical to substituting x = 3 into f(x). For high-degree polynomials, synthetic division is often computationally faster."

- question: "If the remainder when f(x) is divided by (x − c) equals zero, then c is a coefficient of f(x)."
  type: true-false
  answer: false
  explanation: "A zero remainder means f(c) = 0, making c a *root* of the polynomial — not a coefficient. This zero-remainder case is the Factor Theorem: f(c) = 0 if and only if (x − c) is a factor of f(x). Roots and coefficients are entirely different things; confusing them is a sign of not understanding what the theorem is actually claiming."

- question: "Why does dividing f(x) by (x − c) produce a remainder equal to f(c)? Explain the reasoning from the structure of polynomial division."
  type: short-answer
  answer: "Polynomial division gives f(x) = (x − c)·q(x) + r, where r is a constant (since dividing by a degree-1 polynomial leaves a degree-0 remainder). Substituting x = c into both sides: f(c) = (c − c)·q(c) + r = 0 + r = r. The left-hand factor (x − c) vanishes at x = c, leaving only the remainder — which must therefore equal f(c)."
  explanation: "The key move is substituting x = c into the division equation. The (x − c) factor becomes zero, collapsing the entire quotient term and isolating r on the right side. This algebraic argument is short but deep: it shows that the remainder is not just any number — it is structurally forced to equal the polynomial's value at the division point."
```

## Explainer

From polynomial long division and synthetic division, you know how to divide f(x) by a linear factor (x − c) to get a quotient q(x) and a remainder r: f(x) = (x − c)·q(x) + r. Notice that r is a constant — when you divide by a degree-1 polynomial, the remainder is degree 0 (just a number). The **Remainder Theorem** follows immediately: substitute x = c into both sides. The left side gives f(c). The right side gives (c − c)·q(c) + r = 0 + r = r. So f(c) = r. The remainder is not just any number — it is exactly the value of the polynomial at x = c.

This is a shortcut for polynomial evaluation. To find f(7) for f(x) = x⁴ − 3x³ + 2x − 5, you could substitute 7 directly and grind through four multiplications. Alternatively, perform synthetic division with c = 7 and read the remainder — it equals f(7). For high-degree polynomials or repeated evaluations, synthetic division is often faster than direct substitution, and the Remainder Theorem is the theorem that lets you interpret the remainder as a function value.

The theorem also inverts the question. Suppose you know that when f(x) = 2x³ + kx − 1 is divided by (x − 3), the remainder is 8. Then f(3) = 8, so 2(27) + 3k − 1 = 8, giving 54 + 3k − 1 = 8, so 3k = −45 and k = −15. The Remainder Theorem turns remainder information into an equation you can solve for unknown coefficients — a class of problems that would be awkward to approach any other way.

The natural special case is when the remainder equals zero: f(c) = 0 means c is a root of f. This is the **Factor Theorem** (your next topic): f(c) = 0 if and only if (x − c) is a factor of f(x). The Remainder Theorem is the general version; the Factor Theorem is the zero-remainder case. Together they form the bridge between roots of polynomials, factors of polynomials, and the synthetic division process — a trio of ideas that will dominate your work with higher-degree polynomials.


