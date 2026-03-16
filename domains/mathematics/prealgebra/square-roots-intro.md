---
id: square-roots-intro
title: Introduction to Square Roots
domain: mathematics
course: prealgebra
prerequisites:
  - id: exponents-intro
    type: hard
builds-toward:
  - radical-expressions-simplifying
  - pythagorean-theorem
tags: [square-roots, radicals, inverse-operations]
stage: abstract-reasoning
status: validated
---

# Introduction to Square Roots

## Core Idea
The square root of a number is the value that, when multiplied by itself, gives that number. Since 7 × 7 = 49, the square root of 49 is 7, written as sqrt(49) = 7. Square roots are the inverse of squaring — they "undo" the exponent of 2. Perfect squares (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...) have whole-number square roots. Non-perfect squares like 2, 3, 5 have irrational square roots that are non-terminating, non-repeating decimals. Square roots appear in the Pythagorean theorem, distance formulas, and throughout geometry and physics.

## How It's Best Learned
Build a table of perfect squares from 1² to 15² and have students memorize them. Practice finding square roots of perfect squares quickly. For non-perfect squares, estimate by identifying which two consecutive perfect squares the number falls between (sqrt(30) is between 5 and 6, closer to 5.5). Use a calculator to verify. Introduce the radical symbol and practice reading it.

## Common Misconceptions
- Thinking sqrt(25) = 12.5 (dividing by 2 instead of finding the square root).
- Believing every number has a nice whole-number square root.
- Not recognizing that negative numbers do not have real square roots (this comes up more fully in algebra 2 with imaginary numbers).

## Questions

```yaml
- question: "Which of the following is an irrational number?"
  type: multiple-choice
  options: ["sqrt(9)", "sqrt(16)", "sqrt(7)", "sqrt(100)"]
  answer: 2
  explanation: "sqrt(7) is irrational because 7 is not a perfect square — no whole number multiplied by itself equals 7. By contrast, sqrt(9) = 3, sqrt(16) = 4, and sqrt(100) = 10 are all perfect squares with exact whole-number square roots."

- question: "sqrt(36) = 18, because 36 ÷ 2 = 18."
  type: true-false
  answer: false
  explanation: "sqrt(36) = 6, because 6 × 6 = 36. The square root asks 'what number times itself gives 36?' not 'what is 36 divided by 2?' Dividing by 2 gives half of 36; taking a square root is a completely different operation. You can verify: 18 × 18 = 324, not 36."

- question: "Without a calculator, estimate sqrt(50) to one decimal place and explain your reasoning."
  type: short-answer
  answer: "Approximately 7.1. Since 7² = 49 and 8² = 64, sqrt(50) falls between 7 and 8. Because 50 is very close to 49, the root is just barely above 7 (the precise value is about 7.07)."
  explanation: "The bracketing technique — finding the two consecutive perfect squares on either side — is the standard method for estimating irrational square roots. The closer the number is to the lower perfect square, the closer the root is to the lower whole number."
```

## Explainer

You know that squaring a number means multiplying it by itself: 8² = 8 × 8 = 64. The square root is the inverse operation — it asks the question: "What number, when squared, gives this result?" Since 8² = 64, sqrt(64) = 8. Square roots undo exponents of 2, just as division undoes multiplication and subtraction undoes addition. This inverse relationship is the core idea; everything else follows from it.

The numbers whose square roots are whole numbers are called perfect squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, and so on. Memorizing these up to at least 12² or 15² is as important as knowing multiplication tables — they appear constantly in geometry, the Pythagorean theorem, and later algebra. For all other positive integers, the square root is irrational: a decimal that never terminates and never repeats. sqrt(2) ≈ 1.41421... continues forever without pattern. This is not an error or an approximation; irrational numbers simply cannot be written as exact fractions.

A common misconception is that sqrt(36) = 18, arrived at by dividing 36 by 2. This confuses square root with halving. To check: 18 × 18 = 324, which is nowhere near 36. The square root does not split a number in half — it finds the side length of a square with that area. sqrt(36) = 6 because a 6 × 6 square has area 36.

When you need to estimate a square root without a calculator, use the bracketing technique: find the two consecutive perfect squares the number falls between. For sqrt(50): since 7² = 49 and 8² = 64, sqrt(50) is between 7 and 8. Because 50 is much closer to 49 than to 64, the root is closer to 7 — about 7.07. This kind of estimation is a practical skill you will use throughout mathematics whenever an exact value is unavailable.

One important boundary: negative numbers do not have real square roots. Any real number squared is non-negative — (−5)² = 25 and 5² = 25 — so no real number can square to give −1 or any other negative value. The square root function is defined only for non-negative inputs. This boundary is the starting point for complex numbers, which introduce sqrt(−1) = i, a topic you will encounter in later courses.
