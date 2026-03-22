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

## Questions

```yaml
- question: "You are implementing an LRU (Least Recently Used) cache. When an item is accessed, it must be moved to the front of the list instantly. Arbitrary nodes must be removable in O(1). Which list type is the right choice?"
  type: multiple-choice
  options:
    - "Doubly linked list — O(1) deletion with a direct reference (can access both neighbors) plus O(1) head insertion"
    - "Singly linked list — simpler implementation means less overhead per operation"
    - "Circular singly linked list — wrapping avoids null pointer checks at the tail"
    - "Array — random access by index makes deletion faster than any linked list"
  answer: 0
  explanation: "Deleting an arbitrary node in O(1) requires access to its predecessor. A doubly linked list provides this directly (node.prev), so deletion is O(1) given a reference to the node. A singly linked list has no backward pointer, so finding the predecessor takes O(n). Arrays offer O(1) access but O(n) deletion due to shifting. Circularity is irrelevant to this access pattern."

- question: "What is the primary cost of choosing a doubly linked list over a singly linked list?"
  type: multiple-choice
  options:
    - "Each node stores two pointers instead of one, increasing memory usage per node"
    - "Insertion at the head becomes O(n) instead of O(1)"
    - "Traversal from head to tail requires visiting each node twice"
    - "Circular variants cannot be built from doubly linked lists"
  answer: 0
  explanation: "The only structural difference between singly and doubly linked lists is the addition of a prev pointer per node. This doubles the pointer overhead (e.g., two 8-byte pointers vs. one). All other operations — head insertion, tail insertion with a tail pointer, forward traversal — remain O(1) or O(n). The trade-off is memory cost in exchange for O(1) backward traversal and arbitrary deletion."

- question: "In a doubly linked list, deleting a node for which you already hold a direct reference is an O(1) operation."
  type: true-false
  answer: true
  explanation: "With a direct reference to the node, you can access node.prev and node.next in O(1). Relinking the neighbors (node.prev.next = node.next; node.next.prev = node.prev) takes constant time regardless of the list's length. This is the primary advantage over singly linked lists, where finding the predecessor requires O(n) traversal from the head."

- question: "A circular linked list is simply a doubly linked list where the last node points back to the first."
  type: true-false
  answer: false
  explanation: "Circularity and bidirectionality are independent properties. A circular list has its tail node point back to the head instead of null — this can apply to a singly linked list (one pointer per node, forming a one-directional ring) or a doubly linked list (two pointers, forming a bidirectional ring). You can have circular-singly, circular-doubly, or non-circular versions of either."

- question: "Describe a real use case where a circular linked list is the natural fit, and explain which specific property of circular lists makes it appropriate."
  type: short-answer
  answer: "Round-robin scheduling: each process gets a CPU time slice, then the scheduler moves to the next process in order — and after the last process, it wraps back to the first. A circular list models this perfectly because there is no 'end' of the queue; the tail naturally connects back to the head. The key property is the absence of a null terminator, so traversal never has to check for end-of-list and reset to the head manually."
  explanation: "Other examples include circular buffers (a fixed-size buffer where write/read pointers wrap around), multiplayer board games (turn order cycles), and media playlists on repeat. In all cases, the cyclic structure of the problem maps directly onto the circular list's topology. Using a non-circular list would require manual 'if tail, go back to head' logic; the circular structure makes this automatic."
```

## Explainer

You already know a linked list as a chain of nodes where each node holds data and a pointer to the next node. That basic picture is a **singly linked list**: traversal flows in one direction, from head to tail, because each node only knows its successor. If you need to find the node before a given node — say, to delete it — you must walk the entire list from the head, costing O(n). Insertion at the head is O(1), and appending at the tail is O(1) if you maintain a tail pointer, but any operation requiring backward movement is expensive.

A **doubly linked list** solves this by giving each node two pointers: one to the next node and one to the previous node. This doubles the pointer overhead per node, but it buys you O(1) deletion of any node when you already have a reference to it, because you can directly access both neighbors. Think of it like a hallway where every room has doors on both sides versus only on the right — you can now walk in either direction without retracing your steps. Doubly linked lists are the standard choice when you need efficient insertion and deletion at arbitrary positions, which is why they underpin structures like LRU caches and text editor buffers.

**Circular linked lists** modify the termination condition: instead of the last node pointing to null, it points back to the head. This creates a loop. A circular singly linked list has one-directional flow in a ring; a circular doubly linked list forms a bidirectional ring. The practical advantage is that you never hit a dead end — traversal wraps around naturally. This makes circular lists ideal for problems with cyclic structure: round-robin scheduling (each process gets a turn, then the cycle repeats), circular buffers, and multiplayer game turn orders. The implementation difference is small — you replace null checks with head-equality checks — but the conceptual shift matters: there is no "last" node, only a current position in a cycle.

When choosing among variants, the decision comes down to your access pattern. If you only traverse forward and insertions happen at the ends, a singly linked list minimizes overhead. If you need bidirectional traversal or efficient arbitrary deletion, pay the extra pointer cost for a doubly linked list. If the problem has inherent cyclical structure, use a circular variant. Each is the same fundamental idea — nodes connected by pointers — with different trade-offs in memory and operation cost.
