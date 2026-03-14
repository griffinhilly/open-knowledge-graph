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
