---
id: for-loop-patterns-and-iteration
title: For-Loop Patterns and Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loops
  type: hard
- id: variables-and-assignment
  type: hard
builds-toward:
- loop-design-and-invariants
- nested-loops-and-deep-iteration
tags:
- loops
- iteration
- control-flow
stage: abstract-reasoning
status: draft
---

# For-Loop Patterns and Iteration

## Core Idea
For loops iterate a fixed number of times, controlled by an index variable that changes each iteration. Common patterns: counting up (i = 0 to n), counting down, iterating over collections. Understanding the loop variable and termination condition is key.

## How It's Best Learned
Trace loop execution by hand, tracking the index variable each iteration; experiment with off-by-one errors (start at 0 vs 1, iterate while i < n vs i <= n).

## Common Misconceptions
That the loop variable persists after the loop (scope varies by language); that the loop index must be an integer; that i = i + 1 inside the loop conflicts with i++ in the loop header.

## Explainer

You already know how for loops work mechanically — a loop variable is initialized, a condition is checked before each iteration, and the variable is updated after each iteration. Now the question is: what can you *do* with this structure? **For-loop patterns** are the reusable recipes that show up again and again in programming, and recognizing them is the key to writing loops confidently instead of reinventing them each time.

The most basic pattern is **counting**, where you iterate from a start value to an end value. `for i in range(5)` in Python or `for (int i = 0; i < 5; i++)` in C/Java counts from 0 to 4. This pattern shows up whenever you need to do something a known number of times — print 10 stars, process 100 records, repeat an experiment 1000 times. A variant is **counting down**: `for i in range(10, 0, -1)` counts from 10 to 1. Counting down is useful for countdowns, reverse traversal, or any situation where you need to work backward through a sequence.

The **accumulation** pattern uses a loop to build up a result across iterations. You initialize a variable before the loop (like `total = 0` or `result = ""`), then update it inside the loop body (`total += numbers[i]` or `result += char`). Summation, product, counting matches, and string building all follow this template. The closely related **search** pattern scans through data looking for a specific condition: iterate through elements, and when you find what you are looking for, record it and (often) break out of the loop early.

The **collection iteration** pattern walks through every element of a list, array, or other data structure. In Python, `for item in my_list` directly gives you each element; in C-style languages, you use an index: `for (int i = 0; i < length; i++)` and access `array[i]`. A critical detail in all for-loop patterns is the **off-by-one error** — starting at 1 when you should start at 0, or using `<=` when you should use `<`. The best defense is to trace your loop by hand for small inputs: write down the value of the loop variable and any accumulators at each iteration, and verify that the first iteration, last iteration, and total count are all correct. This hand-tracing habit will save you more debugging time than any other single practice.
