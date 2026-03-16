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

## Explainer

From your introduction to dynamic programming, you know the strategy: identify overlapping subproblems, define a recurrence, and build solutions bottom-up in a table. The **0/1 knapsack problem** is the canonical application of this thinking to constrained optimization. Imagine you are packing a backpack with a weight limit W. You have n items, each with a specific weight and value. You want to maximize the total value of items you pack, but you cannot exceed the weight limit, and each item is all-or-nothing — you either take it entirely or leave it behind. The "0/1" in the name refers to this binary choice: zero copies or one copy of each item.

The key insight is that for each item, you face a decision: include it or exclude it. If you include item i, you gain its value but consume its weight, leaving less capacity for remaining items. If you exclude it, your capacity stays the same. The **optimal choice depends on what other items you can still fit** — which is why greedy approaches fail. A greedy algorithm that takes the highest value-per-weight item first can miss combinations where several lighter items together are more valuable. For example, with capacity 10: an item weighing 6 worth $8 looks better per-pound than two items weighing 5 each worth $5, but the two items together give $10 versus $8.

The DP table `dp[i][w]` stores the maximum value achievable using only the first `i` items with weight capacity `w`. For each cell, you compute two options: skip item `i` (taking `dp[i-1][w]`) or include item `i` (taking `dp[i-1][w - weight[i]] + value[i]`, but only if `weight[i] ≤ w`). You take the maximum of these two. The table fills row by row, left to right, and the answer is at `dp[n][W]`. To find out **which items** were actually selected, you backtrack from `dp[n][W]`: if `dp[i][w] ≠ dp[i-1][w]`, item `i` was included, so you record it and move to `dp[i-1][w - weight[i]]`; otherwise item `i` was skipped and you move to `dp[i-1][w]`.

A practical optimization reduces space from O(n × W) to O(W) by using a single one-dimensional array and processing weights in **reverse order** within each item's pass. Since each row only depends on the row above, you can reuse a single row — but you must iterate `w` from W down to `weight[i]` to avoid using an already-updated value from the current row (which would effectively allow taking the same item twice, turning this into the unbounded knapsack problem). This reverse-iteration trick is a signature DP space optimization worth internalizing, as it appears in many tabular DP problems. The 0/1 knapsack's time complexity of O(n × W) is technically **pseudo-polynomial** — polynomial in the numeric value of W, not in the number of bits needed to represent it — which is why the problem remains NP-hard in the general case despite having an efficient-looking DP solution.
