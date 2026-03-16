---
id: linked-list-singly-doubly-circular
title: 'Linked Lists: Singly, Doubly, and Circular Variants'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: linked-lists
  type: soft
builds-toward:
- linked-list-advanced-operations-cycle-detection
tags:
- linked-list
- data-structure
- variants
stage: formal-systems
status: draft
---

# Linked Lists: Singly, Doubly, and Circular Variants

## Core Idea
Singly linked lists use forward pointers (O(n) reverse); doubly linked lists add backward pointers (O(1) reverse, higher memory). Circular variants loop the tail back to the head, useful for round-robin scheduling.

## Explainer

You already know a linked list as a chain of nodes where each node holds data and a pointer to the next node. That basic picture is a **singly linked list**: traversal flows in one direction, from head to tail, because each node only knows its successor. If you need to find the node before a given node — say, to delete it — you must walk the entire list from the head, costing O(n). Insertion at the head is O(1), and appending at the tail is O(1) if you maintain a tail pointer, but any operation requiring backward movement is expensive.

A **doubly linked list** solves this by giving each node two pointers: one to the next node and one to the previous node. This doubles the pointer overhead per node, but it buys you O(1) deletion of any node when you already have a reference to it, because you can directly access both neighbors. Think of it like a hallway where every room has doors on both sides versus only on the right — you can now walk in either direction without retracing your steps. Doubly linked lists are the standard choice when you need efficient insertion and deletion at arbitrary positions, which is why they underpin structures like LRU caches and text editor buffers.

**Circular linked lists** modify the termination condition: instead of the last node pointing to null, it points back to the head. This creates a loop. A circular singly linked list has one-directional flow in a ring; a circular doubly linked list forms a bidirectional ring. The practical advantage is that you never hit a dead end — traversal wraps around naturally. This makes circular lists ideal for problems with cyclic structure: round-robin scheduling (each process gets a turn, then the cycle repeats), circular buffers, and multiplayer game turn orders. The implementation difference is small — you replace null checks with head-equality checks — but the conceptual shift matters: there is no "last" node, only a current position in a cycle.

When choosing among variants, the decision comes down to your access pattern. If you only traverse forward and insertions happen at the ends, a singly linked list minimizes overhead. If you need bidirectional traversal or efficient arbitrary deletion, pay the extra pointer cost for a doubly linked list. If the problem has inherent cyclical structure, use a circular variant. Each is the same fundamental idea — nodes connected by pointers — with different trade-offs in memory and operation cost.
