---
id: multiplying-integers
title: Multiplying Integers
domain: mathematics
course: prealgebra
prerequisites:
  - id: adding-integers
    type: hard
  - id: subtracting-integers
    type: soft
builds-toward:
  - dividing-integers
  - integer-order-of-operations
  - exponents-intro
tags: [integers, multiplication, operations]
stage: abstract-reasoning
status: validated
---

# Multiplying Integers

## Core Idea
Multiplying integers follows two sign rules: the product of two numbers with the same sign is positive, and the product of two numbers with different signs is negative. These rules can be derived from patterns (e.g., 3 × 2 = 6, 3 × 1 = 3, 3 × 0 = 0, 3 × (−1) = −3 — each step decreases by 3) or from the idea that multiplication by −1 reflects a number across zero on the number line. Mastery of integer multiplication is essential for simplifying expressions, working with exponents, and factoring polynomials.

## How It's Best Learned
Show the pattern-based derivation so students see that the sign rules are logical consequences, not arbitrary. Use repeated addition to motivate: 3 × (−2) = (−2) + (−2) + (−2) = −6. For negative times negative, the pattern argument is most convincing. Practice with a mix of sign combinations and emphasize that counting the number of negative factors determines the product's sign.

## Common Misconceptions
- Students may think negative × negative = negative, not recognizing the double-negative pattern.
- Confusing multiplication sign rules with addition sign rules (where same signs means add magnitudes).
- When multiplying more than two integers, students lose track of the sign — teach them to count the number of negatives (even = positive, odd = negative).

## Questions

```yaml
- question: "What is the sign of the product (-2) × (-3) × (-1)?"
  type: multiple-choice
  options: ["Positive, because two negatives make a positive", "Negative, because there are three negative factors", "Positive, because all numbers are even", "Negative, because the product of any negatives is negative"]
  answer: 1
  explanation: "Count the negative factors: there are three (-2, -3, and -1). An odd number of negatives gives a negative product. (-2) × (-3) = 6 (positive), then 6 × (-1) = -6 (negative). Three negatives → negative result."

- question: "Negative times negative equals negative."
  type: true-false
  answer: false
  explanation: "Negative times negative equals positive. For example, (-3) × (-4) = 12. The double-negative 'cancels': multiplying by -1 flips a number to its opposite, so multiplying by -1 twice returns you to the original sign. (-3) × (-4) can be read as 'the opposite of [3 × (-4)]' = 'the opposite of -12' = 12."

- question: "Using the pattern-based argument, explain why a negative number times a negative number must be positive."
  type: short-answer
  answer: "Each multiplication by -1 reverses the sign. Starting from a positive product and multiplying by two negatives reverses the sign twice, returning to positive."
  explanation: "Consider the pattern: 3×2=6, 3×1=3, 3×0=0, 3×(-1)=-3, 3×(-2)=-6. Each step decreases by 3. Now extend: (-3)×2=−6, (-3)×1=−3, (-3)×0=0, (-3)×(-1)=3, (-3)×(-2)=6. The pattern forces the result to be positive — it is not a rule imposed from outside but a consequence of how multiplication behaves."
```

## Explainer

You already know how to add integers. Multiplication is repeated addition, so it is natural to start there. What does 3 × (-2) mean? It means three groups of (-2): (-2) + (-2) + (-2) = -6. A positive times a negative is negative because you are repeating a negative quantity a positive number of times. This gives you the first rule without any memorization.

The harder case is negative times negative. The repeated-addition argument breaks down (what would -3 groups of something mean?), but the pattern argument makes it clear. Look at this column: 3×2=6, 3×1=3, 3×0=0, 3×(-1)=-3, 3×(-2)=-6. Each step down decreases by 3. Now do the same with -3: (-3)×2=-6, (-3)×1=-3, (-3)×0=0, (-3)×(-1)=?, (-3)×(-2)=?. Each step now *increases* by 3. The pattern forces (-3)×(-1)=3 and (-3)×(-2)=6. Negative times negative must be positive.

A more abstract way to see it: multiplying by -1 flips a number to its opposite on the number line. Multiplying by -1 twice flips twice — returning you to where you started. So (-1)×(-1) = 1, and by extension any negative times negative is positive.

When multiplying a chain of integers — like (-2)×(-3)×(-1) — you do not need to track running products. Just count the negative factors. An even number of negatives produces a positive result; an odd number produces a negative result. This "count the negatives" shortcut is essential for simplifying expressions with exponents later, where you will see things like (-2)⁵ (five negative factors → negative) versus (-2)⁴ (four negative factors → positive).

