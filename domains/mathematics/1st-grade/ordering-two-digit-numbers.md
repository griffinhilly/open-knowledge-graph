---
id: ordering-two-digit-numbers
title: Ordering Two-Digit Numbers
domain: mathematics
course: 1st-grade
prerequisites:
- id: core-number
  type: hard
- id: grade-seriation
  type: hard
- id: discernment-same-different
  type: soft
- id: comparing-two-digit-numbers
  type: hard
tags:
- ordering
- two-digit-numbers
- comparing
- number-sense
- least-to-greatest
stage: pre-formal
status: validated
---

# Ordering Two-Digit Numbers

## Core Idea
Ordering two-digit numbers means arranging a set of numbers from least to greatest or greatest to least. Students first sort by tens digit, then by ones digit within ties. This extends pairwise comparison to sequences and prepares students for reasoning about number position on a number line.

## How It's Best Learned
Give students sets of number cards to physically sort and re-sort in both directions. Start with three numbers, then build to larger sets. Require students to explain reasoning using place value language (tens first, then ones).

## Common Misconceptions
- Ordering by ones digit rather than tens digit.
- Difficulty when multiple numbers share the same tens digit.
- Reversing the meaning of 'least to greatest' and 'greatest to least.'

## Questions

```yaml
- question: "Put these numbers in order from least to greatest: 37, 31, 45, 39. Which list is correct?"
  type: multiple-choice
  options:
    - "31, 37, 39, 45"
    - "31, 39, 37, 45 — order by ones digit (1, 9, 7, 5)"
    - "45, 39, 37, 31 — that is greatest to least"
    - "37, 31, 39, 45 — put the smaller 30s first in any order"
  answer: 0
  explanation: "All four numbers have tens digits of 3, 3, 3, and 4. The 40s number (45) is largest, so it goes last. Among the three 30s, compare ones digits: 1 < 7 < 9, giving 31, 37, 39. Option B is the classic error — sorting by ones digit rather than tens digit first."

- question: "You are ordering 54, 47, and 58. Which number belongs in the middle position?"
  type: multiple-choice
  options:
    - "47 — it has the smallest tens digit"
    - "54 — it is between 47 and 58"
    - "58 — it has the largest ones digit"
    - "51 — it is halfway between 47 and 58"
  answer: 1
  explanation: "47 has a tens digit of 4; 54 and 58 both have tens digits of 5. So 47 is least. Between 54 and 58, compare ones: 4 < 8, so 54 < 58. The order is 47, 54, 58 — and 54 is in the middle. Option D names a number not even in the set, which is a common error when students try to calculate a middle rather than ordering what they were given."

- question: "When two numbers share the same tens digit, you compare their ones digits to determine which is smaller."
  type: true-false
  answer: true
  explanation: "Correct. The tens digit is the primary sort key. Only when tens digits are equal do you move to the ones digit as a tiebreaker. For example, 47 and 43 both have tens digit 4, so you compare 7 and 3: since 3 < 7, the number 43 is smaller."

- question: "When ordering the numbers 63, 28, and 71 from least to greatest, the best first step is to compare their ones digits."
  type: true-false
  answer: false
  explanation: "The tens digit is always compared first. Here the tens digits are 6, 2, and 7 — all different — so the order is determined immediately: 28 (2 tens), 63 (6 tens), 71 (7 tens). You only need to examine ones digits when two or more numbers share the same tens digit."

- question: "A student arranges 42, 18, 47, and 23 as: 18, 23, 42, 47. Explain the rule the student used to get this correct order."
  type: short-answer
  answer: "The student sorted by tens digit first: 18 (1 ten) comes before 23 (2 tens), which comes before 42 and 47 (4 tens each). For the two numbers that share a tens digit (42 and 47), the student then compared ones digits: 2 < 7, so 42 comes before 47."
  explanation: "This two-step rule — tens first, ones as a tiebreaker — is the core of ordering two-digit numbers. It mirrors place value: tens represent larger groups, so they dominate the comparison. Ones only matter when tens are equal, just as you sort houses by block before sorting by house number within a block."
```

## Explainer

You already know how to **compare** two two-digit numbers: you look at the tens digit first, and whichever number has more tens is bigger. If the tens digits are the same, you compare the ones. That skill — comparing a pair of numbers — is the foundation for everything in ordering. **Ordering** just means applying that comparison skill to a whole group at once, arranging them from least to greatest or greatest to least.

Here is one way to think about it: imagine each two-digit number as a house on a street. The tens digit tells you which block the house is on (the 20s block, the 40s block, and so on). The ones digit tells you which house within that block. To arrange the houses in order, you first sort them by block — all the 20s together, then all the 30s, then the 40s. Within each block, you sort by house number. This two-step process (tens first, ones second) is exactly the rule for ordering numbers.

A useful strategy when you have a set of numbers is to **group by tens first**. Take the numbers 47, 23, 51, 38, and 29. Before putting them in order, notice: one is in the 50s, one is in the 40s, one is in the 30s, and two are in the 20s. That gives you the rough order immediately — the 20s come first, then 30s, 40s, 50s. The only careful decision is within the 20s: is 23 or 29 smaller? Since 3 < 9, 23 comes before 29. So the full order is 23, 29, 38, 47, 51.

When the direction is **greatest to least**, you are simply reversing this process — starting from the largest (highest tens digit, then highest ones) and working down. The comparison rules are exactly the same; you just read the result in the opposite direction. Practicing both directions builds a flexible sense of where numbers sit on the number line, which you will use throughout all of your future work with numbers.
