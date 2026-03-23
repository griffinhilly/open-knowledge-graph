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
status: validated
---

# Longest Common Subsequence (LCS) Problem

## Core Idea
The longest common subsequence problem finds the longest sequence of characters appearing in the same order (not necessarily contiguous) in two strings. DP solution: dp[i][j] = longest LCS of first i characters of string A and first j characters of string B. Recurrence: if A[i−1] == B[j−1], dp[i][j] = dp[i−1][j−1] + 1; else dp[i][j] = max(dp[i−1][j], dp[i][j−1]).

## How It's Best Learned
Trace the DP table by hand on short strings. Implement and reconstruct the LCS from the table. Test on various examples including repeated characters. See LCS as the foundation for edit distance and diff algorithms.

## Common Misconceptions
- LCS is the same as edit distance (related but different; LCS finds a common subsequence; edit distance counts minimum edits). - LCS finds contiguous matches (no, it preserves order but can skip characters).

## Questions

```yaml
- question: "A greedy algorithm for LCS matches the first common character it finds, then continues from that point in both strings. On strings A = 'ABCB' and B = 'BACB', it matches 'B' at position A[1] and B[0], then 'C' and 'B', finding LCS length 3. Could it have done better?"
  type: multiple-choice
  options:
    - "No — greedy always finds the optimal LCS length"
    - "No — length 3 is the true LCS length, but greedy may have been lucky; on other inputs it can fail"
    - "Yes — the actual LCS is length 4, which greedy missed by committing to 'B' too early"
    - "Yes — but only because the strings have repeated characters, where greedy always fails"
  answer: 1
  explanation: "In this case greedy happened to find the correct length, but the reasoning is wrong. On other inputs, an early greedy match can block a longer overall subsequence — there is no guarantee that grabbing the first match produces the globally optimal result. The problem is that locally optimal choices can prevent globally optimal solutions. LCS requires explicitly comparing the two alternatives when characters don't match (skip from A vs. skip from B) and tracking which gives a longer result. Only exhaustive DP comparison guarantees the true maximum."

- question: "In the LCS DP table, dp[i][j] represents:"
  type: multiple-choice
  options:
    - "Whether characters A[i] and B[j] match"
    - "The length of the LCS of the entire strings A and B, computed by row i and column j"
    - "The length of the LCS of the first i characters of A and the first j characters of B"
    - "The number of characters skipped in A to reach position i in the LCS"
  answer: 2
  explanation: "dp[i][j] is defined as the LCS length for the prefix of A of length i (A[1..i]) and the prefix of B of length j (B[1..j]). This prefix-subproblem structure enables the recurrence: when characters match, you extend dp[i-1][j-1] by one; when they don't match, you take max(dp[i-1][j], dp[i][j-1]). The final answer dp[m][n] gives the LCS of the complete strings."

- question: "The LCS of two strings is always unique — there is exactly one longest common subsequence."
  type: true-false
  answer: false
  explanation: "Multiple subsequences of the same maximum length can exist. For example, the LCS of 'ABAB' and 'BABA' has length 3, but both 'ABA' and 'BAB' are valid LCSs. The DP table gives the LCS length deterministically, but the backtracking step may encounter ties — positions where both 'skip from A' and 'skip from B' are equally optimal. Different tie-breaking choices produce different but equally valid LCS sequences."

- question: "Every substring of a string is also a subsequence of that string, but not every subsequence is a substring."
  type: true-false
  answer: true
  explanation: "A substring requires consecutive characters; a subsequence only requires characters to appear in the same relative order, with gaps allowed. Since consecutive characters trivially maintain order without gaps, every substring is a subsequence. But 'AC' is a subsequence of 'ABC' (skipping 'B') without being a substring. The LCS problem uses the more flexible subsequence definition — this is what makes it applicable to comparing files line-by-line in the Unix diff command, where matching lines need not be adjacent."

- question: "Why doesn't a greedy approach work for the LCS problem, and what does dynamic programming enable that greedy cannot?"
  type: short-answer
  answer: "Greedy matches characters left-to-right, committing to the first match it finds. This fails because an early match can 'use up' a character position in a way that prevents a longer overall subsequence. DP solves this by explicitly considering both alternatives when characters don't match — skip from A or skip from B — and recording the best result in the table. Because the table is filled bottom-up from all prefix subproblems, every possible alignment is implicitly considered and the optimum is guaranteed."
  explanation: "The formal property DP exploits is optimal substructure: the LCS of A[1..i] and B[1..j] can be built from LCSs of smaller prefixes. Once dp[i][j] is computed, it is provably optimal for that prefix pair and never needs to be re-examined. Greedy lacks this guarantee because it commits to a local choice without verifying it doesn't foreclose better global options."
```

## Explainer

From your study of dynamic programming, you know the core pattern: define a subproblem, write a recurrence that relates larger subproblems to smaller ones, and fill in a table bottom-up to avoid redundant computation. The **Longest Common Subsequence (LCS)** problem is one of the cleanest applications of this pattern. Given two strings — say "ABCBDAB" and "BDCAB" — you want the longest sequence of characters that appears in both strings in the same order, though not necessarily consecutively. Here the answer is "BCAB" (length 4). Notice that "B", "C", "A", "B" appear in that order in both strings, but they are not adjacent in either one. This distinction between a **subsequence** (same order, gaps allowed) and a **substring** (same order, no gaps) is critical.

The DP formulation builds a two-dimensional table `dp[i][j]` where each cell represents the length of the LCS of the first `i` characters of string A and the first `j` characters of string B. The base cases are straightforward: `dp[0][j] = 0` and `dp[i][0] = 0`, because the LCS of any string with an empty string is empty. The recurrence handles two cases. If the characters match — `A[i-1] == B[j-1]` — then this matching character extends the best solution from `dp[i-1][j-1]` by one: `dp[i][j] = dp[i-1][j-1] + 1`. If they don't match, you take the better of two options: skip the current character from A (`dp[i-1][j]`) or skip it from B (`dp[i][j-1]`). This "match or skip" logic is what makes LCS a DP problem rather than a greedy one — you cannot simply take the first match you find, because an early match might block a longer overall subsequence.

Once you fill the entire table, `dp[m][n]` gives you the length of the LCS, where m and n are the lengths of the two strings. But often you want the actual subsequence, not just its length. To **reconstruct** the LCS, start at `dp[m][n]` and trace backward: if the characters at position `i` and `j` match, that character is part of the LCS — record it and move diagonally to `dp[i-1][j-1]`. If they don't match, move in the direction of the larger neighbor (up or left). This backtracking follows the decisions the table encoded during the forward pass.

LCS has deep practical significance. The Unix `diff` utility, which shows differences between two files, is fundamentally an LCS computation — the common subsequence represents unchanged lines, and everything else is an insertion or deletion. Version control systems like Git use similar algorithms to merge changes. LCS is also the foundation for **edit distance** (Levenshtein distance), which extends the same table structure by adding a cost for substitutions. If you understand LCS well, edit distance is a natural one-step generalization: instead of just matching or skipping, you also allow replacing one character with another at a cost. The O(n × m) time and space complexity can be reduced to O(min(n, m)) space using the rolling-array optimization you likely saw in your DP introduction, since each row only depends on the previous row.
