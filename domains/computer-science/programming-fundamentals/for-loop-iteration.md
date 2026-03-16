---
id: for-loop-iteration
title: For Loops and Indexed Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: program-structure-and-flow
  type: hard
builds-toward:
- loop-control-statements
- nested-loops
tags:
- loops
- iteration
- for
stage: abstract-reasoning
status: draft
---

# For Loops and Indexed Iteration

## Core Idea
A for loop repeats a block of code a known number of times, typically using an index variable. The loop header (init; condition; update) controls iteration count. For loops are ideal when the number of iterations is known beforehand.

## How It's Best Learned
Write for loops with various iteration counts. Trace the index variable's changes. Use for loops to process fixed-size collections.

## Common Misconceptions
- The loop variable's scope extends beyond the loop (in many languages, it's scoped to the loop).
- Off-by-one errors are unavoidable (careful initialization and condition checking prevent them).

## Explainer

Programs often need to repeat an action multiple times: print ten lines, process every student's grade, or draw a hundred pixels. You could write the same statement ten times, but this is tedious, error-prone, and impossible when the count is not known until the program runs. A **for loop** automates repetition by specifying three things in its header: where to start, when to stop, and how to step forward.

The classic for loop has the structure `for (init; condition; update)`. The **init** step runs once before the loop begins — typically declaring and setting an index variable like `i = 0`. The **condition** is checked before each iteration — if it is true, the loop body executes; if false, the loop ends. The **update** runs after each iteration — usually incrementing the index with `i = i + 1` or `i++`. So `for (i = 0; i < 5; i++)` means: start `i` at 0, keep going while `i` is less than 5, and add 1 to `i` after each pass. The body executes with `i` equal to 0, 1, 2, 3, and 4 — five iterations total.

The most common mistake with for loops is the **off-by-one error**: iterating one time too many or one time too few. This almost always comes from confusing `<` with `<=` in the condition. If you want to iterate 5 times starting from 0, the condition is `i < 5` (which stops when `i` reaches 5) — not `i <= 5` (which would give you six iterations: 0 through 5). A reliable mental check is to substitute the boundary value: when `i` equals 5, should the loop still run? If you want indices 0 through 4, the answer is no, so the condition should exclude 5.

For loops are especially natural when working with collections. To process every element of an array with 10 elements, you write `for (i = 0; i < 10; i++)` and access `array[i]` inside the body. The index variable serves double duty: it counts iterations and also serves as the position for looking up each element. Many modern languages offer a shorthand — the **for-each** loop — that iterates directly over elements without managing an index at all: `for (item in collection)`. But understanding the indexed for loop is essential, because it gives you explicit control over the start point, end point, step size, and current position, which you will need for tasks like iterating backward, skipping every other element, or processing only part of a collection.
