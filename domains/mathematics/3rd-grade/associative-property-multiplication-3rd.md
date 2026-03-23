---
id: associative-property-multiplication-3rd
title: Associative Property of Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: commutative-property-multiplication-3rd
  type: soft
- id: multiplication-facts-threes-through-nines
  type: hard
builds-toward:
- distributive-property
- multi-digit-multiplication
tags:
- multiplication
- properties
- grouping
stage: concrete-operations
status: validated
---

# Associative Property of Multiplication

## Core Idea
The associative property states that (2 × 3) × 4 = 2 × (3 × 4). Grouping factors differently does not change the product. This permits flexible computation: 2 × 3 × 4 can be computed as (2 × 3) × 4 = 6 × 4 or as 2 × (3 × 4) = 2 × 12.

## How It's Best Learned
Use arrays and area models to show that regrouping factors rearranges the dimensions without changing the total. Provide three-factor problems and ask students to solve in two different groupings, verifying the answer matches.

## Common Misconceptions
- Confusing associative with commutative — commutative swaps the order of factors, associative changes which pair gets multiplied first.
- Thinking parentheses always change the answer (they do in addition/subtraction context but not in multiplication).

## Questions

```yaml
- question: "A student solves 4 × 5 × 2 by computing (4 × 5) × 2 = 20 × 2 = 40. A second student computes (4 × 2) × 5 = 8 × 5 = 40. Who got the right answer?"
  type: multiple-choice
  options:
    - "Only the first student — you must always multiply left to right"
    - "Only the second student — you must use parentheses as written"
    - "Both students — the associative property guarantees the same product regardless of which pair is multiplied first"
    - "Neither — the correct answer depends on which parentheses are shown in the original problem"
  answer: 2
  explanation: "The associative property states that grouping (which pair you multiply first) does not affect the product. Both students get 40 because all three factors — 4, 5, and 2 — are still in the problem. The only difference is the order of computation, not the result. This is what makes the property useful: you are free to choose the grouping that is easiest to calculate."

- question: "How does the associative property differ from the commutative property of multiplication?"
  type: multiple-choice
  options:
    - "They are the same thing — both let you rearrange factors"
    - "The commutative property swaps the order of two factors; the associative property changes which pair among three or more factors is multiplied first"
    - "The commutative property applies to three factors; the associative applies only to two"
    - "The associative property works for addition but not multiplication"
  answer: 1
  explanation: "Commutative: 4 × 7 = 7 × 4 — the order of two factors is swapped, same product. Associative: (2 × 3) × 4 = 2 × (3 × 4) — the factors stay the same but the grouping (which multiplication happens first) changes. Confusing these two is common. Together, both properties give complete freedom to rearrange and regroup any multiplication expression."

- question: "Using the associative property, (5 × 2) × 7 = 5 × (2 × 7), and both expressions equal 70."
  type: true-false
  answer: true
  explanation: "(5 × 2) × 7 = 10 × 7 = 70. And 5 × (2 × 7) = 5 × 14 = 70. The associative property guarantees these are equal. Notice that (5 × 2) × 7 is much easier to compute because 5 × 2 = 10 and multiplying by 10 is trivial — this is exactly the kind of strategic simplification the property enables."

- question: "Changing which factors are inside parentheses changes the final product because the operations are performed in a different order."
  type: true-false
  answer: false
  explanation: "In multiplication, changing the grouping never changes the product. The parentheses only affect which calculation you do first, not what values are being multiplied. Unlike subtraction or division (where order and grouping do matter), multiplication is both commutative and associative — all factors contribute equally to the product regardless of grouping order."

- question: "A student needs to compute 5 × 9 × 2. Show how the associative property can make this easier, and explain why the answer stays the same."
  type: short-answer
  answer: "Regroup as (5 × 2) × 9 = 10 × 9 = 90. The answer stays the same because the associative property guarantees that changing which pair you multiply first doesn't change the product — all three factors are still multiplied together."
  explanation: "The 'natural' left-to-right approach gives 5 × 9 = 45, then 45 × 2 = 90 — correct but harder. Noticing that 5 × 2 = 10 and multiplying by 10 is trivial (just append a zero) makes the problem much easier. This is the practical payoff of the associative property: you can shop around for the easiest grouping before computing, and the answer is guaranteed to be the same."
```

## Explainer

You already know from the commutative property that the order of two factors doesn't change the product: 4 × 7 = 7 × 4. The **associative property** extends this freedom to three or more factors: when you multiply, it doesn't matter which pair you multiply first. Parentheses in a multiplication expression are just a suggestion about what to compute first — and you're free to choose a different order if it's easier.

Think about a problem like 2 × 3 × 4. You could do (2 × 3) × 4 = 6 × 4 = 24. Or you could do 2 × (3 × 4) = 2 × 12 = 24. Same answer either way. The parentheses don't change what's being multiplied — all three factors, 2, 3, and 4, are still in the problem. The only thing that changes is which multiplication you perform first.

The real power of this property shows up when you're trying to make a problem easier. Suppose you see 5 × 9 × 2. Your multiplication facts tell you 5 × 9 = 45, and then 45 × 2 = 90 — that works, but 45 × 2 is a bit of work. Alternatively, notice that 5 × 2 = 10, and 10 × 9 = 90 is trivial. Regrouping as (5 × 2) × 9 turns a harder problem into an easy one. The associative property gives you permission to do this.

This idea pairs with the commutative property to give you complete freedom when multiplying several numbers together: you can rearrange the factors in any order and group them any way you like. Together, these properties form the foundation for the more powerful **distributive property** and eventually for multi-digit multiplication, where you'll be breaking large products into pieces, computing each piece, and adding the parts — a strategy that only works because regrouping and reordering factors is always safe.
