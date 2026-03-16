---
id: queue-adt-circular-implementation
title: 'Queue ADT: Circular Array and Linked-List Implementations'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: linked-lists
  type: hard
builds-toward:
- deque-double-ended-queue-operations
- breadth-first-search
tags:
- queue
- adt
- data-structure
stage: formal-systems
status: draft
---

# Queue ADT: Circular Array and Linked-List Implementations

## Core Idea
A queue is a FIFO (First-In-First-Out) data structure supporting enqueue (insert at rear) and dequeue (remove from front). Circular array implementations wrap around to reuse space; linked-list implementations maintain head and tail pointers.

## How It's Best Learned
Implement both array and linked-list queues. Trace enqueue and dequeue operations step-by-step. For circular arrays, understand modular arithmetic (index = (index + 1) % capacity). Compare performance and memory usage.

## Explainer

A **queue** enforces a single behavioral rule: the first element added is the first one removed. This **FIFO** (First-In, First-Out) discipline shows up everywhere — print jobs waiting for a printer, customers in a checkout line, network packets arriving at a router. You already understand arrays and linked lists as concrete data structures; the queue is an abstraction built on top of either one, restricting how you interact with the underlying storage.

The linked-list implementation is straightforward. You maintain a **head** pointer (where dequeues happen) and a **tail** pointer (where enqueues happen). Enqueue creates a new node, attaches it after the current tail, and updates the tail pointer. Dequeue reads the head node's value, advances the head pointer to the next node, and frees the old head. Both operations are O(1) because you never traverse the list — you always work at the endpoints.

The array-based implementation is trickier. A naive approach uses index 0 as the front and tracks where the rear is. Enqueue appends to the rear in O(1), but dequeue from index 0 forces you to shift every remaining element left — O(n) work. The **circular array** solves this elegantly. Instead of shifting, you maintain two indices — `front` and `rear` — and let them wrap around the end of the array using modular arithmetic: `next = (current + 1) % capacity`. Picture the array as a clock face rather than a ruler. When `rear` reaches the last slot and there's free space at the beginning (from prior dequeues), it wraps to index 0 and keeps filling. Both enqueue and dequeue become O(1) because neither operation moves any existing elements.

The one subtlety with circular arrays is distinguishing "full" from "empty." Both conditions look the same if `front == rear`. The standard solutions are to keep a separate count, waste one slot (the queue is full when the next rear position equals front), or use a boolean flag. Each approach trades a tiny amount of space or bookkeeping for the ability to tell the two states apart. Compared to the linked-list version, the circular array avoids per-element memory allocation overhead and keeps data in contiguous memory (better cache performance), but it requires a fixed capacity or occasional resizing.
