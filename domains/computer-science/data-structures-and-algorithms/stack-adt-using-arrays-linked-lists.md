---
id: stack-adt-using-arrays-linked-lists
title: 'Stack ADT: Array and Linked-List Implementations'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: linked-lists
  type: hard
builds-toward:
- stack-infix-postfix-expression-evaluation
tags:
- stack
- adt
- data-structure
stage: formal-systems
status: draft
---

# Stack ADT: Array and Linked-List Implementations

## Core Idea
A stack is a LIFO (Last-In-First-Out) data structure supporting push (insert) and pop (remove) operations. It can be implemented with an array (using an index pointer) or a linked list (using a head pointer), each with different space/time tradeoffs.

## How It's Best Learned
Implement a stack in your language of choice. Push and pop elements, and trace the state after each operation. Compare array vs. linked-list implementations: array is cache-friendly but risks overflow; linked list is flexible but uses extra pointers.

## Common Misconceptions
- A stack must be empty initially (false—it starts empty by definition).
- Stack overflow is only a memory issue (it's also a logic error—trying to pop from empty).
- Array-based stacks are always slower because of reallocation (amortized analysis shows they're O(1)).
