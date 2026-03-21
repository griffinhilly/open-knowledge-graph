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

## Questions

```yaml
- question: "You have a direct reference to a node in the middle of a doubly linked list. What is the time complexity of removing that node?"
  type: multiple-choice
  options:
    - "O(n) — you must traverse to find the predecessor"
    - "O(1) — the node's prev pointer gives direct access to the predecessor"
    - "O(log n) — doubly linked lists use binary search for deletion"
    - "O(1) — doubly linked lists always support O(1) deletion regardless of how the node is found"
  answer: 1
  explanation: "Having a direct reference is the key condition. Because the node stores a prev pointer, you can access its predecessor in O(1) without traversal, making all pointer updates O(1). Option A describes singly linked list behavior. Option D is a subtle trap: doubly linked lists only give O(1) deletion *when you already have the node reference* — if you must search for the node first, that traversal is still O(n)."

- question: "Inserting a new node between nodes A and B in a doubly linked list requires updating how many pointers?"
  type: multiple-choice
  options:
    - "2 — one on A and one on B"
    - "3 — two on the new node and one on either A or B"
    - "4 — two on the new node and one each on A and B"
    - "6 — three on the new node and three on surrounding nodes"
  answer: 2
  explanation: "Inserting node N between A and B requires: (1) N.prev = A, (2) N.next = B, (3) A.next = N, (4) B.prev = N. That's four pointer updates. This is the core bookkeeping overhead of doubly linked lists — forgetting one of these four assignments corrupts the list silently and is the most common implementation bug."

- question: "A doubly linked list is slower than a singly linked list for searching by value, because it must maintain two pointers per node."
  type: true-false
  answer: false
  explanation: "Search by value requires traversing the list regardless of pointer structure — both singly and doubly linked lists require O(n) traversal to find a node by value. The extra prev pointer doesn't affect search speed. The overhead of doubly linked lists is in memory (one extra pointer per node) and in the number of pointer assignments during insertion and deletion — not in traversal."

- question: "In a doubly linked list implementation, sentinel (dummy) nodes at the head and tail eliminate all null-checking edge cases for boundary operations."
  type: true-false
  answer: true
  explanation: "Sentinel nodes ensure every real node always has a valid prev and next pointer, never null. Without sentinels, inserting at the head or tail requires special-case null checks. With a circular sentinel arrangement, the same four-pointer insertion logic works identically whether inserting in the middle or at either end — the sentinel's pointers stand in for the 'before head' and 'after tail' positions."

- question: "Why is a doubly linked list often combined with a hash map in practical implementations like LRU caches? What does each data structure contribute?"
  type: short-answer
  answer: "The hash map provides O(1) lookup by key — finding the specific node to operate on. The doubly linked list provides O(1) removal and reordering of that node once found, because the prev pointer gives direct access to the predecessor. Neither structure alone achieves both goals: a hash map can't maintain order, and a doubly linked list alone requires O(n) search to find a node by key."
  explanation: "This combination is the canonical LRU cache solution. The hash map indexes nodes by key so you jump directly to the node in O(1). The doubly linked list maintains recency order so you can move an accessed node to the front, or evict the tail (least recently used) node, in O(1). Together they achieve O(1) for all three LRU operations: lookup, insert, and eviction."
```

## Explainer

From your study of linked list variants, you know that a singly linked list has one pointer per node — a `next` pointer that leads forward through the chain. This works well for sequential traversal, but it creates an asymmetry: moving forward is O(1) per step, but there's no way to move backward without starting over from the head. A **doubly linked list** fixes this by adding a second pointer, `prev`, to each node. Every node now knows both its successor and its predecessor, creating a chain you can walk in either direction.

The most important consequence of the `prev` pointer is that **deletion becomes O(1) when you already have a reference to the node**. In a singly linked list, deleting a node requires finding its predecessor first — which means traversing from the head, an O(n) operation. With a doubly linked list, the predecessor is right there in `node.prev`. You simply set `node.prev.next = node.next` and `node.next.prev = node.prev`, and the node is unlinked. This is why doubly linked lists are the standard choice for implementing LRU caches, undo histories, and any structure where you frequently need to remove an element from the middle given a direct pointer to it.

The tradeoff is bookkeeping. Every insertion and deletion must update **two pointers per affected node** instead of one. Inserting a new node between A and B requires four pointer updates: set `new.prev = A`, set `new.next = B`, set `A.next = new`, and set `B.prev = new`. Getting the order of these updates wrong — or forgetting one — is the most common source of bugs. A useful defensive technique is the **sentinel node** (or dummy node): a special node that sits at both ends of the list (in a circular arrangement, the sentinel's `next` points to the first real element and its `prev` points to the last). Sentinels eliminate all the null-checking edge cases for empty lists and boundary operations, because every real node always has a valid `prev` and `next`.

In practice, doubly linked lists are most valuable when combined with another data structure that provides fast lookup. A hash map can give you O(1) access to a node by key, and then the doubly linked list gives you O(1) removal and reordering of that node — this combination is exactly how LRU caches work. If your use case only involves forward traversal, appending, or stack/queue operations, a singly linked list or a deque is simpler and uses less memory per node.
