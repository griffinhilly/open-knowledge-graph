---
id: zero-one-knapsack-problem
title: 0/1 Knapsack Problem
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
tags:
- dynamic-programming
- knapsack
- optimization
- combinatorial
- resource-allocation
stage: formal-systems
status: draft
---

# 0/1 Knapsack Problem

## Core Idea
The 0/1 knapsack problem: given items with weights and values, select a subset to maximize value without exceeding weight capacity W. DP solution: dp[i][w] = maximum value using first i items with weight limit w. Recurrence: if weight[i] > w, skip; else dp[i][w] = max(dp[i−1][w], dp[i−1][w−weight[i]] + value[i]). Time: O(n * W), space: O(n * W) or O(W) optimized.

## How It's Best Learned
Trace the DP table on a small instance by hand. Implement and test. Reconstruct selected items by backtracking. See how fractional knapsack has a greedy solution, making 0/1 harder.

## Common Misconceptions
- Greedy approaches work for 0/1 knapsack (they don't; greedy works for fractional knapsack). - Always O(n * W) space (time is always O(n * W); space can be optimized to O(W)).
