---
id: longest-increasing-subsequence-optimization
title: 'Longest Increasing Subsequence: Dynamic Programming and Optimization'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
tags:
- dynamic-programming
- sequences
- optimization
stage: formal-systems
status: draft
---

# Longest Increasing Subsequence: Dynamic Programming and Optimization

## Core Idea
The longest increasing subsequence (LIS) is the longest sequence of elements where each is greater than the previous. DP solves it in O(n²) time. Binary search optimization (tracking smallest tail values of LIS of each length) achieves O(n log n). Applications include stock trading, sequence alignment, and version control.

## How It's Best Learned
Implement O(n²) DP (dp[i] = longest LIS ending at i). Then implement O(n log n) with binary search on tails. Trace both on the same input and observe how binary search prunes comparisons.

## Common Misconceptions
- Thinking LIS requires contiguous elements; it's subsequence (not subarray).
- Assuming O(n²) DP is always sufficient; O(n log n) matters for large sequences.
- Not recognizing that LIS is a canonical DP problem useful for understanding the technique.

## Explainer

The **longest increasing subsequence (LIS)** problem asks: given a sequence of numbers, what is the longest subsequence where each element is strictly greater than the one before it? A subsequence does not need to be contiguous — you can skip elements — which is what distinguishes it from a subarray. For example, in [3, 1, 4, 1, 5, 9, 2, 6], one LIS is [1, 4, 5, 9] with length 4, and another equally valid one is [1, 4, 5, 6].

The classic dynamic programming approach defines dp[i] as the length of the longest increasing subsequence that ends at index i. For each position i, you look back at every earlier position j where the value is smaller, and take dp[i] = max(dp[j] + 1) over all valid j. Since each position checks all earlier positions, this runs in O(n²). This directly applies the DP pattern you already know: define subproblems, establish a recurrence, and fill the table in order. The base case is dp[i] = 1 for every i — each element alone is a subsequence of length 1.

The O(n²) solution works but becomes too slow for sequences of length 100,000 or more. The **patience sorting optimization** brings this down to O(n log n) using a clever auxiliary array called **tails**, where tails[k] stores the smallest possible tail element of any increasing subsequence of length k+1 found so far. As you scan through the input, each new element either extends the longest subsequence (append to tails) or replaces an element in tails using binary search to find the correct position. The key property is that tails is always sorted, which is what makes binary search valid. When a new value is smaller than some tails[k], replacing tails[k] doesn't change the current LIS length — it keeps the door open for longer subsequences to form later by lowering the bar for future extensions.

To build intuition for why this works, imagine you are managing multiple "candidate" subsequences simultaneously. Rather than tracking every candidate explicitly, the tails array compresses them into a single sorted structure that captures just the information you need: the minimum ending value at each possible length. Binary search on this sorted structure replaces the O(n) inner scan of the basic DP, yielding the O(n log n) improvement. If you also need to recover the actual subsequence (not just its length), you maintain a predecessor array alongside tails to trace back through the choices.
