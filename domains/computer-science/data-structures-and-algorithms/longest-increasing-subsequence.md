---
id: longest-increasing-subsequence
title: Longest Increasing Subsequence (LIS) Problem
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
- id: binary-search-algorithm
  type: soft
tags:
- dynamic-programming
- lis
- subsequence
- greedy
- binary-search
stage: formal-systems
status: draft
---

# Longest Increasing Subsequence (LIS) Problem

## Core Idea
The longest increasing subsequence problem finds the longest subsequence of elements in increasing order. Naive DP: O(n²) via dp[i] = 1 + max(dp[j] for all j < i where A[j] < A[i]). Optimal O(n log n) approach: maintain the smallest tail value for each LIS length and binary search to find where the next element fits. This elegantly combines DP and binary search.

## How It's Best Learned
Trace the O(n²) DP approach by hand. Then trace the O(n log n) approach with the tail array and binary search. Compare both on the same input and see the speed difference. Understand the tail-array invariant.

## Common Misconceptions
- LIS requires strict inequality (A[i] > A[j]); non-strictly increasing is a different problem. - The O(n log n) solution is always faster (asymptotically yes; for small n, O(n²) may be faster due to constant factors).

## Explainer

The Longest Increasing Subsequence problem asks: given a sequence of numbers, what is the length of the longest subsequence where each element is strictly larger than the one before it? A **subsequence** does not need to be contiguous — you can skip elements — but the relative order must be preserved. For example, in [3, 1, 4, 1, 5, 9, 2, 6], one LIS is [1, 4, 5, 9] with length 4, and another is [1, 4, 5, 6].

The O(n²) dynamic programming approach builds directly on the DP framework you already know. Define dp[i] as the length of the longest increasing subsequence that ends at index i. For each position i, look back at every earlier position j: if A[j] < A[i], then you could extend the subsequence ending at j by appending A[i], giving dp[i] = max(dp[i], dp[j] + 1). The base case is dp[i] = 1 for all i (every element is a subsequence of length 1 by itself). The answer is max(dp[0..n-1]). This is a textbook example of the "consider all previous states" DP pattern — each state depends on all prior states, yielding the quadratic runtime.

The O(n log n) optimization replaces the inner linear scan with a **binary search**. Maintain an array called `tails`, where tails[k] stores the smallest possible tail element of any increasing subsequence of length k+1 found so far. This array is always sorted — a crucial invariant. For each new element, binary search `tails` to find the leftmost position where the element could be placed: if it extends the longest subsequence found so far, append it; otherwise, replace the first tail value that is greater than or equal to it. The replacement keeps future options open by lowering the bar for extending subsequences of that length.

Walk through [3, 1, 4, 1, 5, 9, 2, 6]: after 3, tails = [3]. After 1, tails = [1] (1 replaces 3 — a subsequence of length 1 ending in 1 is more promising). After 4, tails = [1, 4]. After the second 1, no change. After 5, tails = [1, 4, 5]. After 9, tails = [1, 4, 5, 9]. After 2, tails = [1, 2, 5, 9] (2 replaces 4). After 6, tails = [1, 2, 5, 6] (6 replaces 9). The length of `tails` is 4, which is the LIS length. Note that `tails` itself is not necessarily an actual subsequence from the input — it is a bookkeeping structure that tracks the best possible endpoints. Each element triggers one binary search on the sorted `tails` array, so the total work is O(n log n).
