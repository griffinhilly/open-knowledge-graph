---
id: counting-sort
title: Counting Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward:
- radix-sort
tags:
- sorting
- counting-sort
- linear-time
- non-comparison
- stable
- integer-sorting
stage: formal-systems
status: draft
---

# Counting Sort Algorithm

## Core Idea
Counting sort counts the frequency of each distinct value and uses prefix sums to determine output positions, achieving O(n + k) time where k is the value range. It beats the O(n log n) lower bound for comparison sorts, is stable, uses O(k) space, and is practical for sorting small integers or as a radix-sort subroutine.

## How It's Best Learned
Trace counting sort on a small array with limited range. Build frequency and prefix-sum arrays step-by-step. See how it avoids comparisons entirely. Understand why stability is preserved during output placement.

## Common Misconceptions
- Counting sort is always faster than O(n log n) sorts (it beats comparison sorts but for large k, it becomes impractical). - It requires O(k) space (yes, crucial for the algorithm).

## Explainer

Every comparison-based sorting algorithm — merge sort, quicksort, heapsort — has a proven lower bound of O(n log n) comparisons in the worst case. **Counting sort** breaks through this barrier by not comparing elements at all. Instead, it exploits the fact that the values being sorted are integers within a known range, and it uses array indexing to directly compute where each element belongs in the output.

The algorithm works in three clean steps. Suppose you have an array of n integers, each between 0 and k−1. First, create a **count array** of size k and scan through the input, incrementing count[v] for each value v. After this pass, count[v] tells you exactly how many times value v appears. Second, transform the count array into a **prefix sum array**: replace each count[i] with the sum of all counts from 0 through i. Now prefix[v] tells you the index *after* the last position where value v should go in the output. Third, scan the input array (from right to left for stability), and for each element with value v, place it at position prefix[v]−1 in the output array and decrement prefix[v]. When finished, the output array is sorted.

To build intuition, imagine sorting exam scores from 0 to 100 for a class of 200 students. The count array has 101 entries. After counting, you know that 3 students scored 0, 5 scored 1, and so on. The prefix sums tell you that scores of 0 go in positions 0–2, scores of 1 go in positions 3–7, and so forth. Each score's final position is determined by arithmetic, not by comparing it to other scores. The total work is one pass over the input (O(n)) plus building the prefix sums (O(k)), giving **O(n + k)** time. When k is on the order of n — say, sorting a million integers in the range 0 to 999,999 — this is essentially linear.

**Stability** is a key property that makes counting sort especially useful as a building block. A sort is stable if elements with equal keys maintain their original relative order. Counting sort achieves this by processing the input from right to left during the placement step: the last element with value v is placed at the highest available position for v, the second-to-last at the next position down, and so on. This stability is essential for **radix sort**, which sorts numbers digit by digit from least significant to most significant — each digit pass must be stable so that previous digit orderings are preserved. The limitation is clear: if k is enormous relative to n (say, sorting 100 elements with values up to a billion), the count array wastes massive space and time, and a comparison sort is far more practical.
