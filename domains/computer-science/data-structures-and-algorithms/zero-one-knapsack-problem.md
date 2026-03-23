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
status: validated
---

# 0/1 Knapsack Problem

## Core Idea
The 0/1 knapsack problem: given items with weights and values, select a subset to maximize value without exceeding weight capacity W. DP solution: dp[i][w] = maximum value using first i items with weight limit w. Recurrence: if weight[i] > w, skip; else dp[i][w] = max(dp[i−1][w], dp[i−1][w−weight[i]] + value[i]). Time: O(n * W), space: O(n * W) or O(W) optimized.

## How It's Best Learned
Trace the DP table on a small instance by hand. Implement and test. Reconstruct selected items by backtracking. See how fractional knapsack has a greedy solution, making 0/1 harder.

## Common Misconceptions
- Greedy approaches work for 0/1 knapsack (they don't; greedy works for fractional knapsack). - Always O(n * W) space (time is always O(n * W); space can be optimized to O(W)).

## Questions

```yaml
- question: "You have a knapsack with capacity 10. Item A weighs 6 and is worth $9. Items B and C each weigh 5 and are each worth $6. A greedy algorithm picks by value-per-weight ratio. What does greedy select, and is this optimal?"
  type: multiple-choice
  options:
    - "Greedy picks A ($9, weight 6) — optimal, since it has the best ratio"
    - "Greedy picks A ($9, weight 6) — suboptimal; picking B and C together gives $12"
    - "Greedy picks B and C ($12, weight 10) — optimal"
    - "Greedy cannot determine an answer without a complete table"
  answer: 1
  explanation: "Item A has value-per-weight of $9/6 = $1.50, higher than B or C at $6/5 = $1.20, so greedy picks A (weight 6, leaving only 4 units unused, insufficient for B or C). Total value: $9. But taking B and C together uses exactly 10 units of capacity for $12 — a clearly better solution. This example demonstrates why greedy fails for 0/1 knapsack: a good local choice (high density item) can block a better combination of less-dense items."

- question: "When reducing the 0/1 knapsack DP from a 2D table to a 1D array, why must you iterate the weight dimension in reverse (from W down to weight[i]) for each item?"
  type: multiple-choice
  options:
    - "Reverse iteration is faster on modern hardware due to cache behavior"
    - "Forward iteration would use updated values from the current item's pass, effectively allowing the same item to be taken multiple times"
    - "Reverse iteration ensures the algorithm considers heavier items before lighter ones"
    - "The choice of direction is arbitrary — both give the same result"
  answer: 1
  explanation: "In the 2D recurrence, dp[i][w] uses dp[i-1][w - weight[i]] — the value from the *previous* row. When flattening to 1D, if you iterate w forward (small to large), you might update dp[w - weight[i]] before processing dp[w], and then when you reach dp[w] and look up dp[w - weight[i]], you get the already-updated (current-item) value — allowing the same item twice, turning this into the unbounded knapsack. Reverse iteration ensures that when you compute dp[w], dp[w - weight[i]] still holds the value from the previous item's pass."

- question: "The 0/1 knapsack problem is NP-hard even though the DP solution runs in O(n × W) time."
  type: true-false
  answer: true
  explanation: "O(n × W) is pseudo-polynomial time — polynomial in the *numeric value* of W, not in the number of bits needed to represent it. If W is large (e.g., W = 2^100), the DP table becomes astronomically large. The input size in bits is proportional to log W, so the algorithm is actually exponential in the input size in the worst case. This is the distinction between pseudo-polynomial and truly polynomial algorithms, and it is why 0/1 knapsack remains NP-hard despite having an 'efficient-looking' DP solution."

- question: "A greedy algorithm that always selects the item with the highest value-per-weight ratio will optimally solve the 0/1 knapsack problem."
  type: true-false
  answer: false
  explanation: "Greedy by value density works for the *fractional* knapsack problem, where you can take partial items. In 0/1 knapsack, items are indivisible. A high-density item might use enough capacity to prevent taking multiple lower-density items that together yield more value. The standard counterexample: a 6-weight, $9-value item beats a 5-weight $6 item by density, but if capacity is 10, greedy takes the single item ($9) while the optimal is the two equal-density items ($12). The 0/1 constraint is precisely what forces a combinatorial DP approach."

- question: "Why is it necessary to backtrack through the completed DP table to determine which items were actually selected, rather than reading the answer directly from the table?"
  type: short-answer
  answer: "The DP table stores only the maximum achievable value at each (item, capacity) combination — it does not record which items produced that value. The final cell dp[n][W] tells you the optimal total value, but not which items contribute to it. To reconstruct the solution, you trace backward: if dp[i][w] ≠ dp[i-1][w], item i must have been included (its value changed the optimum), so you record it and move to dp[i-1][w - weight[i]]; otherwise item i was skipped and you move to dp[i-1][w]. This greedy trace of the optimal-value decisions recovers the item set."
  explanation: "This is a general pattern in DP: tabular DP solves the optimization problem but separates the value from the choice. The table encodes 'what is achievable' without recording 'how it was achieved.' Backtracking reconstructs the path of decisions that led to the optimal value. An alternative is to store a separate 'kept' boolean table during the forward pass, but backtracking through the value table suffices and uses no extra space."
```

## Explainer

From your introduction to dynamic programming, you know the strategy: identify overlapping subproblems, define a recurrence, and build solutions bottom-up in a table. The **0/1 knapsack problem** is the canonical application of this thinking to constrained optimization. Imagine you are packing a backpack with a weight limit W. You have n items, each with a specific weight and value. You want to maximize the total value of items you pack, but you cannot exceed the weight limit, and each item is all-or-nothing — you either take it entirely or leave it behind. The "0/1" in the name refers to this binary choice: zero copies or one copy of each item.

The key insight is that for each item, you face a decision: include it or exclude it. If you include item i, you gain its value but consume its weight, leaving less capacity for remaining items. If you exclude it, your capacity stays the same. The **optimal choice depends on what other items you can still fit** — which is why greedy approaches fail. A greedy algorithm that takes the highest value-per-weight item first can miss combinations where several lighter items together are more valuable. For example, with capacity 10: an item weighing 6 worth $8 looks better per-pound than two items weighing 5 each worth $5, but the two items together give $10 versus $8.

The DP table `dp[i][w]` stores the maximum value achievable using only the first `i` items with weight capacity `w`. For each cell, you compute two options: skip item `i` (taking `dp[i-1][w]`) or include item `i` (taking `dp[i-1][w - weight[i]] + value[i]`, but only if `weight[i] ≤ w`). You take the maximum of these two. The table fills row by row, left to right, and the answer is at `dp[n][W]`. To find out **which items** were actually selected, you backtrack from `dp[n][W]`: if `dp[i][w] ≠ dp[i-1][w]`, item `i` was included, so you record it and move to `dp[i-1][w - weight[i]]`; otherwise item `i` was skipped and you move to `dp[i-1][w]`.

A practical optimization reduces space from O(n × W) to O(W) by using a single one-dimensional array and processing weights in **reverse order** within each item's pass. Since each row only depends on the row above, you can reuse a single row — but you must iterate `w` from W down to `weight[i]` to avoid using an already-updated value from the current row (which would effectively allow taking the same item twice, turning this into the unbounded knapsack problem). This reverse-iteration trick is a signature DP space optimization worth internalizing, as it appears in many tabular DP problems. The 0/1 knapsack's time complexity of O(n × W) is technically **pseudo-polynomial** — polynomial in the numeric value of W, not in the number of bits needed to represent it — which is why the problem remains NP-hard in the general case despite having an efficient-looking DP solution.
