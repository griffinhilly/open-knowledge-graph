---
id: division-word-problems
title: Division Word Problems
domain: mathematics
course: 3rd-grade
prerequisites:
- id: division-facts-within-100
  type: hard
- id: multiplication-word-problems
  type: soft
builds-toward:
- multi-step-word-problems-3rd
- intro-to-long-division
tags:
- word-problems
- division
- problem-solving
stage: concrete-operations
status: validated
---

# Division Word Problems

## Core Idea
Division word problems present either sharing (how many in each group?) or grouping (how many groups?) situations. Students must identify the total, the known value (group size or number of groups), and what is unknown. Writing the division equation and solving completes the problem.

## How It's Best Learned
Sort word problems into 'sharing' and 'grouping' categories before solving. Drawing a diagram or using manipulatives to represent the situation before writing the equation prevents the most common errors.

## Common Misconceptions
- Students may divide in the wrong order (divisor and dividend swapped) if they don't carefully identify the total.
- Students sometimes add or subtract when the situation calls for division.

## Questions

```yaml
- question: "48 books are placed equally on shelves. Each shelf holds 8 books. How many shelves are needed? What is unknown in this problem?"
  type: multiple-choice
  options:
    - "The total number of books (48)"
    - "The number of books per shelf (8)"
    - "The number of shelves"
    - "Whether to multiply or divide"
  answer: 2
  explanation: "Every division word problem has three quantities: total, number of groups, and size of each group. Here, the total is 48 books, the group size is 8 books per shelf, and the number of shelves (groups) is unknown. Identifying the unknown is the key step — once you know which of the three quantities is missing, the equation writes itself: 48 ÷ 8 = 6 shelves."

- question: "A student reads: 'There are 6 bags with 9 apples in each bag. How many apples in all?' The student writes 54 ÷ 6 = 9. What went wrong?"
  type: multiple-choice
  options:
    - "Nothing — the student correctly identified this as a division problem"
    - "The student used multiplication facts, which don't apply here"
    - "The student divided instead of multiplied — the total isn't given, so this is a multiplication problem"
    - "The student swapped the dividend and divisor"
  answer: 2
  explanation: "This problem gives you the number of groups (6 bags) and the group size (9 apples each) and asks for the total — that is a multiplication problem: 6 × 9 = 54. Division is used when the total is given and a group or size quantity is unknown. The student confused the structure by treating a known total as something to solve for."

- question: "In a division word problem, the dividend is always the total being divided."
  type: true-false
  answer: true
  explanation: "The dividend is the whole amount — the total being split into groups. In 48 ÷ 6 = 8, the 48 (dividend) is the total. Identifying the total correctly is the most important step in setting up a division equation. Students who swap the dividend and divisor (e.g., writing 6 ÷ 48) get answers that don't make sense in context."

- question: "In a grouping division problem, the known quantity is the number of groups, and the unknown is how many items go in each group."
  type: true-false
  answer: false
  explanation: "This describes a sharing (partitive) problem, not a grouping problem. In grouping (measurement) division, you know the group SIZE and you're finding the number of groups. Example: '24 apples packed into bags of 6 — how many bags?' You know total (24) and group size (6); the number of groups (4) is unknown. The two interpretations are often confused, but recognizing which quantity is unknown is key."

- question: "What are the three quantities in every division word problem, and how do you determine which operation to use once you've identified them?"
  type: short-answer
  answer: "The three quantities are: (1) the total — the whole amount being divided; (2) the number of groups; (3) the size of each group. In a division problem, the total is always known and one of the other two quantities is unknown. If you know total and group size, divide to find number of groups. If you know total and number of groups, divide to find group size. If the total is unknown, multiply instead."
  explanation: "This three-quantity framework is the diagnostic tool that lets you set up any word problem correctly. Before writing an equation, students should label: 'What is my total? What is my group size? What is my number of groups? Which one am I solving for?' That analysis determines both the operation and the correct arrangement of numbers in the equation."
```

## Explainer

You know your division facts within 100, and you've already solved multiplication word problems. Division word problems build on both — but they add one layer of difficulty: you have to figure out what kind of division situation you're reading before you can write the equation.

Division situations come in two varieties. **Sharing** (partitive division) asks: if I split this total into a known number of groups, how many go in each group? "24 apples shared equally among 6 baskets — how many per basket?" You know the total (24) and the number of groups (6); you're finding the group size. **Grouping** (measurement division) asks: if I pack this total into groups of a known size, how many groups do I get? "24 apples packed into bags of 6 — how many bags?" You know the total (24) and the group size (6); you're finding the number of groups. Notice that the equation is identical (24 ÷ 6 = 4) in both cases — only the story and what the answer represents differ.

The practical skill is labeling all three quantities in a story: the **total** (the whole amount being divided), the **number of groups**, and the **size of each group**. Two of the three will be given; the third is what you solve for. "48 students divided into teams of 8 — how many teams?" Total = 48, group size = 8, number of groups = unknown → 48 ÷ 8 = 6. Once you've identified which quantity is missing, the equation writes itself.

The connection to multiplication is deliberate. Division and multiplication are inverse operations, just as subtraction undoes addition. If 6 × 8 = 48, then 48 ÷ 8 = 6 and 48 ÷ 6 = 8. When a division fact is hard to recall, ask: "what times [the divisor] equals the dividend?" — and turn division into multiplication you may already know. Your prior work on multiplication word problems gave you experience identifying totals and groups; division word problems use exactly the same structure, just with a different quantity unknown.
