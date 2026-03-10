---
id: divide-and-conquer-recurrences
title: Divide-and-Conquer and the Master Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations
  type: hard
- id: big-o-notation
  type: hard
- id: solving-linear-recurrences
  type: soft
tags:
- master-theorem
- divide-and-conquer
- merge-sort
- recurrences
- algorithm-analysis
stage: formal-systems
status: draft
---

# Divide-and-Conquer and the Master Theorem

## Core Idea
Divide-and-conquer algorithms split a size-n problem into a subproblems of size n/b and combine results in O(nᵈ) time, yielding the recurrence T(n) = aT(n/b) + O(nᵈ). The Master Theorem gives the asymptotic solution: T(n) = Θ(nᵈ log n) if a = bᵈ, Θ(nᵈ) if a < bᵈ, and Θ(n^(log_b a)) if a > bᵈ. This covers merge sort (a=2, b=2, d=1 → Θ(n log n)), binary search (a=1, b=2, d=0 → Θ(log n)), and Strassen's matrix multiplication algorithm. The theorem is the primary tool for analyzing recursive algorithms.

## How It's Best Learned
Apply the Master Theorem to 5-6 concrete recurrences before studying its proof. Verify each case against the recursion tree: draw the tree, compute work at each level, and sum across levels. Derive merge sort's complexity both via the theorem and by directly expanding the recursion tree.

## Common Misconceptions
- Applying the Master Theorem when the combine cost does not fit the polynomial O(nᵈ) form (e.g., when combine cost has logarithmic factors).
- Forgetting to check that a ≥ 1, b > 1, and d ≥ 0 for valid application.
