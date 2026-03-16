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
stage: abstract-reasoning
status: draft
---

# CYK Parsing Algorithm and CFL Membership

## Core Idea
The Cocke-Younger-Kasami (CYK) algorithm determines in O(n³) time whether a string is in a context-free language given a grammar in CNF. It uses dynamic programming, filling a table where entry (i, j) contains non-terminals that derive the substring of length j starting at position i.

## Explainer

From your work with normal forms, you know that any context-free grammar can be converted to **Chomsky Normal Form (CNF)**, where every production is either A → BC (two non-terminals) or A → a (a single terminal). The CYK algorithm exploits this rigid structure to answer the membership question — "is this string in this language?" — using dynamic programming. The key insight is that CNF's binary branching means every derivation of a substring can be split into exactly two parts, and you can systematically try all possible split points.

The algorithm builds a triangular **parse table** bottom-up. For a string w = w₁w₂...wₙ, start with the base case: for each single character wᵢ, find all non-terminals A such that A → wᵢ is a production rule, and place them in cell (i, 1). These are the non-terminals that generate substrings of length 1. Then work upward to longer substrings. For a substring of length j starting at position i, try every way to split it into two non-empty parts: a prefix of length k and a suffix of length j−k, for k = 1, 2, ..., j−1. If non-terminal B is in cell (i, k) and non-terminal C is in cell (i+k, j−k), and there exists a production A → BC, then A goes into cell (i, j). The string is in the language if and only if the start symbol S appears in cell (1, n).

Consider a concrete example. Suppose you have a simple CNF grammar with S → AB, A → a, B → b, and you want to check whether "ab" is in the language. The base cases give: cell (1,1) = {A} (because A → a) and cell (2,1) = {B} (because B → b). For the full string of length 2 starting at position 1, you try the only split: k=1 gives prefix cell (1,1) = {A} and suffix cell (2,1) = {B}. Since S → AB exists, S goes into cell (1,2). The start symbol is present, so "ab" is in the language. For real grammars with many productions, each cell may contain multiple non-terminals, and there may be many split points to check — but the process is identical, just with more bookkeeping.

The algorithm runs in **O(n³)** time because there are O(n²) cells in the table, and filling each cell requires checking O(n) possible split points. This cubic complexity is significant: it proves that membership testing for any context-free language is decidable in polynomial time — a fundamental result in formal language theory. The CYK algorithm is not the fastest parser for practical programming languages (which typically use specialized linear-time parsers), but it is the most general: it works for any context-free grammar, including ambiguous ones, and its table can be extended to recover all possible parse trees, not just a yes/no answer.
