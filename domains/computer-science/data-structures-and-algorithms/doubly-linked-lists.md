---
id: doubly-linked-lists
title: Doubly Linked Lists
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: linked-lists
  type: hard
- id: circular-linked-lists
  type: soft
builds-toward:
- deques-double-ended-queues
tags:
- linked-lists
- bidirectional
- pointers
- nodes
stage: formal-systems
status: validated
---
# Doubly Linked Lists

## Core Idea
A doubly linked list extends singly linked lists by adding a back-pointer to the previous node in each node, enabling traversal in both directions. This allows finding the predecessor in O(1) instead of O(n) and simplifies deletion without needing the preceding node. The trade-off is extra space per node and more pointer updates during insertion and deletion.

## How It's Best Learned
Implement operations carefully, managing both forward and backward pointers precisely. Practice deletion (especially at boundaries) and bidirectional traversal. Trace through circular doubly linked lists to see how the structure elegantly handles wraparound.

## Common Misconceptions
- Doubly linked lists are always superior to singly linked (they use more memory, and many operations still cost O(n)).

## Questions

```yaml
- question: "You have a pointer to a node in the middle of a list and need to delete it. The operation is O(n) for a singly linked list but O(1) for a doubly linked list. What makes the difference?"
  type: multiple-choice
  options:
    - "Doubly linked lists store sorted data, enabling binary search for the predecessor"
    - "Each node's `prev` pointer gives immediate access to the predecessor, which is all you need to relink the list"
    - "Doubly linked lists use arrays internally, making deletion index-based and faster"
    - "Doubly linked lists avoid the need to update any pointers during deletion"
  answer: 1
  explanation: "To delete a node, you must update the predecessor's `next` pointer to skip the deleted node. In a singly linked list, finding the predecessor requires traversing from the head — O(n). In a doubly linked list, `node.prev` is the predecessor directly, so you access it in O(1). You then set `node.prev.next = node.next` and `node.next.prev = node.prev`. The `prev` pointer doesn't eliminate the pointer update — it eliminates the search for which node to update."

- question: "How many pointer connections must be updated when inserting a new node into the middle of a doubly linked list?"
  type: multiple-choice
  options:
    - "1 — only the new node's `next` pointer"
    - "2 — the new node's `next` and the predecessor's `next`"
    - "4 — the new node's `prev` and `next`, plus the predecessor's `next` and the successor's `prev`"
    - "6 — the new node plus all three neighbors' pointers in both directions"
  answer: 2
  explanation: "Inserting node N between nodes A and B requires: (1) N.next = B, (2) N.prev = A, (3) A.next = N, (4) B.prev = N. That is 4 pointer updates. A singly linked list insertion requires only 2. The doubled update count is the direct cost of the extra flexibility. Missing any of the four — especially on boundary cases — is the primary source of bugs in doubly linked list implementations."

- question: "Deleting a node in a doubly linked list, given only a pointer to that node, can be done in O(1) time."
  type: true-false
  answer: true
  explanation: "This is the central advantage of doubly linked lists. With `node.prev` and `node.next` available in O(1), you can rewire the surrounding nodes directly: set `node.prev.next = node.next` and `node.next.prev = node.prev`. No traversal needed. This property makes doubly linked lists the natural choice for LRU caches, where you need to remove an arbitrary node immediately upon a cache hit — singly linked lists cannot do this in O(1)."

- question: "Doubly linked lists are strictly superior to singly linked lists because the back pointer enables faster operations across the board."
  type: true-false
  answer: false
  explanation: "Doubly linked lists improve only specific operations — primarily arbitrary deletion and backward traversal. Many operations (searching for a value, accessing the k-th element) still cost O(n) because the structure is still a linked chain. Additionally, doubly linked lists consume more memory per node and require more pointer updates per insertion/deletion, increasing the chance of bugs. The right choice depends on the use case: if you need O(1) arbitrary deletion, use doubly linked; if memory is tight or you only traverse forward, singly linked may be better."

- question: "Why are sentinel nodes useful in doubly linked list implementations, and what problem do they solve?"
  type: short-answer
  answer: "Sentinel nodes are dummy head and tail nodes that are always present, even in an empty list. They eliminate special-case handling for insertions and deletions at the boundaries. Without sentinels, you must check whether the node being deleted is the head or tail before updating list pointers. With sentinels, every real node always has a valid `prev` and `next` (pointing to the sentinel at a boundary), so the same four-pointer update works for all positions uniformly. The empty list is simply the two sentinels pointing to each other."
  explanation: "Sentinel nodes exemplify a broader principle: adding a small amount of overhead (two extra nodes) to eliminate disproportionately complex special-case code. Fewer code paths means fewer bugs. Real-world implementations including Python's `collections.deque` and the Linux kernel's `list_head` use this pattern for exactly this reason."
```

## Explainer

In a singly linked list, each node holds a value and a pointer to the next node. This works well for forward traversal, but if you are at a node and need to access the previous one, you are stuck — you must restart from the head and walk forward until you find it, costing O(n). A **doubly linked list** fixes this by giving each node a second pointer: `prev`, pointing to the preceding node. Now every node knows both its successor and its predecessor, enabling O(1) movement in either direction.

The immediate payoff is in **deletion**. In a singly linked list, deleting a node requires access to the node before it (to rewrite that node's `next` pointer). If you only have a pointer to the node you want to delete, you need an O(n) traversal to find the predecessor. In a doubly linked list, the predecessor is right there: `node.prev`. Deletion becomes a constant-time pointer update: set `node.prev.next = node.next` and `node.next.prev = node.prev`. This makes doubly linked lists the natural choice for data structures where you need to remove elements from arbitrary positions quickly — LRU caches, text editor buffers, and undo histories all benefit from this property.

The cost is straightforward: every node now stores two pointers instead of one, roughly doubling the per-node overhead for small data. More importantly, every insertion and deletion must update **four** pointer connections instead of two (the new node's `prev` and `next`, plus the neighboring nodes' pointers). Getting these updates wrong — especially at the boundaries (head, tail, or empty list) — is the primary source of bugs. A common technique to simplify boundary handling is to use **sentinel nodes**: dummy head and tail nodes that are always present. With sentinels, you never insert or delete at a null boundary; every real node always has a valid `prev` and `next`, eliminating special cases.

A **circular doubly linked list** connects the last node's `next` to the first node and the first node's `prev` to the last, forming a ring. With a single sentinel node, the "head" and "tail" are just `sentinel.next` and `sentinel.prev`. This elegant structure means the empty list is simply the sentinel pointing to itself in both directions. Circular doubly linked lists are used internally by operating systems for process scheduling queues and by many standard library implementations (Python's `collections.deque`, Linux kernel's `list_head`). The key insight is that doubly linked lists trade memory for flexibility: when your algorithm needs fast bidirectional traversal or arbitrary-position deletion, the extra pointer per node is well worth it.
