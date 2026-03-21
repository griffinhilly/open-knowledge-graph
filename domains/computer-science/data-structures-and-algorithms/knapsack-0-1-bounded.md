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

## Questions

```yaml
- question: "A knapsack has capacity 10. Three items are available: Item A (weight=6, value=8), Item B (weight=5, value=5), Item C (weight=5, value=5). A greedy algorithm selects items by highest value-to-weight ratio first. What does the greedy algorithm choose, and what is the optimal selection?"
  type: multiple-choice
  options:
    - "Greedy: Item A (value=8); Optimal: Items B and C (value=10)"
    - "Greedy: Items B and C (value=10); Optimal: Item A (value=8)"
    - "Greedy: Item A (value=8); Optimal: Item A (value=8)"
    - "Greedy: Items B and C (value=10); Optimal: Items B and C (value=10)"
  answer: 0
  explanation: "Item A's value-to-weight ratio is 8/6 ≈ 1.33, higher than B or C (1.0 each), so greedy selects A first (total value 8, weight 6). With 4 units of capacity remaining, neither B nor C fits. But selecting B and C uses exactly 10 units of capacity and yields value 10, which is better. This is the core failure of greedy for 0/1 knapsack: the all-or-nothing constraint means that filling capacity with the highest-ratio item may leave insufficient room for combinations of smaller items that total more value."

- question: "After filling a 2D dp[n][W] table for the 0/1 knapsack, how do you determine which items were included in the optimal solution?"
  type: multiple-choice
  options:
    - "Select the n items whose individual values appear in the dp table cells"
    - "Trace backward from dp[n][W]: if dp[i][w] ≠ dp[i-1][w], item i was included; move to dp[i-1][w - weight_i]"
    - "Re-run the greedy algorithm on the items sorted by their DP-table contributions"
    - "Read the items off the final row of the table in left-to-right order"
  answer: 1
  explanation: "The DP table stores optimal values, not item selections. To reconstruct the solution, you backtrack: starting at dp[n][W], if the value differs from dp[i-1][w], item i was included (because we took the 'include' branch in the recurrence). Record item i, subtract its weight, and move to dp[i-1][w - weight_i]. If the values are equal, item i was skipped — just move to dp[i-1][w]. This linear-time reconstruction is a key step that distinguishes computing the optimal value from recovering the optimal subset."

- question: "The 1D (space-optimized) version of the 0/1 knapsack DP requires iterating through capacity values in decreasing order (from W down to weight_i) when processing each item."
  type: true-false
  answer: true
  explanation: "In the standard 2D recurrence, the 'include item i' case reads from the *previous* row (dp[i-1][w - weight_i]). If you collapse to a 1D array and iterate weight from low to high, you would read an already-updated value from the *current* row — effectively allowing item i to be used multiple times. By iterating from high to low, when you update dp[w], dp[w - weight_i] still holds the value from the previous row (before item i was processed), correctly enforcing the 0/1 constraint."

- question: "Since the 0/1 knapsack DP runs in O(nW) time, it is a polynomial-time algorithm and can efficiently handle any input, including cases where W is a 100-digit number."
  type: true-false
  answer: false
  explanation: "O(nW) is *pseudopolynomial* — polynomial in the numeric value of W, but not in the size of the input. The input size for W is O(log W) bits, so an algorithm polynomial in W is exponential in the number of bits needed to represent W. When W is a 100-digit number (roughly 10^100), the DP table is astronomically large and the algorithm is completely infeasible. The 0/1 knapsack problem is NP-hard; O(nW) does not contradict this because W itself can be exponentially large relative to input size."

- question: "Why does the 0/1 knapsack problem require dynamic programming rather than a greedy approach, and what property of the problem makes greedy fail?"
  type: short-answer
  answer: "Greedy fails because selecting items by value-to-weight ratio ignores how items interact with each other given the capacity constraint. The all-or-nothing rule means that choosing the highest-ratio item may consume capacity that would have been better used by a combination of smaller items. DP works because it exhaustively evaluates every possible subset by considering, for each item and each remaining capacity, whether to include or skip the item — capturing the interaction that greedy misses."
  explanation: "The greedy approach works for the *fractional* knapsack (where you can take parts of items) because the exchange argument holds: you can always swap a lower-ratio fraction for a higher-ratio one without loss. But in the 0/1 version, items are indivisible. This creates combinatorial dependencies among items that greedy cannot model. DP's recurrence makes these dependencies explicit: dp[i][w] considers both 'skip item i (inherited solution)' and 'take item i (adds its value, reduces capacity),' correctly modeling all interactions."
```

## Explainer

You already know from your introduction to dynamic programming that DP works by breaking a problem into overlapping subproblems and combining their solutions. The 0/1 knapsack problem is one of the clearest demonstrations of why this strategy is necessary. You have a bag that can carry at most W units of weight, and a set of n items, each with a specific weight and value. Your goal is to pick the combination of items that maximizes total value without exceeding the capacity. The "0/1" constraint means each item is either taken whole or left behind — no splitting allowed.

The greedy instinct is to grab items with the best value-to-weight ratio first. But this fails for the 0/1 case. Consider a knapsack with capacity 10, and three items: one weighing 6 with value 8, one weighing 5 with value 5, and one weighing 5 with value 5. The greedy approach takes the first item (best ratio) for a total value of 8, but taking the two smaller items yields 10. The discrete all-or-nothing choice creates interactions between items that greedy strategies cannot account for.

The DP solution builds a two-dimensional table **dp[i][w]**, where each cell stores the maximum value achievable using the first i items with a capacity limit of w. The key recurrence considers each item in turn: either you skip item i (inheriting dp[i-1][w]) or you include it (adding its value to dp[i-1][w - weight_i], provided it fits). You take whichever option gives a higher value. The base cases are straightforward — with zero items or zero capacity, the maximum value is zero. By filling the table row by row, you systematically evaluate every relevant combination without redundant work.

Once the table is complete, dp[n][W] holds your answer, but you can also **reconstruct the solution** by tracing backward. Starting at dp[n][W], if dp[i][w] differs from dp[i-1][w], item i was included — record it and move to dp[i-1][w - weight_i]. Otherwise item i was skipped, and you move to dp[i-1][w]. This backtracking recovers the exact set of chosen items. A practical optimization reduces space from O(nW) to O(W) by maintaining only a single one-dimensional array and iterating weights in reverse order, since each row depends only on the previous row. The reverse iteration ensures you don't accidentally use an updated value from the current row when you still need the old one.
