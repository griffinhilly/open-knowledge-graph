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
status: draft
---

# Deques and Double-Ended Queues

## Core Idea
A deque (double-ended queue) supports O(1) insertion and deletion at both front and back, combining stack and queue properties. Deques are typically implemented with circular arrays or doubly linked lists and are essential for sliding-window problems, efficient iterative DFS, and algorithms requiring bidirectional access.

## How It's Best Learned
Implement using both circular arrays (handling wraparound indices) and doubly linked lists; compare space and time trade-offs. Solve sliding-window maximum and implement DFS iteratively using a deque to appreciate its utility.

## Common Misconceptions
- Deques are slower than specialized queues or stacks (both ends are O(1) with the right implementation). - Deques have niche applications (they are fundamental to many algorithms).

## Explainer

You already know that a queue supports FIFO access — enqueue at the back, dequeue from the front — and that a stack supports LIFO access at one end. A **deque** (pronounced "deck") generalizes both: it allows O(1) insertion and removal at *both* the front and the back. This means a deque can act as a queue (add back, remove front), a stack (add back, remove back), or something in between, depending on which operations you use. It is the most flexible of the basic linear data structures.

The two standard implementations mirror what you already know from queues. A **circular array** deque uses a fixed-size buffer with two indices — front and back — that wrap around when they reach the ends of the array. Push-front decrements the front index (wrapping to the end of the array if needed); push-back increments the back index. Both are O(1). When the array fills, you resize by allocating a larger array and copying elements, giving O(1) amortized cost. A **doubly linked list** implementation uses your prerequisite knowledge directly: each node has prev and next pointers, so inserting or removing at either end is a constant-time pointer update with no wraparound logic needed. The tradeoff is that linked lists use more memory per element (two pointers per node) and have worse cache locality, while circular arrays are compact and cache-friendly but require occasional resizing.

The deque's most celebrated algorithmic application is the **sliding window maximum** (or minimum) problem. Given an array and a window of size k that slides across it, you need the maximum value in each window position. A naive approach checks all k elements per window — O(nk) total. A deque solves this in O(n): maintain a deque of indices whose values are in decreasing order. As the window slides, you remove from the front any index that has fallen out of the window, remove from the back any index whose value is less than or equal to the new element (since it can never be the maximum), then push the new index onto the back. The front of the deque always holds the index of the current window's maximum. This works precisely because the deque allows efficient access at both ends.

Deques also appear in algorithms where you need to process elements from either direction — for example, implementing iterative depth-first search where you push to and pop from the same end (using the deque as a stack), or breadth-first search variants where you add high-priority items to the front and normal items to the back (a pattern called a "0-1 BFS" for graphs with edge weights of only 0 or 1). In most languages, the standard library provides a deque: Python's `collections.deque`, C++'s `std::deque`, and Java's `ArrayDeque` are all optimized implementations ready for use.
