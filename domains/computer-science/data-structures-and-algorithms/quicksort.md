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
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- quicksort
- pivot
- partition
- in-place
stage: formal-systems
status: draft
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
