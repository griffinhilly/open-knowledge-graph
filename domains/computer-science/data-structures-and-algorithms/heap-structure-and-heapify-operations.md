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

## Questions

```yaml
- question: "A student builds a max-heap from 1,000 elements by inserting them one at a time (each via sift-up). A colleague builds the same heap using bottom-up heapify. The student claims both approaches take O(n log n). Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — both methods require O(log n) work per element in the worst case"
    - "No — bottom-up heapify runs in O(n) because nodes near the bottom of the tree require little or no sift-down work"
    - "No — insertion-based construction is faster because sift-up terminates early on average"
    - "Yes — the difference is only in the constant factor, not the asymptotic complexity class"
  answer: 1
  explanation: "Bottom-up heapify processes nodes from the last internal node up to the root, sifting each one down. Leaves (roughly half the nodes) need zero work. Nodes one level above leaves need at most one swap. Only the root needs O(log n) swaps. Summing across all levels gives a geometric series that converges to O(n). Insertion-based construction sifts each new element up from the bottom, paying up to O(log n) for every one of n elements, for O(n log n) total."

- question: "For a max-heap stored in a 0-indexed array, a node at index 3 is best described as:"
  type: multiple-choice
  options:
    - "The fourth-largest element, since the array is partially sorted"
    - "The left child of the node at index 1"
    - "The right child of the node at index 1"
    - "A node at depth 2 whose value is at least as large as its children but has no required ordering relative to its sibling"
  answer: 3
  explanation: "In a 0-indexed array heap, the left child of node i is at 2i+1 and the right child is at 2i+2. Node at index 3 is the left child of index 1 (2×1+1 = 3). Its structural position is fixed (depth 2, left subtree), and the heap property guarantees its parent (index 1) is ≥ it. But its sibling at index 4 has no required ordering relationship — siblings in a heap can be in any relative order. The array index tells you structure, not rank among all elements."

- question: "The heap property is weaker than the binary search tree property because siblings in a heap have no required ordering relative to each other."
  type: true-false
  answer: true
  explanation: "In a BST, every node in a left subtree is less than the root, and every node in a right subtree is greater — a global left-to-right ordering. The heap property only requires that each parent is ≥ (max-heap) or ≤ (min-heap) its direct children. Two siblings can be in any order. This weaker invariant is sufficient to guarantee the extreme element at the root in O(1), while enabling efficient O(n) construction via bottom-up heapify."

- question: "Deleting an arbitrary element (not the root) from a heap can be done in O(1) time."
  type: true-false
  answer: false
  explanation: "Heaps only provide O(1) access to the root. Finding an arbitrary non-root element requires an O(n) scan (there is no search structure like a BST's ordering). Once found, restoring the heap property after deletion requires sifting up or down — O(log n) additional work. Only root deletion (extract-max or extract-min) is efficiently O(log n) as a full operation, because the root is immediately accessible."

- question: "Why is bottom-up heapify O(n) when inserting elements one at a time takes O(n log n)?"
  type: short-answer
  answer: "Bottom-up heapify sifts each node DOWN, and nodes near the bottom of the tree — which is most nodes — have very little room to sift down. In an n-node heap, roughly n/2 nodes are leaves (0 swaps needed), n/4 need at most 1 swap, n/8 need at most 2, and so on. The total work is n/2 × 0 + n/4 × 1 + n/8 × 2 + ⋯, a geometric series that sums to O(n). Insertion-based construction pays up to log n for each of n elements because it sifts UP from the bottom, where most new elements start."
  explanation: "The key asymmetry is which direction you sift. Sifting down from the top costs O(log n) at the top but almost nothing near the leaves. Since most nodes in a complete binary tree are near the leaves, bottom-up heapify exploits where the work is cheap. Top-down insertion always starts at the bottom and pays full log n cost regardless of position."
```

## Explainer

From your study of binary tree structure, you know that a tree is built from nodes with left and right children, and that a **complete binary tree** fills every level except possibly the last, which is packed from left to right. A heap adds one constraint to this shape: the **heap property**, which says every parent's value must be greater than or equal to its children's values (in a max-heap) or less than or equal (in a min-heap). This is a much weaker condition than a binary search tree's ordering — siblings have no required relationship to each other — but it guarantees that the extreme element (maximum or minimum) always sits at the root, accessible in O(1) time.

The complete-tree shape enables a remarkably efficient trick: **array storage without pointers**. Number the nodes level by level, left to right, starting at index 0. Then for any node at index i, its left child is at 2i + 1, its right child at 2i + 2, and its parent at ⌊(i − 1) / 2⌋. No left/right pointer fields needed — the tree structure is implicit in the arithmetic. This saves memory and improves cache performance because elements are stored contiguously in the array.

**Insertion** works by adding the new element at the end of the array (the next position in the complete tree) and then **sifting up**: comparing it with its parent and swapping if the heap property is violated, repeating until the element finds its correct position or reaches the root. This takes O(log n) in the worst case because the tree's height is ⌊log₂ n⌋. **Deletion** of the root (extracting the max or min) replaces the root with the last element in the array, then **sifts down**: comparing the element with its children, swapping with the larger child (max-heap) or smaller child (min-heap), and repeating until the heap property is restored. Again, O(log n) work.

The most counterintuitive result is **heapify** — building a heap from an arbitrary array. The naive approach inserts elements one by one, each costing O(log n), for O(n log n) total. But the **bottom-up heapify** algorithm is faster: start from the last non-leaf node and sift down each node in reverse order. Why is this O(n) instead of O(n log n)? Because most nodes are near the bottom of the tree where sifting down costs very little — leaves need zero work, nodes one level up need at most one swap, and only the root needs O(log n) swaps. The sum of all sift-down costs across all nodes telescopes to O(n). This linear-time heap construction is what makes heapsort practical and is the foundation for efficient priority queue initialization.
