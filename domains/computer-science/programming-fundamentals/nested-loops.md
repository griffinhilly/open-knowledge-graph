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

## Explainer

You know how a `for` loop repeats a block of code for each item in a sequence, and how a `while` loop repeats as long as a condition is true. A **nested loop** is simply a loop placed inside another loop. The key behavior to internalize is this: for each single iteration of the **outer loop**, the **inner loop** runs completely from start to finish. This is like the hour and minute hands on a clock — the minute hand (inner loop) completes a full 60-minute rotation for every single tick of the hour hand (outer loop).

The classic example is a **multiplication table**. To print a 10×10 table, the outer loop iterates over rows (1 through 10) and the inner loop iterates over columns (1 through 10). For row 1, the inner loop prints 1×1, 1×2, ... 1×10. Then the outer loop advances to row 2, and the inner loop runs again: 2×1, 2×2, ... 2×10. The total number of print operations is 10 × 10 = 100. In general, if the outer loop runs *n* times and the inner loop runs *m* times, the body of the inner loop executes *n × m* times. This multiplicative relationship is what makes nested loops powerful for processing two-dimensional data — and what makes them potentially expensive for large inputs.

Nested loops are the natural tool for working with **grids, matrices, and combinations**. To process every cell in a 2D grid, the outer loop walks through rows and the inner loop walks through columns — each (row, column) pair is visited exactly once. To find all pairs of items in a list (for example, checking if any two numbers sum to a target), the outer loop picks the first number and the inner loop tries every possible second number. To generate all combinations of sizes and colors for a product catalog, the outer loop iterates over sizes and the inner loop iterates over colors. In each case, the nested structure naturally generates every combination of the outer and inner values.

The most important skill is being able to **trace execution by hand**. Write out the values of both loop variables at each step. For a loop like `for i in range(3): for j in range(2): print(i, j)`, the output is: (0,0), (0,1), (1,0), (1,1), (2,0), (2,1). Notice that `j` resets to 0 every time `i` advances — the inner loop starts fresh each time. This reset behavior is essential to understand, and tracing a few examples on paper will make nested loops feel intuitive rather than mysterious. Once you can predict the output of a nested loop by reading the code, you're ready for more complex iteration patterns like nested loops with conditionals, early exits using `break`, and eventually multi-dimensional data structures.
