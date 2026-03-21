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

## Questions

```yaml
- question: "What is the time complexity of the heap-building phase in heapsort (transforming an unsorted array into a max-heap)?"
  type: multiple-choice
  options:
    - "O(n log n) — each of the n elements must be sifted through up to log n levels"
    - "O(n) — most nodes are near the bottom of the heap with little or no sifting required"
    - "O(n²) — each element must be compared against all previously inserted elements"
    - "O(log n) — only the root requires a full sift-down"
  answer: 1
  explanation: "The O(n log n) intuition fails because not all nodes sift the full tree height. About half the nodes are leaves (zero sift work), a quarter are one level up, an eighth two levels up, and so on. The total work is Σ(h=0 to log n) (n/2^(h+1))·h, a convergent geometric series summing to O(n). This is the non-obvious result: even though each sift-down is O(log n), the structure of the heap ensures most sift-downs are cheap. The extraction phase — n−1 extract-max calls — is what contributes O(n log n)."

- question: "Heapsort guarantees O(n log n) worst-case performance. Why do many standard library sort implementations use quicksort-based algorithms instead?"
  type: multiple-choice
  options:
    - "Quicksort has better average-case complexity than O(n log n)"
    - "Heapsort's access pattern causes frequent cache misses, making it slower in practice despite its better worst-case guarantee"
    - "Quicksort is in-place while heapsort requires O(n) auxiliary space"
    - "Heapsort is less numerically stable than quicksort for floating-point keys"
  answer: 1
  explanation: "Heapsort's sift-down accesses parent at index i and children at 2i+1 and 2i+2. For a large heap, these are far apart in memory, causing frequent cache misses. Modern CPUs rely on spatial locality — sequential access hits the cache; random jumps don't. Quicksort's partitioning phase accesses contiguous subarrays, which fits well into cache lines. Both sort in-place with O(1) auxiliary space, so that isn't the distinction. In practice, introsort (quicksort with a heapsort fallback for worst-case protection) is the common compromise."

- question: "Heapsort is a stable sorting algorithm — equal elements preserve their relative order from the input in the sorted output."
  type: true-false
  answer: false
  explanation: "Heapsort is not stable. During extraction, the maximum element is swapped to the end of the unsorted portion, and the subsequent sift-down can move equal-valued elements past each other without tracking their original order. Stability requires that equal elements never overtake each other, which heapsort's swap-and-sift mechanism does not guarantee. When stability is required, merge sort (stable, O(n log n), but O(n) auxiliary space) is the standard alternative."

- question: "Heapsort's extraction phase runs in O(n log n) because each of the n−1 extract-max operations requires an O(log n) sift-down."
  type: true-false
  answer: true
  explanation: "After building the heap, you perform n−1 extract-max operations: swap the root with the last unsorted element, shrink the heap by one, then sift-down the new root to restore the heap property. Sift-down on a heap of size k takes O(log k). Since k decreases from n−1 to 1, total work is Σ(k=1 to n−1) log k ≈ n log n. This phase dominates the O(n) build phase, giving O(n log n) overall."

- question: "Explain why heapsort's O(n log n) worst-case guarantee comes with a real-world performance cost, using the concept of cache locality."
  type: short-answer
  answer: "Heapsort's sift-down operations access a node and its children at indices i, 2i+1, and 2i+2. For a large heap, these indices are far apart in memory — a node near the root has children near position n/2. Modern CPUs load memory in cache lines (contiguous blocks); when accesses jump across the array, each one likely misses the cache and requires a slow fetch from main memory. Quicksort's partitioning scans a contiguous subarray, keeping most accesses within the same cache lines. This cache advantage makes quicksort faster in practice despite its O(n²) worst case."
  explanation: "Big-O hides constant factors and memory access patterns, both of which matter enormously on real hardware. Cache misses can cost 100× more than cache hits. Heapsort and merge sort both offer O(n log n) guarantees but have different access patterns; merge sort is often faster than heapsort in practice despite using O(n) extra space. The lesson: theoretical complexity is necessary but not sufficient for predicting real performance."
```

## Explainer

You already know how a max-heap works: a complete binary tree where every parent is at least as large as its children, supporting insert and extract-max in O(log n) time. Heapsort exploits this structure to sort an array in-place without allocating additional memory. The algorithm has two distinct phases, and understanding why each phase has the complexity it does is the key insight.

**Phase 1: Build the heap.** Given an unsorted array, you transform it into a valid max-heap using a bottom-up process called **heapify**. Starting from the last non-leaf node and working toward the root, you "sift down" each node to restore the heap property. The critical insight — and a common source of confusion — is that this runs in O(n), not O(n log n). The reason is that most nodes are near the bottom of the tree and have very little distance to sift. Roughly half the nodes are leaves (zero work), a quarter are one level up (at most one swap), an eighth are two levels up, and so on. The sum of this geometric series converges to O(n).

**Phase 2: Repeated extraction.** Once the array is a valid max-heap, the largest element sits at index 0. You swap it with the last element of the unsorted portion, shrink the heap by one, and sift-down the new root to restore the heap property. Each extraction takes O(log n), and you perform n-1 of them, giving O(n log n) for this phase. The total is O(n) + O(n log n) = O(n log n).

Heapsort's greatest practical strength is its **guaranteed O(n log n) worst-case** performance — unlike quicksort, which degrades to O(n²) on adversarial inputs. It also sorts in-place with O(1) extra space, unlike merge sort which typically requires O(n) auxiliary storage. The tradeoff is cache performance: heapsort jumps between distant array indices during sift-down operations (parent at index i, children at 2i+1 and 2i+2), causing frequent cache misses. In practice, this makes heapsort slower than quicksort on most real-world data despite its better worst-case guarantee. For this reason, many standard library sort implementations use a hybrid like introsort — quicksort by default, falling back to heapsort only when recursion depth suggests a worst-case input.
