---
id: polynomial-functions-degree-and-leading-coefficient
title: 'Polynomial Functions: Degree and Leading Coefficient'
domain: mathematics
course: algebra-2
prerequisites:
- id: graphing-quadratic-functions
  type: hard
- id: multiplying-polynomials
  type: hard
- id: quadratic-inequalities
  type: soft
builds-toward:
- end-behavior-of-polynomials
- graphing-polynomial-functions
tags:
- polynomials
- degree
- leading-coefficient
- classification
stage: abstract-reasoning
status: validated
---
# Polynomial Functions: Degree and Leading Coefficient

## Core Idea
A polynomial function is a sum of terms of the form a_n*x^n. The degree is the highest power of x with a nonzero coefficient. The leading coefficient is the coefficient of the highest-degree term. The degree determines the maximum number of turning points (at most n-1) and x-intercepts (at most n). Polynomials are classified by degree: linear (1), quadratic (2), cubic (3), quartic (4), quintic (5).

## How It's Best Learned
Identify degree and leading coefficient from various polynomial expressions, including those not in standard form (need to expand or combine like terms first). Graph examples of each degree to develop visual intuition. Discuss how degree affects the shape and complexity of the graph.

## Common Misconceptions
- Counting the number of terms instead of finding the highest power.
- Not combining like terms before identifying the degree.
- Thinking the degree equals the number of x-intercepts (it is the maximum number, not the exact number).

## Questions

```yaml
- question: "What is the degree of the polynomial p(x) = 5x³ - 2x⁴ + x - 7?"
  type: multiple-choice
  options: ["3", "4", "5", "1"]
  answer: 1
  explanation: "The degree is the highest power of x with a nonzero coefficient. Even though x⁴ is not the first term written, it is the highest-power term, so the degree is 4. This polynomial is not in standard form — the degree is determined by the highest power present, not the first term written."

- question: "A degree-4 polynomial generally has exactly 4 x-intercepts."
  type: true-false
  answer: false
  explanation: "The degree gives the maximum number of real x-intercepts, not the exact count. A degree-4 polynomial can have 0, 1, 2, 3, or 4 real x-intercepts. For example, f(x) = x⁴ + 1 has no real x-intercepts because x⁴ + 1 > 0 for all real x. Some intercepts may be complex (non-real) or repeated."

- question: "What is the degree and leading coefficient of p(x) = (x + 2)(x - 1)(x + 3)? You do not need to fully expand."
  type: short-answer
  answer: "Degree: 3. Leading coefficient: 1."
  explanation: "The highest-degree term comes from multiplying the leading x from each factor: x · x · x = x³. The coefficient of x³ is 1 (since each factor contributes a coefficient of 1). With three linear factors multiplied together, the degree must be 3. You can read off both values without expanding the entire product."
```

## Explainer

You've worked extensively with quadratics — polynomials of degree 2. Polynomial functions generalize this: they're sums of terms where each term is a constant times a non-negative integer power of x, and the degree is just the highest power that appears. The degree and leading coefficient are the two most important numbers for understanding a polynomial's shape and behavior.

The **degree** tells you the maximum complexity of the graph. A linear polynomial (degree 1) is a straight line. A quadratic (degree 2) is a parabola — one possible "hill" or "valley." A cubic (degree 3) can have up to two turning points. Each additional degree adds the possibility of one more turning point and one more x-intercept. The degree sets an upper bound, not a guarantee: a degree-4 polynomial can have 0, 2, or 4 real x-intercepts (always even for even degrees if the leading coefficient is positive and constant term is positive — but the key idea is that the exact count can vary).

The **leading coefficient** is the coefficient of the highest-degree term, once the polynomial is in standard form (highest power first). For 3x − 2x² + x⁴, written in standard form as x⁴ − 2x² + 3x, the leading coefficient is 1. For −5x³ + 2x − 1, it's −5. The sign and magnitude of the leading coefficient controls **end behavior** — what happens to the graph as x → +∞ and x → −∞ — which you'll study next.

A common source of confusion: when a polynomial is not in standard form, or when terms need to be combined, the leading term isn't obvious. For p(x) = 3x³ + x³ − 2x², you must first combine like terms: 4x³ − 2x², so the degree is 3 and the leading coefficient is 4. Similarly, when a polynomial is given as a product of factors like (x + 2)(x − 1)(x + 3), you can find the degree (3, since three linear factors multiply together) and leading coefficient (1, from x · x · x) without fully expanding.

The vocabulary — linear, quadratic, cubic, quartic, quintic — gives names to degrees 1 through 5. Each is worth graphing at least once to build a visual sense of how the degree shapes the curve. A cubic always has opposite end behaviors (one end up, one end down); an even-degree polynomial has the same end behavior on both sides (both up or both down depending on the leading coefficient's sign). These patterns all trace back to the degree and leading coefficient.
