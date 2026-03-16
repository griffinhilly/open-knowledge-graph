---
id: insertion-sort
title: Insertion Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward:
- sorting-lower-bounds
tags:
- sorting
- insertion-sort
- comparison-sort
- in-place
- stable
stage: formal-systems
status: draft
---

# Insertion Sort Algorithm

## Core Idea
Insertion sort builds a sorted array by inserting each element into its correct position among the already-sorted prefix. It scans backward to find the position and shifts elements. The algorithm is O(n²) worst-case, O(n) best-case, O(1) space, stable, and efficient for small or nearly-sorted arrays due to low constant factors.

## How It's Best Learned
Trace insertion sort by hand on small arrays. Implement and test on sorted, reverse-sorted, and random data. Measure performance and compare to other O(n²) sorts. Understand why it's stable and efficient on small n.

## Common Misconceptions
- Insertion sort is O(n log n) (no, O(n²) worst-case). - It requires extra space (no, in-place with O(1) space).

## Explainer

Think about how you organize a hand of playing cards. You pick up one card at a time and slide it into the right spot among the cards you're already holding. You never rearrange the whole hand from scratch — you just find where the new card belongs and insert it. That is exactly how **insertion sort** works. The algorithm maintains a sorted region at the front of the array and grows it one element at a time by taking the next unsorted element and placing it in its correct position within that sorted prefix.

Concretely, insertion sort iterates from the second element to the last. For each element (call it the **key**), it compares the key against elements in the sorted prefix, moving from right to left. Every element larger than the key gets shifted one position to the right, opening up the correct slot. The key is then placed into that slot. Because elements are shifted rather than swapped, insertion sort performs fewer writes than selection sort or bubble sort, which contributes to its low constant factors. Since elements with equal values are never reordered relative to each other, the sort is **stable** — a property that matters when sorting by multiple criteria in sequence.

The worst case occurs when the array is in reverse order: every new key must travel all the way to position zero, yielding roughly n²/2 comparisons and shifts — O(n²). The best case occurs when the array is already sorted: each key is compared once against its left neighbor, finds it's already in place, and moves on, giving O(n) total work. This best-case behavior makes insertion sort uniquely well-suited for **nearly sorted data**, where only a few elements are out of place. It also explains why many real-world sorting libraries (including Python's Timsort and Java's dual-pivot quicksort) switch to insertion sort for small subarrays — typically when n drops below 16 to 64 elements. At that scale, the low overhead of insertion sort beats the higher constant factors of more sophisticated O(n log n) algorithms.

One way to build intuition for the quadratic worst case is to count the number of **inversions** in the array — pairs (i, j) where i < j but a[i] > a[j]. Each comparison-and-shift in insertion sort fixes exactly one inversion. A reverse-sorted array of n elements has n(n−1)/2 inversions, so insertion sort does O(n²) work. A nearly sorted array has few inversions, so insertion sort runs close to O(n). This inversion-counting perspective connects insertion sort to the broader study of sorting lower bounds: any comparison-based sort that eliminates one inversion per comparison cannot beat O(n²) on worst-case inputs without a fundamentally different strategy like divide-and-conquer.
