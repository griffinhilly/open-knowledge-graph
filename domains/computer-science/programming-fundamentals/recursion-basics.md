---
id: recursion-basics
title: Recursion Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: return-values
  type: hard
- id: variable-scope
  type: hard
- id: while-loops
  type: soft
builds-toward:
- algorithm-design-basics
tags:
- recursion
- base case
- call stack
- self-reference
- induction
stage: abstract-reasoning
status: draft
---

# Recursion Basics

## Core Idea
A recursive function is one that calls itself as part of its own definition. Every recursive solution requires a base case (a condition that terminates the recursion) and a recursive case (a call on a smaller or simpler version of the problem). Each function call creates a new stack frame with its own local variables; the call stack grows with each recursive call and shrinks as calls return. Many problems — especially those with naturally recursive structure like trees or mathematical sequences — are elegantly expressed recursively.

## How It's Best Learned
Start with factorial and Fibonacci, tracing the call tree by hand. Then implement recursive sum of a list, string reversal, and binary search. Always identify the base case first before writing the recursive case.

## Common Misconceptions
- Forgetting the base case, causing infinite recursion (stack overflow).
- Not returning the result of the recursive call, so the result is lost.
- Thinking recursion is always more efficient than iteration — it often uses more memory due to stack frames.
