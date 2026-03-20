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

## Questions

```yaml
- question: "A programmer writes `for (i = 1; i <= 5; i++)`. How many times does the loop body execute?"
  type: multiple-choice
  options:
    - "4"
    - "5"
    - "6"
    - "It depends on the loop body"
  answer: 1
  explanation: "The loop runs for i = 1, 2, 3, 4, and 5 — five iterations. The condition `i <= 5` includes 5, so the loop continues while i is 1 through 5, then stops when i becomes 6 (where `6 <= 5` is false). Students often confuse this with `i < 5` (which would give only 4 iterations: i = 1, 2, 3, 4) or expect 6 iterations because they start counting from 1 and include the boundary."

- question: "A programmer wants to access every element in a 10-element array with indices 0 through 9. Which loop is correct?"
  type: multiple-choice
  options:
    - "`for (i = 1; i <= 10; i++)`"
    - "`for (i = 0; i < 10; i++)`"
    - "`for (i = 0; i <= 10; i++)`"
    - "`for (i = 1; i < 10; i++)`"
  answer: 1
  explanation: "Arrays are 0-indexed: the first element is at index 0 and the last at index 9. The correct loop starts at 0 and uses `i < 10` (stops when i reaches 10, never executing the body with i = 10). Option 0 misses index 0 and wrongly accesses index 10 (out of bounds). Option 2 tries to access index 10, which is out of bounds. Option 3 misses index 0 and stops at index 8, processing only 9 of 10 elements."

- question: "In a for loop written as `for (i = 0; i < 5; i++)`, the variable `i` takes on the values 0, 1, 2, 3, 4, and 5 during execution."
  type: true-false
  answer: false
  explanation: "The loop body runs with i equal to 0, 1, 2, 3, and 4. When i reaches 5, the condition `5 < 5` is false, and the loop terminates before executing the body. The value 5 is computed by the update step (after i = 4), but the condition is checked immediately — and the body never runs with i = 5. This is the crucial off-by-one insight: the condition determines whether the body executes, not whether the counter was incremented to that value."

- question: "For loops are best used when the number of iterations is not known until the program runs."
  type: true-false
  answer: false
  explanation: "For loops are designed for situations where the number of iterations is known beforehand — a fixed count, the length of a collection, or a defined range. When the number of iterations depends on a condition that could be satisfied at any unpredictable point, a while loop is more appropriate. The for loop's structured header (init; condition; update) is optimized for counting a known range; using it for open-ended termination conditions produces confusing code."

- question: "What is an off-by-one error in a for loop, and what is the most common cause?"
  type: short-answer
  answer: "An off-by-one error is when a loop runs one too many or one too few times — iterating with i = 0 through 5 when 0 through 4 was intended, for example. It is almost always caused by using `<=` instead of `<` (or vice versa) in the loop condition. The fix is to reason about the boundary explicitly: 'When i equals the boundary value, should the loop body still execute?' If the answer is no, use strict inequality (`<`); if yes, use `<=`."
  explanation: "Off-by-one errors are among the most common bugs in programming. The mental model that prevents them is asking: 'What happens on the last iteration?' For an array of length n with 0-based indexing, the last valid index is n-1, so `i < n` is correct and `i <= n` would attempt an out-of-bounds access. Substituting the boundary value into the condition and asking 'should this run?' is the most reliable check."
```

## Explainer

Programs often need to repeat an action multiple times: print ten lines, process every student's grade, or draw a hundred pixels. You could write the same statement ten times, but this is tedious, error-prone, and impossible when the count is not known until the program runs. A **for loop** automates repetition by specifying three things in its header: where to start, when to stop, and how to step forward.

The classic for loop has the structure `for (init; condition; update)`. The **init** step runs once before the loop begins — typically declaring and setting an index variable like `i = 0`. The **condition** is checked before each iteration — if it is true, the loop body executes; if false, the loop ends. The **update** runs after each iteration — usually incrementing the index with `i = i + 1` or `i++`. So `for (i = 0; i < 5; i++)` means: start `i` at 0, keep going while `i` is less than 5, and add 1 to `i` after each pass. The body executes with `i` equal to 0, 1, 2, 3, and 4 — five iterations total.

The most common mistake with for loops is the **off-by-one error**: iterating one time too many or one time too few. This almost always comes from confusing `<` with `<=` in the condition. If you want to iterate 5 times starting from 0, the condition is `i < 5` (which stops when `i` reaches 5) — not `i <= 5` (which would give you six iterations: 0 through 5). A reliable mental check is to substitute the boundary value: when `i` equals 5, should the loop still run? If you want indices 0 through 4, the answer is no, so the condition should exclude 5.

For loops are especially natural when working with collections. To process every element of an array with 10 elements, you write `for (i = 0; i < 10; i++)` and access `array[i]` inside the body. The index variable serves double duty: it counts iterations and also serves as the position for looking up each element. Many modern languages offer a shorthand — the **for-each** loop — that iterates directly over elements without managing an index at all: `for (item in collection)`. But understanding the indexed for loop is essential, because it gives you explicit control over the start point, end point, step size, and current position, which you will need for tasks like iterating backward, skipping every other element, or processing only part of a collection.
