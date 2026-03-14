---
id: longest-common-subsequence
title: Longest Common Subsequence (LCS) Problem
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
builds-toward:
- edit-distance-levenshtein
tags:
- dynamic-programming
- lcs
- subsequence
- string-comparison
stage: formal-systems
status: draft
---

# Longest Common Subsequence (LCS) Problem

## Core Idea
The longest common subsequence problem finds the longest sequence of characters appearing in the same order (not necessarily contiguous) in two strings. DP solution: dp[i][j] = longest LCS of first i characters of string A and first j characters of string B. Recurrence: if A[i−1] == B[j−1], dp[i][j] = dp[i−1][j−1] + 1; else dp[i][j] = max(dp[i−1][j], dp[i][j−1]).

## How It's Best Learned
Trace the DP table by hand on short strings. Implement and reconstruct the LCS from the table. Test on various examples including repeated characters. See LCS as the foundation for edit distance and diff algorithms.

## Common Misconceptions
- LCS is the same as edit distance (related but different; LCS finds a common subsequence; edit distance counts minimum edits). - LCS finds contiguous matches (no, it preserves order but can skip characters).
