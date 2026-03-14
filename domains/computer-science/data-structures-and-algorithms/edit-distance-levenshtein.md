---
id: edit-distance-levenshtein
title: Edit Distance (Levenshtein Distance)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
- id: longest-common-subsequence
  type: soft
tags:
- edit-distance
- levenshtein
- dynamic-programming
- string-distance
- spell-checking
stage: formal-systems
status: draft
---

# Edit Distance (Levenshtein Distance)

## Core Idea
Edit distance is the minimum number of single-character edits (insert, delete, replace) to transform one string into another. DP solution: dp[i][j] = edit distance between first i and first j characters. If A[i−1] == B[j−1], copy dp[i−1][j−1]; else dp[i][j] = 1 + min(dp[i−1][j], dp[i][j−1], dp[i−1][j−1]) for delete, insert, replace.

## How It's Best Learned
Trace edit distance by hand on short strings, filling the DP table. Understand each operation and its cost. Implement and test on spell-checking examples. Reconstruct the actual edits by backtracking.

## Common Misconceptions
- Edit distance equals LCS (related but different; low edit distance doesn't always mean high LCS). - Only consider one operation (all three—insert, delete, replace—are equally important).
