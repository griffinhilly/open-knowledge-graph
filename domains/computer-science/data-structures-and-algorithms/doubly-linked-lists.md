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
