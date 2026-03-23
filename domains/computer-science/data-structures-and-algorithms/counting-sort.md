---
id: counting-sort
title: Counting Sort Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
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
status: validated
---
# Counting Sort Algorithm

## Core Idea
Counting sort counts the frequency of each distinct value and uses prefix sums to determine output positions, achieving O(n + k) time where k is the value range. It beats the O(n log n) lower bound for comparison sorts, is stable, uses O(k) space, and is practical for sorting small integers or as a radix-sort subroutine.

## How It's Best Learned
Trace counting sort on a small array with limited range. Build frequency and prefix-sum arrays step-by-step. See how it avoids comparisons entirely. Understand why stability is preserved during output placement.

## Common Misconceptions
- Counting sort is always faster than O(n log n) sorts (it beats comparison sorts but for large k, it becomes impractical). - It requires O(k) space (yes, crucial for the algorithm).

## Questions

```yaml
- question: "What is the time complexity of counting sort when sorting n integers drawn from the range [0, k−1]?"
  type: multiple-choice
  options:
    - "O(n log n) — same as comparison-based sorts like merge sort"
    - "O(n + k) — one pass over the input plus one pass over the count array"
    - "O(n × k) — each element is compared against all k possible values"
    - "O(k log k) — the count array itself must be sorted"
  answer: 1
  explanation: "Counting sort makes one pass over the n input elements to build the frequency array (O(n)), one pass of length k to compute prefix sums (O(k)), and one final pass over the n input elements to place them (O(n)). Total: O(n + k). There are no comparisons between elements at all — the algorithm uses value-as-index arithmetic. This is how it beats the O(n log n) lower bound that applies only to comparison sorts."

- question: "You need to sort 1,000 integers where each value can range from 0 to 1,000,000,000. Would counting sort be the best approach?"
  type: multiple-choice
  options:
    - "Yes — counting sort is always faster than comparison sorts since O(n + k) beats O(n log n)"
    - "No — with k = 10^9 and only n = 1,000 elements, the count array would require a billion entries, making counting sort far less practical than a comparison sort"
    - "Yes — as long as the values are integers, counting sort outperforms merge sort regardless of range"
    - "It depends only on whether the array is nearly sorted; counting sort is best for nearly-sorted inputs"
  answer: 1
  explanation: "Counting sort's O(n + k) time and O(k) space are only practical when k is on the order of n. With n = 1,000 and k = 10^9, allocating and traversing a billion-element count array dwarfs any savings from avoiding comparisons. In this case, merge sort's O(n log n) ≈ O(10,000) operations on 1,000 elements is vastly more efficient. Option A is the key misconception: 'O(n + k) beats O(n log n)' is only true when k = O(n)."

- question: "Counting sort avoids the O(n log n) comparison-sort lower bound by making fewer comparisons than merge sort — it simply compares elements more cleverly."
  type: true-false
  answer: false
  explanation: "Counting sort makes zero comparisons between elements. It bypasses the comparison lower bound entirely by using a fundamentally different mechanism: it uses each element's value as an index into the count array, then uses arithmetic (prefix sums) to determine output positions. The O(n log n) lower bound applies only to algorithms that determine order exclusively through element comparisons — counting sort doesn't fall in that category at all."

- question: "Counting sort is a stable sorting algorithm, meaning elements with equal keys appear in the output in the same relative order they had in the input."
  type: true-false
  answer: true
  explanation: "Stability is achieved by scanning the input array from right to left during the placement step. The last occurrence of a given value v is placed at the highest available position for v, the second-to-last at the next position down, and so on. This preserves original relative ordering among equal elements. Stability is not incidental — it is deliberately engineered and is essential for counting sort's role as a subroutine in radix sort, where the relative order established by one digit pass must be preserved in the next."

- question: "Explain why counting sort can sort n elements faster than O(n log n) in some cases, but cannot universally replace comparison-based sorting algorithms."
  type: short-answer
  answer: "Counting sort avoids comparisons entirely by using element values as array indices — a trick that only works when values are integers in a known, bounded range [0, k−1]. Its O(n + k) time is better than O(n log n) when k is small relative to n, because the algorithm's work is proportional to the size of the value range, not the number of comparisons needed to establish order. However, if k is large (say, 10^9 for n = 1,000 elements), the O(k) cost to initialize and scan the count array dominates and makes counting sort impractical. Additionally, counting sort cannot handle non-integer keys (floating-point numbers, strings, arbitrary objects) because those cannot serve as array indices. Comparison sorts work on any ordered type regardless of range."
  explanation: "The tradeoff is essentially: counting sort trades the O(n log n) comparison cost for O(k) space and time, which only benefits you when k is manageable. This is why counting sort appears most often as a building block (e.g., in radix sort on digit-by-digit passes) where k is small by construction."
```

## Explainer

Every comparison-based sorting algorithm — merge sort, quicksort, heapsort — has a proven lower bound of O(n log n) comparisons in the worst case. **Counting sort** breaks through this barrier by not comparing elements at all. Instead, it exploits the fact that the values being sorted are integers within a known range, and it uses array indexing to directly compute where each element belongs in the output.

The algorithm works in three clean steps. Suppose you have an array of n integers, each between 0 and k−1. First, create a **count array** of size k and scan through the input, incrementing count[v] for each value v. After this pass, count[v] tells you exactly how many times value v appears. Second, transform the count array into a **prefix sum array**: replace each count[i] with the sum of all counts from 0 through i. Now prefix[v] tells you the index *after* the last position where value v should go in the output. Third, scan the input array (from right to left for stability), and for each element with value v, place it at position prefix[v]−1 in the output array and decrement prefix[v]. When finished, the output array is sorted.

To build intuition, imagine sorting exam scores from 0 to 100 for a class of 200 students. The count array has 101 entries. After counting, you know that 3 students scored 0, 5 scored 1, and so on. The prefix sums tell you that scores of 0 go in positions 0–2, scores of 1 go in positions 3–7, and so forth. Each score's final position is determined by arithmetic, not by comparing it to other scores. The total work is one pass over the input (O(n)) plus building the prefix sums (O(k)), giving **O(n + k)** time. When k is on the order of n — say, sorting a million integers in the range 0 to 999,999 — this is essentially linear.

**Stability** is a key property that makes counting sort especially useful as a building block. A sort is stable if elements with equal keys maintain their original relative order. Counting sort achieves this by processing the input from right to left during the placement step: the last element with value v is placed at the highest available position for v, the second-to-last at the next position down, and so on. This stability is essential for **radix sort**, which sorts numbers digit by digit from least significant to most significant — each digit pass must be stable so that previous digit orderings are preserved. The limitation is clear: if k is enormous relative to n (say, sorting 100 elements with values up to a billion), the count array wastes massive space and time, and a comparison sort is far more practical.
