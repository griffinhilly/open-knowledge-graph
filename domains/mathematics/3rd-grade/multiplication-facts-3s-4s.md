---
id: multiplication-facts-3s-4s
title: 'Multiplication Facts: 3s and 4s'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-twos-fives-tens
  type: hard
builds-toward:
- multiplication-fluency-facts-6-through-9
tags:
- facts
- multiplication
- fluency
stage: concrete-operations
status: validated
---

# Multiplication Facts: 3s and 4s

## Core Idea
Multiplication facts with 3 (3, 6, 9, 12, 15, ..., 27) and 4 (4, 8, 12, 16, ..., 36). The 4s facts are double the 2s facts since 4 = 2 × 2.

## How It's Best Learned
Use skip counting and arrays. Notice that multiplying by 4 is like multiplying by 2 twice.

## Common Misconceptions
Not recognizing patterns; confusing 3 × 6 with 3 + 6.

## Questions

```yaml
- question: "You know 2 × 9 = 18. How can you use this to find 4 × 9 without memorizing it separately?"
  type: multiple-choice
  options:
    - "Add 2 to 18, because 4 is 2 more than 2"
    - "Double 18, because 4 × 9 = (2 × 2) × 9 = 2 × (2 × 9)"
    - "Multiply 18 by 4 again"
    - "You cannot — 4s facts must be memorized independently of the 2s facts"
  answer: 1
  explanation: "The double-doubles strategy: since 4 = 2 × 2, multiplying by 4 is the same as multiplying by 2 twice. So 4 × 9 = 2 × (2 × 9) = 2 × 18 = 36. This reflects a real mathematical relationship. Every 4s fact can be derived by doubling the corresponding 2s fact — which students already know — making the 4s the easiest new fact family to learn."

- question: "A student says '3 × 6 = 9 because 3 plus 6 equals 9.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 3 + 6 = 9, and that is the same as 3 × 6"
    - "Multiplication and addition are different: 3 × 6 means three groups of six, which totals 18, not 9"
    - "The student should have written 3 × 6 = 3 + 3 + 3 + 3 + 3 + 3 instead"
    - "3 + 6 does equal 9, but 3 × 6 = 36"
  answer: 1
  explanation: "Addition and multiplication ask different questions. 3 + 6 = 9 means 'combine 3 and 6 into one total.' 3 × 6 = 18 means 'how much in three groups of six?' — which you can verify by counting three rows of six in an array: 6, 12, 18. Confusing the two is especially common with small numbers because the results seem close enough to be plausible. Arrays keep the distinction clear."

- question: "Knowing 3 × 8 = 24 automatically tells you that 8 × 3 = 24, cutting the number of unique facts you need to memorize nearly in half."
  type: true-false
  answer: true
  explanation: "This is the commutative property of multiplication: a × b = b × a. Every fact like 3 × 8 has a free twin: 8 × 3. A 10×10 multiplication table has 100 entries, but only about 55 are truly distinct once commutativity is applied. Recognizing this relationship is a significant efficiency gain and reflects a genuine mathematical truth, not just a memory trick."

- question: "4 × 7 = 28 can be worked out by adding one more group of 7 to the result of 3 × 7."
  type: true-false
  answer: true
  explanation: "Yes — if 3 × 7 = 21, then 4 × 7 is just one more group of 7: 21 + 7 = 28. This 'build up from a known fact' strategy works because multiplication is repeated addition: 4 groups is 3 groups plus one more. You don't need to memorize facts in isolation — you can always reach an unknown fact from a known one by adding or subtracting a group."

- question: "Explain why multiplying any number by 4 is the same as multiplying it by 2 twice."
  type: short-answer
  answer: "Because 4 = 2 × 2. Making 4 groups of something is the same as making 2 groups of 2 groups. So you can double the number, then double again. For example, 4 × 6 = 2 × (2 × 6) = 2 × 12 = 24. This works for any number because multiplication is associative: (2 × 2) × n = 2 × (2 × n)."
  explanation: "The double-doubles strategy is grounded in the multiplicative structure of 4: it is 2 squared. Mathematically, 4 × n = (2 × 2) × n = 2 × (2 × n). In practice: take the 2s fact you already know and double it. This transforms a potentially difficult fact into two uses of doubling — a skill students already have. Understanding why the strategy works makes it memorable and generalizable to other derived-fact strategies."
```

## Explainer

You've already built fluency with the 2s, 5s, and 10s. Those facts have obvious patterns — the 2s are every other number, the 5s end in 0 or 5, the 10s just add a zero. The 3s and 4s have patterns too, and recognizing them turns memorization into understanding.

The **3s facts** (3, 6, 9, 12, 15, 18, 21, 24, 27) are the skip-count-by-3 sequence. One useful pattern: the digits in multiples of 3 always sum to a multiple of 3. In 12, the digits 1 + 2 = 3. In 24, 2 + 4 = 6. In 27, 2 + 7 = 9. This won't help you compute quickly, but it can help you check: if the digits don't sum to a multiple of 3, you've made an error. The best strategy for mastering 3s is to practice skip counting aloud — 3, 6, 9, 12, 15 — until the rhythm becomes automatic. Think of it as 3 equal groups: 4 × 3 is four groups of three, which you can count: 3, 6, 9, 12.

The **4s facts** have an especially powerful shortcut: **multiplying by 4 is the same as multiplying by 2 twice**. Since 4 = 2 × 2, any fact you knew for the 2s can be doubled to get the 4s. You already know 2 × 7 = 14, so double it: 4 × 7 = 28. You know 2 × 8 = 16, so 4 × 8 = 32. This "double the doubles" strategy is not a trick — it reflects a real mathematical relationship. Once you trust this strategy, the 4s become the easiest new facts to learn.

One common confusion is mixing up multiplication and addition: 3 × 6 is not the same as 3 + 6. Addition asks "how much in total if I combine 3 and 6?" — that's 9. Multiplication asks "how much in total if I have 3 groups of 6?" — that's 18. Arrays help keep this straight: 3 × 6 is a grid with 3 rows and 6 columns, which has 18 cells total. Knowing the 3s and 4s also unlocks derived facts — if you know 3 × 7 = 21, you automatically know 7 × 3 = 21 (commutativity), cutting the number of unique facts you need to memorize nearly in half.
