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

## Explainer

You already know from counting sort that comparison-based sorting has a lower bound of O(n log n), but counting sort beats this by exploiting the structure of the keys — it counts occurrences rather than comparing elements. The limitation of counting sort is that it needs an array as large as the range of values, so sorting 32-bit integers directly would require an array of 4 billion entries. **Radix sort** solves this by applying counting sort one digit at a time, keeping the auxiliary array small while still achieving linear-time performance.

The key insight is processing digits from **least significant to most significant** (LSD radix sort). This seems backwards at first — wouldn't you want to sort by the most important digit first? The reason LSD ordering works is that counting sort is **stable**: elements with equal keys maintain their original relative order. When you sort by the ones digit, ties are left in their input order. When you then sort by the tens digit, elements with the same tens digit remain sorted by their ones digit (because of stability). Each pass refines the ordering without disturbing the work of previous passes. After processing all d digits, the array is fully sorted.

Consider sorting the numbers [329, 457, 657, 839, 436, 720, 355]. In base 10, the first pass sorts by the ones digit: 720, 355, 436, 457, 657, 329, 839. The second pass sorts by the tens digit: 720, 329, 436, 839, 355, 457, 657. The third pass sorts by the hundreds digit: 329, 355, 436, 457, 657, 720, 839. Each pass is a counting sort over just 10 buckets (digits 0–9), processing all n elements in O(n + 10) = O(n) time. With d = 3 passes, total work is O(3n) = O(n) for fixed-length keys.

The general complexity is **O(d × (n + b))**, where d is the number of digit positions and b is the base (number of possible digit values). Choosing the base is a design decision: a larger base reduces d (fewer passes) but increases the size of the counting array. For 32-bit integers, using base 256 means d = 4 passes with a 256-entry counting array — four linear scans over the data, which is often faster than quicksort's O(n log n) comparisons for large n. The tradeoff is that radix sort requires O(n + b) extra space for the counting sort output, making it less memory-efficient than in-place comparison sorts. Radix sort excels when keys are fixed-length integers or strings and the number of digit positions is small relative to log n — exactly the scenarios where its linear time complexity provides a real advantage over comparison-based alternatives.
