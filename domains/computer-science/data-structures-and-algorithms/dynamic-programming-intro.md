---
id: dynamic-programming-intro
title: Dynamic Programming
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: algorithm-design-basics
  type: hard
- id: time-space-complexity
  type: hard
- id: recurrence-relations
  type: soft
- id: topological-sort
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- memoization-and-tabulation
tags:
- dynamic-programming
- DP
- optimal-substructure
- overlapping-subproblems
stage: formal-systems
status: validated
---
# Dynamic Programming

## Core Idea
Dynamic programming (DP) solves optimization and counting problems by breaking them into overlapping subproblems and storing solutions to avoid redundant computation. Two key properties must hold: optimal substructure (the optimal solution contains optimal solutions to subproblems) and overlapping subproblems (the same subproblems recur many times). Classic examples include Fibonacci, 0/1 knapsack, longest common subsequence, and coin change. DP transforms exponential naive recursion into polynomial time by caching intermediate results.

## How It's Best Learned
Start with memoized Fibonacci to see the speedup from caching in isolation. Then tackle structured DP problems: coin change, longest common subsequence, 0/1 knapsack. For each, explicitly define the subproblem before writing any code.

## Common Misconceptions
- DP is not just about filling a table; the hardest part is correctly defining the subproblem and its recurrence.
- Not every recursive problem has overlapping subproblems; divide-and-conquer (merge sort) uses recursion but is not DP because its subproblems are independent.
- Bottom-up tabulation and top-down memoization are equivalent in correctness but differ in stack usage and which subproblems are computed.

## Questions

```yaml
- question: "Which of the following problems is the best candidate for dynamic programming?"
  type: multiple-choice
  options: ["Merge sort on an array of integers", "Binary search on a sorted array", "Computing the minimum number of coins to make change for a given amount", "Finding the maximum element in an unsorted array"]
  answer: 2
  explanation: "Coin change has both required DP properties: optimal substructure (the minimum coins for amount n uses minimum coins for smaller amounts) and overlapping subproblems (the same sub-amounts are computed repeatedly in naive recursion). Merge sort and binary search use divide-and-conquer with non-overlapping subproblems. Finding the maximum element requires a single linear scan with no subproblem reuse."

- question: "Top-down memoization and bottom-up tabulation always produce the same asymptotic time complexity for a given DP problem."
  type: true-false
  answer: true
  explanation: "Both approaches solve each distinct subproblem exactly once. Asymptotic time complexity depends on the number of distinct subproblems times the cost per subproblem — the same quantity regardless of direction. They can differ in practice (stack overhead, whether all subproblems are computed) but not in asymptotic time complexity."

- question: "Before writing any code for a DP problem, what should you define first, and why is this step considered the hardest part?"
  type: short-answer
  answer: "You should precisely define what dp[i] (or dp[i][j], etc.) represents — which subproblem it solves and what its value encodes. This is the hardest step because a vague or incorrect subproblem definition leads to a recurrence that is wrong or cannot be computed, even if the implementation mechanics are correct."
  explanation: "Many DP bugs originate from an ambiguous subproblem definition rather than a wrong recurrence formula. For coin change, dp[i] = 'minimum coins to make amount i' is precise and leads directly to dp[i] = min over all coins c of (1 + dp[i - c]). Without a clear definition first, the recurrence is guesswork that may fail on edge cases."
```

## Explainer

Recursion solves a problem by reducing it to smaller instances of itself. The danger is that naive recursion often recomputes the same smaller instances many times. Consider computing Fibonacci(50) recursively: Fibonacci(3) gets recalculated billions of times because the call tree branches at every level, producing exponential work. Dynamic programming patches this by storing each result the first time it is computed and looking it up instead of recomputing — a technique called memoization.

Two structural properties must hold for DP to apply. **Optimal substructure** means the solution to the full problem can be assembled from optimal solutions to subproblems. The shortest path from A to C through B must use the shortest path from A to B as a segment — if that sub-path were suboptimal, you could improve the full path, contradicting its optimality. **Overlapping subproblems** means the same sub-instances appear repeatedly across the recursion tree. Without overlap, caching adds overhead with no benefit; this is why merge sort, which splits arrays into non-overlapping halves, is divide-and-conquer rather than DP.

The hardest part of dynamic programming is not the code — it is defining the subproblem correctly before you write a line. You should be able to state "dp[i] means ___" in a precise sentence. For coin change, the right definition is: "dp[i] = the minimum number of coins needed to make exactly amount i." Given that, the recurrence follows mechanically: dp[i] = 1 + min over all coins c ≤ i of dp[i - c]. A vague definition like "dp[i] represents the coins used so far" produces an ambiguous recurrence and subtle bugs that are very hard to debug.

Once the subproblem is defined, you can implement it two ways. **Top-down (memoization)**: write the natural recursive solution, add a cache (array or hash map), and check the cache before computing. The code reads like the mathematical recurrence and only computes subproblems that are actually needed. **Bottom-up (tabulation)**: fill a table starting from base cases, computing each entry using previously filled entries. This avoids recursion stack overhead and often performs better in practice. Both have the same asymptotic time complexity — they solve each of the O(n) (or O(n²), etc.) subproblems exactly once.

Your background in recurrence relations connects directly: the DP recurrence is that relation made computational. Your knowledge of time-space complexity explains why DP matters — the transformation from exponential naive recursion to polynomial time, achieved by eliminating redundant computation. And mathematical induction provides the proof structure: show the base case, assume all smaller subproblems are solved correctly, and verify the recurrence step is correct. The inductive structure of correctness proofs and the recursive structure of DP are two sides of the same coin.
