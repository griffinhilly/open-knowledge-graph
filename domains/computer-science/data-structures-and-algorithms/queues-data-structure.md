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
