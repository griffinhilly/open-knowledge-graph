---
id: singly-linked-lists
title: Singly Linked Lists
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward:
- doubly-linked-lists
- stacks-data-structure
- queues-data-structure
tags:
- linked-lists
- pointers
- nodes
- sequential
- insertion
- deletion
stage: formal-systems
status: draft
---

# Singly Linked Lists

## Core Idea
A singly linked list is a sequence of nodes where each node holds a value and a single pointer to the next node, forming a unidirectional chain. Unlike arrays, linked lists enable O(1) insertion and deletion at any location if you possess a pointer to that location, but random access is O(n). This makes them ideal for applications with frequent insertions/deletions and unknown size.

## How It's Best Learned
Draw nodes and pointers visually; trace insertion and deletion step-by-step, carefully managing pointer updates. Implement core operations (insert, delete, search, reverse) from scratch, paying close attention to edge cases like inserting at the head or into an empty list.

## Common Misconceptions
- Singly linked lists are always faster than arrays (they're not; arrays excel at random access and cache locality). - You can insert anywhere in O(1) without a pointer (false; you must have a pointer to the location; finding it costs O(n)).
