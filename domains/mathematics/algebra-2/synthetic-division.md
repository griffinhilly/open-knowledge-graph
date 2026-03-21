---
id: synthetic-division
title: Synthetic Division
domain: mathematics
course: algebra-2
prerequisites:
  - id: polynomial-long-division
    type: hard
builds-toward:
  - remainder-theorem
  - factor-theorem
  - rational-root-theorem
tags: [polynomials, division, synthetic-division, shortcut]
stage: abstract-reasoning
status: validated
---

# Synthetic Division

## Core Idea
Synthetic division is a shorthand method for dividing a polynomial by a linear divisor of the form (x - c). It uses only the coefficients and is faster than long division. The process: write c and the coefficients, bring down, multiply, add, repeat. The last number is the remainder, and the others are the quotient coefficients. Synthetic division is a computational shortcut, not a separate concept from long division.

## How It's Best Learned
First show synthetic division alongside long division for the same problem so students see the correspondence. Practice with various values of c, including negative and fractional. Emphasize including zero coefficients for missing terms. Show that it only works for linear divisors (x - c).

## Common Misconceptions
- Using the wrong sign for c (when dividing by x + 3, use c = -3, not +3).
- Forgetting placeholder zeros for missing degree terms.
- Trying to use synthetic division for divisors of degree 2 or higher (it only works for linear divisors).
- Confusing addition and multiplication steps.

## Questions

```yaml
- question: "You want to divide p(x) = x³ + 2x² − 5x + 1 by (x + 4). What value of c should you write in the box for synthetic division?"
  type: multiple-choice
  options:
    - "4"
    - "-4"
    - "-5"
    - "1"
  answer: 1
  explanation: "Synthetic division divides by (x − c), so you use the value of c — the opposite of the sign in the divisor. Since x + 4 = x − (−4), c = −4. Using c = 4 is the most common error in synthetic division. The pattern to remember: when the divisor is (x + k), c = −k. Getting the sign wrong flips every multiplication step and produces a completely incorrect result."

- question: "After performing synthetic division of p(x) by (x − 3), the last number in the synthetic division row is 7. What does this tell you about p(3)?"
  type: multiple-choice
  options:
    - "p(3) = 0, because the remainder represents the root at x = 3"
    - "p(3) = 7, by the Remainder Theorem — the remainder equals the polynomial evaluated at x = c"
    - "p(3) = 3, because c = 3 was used in the division"
    - "p(3) cannot be determined from the remainder alone"
  answer: 1
  explanation: "The Remainder Theorem states that when p(x) is divided by (x − c), the remainder equals p(c). So a remainder of 7 means p(3) = 7. Synthetic division simultaneously divides the polynomial and evaluates it at x = c. If the remainder were 0, that would mean x = 3 is a root. This connection makes synthetic division the computational engine for testing potential roots via the Factor Theorem."

- question: "When using synthetic division to divide a degree-4 polynomial by (x − 2), you must write exactly 5 numbers in the coefficient row — one for each degree from x⁴ down to x⁰, inserting 0 for any missing terms."
  type: true-false
  answer: true
  explanation: "Every degree position must be represented, even if its coefficient is zero. If the polynomial has no x² term, you must write 0 in that slot. Skipping a missing term shifts all remaining coefficients one position to the left, making every subsequent multiplication and addition wrong and producing a quotient with incorrectly assigned degrees."

- question: "Synthetic division can be used to divide a polynomial by any divisor, including quadratics like (x² − 3x + 2)."
  type: true-false
  answer: false
  explanation: "Synthetic division only works for linear divisors of the form (x − c). The algorithm's multiply-and-add pattern relies on the divisor having exactly one degree. For divisors of degree 2 or higher, the pattern breaks down and produces meaningless results; polynomial long division must be used instead. This restriction is the most important limitation to remember when choosing which method to apply."

- question: "Explain why the remainder in synthetic division equals p(c), and why this makes synthetic division more than just a computational shortcut."
  type: short-answer
  answer: "When p(x) is divided by (x − c), there exist quotient q(x) and remainder r such that p(x) = (x − c) · q(x) + r. Substituting x = c gives p(c) = (c − c) · q(c) + r = 0 + r = r. So the remainder must equal p(c). This means every synthetic division simultaneously divides the polynomial and evaluates it at x = c — making it a fast way to test whether c is a root (remainder = 0), which is the computational foundation of the Factor Theorem and Rational Root Theorem."
  explanation: "This algebraic connection is what elevates synthetic division from arithmetic shortcut to root-finding tool. Every time you perform synthetic division, you are implicitly answering 'does this polynomial equal zero at x = c?' without needing a separate evaluation step. Understanding this connection — rather than just memorizing the bring-down-multiply-add procedure — makes the method useful in the broader context of polynomial analysis."
```

## Explainer

You learned polynomial long division by analogy with numerical long division: divide, multiply, subtract, bring down, repeat. Synthetic division compresses that same process into a row of numbers, eliminating the x symbols entirely. It works only when the divisor is linear — of the form (x - c) — but that covers the most common case, and understanding why it works makes it easier to remember.

Consider dividing 2x³ - 3x² + x - 5 by (x - 2). In long division, every step either multiplies by 2 (the value of c) or subtracts. Synthetic division strips out the variables and just tracks what happens to the coefficients. Write c = 2 in a box, then the coefficients 2, -3, 1, -5 in a row. The algorithm is: bring down the first coefficient (2), multiply it by c (2 × 2 = 4), add it to the next coefficient (-3 + 4 = 1), multiply that result by c (1 × 2 = 2), add to the next (1 + 2 = 3), multiply by c again (3 × 2 = 6), add to the last (-5 + 6 = 1). The row reads 2, 1, 3, 1 — meaning the quotient is 2x² + x + 3 with remainder 1.

The crucial sign rule: when you write (x - c), c is the number you put in the box. For (x - 2), c = 2. For (x + 3) = (x - (-3)), c = -3. Getting the sign wrong flips all your multiplications wrong. Also, if a degree is missing in the original polynomial — say you're dividing x⁴ - 1 — you must include a 0 coefficient for every missing term: 1, 0, 0, 0, -1. Otherwise the positions of your result coefficients will all be wrong.

The reason synthetic division is worth learning is not just speed — it connects directly to the **Remainder Theorem** (which you will see next): when you synthetically divide p(x) by (x - c), the remainder equals p(c). So synthetic division simultaneously divides the polynomial and evaluates it at x = c. This makes it a fast way to test whether c is a zero, which feeds directly into the Factor Theorem and the Rational Root Theorem. Synthetic division is not just a shortcut — it is the computational engine for root-finding.
