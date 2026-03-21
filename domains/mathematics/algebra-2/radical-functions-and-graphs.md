---
id: radical-functions-and-graphs
title: Radical Functions and Graphs
domain: mathematics
course: algebra-2
prerequisites:
  - id: square-roots-intro
    type: hard
  - id: inverse-functions
    type: soft
builds-toward:
  - solving-radical-equations
  - rational-exponents
tags: [radicals, functions, graphing, domain, square-root]
stage: formal-systems
status: validated
---

# Radical Functions and Graphs

## Core Idea
A radical function involves a variable under a radical sign, such as f(x) = sqrt(x), cbrt(x), or sqrt(ax + b). The square root function has domain [0, infinity) and range [0, infinity), producing a half-parabola shape. Transformations (shifts, stretches, reflections) apply as usual. The cube root function has domain and range both all reals. Radical functions are inverses of power functions (restricted to appropriate domains).

## How It's Best Learned
Graph the parent functions y = sqrt(x) and y = cbrt(x). Apply transformations systematically: y = a*sqrt(x - h) + k. Discuss domain restrictions (radicand must be non-negative for even roots). Connect to inverse functions: y = sqrt(x) is the inverse of y = x^2 for x >= 0.

## Common Misconceptions
- Thinking sqrt(x) is defined for negative x (it is not, in the reals).
- Confusing domain restrictions for even and odd roots (even roots require non-negative radicand; odd roots accept all reals).
- Forgetting that y = sqrt(x) gives only the positive root, not both.

## Questions

```yaml
- question: "What is the domain of f(x) = √(3 − 2x)?"
  type: multiple-choice
  options:
    - "All real numbers, since x can be any value"
    - "x ≥ 3/2, since we need 3 − 2x to be non-negative"
    - "x ≤ 3/2, since we need 3 − 2x to be non-negative"
    - "x ≥ 0, since x must be non-negative to appear under a square root"
  answer: 2
  explanation: "For a square root, the radicand must be non-negative: 3 − 2x ≥ 0 → −2x ≥ −3 → x ≤ 3/2. The domain is (−∞, 3/2]. Option D is the most common error: it's the radicand (the expression under the radical) that must be non-negative, not x itself. Option B reverses the inequality — dividing by a negative number (−2) flips the direction."

- question: "Why does f(x) = ∛x accept negative inputs like x = −8, while f(x) = √x does not?"
  type: multiple-choice
  options:
    - "Cube roots are defined differently as a matter of mathematical convention"
    - "Negative numbers have real cube roots because cubing preserves sign, while no real number squared gives a negative result"
    - "The cube root function uses a different branch cut that allows complex inputs"
    - "Both functions actually accept all real inputs; √(−8) simply gives an imaginary output"
  answer: 1
  explanation: "The key distinction is what happens to signs under the inverse operation. Squaring always gives a non-negative result: no real number x satisfies x² = −1, so there is no real square root of a negative number. But cubing preserves sign: (−2)³ = −8, so −2 is a valid cube root of −8. More generally, odd powers preserve sign information, making odd-index radicals (cube root, fifth root, etc.) well-defined for all real numbers. Even powers lose sign, restricting even-index radicals to non-negative radicands in the reals."

- question: "The function f(x) = √x always returns a non-negative value, even though every positive number has both a positive and a negative square root."
  type: true-false
  answer: true
  explanation: "By convention, the radical symbol √ denotes the principal (non-negative) square root only. √9 = 3, not ±3. This is why the range of f(x) = √x is [0, ∞). When solving equations like x² = 9, you write x = ±3 because you're finding all numbers whose square is 9 — but the function √9 evaluates to 3 only. This distinction matters for graphing: the graph of y = √x is a half-curve starting at the origin, not a full parabola."

- question: "The graph of y = √x is the upper half of the parabola y = x², restricted to x ≥ 0."
  type: true-false
  answer: false
  explanation: "The graph of y = √x is the reflection of the right half of y = x² across the line y = x — not the upper half of y = x². These two functions are inverses of each other (for x ≥ 0), and inverse function graphs are reflections across y = x. On y = x², the input runs left-right and output runs up; on y = √x, input runs left-right and output is the square root, rising slowly. The curve starts at (0, 0) and bends upward with decreasing slope, which is the reflected (not the original) parabola."

- question: "Explain why the domain of f(x) = √(x − 3) is [3, ∞), and describe how you would find the domain of a general transformed radical function g(x) = √(ax + b)."
  type: short-answer
  answer: "The square root requires a non-negative radicand. Setting x − 3 ≥ 0 gives x ≥ 3, so the domain is [3, ∞). For g(x) = √(ax + b): set ax + b ≥ 0 and solve for x. If a > 0, the domain is x ≥ −b/a. If a < 0, dividing by a flips the inequality, giving x ≤ −b/a."
  explanation: "The method is always: set the radicand ≥ 0 (for even-index radicals) and solve the resulting inequality. The transformation h in f(x) = √(x − h) shifts the domain's boundary: the left endpoint of the domain moves from 0 to h. This is a direct consequence of the general transformation rule — replacing x with x − h shifts the graph h units to the right, which shifts the domain boundary from 0 to h."
```

## Explainer

You already understand square roots as numbers: √9 = 3 because 3² = 9. A **radical function** makes the input itself a variable: f(x) = √x. This seemingly small change — replacing a number under the radical with x — creates a function with a shape you have not seen before, and its shape is directly explained by your prerequisite knowledge about inverse functions.

Think of it this way: the function g(x) = x² takes any non-negative number and squares it. The square root function f(x) = √x undoes that squaring — it is the inverse of g, but only on the restricted domain x ≥ 0. (You need the restriction because squaring loses sign information: both 3 and −3 square to 9, so the full squaring function cannot be inverted without a restriction.) The graph of f(x) = √x is the graph of g(x) = x² reflected across the line y = x, which explains its curved shape — it starts at the origin and bends upward more and more slowly as x increases. The **domain** is [0, ∞) and the **range** is [0, ∞).

The cube root function f(x) = ∛x behaves differently because cubing never loses sign information: (−2)³ = −8 and 2³ = 8 are distinct, so the full cubic is invertible on all of ℝ. This is why ∛x has domain and range both equal to all real numbers, and its graph passes through the origin with an S-shape. More generally, **even-index radicals** (√, ⁴√, etc.) require a non-negative radicand and produce non-negative outputs; **odd-index radicals** (∛, ⁵√, etc.) accept any real number and can produce negative outputs.

Transformations apply to radical functions exactly as they do to any function. For f(x) = a·√(x − h) + k: shifting by h moves the starting point horizontally (h > 0 shifts right), shifting by k moves it vertically, and a stretches or compresses it vertically — a negative a reflects the curve below the x-axis. The **domain** shifts with h: f(x) = √(x − 3) is only defined for x ≥ 3. Identifying the domain from the formula means setting the radicand ≥ 0 (for even roots) and solving for x.
