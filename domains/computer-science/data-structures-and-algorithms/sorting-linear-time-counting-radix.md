---
id: sorting-linear-time-counting-radix
title: 'Linear-Time Sorting: Counting Sort and Radix Sort'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: sorting-comparison-based-lower-bounds
  type: hard
tags:
- sorting
- linear-time
- counting-radix
stage: formal-systems
status: draft
---

# Linear-Time Sorting: Counting Sort and Radix Sort

## Core Idea
Counting sort achieves O(n + k) time for keys in [0, k-1] by counting occurrences and rebuilding. Radix sort applies counting sort to each digit, sorting in O(d(n + b)) time for d digits and base b. Both break the comparison lower bound by exploiting key structure.

## Explainer

You already know from the comparison-based sorting lower bound that any algorithm which sorts by comparing pairs of elements requires at least O(n log n) comparisons in the worst case. But what if you don't compare elements at all? **Counting sort** and **radix sort** bypass the lower bound entirely by exploiting the structure of the keys rather than comparing them pairwise.

**Counting sort** works when your keys are integers in a known range [0, k−1]. The idea is simple: create an array of k counters, scan the input, and tally how many times each value appears. Then walk through the counter array to reconstruct the sorted output. For example, if you have the input [3, 1, 4, 1, 5] with k = 6, you build counts [0, 2, 0, 1, 1, 1] — meaning zero 0s, two 1s, zero 2s, one 3, one 4, one 5 — and read them back out as [1, 1, 3, 4, 5]. The time is O(n + k): one pass to count, one pass to output. When k is small relative to n, this is linear in n. But if k is huge (say, sorting 100 integers that range up to a billion), the counter array becomes impractically large.

This is where **radix sort** enters. Instead of sorting on the full key at once, radix sort processes one digit at a time, using a stable sort (typically counting sort) as a subroutine for each digit position. Starting from the least significant digit, it sorts all elements by that digit, then by the next digit, and so on up to the most significant digit. Stability is essential — when you sort by digit position d+1, elements with the same value at position d+1 retain their order from the previous sort on digit d. After processing all d digits, the array is fully sorted. With base b (e.g., base 10 for decimal digits, or base 256 for bytes), each digit has only b possible values, so each counting sort pass runs in O(n + b). With d digit positions, the total time is O(d(n + b)).

The practical power of radix sort appears when you choose the base wisely. For 32-bit integers, using base 256 (one byte per digit) gives d = 4 passes, each O(n + 256) — effectively O(4n), which is linear. This routinely outperforms O(n log n) comparison sorts for large arrays of integers or fixed-length strings. The tradeoff is flexibility: counting sort and radix sort require keys with a known, finite structure. They cannot sort arbitrary objects using a custom comparator the way quicksort or merge sort can. They also require O(n + k) or O(n + b) auxiliary space for the counting arrays and output buffer. When the keys fit the constraints, though, these algorithms are among the fastest practical sorting methods available.
