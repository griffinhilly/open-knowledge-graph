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

## Explainer

**Selection sort** works by a simple, almost mechanical process: scan the entire unsorted portion of the array to find the smallest element, then swap it into its correct position at the front. Now that element is sorted. Repeat for the remaining unsorted portion. If you've worked with arrays and indexing, you can already picture this — it's like sorting a hand of playing cards by repeatedly pulling out the lowest card and placing it at the left end of your hand.

Walk through a concrete example. Given the array `[29, 10, 14, 37, 13]`, the algorithm scans all five elements, finds 10 as the minimum, and swaps it with 29 to get `[10, 29, 14, 37, 13]`. Now the sorted region is `[10]` and the unsorted region is `[29, 14, 37, 13]`. Next scan finds 13, swaps with 29: `[10, 13, 14, 37, 29]`. Then 14 is already in place. Then 29 swaps with 37. After n−1 passes, the array is sorted. Notice that regardless of the input, the algorithm always makes the same number of comparisons: n(n−1)/2. Whether the array starts sorted, reversed, or random, selection sort doesn't adapt — it always does O(n²) comparisons.

What selection sort does minimize is **swaps** — exactly n−1 of them, one per pass. This is the fewest swaps of any comparison-based sorting algorithm, and it matters when writes are expensive (think flash memory where writes degrade the hardware, or scenarios where each swap triggers an expensive side effect). By contrast, insertion sort might make O(n²) swaps on a reversed array but can finish in O(n) on a nearly-sorted one. So the choice between them depends on your data: if it's likely almost sorted, insertion sort adapts and runs fast; if write cost dominates, selection sort's minimal swaps win.

One last detail: selection sort is **not stable** in its standard form. Stability means equal elements preserve their original relative order. When selection sort swaps the minimum into position, it can jump an element over others with the same value, breaking their original order. For example, if you have two elements with key 5 at positions 2 and 4, a swap might move the one at position 4 ahead of the one at position 2. This usually doesn't matter for simple integers, but it matters when you're sorting records with multiple fields and want to preserve a prior sort's ordering.
