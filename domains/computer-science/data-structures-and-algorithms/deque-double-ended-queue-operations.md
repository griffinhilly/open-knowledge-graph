---
id: deque-double-ended-queue-operations
title: 'Deque: Double-Ended Queue Operations and Applications'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: queue-adt-circular-implementation
  type: hard
builds-toward:
- two-pointers-sliding-window
tags:
- deque
- queue
- data-structure
stage: formal-systems
status: draft
---

# Deque: Double-Ended Queue Operations and Applications

## Core Idea
A deque (double-ended queue) allows insertion and deletion at both ends. It generalizes both stacks and queues and is useful for sliding-window algorithms, palindrome detection, and work-stealing schedulers.

## Explainer

From your understanding of queues and their circular array implementation, you know that a queue supports insertion at the rear and removal from the front — a strict first-in, first-out discipline. A **deque (double-ended queue)**, pronounced "deck," removes this restriction: you can insert and remove elements at *both* the front and the rear, all in O(1) time. This makes the deque a more general structure that can behave as a queue (add rear, remove front), a stack (add front, remove front), or something in between.

The most common implementation extends the **circular array** approach you already know. Instead of tracking just a front and rear index, the deque maintains both and allows them to move in either direction. To push an element onto the front, you decrement the front index (wrapping around to the end of the array if necessary) and place the element there. To push onto the rear, you place the element at the rear index and increment it. Popping from either end is the reverse. The circular array ensures that all four operations — `pushFront`, `pushBack`, `popFront`, `popBack` — run in amortized O(1) time. When the array fills up, you resize and copy, just as with a dynamic array. An alternative implementation uses a **doubly-linked list**, which provides O(1) worst-case for all operations without resizing, at the cost of higher per-element memory overhead and worse cache locality.

The deque's power becomes clear in algorithmic applications. The classic example is the **sliding window maximum** problem: given an array and a window size k, find the maximum element in each window as it slides across the array. A naive approach checks all k elements per window position, giving O(nk) time. With a deque, you maintain a decreasing sequence of *indices* — elements enter at the rear and are removed from the rear whenever a larger element arrives (since they can never be the maximum while the larger element is in the window), while elements that slide out of the window are removed from the front. This gives O(n) total time because each element enters and leaves the deque at most once.

Deques also appear in systems programming. In **work-stealing schedulers** (used by parallel runtimes like Intel TBB and Java's ForkJoinPool), each thread maintains a deque of tasks. The owning thread pushes and pops tasks from one end (like a stack, for locality), while idle threads steal tasks from the other end. This design minimizes contention because the owner and the thief operate on opposite ends of the deque. In standard libraries, most languages provide a deque: Python's `collections.deque`, C++'s `std::deque`, and Java's `ArrayDeque` are all built on these principles.
