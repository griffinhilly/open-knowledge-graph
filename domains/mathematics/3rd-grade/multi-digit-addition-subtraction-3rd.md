---
id: multi-digit-addition-subtraction-3rd
title: Multi-Digit Addition and Subtraction
domain: mathematics
course: 3rd-grade
prerequisites:
- id: place-value-three-digits-3rd
  type: hard
builds-toward:
- multi-step-word-problems-addition-subtraction-3rd
tags:
- addition
- subtraction
- multi-digit
- regrouping
stage: concrete-operations
status: validated
---

# Multi-Digit Addition and Subtraction

## Core Idea
Align numbers by place value and operate on each place separately. With regrouping (trading), 10 ones become 1 ten or 10 tens become 1 hundred. 27 + 15: ones (7 + 5 = 12, regroup to 1 ten + 2 ones), tens (2 + 1 + 1 = 4), result is 42.

## How It's Best Learned
Use base-ten blocks to show regrouping. Write in vertical format. Practice repeatedly.

## Common Misconceptions
Not aligning place values; regrouping errors; confusing addition and subtraction regrouping.

## Questions

```yaml
- question: "In the addition problem 27 + 15, you get 12 in the ones column. What do you do with this result?"
  type: multiple-choice
  options:
    - "Write '12' in the ones place of the answer"
    - "Ignore the extra digit and write '2' in the ones place"
    - "Regroup: write '2' in the ones place and carry '1' to the tens column"
    - "Start over — getting 12 in the ones column means you made an error"
  answer: 2
  explanation: "The ones place can only hold a single digit (0–9). When you get 12 ones, that means you have 1 group of ten and 2 leftover ones. You regroup by writing 2 in the ones place and 'carrying' (adding) 1 to the tens column. This regrouping is not a trick — it is the rule that 10 ones equals 1 ten, applied mechanically."

- question: "A student sets up 35 + 214 vertically and aligns the leftmost digits: the 3 in 35 is placed under the 2 in 214. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — you always align the leftmost digits when adding"
    - "The numbers are misaligned; the 5 in 35 should be under the 4 in 214, aligning by the ones place"
    - "35 is too small to add to 214 — you need numbers of equal length"
    - "The student should convert 35 to 035 before beginning"
  answer: 1
  explanation: "Numbers must be aligned by place value — ones under ones, tens under tens, hundreds under hundreds. The 5 in 35 is in the ones place; it belongs under the 4 in 214 (also ones). The 3 in 35 is in the tens place; it belongs under the 1 in 214 (also tens). If you align leftmost digits instead, you end up adding tens to hundreds, which produces a completely wrong answer."

- question: "In subtraction with borrowing, you are trading 1 ten for 10 ones, which keeps the total value of the number the same."
  type: true-false
  answer: true
  explanation: "Borrowing is a trade, not a loss. When you take 1 ten from the tens column and convert it to 10 ones in the ones column, the total value of the number is unchanged (1 ten = 10 ones). You are just repackaging the same quantity into smaller units so you can subtract. This is the reverse of what regrouping in addition does (trading 10 ones for 1 ten)."

- question: "When adding multi-digit numbers using the standard algorithm, you can start from either the left or the right and get the same result."
  type: true-false
  answer: false
  explanation: "The standard addition algorithm requires working right to left (ones first, then tens, then hundreds) because regrouping goes from smaller to larger place values. If you start from the left, you cannot yet know whether a carry will come in from the right, so you cannot correctly fill in the tens or hundreds columns until you have processed the ones. Starting from the left only works if you come back and adjust, which defeats the purpose."

- question: "Why must you align numbers by place value before adding or subtracting? What goes wrong if you don't?"
  type: short-answer
  answer: "Place value alignment ensures that you are adding digits that represent the same-sized units together: ones with ones, tens with tens, hundreds with hundreds. If you misalign, you end up adding, say, tens to hundreds — combining units of different sizes — which produces a nonsense result. For example, adding 35 and 214 with leftmost alignment would put the 3 (30) under the 2 (200), yielding 230 + 14 + 5 = a completely wrong answer."
  explanation: "Alignment is the foundation of the algorithm, not a cosmetic convention. The entire logic of column-by-column arithmetic depends on each column holding digits with the same place value. This is why the vertical format matters — it is a visual tool for enforcing alignment."
```

## Explainer

You already understand three-digit place value — that in the number 347, the 3 means 3 hundreds, the 4 means 4 tens, and the 7 means 7 ones. Multi-digit addition and subtraction is built entirely on that foundation. The standard algorithm is just a systematic way of applying place value one column at a time, from smallest to largest.

When you add 27 + 15, you start with the ones: 7 + 5 = 12. But "12 ones" is a problem — the ones place can only hold a single digit. So you **regroup**: you trade 10 of those ones for 1 ten, leaving 2 ones behind. Now the tens place: 2 tens + 1 ten + the regrouped 1 ten = 4 tens. Result: 42. Every step of this process is just place value — you're applying the rule that 10 of any place value equals 1 of the next larger place.

Subtraction regrouping works in the opposite direction. In 53 − 28, you need to subtract 8 ones from 3 ones — but 3 < 8. So you **borrow** (or "trade"): take 1 ten from the tens column and convert it into 10 ones. Now you have 13 ones and only 4 tens remaining. Then 13 − 8 = 5 ones, and 4 − 2 = 2 tens. Result: 25. You're trading a larger unit for 10 smaller units, which is the reverse of what addition regrouping does.

The vertical format (stacking numbers on top of each other) is a visual aid for keeping place values aligned. Ones above ones, tens above tens, hundreds above hundreds. If you misalign — adding a hundreds digit to a tens digit — you get nonsense. **Alignment is the entire basis of the algorithm.** Base-ten blocks make this concrete: a tens rod really does contain 10 ones blocks, and you can physically snap them apart (borrowing) or click them together (carrying). Once you've done that physically, the written symbols on paper represent the same trade.
