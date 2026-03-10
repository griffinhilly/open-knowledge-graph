---
id: dynamic-programming-intro
title: Dynamic Programming
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: algorithm-design-basics
  type: hard
- id: time-space-complexity
  type: hard
- id: recurrence-relations
  type: soft
builds-toward:
- memoization-and-tabulation
tags:
- dynamic-programming
- DP
- optimal-substructure
- overlapping-subproblems
stage: formal-systems
status: draft
---

# Dynamic Programming

## Core Idea
Dynamic programming (DP) solves optimization and counting problems by breaking them into overlapping subproblems and storing solutions to avoid redundant computation. Two key properties must hold: optimal substructure (the optimal solution contains optimal solutions to subproblems) and overlapping subproblems (the same subproblems recur many times). Classic examples include Fibonacci, 0/1 knapsack, longest common subsequence, and coin change. DP transforms exponential naive recursion into polynomial time by caching intermediate results.

## How It's Best Learned
Start with memoized Fibonacci to see the speedup from caching in isolation. Then tackle structured DP problems: coin change, longest common subsequence, 0/1 knapsack. For each, explicitly define the subproblem before writing any code.

## Common Misconceptions
- DP is not just about filling a table; the hardest part is correctly defining the subproblem and its recurrence.
- Not every recursive problem has overlapping subproblems; divide-and-conquer (merge sort) uses recursion but is not DP because its subproblems are independent.
- Bottom-up tabulation and top-down memoization are equivalent in correctness but differ in stack usage and which subproblems are computed.
