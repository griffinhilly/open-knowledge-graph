---
id: nested-loops
title: Nested Loops and Multi-Level Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loop-iteration
  type: hard
- id: while-loop-iteration
  type: hard
tags:
- loops
- nesting
- iteration
stage: abstract-reasoning
status: draft
---

# Nested Loops and Multi-Level Iteration

## Core Idea
A nested loop contains another loop inside it. The inner loop completes fully for each iteration of the outer loop. Nested loops process multi-dimensional data, such as matrices or generating all combinations.

## How It's Best Learned
Trace nested loop execution by hand. Print a multiplication table or pattern to see nesting in action.

## Common Misconceptions
- The total iterations equals outer × inner (this is true for independent loops; be aware of early exits via break).
- Nested loops are always inefficient (they're appropriate for their use cases, but quadratic complexity can be problematic for large inputs).
