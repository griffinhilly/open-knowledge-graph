---
id: heaps-and-priority-queues
title: Heaps and Priority Queues
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: hard
- id: queues-data-structure
  type: hard
- id: time-space-complexity
  type: soft
builds-toward:
- heapsort
- dijkstras-algorithm
- greedy-algorithms
tags:
- heap
- priority-queue
- min-heap
- max-heap
- heapify
stage: formal-systems
status: draft
---

# Heaps and Priority Queues

## Core Idea
A heap is a complete binary tree satisfying the heap property: in a max-heap, every parent is greater than or equal to its children; in a min-heap, every parent is smaller. Heaps are efficiently stored in arrays using index arithmetic: the parent of node i is ⌊(i−1)/2⌋ and its children are 2i+1 and 2i+2. Insertion and deletion each run in O(log n). A priority queue is an abstract data type most commonly implemented with a heap, supporting O(log n) insertion and O(1) peek at the min/max element.

## How It's Best Learned
Implement a min-heap from scratch using an array. Carefully trace the sift-up (after insertion) and sift-down (after extraction) operations. Then use Python's heapq module and verify it matches your implementation.

## Common Misconceptions
- A heap is NOT sorted; it only guarantees the root is the min/max. Extracting all elements in order takes O(n log n).
- Array-based heap indexing differs based on whether the root is at index 0 or 1; off-by-one errors in index formulas are common.
