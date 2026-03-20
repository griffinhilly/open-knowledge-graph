---
id: order-of-operations
title: Order of Operations
domain: mathematics
course: 5th-grade
prerequisites:
  - id: order-of-operations-intro
    type: hard
builds-toward:
  - writing-numerical-expressions
  - evaluating-expressions-with-grouping
tags: [arithmetic, algebra-readiness, operations, expressions]
stage: concrete-operations
status: validated
---

# Order of Operations

## Core Idea
The full order of operations (often remembered as PEMDAS/GEMDAS) specifies: (1) Parentheses/Grouping symbols first, (2) Exponents, (3) Multiplication and Division from left to right, (4) Addition and Subtraction from left to right. In fifth grade, students work with all of these including simple exponents (squares, cubes). The order of operations is not an arbitrary rule but a convention that ensures mathematical expressions have a single, unambiguous meaning. Without it, 2 + 3 x 4 could reasonably mean 14 or 20.

## How It's Best Learned
Evaluate expressions step by step, showing only one operation per step. Use color-coding or underlining to highlight which operation comes next. Include nested parentheses and expressions where left-to-right order matters within the same priority level. Have students create expressions that produce a target number using given digits and operations. Discuss why the convention exists rather than just memorizing the acronym.

## Common Misconceptions
- Believing multiplication always comes before division (they have equal priority, left to right).
- Believing addition always comes before subtraction (same issue).
- Evaluating strictly left to right, ignoring operation hierarchy.
- Misinterpreting PEMDAS as six levels instead of four (P, E, MD, AS).

## Questions

```yaml
- question: "What is the value of 12 ÷ 3 × 2?"
  type: multiple-choice
  options:
    - "2 — divide last because multiplication comes before division in PEMDAS"
    - "8 — multiplication and division have equal priority, so evaluate left to right"
    - "18 — multiply 3 × 2 first because M comes before D in the acronym"
    - "4 — work right to left when operations have the same letter pair"
  answer: 1
  explanation: "Multiplication and division are the same priority level — neither always comes first. The rule is to evaluate them left to right. So: 12 ÷ 3 = 4, then 4 × 2 = 8. Option A is the most common wrong answer — treating PEMDAS as six separate ranked levels causes students to always multiply before dividing, which is incorrect."

- question: "A student evaluates 20 − 4 + 3 by doing 4 + 3 = 7 first, then 20 − 7 = 13. What went wrong?"
  type: multiple-choice
  options:
    - "They should have subtracted before adding because subtraction comes before addition"
    - "They should have added before subtracting because A comes before S in PEMDAS"
    - "Addition and subtraction have equal priority and must go left to right; 20 − 4 should come first, giving 16 + 3 = 19"
    - "Nothing went wrong; 13 is the correct answer"
  answer: 2
  explanation: "Addition and subtraction, like multiplication and division, are equal-priority partners — neither always precedes the other. The correct approach is left to right: 20 − 4 = 16, then 16 + 3 = 19. The student treated 'AS' as meaning 'addition first,' which is a misreading of the acronym. PEMDAS has four levels, not six."

- question: "Placing parentheses around part of an expression can change its value even if the operations inside are the same."
  type: true-false
  answer: true
  explanation: "Parentheses override the default priority order. Without parentheses, 2 + 3 × 4 = 14 (multiply first). With parentheses, (2 + 3) × 4 = 20 (add first). The parentheses force the addition to happen before the multiplication, producing a different result. This is precisely their purpose: communicating which operation should happen first."

- question: "In PEMDAS, multiplication always comes before division because M appears before D in the acronym."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions about order of operations. M and D represent a single priority level, not two separate ones. When an expression contains both multiplication and division (with no parentheses separating them), you evaluate left to right — whichever appears first gets done first. The acronym groups them together for a reason: MD is one level, AS is one level."

- question: "Why does 2 + 3 × 4 equal 14 and not 20? Explain using the purpose of the order of operations convention."
  type: short-answer
  answer: "The order of operations is a shared convention that ensures every mathematical expression has exactly one value. Under the convention, multiplication is evaluated before addition, so 3 × 4 = 12 is computed first, then 2 + 12 = 14. If we added first, (2 + 3) × 4 = 20 — a different answer. The convention exists so writers and readers of expressions always agree on meaning."
  explanation: "The key insight is that the order of operations is not an arbitrary rule but a necessary agreement. Without it, an expression like 2 + 3 × 4 would be ambiguous — two mathematicians could read it and get different answers. The convention resolves that ambiguity by specifying which operations bind more tightly. Parentheses let you override the convention when you need a different grouping."
```

## Explainer

You've been introduced to the idea that operations must be evaluated in a specific order. Now you're working with the full rule, including exponents and the subtle left-to-right rule within priority levels. The reason this convention exists is simple: an expression like 2 + 3 × 4 is ambiguous without it. If you add first: (2 + 3) × 4 = 20. If you multiply first: 2 + (3 × 4) = 14. Both can't be right. Mathematicians agreed on a convention so that every correctly formed expression has exactly one value. That convention is what PEMDAS (or GEMDAS) describes.

The four priority levels are: (1) **Grouping symbols** — parentheses, brackets, or fraction bars — resolved first, from innermost to outermost; (2) **Exponents** — powers and roots; (3) **Multiplication and Division** together, evaluated left to right with equal priority; (4) **Addition and Subtraction** together, evaluated left to right with equal priority. The most common mistake is treating PEMDAS as six separate levels and always doing multiplication before division. Consider 12 ÷ 3 × 2. If you multiply first: 12 ÷ 6 = 2. But the left-to-right rule gives: (12 ÷ 3) × 2 = 4 × 2 = 8. The correct answer is 8. Multiplication and division are partners — whichever comes first from the left gets done first.

Parentheses are the override key. They let the writer of an expression say "evaluate this part first, no matter what." When you write (2 + 3) × 4, the parentheses force the addition before the multiplication, giving 20 instead of 14. This is why algebra uses parentheses constantly — they communicate intent precisely. As you move into writing your own numerical and algebraic expressions, you'll use parentheses not just to follow the rules but to make your mathematical meaning unambiguous to anyone who reads your work. The order of operations is less a set of restrictions and more a shared language for expressing mathematical ideas without confusion.
