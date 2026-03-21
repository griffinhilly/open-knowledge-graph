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

## Questions

```yaml
- question: "You need to find the length of the longest contiguous subarray with a sum at most K in an array of positive integers. Which technique is most appropriate?"
  type: multiple-choice
  options:
    - "Binary search on the answer, because the subarray length can be searched directly"
    - "Sliding window, because positive integers create a monotonic relationship between window size and sum"
    - "Converging two pointers, because you need to sort the array first"
    - "Brute force O(n²), because subarrays have no exploitable structure"
  answer: 1
  explanation: "Sliding window works here because positive integers give monotonicity: expanding the window (moving right pointer right) can only increase the sum; contracting it (moving left pointer right) can only decrease it. This one-directional relationship means each pointer decision permanently eliminates states, making O(n) possible. Without this monotonic structure — for example, if the array contained negative numbers — the sliding window would not apply and brute force or prefix sums would be needed."

- question: "In a sliding window, both the left and right pointers visit each element, so each element is processed twice. Why does this give O(n) rather than O(n²) time complexity?"
  type: multiple-choice
  options:
    - "It is actually O(n log n) — the O(n) claim is an approximation"
    - "Elements processed by the left pointer are cheaper, so the average cost is O(1) per element"
    - "Both pointers only move forward, so across the entire run each traverses the array at most once — 2n total steps"
    - "The window size is bounded by a constant, so the inner loop cost is O(1)"
  answer: 2
  explanation: "The critical invariant: neither pointer ever moves backward. The right pointer advances from index 0 to n−1 (n steps total). The left pointer advances from index 0 to at most n−1 (n steps total). No matter how many expand-contract cycles occur, the total work is at most 2n steps, giving O(n). In a naive nested loop the inner index can restart from any position — allowing O(n²) work. The monotonic forward movement is what prevents revisiting past states."

- question: "The two-pointer technique can be applied to find a pair of elements that sum to a target in any array of integers, regardless of whether the array is sorted."
  type: true-false
  answer: false
  explanation: "False. The converging two-pointer technique requires a sorted array (or a monotonic structure). When you move the left pointer right, you need to know this increases the sum — ruling out smaller left values. In an unsorted array, moving left forward might increase or decrease the sum unpredictably, so you cannot safely eliminate states. Without monotonicity the technique degenerates to brute force. Sorting first then applying two pointers is valid, but the sorted order is what makes the technique work."

- question: "In the sliding window pattern, the left pointer may need to move backward in some cases to restore a violated invariant."
  type: true-false
  answer: false
  explanation: "False. The left pointer only ever moves forward — this is non-negotiable. Moving it backward would reintroduce previously removed elements and break the O(n) guarantee by potentially creating an infinite loop. When the window's invariant is violated, you advance the left pointer (shrink the window) until the invariant is restored. This one-directional movement is precisely what ensures each element is visited at most twice, keeping the algorithm linear."

- question: "What is the key structural property that makes two pointers or sliding window applicable to a problem, and why does this property allow you to avoid revisiting past states?"
  type: short-answer
  answer: "The key property is monotonicity: moving a pointer in a given direction has a predictable, one-directional effect on the quantity being optimized or the condition being checked. Because each pointer decision unambiguously moves the quantity in one direction, any state 'behind' the pointer can be permanently ruled out — it cannot be part of an optimal answer that the current state does not already account for."
  explanation: "Without monotonicity, a pointer decision might need to be undone (moving backward), which eliminates the linear-time guarantee. With monotonicity, each step eliminates an entire region of the search space. In a sorted two-sum, moving the left pointer forward can only increase the sum — all pairs with the old left value are definitively handled. In a sliding window, expanding can only add to the aggregate. This structural guarantee transforms O(n²) into O(n)."
```

## Explainer

Many array problems have a brute-force solution that checks all pairs or all subarrays, running in O(n²) or worse. The **two-pointer technique** eliminates redundant work by maintaining two indices that move through the array in a coordinated way, reducing the time to O(n). The key insight is that certain structural properties of the problem — sortedness, monotonicity, or contiguity — let you rule out large regions of the search space as one pointer advances.

The classic example is finding two numbers in a sorted array that sum to a target. Place one pointer at the start (left) and one at the end (right). If their sum is too small, move left forward — you need a larger value. If the sum is too large, move right backward. Because the array is sorted, each pointer movement eliminates an entire row or column of the implicit pair matrix. The pointers converge toward each other and meet in at most n steps. Compare this to the naive approach of checking all n² pairs: the sorted structure lets each pointer decision discard many candidates at once.

The **sliding window** is a specialized two-pointer pattern where both pointers move in the same direction, defining a contiguous subarray (the "window") that expands and contracts. You advance the right pointer to grow the window until some condition is met or violated, then advance the left pointer to shrink it. The critical invariant is that the left pointer never moves backward — both pointers only move forward, so each element is visited at most twice (once by each pointer), giving O(n) total time. For example, to find the longest substring without repeating characters, expand the window rightward until a duplicate appears, then contract from the left until the duplicate is removed.

What makes these patterns work is **monotonicity in the decision**. In the converging two-pointer pattern, moving left forward can only increase the sum (in a sorted array), and moving right backward can only decrease it. In the sliding window, expanding the window can only add elements (potentially making a condition harder to satisfy), and contracting can only remove them. This one-directional effect means you never need to revisit a previous state — the pointers encode all the information about what you've already eliminated. When you encounter a new array problem, ask: "Is there a monotonic relationship between pointer movement and the quantity I'm optimizing?" If yes, two pointers or sliding window likely applies.
