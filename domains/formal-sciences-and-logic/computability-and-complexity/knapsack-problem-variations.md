---
id: knapsack-problem-variations
title: Knapsack Problem and Pseudo-Polynomial Time
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
builds-toward:
- fixed-parameter-tractability
tags:
- np-hard
- optimization
- dynamic-programming
stage: advanced
status: draft
---

# Knapsack Problem and Pseudo-Polynomial Time

## Core Idea
The 0/1 knapsack problem is NP-hard in the strong sense, but admits a pseudo-polynomial time algorithm using dynamic programming. This algorithm runs in time O(nW) where W is the knapsack capacity. Pseudo-polynomial algorithms are tractable when input values are small but become exponential if values are encoded in binary, illustrating the distinction between weak and strong NP-hardness.

## How It's Best Learned
Implement the DP solution O(nW) and observe that it depends on the value W, not the bit-length of W. Try the same problem with exponentially large weights to see where the algorithm breaks down.

## Common Misconceptions
- Pseudo-polynomial algorithms solve NP-hard problems (they only work when weights are bounded).
- If W is polynomial in n, the algorithm is polynomial time (it is, but this requires W = poly(n) which is not guaranteed).
