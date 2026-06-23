---
id: arithmetic-patterns-3rd
title: Arithmetic Patterns
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-within-100
  type: hard
- id: addition-within-100
  type: soft
- id: multiples-of-a-number
  type: soft
- id: number-patterns-skip-counting-1st
  type: soft
builds-toward:
- number-patterns-and-relationships
- factors-and-multiples
- arithmetic-sequences
tags:
- patterns
- arithmetic
- sequences
- multiplication
stage: concrete-operations
status: validated
---

# Arithmetic Patterns

## Core Idea
Arithmetic patterns are regular numerical sequences formed by adding or multiplying the same amount each step. Students identify and extend patterns in addition tables (each row increases by the same amount) and multiplication tables (products in a column are multiples of the column number). They explain patterns using properties of operations.

## How It's Best Learned
Use color-coding on multiplication tables to highlight patterns: the 9s column has digits that sum to 9, every second multiple of 2 is even, and so on. Have students write rules in their own words before formalizing.

## Common Misconceptions
- Students may spot a pattern in the first few terms but then make an error when extending it.
- Confusing additive and multiplicative patterns — '×3' and '+3' produce very different sequences.

## Questions

```yaml
- question: "A student looks at the sequence 2, 6, 18, 54 and says 'Add 4 each time to get the next number.' What is wrong with this analysis?"
  type: multiple-choice
  options:
    - "The sequence doesn't have a rule"
    - "The student confused a multiplicative pattern for an additive one; each term is multiplied by 3, not increased by 4"
    - "The student is correct; 2 + 4 = 6"
    - "The student used the right type of rule but made an arithmetic mistake"
  answer: 1
  explanation: "2, 6, 18, 54 is a multiplicative pattern: each term is multiplied by 3 (2×3=6, 6×3=18, 18×3=54). It is not an additive pattern — the gaps between consecutive terms are 4, 12, 36, which are not equal. The student noticed that 6−2=4 and assumed that gap repeats, but additive patterns require a *constant* difference. This is the core distinction: additive patterns grow by adding the same amount; multiplicative patterns grow by multiplying by the same factor."

- question: "In a multiplication table, what is always true of every product in the 5s column?"
  type: multiple-choice
  options:
    - "Every number is odd"
    - "Every number ends in 5 or 0"
    - "Every number is greater than 10"
    - "Every number is a multiple of 2"
  answer: 1
  explanation: "Multiples of 5 always end in 5 or 0, alternating as you go down the column: 5, 10, 15, 20, 25... This is a consequence of how base-ten place value interacts with multiplication by 5. Noticing this pattern is an example of using arithmetic structure — rather than memorizing each product separately, you can check your work using the 'ends in 5 or 0' rule. Similar patterns exist for 2s (always even), 9s (digits sum to 9), and others."

- question: "Two number sequences can start with the same first two terms but diverge dramatically if one follows an additive rule and the other follows a multiplicative rule."
  type: true-false
  answer: true
  explanation: "True. For example, both '+3' and '×3' sequences starting from 3 would begin 3, 6... but then diverge: the additive sequence continues 9, 12, 15, 18..., while the multiplicative sequence continues 18, 54, 162, 486... By the tenth term, the additive sequence is around 30 while the multiplicative sequence is over 19,000. Additive growth is linear; multiplicative growth is exponential. The distinction is not just academic — it changes every prediction you make."

- question: "Finding the next two terms of a pattern is sufficient evidence that you understand the pattern's rule."
  type: true-false
  answer: false
  explanation: "False. You can get the next few terms right by trial-and-error or by noticing the immediate difference between adjacent terms — without grasping the underlying rule. The rule is a more powerful thing: 'add 6 each time' or 'each term is 4 times its position number.' With the rule, you can find the 50th term, check whether 148 belongs to the pattern, or explain why the pattern works. Extending a few terms shows recognition; articulating the rule shows understanding."

- question: "What is the difference between an additive pattern and a multiplicative pattern, and why does the distinction matter?"
  type: short-answer
  answer: "An additive pattern is formed by adding the same amount each step (e.g., 3, 7, 11, 15 — add 4 each time). A multiplicative pattern is formed by multiplying by the same factor each step (e.g., 2, 6, 18, 54 — multiply by 3 each time). The distinction matters because they grow at completely different rates: additive patterns grow linearly while multiplicative patterns grow exponentially, and confusing the two rule-type leads to badly wrong predictions for later terms."
  explanation: "Recognizing which type of rule governs a pattern is the key analytical step — before you can extend a pattern accurately, you have to know whether to add or multiply. This distinction also builds the groundwork for algebra: additive patterns become linear equations, multiplicative patterns become exponential ones. Developing the habit of asking 'is this a constant difference or a constant ratio?' is the beginning of algebraic thinking."
```

## Explainer

A pattern is a sequence with a rule. Once you know the rule, you can predict any term in the sequence — even ones far down the list — without writing them all out. In arithmetic, there are two main kinds of rules: **additive patterns** (add the same amount each step) and **multiplicative patterns** (multiply by the same amount each step). These look different and grow at very different rates.

In an additive pattern like 5, 8, 11, 14, ..., you're adding 3 each time. The gap between any two neighbors is always 3. This is the same structure as skip-counting, which you've practiced before. In a multiplication table, each row is also an additive pattern: the row for 4 goes 4, 8, 12, 16, ... — you add 4 each time. The row for 7 adds 7 each time. Recognizing this helps you see multiplication tables not as a list to memorize but as a system with built-in structure.

When you look at a multiplication table, more patterns emerge. Every number in the 2s column is even. The 5s column alternates between 5 and 0 in the ones place. The 9s column has a special property: the two digits of each product always sum to 9 (9, 18, 27, 36 — check: 1+8=9, 2+7=9, 3+6=9). These aren't coincidences; they're consequences of how multiplication works with our base-ten number system.

The key skill is being able to describe a pattern with a **rule** — not just the next few terms. "Add 6 each time" is a rule. "Each number is three times the position number" is a rule. Once you have the rule, you can extend the pattern confidently, check whether a number belongs to it, and explain to someone else why the pattern works. This is early algebraic thinking: you're treating a rule as an object you can describe and use, not just a sequence you happen to notice.
