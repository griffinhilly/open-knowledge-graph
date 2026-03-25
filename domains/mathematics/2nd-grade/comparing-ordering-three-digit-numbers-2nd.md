---
id: comparing-ordering-three-digit-numbers-2nd
title: Comparing and Ordering Three-Digit Numbers
domain: mathematics
course: 2nd-grade
prerequisites:
- id: place-value-hundreds-2nd
  type: hard
- id: comparing-two-digit-numbers
  type: hard
- id: comparing-two-digit-numbers-2nd-grade
  type: soft
builds-toward:
- estimation-and-rounding-2nd
tags:
- comparison
- three-digit
- ordering
stage: concrete-operations
status: validated
---
# Comparing and Ordering Three-Digit Numbers

## Core Idea
Ordering three-digit numbers follows a hierarchy: compare hundreds first, then tens, then ones. Numbers can be arranged from least to greatest or greatest to least using place-value understanding.

## Questions

```yaml
- question: "A student compares 356 and 419. She says 356 is greater because it has a 5 in the tens place and 419 only has a 1. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "She is correct — the tens digit is the most important digit"
    - "She forgot to also check the ones place"
    - "She compared tens first, but hundreds must be checked first — 419 has 4 hundreds and 356 has 3 hundreds, so 419 is greater"
    - "She should add all the digits together to compare"
  answer: 2
  explanation: "The hundreds place is always checked first when comparing three-digit numbers. 419 has 4 hundreds (400) and 356 has 3 hundreds (300). Since 4 > 3, 419 is greater — the tens and ones digits are irrelevant. The hundreds place contributes up to 900 to a number's value, while tens and ones together contribute at most 99. A single hundreds difference always overrules any combination of lower digits."

- question: "Put these numbers in order from least to greatest: 743, 128, 734"
  type: multiple-choice
  options:
    - "128, 743, 734"
    - "128, 734, 743"
    - "734, 128, 743"
    - "734, 743, 128"
  answer: 1
  explanation: "First, 128 has 1 hundred — clearly smallest. Then compare 743 and 734: both have 7 hundreds (tied), so move to tens. 743 has 4 tens; 734 has 3 tens. Since 4 > 3, 743 > 734. Correct order: 128, 734, 743. The three-step process — compare hundreds, then tens, then ones — is applied one place at a time, stopping as soon as a difference is found."

- question: "When comparing 503 and 498, the hundreds digit alone tells you which number is greater without needing to look at the tens or ones."
  type: true-false
  answer: true
  explanation: "503 has 5 hundreds; 498 has 4 hundreds. Since 5 > 4, 503 > 498, regardless of what the tens and ones say. You never need to examine lower place values when a higher place value has already decided the comparison. The ones digit 3 vs. 8 is irrelevant here."

- question: "A number with a 9 in the ones place is always greater than a number with a 1 in the ones place."
  type: true-false
  answer: false
  explanation: "The ones place is the least important position. For example, 201 > 199, even though 199 has a 9 in the ones place and 201 has only a 1. The hundreds digit (2 vs. 1) determines the comparison before the ones digit is ever considered. Higher place values always override lower ones."

- question: "If two three-digit numbers have different hundreds digits, do you need to look at the tens or ones digits to determine which is greater? Explain why."
  type: short-answer
  answer: "No. If the hundreds digits differ, the number with the larger hundreds digit is greater — period. The hundreds place contributes up to 900 to a number's value, while tens and ones together contribute at most 99. A difference of just 1 hundred (100) is always more than the maximum possible contribution from tens and ones combined."
  explanation: "Place value is a strict hierarchy. Each place is worth ten times the place to its right, so a larger digit in a higher position always wins. The ones and tens digits only matter as tiebreakers when the higher digits are equal."
```

## Explainer

When you learned to compare two-digit numbers, you discovered a key rule: look at the tens place first. If the tens digits differ, the number with the bigger tens digit is larger — no matter what the ones digit says. You can extend exactly the same logic to three-digit numbers, adding one step at the front: start with the hundreds place.

Think of a three-digit number as having three slots, each with a different level of importance. The **hundreds place** is the most important — it tells you roughly how big the number is. The **tens place** is the middle slot, used only when the hundreds digits are equal. The **ones place** is the tiebreaker, used only when both hundreds and tens match. This three-step process is called **comparing by place value**, and it is the same strategy you used with two-digit numbers, just with one extra layer added at the front.

Here is a concrete example: compare 453 and 481. Both have a 4 in the hundreds place, so hundreds are tied — move to tens. 453 has 5 tens and 481 has 8 tens. Since 5 < 8, we conclude 453 < 481. We never needed to look at the ones place. Now try 327 vs. 319. Hundreds are tied (both 3). Tens: 327 has 2 tens, 319 has 1 ten. Since 2 > 1, we conclude 327 > 319 — the ones digits are irrelevant.

**Ordering** a list of numbers from least to greatest (or greatest to least) is just comparing done repeatedly. A helpful strategy is to sort by hundreds first — group all the 100s together, all the 200s together, and so on. Within each hundreds group, sort by tens, then by ones. This is like sorting a stack of envelopes: rough groupings first, then fine-tuning within each group. With practice, this left-to-right place-value scan becomes automatic and fast.
