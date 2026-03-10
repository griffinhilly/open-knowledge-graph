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
status: draft
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
