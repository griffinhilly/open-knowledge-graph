---
id: while-loops
title: While Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: conditional-statements
  type: hard
- id: boolean-logic-programming
  type: soft
builds-toward:
- for-loops
- loop-control-statements
- recursion-basics
tags:
- while
- iteration
- loops
- control flow
- termination
stage: abstract-reasoning
status: draft
---

# While Loops

## Core Idea
A while loop repeatedly executes a block of code as long as its condition remains true. Before each iteration the condition is evaluated; when it becomes false the loop exits and execution continues after the loop body. The loop body must eventually cause the condition to become false, or the loop runs forever (an infinite loop). While loops are best used when the number of iterations is not known in advance.

## How It's Best Learned
Trace loops by hand, updating a variable table after each iteration. Deliberately create an infinite loop, observe the behavior, and fix it. Implement classic examples: countdown, sum of digits, user input validation.

## Common Misconceptions
- Forgetting to update the loop variable inside the body, causing an infinite loop.
- Off-by-one errors in the condition (< vs <=).
- Assuming the condition is checked continuously rather than only at the top of each iteration.
