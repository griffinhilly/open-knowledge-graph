---
id: heapsort
title: Heapsort
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heaps-and-priority-queues
  type: hard
- id: time-space-complexity
  type: hard
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- heapsort
- heap
- in-place
stage: formal-systems
status: validated
---

# Heapsort

## Core Idea
Heapsort sorts an array by first building a max-heap in O(n) time, then repeatedly extracting the maximum element and placing it at the end of the array. The full algorithm runs in O(n log n) time and sorts in-place using O(1) auxiliary space. Heapsort provides guaranteed O(n log n) worst-case performance unlike quicksort. However, it exhibits poor cache performance and is not stable.

## How It's Best Learned
Implement heapsort by reusing the heap operations from a prior heap implementation. Trace through both phases (heapify the entire array, then repeatedly extract-max) on a 7-element example.

## Common Misconceptions
- The heapify phase that builds the initial heap is O(n), not O(n log n) — a non-obvious result that follows from most nodes being near the bottom of the heap.
- Heapsort is not stable, so it cannot be used where equal-element ordering matters.

## Explainer

You already know how a max-heap works: a complete binary tree where every parent is at least as large as its children, supporting insert and extract-max in O(log n) time. Heapsort exploits this structure to sort an array in-place without allocating additional memory. The algorithm has two distinct phases, and understanding why each phase has the complexity it does is the key insight.

**Phase 1: Build the heap.** Given an unsorted array, you transform it into a valid max-heap using a bottom-up process called **heapify**. Starting from the last non-leaf node and working toward the root, you "sift down" each node to restore the heap property. The critical insight — and a common source of confusion — is that this runs in O(n), not O(n log n). The reason is that most nodes are near the bottom of the tree and have very little distance to sift. Roughly half the nodes are leaves (zero work), a quarter are one level up (at most one swap), an eighth are two levels up, and so on. The sum of this geometric series converges to O(n).

**Phase 2: Repeated extraction.** Once the array is a valid max-heap, the largest element sits at index 0. You swap it with the last element of the unsorted portion, shrink the heap by one, and sift-down the new root to restore the heap property. Each extraction takes O(log n), and you perform n-1 of them, giving O(n log n) for this phase. The total is O(n) + O(n log n) = O(n log n).

Heapsort's greatest practical strength is its **guaranteed O(n log n) worst-case** performance — unlike quicksort, which degrades to O(n²) on adversarial inputs. It also sorts in-place with O(1) extra space, unlike merge sort which typically requires O(n) auxiliary storage. The tradeoff is cache performance: heapsort jumps between distant array indices during sift-down operations (parent at index i, children at 2i+1 and 2i+2), causing frequent cache misses. In practice, this makes heapsort slower than quicksort on most real-world data despite its better worst-case guarantee. For this reason, many standard library sort implementations use a hybrid like introsort — quicksort by default, falling back to heapsort only when recursion depth suggests a worst-case input.
