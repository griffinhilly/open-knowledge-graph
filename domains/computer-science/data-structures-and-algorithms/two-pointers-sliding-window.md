---
id: two-pointers-sliding-window
title: Two Pointers and Sliding Window
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: hard
- id: for-loops
  type: soft
tags:
- two-pointers
- sliding-window
- arrays
- optimization
stage: formal-systems
status: validated
---

# Two Pointers and Sliding Window

## Core Idea
The two-pointer technique uses two indices moving through an array to solve in O(n) time problems that naively require O(n²). The pointers may converge toward each other (e.g., two-sum in a sorted array) or move in the same direction (sliding window). A sliding window maintains a contiguous subarray of variable or fixed size, updating an aggregate as the window expands or contracts; applications include maximum subarray sum, longest substring without repeating characters, and minimum window substring. These patterns replace nested loops with a single linear pass.

## How It's Best Learned
Practice two-pointer on: two-sum in sorted array, container with most water. Practice sliding window on: longest substring without repeats, minimum window substring. For each, identify explicitly when the window should expand and when it should contract.

## Common Misconceptions
- Two pointers directly apply only to sorted arrays or problems with monotonic structure; they do not generalize to arbitrary array problems.
- The sliding window pattern does not require exactly two pointer variables — what matters is maintaining valid window boundaries, regardless of implementation.

## Explainer

Many array problems have a brute-force solution that checks all pairs or all subarrays, running in O(n²) or worse. The **two-pointer technique** eliminates redundant work by maintaining two indices that move through the array in a coordinated way, reducing the time to O(n). The key insight is that certain structural properties of the problem — sortedness, monotonicity, or contiguity — let you rule out large regions of the search space as one pointer advances.

The classic example is finding two numbers in a sorted array that sum to a target. Place one pointer at the start (left) and one at the end (right). If their sum is too small, move left forward — you need a larger value. If the sum is too large, move right backward. Because the array is sorted, each pointer movement eliminates an entire row or column of the implicit pair matrix. The pointers converge toward each other and meet in at most n steps. Compare this to the naive approach of checking all n² pairs: the sorted structure lets each pointer decision discard many candidates at once.

The **sliding window** is a specialized two-pointer pattern where both pointers move in the same direction, defining a contiguous subarray (the "window") that expands and contracts. You advance the right pointer to grow the window until some condition is met or violated, then advance the left pointer to shrink it. The critical invariant is that the left pointer never moves backward — both pointers only move forward, so each element is visited at most twice (once by each pointer), giving O(n) total time. For example, to find the longest substring without repeating characters, expand the window rightward until a duplicate appears, then contract from the left until the duplicate is removed.

What makes these patterns work is **monotonicity in the decision**. In the converging two-pointer pattern, moving left forward can only increase the sum (in a sorted array), and moving right backward can only decrease it. In the sliding window, expanding the window can only add elements (potentially making a condition harder to satisfy), and contracting can only remove them. This one-directional effect means you never need to revisit a previous state — the pointers encode all the information about what you've already eliminated. When you encounter a new array problem, ask: "Is there a monotonic relationship between pointer movement and the quantity I'm optimizing?" If yes, two pointers or sliding window likely applies.
