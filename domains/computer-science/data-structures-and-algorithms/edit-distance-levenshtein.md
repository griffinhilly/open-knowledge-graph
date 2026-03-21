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

## Questions

```yaml
- question: "You are computing the edit distance between 'cat' and 'cut'. At position (i=2, j=2), characters 'a' and 'u' differ. Which recurrence applies and what does each option represent?"
  type: multiple-choice
  options:
    - "dp[i][j] = dp[i-1][j-1] — since both strings have length 3, matching positions cost nothing"
    - "dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) — delete, insert, or replace respectively"
    - "dp[i][j] = dp[i][j-1] — insertion is always cheapest when characters differ"
    - "dp[i][j] = dp[i-1][j] + dp[i][j-1] — both a deletion and insertion are required"
  answer: 1
  explanation: "When A[i-1] ≠ B[j-1], we can't copy — we must pay 1 plus the cheapest of three subproblems: dp[i-1][j] (delete A[i-1]), dp[i][j-1] (insert B[j-1]), or dp[i-1][j-1] (substitute A[i-1] for B[j-1]). We always evaluate all three and take the minimum — the algorithm doesn't commit to one operation type. Option A is the equal-character case; options C and D ignore the full set of choices."

- question: "For identical strings A = 'abc' and B = 'abc', what is dp[3][3], and why?"
  type: multiple-choice
  options:
    - "3, because there are 3 character positions to compare"
    - "6, because every pair of characters must be evaluated"
    - "0, because matching characters propagate the previous subproblem's cost unchanged"
    - "1, because the DP always performs at least one comparison operation"
  answer: 2
  explanation: "When A[i-1] == B[j-1] at every position, dp[i][j] = dp[i-1][j-1] with no added cost. This propagates dp[0][0] = 0 unchanged across every cell along the diagonal, giving dp[3][3] = 0. No edits are needed to transform a string into itself — the algorithm correctly finds this by the equal-character case."

- question: "When A[i-1] == B[j-1], dp[i][j] = dp[i-1][j-1] with no additional cost — no operation is charged."
  type: true-false
  answer: true
  explanation: "This is the key 'copy' case in the recurrence: matching characters need no edit, so we simply inherit the cost of aligning the shorter prefixes A[1..i-1] and B[1..j-1]. This is what makes edit distance efficient — long stretches of matching characters cost nothing and reduce to a previously solved subproblem."

- question: "Two strings with a small edit distance will always share a long longest common subsequence."
  type: true-false
  answer: false
  explanation: "Edit distance and LCS are related but different measures. 'abc' and 'xyz' have edit distance 3 (three substitutions) and LCS length 0. 'ab' and 'ba' have edit distance 2 (a swap requires two single-character edits) but LCS length 1. Low edit distance does not guarantee high LCS, nor vice versa — they quantify different aspects of string similarity."

- question: "When characters A[i-1] and B[j-1] differ, the recurrence considers exactly three sub-problems: dp[i-1][j], dp[i][j-1], and dp[i-1][j-1]. What edit operation does each sub-problem represent?"
  type: short-answer
  answer: "dp[i-1][j] corresponds to deleting A[i-1] from A — consuming one character from A without advancing in B. dp[i][j-1] corresponds to inserting B[j-1] into A — advancing one step in B without consuming a new character from A. dp[i-1][j-1] corresponds to substituting A[i-1] with B[j-1] — consuming one character from each string simultaneously. Each costs 1, and the minimum is taken because we want the cheapest sequence of edits."
  explanation: "The insight is that each operation maps to a different relationship between the remaining prefix lengths. Because all three cost the same (1 in standard Levenshtein), the DP simply finds which direction leads to the cheapest remaining alignment. Backtracking through the choices at each cell reconstructs the actual edit sequence."
```

## Explainer

From dynamic programming, you know the technique of breaking a problem into overlapping subproblems and storing their solutions to avoid redundant computation. From longest common subsequence, you have practiced filling a 2D table where each cell depends on its neighbors. Edit distance applies this same framework to a different question: given two strings A and B, what is the minimum number of single-character operations needed to transform A into B? The allowed operations are **insertion** (add a character), **deletion** (remove a character), and **substitution** (replace one character with another), each costing 1.

The key insight is that the problem has **optimal substructure** on string prefixes. To compute the edit distance between A[1..i] and B[1..j], consider the last characters. If A[i] equals B[j], no operation is needed for these characters — the answer is just the edit distance between A[1..i-1] and B[1..j-1]. If they differ, you have three choices: substitute A[i] with B[j] (cost 1 plus the distance for A[1..i-1] and B[1..j-1]), delete A[i] (cost 1 plus the distance for A[1..i-1] and B[1..j]), or insert B[j] after A[i] (cost 1 plus the distance for A[1..i] and B[1..j-1]). The minimum of these three options gives dp[i][j]. The base cases are straightforward: transforming an empty string into B[1..j] requires j insertions, and transforming A[1..i] into an empty string requires i deletions.

To build intuition, trace through a small example. Converting "kitten" to "sitting" requires three edits: substitute k→s, substitute e→i, insert g. The DP table makes this systematic. Create a grid with "kitten" along the top and "sitting" along the side. Each cell (i, j) represents the cost of transforming the first i characters of "kitten" into the first j characters of "sitting." Fill the table row by row, and the bottom-right cell gives the final answer: 3. By tracing back through the table — following which of the three choices was minimal at each step — you can reconstruct the actual sequence of edits, not just the count.

Edit distance has remarkably broad applications. **Spell checkers** use it to suggest corrections: words within edit distance 1 or 2 of a misspelled word are likely candidates. **Bioinformatics** uses variants of edit distance (with different costs for insertions, deletions, and substitutions) to align DNA and protein sequences, measuring evolutionary divergence. **Fuzzy search** in databases uses edit distance to match records despite typos. The standard algorithm runs in O(n·m) time and space, but if you only need the distance (not the edit sequence), you can reduce space to O(min(n, m)) by keeping only two rows of the table at a time — a practical optimization when comparing very long strings.
