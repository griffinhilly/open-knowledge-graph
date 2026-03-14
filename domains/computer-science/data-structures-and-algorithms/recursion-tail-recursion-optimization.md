---
id: recursion-tail-recursion-optimization
title: Recursion and Tail-Recursion Optimization
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
builds-toward:
- backtracking-constraint-satisfaction-problems
- solving-recurrence-relations-master-theorem
tags:
- recursion
- tail-call
- optimization
stage: formal-systems
status: draft
---

# Recursion and Tail-Recursion Optimization

## Core Idea
Recursion breaks a problem into smaller instances of itself. Tail recursion occurs when the recursive call is the last operation; some compilers optimize it to iteration, avoiding stack overhead. Understanding when to use recursion vs. iteration, and how to structure recursive calls, is fundamental to algorithm design.

## How It's Best Learned
Implement classic recursive algorithms: factorial, fibonacci, tree traversal. Trace the call stack by hand to see growth. Compare recursive and iterative versions of the same function. Experiment with tail-recursive functions and observe stack usage in a language with tail-call optimization (Scheme, some functional languages).

## Common Misconceptions
- Recursion is always slower than iteration—not true if the compiler applies tail-call optimization.
- Every recursive function can be easily rewritten as iteration—true, but not always readable or natural.
- Stack overflow is inevitable for deep recursion—not if the language supports tail calls.
