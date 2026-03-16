---
id: linked-lists
title: Linked Lists
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: primitive-data-types
  type: hard
- id: intro-to-classes
  type: soft
builds-toward:
- stacks-data-structure
- queues-data-structure
- binary-trees
tags:
- linked-list
- nodes
- pointers
- data-structures
stage: formal-systems
status: validated
---

# Linked Lists

## Core Idea
A linked list is a linear data structure where each element (node) stores a value and a reference (pointer) to the next node. Unlike arrays, linked lists do not require contiguous memory; elements are connected via pointers. Singly linked lists allow traversal in one direction; doubly linked lists add a previous pointer enabling bidirectional traversal. Insertions and deletions at known positions run in O(1) time, but random access requires O(n) traversal.

## How It's Best Learned
Implement a Node class with value and next fields, then build operations (insert, delete, traverse) from scratch. Drawing box-and-arrow diagrams for each operation makes pointer manipulation concrete before coding.

## Common Misconceptions
- Linked lists are not always faster than arrays; the O(1) insertion advantage only applies when you already hold a reference to the position.
- Forgetting to update the tail pointer during append operations is a common bug.
- Doubly linked lists use more memory per node due to the extra pointer.

## Questions

```yaml
- question: "You hold a reference to a node in the middle of a singly linked list. What is the time complexity to insert a new node immediately after it?"
  type: multiple-choice
  options: ["O(1)", "O(log n)", "O(n)", "O(n²)"]
  answer: 0
  explanation: "When you already have a reference to the target node, insertion requires only updating two pointers (new node's next = target's next; target's next = new node). No traversal is needed. The O(n) cost only applies when you must first search for the insertion position."

- question: "Linked lists are always faster than arrays for insertion because linked list insertions run in O(1)."
  type: true-false
  answer: false
  explanation: "O(1) insertion only applies when you already hold a reference to the insertion position. Finding that position requires O(n) traversal. Arrays also have O(n) insertion in the average case (due to shifting), but with better cache performance. Neither structure is universally faster."

- question: "What is the key structural difference between a singly and doubly linked list, and what does each trade off?"
  type: short-answer
  answer: "A singly linked list stores only a next pointer per node, allowing forward traversal only. A doubly linked list adds a prev pointer, enabling bidirectional traversal and O(1) deletion given a node reference, at the cost of extra memory per node."
  explanation: "The extra prev pointer in a doubly linked list enables operations like deleting a node without needing its predecessor (you can follow prev instead of traversing from the head). This is why most standard library deques and LRU caches use doubly linked lists."
```

## Explainer

Arrays store elements in contiguous memory, so accessing element i is a single calculation (base address + i × element size) — O(1) random access. The cost is that inserting or deleting in the middle requires shifting all subsequent elements. Linked lists take the opposite trade: elements live anywhere in memory, connected by pointers. This makes insertion and deletion cheap at known positions but makes random access expensive — you must follow the chain one node at a time.

Each node in a singly linked list contains two things: a **value** and a **next pointer** referencing the following node. The last node's next pointer is null, marking the end of the list. A **head pointer** is the entry point to the whole structure. To traverse the list, you start at head and follow next pointers until you reach null. To insert after a given node `p`: set `newNode.next = p.next`, then `p.next = newNode` — two pointer updates, O(1). Order matters: if you set `p.next = newNode` first, you lose the reference to the rest of the list.

The O(1) insertion claim requires an important qualification: it assumes you already *have* a reference to the node you are inserting after. If you need to find that node first — say, "insert after the node with value 42" — you pay O(n) for the traversal. This is why the "linked lists beat arrays for insertion" argument is only true in specific contexts (like building a queue where you always append to the tail, which you can maintain as a constant-time pointer).

Doubly linked lists add a **prev pointer** to each node. This costs memory (two pointers instead of one per node) but pays off in flexibility: you can traverse backward, and you can delete a node in O(1) given only a reference to it (because you can reach its predecessor via `node.prev`). In a singly linked list, deleting a node requires its predecessor's reference, forcing a traversal from the head. Data structures like browser history, LRU caches, and the standard library's `deque` use doubly linked lists for this reason.

Linked lists are the conceptual foundation for the stack, queue, and tree structures you will encounter next. Once you can reliably manipulate pointers — insert, delete, reverse — those more complex structures become much easier to reason about, because they are all variations on the same node-and-pointer model.

