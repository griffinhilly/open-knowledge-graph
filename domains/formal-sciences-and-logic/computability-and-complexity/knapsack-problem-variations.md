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

## Explainer

The 0/1 knapsack problem asks: given n items each with a weight and a value, and a capacity W, which items should you pack to maximize value without exceeding the capacity? You already know this is NP-hard. But it behaves differently from problems like graph 3-coloring or SAT in a subtle and instructive way: it has a dynamic programming solution that appears — but isn't quite — polynomial.

The DP algorithm builds a table where entry (i, w) stores the maximum value achievable using the first i items with weight budget w. Filling this table takes O(nW) time. For small W — say, items with weights in the hundreds — this is perfectly practical. The confusion arises because complexity is measured in the **bit-length** of the input, not the numerical value of the numbers. W can be encoded in log₂W bits, meaning that if W = 2^{100}, the input is only about 100 bits long but the DP table has 2^{100} entries. The algorithm's running time is exponential in the input size. This is what **pseudo-polynomial time** means: polynomial in the numerical value of the input, but potentially exponential in the bit-length.

This distinction separates **weakly NP-hard** problems from **strongly NP-hard** ones. Knapsack is weakly NP-hard: hard in general, but tractable when input values are bounded by a polynomial in n. By contrast, 3-SAT is strongly NP-hard — no pseudo-polynomial shortcut exists because the problem has no natural numeric parameter to exploit. The significance for approximation is that weakly NP-hard problems often admit an FPTAS. For knapsack, you can round the item values to nearby multiples, making W effectively small enough for the DP to run in polynomial time in both n and 1/ε — giving a (1+ε)-approximation for any ε > 0 at polynomial cost.

The knapsack problem is also a useful lens on the relationship between DP and NP-hardness more generally. Dynamic programming solves many optimization problems efficiently by exploiting **optimal substructure** — the property that the optimal solution to the whole problem can be built from optimal solutions to subproblems. For knapsack, this structure exists, but the state space (the table size) depends on the input values rather than just their count. When the values are bounded, the DP is fast. When they are unbounded, the DP is exponential, and we are back to the NP-hard baseline. The lesson: DP does not bypass NP-hardness; it works within it when the problem's numeric structure allows.
