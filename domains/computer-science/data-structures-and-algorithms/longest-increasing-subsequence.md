---
id: longest-increasing-subsequence
title: Longest Increasing Subsequence (LIS) Problem
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
- id: binary-search-algorithm
  type: soft
- id: longest-common-subsequence
  type: soft
- id: knapsack-0-1-bounded
  type: soft
tags:
- dynamic-programming
- lis
- subsequence
- greedy
- binary-search
stage: formal-systems
status: validated
---
# Longest Increasing Subsequence (LIS) Problem

## Core Idea
The longest increasing subsequence problem finds the longest subsequence of elements in increasing order. Naive DP: O(n²) via dp[i] = 1 + max(dp[j] for all j < i where A[j] < A[i]). Optimal O(n log n) approach: maintain the smallest tail value for each LIS length and binary search to find where the next element fits. This elegantly combines DP and binary search.

## How It's Best Learned
Trace the O(n²) DP approach by hand. Then trace the O(n log n) approach with the tail array and binary search. Compare both on the same input and see the speed difference. Understand the tail-array invariant.

## Common Misconceptions
- LIS requires strict inequality (A[i] > A[j]); non-strictly increasing is a different problem. - The O(n log n) solution is always faster (asymptotically yes; for small n, O(n²) may be faster due to constant factors).

## Questions

```yaml
- question: "While running the O(n log n) LIS algorithm on [3, 1, 4, 1, 5, 9, 2, 6], after processing all elements the tails array is [1, 2, 5, 6]. Which statement is correct?"
  type: multiple-choice
  options:
    - "The longest increasing subsequence is 1, 2, 5, 6 taken directly from the input"
    - "The length of the LIS is 4, but the actual subsequence must be reconstructed separately"
    - "The tails array length is wrong — the LIS length should be 5 since 9 appeared"
    - "The algorithm failed because replacing 4 with 2 corrupted the subsequence"
  answer: 1
  explanation: "The tails array is a bookkeeping structure, not the actual LIS. Its length (4) is correct — the LIS length is 4 — but [1, 2, 5, 6] does not correspond to any single valid increasing subsequence: 2 appears at index 6 in the input while 5 appears at index 4, so 1→2→5→6 cannot be read left-to-right from the array. The actual LIS (such as [1, 4, 5, 9] or [1, 4, 5, 6]) must be reconstructed by tracking parent pointers during the algorithm. Option D misunderstands the algorithm: replacing 4 with 2 is correct because a subsequence of length 2 ending in 2 is more extensible than one ending in 4."

- question: "In the O(n log n) LIS algorithm, why must the tails array always remain sorted?"
  type: multiple-choice
  options:
    - "So that duplicate elements can be detected and skipped"
    - "Because the DP recurrence requires tails in ascending order to compute dp[i]"
    - "So that binary search can locate the correct insertion position in O(log n)"
    - "So that the actual LIS can be read off directly from left to right"
  answer: 2
  explanation: "The entire O(n log n) speedup comes from replacing the O(n) inner scan of the O(n²) DP with a binary search. Binary search requires a sorted array. The tails invariant — tails[k] stores the smallest possible tail of any increasing subsequence of length k+1 — guarantees sorted order: a length-2 subsequence must end at a smaller value than any length-3 subsequence's tail. If the array weren't sorted, binary search would be invalid and you'd be back to linear scanning, losing the speedup."

- question: "The tails array in the O(n log n) LIS algorithm directly stores the actual longest increasing subsequence found in the input."
  type: true-false
  answer: false
  explanation: "This is the central misconception about the algorithm. The tails array is a bookkeeping structure that tracks the smallest possible tail element for subsequences of each length. When an element replaces an existing tail, the resulting array may not correspond to any valid subsequence of the input — the indices don't have to appear in increasing order. The tails array length equals the LIS length, which is the answer the algorithm reports, but the actual subsequence requires separate reconstruction using parent pointers."

- question: "For any input sequence of length n, the O(n log n) LIS algorithm performs exactly n binary searches on the tails array."
  type: true-false
  answer: true
  explanation: "Every element of the input is processed exactly once: for each element, one binary search on the tails array finds its insertion position, then the element either appends (extending the longest subsequence) or replaces an existing tail entry. This gives exactly n binary searches, each costing O(log n) — yielding the O(n log n) total runtime. No element is revisited or skipped."

- question: "Why does the O(n log n) LIS algorithm replace an existing tail entry rather than simply skipping elements that don't extend the current longest subsequence? What invariant does replacement maintain?"
  type: short-answer
  answer: "Replacement keeps future options open by minimizing each tail value. The invariant is that tails[k] holds the smallest possible tail for any increasing subsequence of length k+1 seen so far. A new element that is smaller than tails[k] but larger than tails[k-1] can start a length-(k+1) subsequence ending lower, making future extensions easier. Skipping it would preserve a larger tail value, incorrectly blocking valid extensions and potentially returning a wrong (too-short) LIS length."
  explanation: "The tails invariant is what keeps the array sorted and enables binary search. Minimizing each tail maximizes the chance that future elements can extend a subsequence of that length. This is the key insight separating the O(n log n) approach from naive DP: instead of tracking every possible ending value, you track only the best (smallest) ending value at each length. The binary search then asks: 'what is the longest subsequence this new element can extend?' — which is equivalent to finding the rightmost tail smaller than the new element."
```

## Explainer

The Longest Increasing Subsequence problem asks: given a sequence of numbers, what is the length of the longest subsequence where each element is strictly larger than the one before it? A **subsequence** does not need to be contiguous — you can skip elements — but the relative order must be preserved. For example, in [3, 1, 4, 1, 5, 9, 2, 6], one LIS is [1, 4, 5, 9] with length 4, and another is [1, 4, 5, 6].

The O(n²) dynamic programming approach builds directly on the DP framework you already know. Define dp[i] as the length of the longest increasing subsequence that ends at index i. For each position i, look back at every earlier position j: if A[j] < A[i], then you could extend the subsequence ending at j by appending A[i], giving dp[i] = max(dp[i], dp[j] + 1). The base case is dp[i] = 1 for all i (every element is a subsequence of length 1 by itself). The answer is max(dp[0..n-1]). This is a textbook example of the "consider all previous states" DP pattern — each state depends on all prior states, yielding the quadratic runtime.

The O(n log n) optimization replaces the inner linear scan with a **binary search**. Maintain an array called `tails`, where tails[k] stores the smallest possible tail element of any increasing subsequence of length k+1 found so far. This array is always sorted — a crucial invariant. For each new element, binary search `tails` to find the leftmost position where the element could be placed: if it extends the longest subsequence found so far, append it; otherwise, replace the first tail value that is greater than or equal to it. The replacement keeps future options open by lowering the bar for extending subsequences of that length.

Walk through [3, 1, 4, 1, 5, 9, 2, 6]: after 3, tails = [3]. After 1, tails = [1] (1 replaces 3 — a subsequence of length 1 ending in 1 is more promising). After 4, tails = [1, 4]. After the second 1, no change. After 5, tails = [1, 4, 5]. After 9, tails = [1, 4, 5, 9]. After 2, tails = [1, 2, 5, 9] (2 replaces 4). After 6, tails = [1, 2, 5, 6] (6 replaces 9). The length of `tails` is 4, which is the LIS length. Note that `tails` itself is not necessarily an actual subsequence from the input — it is a bookkeeping structure that tracks the best possible endpoints. Each element triggers one binary search on the sorted `tails` array, so the total work is O(n log n).
