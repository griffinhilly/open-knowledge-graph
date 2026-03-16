---
id: doubly-linked-lists
title: Doubly Linked Lists
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: singly-linked-lists
  type: hard
builds-toward:
- deques-double-ended-queues
tags:
- linked-lists
- bidirectional
- pointers
- nodes
stage: formal-systems
status: draft
---

# Doubly Linked Lists

## Core Idea
A doubly linked list extends singly linked lists by adding a back-pointer to the previous node in each node, enabling traversal in both directions. This allows finding the predecessor in O(1) instead of O(n) and simplifies deletion without needing the preceding node. The trade-off is extra space per node and more pointer updates during insertion and deletion.

## How It's Best Learned
Implement operations carefully, managing both forward and backward pointers precisely. Practice deletion (especially at boundaries) and bidirectional traversal. Trace through circular doubly linked lists to see how the structure elegantly handles wraparound.

## Common Misconceptions
- Doubly linked lists are always superior to singly linked (they use more memory, and many operations still cost O(n)).

## Explainer

In a singly linked list, each node holds a value and a pointer to the next node. This works well for forward traversal, but if you are at a node and need to access the previous one, you are stuck — you must restart from the head and walk forward until you find it, costing O(n). A **doubly linked list** fixes this by giving each node a second pointer: `prev`, pointing to the preceding node. Now every node knows both its successor and its predecessor, enabling O(1) movement in either direction.

The immediate payoff is in **deletion**. In a singly linked list, deleting a node requires access to the node before it (to rewrite that node's `next` pointer). If you only have a pointer to the node you want to delete, you need an O(n) traversal to find the predecessor. In a doubly linked list, the predecessor is right there: `node.prev`. Deletion becomes a constant-time pointer update: set `node.prev.next = node.next` and `node.next.prev = node.prev`. This makes doubly linked lists the natural choice for data structures where you need to remove elements from arbitrary positions quickly — LRU caches, text editor buffers, and undo histories all benefit from this property.

The cost is straightforward: every node now stores two pointers instead of one, roughly doubling the per-node overhead for small data. More importantly, every insertion and deletion must update **four** pointer connections instead of two (the new node's `prev` and `next`, plus the neighboring nodes' pointers). Getting these updates wrong — especially at the boundaries (head, tail, or empty list) — is the primary source of bugs. A common technique to simplify boundary handling is to use **sentinel nodes**: dummy head and tail nodes that are always present. With sentinels, you never insert or delete at a null boundary; every real node always has a valid `prev` and `next`, eliminating special cases.

A **circular doubly linked list** connects the last node's `next` to the first node and the first node's `prev` to the last, forming a ring. With a single sentinel node, the "head" and "tail" are just `sentinel.next` and `sentinel.prev`. This elegant structure means the empty list is simply the sentinel pointing to itself in both directions. Circular doubly linked lists are used internally by operating systems for process scheduling queues and by many standard library implementations (Python's `collections.deque`, Linux kernel's `list_head`). The key insight is that doubly linked lists trade memory for flexibility: when your algorithm needs fast bidirectional traversal or arbitrary-position deletion, the extra pointer per node is well worth it.
