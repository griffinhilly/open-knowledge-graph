---
id: cyk-parsing-algorithm
title: CYK Parsing Algorithm and CFL Membership
domain: computer-science
course: theory-of-computation
prerequisites:
- id: normal-forms-for-context-free-grammars
  type: hard
builds-toward:
- closure-properties-context-free
- limitations-of-context-free
tags:
- parsing
- cyk-algorithm
- membership
stage: advanced
status: validated
---

# CYK Parsing Algorithm and CFL Membership

## Core Idea
The Cocke-Younger-Kasami (CYK) algorithm determines in O(n³) time whether a string is in a context-free language given a grammar in CNF. It uses dynamic programming, filling a table where entry (i, j) contains non-terminals that derive the substring of length j starting at position i.

## Questions

```yaml
- question: "You want to run the CYK algorithm using a grammar that contains the rule S → A B C. What must you do before CYK can be applied?"
  type: multiple-choice
  options:
    - "Nothing — CYK can directly handle productions with three or more non-terminals"
    - "Convert the grammar to Chomsky Normal Form by introducing an intermediate non-terminal, e.g., replacing S → ABC with S → AD and D → BC"
    - "Add ε-productions to allow the algorithm to handle empty substrings"
    - "Reverse the input string before filling the parse table"
  answer: 1
  explanation: "CYK requires the grammar to be in Chomsky Normal Form (CNF), where every rule is either A → BC (exactly two non-terminals) or A → a (a single terminal). A production like S → ABC violates CNF. The fix is to introduce a new non-terminal — e.g., D → BC — then replace S → ABC with S → AD. The algorithm's dynamic programming approach depends on CNF's binary branching: each substring can be split at exactly one point into two pieces, and the table is filled by trying all such splits. Three-way productions break this structure and make systematic lookup impossible."

- question: "Why does the CYK algorithm run in O(n³) time, where n is the length of the input string?"
  type: multiple-choice
  options:
    - "Because there are n³ possible substrings of a string of length n"
    - "Because the parse table has O(n²) cells, and filling each cell requires checking O(n) possible split points"
    - "Because each grammar rule must be checked n³ times against the input string"
    - "Because the algorithm requires three complete passes over the entire input string"
  answer: 1
  explanation: "The parse table is triangular with O(n²) cells — one for each (starting position, substring length) pair. Filling each cell requires trying every possible split point: for a substring of length j, there are j−1 ways to split it into two non-empty parts, which is O(n) in the worst case. Total work is O(n²) cells × O(n) split checks = O(n³). This is not just an efficiency observation — it proves that membership testing for any CFL is decidable in polynomial time, a foundational result in formal language theory."

- question: "For a string of length n, the CYK algorithm fills O(n²) cells in a parse table, and filling each cell requires checking O(n) possible split points, giving an overall time complexity of O(n³)."
  type: true-false
  answer: true
  explanation: "This is the correct complexity analysis. The parse table has one cell for each (starting position, length) pair: starting positions range from 1 to n and lengths range from 1 to n, giving O(n²) cells in the triangular table. For a cell corresponding to a substring of length j, there are j−1 possible split points — O(n) in the worst case. Multiplying gives O(n³) total operations. The significance is that O(n³) is polynomial, proving CFL membership is decidable in polynomial time."

- question: "The CYK algorithm can be applied directly to any context-free grammar without preprocessing, as long as the grammar contains no left-recursive rules."
  type: true-false
  answer: false
  explanation: "CYK requires Chomsky Normal Form (CNF), not merely the absence of left recursion. CNF requires every production to be either A → BC or A → a. A grammar without left recursion might still have unit productions (A → B), ε-productions (A → ε), or rules with three or more symbols (A → BCD), all of which violate CNF and prevent direct application of CYK. Converting to CNF is a necessary preprocessing step — but it is always possible, since any CFG can be converted to CNF without changing the language it generates."

- question: "Why does CYK require the grammar to be in Chomsky Normal Form, and what property of CNF makes the dynamic programming approach work?"
  type: short-answer
  answer: "CYK's dynamic programming approach depends on being able to split every substring of length > 1 into exactly two non-overlapping parts and check whether each part is derivable from some non-terminal. CNF enforces binary branching — every rule produces exactly two non-terminals (A → BC) or one terminal (A → a). This means every derivation of a substring has exactly one structural split into two shorter substrings, which can each be looked up in previously filled table cells. Rules with three or more non-terminals would require splitting at two places with three pieces, making the table structure invalid and the lookup undefined."
  explanation: "The question asks students to see why CNF is not just a precondition but the structural property that enables the algorithm. Binary branching means every derivation step can be represented as a combination of exactly two previously computed subproblems — the essential requirement for dynamic programming. Without CNF, the subproblem structure breaks down and the algorithm cannot be applied."
```

## Explainer

From your work with normal forms, you know that any context-free grammar can be converted to **Chomsky Normal Form (CNF)**, where every production is either A → BC (two non-terminals) or A → a (a single terminal). The CYK algorithm exploits this rigid structure to answer the membership question — "is this string in this language?" — using dynamic programming. The key insight is that CNF's binary branching means every derivation of a substring can be split into exactly two parts, and you can systematically try all possible split points.

The algorithm builds a triangular **parse table** bottom-up. For a string w = w₁w₂...wₙ, start with the base case: for each single character wᵢ, find all non-terminals A such that A → wᵢ is a production rule, and place them in cell (i, 1). These are the non-terminals that generate substrings of length 1. Then work upward to longer substrings. For a substring of length j starting at position i, try every way to split it into two non-empty parts: a prefix of length k and a suffix of length j−k, for k = 1, 2, ..., j−1. If non-terminal B is in cell (i, k) and non-terminal C is in cell (i+k, j−k), and there exists a production A → BC, then A goes into cell (i, j). The string is in the language if and only if the start symbol S appears in cell (1, n).

Consider a concrete example. Suppose you have a simple CNF grammar with S → AB, A → a, B → b, and you want to check whether "ab" is in the language. The base cases give: cell (1,1) = {A} (because A → a) and cell (2,1) = {B} (because B → b). For the full string of length 2 starting at position 1, you try the only split: k=1 gives prefix cell (1,1) = {A} and suffix cell (2,1) = {B}. Since S → AB exists, S goes into cell (1,2). The start symbol is present, so "ab" is in the language. For real grammars with many productions, each cell may contain multiple non-terminals, and there may be many split points to check — but the process is identical, just with more bookkeeping.

The algorithm runs in **O(n³)** time because there are O(n²) cells in the table, and filling each cell requires checking O(n) possible split points. This cubic complexity is significant: it proves that membership testing for any context-free language is decidable in polynomial time — a fundamental result in formal language theory. The CYK algorithm is not the fastest parser for practical programming languages (which typically use specialized linear-time parsers), but it is the most general: it works for any context-free grammar, including ambiguous ones, and its table can be extended to recover all possible parse trees, not just a yes/no answer.
