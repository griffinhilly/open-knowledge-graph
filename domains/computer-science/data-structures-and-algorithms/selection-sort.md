---
id: selection-sort
title: Selection Sort Algorithm
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
- selection-sort
- comparison-sort
- in-place
stage: formal-systems
status: draft
---

# Selection Sort Algorithm

## Core Idea
Selection sort divides the array into sorted and unsorted regions, repeatedly finding the minimum in the unsorted region and swapping it to the end of the sorted region. It is O(n²) in all cases (best, average, worst), makes exactly n−1 swaps (minimal), and requires O(1) space. It is useful when memory writes are expensive.

## How It's Best Learned
Trace selection sort, seeing the sorted region grow one element at a time. Implement and count comparisons and swaps. Compare to insertion sort: fewer swaps but same comparison count. Understand why it's not inherently stable.

## Common Misconceptions
- Selection sort is faster than insertion sort (both O(n²); selection makes fewer swaps but insertion may be faster on nearly-sorted data). - Selection sort is stable (not inherently, though careful implementation can make it so).

## Questions

```yaml
- question: "An array of 1,000 elements is already perfectly sorted. How many comparisons does selection sort make?"
  type: multiple-choice
  options:
    - "Zero — it detects the sorted order and terminates early"
    - "About 1,000 — one per element to verify it is in place"
    - "499,500 — the same n(n−1)/2 it would make on any input"
    - "About 500,000, but fewer than for a reversed array"
  answer: 2
  explanation: "Selection sort always makes exactly n(n−1)/2 comparisons regardless of the input's initial order. On each pass it scans the entire unsorted portion to find the minimum — it has no mechanism to detect that elements are already in order. This contrasts sharply with insertion sort, which degenerates to O(n) on already-sorted data. Selection sort simply does not adapt."

- question: "You are sorting records stored in flash memory, where each write operation physically degrades the storage medium. Which property of selection sort makes it most appropriate for this context?"
  type: multiple-choice
  options:
    - "Selection sort is O(n log n) in the best case, minimizing total operations"
    - "Selection sort is stable, preserving the original order of equal-key records"
    - "Selection sort makes exactly n−1 swaps, minimizing the number of write operations"
    - "Selection sort runs entirely in-place, requiring no additional flash memory"
  answer: 2
  explanation: "Selection sort's defining property is that it makes exactly n−1 swaps — one per pass, not per comparison. No comparison-based sort makes fewer swaps. When writes are expensive (flash memory wears out; each swap triggers a costly side effect), this minimal-write property is decisive. Option B is a misconception: selection sort is NOT stable in its standard form. And option A is wrong: selection sort is O(n²) in all cases."

- question: "Selection sort makes exactly n−1 swaps to sort an array of n elements, regardless of the initial ordering."
  type: true-false
  answer: true
  explanation: "Selection sort performs one swap per pass: find the minimum of the unsorted region and swap it into position. With n elements there are n−1 passes (the last element is trivially in place), so exactly n−1 swaps occur. This holds whether the array starts sorted, reversed, or random — even a sorted array triggers n−1 swaps of elements with themselves. This is selection sort's key advantage when write cost dominates."

- question: "Selection sort is generally faster than insertion sort on nearly-sorted input because selection sort makes fewer swaps."
  type: true-false
  answer: false
  explanation: "This is the classic misconception. On nearly-sorted input, insertion sort runs in near-O(n) time because each element is close to its correct position and the inner loop exits early. Selection sort ignores existing order completely — it always makes n(n−1)/2 comparisons and n−1 swaps. On nearly-sorted data, insertion sort decisively outperforms selection sort. The swap-minimization advantage of selection sort is relevant only when write cost (not total operation count) is the bottleneck."

- question: "Explain why selection sort's time complexity is O(n²) in the best case, even when the input is already sorted. What algorithmic property causes this?"
  type: short-answer
  answer: "Selection sort has no mechanism to detect or exploit existing order. On each pass it must scan the entire unsorted portion to find the minimum — even if that minimum is already in the correct position. It compares every remaining element against the current candidate before confirming which element to swap. This scan always takes O(n) per pass and there are O(n) passes, giving O(n²) regardless of input."
  explanation: "The root cause is that selection sort's inner loop has no early-exit condition. The algorithm commits to finding the true minimum of the unsorted region, which requires exhaustive comparison. Insertion sort, by contrast, shifts elements right only until it finds the correct insertion point — on a sorted array the inner loop exits immediately after zero shifts, giving O(1) work per element and O(n) total."
```

## Explainer

**Selection sort** works by a simple, almost mechanical process: scan the entire unsorted portion of the array to find the smallest element, then swap it into its correct position at the front. Now that element is sorted. Repeat for the remaining unsorted portion. If you've worked with arrays and indexing, you can already picture this — it's like sorting a hand of playing cards by repeatedly pulling out the lowest card and placing it at the left end of your hand.

Walk through a concrete example. Given the array `[29, 10, 14, 37, 13]`, the algorithm scans all five elements, finds 10 as the minimum, and swaps it with 29 to get `[10, 29, 14, 37, 13]`. Now the sorted region is `[10]` and the unsorted region is `[29, 14, 37, 13]`. Next scan finds 13, swaps with 29: `[10, 13, 14, 37, 29]`. Then 14 is already in place. Then 29 swaps with 37. After n−1 passes, the array is sorted. Notice that regardless of the input, the algorithm always makes the same number of comparisons: n(n−1)/2. Whether the array starts sorted, reversed, or random, selection sort doesn't adapt — it always does O(n²) comparisons.

What selection sort does minimize is **swaps** — exactly n−1 of them, one per pass. This is the fewest swaps of any comparison-based sorting algorithm, and it matters when writes are expensive (think flash memory where writes degrade the hardware, or scenarios where each swap triggers an expensive side effect). By contrast, insertion sort might make O(n²) swaps on a reversed array but can finish in O(n) on a nearly-sorted one. So the choice between them depends on your data: if it's likely almost sorted, insertion sort adapts and runs fast; if write cost dominates, selection sort's minimal swaps win.

One last detail: selection sort is **not stable** in its standard form. Stability means equal elements preserve their original relative order. When selection sort swaps the minimum into position, it can jump an element over others with the same value, breaking their original order. For example, if you have two elements with key 5 at positions 2 and 4, a swap might move the one at position 4 ahead of the one at position 2. This usually doesn't matter for simple integers, but it matters when you're sorting records with multiple fields and want to preserve a prior sort's ordering.
