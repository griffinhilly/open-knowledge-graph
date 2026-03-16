---
id: priority-queue-implementations
title: 'Priority Queues: Heap-Based and Binary Search Tree Implementations'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heap-structure-and-heapify-operations
  type: hard
builds-toward:
- dijkstras-algorithm
- astar-search-algorithm
tags:
- priority-queue
- heap
- queue
stage: formal-systems
status: draft
---

# Priority Queues: Heap-Based and Binary Search Tree Implementations

## Core Idea
A priority queue supports extracting elements by priority, not insertion order. Heap-based implementations are efficient (O(log n) insert/extract) and space-efficient. BST-based versions offer O(log n) operations too but with higher overhead.

## Explainer

A **priority queue** is an abstract data type where each element has an associated priority, and the operation you care most about is "give me the highest-priority element." Unlike a regular queue where the first item in is the first out, a priority queue always serves the most urgent item first, regardless of when it arrived. The question is: what concrete data structure should back this abstraction?

The dominant answer is a **binary heap**, which you studied in heap structure and heapify operations. A min-heap keeps the smallest element at the root; a max-heap keeps the largest. Insertion works by placing the new element at the bottom of the heap and "bubbling up" — comparing with its parent and swapping until the heap property is restored. Extraction removes the root, moves the last element to the root position, and "bubbles down" — swapping with the smaller (or larger) child until the heap property holds again. Both operations are O(log n) because the heap is a complete binary tree with height log n. Crucially, heaps are stored in a flat array with no pointer overhead: the children of element at index i live at indices 2i+1 and 2i+2. This compact layout gives excellent cache performance and makes heaps the default choice for priority queues in practice.

A **balanced binary search tree** (like a red-black tree or AVL tree) can also implement a priority queue: the minimum is always the leftmost node, extractable in O(log n), and insertion is O(log n). BSTs additionally support operations that heaps cannot efficiently provide — finding an arbitrary element, deleting by value, or iterating in sorted order. However, BSTs carry per-node pointer overhead (left child, right child, parent, balance metadata), worse cache locality due to scattered memory allocation, and more complex rebalancing logic. If all you need is insert and extract-min, this extra machinery is wasted.

The choice between implementations reduces to what operations you need. If your workload is purely "insert elements, extract the best one," a binary heap wins on simplicity, memory, and constant factors. If you also need to search for or delete arbitrary elements by value — as in some scheduling algorithms — a BST or an augmented heap (like an indexed priority queue) is worth the overhead. Algorithms like Dijkstra's shortest path and A* search rely heavily on priority queues, performing one extract-min and potentially many decrease-key operations per iteration, which is why the efficiency of the underlying heap directly determines the algorithm's practical speed.
