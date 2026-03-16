---
id: doubly-linked-list-operations
title: 'Doubly Linked Lists: Structure and Operations'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: linked-list-singly-doubly-circular
  type: hard
builds-toward:
- deque-double-ended-queue-operations
tags:
- linked-lists
- pointers
- bidirectional
stage: formal-systems
status: draft
---

# Doubly Linked Lists: Structure and Operations

## Core Idea
Doubly linked lists maintain forward and backward pointers, enabling O(1) traversal in both directions and O(1) removal given a node reference (since you have the predecessor). The tradeoff is extra space per node and overhead when updating two pointers.

## How It's Best Learned
Implement insert, delete, and reverse operations. Observe how backward pointers simplify removal and how circular doubly linked lists enable efficient deque operations.

## Common Misconceptions
- Thinking doubly linked lists eliminate the O(1) removal advantage when you don't have a pointer to the node.
- Forgetting to update both pointers during insertion/deletion, causing corruption.
- Assuming bidirectional traversal is always needed; singly linked lists often suffice.

## Explainer

From your study of linked list variants, you know that a singly linked list has one pointer per node — a `next` pointer that leads forward through the chain. This works well for sequential traversal, but it creates an asymmetry: moving forward is O(1) per step, but there's no way to move backward without starting over from the head. A **doubly linked list** fixes this by adding a second pointer, `prev`, to each node. Every node now knows both its successor and its predecessor, creating a chain you can walk in either direction.

The most important consequence of the `prev` pointer is that **deletion becomes O(1) when you already have a reference to the node**. In a singly linked list, deleting a node requires finding its predecessor first — which means traversing from the head, an O(n) operation. With a doubly linked list, the predecessor is right there in `node.prev`. You simply set `node.prev.next = node.next` and `node.next.prev = node.prev`, and the node is unlinked. This is why doubly linked lists are the standard choice for implementing LRU caches, undo histories, and any structure where you frequently need to remove an element from the middle given a direct pointer to it.

The tradeoff is bookkeeping. Every insertion and deletion must update **two pointers per affected node** instead of one. Inserting a new node between A and B requires four pointer updates: set `new.prev = A`, set `new.next = B`, set `A.next = new`, and set `B.prev = new`. Getting the order of these updates wrong — or forgetting one — is the most common source of bugs. A useful defensive technique is the **sentinel node** (or dummy node): a special node that sits at both ends of the list (in a circular arrangement, the sentinel's `next` points to the first real element and its `prev` points to the last). Sentinels eliminate all the null-checking edge cases for empty lists and boundary operations, because every real node always has a valid `prev` and `next`.

In practice, doubly linked lists are most valuable when combined with another data structure that provides fast lookup. A hash map can give you O(1) access to a node by key, and then the doubly linked list gives you O(1) removal and reordering of that node — this combination is exactly how LRU caches work. If your use case only involves forward traversal, appending, or stack/queue operations, a singly linked list or a deque is simpler and uses less memory per node.
