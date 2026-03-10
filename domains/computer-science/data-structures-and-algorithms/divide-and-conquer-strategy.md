---
id: divide-and-conquer-strategy
title: Divide and Conquer
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: time-space-complexity
  type: hard
- id: divide-and-conquer-recurrences
  type: soft
- id: recurrence-relations
  type: soft
builds-toward:
- merge-sort
- quicksort
tags:
- divide-and-conquer
- recursion
- algorithm-design
- master-theorem
stage: formal-systems
status: draft
---

# Divide and Conquer

## Core Idea
Divide and conquer solves problems by recursively splitting them into smaller subproblems of the same type, solving each independently, and combining results. The paradigm has three phases: divide (split the problem), conquer (solve recursively), and combine (merge results). The Master Theorem provides a closed-form solution for recurrences of the form T(n) = aT(n/b) + f(n), covering most divide-and-conquer algorithms. Classic applications include merge sort, quicksort, and Strassen's matrix multiplication.

## How It's Best Learned
Use merge sort as the canonical example. Explicitly draw the recursion tree for small inputs and verify that the work at each level sums to the predicted total. Practice applying the Master Theorem to derive complexity from recurrences.

## Common Misconceptions
- The combine step is often where most of the work happens (as in merge sort) — it is not always trivial.
- Not all recursive algorithms are divide and conquer; dynamic programming also uses recursion but focuses on overlapping subproblems rather than independent ones.
