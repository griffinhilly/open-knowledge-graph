---
id: comparing-three-digit-numbers
title: Comparing Three-Digit Numbers
domain: mathematics
course: 2nd-grade
prerequisites:
- id: three-digit-number-forms
  type: hard
- id: comparing-two-digit-numbers
  type: hard
builds-toward:
- number-line-to-1000
- rounding-whole-numbers
tags:
- comparison
- three-digit
- greater-than
- less-than
- ordering
stage: concrete-operations
status: validated
---

# Comparing Three-Digit Numbers

## Core Idea
To compare three-digit numbers, compare digits from left to right, starting with the hundreds place. If the hundreds digits differ, the number with the greater hundreds digit is larger — regardless of the tens and ones. If hundreds are equal, compare the tens digits; if those are equal too, compare ones. Record comparisons using the symbols >, <, and =.

## How It's Best Learned
Start by comparing numbers with very different hundreds digits (e.g., 721 vs. 389) before introducing cases where hundreds are the same. Use base-ten blocks to make the comparison concrete. Have students justify their comparisons verbally: 'I know 721 > 389 because 7 hundreds is more than 3 hundreds.'

## Common Misconceptions
- Comparing the total number of digits rather than place values (thinking 99 > 100 because 9 > 1).
- Not stopping at the first unequal place — continuing to compare all digits unnecessarily.
- Reversing the < and > symbols.

## Questions

```yaml
- question: "A student compares 482 and 97 and says 97 is bigger because '9 is greater than 4.' What mistake is the student making?"
  type: multiple-choice
  options:
    - "The student is using the wrong comparison symbol"
    - "The student compared the wrong digit — they should compare the first digits of the longer number to get the right answer"
    - "The student compared individual digits without considering their place values — 482 has a hundreds digit and 97 does not, making 482 far larger"
    - "The student forgot to add the digits together first"
  answer: 2
  explanation: "The 9 in 97 is in the tens place (representing 90), while the 4 in 482 is in the hundreds place (representing 400). When comparing numbers with different numbers of digits, the number with more digits is always larger — hundreds beat tens. The student's error is cherry-picking the largest-looking digit without considering what place value it occupies."

- question: "To compare 563 and 578, what is the correct first step?"
  type: multiple-choice
  options:
    - "Compare the ones digits: 3 vs. 8"
    - "Compare the tens digits: 6 vs. 7"
    - "Compare the hundreds digits: 5 vs. 5"
    - "Add all the digits in each number and compare the sums"
  answer: 2
  explanation: "Always start at the leftmost (highest) place value: the hundreds. Here, both numbers have 5 hundreds, so they are equal at this position and you move to the tens. Comparing ones first or adding all digits are incorrect strategies that can give wrong results. Adding the digits (5+6+3=14 vs. 5+7+8=20) doesn't compare place values and would give nonsense comparisons."

- question: "When comparing two three-digit numbers, you must examine all three digits before deciding which number is greater."
  type: true-false
  answer: false
  explanation: "You only need to compare until you find a difference. If the hundreds digits differ, the comparison is done — the one with more hundreds is greater, regardless of the tens and ones. You only move to the tens if hundreds are equal, and only to ones if tens are also equal. Stopping at the first unequal digit is both faster and the logical basis of place-value comparison."

- question: "In the comparison 741 > 389, you only need to look at the hundreds digits to determine which number is greater."
  type: true-false
  answer: true
  explanation: "741 has 7 hundreds; 389 has 3 hundreds. Seven hundreds (700) is greater than three hundreds (300), regardless of what the tens and ones say. Once the highest place value differs, the comparison is settled. This is exactly what makes place-value notation powerful: the most significant digit tells you the most."

- question: "Explain why, when comparing 741 and 389, you don't need to look at the tens or ones digits at all."
  type: short-answer
  answer: "The hundreds digit represents the largest value in a three-digit number. 741 has 7 hundreds (700) and 389 has only 3 hundreds (300). Even if 389 had the largest possible tens and ones (99), it would only reach 399 — still less than 700. Once you see that one number has more hundreds, no combination of tens and ones in the other number can make up the difference."
  explanation: "Place value is hierarchical: each position is worth ten times the position to its right. The hundreds place dominates because 1 hundred = 10 tens = 100 ones. Seeing this hierarchy is the key insight behind left-to-right comparison: the leftmost digit tells you the most, so you start there and stop as soon as you find a difference."
```

## Explainer

When you learned to compare two-digit numbers, you discovered that the **tens place** is the most important digit — 73 is greater than 58 because 7 tens beats 5 tens, no matter what the ones digits say. Three-digit numbers work exactly the same way, just with one extra place added at the front: the **hundreds place**. And hundreds beat everything. A number with more hundreds is bigger, period — you do not even need to look at the tens or ones.

Compare 741 and 389. How many hundreds does each have? 741 has 7 hundreds; 389 has 3 hundreds. Seven hundreds is more than three hundreds, so 741 > 389. You are done — the tens and ones digits are irrelevant. This is why place value is so powerful: it lets you make decisions quickly by looking at the most significant digit first.

Now suppose the hundreds are the same. Compare 456 and 431. Both have 4 hundreds, so move to the **tens place**: 5 tens versus 3 tens. Five is more, so 456 > 431. If the tens are also equal — compare 527 and 524 — then finally look at the **ones place**: 7 versus 4, so 527 > 524. The rule is always "compare left to right, and stop as soon as you find a difference."

A helpful way to remember the **< and > symbols** is that the symbol is an arrow that opens toward the bigger number. 741 > 389 means "741 is greater than 389," and the open mouth of > faces the 741. Alternatively, think of the symbol as a hungry mouth that always eats the bigger number. Use base-ten blocks if you want a concrete check: build both numbers and see which pile of hundreds blocks is taller.
