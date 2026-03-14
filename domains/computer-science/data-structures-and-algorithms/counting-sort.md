---
id: counting-sort
title: Counting Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward:
- radix-sort
tags:
- sorting
- counting-sort
- linear-time
- non-comparison
- stable
- integer-sorting
stage: formal-systems
status: draft
---

# Counting Sort Algorithm

## Core Idea
Counting sort counts the frequency of each distinct value and uses prefix sums to determine output positions, achieving O(n + k) time where k is the value range. It beats the O(n log n) lower bound for comparison sorts, is stable, uses O(k) space, and is practical for sorting small integers or as a radix-sort subroutine.

## How It's Best Learned
Trace counting sort on a small array with limited range. Build frequency and prefix-sum arrays step-by-step. See how it avoids comparisons entirely. Understand why stability is preserved during output placement.

## Common Misconceptions
- Counting sort is always faster than O(n log n) sorts (it beats comparison sorts but for large k, it becomes impractical). - It requires O(k) space (yes, crucial for the algorithm).
