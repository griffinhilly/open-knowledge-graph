---
id: divide-conquer-recurrence-analysis
title: Divide-and-Conquer Recurrences and the Master Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: nonhomogeneous-recurrence-solutions
  type: soft
- id: dijkstra-algorithm
  type: soft
- id: topological-sorting
  type: soft
tags:
- recurrence-relations
- algorithms
stage: formal-systems
status: validated
---
# Divide-and-Conquer Recurrences and the Master Theorem

## Core Idea
Divide-and-conquer algorithms produce recurrences T(n) = aT(n/b) + f(n), where a subproblems of size n/b are solved plus f(n) work. The Master Theorem provides closed-form solutions by comparing f(n) to n^(log_b a).

## Questions

```yaml
- question: "An algorithm divides a problem of size n into 9 subproblems each of size n/3 and does O(n) combining work. Which case of the Master Theorem applies, and what is the runtime?"
  type: multiple-choice
  options:
    - "Case 2: T(n) = Θ(n log n) because the combining work and leaf work are similar"
    - "Case 1: T(n) = Θ(n²) because n^(log₃ 9) = n² dominates f(n) = n"
    - "Case 3: T(n) = Θ(n) because the combining work f(n) = O(n) dominates at the root"
    - "Case 1: T(n) = Θ(n) because f(n) = O(n) is already a simple expression"
  answer: 1
  explanation: "Here a=9, b=3, so n^(log₃ 9) = n². Since f(n) = Θ(n) is polynomially smaller than n² (by ε=1), Case 1 applies: leaf work dominates and T(n) = Θ(n²). Option C is the classic confusion: the root does O(n) work, but the leaves collectively do Θ(n²) work total — which is far more. Option A might feel right because n and n² are 'in the same ballpark,' but Case 2 requires f(n) ≈ n^(log_b a), and n is polynomially — not just logarithmically — smaller than n²."

- question: "For merge sort, a=2, b=2, f(n)=Θ(n), and n^(log₂ 2)=n. The Master Theorem gives T(n)=Θ(n log n). What does the recursion tree tell us about WHY a log factor appears?"
  type: multiple-choice
  options:
    - "The log factor comes from the tree's height: work is distributed uniformly across all O(log n) levels, each doing Θ(n) total work"
    - "The log factor appears because f(n) is too large for Case 1 but not large enough for Case 3, so extra counting is needed"
    - "The log factor comes because leaf work (Θ(n)) exceeds root work, requiring an adjustment term"
    - "The log factor accounts for memory allocation overhead at each recursive call level"
  answer: 0
  explanation: "Case 2 applies when f(n) ≈ n^(log_b a) — work spreads evenly across every level of the recursion tree. Merge sort's tree has Θ(log n) levels, and each level does Θ(n) total work (n/2 merges at depth 1, n/4 + n/4 at depth 2, etc., each level summing to n). Multiply: Θ(n) × Θ(log n) = Θ(n log n). The log factor is literally the height of the tree. Option B is a description of the theorem's boundary conditions, not an explanation of where the log comes from geometrically."

- question: "The quantity n^(log_b a) in the Master Theorem represents the total work done at the root of the recursion tree."
  type: true-false
  answer: false
  explanation: "n^(log_b a) = a^(log_b n) is the number of leaf nodes in the recursion tree — it represents the total base-case work at the leaves, not the root's work. The root does f(n) work. This distinction is exactly what the three cases capture: Case 1 means leaves dominate (n^(log_b a) > f(n)), Case 3 means root dominates (f(n) > n^(log_b a)), and Case 2 means they balance. Confusing the leaf count with root work reverses the meaning of Cases 1 and 3."

- question: "If T(n) = 2T(n/2) + Θ(n²), Case 3 of the Master Theorem applies because f(n) = Θ(n²) is polynomially larger than n^(log₂ 2) = n."
  type: true-false
  answer: true
  explanation: "n^(log₂ 2) = n¹ = n. Since f(n) = Θ(n²) = Ω(n^(1+1)), the polynomially-larger condition for Case 3 is satisfied (with ε=1). The regularity condition also holds: a·f(n/b) = 2·(n/2)² = n²/2 ≤ (1/2)·n², satisfying af(n/b) ≤ cf(n) for c=1/2 < 1. So T(n) = Θ(n²) — the combining step is the bottleneck, and all the recursive work is negligible by comparison."

- question: "Explain the core intuition behind the Master Theorem's three cases using the recursion tree. What is the theorem really asking?"
  type: short-answer
  answer: "The recursion tree has O(log_b n) levels. At each depth k, there are a^k nodes each doing f(n/b^k) work. The per-level total is a^k · f(n/b^k). The Master Theorem asks: does this per-level work grow (leaves dominate → Case 1), stay constant (uniform spread → Case 2), or shrink (root dominates → Case 3) as you go deeper?"
  explanation: "Seeing the cases geometrically removes the mystery. Case 1: work concentrates at the leaves — the recursion fans out into many small subproblems. Case 2: work is even across O(log n) levels, so you pick up exactly one log factor. Case 3: work concentrates at the root — the combining step is the expensive part, and recursive calls add only constant overhead. The comparison f(n) vs. n^(log_b a) is a shortcut for determining which regime applies, but the recursion tree picture shows *why* each regime gives the answer it does."
```

## Explainer

When an algorithm divides a problem of size n into **a** subproblems each of size n/b and combines the results with f(n) additional work, its runtime satisfies the recurrence T(n) = aT(n/b) + f(n). This is the canonical form of divide-and-conquer. Merge sort, for instance, splits n elements into 2 halves, recurses on each, and merges in O(n) time — giving T(n) = 2T(n/2) + O(n). Binary search splits into 1 subproblem of half the size with O(1) comparison work — giving T(n) = T(n/2) + O(1). From your study of recurrences, you know these can be solved by unrolling or substitution; the Master Theorem gives a direct shortcut for this specific form.

The Master Theorem hinges on comparing f(n) to n^(log_b a). This quantity represents the work done at the *leaves* of the recursion tree — the total number of base-case subproblems created. The central question is: does work concentrate at the leaves, at the root, or spread evenly across all levels? **Case 1**: If f(n) is polynomially smaller than n^(log_b a) — specifically f(n) = O(n^(log_b a − ε)) for some ε > 0 — then leaf work dominates and T(n) = Θ(n^(log_b a)). **Case 2**: If f(n) ≈ n^(log_b a) (possibly with a log factor) — specifically f(n) = Θ(n^(log_b a) · logᵏ n) — then work spreads evenly and a log factor accumulates: T(n) = Θ(n^(log_b a) · logᵏ⁺¹ n). **Case 3**: If f(n) is polynomially larger — f(n) = Ω(n^(log_b a + ε)) — then root work dominates and T(n) = Θ(f(n)).

Applying this to merge sort: a = 2, b = 2, f(n) = Θ(n). So n^(log_b a) = n^(log₂ 2) = n. Since f(n) = Θ(n), Case 2 applies with k = 0, giving T(n) = Θ(n log n). For binary search: a = 1, b = 2, f(n) = Θ(1). So n^(log₂ 1) = n⁰ = 1. Since f(n) = Θ(1), Case 2 again gives T(n) = Θ(log n). Notice the theorem produces the familiar results you likely know intuitively — now with formal justification.

The recursion tree visualization makes the logic transparent. At depth k there are aᵏ nodes each doing f(n/bᵏ) work. The total work at depth k is aᵏ · f(n/bᵏ). If this product grows with k, leaf work dominates (Case 1). If it's constant, work is uniform (Case 2). If it shrinks, root work dominates (Case 3). The Master Theorem simply identifies the regime and reads off the sum. One caveat: the theorem has gaps — it doesn't cover all cases (e.g., f(n) = n/log n falls between Cases 1 and 2), and Case 3 requires an additional "regularity condition." But it handles the vast majority of divide-and-conquer recurrences encountered in practice.
