---
id: radix-sort
title: Radix Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: counting-sort
  type: hard
- id: algorithm-design-basics
  type: soft
tags:
- sorting
- radix-sort
- linear-time
- non-comparison
- digit-by-digit
- stable
stage: formal-systems
status: draft
---

# Radix Sort Algorithm

## Core Idea
Radix sort treats numbers as sequences of digits and sorts them digit-by-digit using a stable sub-sort (like counting sort). Processing digits from least-significant to most-significant yields O(d * (n + b)) time, where d is the number of digits and b is the base. For fixed-length integers, this is linear in input size and faster than comparison sorts in practice.

## How It's Best Learned
Trace radix sort on small numbers, processing one digit at a time. Implement using counting sort as the stable sub-sort. Understand why least-significant-digit processing works. Compare performance to quicksort and mergesort on large integer arrays.

## Common Misconceptions
- Radix sort is always faster than quicksort (depends on digit count and constant factors; quicksort is more general). - It only works on integers (strings are sequences of character digits and can be radix-sorted too).
