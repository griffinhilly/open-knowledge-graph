---
id: algorithm-complexity
title: Algorithm Analysis and Complexity Classes
domain: mathematics
course: discrete-math
prerequisites:
- id: big-o-notation
  type: hard
- id: recurrence-relations
  type: soft
builds-toward:
- divide-and-conquer-recurrences
tags:
- algorithm-analysis
- time-complexity
- P-vs-NP
- NP-complete
- sorting-algorithms
stage: formal-systems
status: draft
---

# Algorithm Analysis and Complexity Classes

## Core Idea
Algorithm analysis applies Big-O notation to classify algorithms by their time and space requirements as functions of input size n. Linear search is O(n); binary search is O(log n); comparison-based sorting is Ω(n log n), achieved by merge sort and heap sort. The complexity classes P (problems solvable in polynomial time) and NP (problems whose solutions are verifiable in polynomial time) frame the central open question of theoretical computer science: whether P = NP. NP-complete problems — the hardest problems in NP — include SAT, graph coloring, and Hamiltonian circuits.

## How It's Best Learned
Analyze familiar algorithms step by step, deriving their complexity by counting operations as a function of n. Understand binary search's O(log n) cost from the halving argument. Discuss P vs. NP conceptually: why verifying a solution is often easier than finding one.

## Common Misconceptions
- Thinking O(n²) is always worse than O(n log n) for all n — for small inputs, constants dominate.
- Confusing the complexity of an algorithm with the complexity of a problem (the problem's complexity is the minimum over all correct algorithms).
- Believing NP stands for 'not polynomial' — NP means solutions are verifiable in polynomial time.
