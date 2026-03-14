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
