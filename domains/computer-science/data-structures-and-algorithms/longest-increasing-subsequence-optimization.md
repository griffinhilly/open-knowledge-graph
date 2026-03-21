---
id: longest-increasing-subsequence-optimization
title: 'Longest Increasing Subsequence: Dynamic Programming and Optimization'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
tags:
- dynamic-programming
- sequences
- optimization
stage: formal-systems
status: draft
---

# Longest Increasing Subsequence: Dynamic Programming and Optimization

## Core Idea
The longest increasing subsequence (LIS) is the longest sequence of elements where each is greater than the previous. DP solves it in O(n²) time. Binary search optimization (tracking smallest tail values of LIS of each length) achieves O(n log n). Applications include stock trading, sequence alignment, and version control.

## How It's Best Learned
Implement O(n²) DP (dp[i] = longest LIS ending at i). Then implement O(n log n) with binary search on tails. Trace both on the same input and observe how binary search prunes comparisons.

## Common Misconceptions
- Thinking LIS requires contiguous elements; it's subsequence (not subarray).
- Assuming O(n²) DP is always sufficient; O(n log n) matters for large sequences.
- Not recognizing that LIS is a canonical DP problem useful for understanding the technique.

## Questions

```yaml
- question: "You are implementing the O(n log n) LIS algorithm. After processing several elements, your tails array is [2, 5, 7]. You now encounter the value 4. What happens?"
  type: multiple-choice
  options:
    - "4 is appended to tails, making it [2, 5, 7, 4]"
    - "4 replaces 5 in tails, making it [2, 4, 7]"
    - "4 is ignored because 5 is already smaller than 7 at that position"
    - "The entire tails array is rebuilt from scratch with 4 included"
  answer: 1
  explanation: "Binary search finds the leftmost value in tails that is >= 4, which is 5 at index 1. We replace it with 4, yielding [2, 4, 7]. This replacement doesn't reduce the current LIS length (still 3) but lowers the 'bar' at length 2, keeping the door open for future extensions. The tails array always stays sorted, which is what makes binary search valid."

- question: "An O(n²) DP solution for LIS defines dp[i] as the longest increasing subsequence ending at index i. Which element in [3, 1, 4, 1, 5, 9, 2, 6] would have dp[i] = 1 forced by definition, not just as a minimum?"
  type: multiple-choice
  options:
    - "Only the first element (3), because no elements precede it"
    - "Every element whose value is smaller than all previous elements"
    - "Every element individually, since each element alone forms a subsequence of length 1"
    - "Only elements that are local minima in the sequence"
  answer: 2
  explanation: "Every element alone is an increasing subsequence of length 1 — this is the base case. dp[i] starts at 1 for all i, then we look back at every j < i where arr[j] < arr[i] and update dp[i] = max(dp[i], dp[j]+1). The base case doesn't apply only to the first element or only to minima — it applies universally, which is what makes the DP recurrence well-founded."

- question: "The longest increasing subsequence requires the selected elements to be contiguous in the original array."
  type: true-false
  answer: false
  explanation: "This is the most common misconception. LIS is a *subsequence*, not a *subarray* — you can skip elements. In [3, 1, 4, 1, 5, 9, 2, 6], the LIS [1, 4, 5, 9] skips the second 1 entirely, and [1, 2, 6] skips everything in between. A subarray (or substring) requires contiguity; a subsequence only requires preserving the original order."

- question: "In the O(n log n) LIS algorithm, the tails array at the end of processing always stores the actual longest increasing subsequence."
  type: true-false
  answer: false
  explanation: "This is a subtle but important point. The tails array stores the *smallest possible tail element* of any increasing subsequence of each length found so far — it is an auxiliary structure optimized for extending subsequences, not for recording the actual sequence. For example, after processing [3, 1, 2], tails might be [1, 2] even though the LIS starting with 3 existed earlier. To recover the actual subsequence, you need a separate predecessor array. The tails array gives you the correct *length*, not the elements."

- question: "Explain why the tails array in the O(n log n) LIS algorithm remains sorted throughout the algorithm, and why that property is essential."
  type: short-answer
  answer: "The tails array is sorted because tails[k] represents the minimum possible ending value of any increasing subsequence of length k+1. A subsequence of length k+1 must end with a value strictly greater than any subsequence of length k, so tails[k] < tails[k+1] always holds. Whenever we place a new value, binary search finds the correct sorted position and either replaces an existing entry or appends. The sorted property is essential because it is what makes binary search valid — without it, we'd have to scan linearly, restoring the O(n²) behavior we were trying to escape."
  explanation: "The invariant tails[k] < tails[k+1] is maintained by the algorithm's logic: you can only extend a length-k subsequence with a value strictly greater than its ending value. This guarantees tails stays sorted. If tails were unsorted, binary search would give wrong results, and the entire O(log n) per element advantage would collapse. This is the core mathematical reason the optimization works."
```

## Explainer

The **longest increasing subsequence (LIS)** problem asks: given a sequence of numbers, what is the longest subsequence where each element is strictly greater than the one before it? A subsequence does not need to be contiguous — you can skip elements — which is what distinguishes it from a subarray. For example, in [3, 1, 4, 1, 5, 9, 2, 6], one LIS is [1, 4, 5, 9] with length 4, and another equally valid one is [1, 4, 5, 6].

The classic dynamic programming approach defines dp[i] as the length of the longest increasing subsequence that ends at index i. For each position i, you look back at every earlier position j where the value is smaller, and take dp[i] = max(dp[j] + 1) over all valid j. Since each position checks all earlier positions, this runs in O(n²). This directly applies the DP pattern you already know: define subproblems, establish a recurrence, and fill the table in order. The base case is dp[i] = 1 for every i — each element alone is a subsequence of length 1.

The O(n²) solution works but becomes too slow for sequences of length 100,000 or more. The **patience sorting optimization** brings this down to O(n log n) using a clever auxiliary array called **tails**, where tails[k] stores the smallest possible tail element of any increasing subsequence of length k+1 found so far. As you scan through the input, each new element either extends the longest subsequence (append to tails) or replaces an element in tails using binary search to find the correct position. The key property is that tails is always sorted, which is what makes binary search valid. When a new value is smaller than some tails[k], replacing tails[k] doesn't change the current LIS length — it keeps the door open for longer subsequences to form later by lowering the bar for future extensions.

To build intuition for why this works, imagine you are managing multiple "candidate" subsequences simultaneously. Rather than tracking every candidate explicitly, the tails array compresses them into a single sorted structure that captures just the information you need: the minimum ending value at each possible length. Binary search on this sorted structure replaces the O(n) inner scan of the basic DP, yielding the O(n log n) improvement. If you also need to recover the actual subsequence (not just its length), you maintain a predecessor array alongside tails to trace back through the choices.
