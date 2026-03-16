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
- id: divide-and-conquer-recurrences
  type: soft
- id: big-o-notation
  type: soft
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- merge-sort
- divide-and-conquer
- stable-sort
stage: formal-systems
status: validated
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

## Explainer

You already understand divide-and-conquer: break a problem into smaller subproblems, solve each recursively, and combine the results. Merge sort is the textbook application of this strategy to sorting. The key insight is that merging two already-sorted arrays into one sorted array is easy and fast — you just compare the front elements of each array and take the smaller one, repeating until both are exhausted. If you can produce sorted halves, combining them is an O(n) operation.

The algorithm works recursively. Given an array of n elements, split it into two halves of roughly equal size. Recursively sort the left half. Recursively sort the right half. Then **merge** the two sorted halves. The base case is an array of one element, which is trivially sorted. Picture the recursion as a tree: an 8-element array splits into two 4-element arrays, each splits into two 2-element arrays, each splits into two singletons. That's log₂(n) levels of splitting. At each level, the total merge work across all subproblems is O(n) — every element participates in exactly one merge at each level. So the total work is O(n log n), and this holds regardless of the input order. There is no "worst case" that degrades performance, unlike quicksort's O(n²) worst case.

The merge step requires a temporary array to hold the merged result, giving merge sort O(n) **auxiliary space** complexity. This is its main tradeoff compared to in-place sorts like quicksort or heapsort. However, merge sort has a crucial property those algorithms lack: **stability**. A stable sort preserves the relative order of elements with equal keys. If you sort a list of students by grade and two students both have a B+, they stay in whatever order they were in before the sort. This matters when sorting by multiple criteria — sort by name first, then by grade, and students with the same grade remain alphabetically ordered.

Merge sort also shines in two settings where other sorts struggle. For **linked lists**, the merge step can be done in-place by relinking pointers, eliminating the space overhead entirely. For **external sorting** — when data is too large to fit in memory — merge sort's sequential access pattern (reading and writing long runs) maps naturally onto disk I/O. You sort chunks that fit in memory, write them to disk, then merge the sorted chunks. This is why most database systems and many standard library sorts (like Python's Timsort, which is a hybrid merge-insertion sort) are built on merge sort's foundation.
