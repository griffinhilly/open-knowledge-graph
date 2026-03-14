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
