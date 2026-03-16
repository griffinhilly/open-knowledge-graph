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

## Explainer

From dynamic programming, you know the technique of breaking a problem into overlapping subproblems and storing their solutions to avoid redundant computation. From longest common subsequence, you have practiced filling a 2D table where each cell depends on its neighbors. Edit distance applies this same framework to a different question: given two strings A and B, what is the minimum number of single-character operations needed to transform A into B? The allowed operations are **insertion** (add a character), **deletion** (remove a character), and **substitution** (replace one character with another), each costing 1.

The key insight is that the problem has **optimal substructure** on string prefixes. To compute the edit distance between A[1..i] and B[1..j], consider the last characters. If A[i] equals B[j], no operation is needed for these characters — the answer is just the edit distance between A[1..i-1] and B[1..j-1]. If they differ, you have three choices: substitute A[i] with B[j] (cost 1 plus the distance for A[1..i-1] and B[1..j-1]), delete A[i] (cost 1 plus the distance for A[1..i-1] and B[1..j]), or insert B[j] after A[i] (cost 1 plus the distance for A[1..i] and B[1..j-1]). The minimum of these three options gives dp[i][j]. The base cases are straightforward: transforming an empty string into B[1..j] requires j insertions, and transforming A[1..i] into an empty string requires i deletions.

To build intuition, trace through a small example. Converting "kitten" to "sitting" requires three edits: substitute k→s, substitute e→i, insert g. The DP table makes this systematic. Create a grid with "kitten" along the top and "sitting" along the side. Each cell (i, j) represents the cost of transforming the first i characters of "kitten" into the first j characters of "sitting." Fill the table row by row, and the bottom-right cell gives the final answer: 3. By tracing back through the table — following which of the three choices was minimal at each step — you can reconstruct the actual sequence of edits, not just the count.

Edit distance has remarkably broad applications. **Spell checkers** use it to suggest corrections: words within edit distance 1 or 2 of a misspelled word are likely candidates. **Bioinformatics** uses variants of edit distance (with different costs for insertions, deletions, and substitutions) to align DNA and protein sequences, measuring evolutionary divergence. **Fuzzy search** in databases uses edit distance to match records despite typos. The standard algorithm runs in O(n·m) time and space, but if you only need the distance (not the edit sequence), you can reduce space to O(min(n, m)) by keeping only two rows of the table at a time — a practical optimization when comparing very long strings.
