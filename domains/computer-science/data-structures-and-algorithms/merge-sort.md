---
id: merge-sort
title: Merge Sort
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: divide-and-conquer-strategy
  type: hard
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: hard
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- merge-sort
- divide-and-conquer
- stable-sort
stage: formal-systems
status: draft
---

# Merge Sort

## Core Idea
Merge sort is a divide-and-conquer algorithm that recursively splits an array into halves, sorts each half, and merges the sorted halves. The merge step, which combines two sorted arrays in O(n) time, is the core operation. The overall time complexity is O(n log n) in all cases, making it more predictable than quicksort. Merge sort is stable (equal elements retain their original order) and well-suited to linked lists and external sorting where data does not fit in memory.

## How It's Best Learned
Implement the merge function first in isolation, then build the recursive mergeSort on top of it. Trace through an 8-element example drawing the full recursion tree and each merge step explicitly.

## Common Misconceptions
- Merge sort requires O(n) auxiliary space for the merge step, unlike in-place sorts.
- Bottom-up (iterative) merge sort avoids recursion overhead and is used in many standard library implementations (e.g., Python's Timsort).
- Merge sort's stability is a significant practical advantage when sorting records by multiple keys.
