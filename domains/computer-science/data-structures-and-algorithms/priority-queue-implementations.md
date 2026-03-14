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
