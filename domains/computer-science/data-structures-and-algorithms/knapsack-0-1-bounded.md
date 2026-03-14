---
id: knapsack-0-1-bounded
title: '0/1 Knapsack Problem: Bounded Capacity DP'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
tags:
- dynamic-programming
- optimization
- greedy
stage: formal-systems
status: draft
---

# 0/1 Knapsack Problem: Bounded Capacity DP

## Core Idea
The 0/1 knapsack problem: given items with weights and values, select items maximizing total value subject to a weight capacity. DP solves it in O(nW) time and space via dp[i][w] = maximum value using items 0..i-1 with capacity w. Unlike the fractional variant, you cannot take partial items.

## How It's Best Learned
Implement the DP table and trace on a small example. Reconstruct the selected items by backtracking. Compare to the fractional knapsack (greedy) to see why DP is necessary.

## Common Misconceptions
- Assuming a greedy approach (highest value/weight ratio) is optimal; counterexample: one high-value item beats multiple small ones.
- Not optimizing space; the table can be reduced to O(W) using a 1D array and reverse iteration.
- Forgetting that O(nW) is pseudopolynomial; if W is very large, this is infeasible.
