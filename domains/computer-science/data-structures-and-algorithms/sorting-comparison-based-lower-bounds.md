---
id: sorting-comparison-based-lower-bounds
title: 'Comparison-Based Sorting: Lower Bounds and Optimality'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: asymptotic-notation-big-o-omega-theta
  type: hard
- id: sorting-lower-bounds
  type: soft
builds-toward:
- sorting-linear-time-counting-radix
tags:
- sorting
- lower-bounds
- comparison
stage: formal-systems
status: draft
---

# Comparison-Based Sorting: Lower Bounds and Optimality

## Core Idea
Any comparison-based sort requires at least Ω(n log n) comparisons in the worst case (information-theoretic lower bound: n! orderings need log₂(n!) ≈ n log n bits). Merge sort, heap sort, and quicksort (expected) achieve this bound, proving they're optimal.
