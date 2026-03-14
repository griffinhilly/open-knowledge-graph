---
id: nested-loops
title: Nested Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loops
  type: hard
- id: arrays-and-lists
  type: soft
- id: loop-control-statements
  type: soft
builds-toward:
- algorithm-design-basics
- list-comprehensions
tags:
- nested loops
- 2D data
- matrix traversal
- combinatorics
- iteration
stage: abstract-reasoning
status: validated
---

# Nested Loops

## Core Idea
A nested loop is a loop placed inside the body of another loop. For each iteration of the outer loop, the inner loop runs to completion. This pattern is used to process two-dimensional data (matrices, grids), generate all pairs from two sequences, or implement algorithms that compare every element with every other element. Nested loops have multiplicative time complexity: if the outer runs m times and the inner n times, the body executes m × n times.

## How It's Best Learned
Trace nested loops on paper for small inputs, writing out the values of both loop variables at each step. Implement multiplication tables, matrix printing, and all-pairs comparisons.

## Common Misconceptions
- Confusing which loop variable belongs to which loop in deeply nested code.
- Forgetting that break only exits the innermost loop.
- Underestimating how quickly nested loop complexity grows with input size.
