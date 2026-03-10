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
status: draft
---

# Heapsort

## Core Idea
Heapsort sorts an array by first building a max-heap in O(n) time, then repeatedly extracting the maximum element and placing it at the end of the array. The full algorithm runs in O(n log n) time and sorts in-place using O(1) auxiliary space. Heapsort provides guaranteed O(n log n) worst-case performance unlike quicksort. However, it exhibits poor cache performance and is not stable.

## How It's Best Learned
Implement heapsort by reusing the heap operations from a prior heap implementation. Trace through both phases (heapify the entire array, then repeatedly extract-max) on a 7-element example.

## Common Misconceptions
- The heapify phase that builds the initial heap is O(n), not O(n log n) — a non-obvious result that follows from most nodes being near the bottom of the heap.
- Heapsort is not stable, so it cannot be used where equal-element ordering matters.
