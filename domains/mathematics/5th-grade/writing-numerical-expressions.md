---
id: writing-numerical-expressions
title: Writing and Interpreting Numerical Expressions
domain: mathematics
course: 5th-grade
prerequisites:
- id: input-output-tables
  type: soft
- id: patterns-and-sequences
  type: soft
- id: order-of-operations-intro-4th-grade
  type: hard
builds-toward:
- evaluating-expressions-with-grouping
tags:
- expressions
- algebra-readiness
- notation
stage: concrete-operations
status: validated
---
# Writing and Interpreting Numerical Expressions

## Core Idea
Students learn to translate between verbal descriptions and mathematical expressions. "Add 8 and 7, then multiply by 2" becomes 2 x (8 + 7) or (8 + 7) x 2. "Multiply 8 by 7, then add 2" becomes 8 x 7 + 2. Students also interpret expressions without evaluating them: they can compare "3 x (12 + 8)" and "3 x 12 + 3 x 8" and explain why they are equal (distributive property) without computing. This skill bridges arithmetic and algebra -- the ability to read and write expressions is the foundation for all equation-solving and algebraic reasoning.

## How It's Best Learned
Start with verbal-to-symbolic translation: give word descriptions and have students write the expression, paying careful attention to where parentheses are needed. Then reverse: show an expression and have students describe it in words. Include comparison problems where students determine whether two expressions are equivalent without evaluating. Use real-world contexts ("double the sum of your scores").

## Common Misconceptions
- Translating word order directly into symbol order without considering operation priority (writing 8 + 7 x 2 for "add 8 and 7, then multiply by 2").
- Omitting necessary parentheses.
- Confusing "sum of a and b, multiplied by c" with "a plus b multiplied by c" (they mean different things without parentheses).

## Questions

```yaml
- question: "A student translates 'add 5 and 3, then double the result' as 5 + 3 × 2. What is wrong with this expression?"
  type: multiple-choice
  options:
    - "Nothing — 5 + 3 × 2 = 16, which is correctly double 8"
    - "By order of operations, 5 + 3 × 2 = 11, not 16 — the student needed to write (5 + 3) × 2"
    - "The student should have written 2 × 5 + 3 = 13"
    - "There is no mathematical way to represent 'add first, then multiply'"
  answer: 1
  explanation: "Without parentheses, order of operations multiplies first: 5 + (3 × 2) = 5 + 6 = 11. But the verbal description says to add first, then double the result: (5 + 3) × 2 = 8 × 2 = 16. Parentheses are essential to override the default multiplication-first priority. This is exactly the misconception described in the topic: translating word order directly into symbol order without considering operation priority."

- question: "Without calculating either expression, which is larger: 5 × (20 + 3) or 5 × 20 + 3?"
  type: multiple-choice
  options:
    - "They are equal — the distributive property makes them equivalent"
    - "5 × (20 + 3) is larger — the 5 multiplies the entire sum of 23"
    - "5 × 20 + 3 is larger — adding 3 at the end increases the result"
    - "You cannot compare them without calculating both"
  answer: 1
  explanation: "In 5 × (20 + 3), the 5 multiplies the full sum 23, giving 115. In 5 × 20 + 3, only 20 is multiplied by 5 (= 100), then 3 is added, giving 103. Recognizing structure — what is inside the parentheses versus outside — lets you compare without full calculation. Option A is wrong: the distributive property says 5 × (20 + 3) = 5 × 20 + 5 × 3, not 5 × 20 + 3."

- question: "The expression (8 + 7) × 2 correctly represents the instruction 'add 8 and 7, then multiply the result by 2.'"
  type: true-false
  answer: true
  explanation: "Parentheses force the addition to happen first: (8 + 7) = 15, then × 2 = 30. Without parentheses, 8 + 7 × 2 would follow order of operations, computing 7 × 2 = 14 first, then 8 + 14 = 22 — a different and incorrect result. The parentheses are not optional; they carry the precise meaning of the verbal instruction."

- question: "The expressions 3 × (4 + 5) and 3 × 4 + 5 are equivalent because multiplication distributes over addition."
  type: true-false
  answer: false
  explanation: "3 × (4 + 5) = 3 × 9 = 27. 3 × 4 + 5 = 12 + 5 = 17. These are NOT equal. The distributive property says 3 × (4 + 5) = 3 × 4 + 3 × 5 = 27 — you must multiply 3 by each term inside the parentheses. Simply dropping the parentheses (getting 3 × 4 + 5) is not distribution; it changes the expression's value entirely."

- question: "Why do parentheses change the meaning of a mathematical expression, and when must they be used when translating a verbal description?"
  type: short-answer
  answer: "Parentheses override the default order of operations (multiplication before addition). They must be used whenever a verbal description says to perform an addition or subtraction before a multiplication or division — that is, whenever the intended sequence differs from the order that operations would naturally execute without parentheses."
  explanation: "This is the bridge between natural language and mathematical notation. English can describe any sequence of operations ('first do this, then that'), but mathematical notation executes in a fixed default order. Parentheses are the tool that encodes the intended sequence. Missing them produces a syntactically valid expression that means something different than what was described."
```

## Explainer

You already know the **order of operations** — the rules that say multiplication happens before addition unless parentheses say otherwise. Writing numerical expressions is the flip side of evaluating them: instead of computing an expression someone handed you, you're constructing the expression yourself to capture an intended calculation. The challenge is that English word order and mathematical operator order don't always match.

Consider "add 8 and 7, then multiply by 2." The word "add" appears first, which might tempt you to write 8 + 7 × 2 — but that expression, following order of operations, multiplies 7 × 2 first, giving 8 + 14 = 22. The intended computation adds first: (8 + 7) × 2 = 30. The **parentheses** are doing essential work: they override the default order and preserve the sequence of operations the words described. Any time a verbal description says "first do X, then do Y" and X is addition while Y is multiplication, you need parentheses around the addition.

The reverse skill — reading an expression and putting it into words — builds the same understanding from the other direction. When you see 3 × (12 + 8), you can say "3 times the sum of 12 and 8." You're parsing the expression as a recipe: what happens first (add 12 and 8 inside the parentheses) and what happens to the result (multiply by 3). Importantly, you can observe that 3 × (12 + 8) must equal 3 × 12 + 3 × 8 — the **distributive property** — without computing either side. The structure of the expressions reveals the equivalence; calculation isn't required to see it.

This topic is where arithmetic becomes **algebra readiness**. A numerical expression is just an algebraic expression where every value is a known number. The skills you're building now — recognizing what is nested inside what, translating between words and symbols, comparing expressions without evaluating them — transfer directly when variables appear. "The sum of a number and 7, doubled" becomes 2 × (n + 7). The expression-writing logic is identical; only the notation changes. Every student who struggles with early algebra can trace the difficulty back to not having fully internalized what a written expression *means*.
