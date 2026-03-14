---
id: insertion-sort
title: Insertion Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- insertion-sort
- comparison-sort
- in-place
- stable
stage: formal-systems
status: draft
---

# Insertion Sort Algorithm

## Core Idea
Insertion sort builds a sorted array by inserting each element into its correct position among the already-sorted prefix. It scans backward to find the position and shifts elements. The algorithm is O(n²) worst-case, O(n) best-case, O(1) space, stable, and efficient for small or nearly-sorted arrays due to low constant factors.

## How It's Best Learned
Trace insertion sort by hand on small arrays. Implement and test on sorted, reverse-sorted, and random data. Measure performance and compare to other O(n²) sorts. Understand why it's stable and efficient on small n.

## Common Misconceptions
- Insertion sort is O(n log n) (no, O(n²) worst-case). - It requires extra space (no, in-place with O(1) space).
