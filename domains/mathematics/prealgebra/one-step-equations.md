---
id: one-step-equations
title: One-Step Equations
domain: mathematics
course: prealgebra
prerequisites:
- id: variable-expressions
  type: hard
- id: adding-integers
  type: hard
- id: multiplying-integers
  type: hard
- id: unknown-factor-problems
  type: soft
- id: combining-like-terms
  type: soft
- id: opposites-and-additive-inverses
  type: soft
- id: writing-and-interpreting-expressions
  type: soft
builds-toward:
- two-step-equations
- one-step-inequalities
- solving-multi-step-equations
tags:
- equations
- solving
- inverse-operations
- algebra
stage: abstract-reasoning
status: validated
---
# One-Step Equations

## Core Idea
A one-step equation requires a single inverse operation to isolate the variable. For x + 5 = 12, subtract 5 from both sides to get x = 7. For 3x = 21, divide both sides by 3 to get x = 7. The foundational principle is balance — whatever you do to one side of the equation, you must do to the other. This concept of maintaining equality through inverse operations is the core mechanic of all equation solving in algebra and beyond. One-step equations train students to think about "undoing" operations, which is the essence of algebraic reasoning.

## How It's Best Learned
Use a balance scale model (physical or visual) to show that both sides must stay equal. Start with addition/subtraction equations, then multiplication/division. Have students check their answers by substituting back into the original equation. Introduce equations with negative numbers and fractions once the concept is solid.

## Common Misconceptions
- Performing the same operation on both sides instead of the inverse operation (adding 5 to both sides of x + 5 = 12).
- Only operating on one side of the equation.
- With multiplication equations, subtracting instead of dividing (trying to solve 3x = 21 by subtracting 3).

## Questions

```yaml
- question: "Which operation should you apply to both sides of 4x = 28 to solve for x?"
  type: multiple-choice
  options: ["Subtract 4", "Add 4", "Multiply by 4", "Divide by 4"]
  answer: 3
  explanation: "4x means 4 times x, so the operation attached to x is multiplication by 4. The inverse of multiplication is division, so you divide both sides by 4: 4x ÷ 4 = 28 ÷ 4, giving x = 7. Subtracting 4 would not undo multiplication."

- question: "To solve x - 9 = 3, you should subtract 9 from both sides."
  type: true-false
  answer: false
  explanation: "To undo subtraction of 9, you add 9 to both sides: x - 9 + 9 = 3 + 9, giving x = 12. Subtracting 9 again would apply the same operation rather than the inverse, producing x - 18 = -6 and moving further from isolating x."

- question: "A student solves 5x = 30 by subtracting 5 from both sides, arriving at 5x - 5 = 25 and concluding x = 5. Is this correct? Explain why or why not."
  type: short-answer
  answer: "No. 5x = 30 means 5 times x equals 30. To isolate x, divide both sides by 5: x = 30 ÷ 5 = 6. Subtracting 5 does not undo multiplication — it just shifts the equation without isolating x."
  explanation: "The student applied the wrong inverse operation. Multiplication is undone by division, not subtraction. Substituting the student's answer back in confirms the error: 5 × 5 = 25, not 30. Checking by substitution is the reliable way to catch this kind of mistake."
```

## Explainer

An equation is a mathematical sentence asserting that two expressions are equal. The equation x + 5 = 12 says "some unknown number, plus 5, equals 12." Solving it means finding which value of x makes the sentence true. The strategy is always the same: get x alone on one side — that is, isolate the variable.

The governing principle is balance. An equation is like a perfectly level scale. If you add, subtract, multiply, or divide on one side, you must do the identical thing to the other side, or the scale tips and the equation is no longer valid. The operation you choose should be the inverse (opposite) of whatever is currently attached to x. If 5 is being added to x, subtract 5 from both sides. If x is being multiplied by 3, divide both sides by 3.

A very common mistake is applying the same operation rather than the inverse. Faced with x + 5 = 12, a student might add 5 to both sides, getting x + 10 = 17. The equation is still balanced — but x is no more isolated than before, and the number attached to it just grew. The goal is not merely to do something to both sides; it is to do the thing that undoes the operation on x.

Another frequent error is operating on only one side. Subtracting 5 from the left without subtracting from the right gives x = 7 and 12 — but 7 ≠ 12, so the original equality has been destroyed. This is equivalent to removing weight from one pan of a scale without removing anything from the other: the balance is lost. Whatever you do to one side, you must do to both.

Once you find a solution, verify it by substituting back into the original equation. If x = 7 and the equation is x + 5 = 12, check: 7 + 5 = 12. ✓ This habit builds the deeper understanding that a solution is a value that makes the equation true — not just a number produced at the end of a sequence of steps. Every more complex equation you will ever solve uses exactly this same logic of inverse operations on both sides.
