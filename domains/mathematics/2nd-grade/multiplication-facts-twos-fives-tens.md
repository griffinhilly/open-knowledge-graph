---
id: multiplication-facts-twos-fives-tens
title: 'Multiplication Facts: 2s, 5s, and 10s'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: multiplication-facts-basic-2nd
  type: hard
- id: skip-counting-as-multiplication
  type: soft
tags:
- multiplication
- facts
- 2s
- 5s
- 10s
stage: concrete-operations
status: draft
---

# Multiplication Facts: 2s, 5s, and 10s

## Core Idea
The 2s, 5s, and 10s multiplication facts are easiest to learn because of patterns in skip counting. 2×5=10, 5×4=20, 10×3=30. Mastering these facts provides a foundation for harder facts in later grades.

## Questions

```yaml
- question: "You know that 5 × 8 = 40. How can this help you figure out 6 × 8?"
  type: multiple-choice
  options:
    - "It can't — 6 × 8 is a completely different fact"
    - "Add one more group of 8: 40 + 8 = 48, because 6 groups is one more than 5 groups"
    - "Double 40, because 6 is close to double 5"
    - "Add 6 and 5 to get 11, then multiply by 8"
  answer: 1
  explanation: "This is the 'anchor facts' idea: 6 × 8 means six groups of 8. If five groups of 8 is 40, you need exactly one more group of 8 to reach six groups: 40 + 8 = 48. The 2s, 5s, and 10s facts serve as anchor points precisely because nearby harder facts can always be reached by adding or subtracting one group. This strategy turns memorization into a reasoning process."

- question: "Why does multiplying any whole number by 10 always produce an answer that ends in zero?"
  type: multiple-choice
  options:
    - "Because 10 is an even number, and even times any number ends in zero"
    - "Because multiplying by 10 shifts every digit one place to the left in our place-value system, leaving the ones place empty"
    - "It is a coincidence that happens to be useful for the multiplication table"
    - "Because 10 has two digits, so the answer always gains an extra digit on the right"
  answer: 1
  explanation: "Multiplying by 10 is a place-value shift. In our base-10 system, each place is worth 10 times the place to its right. Multiplying by 10 moves every digit one step to the left — ones become tens, tens become hundreds — and the ones place is now empty, so it reads as 0. 6 × 10 = 60: the 6 has moved from the ones place to the tens place. This insight connects multiplication directly to place value and explains why the pattern is perfectly reliable."

- question: "Multiplying 2 × 9 gives the same result as adding 9 + 9."
  type: true-false
  answer: true
  explanation: "Multiplying by 2 means 'two groups of,' which is exactly the same as adding the number to itself. 2 × 9 = two groups of 9 = 9 + 9 = 18. This connection to addition doubles is what makes the 2s facts easiest to learn — every 2s fact is already a known double: 2 × 3 = 3 + 3 = 6, 2 × 7 = 7 + 7 = 14."

- question: "The 2s, 5s, and 10s facts are called 'anchor facts' because they are the only multiplication facts students ever need to know."
  type: true-false
  answer: false
  explanation: "Anchor facts are called that because you use them to derive other, harder facts — not because they're sufficient on their own. Knowing 5 × 8 = 40 helps you find 6 × 8 (add one group of 8), and knowing 2 × 7 = 14 helps you find 4 × 7 (double it). The 2s, 5s, and 10s are stepping stones toward the full multiplication table, not the complete destination."

- question: "How is multiplying by 2 connected to skip counting, and why does this connection help with the 2s facts?"
  type: short-answer
  answer: "Skip counting by 2 (2, 4, 6, 8, 10, ...) produces the 2s multiplication table in order. The nth number in the sequence is 2 × n — so the 4th stop, 8, is the answer to 2 × 4. The connection helps because skip counting is already familiar: you can reconstruct any 2s fact by counting up by 2s to the nth stop, even before you have it memorized."
  explanation: "Multiplication and skip counting describe the same thing in two ways. Skip counting describes the process: take equal-sized steps. Multiplication gives the destination a compact label: the 4th stop of 'count by 2s' is labeled 2 × 4. Students who already know skip-counting sequences can immediately make sense of multiplication facts — they're not starting from zero, they're attaching a name to a familiar counting pattern. This is why the 2s, 5s, and 10s come first: they have skip-counting sequences students already know."
```

## Explainer

You already know how to skip count — saying "2, 4, 6, 8, 10" by twos, or "5, 10, 15, 20" by fives. Here's the connection: every time you skip count by 2, you're computing the next multiple of 2. The 4th stop in the "count by 2s" sequence (2, 4, 6, **8**) is the answer to 2 × 4. Multiplication is skip counting with a shortcut label. Instead of counting all the way out, you memorize the destination.

The **2s facts** are doubles — amounts you've probably seen before with addition (2 + 2 = 4, 3 + 3 = 6). Multiplying by 2 just means "two groups of that number," which is the same as adding the number to itself. 2 × 7 = 7 + 7 = 14. The **10s facts** are the most obvious pattern of all: the answer is always the other number with a zero appended. 10 × 6 = 60, 10 × 9 = 90. This works because multiplying by 10 shifts every digit one place to the left — a place-value idea you'll return to many times.

The **5s facts** sit halfway between: each answer ends in either 0 or 5, alternating perfectly. 5×1=5, 5×2=10, 5×3=15, 5×4=20 — a reliable rhythm you can always reconstruct by skip counting if you forget a fact. The clock face is a natural 5s table: the minute hand at the 3 means 15 minutes, at the 6 means 30, at the 9 means 45.

These three fact families form a backbone for everything harder. Knowing 5 × 8 = 40 helps you figure out 6 × 8 later (just add one more group of 8: 40 + 8 = 48). Knowing 2 × 7 = 14 helps you get to 4 × 7 = 28 by doubling. The 2s, 5s, and 10s aren't just three easy rows on a multiplication table — they're **anchor facts** that you'll use to derive the ones you don't yet have memorized.
