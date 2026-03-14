---
id: memoization-and-tabulation
title: Memoization and Tabulation
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
- id: hash-tables
  type: soft
- id: arrays-and-lists
  type: soft
- id: recurrence-relations
  type: soft
tags:
- memoization
- tabulation
- top-down
- bottom-up
- DP-implementation
stage: formal-systems
status: validated
---

# Memoization and Tabulation

## Core Idea
Memoization (top-down DP) augments a recursive solution with a cache so each subproblem is solved only once; it is natural to implement but uses the call stack. Tabulation (bottom-up DP) fills a table iteratively from base cases, avoiding recursion entirely. Both achieve the same asymptotic complexity but differ in which subproblems are computed — memoization computes only subproblems needed for the query, while tabulation computes all subproblems in a fixed order. Tabulation also enables space optimizations by discarding rows of the DP table that are no longer needed.

## How It's Best Learned
Implement both approaches for the same 2-3 canonical problems: Fibonacci, coin change, and longest common subsequence. Verify identical results and compare space usage. Then optimize the tabulation version to use O(n) space instead of O(n²) for LCS.

## Common Misconceptions
- Memoization does not change the recursion structure; if the recursion is wrong, caching it will not fix correctness.
- Bottom-up tabulation often allows significant space optimization (e.g., reducing a 2D DP table to two 1D arrays) that is harder to apply to memoization.
