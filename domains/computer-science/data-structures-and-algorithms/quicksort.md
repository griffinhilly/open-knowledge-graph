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
- id: big-o-complexity-analysis
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

## Questions

```yaml
- question: "A programmer implements quicksort using the first element as pivot, then runs it on 10,000 names already in alphabetical order. What is the likely time complexity, and why?"
  type: multiple-choice
  options:
    - "O(n log n) — sorted input is the best case for quicksort"
    - "O(n²) — the pivot is always the minimum, producing maximally unbalanced partitions"
    - "O(n) — the partition step recognizes the array is sorted and skips work"
    - "O(n log n) regardless — quicksort's performance doesn't depend on pivot choice"
  answer: 1
  explanation: "On a sorted array with the first element as pivot, the pivot is always the minimum. After each partition the left subarray is empty and the right has n−1 elements. The recursion tree degenerates to depth n rather than log n, and total comparisons become 1 + 2 + ... + n = O(n²). This is quicksort's worst case. Randomized pivot selection prevents this by making it overwhelmingly unlikely to consistently pick near-extreme pivots, regardless of input order."

- question: "Quicksort and merge sort both have O(n log n) average-case complexity. In practice, quicksort is often faster on large arrays. What best explains this?"
  type: multiple-choice
  options:
    - "Quicksort makes fewer comparisons than merge sort in all cases"
    - "Quicksort operates in-place on a contiguous memory block, producing better CPU cache performance"
    - "Quicksort's recursion is shallower because it uses three-way partitioning by default"
    - "Merge sort has O(n²) worst case, making its average performance slower"
  answer: 1
  explanation: "Quicksort's practical advantage is cache locality. It swaps elements within a single contiguous array, so memory accesses are sequential and cache-friendly. Merge sort copies elements between arrays during merging, causing more cache misses on real hardware. Both algorithms have O(n log n) average complexity. Merge sort's worst case is actually O(n log n) — better than quicksort's O(n²) worst case. The advantage is a constant-factor difference in average performance due to memory access patterns."

- question: "Randomized quicksort achieves O(n log n) expected running time on any input, but this is a probabilistic expectation — not a worst-case guarantee."
  type: true-false
  answer: true
  explanation: "True. Randomized quicksort picks a pivot uniformly at random. The expected number of comparisons is about 1.39n log n regardless of input order. However, there is a small (but nonzero) probability that random pivot choices are consistently bad on any given run, producing O(n²) behavior. For worst-case guarantees, algorithms like merge sort or heapsort are needed."

- question: "Quicksort is called 'in-place' because it requires no additional memory beyond the input array, giving it O(1) space complexity."
  type: true-false
  answer: false
  explanation: "False. 'In-place' means no extra array is allocated for elements, but quicksort still uses O(log n) stack space for recursive calls. Each recursion level adds a frame tracking partition boundaries and the pivot. With balanced splits (good pivot), recursion depth is O(log n). In the worst case (unbalanced splits), stack depth reaches O(n). So quicksort's space complexity is O(log n) expected — not O(1)."

- question: "Explain why choosing the first element as pivot performs poorly on already-sorted arrays, and how randomized pivot selection fixes this."
  type: short-answer
  answer: "On a sorted array, the first element is always the minimum. After partitioning, the left subarray is empty and the right has n−1 elements — the worst possible split. This repeats at every level: the recursion tree has depth n instead of log n, and total work is O(n²). Randomized pivot selection picks a pivot uniformly at random, making it extremely unlikely to consistently choose near-extreme elements. The expected split is balanced enough that recursion depth is O(log n), giving O(n log n) expected time regardless of input order."
  explanation: "The intuition: a random pivot lands in the middle 50% of elements with probability 1/2, producing a split no worse than 75%/25%. When roughly half of all pivots are 'good' splits, the recursion tree height is O(log n) in expectation. The resulting expected comparison count is about 1.39n log n — only 39% above the theoretical minimum for comparison-based sorting."
```

## Explainer

Quicksort is the canonical example of divide-and-conquer applied to sorting. The strategy you learned in divide-and-conquer — break the problem into smaller subproblems, solve them recursively, combine the results — takes a specific form here: **partitioning** does all the real work up front, and the "combine" step is trivial because the subarrays are already in the right positions.

The algorithm picks a **pivot** element, then rearranges the array so that everything less than the pivot comes before it and everything greater comes after it. After partitioning, the pivot is in its final sorted position. Recursively sort the left and right subarrays, and you're done — no merging needed. The Lomuto partition scheme walks a single pointer through the array, swapping elements smaller than the pivot to the front. The Hoare scheme uses two pointers converging from opposite ends, which typically performs fewer swaps. Both achieve the same goal: placing the pivot and separating smaller from larger elements.

The efficiency of quicksort depends almost entirely on pivot quality. If the pivot lands near the median, you get two roughly equal subarrays, the recursion tree has depth O(log n), and each level does O(n) work — giving O(n log n) total. If the pivot is consistently the smallest or largest element (imagine sorting an already-sorted array with the first element as pivot), one subarray is empty and the other has n−1 elements. The recursion tree degenerates to depth n, and total work becomes O(n²). **Randomized pivot selection** — picking a uniformly random element as the pivot — makes the expected number of comparisons about 1.39n log n regardless of input order, which is why production implementations always randomize.

Quicksort's practical speed advantage over merge sort comes from **cache locality**. Quicksort operates on a contiguous block of memory, accessing elements sequentially and swapping in-place. Merge sort, by contrast, copies elements between arrays during the merge step, which causes more cache misses. This constant-factor advantage makes quicksort faster on real hardware despite both algorithms having O(n log n) expected time. The tradeoff is that quicksort is **not stable** — equal elements may be reordered during partitioning — and its worst case is quadratic. When worst-case guarantees matter more than average-case speed, merge sort or heapsort may be preferable.
