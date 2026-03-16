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

## Explainer

A **stack** is one of the simplest and most useful abstract data types: it stores elements in a last-in, first-out (LIFO) order, supporting just two primary operations — **push** (add to the top) and **pop** (remove from the top). Think of a stack of plates in a cafeteria: you always add and remove from the top, so the most recently placed plate is the first one taken. This simple constraint turns out to be exactly what you need for tracking function calls (the call stack), undoing operations (undo history), parsing matched parentheses, and evaluating expressions.

Since you already understand arrays and linked lists, you can see that a stack is not a new storage mechanism — it is a *behavioral contract* imposed on top of a concrete data structure. The **array-based implementation** uses an integer variable `top` that tracks the index of the topmost element. Push increments `top` and writes the value; pop reads the value at `top` and decrements it. Both are O(1). The tradeoff is that an array has a fixed capacity — when it fills up, you must allocate a larger array and copy everything over. This resize is O(n) for that single operation, but because you typically double the array size, the cost amortizes to O(1) per push over a sequence of operations. Array-based stacks also benefit from **cache locality**: elements sit in contiguous memory, so the CPU cache can prefetch nearby data efficiently.

The **linked-list implementation** uses the head of the list as the top of the stack. Push creates a new node, sets its `next` pointer to the current head, and updates the head pointer. Pop saves the head's value, moves the head to `head.next`, and returns the saved value. Both operations are O(1) with no amortization needed — there is never a resize because each node is independently allocated. The tradeoff is that every element carries the overhead of a pointer (8 bytes on a 64-bit system), and nodes are scattered across memory, reducing cache performance compared to an array.

Choosing between the two comes down to your workload. If you know a reasonable upper bound on the stack size, or if you want the best raw performance from cache-friendly memory access, the array-based stack is usually preferable. If the stack size is highly unpredictable and you want to avoid any risk of expensive resize operations, the linked-list version offers more consistent per-operation cost. In practice, most standard library stack implementations (like Java's `ArrayDeque` or Python's `list` used as a stack) are array-based because the amortized O(1) guarantee and cache benefits outweigh the occasional resize cost.
