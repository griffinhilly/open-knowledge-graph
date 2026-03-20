---
id: factor-theorem
title: Factor Theorem
domain: mathematics
course: algebra-2
prerequisites:
  - id: remainder-theorem
    type: hard
builds-toward:
  - rational-root-theorem
  - fundamental-theorem-of-algebra
tags: [polynomials, factor-theorem, zeros, roots]
stage: abstract-reasoning
status: validated
---

# Factor Theorem

## Core Idea
The Factor Theorem is a corollary of the Remainder Theorem: (x - c) is a factor of f(x) if and only if f(c) = 0. In other words, c is a zero (root) of f(x) exactly when (x - c) divides f(x) evenly. This connects the algebraic concept of factoring with the graphical concept of x-intercepts: every zero of the polynomial corresponds to a linear factor.

## How It's Best Learned
Given a polynomial and a candidate zero, use synthetic division or direct evaluation to test whether it is a root. If the remainder is 0, write the factorization. Practice finding all factors of a polynomial by combining the factor theorem with the rational root theorem. Connect zeros to x-intercepts on the graph.

## Common Misconceptions
- Confusing roots (values of x where f(x) = 0) with factors ((x - c) divides f(x)).
- Forgetting the sign: if c is a root, the factor is (x - c), not (x + c).
- Thinking the factor theorem provides a method for finding roots (it only tests candidates; the rational root theorem provides candidates).

## Questions

```yaml
- question: "You are told that f(3) = 0. Which of the following is therefore a factor of f(x)?"
  type: multiple-choice
  options:
    - "(x + 3)"
    - "(x − 3)"
    - "(3x)"
    - "(x · f(3))"
  answer: 1
  explanation: "The Factor Theorem states: if c is a root (f(c) = 0), then (x − c) is a factor. With c = 3, the factor is (x − 3), not (x + 3). The sign flip is the most common error: students see the root '3' and write '+3' in the factor. Remember the factor always uses subtraction: (x minus the root)."

- question: "A student evaluates f(2) = 0 for the polynomial f(x) = x³ − 6x² + 11x − 6. What is the correct next step to find all remaining roots?"
  type: multiple-choice
  options:
    - "Evaluate f at several other integers until finding values where f(c) = 0, then list all such c as roots"
    - "Divide f(x) by (x − 2) to obtain a quotient polynomial of lower degree, then factor or solve that quotient"
    - "Apply the quadratic formula to f(x) after substituting x = 2 into the quadratic terms"
    - "Conclude that x = 2 is the only root, since the Factor Theorem was already applied"
  answer: 1
  explanation: "Once (x − 2) is confirmed as a factor, synthetic or long division peels it off: f(x) ÷ (x − 2) gives a degree-2 quotient that can be factored by inspection or the quadratic formula. This 'testing and peeling' process dismantles the polynomial one factor at a time. Option A is the brute-force approach and misses the efficiency of division; option D incorrectly assumes a cubic has only one real root."

- question: "The Factor Theorem tells you which values of c to test as potential roots of a polynomial."
  type: true-false
  answer: false
  explanation: "The Factor Theorem only confirms or refutes a candidate: if you evaluate f(c) and get 0, the theorem tells you (x − c) is a factor. It does not supply the candidates to try. That job belongs to the Rational Root Theorem, which lists all possible rational roots based on the leading coefficient and constant term. The two theorems work in tandem: Rational Root Theorem provides the candidates; Factor Theorem tests them."

- question: "If (x − c) is a factor of f(x), then the graph of y = f(x) crosses or touches the x-axis at the point (c, 0)."
  type: true-false
  answer: true
  explanation: "This is the geometric leg of the three-way equivalence at the heart of the Factor Theorem: c is a zero of f (f(c) = 0) ↔ (x − c) is a factor of f(x) ↔ the graph of y = f(x) has an x-intercept at (c, 0). Each description says the same thing in a different language — algebraic (root), algebraic-structural (factor), and geometric (intercept)."

- question: "Explain the three-way equivalence stated in the Factor Theorem, connecting the concepts of a zero, a factor, and an x-intercept."
  type: short-answer
  answer: "For a polynomial f(x), these three statements are all equivalent — if any one is true, all three are true: (1) c is a zero of f, meaning f(c) = 0; (2) (x − c) is a factor of f(x), meaning f(x) = (x − c)·q(x) for some polynomial q with no remainder; (3) (c, 0) is an x-intercept of the graph of y = f(x). Finding a root graphically tells you a factor; confirming a factor algebraically tells you an x-intercept. The theorem bridges the algebraic and geometric representations of polynomials."
  explanation: "This three-way equivalence is what makes the Factor Theorem powerful rather than a mere corollary of the Remainder Theorem. It means you can move freely between representations: use a graph to spot an approximate intercept, test the nearby integer with f(c), and if it's zero, write the factor and divide it out. Each representation gives you information the others make use of."
```

## Explainer

The **Remainder Theorem**, your prerequisite, tells you that when you divide a polynomial f(x) by (x − c), the remainder is exactly f(c). The Factor Theorem asks: what if the remainder is zero? If f(c) = 0, then (x − c) divides f(x) with no remainder — meaning (x − c) is a **factor** of f(x). And if (x − c) is a factor, then substituting x = c into f(x) gives zero. These two directions together form an "if and only if": c is a root of f exactly when (x − c) is a factor.

This creates a three-way equivalence connecting algebra and geometry. For a polynomial f(x): (1) c is a **zero** — f(c) = 0. (2) (x − c) is a **factor** — f(x) = (x − c) · q(x) for some polynomial q. (3) c is an **x-intercept** — the graph of y = f(x) crosses or touches the x-axis at the point (c, 0). These three descriptions say the same thing. When you find a root graphically, you know the factor. When you confirm a factor algebraically, you know the intercept.

In practice, the theorem is used as a testing and peeling tool. Suppose f(x) = x³ − 6x² + 11x − 6 and you suspect x = 2 is a root. Evaluate: f(2) = 8 − 24 + 22 − 6 = 0. ✓ So (x − 2) is a factor. Divide f(x) by (x − 2) — using synthetic division or long division — to get the quotient q(x) = x² − 4x + 3. Now factor q: (x − 1)(x − 3). The full factorization is (x − 2)(x − 1)(x − 3), and all three roots appear as the constants with reversed sign: 1, 2, 3.

Notice what the theorem does and does not do: it **confirms** a root and **extracts** the corresponding factor, but it does not tell you which c to try first. That job belongs to the Rational Root Theorem, which provides the candidates. The Factor Theorem is the test — once you have a candidate, evaluate f(c); if the result is zero, you've found a factor. Together, these two tools let you systematically dismantle a polynomial into linear (and eventually irreducible quadratic) pieces, which is the foundation for everything from solving higher-degree equations to analyzing rational functions.
