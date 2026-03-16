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

## Explainer

You already know that a binary tree organizes data hierarchically and that a queue serves elements in first-in, first-out order. A **heap** merges these ideas into something new: a binary tree where the ordering rule applies only between parents and children, not across siblings. In a **min-heap**, every parent is smaller than or equal to its children, which guarantees the smallest element is always at the root. A **max-heap** flips this so the largest element sits on top. Unlike a binary search tree, a heap makes no promise about left-versus-right ordering — it only enforces the vertical parent-child relationship. This weaker constraint is exactly what makes heaps fast for their intended purpose: quickly accessing the extreme element.

The elegant trick behind heaps is that they can be stored in a plain array rather than a tree of linked nodes. Because a heap is a **complete binary tree** — every level is fully filled except possibly the last, which fills left to right — there are no gaps in the array. For a node at index `i`, its left child is at `2i + 1`, its right child at `2i + 2`, and its parent at `⌊(i−1)/2⌋`. This index arithmetic replaces pointers entirely, giving you cache-friendly memory access and zero overhead for storing child/parent links. When you insert a new element, you place it at the end of the array (the next open leaf position) and **sift up**: compare it with its parent, swap if the heap property is violated, and repeat until it settles. When you extract the root (the min or max), you move the last element to the root and **sift down**: compare it with its children, swap with the smaller (or larger) child, and repeat. Both operations follow a single root-to-leaf or leaf-to-root path, so they run in O(log n) time — the height of the tree.

A **priority queue** is the abstract interface that heaps implement. It supports three operations: insert an element with a priority, peek at the highest-priority element in O(1), and extract (remove) the highest-priority element in O(log n). You can think of it as a queue where cutting in line is allowed based on urgency. Priority queues appear everywhere: operating system schedulers pick the highest-priority process, Dijkstra's algorithm always relaxes the nearest unvisited node, and event-driven simulations process the earliest upcoming event. In each case, the key requirement is the same — efficiently find and remove the extreme element from a dynamic collection.

One important subtlety: a heap is **not sorted**. The min-heap guarantee only means the root is the smallest — the second-smallest element could be anywhere in the second level. If you need all elements in order, you must extract them one at a time, each extraction costing O(log n), for a total of O(n log n). This is exactly what heapsort does. But if you only ever need the current minimum or maximum, a heap gives you that in constant time with logarithmic maintenance — a sweet spot that no sorted array or balanced BST matches for this specific access pattern.
