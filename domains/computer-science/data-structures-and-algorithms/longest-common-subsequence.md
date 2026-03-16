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

## Explainer

From your study of dynamic programming, you know the core pattern: define a subproblem, write a recurrence that relates larger subproblems to smaller ones, and fill in a table bottom-up to avoid redundant computation. The **Longest Common Subsequence (LCS)** problem is one of the cleanest applications of this pattern. Given two strings — say "ABCBDAB" and "BDCAB" — you want the longest sequence of characters that appears in both strings in the same order, though not necessarily consecutively. Here the answer is "BCAB" (length 4). Notice that "B", "C", "A", "B" appear in that order in both strings, but they are not adjacent in either one. This distinction between a **subsequence** (same order, gaps allowed) and a **substring** (same order, no gaps) is critical.

The DP formulation builds a two-dimensional table `dp[i][j]` where each cell represents the length of the LCS of the first `i` characters of string A and the first `j` characters of string B. The base cases are straightforward: `dp[0][j] = 0` and `dp[i][0] = 0`, because the LCS of any string with an empty string is empty. The recurrence handles two cases. If the characters match — `A[i-1] == B[j-1]` — then this matching character extends the best solution from `dp[i-1][j-1]` by one: `dp[i][j] = dp[i-1][j-1] + 1`. If they don't match, you take the better of two options: skip the current character from A (`dp[i-1][j]`) or skip it from B (`dp[i][j-1]`). This "match or skip" logic is what makes LCS a DP problem rather than a greedy one — you cannot simply take the first match you find, because an early match might block a longer overall subsequence.

Once you fill the entire table, `dp[m][n]` gives you the length of the LCS, where m and n are the lengths of the two strings. But often you want the actual subsequence, not just its length. To **reconstruct** the LCS, start at `dp[m][n]` and trace backward: if the characters at position `i` and `j` match, that character is part of the LCS — record it and move diagonally to `dp[i-1][j-1]`. If they don't match, move in the direction of the larger neighbor (up or left). This backtracking follows the decisions the table encoded during the forward pass.

LCS has deep practical significance. The Unix `diff` utility, which shows differences between two files, is fundamentally an LCS computation — the common subsequence represents unchanged lines, and everything else is an insertion or deletion. Version control systems like Git use similar algorithms to merge changes. LCS is also the foundation for **edit distance** (Levenshtein distance), which extends the same table structure by adding a cost for substitutions. If you understand LCS well, edit distance is a natural one-step generalization: instead of just matching or skipping, you also allow replacing one character with another at a cost. The O(n × m) time and space complexity can be reduced to O(min(n, m)) space using the rolling-array optimization you likely saw in your DP introduction, since each row only depends on the previous row.
