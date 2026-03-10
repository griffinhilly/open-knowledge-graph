---
id: binary-search-algorithm
title: Binary Search
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: soft
- id: recursion-basics
  type: soft
builds-toward:
- binary-search-trees
- divide-and-conquer-strategy
tags:
- searching
- binary-search
- divide-and-conquer
- sorted-arrays
stage: formal-systems
status: draft
---

# Binary Search

## Core Idea
Binary search finds a target value in a sorted array by repeatedly halving the search space. At each step, the algorithm compares the target to the middle element and eliminates half of the remaining candidates. This achieves O(log n) time complexity, a dramatic improvement over O(n) linear search for large datasets. Binary search requires that the input array be sorted, and the key insight is that sortedness allows drawing definitive conclusions about entire halves of the array.

## How It's Best Learned
Implement both iterative and recursive versions. Practice on concrete sorted arrays and trace through the index arithmetic step by step. Pay careful attention to off-by-one errors in the loop bounds (< vs <=, mid+1 vs mid).

## Common Misconceptions
- Binary search only works on sorted data; applying it to unsorted arrays yields incorrect results.
- Off-by-one errors in the index update are the most common source of bugs and can cause infinite loops.
- The iterative version avoids stack overflow risks for very large inputs compared to the recursive version.
