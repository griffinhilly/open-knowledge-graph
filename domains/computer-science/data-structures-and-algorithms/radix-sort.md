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
- id: selection-sort
  type: soft
tags:
- sorting
- radix-sort
- linear-time
- non-comparison
- digit-by-digit
- stable
stage: formal-systems
status: validated
---
# Radix Sort Algorithm

## Core Idea
Radix sort treats numbers as sequences of digits and sorts them digit-by-digit using a stable sub-sort (like counting sort). Processing digits from least-significant to most-significant yields O(d * (n + b)) time, where d is the number of digits and b is the base. For fixed-length integers, this is linear in input size and faster than comparison sorts in practice.

## How It's Best Learned
Trace radix sort on small numbers, processing one digit at a time. Implement using counting sort as the stable sub-sort. Understand why least-significant-digit processing works. Compare performance to quicksort and mergesort on large integer arrays.

## Common Misconceptions
- Radix sort is always faster than quicksort (depends on digit count and constant factors; quicksort is more general). - It only works on integers (strings are sequences of character digits and can be radix-sorted too).

## Questions

```yaml
- question: "You implement LSD radix sort but accidentally use an unstable sub-sort (equal-key elements may reorder arbitrarily). What is the consequence?"
  type: multiple-choice
  options:
    - "The algorithm runs faster because stability checking overhead is removed"
    - "The algorithm still sorts correctly for integers, but fails for strings"
    - "Later digit passes destroy the relative ordering established by earlier passes, corrupting the final result"
    - "The algorithm crashes because it requires stable memory pointers"
  answer: 2
  explanation: "Stability is not a performance optimization — it is the correctness mechanism. When you sort by the tens digit, you must preserve the ordering by ones digit that the previous pass established. An unstable sub-sort scrambles equal-key elements arbitrarily, undoing that work. LSD radix sort is correct precisely because stability ensures each pass refines the ordering without disturbing previous passes. Replace the stable sub-sort with an unstable one and the algorithm produces incorrect results."

- question: "You implement radix sort on 32-bit integers using base 256 (b = 256, so each digit represents one byte). How many passes over the data are required?"
  type: multiple-choice
  options:
    - "32 passes — one per bit"
    - "8 passes — one per pair of bits (nibble)"
    - "4 passes — one per byte"
    - "2 passes — one for the low 16 bits, one for the high 16 bits"
  answer: 2
  explanation: "In base 256, each 'digit' represents 8 bits (one byte). A 32-bit integer has 4 bytes, so 4 passes suffice, each scanning all n elements using a 256-entry counting array. Choosing base 256 is a deliberate optimization: it minimizes passes to 4 (versus 32 for base-2) while keeping the auxiliary array small. The general formula is d = (key width in bits) / log2(b)."

- question: "Radix sort achieves its linear-time performance by comparing elements directly, just more cleverly than comparison-based sorts like quicksort."
  type: true-false
  answer: false
  explanation: "Radix sort is a non-comparison sort — it never compares two elements against each other. Instead, it inspects individual digits and places elements into buckets using counting sort. This is exactly why it can break the O(n log n) comparison-sort lower bound: that lower bound applies only to algorithms that determine order by comparing pairs of elements. Radix sort exploits the structure of the keys (they're sequences of digits) to sort without comparisons."

- question: "Stability of the sub-sort is essential to the correctness of LSD radix sort — without it, the algorithm cannot guarantee a sorted result."
  type: true-false
  answer: true
  explanation: "Stability is the mechanism that makes LSD ordering work. After the first pass (ones digit), elements with equal ones digits are in their input order. The second pass (tens digit) sorts by tens digit while preserving ones-digit order for ties, because a stable sort maintains relative order for equal keys. This means each pass adds information rather than discarding the previous pass's work. Without stability, passes would interfere with each other and correctness would be lost."

- question: "Why does LSD radix sort process digits from least significant to most significant, rather than most to least significant? What would go wrong if you reversed the order?"
  type: short-answer
  answer: "Processing least-significant digits first works because the sub-sort is stable: each subsequent pass sorts by a more significant digit while preserving the relative order established by less significant digits. If you reversed the order (MSD first), a later pass sorting by a less significant digit would destroy the ordering of more significant digits, since there's no mechanism to say 'only reorder elements that are tied on the more significant digit.'"
  explanation: "The key is that stability lets each pass 'refine' rather than 'restart.' MSD-first radix sort does exist but requires a different structure — typically a recursive approach that partitions into buckets by the most significant digit, then recursively sorts within each bucket. LSD is simpler because a single linear pass of a stable sub-sort is sufficient at each level."
```

## Explainer

You already know from counting sort that comparison-based sorting has a lower bound of O(n log n), but counting sort beats this by exploiting the structure of the keys — it counts occurrences rather than comparing elements. The limitation of counting sort is that it needs an array as large as the range of values, so sorting 32-bit integers directly would require an array of 4 billion entries. **Radix sort** solves this by applying counting sort one digit at a time, keeping the auxiliary array small while still achieving linear-time performance.

The key insight is processing digits from **least significant to most significant** (LSD radix sort). This seems backwards at first — wouldn't you want to sort by the most important digit first? The reason LSD ordering works is that counting sort is **stable**: elements with equal keys maintain their original relative order. When you sort by the ones digit, ties are left in their input order. When you then sort by the tens digit, elements with the same tens digit remain sorted by their ones digit (because of stability). Each pass refines the ordering without disturbing the work of previous passes. After processing all d digits, the array is fully sorted.

Consider sorting the numbers [329, 457, 657, 839, 436, 720, 355]. In base 10, the first pass sorts by the ones digit: 720, 355, 436, 457, 657, 329, 839. The second pass sorts by the tens digit: 720, 329, 436, 839, 355, 457, 657. The third pass sorts by the hundreds digit: 329, 355, 436, 457, 657, 720, 839. Each pass is a counting sort over just 10 buckets (digits 0–9), processing all n elements in O(n + 10) = O(n) time. With d = 3 passes, total work is O(3n) = O(n) for fixed-length keys.

The general complexity is **O(d × (n + b))**, where d is the number of digit positions and b is the base (number of possible digit values). Choosing the base is a design decision: a larger base reduces d (fewer passes) but increases the size of the counting array. For 32-bit integers, using base 256 means d = 4 passes with a 256-entry counting array — four linear scans over the data, which is often faster than quicksort's O(n log n) comparisons for large n. The tradeoff is that radix sort requires O(n + b) extra space for the counting sort output, making it less memory-efficient than in-place comparison sorts. Radix sort excels when keys are fixed-length integers or strings and the number of digit positions is small relative to log n — exactly the scenarios where its linear time complexity provides a real advantage over comparison-based alternatives.
