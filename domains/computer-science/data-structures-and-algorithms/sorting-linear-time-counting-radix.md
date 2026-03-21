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

## Questions

```yaml
- question: "You have 10 million employee records, each with a department code from 0 to 999. Which algorithm is most efficient for sorting by department code, and why?"
  type: multiple-choice
  options:
    - "Merge sort — it's stable and handles any key type"
    - "Quicksort — it's faster in practice than merge sort"
    - "Counting sort — the key range is small and no comparisons are needed"
    - "Heapsort — it guarantees O(n log n) in all cases"
  answer: 2
  explanation: "With only 1,000 possible values and 10 million records, counting sort runs in O(n + 1000) ≈ O(n) — effectively linear. Merge sort and quicksort cannot beat O(n log n) because they sort by comparison, and the comparison-based lower bound applies to them. This is exactly the scenario where counting sort shines: a small, known key range over a large input."

- question: "A student argues that radix sort's O(d(n+b)) time complexity means it is always faster than merge sort's O(n log n). What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Radix sort is not stable, which limits its practical use"
    - "Radix sort requires O(n²) auxiliary space"
    - "d can be large enough that d(n+b) exceeds n log n, and radix sort only works on keys with a known, finite structure — unlike merge sort"
    - "Radix sort's average case degrades to O(n log n), matching merge sort"
  answer: 2
  explanation: "The student ignores two things. First, for large keys with many digit positions, d can be large enough that d(n+b) exceeds n log n. Second, and more fundamentally, radix sort only works on keys with a known, finite structure (integers, fixed-length strings). Merge sort works on any type with a comparator. When the key constraints are met and d is small, radix sort wins; when they aren't, it can't be applied at all."

- question: "Counting sort and radix sort can achieve linear time only because they do not sort by comparing pairs of elements."
  type: true-false
  answer: true
  explanation: "True. The Ω(n log n) lower bound applies exclusively to comparison-based algorithms — any algorithm that determines order solely through pairwise comparisons requires at least n log n comparisons in the worst case. By counting occurrences or processing digit positions, counting sort and radix sort sidestep comparisons entirely and bypass the lower bound. The tradeoff is that they require structured, bounded keys."

- question: "Radix sort achieves correct results by sorting from the most significant digit to the least significant digit."
  type: true-false
  answer: false
  explanation: "False. Radix sort must process digits from least significant to most significant (LSD-first). Starting from the most significant digit would require a complex recursive or multiway partition approach. LSD-first works because each pass uses a stable sort: when you sort by a more significant digit, elements sharing the same value at that digit retain their relative order from the prior pass on the less significant digit — preserving the work already done."

- question: "Why is stability a requirement for radix sort to produce correct results?"
  type: short-answer
  answer: "Radix sort processes one digit at a time from least to most significant. After each pass, elements with the same value at the current digit position must retain their relative order from the previous pass (which established ordering by a less significant digit). If the subroutine were unstable, it would randomly reorder ties, destroying the ordering built up by prior passes. The final result would reflect only the most significant digit, ignoring all less significant digits."
  explanation: "Stability is the mechanism that carries ordering information across passes. Each pass adds one digit's worth of ordering while preserving all prior ordering for ties. Without stability, each pass overwrites rather than refines — the multi-pass structure collapses."
```

## Explainer

You already know from the comparison-based sorting lower bound that any algorithm which sorts by comparing pairs of elements requires at least O(n log n) comparisons in the worst case. But what if you don't compare elements at all? **Counting sort** and **radix sort** bypass the lower bound entirely by exploiting the structure of the keys rather than comparing them pairwise.

**Counting sort** works when your keys are integers in a known range [0, k−1]. The idea is simple: create an array of k counters, scan the input, and tally how many times each value appears. Then walk through the counter array to reconstruct the sorted output. For example, if you have the input [3, 1, 4, 1, 5] with k = 6, you build counts [0, 2, 0, 1, 1, 1] — meaning zero 0s, two 1s, zero 2s, one 3, one 4, one 5 — and read them back out as [1, 1, 3, 4, 5]. The time is O(n + k): one pass to count, one pass to output. When k is small relative to n, this is linear in n. But if k is huge (say, sorting 100 integers that range up to a billion), the counter array becomes impractically large.

This is where **radix sort** enters. Instead of sorting on the full key at once, radix sort processes one digit at a time, using a stable sort (typically counting sort) as a subroutine for each digit position. Starting from the least significant digit, it sorts all elements by that digit, then by the next digit, and so on up to the most significant digit. Stability is essential — when you sort by digit position d+1, elements with the same value at position d+1 retain their order from the previous sort on digit d. After processing all d digits, the array is fully sorted. With base b (e.g., base 10 for decimal digits, or base 256 for bytes), each digit has only b possible values, so each counting sort pass runs in O(n + b). With d digit positions, the total time is O(d(n + b)).

The practical power of radix sort appears when you choose the base wisely. For 32-bit integers, using base 256 (one byte per digit) gives d = 4 passes, each O(n + 256) — effectively O(4n), which is linear. This routinely outperforms O(n log n) comparison sorts for large arrays of integers or fixed-length strings. The tradeoff is flexibility: counting sort and radix sort require keys with a known, finite structure. They cannot sort arbitrary objects using a custom comparator the way quicksort or merge sort can. They also require O(n + k) or O(n + b) auxiliary space for the counting arrays and output buffer. When the keys fit the constraints, though, these algorithms are among the fastest practical sorting methods available.
