---
id: insertion-sort
title: Insertion Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: algorithm-design-basics
  type: soft
- id: radix-sort
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
status: validated
---
# Insertion Sort Algorithm

## Core Idea
Insertion sort builds a sorted array by inserting each element into its correct position among the already-sorted prefix. It scans backward to find the position and shifts elements. The algorithm is O(n²) worst-case, O(n) best-case, O(1) space, stable, and efficient for small or nearly-sorted arrays due to low constant factors.

## How It's Best Learned
Trace insertion sort by hand on small arrays. Implement and test on sorted, reverse-sorted, and random data. Measure performance and compare to other O(n²) sorts. Understand why it's stable and efficient on small n.

## Common Misconceptions
- Insertion sort is O(n log n) (no, O(n²) worst-case). - It requires extra space (no, in-place with O(1) space).

## Questions

```yaml
- question: "An array of 1,000 elements has exactly 5 elements out of place. Which sorting algorithm will likely perform closest to O(n) on this input?"
  type: multiple-choice
  options:
    - "Merge sort, because it is always O(n log n) regardless of input"
    - "Insertion sort, because nearly-sorted arrays have few inversions and it removes exactly one inversion per operation"
    - "Selection sort, because it scans linearly and skips sorted regions"
    - "Heap sort, because its heapify step is optimized for small perturbations"
  answer: 1
  explanation: "Insertion sort's running time is proportional to the number of inversions in the array — pairs (i,j) where i<j but a[i]>a[j]. With only 5 elements out of place, there are at most O(n) inversions, so insertion sort runs in O(n) time on this input. Merge sort and heap sort always take O(n log n) regardless of sortedness. Selection sort is always O(n²) because it must find the minimum each pass. This is also why hybrid sorts like Timsort switch to insertion sort when subarrays become small or nearly sorted."

- question: "Why do real-world sorting libraries like Python's Timsort often switch to insertion sort for subarrays smaller than about 64 elements, even though insertion sort is O(n²)?"
  type: multiple-choice
  options:
    - "Insertion sort has lower memory usage than merge sort, which is the bottleneck at small sizes"
    - "Insertion sort is stable and Timsort requires stability throughout"
    - "At small n, insertion sort's low constant factors and cache-friendly sequential access beat the overhead of recursive O(n log n) algorithms"
    - "Insertion sort is parallelizable in ways merge sort is not"
  answer: 2
  explanation: "Big-O notation hides constant factors. Merge sort requires recursive function calls, auxiliary memory allocation, and non-sequential memory access — overhead that costs more than the algorithmic savings when n is small. Insertion sort scans sequentially, shifts elements in-place, and has almost no bookkeeping overhead. At n=16, O(n²) with tiny constants beats O(n log n) with large constants. Stability is a real property of insertion sort, but it is not why Timsort uses it for small subarrays — the primary reason is constant-factor performance."

- question: "Insertion sort runs in O(n) time when the input array is already sorted."
  type: true-false
  answer: true
  explanation: "When the array is already sorted, each element is compared once against its left neighbor, finds it is already in place, and moves on with no shifts. The total work is exactly n-1 comparisons — O(n). This is the zero-inversion case: a sorted array has no inversions, and insertion sort does work proportional to the number of inversions. The O(n) best case is unique among simple sorting algorithms — selection sort is always O(n²) because it must scan for the minimum each pass regardless of input order."

- question: "Insertion sort is always slower in practice than merge sort or quicksort, because those algorithms have better asymptotic complexity."
  type: true-false
  answer: false
  explanation: "Asymptotic notation describes growth rate, not actual speed for all inputs. Insertion sort outperforms merge sort and quicksort in two important real-world cases: (1) very small arrays (n < ~64), where insertion sort's constant factors are much lower than the recursive overhead of divide-and-conquer algorithms; and (2) nearly-sorted data, where insertion sort approaches O(n) while merge sort stays at O(n log n). This is why production sorting libraries routinely use insertion sort as the base case in hybrid algorithms — it is faster in practice for exactly these common scenarios."

- question: "What is the relationship between the number of inversions in an array and the amount of work insertion sort performs? Why does this explain its O(n) best case and O(n²) worst case?"
  type: short-answer
  answer: "An inversion is a pair (i,j) where i<j but a[i]>a[j] — an element that is ahead of something it should follow. Each comparison-and-shift in insertion sort eliminates exactly one inversion. A sorted array has zero inversions, so insertion sort finishes in O(n) time (only n-1 comparisons needed to verify). A reverse-sorted array of n elements has n(n-1)/2 inversions — the maximum — so insertion sort does O(n²) work. Any nearly-sorted array with only k inversions runs in O(n+k) time."
  explanation: "The inversion-counting perspective makes insertion sort's behavior precise rather than a vague claim that 'sorted inputs are fast.' It also connects to broader sorting theory: any algorithm that eliminates exactly one inversion per comparison cannot sort a worst-case input in fewer than O(n²) comparisons. Escaping this bound requires strategies like merge sort, which eliminates many inversions per step by merging sorted halves."
```

## Explainer

Think about how you organize a hand of playing cards. You pick up one card at a time and slide it into the right spot among the cards you're already holding. You never rearrange the whole hand from scratch — you just find where the new card belongs and insert it. That is exactly how **insertion sort** works. The algorithm maintains a sorted region at the front of the array and grows it one element at a time by taking the next unsorted element and placing it in its correct position within that sorted prefix.

Concretely, insertion sort iterates from the second element to the last. For each element (call it the **key**), it compares the key against elements in the sorted prefix, moving from right to left. Every element larger than the key gets shifted one position to the right, opening up the correct slot. The key is then placed into that slot. Because elements are shifted rather than swapped, insertion sort performs fewer writes than selection sort or bubble sort, which contributes to its low constant factors. Since elements with equal values are never reordered relative to each other, the sort is **stable** — a property that matters when sorting by multiple criteria in sequence.

The worst case occurs when the array is in reverse order: every new key must travel all the way to position zero, yielding roughly n²/2 comparisons and shifts — O(n²). The best case occurs when the array is already sorted: each key is compared once against its left neighbor, finds it's already in place, and moves on, giving O(n) total work. This best-case behavior makes insertion sort uniquely well-suited for **nearly sorted data**, where only a few elements are out of place. It also explains why many real-world sorting libraries (including Python's Timsort and Java's dual-pivot quicksort) switch to insertion sort for small subarrays — typically when n drops below 16 to 64 elements. At that scale, the low overhead of insertion sort beats the higher constant factors of more sophisticated O(n log n) algorithms.

One way to build intuition for the quadratic worst case is to count the number of **inversions** in the array — pairs (i, j) where i < j but a[i] > a[j]. Each comparison-and-shift in insertion sort fixes exactly one inversion. A reverse-sorted array of n elements has n(n−1)/2 inversions, so insertion sort does O(n²) work. A nearly sorted array has few inversions, so insertion sort runs close to O(n). This inversion-counting perspective connects insertion sort to the broader study of sorting lower bounds: any comparison-based sort that eliminates one inversion per comparison cannot beat O(n²) on worst-case inputs without a fundamentally different strategy like divide-and-conquer.
