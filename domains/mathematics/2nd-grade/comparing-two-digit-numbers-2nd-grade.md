---
id: comparing-two-digit-numbers-2nd-grade
title: Comparing Two-Digit Numbers
domain: mathematics
course: 2nd-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
- id: comparing-quantities-more-less
  type: soft
builds-toward:
- comparing-ordering-three-digit-numbers-2nd
tags:
- comparison
- two-digit
- greater-than
- less-than
stage: concrete-operations
status: validated
---

# Comparing Two-Digit Numbers

## Core Idea
Comparing two-digit numbers first examines the tens digits. If they differ, the number with more tens is greater. If tens are equal, compare the ones digits. Understanding place value is key to accurate comparison.

## Questions

```yaml
- question: "A student says 48 is greater than 51 because 'the ones digit 8 is bigger than the ones digit 1.' What mistake is the student making?"
  type: multiple-choice
  options:
    - "The student is correct — 8 > 1, so 48 > 51"
    - "The student is comparing ones digits without first comparing tens digits. 51 has 5 tens and 48 has only 4 tens, so 51 > 48 regardless of the ones"
    - "The student needs to add all the digits: 4 + 8 = 12 and 5 + 1 = 6, so 48 wins"
    - "Both numbers are equal because they each have exactly two digits"
  answer: 1
  explanation: "This is the core misconception this topic addresses. Tens must always be compared first because one ten (10) is worth more than any possible ones digit (maximum 9). No matter how large the ones digit of 48 is, 48 can never exceed 51 while having fewer tens. Once the tens differ, the comparison is decided — the ones digits are irrelevant."

- question: "Compare 73 and 76. Which statement is correct, and why?"
  type: multiple-choice
  options:
    - "73 > 76, because 3 ones is less than 6 ones and smaller parts make the whole larger"
    - "73 < 76, because the tens digits are equal, so the ones digits decide: 3 ones < 6 ones"
    - "73 = 76, because both numbers have the same tens digit (7)"
    - "73 > 76, because 7 + 3 = 10, which is larger than 7 + 6 = 13"
  answer: 1
  explanation: "When the tens digits are equal — both numbers have 7 tens — the tens cannot break the tie. You then move to the ones: 3 < 6, so 73 < 76. This is the second step of the comparison rule: start at the tens, move to ones only if needed. Option 2 is wrong because equal tens do not mean equal numbers — you still need to check ones."

- question: "When comparing 62 and 57, you must look at the ones digits to determine which number is greater."
  type: true-false
  answer: false
  explanation: "62 has 6 tens and 57 has 5 tens. Since the tens digits differ, the comparison is decided by the tens alone: 6 tens > 5 tens, so 62 > 57. You never need to look at the ones digits when the tens are already different. The rule is: compare tens first; only move to ones if tens are equal."

- question: "A number with 3 tens and 9 ones is always greater than any number with only 2 tens."
  type: true-false
  answer: true
  explanation: "A number with 3 tens and 9 ones is 39. Any number with only 2 tens is at most 29 (2 tens and 9 ones). Since 3 tens > 2 tens, the first number wins regardless of the ones digit. One ten equals 10, which is larger than the maximum ones digit (9), so a difference of even one full ten can never be overcome by the ones digit alone."

- question: "Explain why you always compare the tens digits first when comparing two two-digit numbers, and when you need to look at the ones digits."
  type: short-answer
  answer: "You compare tens first because tens are worth more than ones. A single ten (10) is already greater than the largest possible ones digit (9), so any difference in the tens place determines which number is larger — the ones digits cannot change that outcome. You only need to compare ones digits when the tens digits are exactly equal, because only then does the tens place leave the comparison unresolved."
  explanation: "This same 'start with the highest place value' logic extends to three-digit, four-digit, and larger numbers. The principle is always: compare the most significant digit first, move right only when digits tie. Understanding why it works — not just that it works — lets students apply the rule confidently to larger numbers."
```

## Explainer

You already know that two-digit numbers are built from **tens** and **ones** — 47 means four tens and seven ones, not forty-seven isolated objects. That place-value understanding is exactly what makes comparing two-digit numbers logical rather than a guessing game: you compare the most powerful digit first.

Here is the key insight: tens are worth more than ones. One ten (10) is already bigger than the largest single digit (9). So when you compare 47 and 53, you don't need to look at the ones digits at all — the tens tell the whole story. 53 has 5 tens; 47 has only 4 tens. Five tens beats four tens, so 53 > 47. Even if 47 had 9 ones instead of 7, it would still be less than 53, because no number of ones can overcome the gap of one full ten.

The interesting case is when the tens digits are equal. Compare 47 and 43: both have 4 tens, so they're tied. Now the **ones digits** break the tie. 47 has 7 ones; 43 has only 3 ones. Seven ones beats three ones, so 47 > 43. The rule is always the same: start with the largest place value, work toward the smallest, and stop as soon as the digits differ.

The symbols >, <, and = record these comparisons. A helpful image: the open end of > or < always faces the larger number, like a mouth eating the bigger amount. So 47 < 53 and 53 > 47 express the exact same relationship from two different viewpoints. When both digits are identical — like 50 and 50 — the equals sign = applies: same tens, same ones, same value.
