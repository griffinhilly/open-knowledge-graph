---
id: divide-conquer-recurrence-analysis
title: Divide-and-Conquer Recurrences and the Master Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: nonhomogeneous-recurrence-solutions
  type: soft
tags:
- recurrence-relations
- algorithms
stage: formal-systems
status: draft
---

# Divide-and-Conquer Recurrences and the Master Theorem

## Core Idea
Divide-and-conquer algorithms produce recurrences T(n) = aT(n/b) + f(n), where a subproblems of size n/b are solved plus f(n) work. The Master Theorem provides closed-form solutions by comparing f(n) to n^(log_b a).

## Explainer

When an algorithm divides a problem of size n into **a** subproblems each of size n/b and combines the results with f(n) additional work, its runtime satisfies the recurrence T(n) = aT(n/b) + f(n). This is the canonical form of divide-and-conquer. Merge sort, for instance, splits n elements into 2 halves, recurses on each, and merges in O(n) time — giving T(n) = 2T(n/2) + O(n). Binary search splits into 1 subproblem of half the size with O(1) comparison work — giving T(n) = T(n/2) + O(1). From your study of recurrences, you know these can be solved by unrolling or substitution; the Master Theorem gives a direct shortcut for this specific form.

The Master Theorem hinges on comparing f(n) to n^(log_b a). This quantity represents the work done at the *leaves* of the recursion tree — the total number of base-case subproblems created. The central question is: does work concentrate at the leaves, at the root, or spread evenly across all levels? **Case 1**: If f(n) is polynomially smaller than n^(log_b a) — specifically f(n) = O(n^(log_b a − ε)) for some ε > 0 — then leaf work dominates and T(n) = Θ(n^(log_b a)). **Case 2**: If f(n) ≈ n^(log_b a) (possibly with a log factor) — specifically f(n) = Θ(n^(log_b a) · logᵏ n) — then work spreads evenly and a log factor accumulates: T(n) = Θ(n^(log_b a) · logᵏ⁺¹ n). **Case 3**: If f(n) is polynomially larger — f(n) = Ω(n^(log_b a + ε)) — then root work dominates and T(n) = Θ(f(n)).

Applying this to merge sort: a = 2, b = 2, f(n) = Θ(n). So n^(log_b a) = n^(log₂ 2) = n. Since f(n) = Θ(n), Case 2 applies with k = 0, giving T(n) = Θ(n log n). For binary search: a = 1, b = 2, f(n) = Θ(1). So n^(log₂ 1) = n⁰ = 1. Since f(n) = Θ(1), Case 2 again gives T(n) = Θ(log n). Notice the theorem produces the familiar results you likely know intuitively — now with formal justification.

The recursion tree visualization makes the logic transparent. At depth k there are aᵏ nodes each doing f(n/bᵏ) work. The total work at depth k is aᵏ · f(n/bᵏ). If this product grows with k, leaf work dominates (Case 1). If it's constant, work is uniform (Case 2). If it shrinks, root work dominates (Case 3). The Master Theorem simply identifies the regime and reads off the sum. One caveat: the theorem has gaps — it doesn't cover all cases (e.g., f(n) = n/log n falls between Cases 1 and 2), and Case 3 requires an additional "regularity condition." But it handles the vast majority of divide-and-conquer recurrences encountered in practice.
