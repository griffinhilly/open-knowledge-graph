---
id: fundamental-theorem-of-algebra
title: Fundamental Theorem of Algebra
domain: mathematics
course: algebra-2
prerequisites:
- id: complex-numbers-intro
  type: hard
- id: factor-theorem
  type: hard
- id: quadratic-formula-review
  type: soft
- id: graphing-polynomial-functions
  type: soft
- id: operations-with-complex-numbers
  type: soft
- id: rational-root-theorem
  type: soft
builds-toward:
- polynomial-division-review
tags:
- polynomials
- fundamental-theorem
- complex-roots
- degree
stage: abstract-reasoning
status: validated
---
# Fundamental Theorem of Algebra

## Core Idea
The Fundamental Theorem of Algebra states that every non-constant polynomial with complex coefficients has at least one complex root. A corollary: a degree-n polynomial has exactly n roots (counted with multiplicity) in the complex numbers. Complex roots of polynomials with real coefficients come in conjugate pairs: if a + bi is a root, so is a - bi. This theorem guarantees that the complex number system is "complete" for polynomial equations.

## How It's Best Learned
Start with examples: a degree-2 polynomial has 2 roots, a degree-3 has 3, etc. Show cases where some roots are complex (x^2 + 1 has roots i and -i). Emphasize the conjugate pairs property for real-coefficient polynomials. Practice writing polynomials given their roots (including complex ones). Do NOT attempt to prove the theorem; it requires analysis beyond Algebra 2.

## Common Misconceptions
- Thinking real roots and complex roots are separate categories (real numbers are complex numbers with imaginary part 0).
- Forgetting to count roots with multiplicity (x^2 = 0 has root x = 0 with multiplicity 2).
- Not recognizing the conjugate pairs requirement for real-coefficient polynomials.
- Thinking a degree-3 polynomial must have 3 real roots (it has 3 complex roots, of which 1 or 3 are real).

## Questions

```yaml
- question: "A degree-4 polynomial with real coefficients has roots 2, -1, and 3 + 2i. What must the fourth root be?"
  type: multiple-choice
  options:
    - "3 - 2i"
    - "-3 + 2i"
    - "-3 - 2i"
    - "There is no fourth root — a degree-4 polynomial can have fewer than 4 roots if one has high multiplicity"
  answer: 0
  explanation: "For a polynomial with real coefficients, complex roots always come in conjugate pairs: if a + bi is a root, then a - bi must also be a root. The conjugate of 3 + 2i is 3 - 2i, so that must be the fourth root. By the Fundamental Theorem, a degree-4 polynomial has exactly 4 roots counted with multiplicity — here all four are accounted for: 2, -1, 3 + 2i, and 3 - 2i. Option D is wrong: the theorem guarantees exactly n roots counted with multiplicity; a degree-4 polynomial always has 4."

- question: "A student argues that the cubic polynomial p(x) = x³ + x² + x + 1 might have no real roots, since all three roots could be complex. Is this argument valid?"
  type: multiple-choice
  options:
    - "Yes — the roots of a cubic depend entirely on its coefficients, and complex roots are always possible"
    - "No — for a polynomial with real coefficients of odd degree, complex roots come in conjugate pairs, so at least one root must be real"
    - "Yes — x³ + x² + x + 1 has no positive real roots by Descartes' Rule, confirming they could all be complex"
    - "No — the Fundamental Theorem guarantees all roots of a real polynomial are real numbers"
  answer: 1
  explanation: "Complex (non-real) roots of real-coefficient polynomials come in conjugate pairs, each pair accounting for 2 roots. A degree-3 polynomial has 3 roots total. If any non-real complex roots exist, they come in pairs — but you cannot have 1.5 pairs. The remaining unpaired root must be real. Therefore, any odd-degree real polynomial has at least one real root. (In this specific case, x = -1 is a root.) Option D is wrong — real polynomials can certainly have non-real complex roots; they just can't all be non-real when the degree is odd."

- question: "A degree-5 polynomial with real coefficients can have exactly 1 real root and 4 non-real complex roots."
  type: true-false
  answer: true
  explanation: "Four non-real complex roots can occur as two conjugate pairs — (a + bi, a - bi) and (c + di, c - di) — which is perfectly consistent with real coefficients. Together with 1 real root, that accounts for all 5 roots that a degree-5 polynomial must have. This is a valid root structure. In contrast, a degree-5 polynomial cannot have exactly 2 real and 3 non-real complex roots, because 3 non-real roots cannot all be arranged in conjugate pairs."

- question: "The polynomial x² - 6x + 9 = (x - 3)² has two distinct roots because it is a degree-2 polynomial and the Fundamental Theorem guarantees exactly two roots."
  type: true-false
  answer: false
  explanation: "The Fundamental Theorem guarantees exactly 2 roots counted *with multiplicity*, not 2 distinct roots. The polynomial (x - 3)² has root x = 3 with multiplicity 2 — it is a double root, not two separate roots. There is only one distinct root value. Multiplicity counts how many times a factor (x - r) appears in the complete factorization. Confusing 'n roots counted with multiplicity' with 'n distinct roots' is a common error: a degree-n polynomial can have fewer than n distinct roots, but always exactly n when multiplicity is counted."

- question: "A student argues: 'x² + 4 has no roots because there is no real number whose square equals -4.' How does the Fundamental Theorem of Algebra respond to this claim?"
  type: short-answer
  answer: "The student is correct over the real numbers but wrong overall. The Fundamental Theorem guarantees that x² + 4 has exactly 2 roots in the complex numbers: x = 2i and x = -2i. These are non-real complex numbers (imaginary part ≠ 0) that satisfy the equation: (2i)² + 4 = -4 + 4 = 0. The theorem's key claim is that the complex number system is algebraically closed — every non-constant polynomial has exactly as many roots as its degree when complex numbers are allowed. Real numbers are not algebraically closed because polynomials like x² + 4 escape them."
  explanation: "The student's argument shows why real numbers alone are insufficient for polynomial algebra: some degree-n polynomials have fewer than n real roots (or none at all), breaking the elegant count that the Fundamental Theorem promises. Complex numbers were historically introduced precisely to fix this gap. Once you accept complex numbers, x² + 4 behaves like any other degree-2 polynomial — two roots, found by solving x² = -4, which gives x = ±√(-4) = ±2i. The theorem transforms a patchwork of special cases into a single universal guarantee."
```

## Explainer

You've already studied complex numbers and the Factor Theorem. Now you have the tools to appreciate one of the most satisfying guarantees in all of mathematics. The **Fundamental Theorem of Algebra** says: every polynomial equation of degree n ≥ 1 has exactly n roots — but only if you allow complex numbers. Over the real numbers, polynomials can run out of roots (x² + 1 = 0 has no real solution). Over the complex numbers, they never do.

The Factor Theorem tells you that if r is a root of p(x), then (x - r) is a factor. The Fundamental Theorem guarantees the first root always exists, so you can always factor out at least one linear factor. Apply the theorem again to the remaining degree-(n-1) polynomial — it too has a root, so factor out another linear factor. Repeat until you've extracted all n factors. The conclusion: every degree-n polynomial factors completely as p(x) = a(x - r₁)(x - r₂)···(x - rₙ), where r₁, ..., rₙ are the n roots (counted with **multiplicity**) in ℂ. Multiplicity matters: x² = (x - 0)(x - 0) has root 0 with multiplicity 2, which still counts as 2 roots.

For polynomials with real coefficients, complex roots always come in **conjugate pairs**: if a + bi is a root, so is a - bi. This is because the coefficients are real, so taking the complex conjugate of the equation p(r) = 0 gives p(r̄) = 0. Practically: a degree-4 real polynomial with roots 2 and 3 + i must also have root 3 - i, accounting for 3 of its 4 roots. The fourth root must be real (since complex roots come in pairs). Similarly, a real polynomial of odd degree must have at least one real root — complex non-real roots pair up, and a single root is left over that must be real.

Think of the theorem as a completeness certificate. The real numbers are not **algebraically closed** — they leave x² + 1 = 0 unsolved. The complex numbers are algebraically closed: you never need to invent a new number system to solve polynomial equations. This is why complex numbers are not just useful in algebra, but central to it. In practice, the theorem guides every polynomial factoring problem: know the degree, know the exact count of roots, apply the conjugate pairs rule to constrain which roots are real.
