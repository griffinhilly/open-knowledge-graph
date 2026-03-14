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
