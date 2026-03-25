---
id: queue-adt-circular-implementation
title: "Queue ADT: Circular Array and Linked-List Implementations"
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: queues-data-structure
  type: hard
- id: arrays-and-lists
  type: hard
- id: linked-lists
  type: hard
builds-toward:
- deques-double-ended-queues
- breadth-first-search
tags:
- queue
- adt
- data-structure
stage: formal-systems
status: validated
---
# Queue ADT: Circular Array and Linked-List Implementations

## Core Idea
A queue is a FIFO (First-In-First-Out) data structure supporting enqueue (insert at rear) and dequeue (remove from front). Circular array implementations wrap around to reuse space; linked-list implementations maintain head and tail pointers.

## How It's Best Learned
Implement both array and linked-list queues. Trace enqueue and dequeue operations step-by-step. For circular arrays, understand modular arithmetic (index = (index + 1) % capacity). Compare performance and memory usage.

## Questions

```yaml
- question: "A naive array-based queue always uses index 0 as the front and shifts all remaining elements left on every dequeue. After 10,000 enqueue-then-dequeue operations on a queue that never holds more than 5 elements at a time, what is the overall time complexity behavior?"
  type: multiple-choice
  options:
    - "O(n) per dequeue due to shifting, where n is the current queue size — even if the queue is small, each shift still occurs"
    - "O(1) per operation because the queue size stays bounded by 5"
    - "O(log n) because the array shrinks as elements are removed"
    - "O(n) per enqueue only; dequeue is always O(1)"
  answer: 0
  explanation: "In a naive implementation, dequeue from index 0 requires shifting every remaining element one position to the left. If the queue holds k elements, that is k shifts — O(k) work. Even if k stays small (like 5), the cost is still O(n) in the general case. The circular array eliminates this by moving a pointer instead of moving data."

- question: "A circular array queue has capacity 5. The front index is 3 and the rear index is 1 (elements wrap around the array end). What index should the next enqueue write to, and how is it computed?"
  type: multiple-choice
  options:
    - "Index 2, computed as (rear + 1) % capacity = (1 + 1) % 5"
    - "Index 2, but only if there is a gap between rear and front — otherwise the queue must resize first"
    - "Index 6, by extending the array past its current end"
    - "Index 0, because rear has passed the midpoint of the array"
  answer: 0
  explanation: "The circular array uses modular arithmetic: next_rear = (rear + 1) % capacity. This wraps the index back to the beginning of the array when it reaches the end, treating the array as a ring. The key insight is that 'where the array ends' is arbitrary — the logical structure is circular, not linear."

- question: "In a circular array queue, both enqueue and dequeue run in O(1) time."
  type: true-false
  answer: true
  explanation: "True. Neither operation moves existing elements. Enqueue writes to the rear index and increments it (with wrap-around). Dequeue reads from the front index and increments it. All work is constant regardless of queue size — which is exactly the improvement over the naive shifting approach."

- question: "A linked-list queue is always more efficient than a circular array queue because it avoids the need for resizing."
  type: true-false
  answer: false
  explanation: "False. The comparison is more nuanced. A linked-list queue avoids resizing but incurs per-element heap allocation overhead and stores data in non-contiguous memory, hurting cache performance. A circular array keeps all elements contiguous in memory, which is cache-friendly and avoids allocation costs — at the price of a fixed capacity or occasional resizing. Neither is universally superior."

- question: "Why does a circular array solve the performance problem of a naive array-based queue, and what is the single conceptual shift that makes it work?"
  type: short-answer
  answer: "A naive queue dequeues from index 0 and must shift every remaining element left — O(n) work. The circular array replaces 'shift the data' with 'move a pointer': front and rear are just indices that advance with modular arithmetic, (index + 1) % capacity, so they wrap around to the beginning when they reach the end. The conceptual shift is treating the array as a ring rather than a line — there is no fixed start or end, just two moving pointers. Both enqueue and dequeue become O(1) because no elements are ever moved."
  explanation: "The modular arithmetic is the mechanical implementation of the circular idea. Understanding this derivation (not just memorizing the formula) is what lets you handle the full vs. empty ambiguity and adapt the approach to related structures like deques."
```

## Explainer

A **queue** enforces a single behavioral rule: the first element added is the first one removed. This **FIFO** (First-In, First-Out) discipline shows up everywhere — print jobs waiting for a printer, customers in a checkout line, network packets arriving at a router. You already understand arrays and linked lists as concrete data structures; the queue is an abstraction built on top of either one, restricting how you interact with the underlying storage.

The linked-list implementation is straightforward. You maintain a **head** pointer (where dequeues happen) and a **tail** pointer (where enqueues happen). Enqueue creates a new node, attaches it after the current tail, and updates the tail pointer. Dequeue reads the head node's value, advances the head pointer to the next node, and frees the old head. Both operations are O(1) because you never traverse the list — you always work at the endpoints.

The array-based implementation is trickier. A naive approach uses index 0 as the front and tracks where the rear is. Enqueue appends to the rear in O(1), but dequeue from index 0 forces you to shift every remaining element left — O(n) work. The **circular array** solves this elegantly. Instead of shifting, you maintain two indices — `front` and `rear` — and let them wrap around the end of the array using modular arithmetic: `next = (current + 1) % capacity`. Picture the array as a clock face rather than a ruler. When `rear` reaches the last slot and there's free space at the beginning (from prior dequeues), it wraps to index 0 and keeps filling. Both enqueue and dequeue become O(1) because neither operation moves any existing elements.

The one subtlety with circular arrays is distinguishing "full" from "empty." Both conditions look the same if `front == rear`. The standard solutions are to keep a separate count, waste one slot (the queue is full when the next rear position equals front), or use a boolean flag. Each approach trades a tiny amount of space or bookkeeping for the ability to tell the two states apart. Compared to the linked-list version, the circular array avoids per-element memory allocation overhead and keeps data in contiguous memory (better cache performance), but it requires a fixed capacity or occasional resizing.
