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

## Questions

```yaml
- question: "You implement a queue using a plain array: enqueue adds to the end, and dequeue removes from the front by shifting all remaining elements left. What is the time complexity of dequeue?"
  type: multiple-choice
  options:
    - "O(1), because you are only accessing the first element"
    - "O(log n), because the shift operation uses binary search"
    - "O(n), because shifting all remaining elements requires touching each one"
    - "O(1) amortized, because shifts are rare in practice"
  answer: 2
  explanation: "Shifting all remaining elements after removing the front element requires touching every remaining element — that's O(n). This makes the naive array queue inefficient for large queues or frequent dequeue operations. The fix is a circular buffer, which uses two index pointers that advance without ever shifting elements, achieving O(1) dequeue. Python's collections.deque similarly provides O(1) pops from both ends."

- question: "A circular buffer has capacity 5 and holds [_, A, B, C, _] with front=1 and rear=4. After one enqueue (D) and two dequeues, what are the new front and rear indices?"
  type: multiple-choice
  options:
    - "front=3, rear=0 (rear wrapped around using modular arithmetic)"
    - "front=1, rear=5 (rear advanced past the end)"
    - "front=3, rear=5 (both advanced without wrapping)"
    - "front=0, rear=4 (elements were shifted to fill the gap)"
  answer: 0
  explanation: "After enqueueing D: rear advances to index 4, placing D there, then rear becomes (4+1)%5 = 0, wrapping around. After two dequeues: front advances from 1 to 2 (removing A), then to 3 (removing B). Result: front=3, rear=0. No elements shifted — both indices simply advance with modular arithmetic. This is the core efficiency of the circular buffer: O(1) operations with no element movement."

- question: "A queue and a stack differ only in which end elements are added to — both structures remove elements from the same (front) end."
  type: true-false
  answer: false
  explanation: "Stacks use LIFO (last-in, first-out): elements are added and removed from the same end (the top). Queues use FIFO (first-in, first-out): elements are added to the back and removed from the front. They enforce fundamentally different orderings. A stack reverses insertion order; a queue preserves it. This distinction is why stacks work for depth-first search and function call tracking, while queues work for breadth-first search and scheduling."

- question: "Using a linked list with both head and tail pointers to implement a queue allows O(1) enqueue and O(1) dequeue with no fixed-capacity limitation."
  type: true-false
  answer: true
  explanation: "With both head and tail pointers: enqueue appends a new node at the tail (update the tail pointer — O(1)), and dequeue removes the node at the head (update the head pointer — O(1)). No shifting is ever needed. Unlike a circular buffer, a linked-list queue has no fixed capacity — it grows dynamically. The tradeoff is extra memory per node for the pointer storage, but the O(1) performance guarantee holds."

- question: "Why is a circular buffer the preferred array-based implementation of a queue, and what problem does it solve over a naive array approach?"
  type: short-answer
  answer: "A naive array queue makes dequeue O(n) because removing the front element requires shifting all remaining elements left. A circular buffer solves this by maintaining two indices — front and rear — that advance through the array using modular arithmetic (wrapping from the last index back to 0). Enqueue places a new element at rear and advances rear; dequeue reads from front and advances front. Neither operation touches any other element, so both are O(1). The array's physical positions are reused in a cycle, hence 'circular.'"
  explanation: "The key insight is that you don't need elements to be at physical position 0 to be logically 'first' — you just need a pointer to wherever the front currently is. By separating the logical front from the physical array position, you eliminate all shifting and achieve constant-time operations at the cost of a fixed capacity."
```

## Explainer

A **queue** enforces a simple discipline: the first item added is the first item removed. This is called **FIFO** — first-in, first-out — and it models the behavior of any real-world waiting line. When you join the back of a line at a grocery store and leave from the front, you are participating in a queue. The two fundamental operations are **enqueue** (add an element to the back) and **dequeue** (remove the element from the front), and both must run in O(1) time for the data structure to be useful.

You already know how arrays and linked lists work, and both can implement a queue — but with important differences. A linked list makes queues straightforward: maintain a pointer to both the head and the tail. Enqueue appends a new node at the tail, dequeue removes the node at the head, and both operations are O(1) with no wasted space. The downside is the per-node memory overhead from storing pointers.

An array-based queue is trickier. The naive approach — adding to the end and removing from the front by shifting all remaining elements left — makes dequeue O(n), which defeats the purpose. The solution is a **circular buffer** (also called a ring buffer): you maintain two indices, front and rear, that wrap around the array using modular arithmetic. When rear reaches the end of the array, it wraps to index 0 if space is available. Enqueue places an element at rear and advances it; dequeue reads from front and advances it. Both are O(1), and no elements ever need to shift. The tradeoff is that circular buffers have a fixed capacity — when full, you must either reject new elements or resize the underlying array (an amortized O(1) operation if you double the capacity).

Queues appear everywhere in computing. Breadth-first search — which you will encounter soon — depends on a queue to explore graph nodes level by level: you enqueue all unvisited neighbors, then dequeue the next node to process, guaranteeing that closer nodes are visited before farther ones. Operating systems use queues for CPU scheduling (processes wait their turn), print spoolers (documents print in submission order), and network packet buffering. The **priority queue** extends this concept by dequeuing based on priority rather than arrival order, but that requires a heap — a different data structure entirely — rather than a simple FIFO buffer.
