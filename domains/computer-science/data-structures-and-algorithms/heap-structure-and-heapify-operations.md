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
