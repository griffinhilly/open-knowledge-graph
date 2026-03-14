---
id: selection-sort
title: Selection Sort Algorithm
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
- selection-sort
- comparison-sort
- in-place
stage: formal-systems
status: draft
---

# Selection Sort Algorithm

## Core Idea
Selection sort divides the array into sorted and unsorted regions, repeatedly finding the minimum in the unsorted region and swapping it to the end of the sorted region. It is O(n²) in all cases (best, average, worst), makes exactly n−1 swaps (minimal), and requires O(1) space. It is useful when memory writes are expensive.

## How It's Best Learned
Trace selection sort, seeing the sorted region grow one element at a time. Implement and count comparisons and swaps. Compare to insertion sort: fewer swaps but same comparison count. Understand why it's not inherently stable.

## Common Misconceptions
- Selection sort is faster than insertion sort (both O(n²); selection makes fewer swaps but insertion may be faster on nearly-sorted data). - Selection sort is stable (not inherently, though careful implementation can make it so).
