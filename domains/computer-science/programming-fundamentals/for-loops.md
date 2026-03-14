---
id: for-loops
title: For Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: while-loops
  type: hard
builds-toward:
- loop-control-statements
- arrays-and-lists
- nested-loops
- list-comprehensions
tags:
- for
- iteration
- range
- traversal
- sequences
stage: abstract-reasoning
status: validated
---

# For Loops

## Core Idea
A for loop iterates over a sequence (a range of numbers, a list, a string, etc.), executing the loop body once for each element. In most modern languages, for-each style loops bind the loop variable to each element in turn, making traversal cleaner than equivalent while loops. Range-based iteration (e.g., range(n)) generates a sequence of integers, enabling counted repetition. For loops are preferred when the number of iterations or the sequence to traverse is known ahead of time.

## How It's Best Learned
Convert while loops to for loops and vice versa to understand their equivalence. Iterate over strings, lists, and ranges. Count elements, accumulate sums, and search for values.

## Common Misconceptions
- Modifying a list while iterating over it with a for loop, causing skipped or repeated elements.
- Confusing the loop variable (element) with the index.
- Assuming range(n) includes n (it stops at n-1).
