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

## Explainer

From your study of dynamic programming, you know the core technique: break a problem into overlapping subproblems, solve each one once, and store the results in a table. The **edit distance** problem (also called **Levenshtein distance**) is one of the cleanest applications of this idea. Given two strings — say "kitten" and "sitting" — the edit distance is the minimum number of single-character operations (insert, delete, or replace) needed to transform one string into the other. For "kitten" → "sitting," the answer is 3: replace k→s, replace e→i, insert g.

The DP solution builds a 2D table where dp[i][j] represents the edit distance between the first i characters of string A and the first j characters of string B. The base cases are straightforward: dp[i][0] = i (deleting all i characters from A to reach an empty B) and dp[0][j] = j (inserting all j characters of B into an empty A). For the general case, you compare A[i] with B[j]. If they match, no operation is needed and dp[i][j] = dp[i-1][j-1]. If they differ, you take the minimum of three choices: **replace** A[i] with B[j] (cost = dp[i-1][j-1] + 1), **delete** A[i] (cost = dp[i-1][j] + 1), or **insert** B[j] after A[i] (cost = dp[i][j-1] + 1). Each cell in the table depends only on the cell above, to the left, and diagonally above-left.

Walking through a small example makes this concrete. For A = "cat" and B = "car," the table is 4×4. The diagonal represents matching characters: c=c (cost 0), a=a (cost 0), t≠r (cost 1 for replacement). The final cell dp[3][3] = 1, confirming that one replacement transforms "cat" into "car." For longer strings, the table fills out the same way — and the beauty of DP is that each cell is computed once, giving O(mn) time for strings of length m and n.

The applications are remarkably broad. Spell checkers use edit distance to rank correction candidates — "teh" has distance 1 from "the" but distance 2 from "tea." Bioinformatics uses a generalized version (sequence alignment) where different operations have different costs to compare DNA sequences and identify mutations. Search engines use it to handle typos in queries. The space optimization is also worth knowing: since each row of the table depends only on the previous row, you can use two rolling arrays of size min(m, n) instead of the full m × n table, reducing space from O(mn) to O(min(m, n)) while keeping the same O(mn) time complexity.
