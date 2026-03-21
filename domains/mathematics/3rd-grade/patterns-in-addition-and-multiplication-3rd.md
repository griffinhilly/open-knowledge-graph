---
id: patterns-in-addition-and-multiplication-3rd
title: Patterns in Addition and Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: arithmetic-patterns-3rd
  type: soft
- id: number-patterns-and-relationships
  type: soft
builds-toward:
- patterns-and-sequences
tags:
- patterns
- sequences
- number-sense
stage: concrete-operations
status: draft
---

# Patterns in Addition and Multiplication

## Core Idea
Patterns appear in multiplication tables (e.g., 5s always end in 5 or 0; 9s have digits that sum to 9). Recognizing patterns helps with fluency and mental math. Number sequences (e.g., 2, 4, 6, 8...) show the structure of addition and multiplication.

## Questions

```yaml
- question: "A student is checking whether 47 is a multiple of 9 using the digit-sum pattern. She adds 4 + 7 = 11. What should she conclude?"
  type: multiple-choice
  options:
    - "47 is a multiple of 9 because 11 is close to 9"
    - "47 is not a multiple of 9 because 11 does not equal 9 or a multiple of 9"
    - "She needs to check if 47 ends in 7 before deciding"
    - "The digit-sum pattern only works for numbers less than 40"
  answer: 1
  explanation: "The 9s digit-sum pattern says: the digits of any multiple of 9 sum to 9 (or a multiple of 9). 4 + 7 = 11, which is neither 9 nor a multiple of 9, so 47 is NOT a multiple of 9. (Verify: 9 × 5 = 45, 9 × 6 = 54 — 47 is between them.) 'Close to 9' is not the same as 'equals 9.' The pattern gives a definitive test, not an approximation."

- question: "Why do all multiples of 5 end in either 0 or 5, without exception?"
  type: multiple-choice
  options:
    - "It's a coincidence that happens to be true for small numbers but breaks down for large ones"
    - "Multiples of 5 end in 5 or 0 because of a rule someone invented to make the pattern easier"
    - "Multiplying by 5 is repeated addition of 5, and adding 5 makes the ones digit cycle: 5, 0, 5, 0..."
    - "Only odd multiples of 5 end in 5; even multiples end in 0"
  answer: 2
  explanation: "Multiples of 5 are 5, 10, 15, 20, 25... — you're adding 5 each time. Starting from 5: ones digit is 5. Add 5 → ones digit is 0. Add 5 → ones digit is 5 again. The ones digit alternates between 5 and 0 forever, because adding 5 to a number ending in 5 always gives a number ending in 0, and vice versa. This is a consequence of how base-10 arithmetic works, not a coincidence."

- question: "Every multiple of 5 ends in either 0 or 5 — no exceptions, no matter how large the number."
  type: true-false
  answer: true
  explanation: "This pattern holds for all multiples of 5 without exception, because it follows from the structure of base-10 arithmetic. When you repeatedly add 5, the ones digit alternates perfectly between 5 and 0: 5, 10, 15, 20... 995, 1000, 1005... The pattern never breaks because the ones digit only depends on the ones digits of the numbers being added, and those cycle perfectly."

- question: "Patterns in multiplication tables (like the 5s ending in 0 or 5) are just memory tricks — they don't reflect any real mathematical reason."
  type: true-false
  answer: false
  explanation: "These patterns are mathematical consequences, not arbitrary tricks. They arise directly from two facts: (1) multiplication is repeated addition, and (2) our base-10 number system makes ones digits cycle when you add. The 5s pattern exists because adding 5 repeatedly makes ones digits cycle between 5 and 0 — that's a mathematical fact about how numbers work. Understanding why makes the pattern far more memorable and useful."

- question: "Why do the digits of multiples of 9 always sum to 9 (or a multiple of 9), and how can you use this to check if a number is a multiple of 9?"
  type: short-answer
  answer: "In base 10, each time you add 9 to a number, the tens digit increases by 1 and the ones digit decreases by 1 — keeping the digit sum constant. To check if a number is a multiple of 9, add its digits: if they sum to 9 (or a multiple of 9), the number is a multiple of 9; if not, it isn't."
  explanation: "For example: 9 (digit sum 9), 18 (1+8=9), 27 (2+7=9), 36 (3+6=9), 45 (4+5=9). The pattern holds for large numbers too: 99 (9+9=18, 1+8=9), 108 (1+0+8=9). This is a real mathematical property of 9 in base 10, not a memorization shortcut — though it doubles as one of the most useful mental math checks a student can learn."
```

## Explainer

A **pattern** in mathematics is a rule that repeats or grows in a predictable way. You've seen patterns before — in sequences like 2, 4, 6, 8 (add 2 each time) or 5, 10, 15, 20 (add 5). These sequences are directly connected to multiplication: the sequence 5, 10, 15, 20 is just the 5-times table in order. Counting by 5s and multiplying by 5 are the same process described differently.

The multiplication table is full of patterns worth noticing. The **5s pattern** is one of the most obvious: every multiple of 5 ends in either 0 or 5. 5, 10, 15, 20, 25 — the ones digit just alternates between 5 and 0. Once you see this, you can quickly check whether a number could be a multiple of 5. The **9s pattern** is more surprising: add the digits of any multiple of 9, and they always sum to 9 (or to a multiple of 9). 18 → 1 + 8 = 9. 27 → 2 + 7 = 9. 36 → 3 + 6 = 9. This makes the 9-times table one of the easiest to verify.

The **even numbers** — 2, 4, 6, 8, 10, 12... — are the multiples of 2, and they always end in 0, 2, 4, 6, or 8. The pattern of skip-counting by 2 is the same as the 2-times table. Every time you count by a number, you're producing that number's multiples in order.

Why do these patterns exist? Because multiplication is repeated addition — and when you add the same amount over and over, the results must follow a regular pattern. The ones digit cycles because of how our base-ten number system works: once a column fills up to 10, it starts over. Noticing these patterns doesn't just help you memorize facts — it helps you understand why the facts are true, which makes them much harder to forget.
