---
id: recursion-and-recursive-calls
title: Recursion and Recursive Function Calls
domain: computer-science
course: programming-fundamentals
prerequisites:
- call-stack-and-function-calls
tags:
- functions
- recursion
stage: abstract-reasoning
status: draft
---

# Recursion and Recursive Function Calls

## Core Idea
A recursive function calls itself, either directly or indirectly. Recursion requires a base case (to stop) and a recursive case (that makes progress toward the base case). Recursion naturally expresses problems with self-similar structure, like tree traversal or factorial.

## How It's Best Learned
Implement classic recursive functions (factorial, fibonacci). Trace execution by hand to see how recursion unfolds and returns.

## Common Misconceptions
- Recursion is always more efficient than iteration (recursion can have higher overhead; use it for clarity, not performance).
- Without a base case, recursion infinitely recurses (without a proper base case, the function will overflow the stack).
