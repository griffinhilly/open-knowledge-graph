---
id: polynomial-division-review
title: Polynomial Division Review
domain: mathematics
course: precalculus
prerequisites:
  - id: variable-expressions
    type: hard
builds-toward:
  - rational-functions-asymptotes-review
  - partial-fractions
tags: [polynomials, division, algebra-review]
stage: formal-systems
status: validated
---

# Polynomial Division Review

## Core Idea
Polynomial long division and synthetic division are algorithms for dividing one polynomial by another, producing a quotient and remainder. This is the polynomial analogue of integer long division. The result can be written as f(x) = d(x) * q(x) + r(x). This skill is essential for finding oblique asymptotes of rational functions, factoring polynomials, and performing partial fraction decomposition.

## How It's Best Learned
Practice long division first with clear, step-by-step layout. Introduce synthetic division as a shortcut when dividing by linear factors (x - c). Connect to the Remainder Theorem: f(c) equals the remainder when dividing f(x) by (x - c).

## Common Misconceptions
- Forgetting to include zero-coefficient placeholder terms (e.g., 0x^2).
- Applying synthetic division when the divisor is not linear.
- Sign errors in synthetic division when dividing by (x + c) instead of (x - c).

## Questions

```yaml
- question: "You want to use synthetic division to divide x³ - 2x² + 5 by x² - 1. What is the problem?"
  type: multiple-choice
  options:
    - "You cannot use synthetic division here because the divisor is not of the form x - c"
    - "The dividend has degree greater than 2, so synthetic division does not apply"
    - "There is no problem — synthetic division works for any divisor"
    - "You must first divide by x - 1, then divide again by x + 1"
  answer: 0
  explanation: "Synthetic division only works when the divisor is a linear polynomial of the exact form x - c (degree 1, leading coefficient 1). A quadratic divisor like x² - 1 requires polynomial long division. While x² - 1 = (x-1)(x+1) means you could divide by each factor separately, that is a multi-step process — not a direct application of synthetic division."

- question: "If f(x) = x⁴ - 3x² + x - 7 and you divide f(x) by (x + 2), the Remainder Theorem says the remainder equals:"
  type: multiple-choice
  options:
    - "f(2) = 16 - 12 + 2 - 7 = -1"
    - "f(-2) = 16 - 12 - 2 - 7 = -5"
    - "0, because -2 must be a root"
    - "f(0) = -7, the constant term"
  answer: 1
  explanation: "The Remainder Theorem states that dividing f(x) by (x - c) gives remainder f(c). Since the divisor is (x + 2) = (x - (-2)), we use c = -2. f(-2) = (-2)⁴ - 3(-2)² + (-2) - 7 = 16 - 12 - 2 - 7 = -5. Option A uses c = +2 — the classic sign error that occurs when students forget that dividing by (x + 2) means c = -2, not +2."

- question: "If f(3) = 0, then (x - 3) is guaranteed to be a factor of f(x)."
  type: true-false
  answer: true
  explanation: "By the Remainder Theorem, the remainder when f(x) is divided by (x - 3) equals f(3). If f(3) = 0, the remainder is 0, which means (x - 3) divides f(x) evenly — it is a factor. This is the Factor Theorem, a direct consequence of the Remainder Theorem. It provides a powerful method for factoring: evaluate at candidate roots, and zeros produce linear factors."

- question: "Synthetic division can be used to divide 2x³ - x + 4 by 2x - 3."
  type: true-false
  answer: false
  explanation: "Standard synthetic division requires the divisor to have the form x - c: degree 1 and leading coefficient exactly 1. The divisor 2x - 3 has leading coefficient 2, not 1. Applying synthetic division without adjusting for the leading coefficient produces an incorrect quotient. You would need to use polynomial long division or factor out the 2 first."

- question: "Explain why synthetic division is equivalent to evaluating the polynomial at x = c when the divisor is (x - c)."
  type: short-answer
  answer: "By the Remainder Theorem, the remainder when f(x) is divided by (x - c) equals f(c). Synthetic division computes this remainder as its final entry. So running synthetic division with value c is a numerically efficient way to evaluate f(c) — essentially Horner's method for polynomial evaluation, which organizes the arithmetic to minimize operations."
  explanation: "This connection transforms synthetic division from a mere algebraic shortcut into a polynomial evaluation algorithm. For a degree-n polynomial, synthetic division evaluates f(c) in n multiplications and n additions, the same count as direct substitution but with better numerical organization. The Remainder Theorem is the bridge: dividing by (x - c) and evaluating at x = c are mathematically identical operations."
```

## Explainer

You already know how to manipulate variable expressions and combine like terms. **Polynomial long division** extends this to dividing polynomials, using the exact same logic as integer long division — the algorithm you learned for dividing numbers like 748 ÷ 23. The key insight is that both work by repeatedly asking: "how many times does the divisor fit into the leading term of what remains?"

Here is the pattern: to divide f(x) = 2x³ − 3x + 1 by d(x) = x − 2, ask how many times x goes into 2x³. The answer is 2x², so write 2x² as the first term of the quotient, multiply back (2x² · (x − 2) = 2x³ − 4x²), and subtract from f(x). This leaves 4x² − 3x + 1. Repeat: x goes into 4x² exactly 4x times, multiply back, subtract. Continue until the remainder has degree less than the divisor. The result is f(x) = (x − 2)(2x² + 4x + 5) + 11, meaning the quotient is 2x² + 4x + 5 with remainder 11. The structure is always f(x) = d(x) · q(x) + r(x) — exactly the **division algorithm**, a polynomial analogue of the integer fact that 748 = 23 × 32 + 12.

**Synthetic division** is a streamlined shortcut for the special case where the divisor is linear — specifically x − c. Instead of carrying the variable symbols, you just work with the coefficients in a row. For dividing by x − 2, you write c = 2 in the corner, list the coefficients of f(x) across the top, and proceed by bring-down, multiply-by-c, add. The last number in the row is the remainder. Synthetic division is faster once you're comfortable with it, but it only works when the divisor has the form x − c (degree 1, leading coefficient 1). Notice the sign convention: dividing by x − 2 uses c = +2, and dividing by x + 3 uses c = −3.

The **Remainder Theorem** connects the remainder directly to function evaluation: when f(x) is divided by x − c, the remainder equals f(c). This means synthetic division doubles as a method for evaluating polynomials at specific points. If you want to know f(7) for a degree-4 polynomial, synthetic division with c = 7 gives you the answer in fewer arithmetic operations than plugging 7 directly into the formula. This connection also underlies the **Factor Theorem**: x − c is a factor of f(x) if and only if f(c) = 0, which is to say the remainder is zero. Both theorems make polynomial division far more powerful than it first appears — it's not just a mechanical algorithm, but a tool for factoring and root-finding that you'll use in rational functions and partial fraction decomposition.
