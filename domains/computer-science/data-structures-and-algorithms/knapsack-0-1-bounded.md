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

## Explainer

You already know from your introduction to dynamic programming that DP works by breaking a problem into overlapping subproblems and combining their solutions. The 0/1 knapsack problem is one of the clearest demonstrations of why this strategy is necessary. You have a bag that can carry at most W units of weight, and a set of n items, each with a specific weight and value. Your goal is to pick the combination of items that maximizes total value without exceeding the capacity. The "0/1" constraint means each item is either taken whole or left behind — no splitting allowed.

The greedy instinct is to grab items with the best value-to-weight ratio first. But this fails for the 0/1 case. Consider a knapsack with capacity 10, and three items: one weighing 6 with value 8, one weighing 5 with value 5, and one weighing 5 with value 5. The greedy approach takes the first item (best ratio) for a total value of 8, but taking the two smaller items yields 10. The discrete all-or-nothing choice creates interactions between items that greedy strategies cannot account for.

The DP solution builds a two-dimensional table **dp[i][w]**, where each cell stores the maximum value achievable using the first i items with a capacity limit of w. The key recurrence considers each item in turn: either you skip item i (inheriting dp[i-1][w]) or you include it (adding its value to dp[i-1][w - weight_i], provided it fits). You take whichever option gives a higher value. The base cases are straightforward — with zero items or zero capacity, the maximum value is zero. By filling the table row by row, you systematically evaluate every relevant combination without redundant work.

Once the table is complete, dp[n][W] holds your answer, but you can also **reconstruct the solution** by tracing backward. Starting at dp[n][W], if dp[i][w] differs from dp[i-1][w], item i was included — record it and move to dp[i-1][w - weight_i]. Otherwise item i was skipped, and you move to dp[i-1][w]. This backtracking recovers the exact set of chosen items. A practical optimization reduces space from O(nW) to O(W) by maintaining only a single one-dimensional array and iterating weights in reverse order, since each row depends only on the previous row. The reverse iteration ensures you don't accidentally use an updated value from the current row when you still need the old one.
