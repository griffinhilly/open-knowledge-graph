---
id: three-digit-addition-with-regrouping
title: Three-Digit Addition With Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: three-digit-addition-no-regrouping
  type: hard
- id: regrouping-addition-trading-ones-for-tens
  type: hard
builds-toward:
- multi-digit-addition
tags:
- addition
- regrouping
- place-value
stage: concrete-operations
status: draft
---

# Three-Digit Addition With Regrouping

## Core Idea
When adding three-digit numbers, you may need to trade ten ones for one ten, or ten tens for one hundred. This regrouping (carrying) allows you to solve additions like 187 + 125 correctly.

## How It's Best Learned
Start with base-ten blocks to physically show when ten ones must be traded for a ten. Gradually move to drawings, then to the abstract algorithm.

## Common Misconceptions
- Forgetting to add the regrouped ten or hundred.
- Regrouping at the wrong place value.

## Questions

```yaml
- question: "A student solves 256 + 178. In the ones column, she calculates 6 + 8 = 14 and writes '14' in the ones place, then continues to the tens column. What is her error?"
  type: multiple-choice
  options:
    - "She should have started with the hundreds column, not the ones"
    - "She wrote both digits of 14 in the ones place; she should write 4 in the ones place and carry 1 to the tens column"
    - "She made an arithmetic mistake; 6 + 8 does not equal 14"
    - "She should have written 14 in the tens column instead"
  answer: 1
  explanation: "The ones place can only hold a single digit (0–9). When a column sum reaches 10 or more, you cannot write the two-digit result in one column. Instead, write the ones digit (4) in the ones place and carry the tens digit (1) to the next column to the left — this is regrouping. Writing '14' in the ones place implicitly squeezes a tens-place digit into the wrong column, producing a wildly incorrect answer. The carry represents the real-world trade: 14 ones = 1 ten and 4 ones."

- question: "What is the correct answer to 487 + 365?"
  type: multiple-choice
  options:
    - "742"
    - "752"
    - "852"
    - "842"
  answer: 2
  explanation: "Ones: 7 + 5 = 12; write 2, carry 1. Tens: 8 + 6 + 1 (carried) = 15; write 5, carry 1. Hundreds: 4 + 3 + 1 (carried) = 8. Answer: 852. The two most common errors are forgetting to add the carried digit in the tens column (giving 742 or 752 without the second carry) and mishandling two separate carries in the same problem."

- question: "When adding three-digit numbers, it is possible to need to regroup twice in the same problem — once in the ones column and once in the tens column."
  type: true-false
  answer: true
  explanation: "True. Each column is evaluated independently. If the ones column produces a sum of 10 or more, you carry 1 to the tens column. Then the tens column adds its two digits plus the carried 1 — and if that sum also reaches 10 or more, you carry 1 to the hundreds column. Both carries can occur in the same problem. Handling them one at a time, column by column from right to left, keeps the process manageable."

- question: "When you 'carry' a digit in addition, you are changing the total value of the numbers you are adding."
  type: true-false
  answer: false
  explanation: "False. Carrying does not change the value — it reorganizes the same value into proper place-value notation. When ones-column sum equals 12, writing '2' in ones and carrying '1' to tens is just writing 12 as '1 ten and 2 ones,' which equals 12. The total is preserved; you are simply expressing it in a way that fits the positional system. This is why carrying is not a trick — it is the same ten-for-one trade you have been doing with base-ten blocks all along."

- question: "Why is 'carrying' in column addition not a separate trick, but rather the same trade you have been doing with place value all along?"
  type: short-answer
  answer: "Carrying is just the written expression of the trade '10 ones = 1 ten' (or '10 tens = 1 hundred') that you've practiced physically with base-ten blocks. When a column sums to 12, you can't write two digits in one place, so you trade 10 of those units for 1 of the next larger unit — the same trade as swapping 10 unit cubes for 1 rod. The algorithm records this by writing the leftover units in the current column and moving the bundled unit to the next column as a carried digit."
  explanation: "Seeing carrying as a familiar concept (not a new rule) helps students understand *why* the algorithm works rather than memorizing steps blindly. When students understand that a carry represents a real trade — the same trade they made with physical blocks — they are less likely to forget the carried digit and more likely to apply the procedure correctly even in new situations like three-carry problems or multi-digit subtraction with borrowing."
```

## Explainer

You already know how to add three-digit numbers when no place value overflows — you just line up hundreds, tens, and ones and add each column. You also know how to trade 10 ones for 1 ten. Now those two skills combine. When a column's sum reaches 10 or more, you can't fit it in one digit, so you **regroup**: carry 1 into the next column to the left and write only the leftover ones.

Take 187 + 125. Start with the ones: 7 + 5 = 12. You can't write "12" in the ones place, so you write the 2 and carry the 1 ten to the tens column. Now the tens: 1 (carried) + 8 + 2 = 11 tens. Again, too big for one digit — write 1 in the tens place and carry 1 hundred. Finally the hundreds: 1 (carried) + 1 + 1 = 3. Answer: 312. The key is that "carrying" isn't magic — it's the same trade you've always made, just happening inside the written algorithm.

The most common mistake is forgetting the carried digit. A good habit: before moving to the next column, check that you've written the carry mark above it. When you need to regroup twice in one problem — once in the ones and once in the tens — do it one column at a time, left to right from smallest place to largest. Each column is its own mini-problem; the only connection is the digit you carry forward. Keep that carry visible and the rest follows naturally.
