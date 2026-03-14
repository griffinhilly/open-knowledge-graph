---
id: edit-distance-dynamic-programming
title: 'Edit Distance: Levenshtein Distance and DP'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
tags:
- dynamic-programming
- strings
- distance
stage: formal-systems
status: draft
---

# Edit Distance: Levenshtein Distance and DP

## Core Idea
Edit distance (Levenshtein distance) is the minimum number of single-character edits (insert, delete, replace) to transform one string to another. DP solves it in O(mn) time and space. Applications include spell checking, sequence alignment, and DNA comparison.

## How It's Best Learned
Implement the DP recurrence: dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + cost). Trace on short strings. Optimize space to O(min(m,n)) using rolling arrays.

## Common Misconceptions
- Confusing edit distance with longest common subsequence; they're related but distinct.
- Not understanding the three operations (insert, delete, replace) and their costs.
- Assuming O(mn) space is necessary; space optimization often applies.
