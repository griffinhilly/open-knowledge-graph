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
