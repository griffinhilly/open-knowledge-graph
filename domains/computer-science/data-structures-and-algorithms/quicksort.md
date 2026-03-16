---
id: quicksort
title: Quicksort
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: divide-and-conquer-strategy
  type: hard
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: hard
- id: divide-and-conquer-recurrences
  type: soft
- id: big-o-notation
  type: soft
- id: expected-value-and-variance
  type: soft
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- quicksort
- pivot
- partition
- in-place
stage: formal-systems
status: validated
---

# Quicksort

## Core Idea
Quicksort partitions an array around a pivot element such that smaller elements precede the pivot and larger elements follow, then recursively sorts each partition. With a good pivot (random or median-of-three), the expected time complexity is O(n log n) and the algorithm sorts in-place using O(log n) stack space. A bad pivot choice, such as always picking the minimum on a sorted array, yields O(n²) worst-case behavior. Quicksort is typically faster in practice than merge sort due to better cache locality.

## How It's Best Learned
Implement both the Lomuto and Hoare partition schemes and compare them. Test on sorted, reverse-sorted, and random inputs. Study how random pivot selection mitigates worst-case behavior.

## Common Misconceptions
- Quicksort's average case is O(n log n), not its guaranteed worst case; always randomize the pivot for production use.
- Quicksort is not stable — equal elements may be reordered.
- 'In-place' means no extra array space is needed, but quicksort still uses O(log n) stack space for recursion.

## Explainer

Quicksort is the canonical example of divide-and-conquer applied to sorting. The strategy you learned in divide-and-conquer — break the problem into smaller subproblems, solve them recursively, combine the results — takes a specific form here: **partitioning** does all the real work up front, and the "combine" step is trivial because the subarrays are already in the right positions.

The algorithm picks a **pivot** element, then rearranges the array so that everything less than the pivot comes before it and everything greater comes after it. After partitioning, the pivot is in its final sorted position. Recursively sort the left and right subarrays, and you're done — no merging needed. The Lomuto partition scheme walks a single pointer through the array, swapping elements smaller than the pivot to the front. The Hoare scheme uses two pointers converging from opposite ends, which typically performs fewer swaps. Both achieve the same goal: placing the pivot and separating smaller from larger elements.

The efficiency of quicksort depends almost entirely on pivot quality. If the pivot lands near the median, you get two roughly equal subarrays, the recursion tree has depth O(log n), and each level does O(n) work — giving O(n log n) total. If the pivot is consistently the smallest or largest element (imagine sorting an already-sorted array with the first element as pivot), one subarray is empty and the other has n−1 elements. The recursion tree degenerates to depth n, and total work becomes O(n²). **Randomized pivot selection** — picking a uniformly random element as the pivot — makes the expected number of comparisons about 1.39n log n regardless of input order, which is why production implementations always randomize.

Quicksort's practical speed advantage over merge sort comes from **cache locality**. Quicksort operates on a contiguous block of memory, accessing elements sequentially and swapping in-place. Merge sort, by contrast, copies elements between arrays during the merge step, which causes more cache misses. This constant-factor advantage makes quicksort faster on real hardware despite both algorithms having O(n log n) expected time. The tradeoff is that quicksort is **not stable** — equal elements may be reordered during partitioning — and its worst case is quadratic. When worst-case guarantees matter more than average-case speed, merge sort or heapsort may be preferable.
