---
id: exponents-intro
title: Introduction to Exponents
domain: mathematics
course: prealgebra
prerequisites:
  - id: multiplying-integers
    type: hard
  - id: order-of-operations
    type: hard
builds-toward:
  - scientific-notation-intro
  - exponent-rules-product-power-quotient
  - negative-exponents
  - zero-exponent
tags: [exponents, powers, repeated-multiplication]
stage: abstract-reasoning
status: validated
---

# Introduction to Exponents

## Core Idea
An exponent tells you how many times to use a base as a factor. In 3⁴, the base is 3 and the exponent is 4, meaning 3 × 3 × 3 × 3 = 81. Exponents are shorthand for repeated multiplication, just as multiplication is shorthand for repeated addition. Key terminology: 3² is "three squared" (area of a square with side 3), 3³ is "three cubed" (volume of a cube with side 3). Exponents grow numbers rapidly, which is why they appear in scientific notation, compound interest, population models, and computer science.

## How It's Best Learned
Start with expanded form: write 2⁵ as 2 × 2 × 2 × 2 × 2, then compute. Build a powers table for bases 2 through 10. Emphasize that exponents are not multiplication — 3⁴ is not 3 × 4. Practice evaluating expressions with exponents within order of operations. Include negative bases with and without parentheses: (−2)³ = −8 vs. −2³ = −8 (same here, but (−2)² = 4 vs. −2² = −4).

## Common Misconceptions
- Computing 3⁴ as 3 × 4 = 12 instead of 81.
- Confusing (−2)⁴ = 16 with −2⁴ = −16.
- Thinking x¹ = 0 or that any number to the first power changes it somehow (x¹ = x always).

## Questions

```yaml
- question: "What is the value of (-3)²?"
  type: multiple-choice
  options: ["-9", "9", "-6", "6"]
  answer: 1
  explanation: "(-3)² means (-3) × (-3) = 9. The parentheses make the exponent apply to the negative sign as well, and a negative times a negative is positive. This is different from -3² = -(3 × 3) = -9, where the exponent applies only to 3."

- question: "The expression 2⁵ equals 10."
  type: true-false
  answer: false
  explanation: "2⁵ means 2 × 2 × 2 × 2 × 2 = 32, not 2 × 5 = 10. Exponents represent repeated multiplication, not multiplication. Confusing 2⁵ with 2 × 5 is the single most common exponent error — the exponent counts how many times the base appears as a factor."

- question: "Using the definition of exponents as repeated multiplication, explain why 2³ × 2⁴ = 2⁷."
  type: short-answer
  answer: "2³ × 2⁴ = (2 × 2 × 2) × (2 × 2 × 2 × 2) = 2⁷, because you are combining 3 twos and 4 twos into a single product of 7 twos."
  explanation: "Writing out each factor explicitly shows that multiplication joins two groups of repeated factors into one. The exponents add because you are counting the total number of times the base appears: 3 + 4 = 7. This is the intuition behind the product-of-powers rule you will learn next."
```

## Explainer

You already know that multiplication is shorthand for repeated addition: 5 × 3 means 5 + 5 + 5. Exponents take this one step further — they are shorthand for repeated multiplication. So 2⁵ means 2 × 2 × 2 × 2 × 2, or five twos multiplied together, which equals 32. The base (2) is the number being repeated; the exponent (5) tells you how many times it appears as a factor.

The most common mistake beginners make is computing 2⁵ as 2 × 5 = 10. This confuses exponentiation with multiplication. The exponent counts how many times you multiply, not how many times you add. Building a powers table — 2¹ = 2, 2² = 4, 2³ = 8, 2⁴ = 16, 2⁵ = 32 — and seeing how quickly the values grow makes it viscerally clear that these are fundamentally different operations.

Negative bases require extra care. When a negative number is inside parentheses and the exponent is applied to it, the negative sign participates in every multiplication: (−3)² = (−3) × (−3) = 9. But without parentheses, −3² means "the negative of 3 squared": −(3²) = −9. The parentheses completely change the meaning. The rule: if the negative sign is inside the parentheses, it is part of the base and gets squared along with the digit.

Exponents also have a defined position in the order of operations. They are evaluated before multiplication, division, addition, and subtraction — only parentheses come first. So in 2 + 3 × 4², you compute 4² = 16 first, then 3 × 16 = 48, then 2 + 48 = 50. Skipping this order leads to wrong answers, so knowing where exponents sit in the hierarchy is essential.

Finally, the names "squared" and "cubed" are not arbitrary — 3² = 9 is the area of a 3 × 3 square, and 3³ = 27 is the volume of a 3 × 3 × 3 cube. These geometric origins hint at why exponents appear so naturally in area, volume, and physical formulas, and they are a preview of how broadly useful this compact notation becomes across all of mathematics and science.
