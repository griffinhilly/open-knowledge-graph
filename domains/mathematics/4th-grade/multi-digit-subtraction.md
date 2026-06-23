---
id: multi-digit-subtraction
title: Multi-Digit Subtraction
domain: mathematics
course: 4th-grade
prerequisites:
- id: place-value-whole-numbers
  type: hard
- id: multi-digit-addition
  type: soft
- id: three-digit-subtraction
  type: soft
- id: two-digit-subtraction-with-regrouping
  type: soft
- id: two-step-word-problems
  type: soft
- id: three-digit-subtraction-with-regrouping
  type: hard
builds-toward:
- estimation-strategies
- adding-subtracting-decimals
tags:
- arithmetic
- subtraction
- place-value
stage: concrete-operations
status: validated
---
# Multi-Digit Subtraction

## Core Idea
Multi-digit subtraction requires "borrowing" or regrouping when a digit in the top number is smaller than the corresponding digit in the bottom number. Regrouping means converting 1 of the next-higher unit into 10 of the current unit (1 hundred becomes 10 tens). Subtraction across zeros (e.g., 4,003 - 1,257) is especially challenging because the student must regroup across multiple places. Understanding subtraction as both "take away" and "difference" (the distance between two numbers) supports flexible thinking.

## How It's Best Learned
Base-ten blocks make regrouping tangible: physically break a hundred-flat into 10 ten-rods. Practice subtraction across zeros with explicit attention to the chain of borrowing. Alternative strategies like "counting up" (finding the difference by adding from the smaller to the larger) build number sense alongside the standard algorithm.

## Common Misconceptions
- Subtracting the smaller digit from the larger in each column regardless of position (e.g., 42 - 17 = 35 because 7 - 2 = 5).
- Regrouping errors when zeros are involved, especially in numbers like 3,000 or 5,006.
- Forgetting to reduce the digit in the column borrowed from.

## Questions

```yaml
- question: "A student solves 432 - 175 and writes 343 as the answer. Which error explains this result?"
  type: multiple-choice
  options:
    - "They forgot to reduce the hundreds digit after borrowing"
    - "They subtracted the smaller digit from the larger in each column, reversing the direction when the bottom digit was bigger"
    - "They borrowed correctly but then added instead of subtracted"
    - "They regrouped in the wrong column"
  answer: 1
  explanation: "The student saw 2 < 5 in the ones column and did 5 - 2 = 3 instead of borrowing; in the tens column, 3 < 7, so they did 7 - 3 = 4; hundreds: 4 - 1 = 3 normally. Result: 343. The correct approach requires borrowing: ones column borrows (12 - 5 = 7, tens becomes 2); tens column borrows (12 - 7 = 5, hundreds becomes 3); hundreds: 3 - 1 = 2. Correct answer: 257."

- question: "To solve 3,000 - 1,456, a student must borrow for the ones column. Which column can they actually borrow from?"
  type: multiple-choice
  options:
    - "The tens column — 3,000 has plenty of tens"
    - "They cannot solve this because there are no tens, hundreds, or ones to borrow from directly"
    - "The thousands column — borrow 1 thousand and convert it through hundreds and tens to get 10 ones"
    - "Skip borrowing and round 3,000 to 2,999 first"
  answer: 2
  explanation: "In 3,000, the ones, tens, and hundreds are all zero — there is nothing to borrow from directly. The student must go to the thousands place (3) and borrow 1 thousand. That becomes 10 hundreds; then borrow 1 hundred, which becomes 10 tens; then borrow 1 ten, which becomes 10 ones. This chain converts value down three columns. The result: 3,000 - 1,456 = 1,544."

- question: "When subtracting across zeros (like 4,000 - 1,234), you must borrow from the thousands place because the hundreds, tens, and ones places are all zero."
  type: true-false
  answer: true
  explanation: "Correct. When the column you need to borrow from holds a 0, you must look further left until you find a nonzero digit. In 4,000, the hundreds (0), tens (0), and ones (0) have nothing to lend. You borrow 1 thousand and chain it down: 1,000 → 10 hundreds → 10 tens → 10 ones. Each step in the chain is just the standard regroup move repeated."

- question: "The counting-up strategy for subtraction only works when the two numbers are close together."
  type: true-false
  answer: false
  explanation: "Counting up — adding from the smaller number to the larger — works for any subtraction problem. For 4,003 - 1,257: count up from 1,257 by adding 3 (→1,260), then 40 (→1,300), then 700 (→2,000), then 2,000 (→4,000), then 3 (→4,003), totaling 2,746. The strategy avoids borrowing entirely and is especially useful for problems involving zeros."

- question: "Explain what must happen when you try to subtract 4,001 - 2,345 and need to borrow for the ones column. Why can't you borrow from the tens place?"
  type: short-answer
  answer: "You can't borrow from the tens place because it holds a 0 — there is nothing there. The hundreds place also holds 0. You must go to the thousands place (4), borrow 1 thousand (thousands becomes 3), convert it to 10 hundreds; then borrow 1 hundred (hundreds becomes 9), convert to 10 tens; then borrow 1 ten (tens becomes 9), convert to 10 ones. Now the ones column has 11 and the subtraction can proceed."
  explanation: "Regrouping across zeros requires a chain: you can only borrow from a column that has a nonzero digit. Each borrowed unit converts to 10 of the next smaller unit. This chain is the standard regroup move repeated until you find a nonzero digit — a key skill in multi-digit subtraction."
```

## Explainer

You know place value for whole numbers and you've done two- and three-digit subtraction with regrouping. Multi-digit subtraction extends that same borrowing process to larger numbers — thousands, ten-thousands, and beyond. The algorithm never changes: work right to left, and whenever a digit on top is smaller than the digit below it in the same column, borrow 1 from the next column to the left, converting it into 10 of the current unit.

The most challenging case is subtracting across zeros, like 4,003 − 1,257. When you reach the ones column (3 − 7), you need to borrow — but the tens column has a 0, so there's nothing to borrow from there. You must look further left to the hundreds place, which also has a 0. Keep going left until you find a nonzero digit (the thousands place has 4). You borrow 1 thousand, which becomes 10 hundreds; then borrow 1 hundred, which becomes 10 tens; then borrow 1 ten, which becomes 10 ones. After all that, your ones column has 13, and you can subtract. The chain-borrowing is just the same move repeated across multiple columns. Base-ten blocks make this tangible: physically break a thousand-cube into ten hundred-flats, then break one flat into ten ten-rods, then break one rod into ten unit cubes.

An alternative worth knowing is the **counting-up strategy**: instead of subtracting, find the difference by adding from the smaller number to the larger. To solve 4,003 − 1,257, ask "how much do I need to add to 1,257 to reach 4,003?" Count up to 1,260 (add 3), then to 1,300 (add 40), then to 2,000 (add 700), then to 4,000 (add 2,000), then to 4,003 (add 3). Total added: 3 + 40 + 700 + 2,000 + 3 = 2,746. This method avoids borrowing entirely and is especially useful when the numbers are far apart. Using both methods — and checking one with the other — builds deep number sense alongside algorithmic fluency.
