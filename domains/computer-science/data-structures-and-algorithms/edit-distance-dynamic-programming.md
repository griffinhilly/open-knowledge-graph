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

## Questions

```yaml
- question: "You are computing the edit distance between 'CA' and 'ABC'. What is dp[1][1] — the edit distance between the prefix 'C' and the prefix 'A'?"
  type: multiple-choice
  options:
    - "0, because both substrings have length 1"
    - "1, because one replacement transforms 'C' into 'A'"
    - "2, because you must delete 'C' and then insert 'A'"
    - "Cannot be determined without computing the full table first"
  answer: 1
  explanation: "dp[1][1] asks: what is the minimum number of edits to turn the 1-character string 'C' into the 1-character string 'A'? Since C ≠ A, you apply the recurrence: min(dp[0][0]+1, dp[0][1]+1, dp[1][0]+1) = min(0+1, 1+1, 1+1) = 1. One replacement suffices. Option C represents a misunderstanding — delete-then-insert costs 2, but the recurrence already finds the cheaper replacement path. Option A mistakes 'same length' for 'same content.'"

- question: "A programmer wants to reduce the O(mn) space of the edit distance algorithm. They realize they can use only two rows instead of the full table. Which property of the recurrence makes this optimization valid?"
  type: multiple-choice
  options:
    - "The recurrence is linear, so intermediate results can be discarded"
    - "Each cell dp[i][j] depends only on dp[i-1][j-1], dp[i-1][j], and dp[i][j-1] — the previous row and the current row so far"
    - "The strings must have equal length for the optimization to work"
    - "The optimization only applies when using memoization rather than tabulation"
  answer: 1
  explanation: "The recurrence dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1) looks at exactly three neighbors: directly above (i-1, j), diagonally above-left (i-1, j-1), and directly left (i, j-1). No cell further back than row i-1 is ever needed. This means you can fill row i using only row i-1 and the partially-filled row i, then discard all earlier rows. With care, even the two-row space can be reduced to O(min(m,n)) using a single rolling array."

- question: "The edit distance between two strings is symmetric: dist('kitten', 'sitting') equals dist('sitting', 'kitten')."
  type: true-false
  answer: true
  explanation: "Every insertion in one direction corresponds to a deletion in the reverse direction, and replacements are symmetric. Any sequence of edits transforming A into B can be reversed to transform B into A with the same number of operations. This symmetry is not immediately obvious from the recurrence (the table is not symmetric), but the optimal cost works out equal in both directions."

- question: "Edit distance and longest common subsequence (LCS) measure the same underlying relationship between strings — one just counts edits while the other counts shared characters."
  type: true-false
  answer: false
  explanation: "Although both relate to string similarity, they measure different things with different operations. LCS counts the length of the longest subsequence common to both strings and only uses matches (characters that appear in order in both). Edit distance counts the minimum edits using insert, delete, and replace. A pair of strings can have a long LCS yet still require many edits (e.g., if one string has many extra characters), and the relationship between the two measures is not a simple formula."

- question: "Explain what each of the three terms in the edit distance recurrence — dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1 — represents when A[i] ≠ B[j]. Why does each term add exactly 1?"
  type: short-answer
  answer: "dp[i-1][j-1]+1 represents replacing A[i] with B[j]: you already paid to align the first i-1 characters of A with the first j-1 characters of B, and now pay 1 to swap the mismatched characters. dp[i-1][j]+1 represents deleting A[i]: you pay 1 to remove A[i], then the cost reduces to aligning the first i-1 characters of A with all j characters of B. dp[i][j-1]+1 represents inserting B[j]: you pay 1 to insert B[j] at this position, then the cost reduces to aligning all i characters of A with the first j-1 characters of B. Each adds exactly 1 because each operation is one edit."
  explanation: "The key insight is that each cell reference corresponds to a specific operation: diagonal = replace, up = delete from A, left = insert from B. Taking the minimum selects the cheapest of the three ways to handle the mismatch. When A[i] = B[j], no edit is needed so dp[i][j] = dp[i-1][j-1] with no +1 — the diagonal move is free."
```

## Explainer

From your study of dynamic programming, you know the core technique: break a problem into overlapping subproblems, solve each one once, and store the results in a table. The **edit distance** problem (also called **Levenshtein distance**) is one of the cleanest applications of this idea. Given two strings — say "kitten" and "sitting" — the edit distance is the minimum number of single-character operations (insert, delete, or replace) needed to transform one string into the other. For "kitten" → "sitting," the answer is 3: replace k→s, replace e→i, insert g.

The DP solution builds a 2D table where dp[i][j] represents the edit distance between the first i characters of string A and the first j characters of string B. The base cases are straightforward: dp[i][0] = i (deleting all i characters from A to reach an empty B) and dp[0][j] = j (inserting all j characters of B into an empty A). For the general case, you compare A[i] with B[j]. If they match, no operation is needed and dp[i][j] = dp[i-1][j-1]. If they differ, you take the minimum of three choices: **replace** A[i] with B[j] (cost = dp[i-1][j-1] + 1), **delete** A[i] (cost = dp[i-1][j] + 1), or **insert** B[j] after A[i] (cost = dp[i][j-1] + 1). Each cell in the table depends only on the cell above, to the left, and diagonally above-left.

Walking through a small example makes this concrete. For A = "cat" and B = "car," the table is 4×4. The diagonal represents matching characters: c=c (cost 0), a=a (cost 0), t≠r (cost 1 for replacement). The final cell dp[3][3] = 1, confirming that one replacement transforms "cat" into "car." For longer strings, the table fills out the same way — and the beauty of DP is that each cell is computed once, giving O(mn) time for strings of length m and n.

The applications are remarkably broad. Spell checkers use edit distance to rank correction candidates — "teh" has distance 1 from "the" but distance 2 from "tea." Bioinformatics uses a generalized version (sequence alignment) where different operations have different costs to compare DNA sequences and identify mutations. Search engines use it to handle typos in queries. The space optimization is also worth knowing: since each row of the table depends only on the previous row, you can use two rolling arrays of size min(m, n) instead of the full m × n table, reducing space from O(mn) to O(min(m, n)) while keeping the same O(mn) time complexity.
