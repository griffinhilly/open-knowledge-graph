---
id: heap-structure-and-heapify-operations
title: Heap Structure and Heapify Operations
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-tree-structure-node-representation
  type: hard
builds-toward:
- priority-queue-implementations
- heapsort
tags:
- heap
- data-structure
- operations
stage: formal-systems
status: draft
---

# Heap Structure and Heapify Operations

## Core Idea
A heap is a complete binary tree satisfying the heap property: parent ≥ children (max-heap) or parent ≤ children (min-heap). Stored compactly in an array, heaps support O(log n) insertion and deletion, and O(1) peek.

## Explainer

From your study of binary tree structure, you know that a tree is built from nodes with left and right children, and that a **complete binary tree** fills every level except possibly the last, which is packed from left to right. A heap adds one constraint to this shape: the **heap property**, which says every parent's value must be greater than or equal to its children's values (in a max-heap) or less than or equal (in a min-heap). This is a much weaker condition than a binary search tree's ordering — siblings have no required relationship to each other — but it guarantees that the extreme element (maximum or minimum) always sits at the root, accessible in O(1) time.

The complete-tree shape enables a remarkably efficient trick: **array storage without pointers**. Number the nodes level by level, left to right, starting at index 0. Then for any node at index i, its left child is at 2i + 1, its right child at 2i + 2, and its parent at ⌊(i − 1) / 2⌋. No left/right pointer fields needed — the tree structure is implicit in the arithmetic. This saves memory and improves cache performance because elements are stored contiguously in the array.

**Insertion** works by adding the new element at the end of the array (the next position in the complete tree) and then **sifting up**: comparing it with its parent and swapping if the heap property is violated, repeating until the element finds its correct position or reaches the root. This takes O(log n) in the worst case because the tree's height is ⌊log₂ n⌋. **Deletion** of the root (extracting the max or min) replaces the root with the last element in the array, then **sifts down**: comparing the element with its children, swapping with the larger child (max-heap) or smaller child (min-heap), and repeating until the heap property is restored. Again, O(log n) work.

The most counterintuitive result is **heapify** — building a heap from an arbitrary array. The naive approach inserts elements one by one, each costing O(log n), for O(n log n) total. But the **bottom-up heapify** algorithm is faster: start from the last non-leaf node and sift down each node in reverse order. Why is this O(n) instead of O(n log n)? Because most nodes are near the bottom of the tree where sifting down costs very little — leaves need zero work, nodes one level up need at most one swap, and only the root needs O(log n) swaps. The sum of all sift-down costs across all nodes telescopes to O(n). This linear-time heap construction is what makes heapsort practical and is the foundation for efficient priority queue initialization.
