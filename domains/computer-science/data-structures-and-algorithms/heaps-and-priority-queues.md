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
status: validated
---

# Heaps and Priority Queues

## Core Idea
A heap is a complete binary tree satisfying the heap property: in a max-heap, every parent is greater than or equal to its children; in a min-heap, every parent is smaller. Heaps are efficiently stored in arrays using index arithmetic: the parent of node i is ⌊(i−1)/2⌋ and its children are 2i+1 and 2i+2. Insertion and deletion each run in O(log n). A priority queue is an abstract data type most commonly implemented with a heap, supporting O(log n) insertion and O(1) peek at the min/max element.

## How It's Best Learned
Implement a min-heap from scratch using an array. Carefully trace the sift-up (after insertion) and sift-down (after extraction) operations. Then use Python's heapq module and verify it matches your implementation.

## Common Misconceptions
- A heap is NOT sorted; it only guarantees the root is the min/max. Extracting all elements in order takes O(n log n).
- Array-based heap indexing differs based on whether the root is at index 0 or 1; off-by-one errors in index formulas are common.

## Questions

```yaml
- question: "You extract the minimum from a min-heap of 10 elements. What happens next in the heap's internal array representation?"
  type: multiple-choice
  options:
    - "The second-smallest element, which is always one of the root's children, automatically becomes the new root"
    - "The array is scanned linearly to find the next minimum, which is moved to index 0"
    - "The last element in the array is moved to the root position and sifted down by swapping with the smaller child until the heap property is restored"
    - "The left subtree of the root becomes the new heap, discarding the right subtree"
  answer: 2
  explanation: "After extracting the root, the heap's structural integrity must be preserved: it must remain a complete binary tree. The cleanest way to do this is to move the last element in the array (the rightmost node at the deepest level) to the root position, then sift it down — repeatedly swapping it with the smaller of its children until the heap property is restored. This takes O(log n) time. Option A is the most common misconception: the second-smallest element is NOT guaranteed to be a child of the root in a heap (siblings have no ordering relationship to each other). Option B would take O(n) time and destroy the heap structure."

- question: "In a 0-indexed min-heap stored as an array, the node at index 7 has its parent at index:"
  type: multiple-choice
  options:
    - "3"
    - "6"
    - "4"
    - "13"
  answer: 0
  explanation: "For a 0-indexed heap, the parent of node at index i is at index ⌊(i − 1) / 2⌋. For i = 7: ⌊(7 − 1) / 2⌋ = ⌊6 / 2⌋ = ⌊3⌋ = 3. The children of the node at index 3 are at indices 2×3+1 = 7 and 2×3+2 = 8, which confirms index 3 is the parent of index 7. Option B (6) would be the result of ⌊i/2⌋ (the 1-indexed formula applied incorrectly). Option C (4) is a common off-by-one error. Index arithmetic is the foundation of the array-based heap representation — getting it wrong produces silent, hard-to-debug errors."

- question: "After inserting elements into a min-heap, the array representation contains the elements in sorted order from smallest to largest."
  type: true-false
  answer: false
  explanation: "A heap is NOT sorted. The heap property only guarantees that every parent is smaller than or equal to its children — it says nothing about the relative ordering of sibling nodes or nodes at the same level. The smallest element is at the root (index 0), but the second-smallest could be anywhere among the root's children, and the third-smallest could be scattered further down. If you want elements in sorted order, you must perform heapsort: extract the minimum n times, each extraction costing O(log n), for a total of O(n log n). The misconception that heaps are sorted arrays is extremely common and leads to bugs when assuming random access to the k-th smallest element is O(1)."

- question: "A priority queue implemented as a min-heap supports O(1) access to the minimum element and O(log n) insertion and extraction."
  type: true-false
  answer: true
  explanation: "Peeking at the minimum is O(1) because the minimum is always at the root (index 0 in a 0-indexed array) — no traversal needed. Insertion is O(log n): place the new element at the end of the array, then sift up along at most one root-to-leaf path of length O(log n). Extraction of the minimum is O(log n): move the last element to the root, then sift down along a similar path. This combination — constant-time peek, log-time insert and extract — is why heaps are the standard implementation for priority queues, outperforming sorted arrays (O(n) insertion) and unsorted arrays (O(n) extraction) for the typical priority queue workload."

- question: "Why does a heap not guarantee that all elements are in sorted order, and how does this 'weak' ordering property actually make it more efficient for its intended use?"
  type: short-answer
  answer: "A heap only guarantees the heap property: every parent is ≤ (min-heap) or ≥ (max-heap) its children. This says nothing about sibling ordering or any comparison between nodes not on the same root-to-leaf path. Full sorted order would require a much stronger invariant — maintained by BSTs or sorted arrays. The weak ordering is more efficient because maintaining it requires only O(log n) work per insertion or extraction: the sift-up or sift-down operation only traverses one path from root to leaf. Maintaining full sorted order on every insertion costs O(n) in an array or O(log n) in a balanced BST, but the BST has higher constant factors and worse cache behavior. For workloads that only need the current minimum or maximum — schedulers, Dijkstra's algorithm, simulation event queues — the heap's weak guarantee is sufficient and faster to maintain."
  explanation: "The heap's design is a lesson in matching data structure complexity to the actual access pattern. If you need arbitrary access (find the 5th smallest element), a heap is the wrong structure. If you only need the extreme element repeatedly, the heap's weak invariant provides exactly what you need at minimum overhead. This principle — sufficient invariants are better than unnecessarily strong ones — appears throughout algorithm design."
```

## Explainer

You already know that a binary tree organizes data hierarchically and that a queue serves elements in first-in, first-out order. A **heap** merges these ideas into something new: a binary tree where the ordering rule applies only between parents and children, not across siblings. In a **min-heap**, every parent is smaller than or equal to its children, which guarantees the smallest element is always at the root. A **max-heap** flips this so the largest element sits on top. Unlike a binary search tree, a heap makes no promise about left-versus-right ordering — it only enforces the vertical parent-child relationship. This weaker constraint is exactly what makes heaps fast for their intended purpose: quickly accessing the extreme element.

The elegant trick behind heaps is that they can be stored in a plain array rather than a tree of linked nodes. Because a heap is a **complete binary tree** — every level is fully filled except possibly the last, which fills left to right — there are no gaps in the array. For a node at index `i`, its left child is at `2i + 1`, its right child at `2i + 2`, and its parent at `⌊(i−1)/2⌋`. This index arithmetic replaces pointers entirely, giving you cache-friendly memory access and zero overhead for storing child/parent links. When you insert a new element, you place it at the end of the array (the next open leaf position) and **sift up**: compare it with its parent, swap if the heap property is violated, and repeat until it settles. When you extract the root (the min or max), you move the last element to the root and **sift down**: compare it with its children, swap with the smaller (or larger) child, and repeat. Both operations follow a single root-to-leaf or leaf-to-root path, so they run in O(log n) time — the height of the tree.

A **priority queue** is the abstract interface that heaps implement. It supports three operations: insert an element with a priority, peek at the highest-priority element in O(1), and extract (remove) the highest-priority element in O(log n). You can think of it as a queue where cutting in line is allowed based on urgency. Priority queues appear everywhere: operating system schedulers pick the highest-priority process, Dijkstra's algorithm always relaxes the nearest unvisited node, and event-driven simulations process the earliest upcoming event. In each case, the key requirement is the same — efficiently find and remove the extreme element from a dynamic collection.

One important subtlety: a heap is **not sorted**. The min-heap guarantee only means the root is the smallest — the second-smallest element could be anywhere in the second level. If you need all elements in order, you must extract them one at a time, each extraction costing O(log n), for a total of O(n log n). This is exactly what heapsort does. But if you only ever need the current minimum or maximum, a heap gives you that in constant time with logarithmic maintenance — a sweet spot that no sorted array or balanced BST matches for this specific access pattern.
