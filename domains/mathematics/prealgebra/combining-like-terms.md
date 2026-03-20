---
id: combining-like-terms
title: Combining Like Terms
domain: mathematics
course: prealgebra
prerequisites:
- id: variable-expressions
  type: hard
- id: adding-integers
  type: hard
- id: subtracting-integers
  type: hard
- id: properties-of-operations
  type: soft
builds-toward:
- one-step-equations
- two-step-equations
- adding-subtracting-polynomials
tags:
- like-terms
- simplifying
- expressions
- algebra
stage: abstract-reasoning
status: validated
---
# Combining Like Terms

## Core Idea
Like terms are terms that have the same variable raised to the same power. For example, 3x and 5x are like terms (both have x to the first power), but 3x and 3x² are not. Combining like terms means adding or subtracting their coefficients: 3x + 5x = 8x, and 7y² − 2y² = 5y². This is the algebraic version of the idea that you can only add things of the same kind — you can add 3 apples and 5 apples to get 8 apples, but you cannot combine 3 apples and 5 oranges. Simplifying expressions by combining like terms is a fundamental skill used in every subsequent algebra topic.

## How It's Best Learned
Use algebra tiles or color-coded cards to make the concept concrete — same shape/color means "like." Sort terms into groups before combining. Practice with expressions that have multiple variable types (e.g., 3x + 2y + 5x − y = 8x + y). Emphasize that constants are like terms with each other.

## Common Misconceptions
- Combining unlike terms: adding 3x + 4y to get 7xy.
- Forgetting that a variable with no written coefficient has a coefficient of 1 (x means 1x).
- Adding exponents when combining like terms: writing 3x + 5x = 8x² instead of 8x.

## Questions

```yaml
- question: "Simplify 3x² + 5x. Which answer is correct?"
  type: multiple-choice
  options:
    - "8x²"
    - "8x³"
    - "8x"
    - "3x² + 5x — it cannot be simplified further"
  answer: 3
  explanation: "3x² and 5x are NOT like terms — x² and x have different exponents, so they represent different 'units' (copies of x-squared vs. copies of x). They cannot be combined, just as you cannot add 3 square feet and 5 feet into a single measurement. The most common wrong answer is 8x², which incorrectly adds the coefficients as if the terms were alike."

- question: "Simplify: 4x + 2y + 3x − y"
  type: multiple-choice
  options:
    - "9xy"
    - "9x"
    - "7x + y"
    - "7x + 3y"
  answer: 2
  explanation: "Group like terms separately: (4x + 3x) = 7x, and (2y − y) = 2y − 1y = 1y = y. Result: 7x + y. Key trap: 'y' alone means 1y (an invisible coefficient of 1), so 2y − y = 1y = y, not 2y. Option A wrongly multiplies variables together. Option D incorrectly handles the subtraction, treating −y as though it were +y."

- question: "The expression 6a − a simplifies to 5a, because 'a' has an implied coefficient of 1."
  type: true-false
  answer: true
  explanation: "Correct. Any variable written without a visible coefficient has a coefficient of 1: a = 1a. So 6a − a = 6a − 1a = (6 − 1)a = 5a. This applies universally — x means 1x, y² means 1y², and so on. Forgetting the invisible 1 is one of the most common errors in simplifying expressions."

- question: "When combining like terms such as 3x³ + 5x³, you add the exponents to get 8x⁶."
  type: true-false
  answer: false
  explanation: "Exponents are never added when combining like terms. 3x³ + 5x³ = (3 + 5)x³ = 8x³ — the exponent stays the same because you are adding the counts of copies of x³, not multiplying. Exponents add only when you multiply terms (e.g., x³ · x³ = x⁶). Combining like terms is coefficient addition, which leaves the variable and its exponent unchanged."

- question: "Explain why 3x and 5x can be combined into 8x, but 3x and 5x² cannot be combined. Use the idea of 'counting copies.'"
  type: short-answer
  answer: "3x means '3 copies of x' and 5x means '5 copies of x' — they count the same unit, so you add the counts: 3 + 5 = 8 copies of x, giving 8x. But 3x means '3 copies of x' and 5x² means '5 copies of x-squared,' which are different units entirely (like feet vs. square feet). You cannot add counts of different things into a single number, so the expression stays as 3x + 5x²."
  explanation: "The underlying mechanism is the distributive property: 3x + 5x = (3 + 5)x = 8x. The variable is the common factor being 'counted'; the coefficients are the counts. Different exponents mean different variables in the sense that x and x² are different quantities — just as distance and area are different even though they both measure physical things."
```

## Explainer

You already know how to add and subtract integers, and you know that a variable expression like 3x means "3 times x" — the **coefficient** counts how many copies of the variable you have. Combining like terms builds directly on this: it is just adding and subtracting counts of the same thing.

Think of it in terms of fruit, an analogy that makes the logic transparent. Three apples plus five apples equals eight apples — you add the counts because the units match. But three apples plus five oranges cannot be simplified to a single number; you must keep them separate as "3 apples + 5 oranges." Variable terms work identically: 3x + 5x = 8x because both measure copies of x. But 3x + 5y cannot be simplified — x and y are different "units," and merging them would be like adding apples and oranges.

The underlying mechanism is the **distributive property** (from your properties-of-operations work): 3x + 5x = (3 + 5)x = 8x. You are factoring out the variable and adding the coefficients. This is why you add the coefficients and leave the variable unchanged — the variable is the common unit, and the coefficients are the counts being summed. Subtraction works the same way: 7y² − 2y² = (7 − 2)y² = 5y².

With multiple variable types, the strategy is to sort before you simplify. Given 4x + 2y + 3x − y, group by type: (4x + 3x) + (2y − y) = 7x + y. Work one group at a time. And remember: **powers are part of the term's identity**. The terms 3x² and 5x are not like terms. x² is "copies of x-squared" and x is "copies of x" — they measure completely different quantities, just like square feet and feet are different units. You cannot combine them, and you must never add the exponents (3x + 5x ≠ 8x², because you are counting copies, not multiplying).
