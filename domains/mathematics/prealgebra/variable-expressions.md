---
id: variable-expressions
title: Variable Expressions
domain: mathematics
course: prealgebra
prerequisites:
  - id: integer-order-of-operations
    type: hard
  - id: order-of-operations
    type: hard
builds-toward:
  - combining-like-terms
  - distributive-property
  - one-step-equations
  - variables-and-expressions-review
tags: [variables, expressions, evaluation, algebra-intro]
stage: abstract-reasoning
status: validated
---

# Variable Expressions

## Core Idea
A variable expression (or algebraic expression) uses letters to represent unknown or changing quantities. In the expression 3x + 7, the variable x can take on different values, and the expression's value changes accordingly. Evaluating an expression means substituting a specific number for the variable and computing the result. Writing and evaluating variable expressions is the gateway to algebra — it shifts mathematics from computing with known numbers to reasoning about relationships and unknowns. Students must understand that a variable is not a mystery to be feared but a placeholder that represents a number.

## How It's Best Learned
Translate verbal phrases into algebraic expressions: "five more than a number" becomes n + 5. Practice evaluation with a substitution table: given x = 2, 3, 4, what is 2x − 1? Connect to patterns — the expression is a rule that generates a sequence. Use physical models (algebra tiles) to make expressions tangible before moving to pure symbols.

## Common Misconceptions
- Thinking a variable always represents one specific unknown number, rather than understanding it can vary.
- Writing "3x" as "thirty-something" — confusing concatenation with multiplication.
- Forgetting to apply order of operations when evaluating (e.g., evaluating 2 + 3x when x = 4 as 20 instead of 14).

## Questions

```yaml
- question: "What is the value of 2 + 3x when x = 4?"
  type: multiple-choice
  options: ["20", "14", "24", "9"]
  answer: 1
  explanation: "Order of operations requires multiplication before addition: 3 × 4 = 12, then 2 + 12 = 14. The common error is computing 2 + 3 = 5 first, then 5 × 4 = 20 — but the expression means 2 + (3 × x), not (2 + 3) × x."

- question: "In the expression 3x, the notation means the digit 3 is placed before the digit x to form a two-digit number (like thirty-something)."
  type: true-false
  answer: false
  explanation: "In algebra, 3x means 3 × x — three times the variable x. Letters are not digits; placing a number and a variable side by side indicates multiplication, not concatenation. If x = 5, then 3x = 15, not 35."

- question: "What does it mean to evaluate the expression 5n − 3 when n = 2?"
  type: short-answer
  answer: "Substitute 2 for n and apply order of operations: 5(2) − 3 = 10 − 3 = 7."
  explanation: "Evaluating an expression means replacing each variable with a given number and then computing the result. The variable is no longer a placeholder — it has a specific value — and standard arithmetic (following order of operations) gives the final answer."
```

## Explainer

A variable is simply a letter standing in for a number — one that we don't know yet, or one that can change. When you write the expression 3x + 7, you are describing a rule: take a number, multiply it by 3, then add 7. The letter x is not mysterious; it is a placeholder, the same way a blank in a fill-in-the-sentence holds space for a word. Different values of x produce different results, which is why expressions are more powerful than plain arithmetic — they describe whole families of calculations at once.

Evaluating an expression means plugging in a specific value and computing the result. If x = 4, then 3x + 7 becomes 3(4) + 7. At this point, order of operations — which you already know from integer arithmetic — takes over: multiplication before addition gives 12 + 7 = 19. Changing x to 5 gives 3(5) + 7 = 22. Think of the expression as a machine: substitution provides the input, order of operations runs the machine, and the result is the output.

One of the most important conventions to internalize is that 3x does NOT mean "thirty-something." In algebra, two symbols written next to each other mean multiplication: 3x = 3 × x. This is called implicit multiplication, and it appears throughout algebra. Once you recognize it, expressions like 5n, 2ab, or 7y stop looking like codes and start looking like ordinary multiplication written in a compact form.

Variables can appear in more complex positions — like 2x² − 5x + 1. The same rules apply: substitute first, then follow order of operations carefully. With x = 3: 2(3²) − 5(3) + 1 = 2(9) − 15 + 1 = 18 − 15 + 1 = 4. The exponent applies to x before multiplying by 2. Writing out the substitution explicitly before simplifying prevents most errors.

As you move deeper into algebra, expressions appear everywhere — as formulas, function rules, and equations to solve. Every one of them is built from variables and the operations you already know. The skill you are practicing now — reading, writing, and evaluating expressions — is the foundation for combining like terms, using the distributive property, and eventually solving equations.
