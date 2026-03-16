---
id: queues-data-structure
title: Queues
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: linked-lists
  type: soft
builds-toward:
- breadth-first-search
- heaps-and-priority-queues
tags:
- queue
- FIFO
- data-structures
- enqueue-dequeue
stage: formal-systems
status: validated
---

# Queues

## Core Idea
A queue is a first-in, first-out (FIFO) data structure that supports enqueue (add to back) and dequeue (remove from front), both in O(1) time. Queues model real-world waiting lines, print spoolers, and process scheduling. A circular buffer (ring buffer) efficiently implements a queue using a fixed-size array without shifting elements. Priority queues extend this concept by dequeuing based on priority rather than arrival order.

## How It's Best Learned
Implement a queue using a linked list and then using a circular array with modular index arithmetic. Study how BFS uses a queue to explore graph nodes level by level.

## Common Misconceptions
- A naive array-based queue that shifts elements on dequeue is O(n), not O(1); use a circular buffer or linked list.
- Dequeuing from the front of a Python list is O(n) — use collections.deque for O(1) pops from both ends.

## Explainer

A **queue** enforces a simple discipline: the first item added is the first item removed. This is called **FIFO** — first-in, first-out — and it models the behavior of any real-world waiting line. When you join the back of a line at a grocery store and leave from the front, you are participating in a queue. The two fundamental operations are **enqueue** (add an element to the back) and **dequeue** (remove the element from the front), and both must run in O(1) time for the data structure to be useful.

You already know how arrays and linked lists work, and both can implement a queue — but with important differences. A linked list makes queues straightforward: maintain a pointer to both the head and the tail. Enqueue appends a new node at the tail, dequeue removes the node at the head, and both operations are O(1) with no wasted space. The downside is the per-node memory overhead from storing pointers.

An array-based queue is trickier. The naive approach — adding to the end and removing from the front by shifting all remaining elements left — makes dequeue O(n), which defeats the purpose. The solution is a **circular buffer** (also called a ring buffer): you maintain two indices, front and rear, that wrap around the array using modular arithmetic. When rear reaches the end of the array, it wraps to index 0 if space is available. Enqueue places an element at rear and advances it; dequeue reads from front and advances it. Both are O(1), and no elements ever need to shift. The tradeoff is that circular buffers have a fixed capacity — when full, you must either reject new elements or resize the underlying array (an amortized O(1) operation if you double the capacity).

Queues appear everywhere in computing. Breadth-first search — which you will encounter soon — depends on a queue to explore graph nodes level by level: you enqueue all unvisited neighbors, then dequeue the next node to process, guaranteeing that closer nodes are visited before farther ones. Operating systems use queues for CPU scheduling (processes wait their turn), print spoolers (documents print in submission order), and network packet buffering. The **priority queue** extends this concept by dequeuing based on priority rather than arrival order, but that requires a heap — a different data structure entirely — rather than a simple FIFO buffer.
