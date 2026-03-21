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

## Questions

```yaml
- question: "Consider this nested loop: for i in range(3), and inside it for j in range(2), printing (i, j) each iteration. How many lines of output does this produce, and what is the last line printed?"
  type: multiple-choice
  options:
    - "3 lines; last line is (2, 2)"
    - "5 lines; last line is (2, 1)"
    - "6 lines; last line is (2, 1)"
    - "6 lines; last line is (3, 2)"
  answer: 2
  explanation: "The outer loop runs 3 times (i = 0, 1, 2). For each value of i, the inner loop runs completely through j = 0 and j = 1 — that is 2 iterations. Total = 3 × 2 = 6 lines. The last pair is when i = 2 (last outer iteration) and j = 1 (last inner iteration). Option D is wrong because range(3) stops at 2, not 3."

- question: "A nested loop has an outer loop that runs 5 times and an inner loop that runs 4 times. How many times does the body of the inner loop execute in total?"
  type: multiple-choice
  options:
    - "9 times (5 + 4)"
    - "20 times (5 × 4)"
    - "16 times (4 squared)"
    - "It depends on the specific loop conditions at runtime"
  answer: 1
  explanation: "For each of the 5 outer iterations, the inner loop completes all 4 of its iterations. The total is 5 × 4 = 20. The additive answer (9) is a common misconception — addition would apply if the loops ran sequentially (first one, then the other), not nested. Nesting creates multiplication because every inner iteration is repeated for every outer iteration."

- question: "In a nested loop, the inner loop's counter variable retains its final value from the previous outer iteration when the outer loop advances to the next iteration."
  type: true-false
  answer: false
  explanation: "The inner loop resets to its starting value each time the outer loop advances. The inner loop is a complete, fresh execution each time the outer loop body runs. For example, with `for i in range(3): for j in range(2)`, j always starts at 0 when a new value of i begins — it does not carry over. This reset behavior is essential to understand when tracing execution."

- question: "Nested loops are the natural structure for generating every combination of items from two independent sets."
  type: true-false
  answer: true
  explanation: "Because the inner loop runs completely for each outer iteration, every (outer value, inner value) pair is visited exactly once — the full Cartesian product of the two sets. Generating all size-color combinations, visiting every cell in a grid, or checking all pairs of numbers in a list all require this structure."

- question: "Why does the body of the inner loop execute outer × inner times rather than outer + inner times?"
  type: short-answer
  answer: "Because for each single iteration of the outer loop, the entire inner loop runs from start to finish. The outer loop does not advance until the inner loop completes all its iterations. This means every inner iteration is paired with every outer iteration — a multiplicative relationship, not an additive one. Analogy: a clock's minute hand completes 60 rotations for every 1 rotation of the hour hand, giving 60 × 1 total minute-hand positions per hour-hand position."
  explanation: "Addition would apply if the loops were sequential — first loop A runs n times, then loop B runs m times, for n + m total. Nesting creates multiplication because every step of A triggers a complete run of B. This multiplicative structure is also why nested loops can become computationally expensive: two loops of length n produce O(n²) operations, three loops produce O(n³), and so on."
```

## Explainer

You know how a `for` loop repeats a block of code for each item in a sequence, and how a `while` loop repeats as long as a condition is true. A **nested loop** is simply a loop placed inside another loop. The key behavior to internalize is this: for each single iteration of the **outer loop**, the **inner loop** runs completely from start to finish. This is like the hour and minute hands on a clock — the minute hand (inner loop) completes a full 60-minute rotation for every single tick of the hour hand (outer loop).

The classic example is a **multiplication table**. To print a 10×10 table, the outer loop iterates over rows (1 through 10) and the inner loop iterates over columns (1 through 10). For row 1, the inner loop prints 1×1, 1×2, ... 1×10. Then the outer loop advances to row 2, and the inner loop runs again: 2×1, 2×2, ... 2×10. The total number of print operations is 10 × 10 = 100. In general, if the outer loop runs *n* times and the inner loop runs *m* times, the body of the inner loop executes *n × m* times. This multiplicative relationship is what makes nested loops powerful for processing two-dimensional data — and what makes them potentially expensive for large inputs.

Nested loops are the natural tool for working with **grids, matrices, and combinations**. To process every cell in a 2D grid, the outer loop walks through rows and the inner loop walks through columns — each (row, column) pair is visited exactly once. To find all pairs of items in a list (for example, checking if any two numbers sum to a target), the outer loop picks the first number and the inner loop tries every possible second number. To generate all combinations of sizes and colors for a product catalog, the outer loop iterates over sizes and the inner loop iterates over colors. In each case, the nested structure naturally generates every combination of the outer and inner values.

The most important skill is being able to **trace execution by hand**. Write out the values of both loop variables at each step. For a loop like `for i in range(3): for j in range(2): print(i, j)`, the output is: (0,0), (0,1), (1,0), (1,1), (2,0), (2,1). Notice that `j` resets to 0 every time `i` advances — the inner loop starts fresh each time. This reset behavior is essential to understand, and tracing a few examples on paper will make nested loops feel intuitive rather than mysterious. Once you can predict the output of a nested loop by reading the code, you're ready for more complex iteration patterns like nested loops with conditionals, early exits using `break`, and eventually multi-dimensional data structures.
