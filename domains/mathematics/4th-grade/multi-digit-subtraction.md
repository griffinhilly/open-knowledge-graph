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

## Explainer

You know place value for whole numbers and you've done two- and three-digit subtraction with regrouping. Multi-digit subtraction extends that same borrowing process to larger numbers — thousands, ten-thousands, and beyond. The algorithm never changes: work right to left, and whenever a digit on top is smaller than the digit below it in the same column, borrow 1 from the next column to the left, converting it into 10 of the current unit.

The most challenging case is subtracting across zeros, like 4,003 − 1,257. When you reach the ones column (3 − 7), you need to borrow — but the tens column has a 0, so there's nothing to borrow from there. You must look further left to the hundreds place, which also has a 0. Keep going left until you find a nonzero digit (the thousands place has 4). You borrow 1 thousand, which becomes 10 hundreds; then borrow 1 hundred, which becomes 10 tens; then borrow 1 ten, which becomes 10 ones. After all that, your ones column has 13, and you can subtract. The chain-borrowing is just the same move repeated across multiple columns. Base-ten blocks make this tangible: physically break a thousand-cube into ten hundred-flats, then break one flat into ten ten-rods, then break one rod into ten unit cubes.

An alternative worth knowing is the **counting-up strategy**: instead of subtracting, find the difference by adding from the smaller number to the larger. To solve 4,003 − 1,257, ask "how much do I need to add to 1,257 to reach 4,003?" Count up to 1,260 (add 3), then to 1,300 (add 40), then to 2,000 (add 700), then to 4,000 (add 2,000), then to 4,003 (add 3). Total added: 3 + 40 + 700 + 2,000 + 3 = 2,746. This method avoids borrowing entirely and is especially useful when the numbers are far apart. Using both methods — and checking one with the other — builds deep number sense alongside algorithmic fluency.
