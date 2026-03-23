---
id: deques-double-ended-queues
title: Deques and Double-Ended Queues
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: doubly-linked-lists
  type: soft
- id: queues-data-structure
  type: hard
tags:
- deques
- stacks
- queues
- double-ended
- sliding-window
stage: formal-systems
status: validated
---

# Deques and Double-Ended Queues

## Core Idea
A deque (double-ended queue) supports O(1) insertion and deletion at both front and back, combining stack and queue properties. Deques are typically implemented with circular arrays or doubly linked lists and are essential for sliding-window problems, efficient iterative DFS, and algorithms requiring bidirectional access.

## How It's Best Learned
Implement using both circular arrays (handling wraparound indices) and doubly linked lists; compare space and time trade-offs. Solve sliding-window maximum and implement DFS iteratively using a deque to appreciate its utility.

## Common Misconceptions
- Deques are slower than specialized queues or stacks (both ends are O(1) with the right implementation). - Deques have niche applications (they are fundamental to many algorithms).

## Questions

```yaml
- question: "You need to find the maximum value in every window of size k as it slides across an array of n elements. Which approach correctly uses a deque to solve this in O(n)?"
  type: multiple-choice
  options:
    - "Store all k elements in the deque for each window and scan for the max — O(k) per window"
    - "Maintain a deque of indices in decreasing value order, removing expired indices from the front and smaller indices from the back as each new element arrives"
    - "Use the deque as a sorted set, inserting in order at each step"
    - "Push all elements onto the deque and pop the front k times per window"
  answer: 1
  explanation: "The key insight is that the deque's bidirectional O(1) access enables a clever invariant: the front always holds the index of the current maximum. When a new element arrives, you remove from the back any index whose value is ≤ the new element (they can never be a future maximum), and remove from the front any index that has slid out of the window. This processes each element at most twice — once pushed, once popped — giving O(n) total. Option A is the naive O(nk) approach; options C and D misuse the deque."

- question: "A deque is implemented with a circular array. Which statement best describes the trade-off compared to a doubly linked list implementation?"
  type: multiple-choice
  options:
    - "The circular array is slower because it must check for wraparound on every operation"
    - "The doubly linked list has better cache locality because elements are stored sequentially in memory"
    - "The circular array has better cache locality and avoids per-element pointer overhead, but requires occasional resizing"
    - "Both implementations have identical performance characteristics"
  answer: 2
  explanation: "Cache locality is the key difference. A circular array stores elements contiguously in memory, so sequential access benefits from CPU cache lines. A doubly linked list scatters nodes across the heap; each pointer dereference may cause a cache miss. The linked list trades this for no resizing overhead and simpler wraparound logic, but the circular array's cache efficiency typically wins in practice. The wraparound check in a circular array is a single modulo or branch — negligible compared to cache misses."

- question: "A deque can simulate both a stack (LIFO) and a queue (FIFO) by choosing which ends to use for insertion and removal."
  type: true-false
  answer: true
  explanation: "This is precisely the deque's defining property. Use push-back and pop-back exclusively and it behaves as a stack. Use push-back and pop-front exclusively and it behaves as a FIFO queue. Use both ends freely and you get a structure neither a pure stack nor queue can express — for example, adding high-priority items to the front and normal items to the back (as in 0-1 BFS)."

- question: "A deque's O(1) performance at both ends makes it strictly slower than a dedicated stack or queue for applications that only need one-ended access."
  type: true-false
  answer: false
  explanation: "This is a common misconception. A deque with the right implementation (circular array or doubly linked list) performs single-ended operations in O(1) — identical to a stack or queue. There is no overhead for 'having' the extra capability if you don't use it. In practice, standard library deques (Python's collections.deque, Java's ArrayDeque) are often used even when only stack or queue behavior is needed."

- question: "Explain why a deque, rather than a simple queue or stack, is the right data structure for the sliding window maximum problem."
  type: short-answer
  answer: "The sliding window maximum requires removing expired elements from the front (the old maximum's index has left the window) and removing dominated elements from the back (any index with a value smaller than the new element can never become the maximum). These are two distinct removal operations at opposite ends — exactly what a deque supports in O(1). A queue only removes from one end; a stack from the other. Neither alone can express 'maintain a decreasing sequence while expiring old elements from the front.'"
  explanation: "The algorithm's elegance comes from the deque enforcing an invariant: elements are in decreasing order of value, and the front is always the current window's maximum. Both ends are actively used during every element insertion — the back is cleaned of dominated elements, and the front is checked for expiry. This is a pattern that appears in many sliding-window optimization problems and is the canonical demonstration of why deques are 'fundamental to many algorithms,' not niche."
```

## Explainer

You already know that a queue supports FIFO access — enqueue at the back, dequeue from the front — and that a stack supports LIFO access at one end. A **deque** (pronounced "deck") generalizes both: it allows O(1) insertion and removal at *both* the front and the back. This means a deque can act as a queue (add back, remove front), a stack (add back, remove back), or something in between, depending on which operations you use. It is the most flexible of the basic linear data structures.

The two standard implementations mirror what you already know from queues. A **circular array** deque uses a fixed-size buffer with two indices — front and back — that wrap around when they reach the ends of the array. Push-front decrements the front index (wrapping to the end of the array if needed); push-back increments the back index. Both are O(1). When the array fills, you resize by allocating a larger array and copying elements, giving O(1) amortized cost. A **doubly linked list** implementation uses your prerequisite knowledge directly: each node has prev and next pointers, so inserting or removing at either end is a constant-time pointer update with no wraparound logic needed. The tradeoff is that linked lists use more memory per element (two pointers per node) and have worse cache locality, while circular arrays are compact and cache-friendly but require occasional resizing.

The deque's most celebrated algorithmic application is the **sliding window maximum** (or minimum) problem. Given an array and a window of size k that slides across it, you need the maximum value in each window position. A naive approach checks all k elements per window — O(nk) total. A deque solves this in O(n): maintain a deque of indices whose values are in decreasing order. As the window slides, you remove from the front any index that has fallen out of the window, remove from the back any index whose value is less than or equal to the new element (since it can never be the maximum), then push the new index onto the back. The front of the deque always holds the index of the current window's maximum. This works precisely because the deque allows efficient access at both ends.

Deques also appear in algorithms where you need to process elements from either direction — for example, implementing iterative depth-first search where you push to and pop from the same end (using the deque as a stack), or breadth-first search variants where you add high-priority items to the front and normal items to the back (a pattern called a "0-1 BFS" for graphs with edge weights of only 0 or 1). In most languages, the standard library provides a deque: Python's `collections.deque`, C++'s `std::deque`, and Java's `ArrayDeque` are all optimized implementations ready for use.
