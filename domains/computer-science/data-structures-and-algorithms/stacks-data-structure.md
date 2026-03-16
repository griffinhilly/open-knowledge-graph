---
id: stacks-data-structure
title: Stacks
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: linked-lists
  type: soft
builds-toward:
- depth-first-search
- topological-sort
tags:
- stack
- LIFO
- data-structures
- push-pop
stage: formal-systems
status: validated
---

# Stacks

## Core Idea
A stack is a last-in, first-out (LIFO) data structure that supports two core operations: push (add to top) and pop (remove from top), both in O(1) time. Stacks naturally model function call frames, undo/redo history, and expression parsing. They can be implemented using a dynamic array (with a top pointer) or a linked list (with insertions at the head). A peek operation returns the top element without removing it.

## How It's Best Learned
Implement a stack from both an array and a linked list. Then solve classic stack problems: balanced parentheses checking, postfix expression evaluation, and the next-greater-element problem.

## Common Misconceptions
- Stack overflow (too many recursive calls) is a real-world manifestation of a call stack running out of space.
- Stacks are not limited to numeric data; they hold any type of element.
- Checking whether the stack is empty before popping is essential to avoid underflow errors.

## Explainer

You already know arrays and linked lists as linear collections where you can access or insert elements at various positions. A **stack** restricts this flexibility on purpose: you can only add and remove elements from one end, called the **top**. This last-in, first-out (LIFO) constraint is not a limitation — it is the entire point. By restricting access, a stack gives you a data structure that naturally tracks "what was I doing most recently?" and provides O(1) push, pop, and peek operations with zero bookkeeping overhead.

The simplest way to implement a stack is with a **dynamic array and a top index**. You maintain a variable `top` that tracks the index of the most recent element. Push increments `top` and writes the new element; pop reads the element at `top` and decrements it. If you reach the array's capacity, you resize (typically doubling), which gives amortized O(1) push. Alternatively, you can implement a stack using a **linked list** where each push prepends a new node at the head and each pop removes the head node. The linked-list version never needs resizing but uses extra memory for pointers and has worse cache locality. In practice, the array-based approach is faster for most use cases.

The power of stacks becomes clear when you see them in action. Consider **balanced parentheses checking**: scan a string left to right, push every opening bracket onto the stack, and when you encounter a closing bracket, pop and verify it matches. If the stack is empty when you try to pop, or non-empty when the string ends, the brackets are unbalanced. The stack naturally handles nesting of any depth because the most recently opened bracket is always on top — exactly the one that the next closing bracket should match. Another classic application is **postfix (reverse Polish) expression evaluation**: given an expression like `3 4 + 2 *`, push operands onto the stack; when you encounter an operator, pop two operands, apply the operator, and push the result. The stack manages operator precedence implicitly without needing parentheses.

The most pervasive stack in computing is one you use every time you call a function: the **call stack**. Each function call pushes a new frame containing local variables and the return address. When the function returns, its frame is popped, restoring the caller's state. This is why recursion works — each recursive call gets its own frame on the stack, and they unwind in reverse order. It is also why deep recursion can cause a **stack overflow**: the call stack has a fixed size (typically 1-8 MB), and exceeding it crashes the program. Understanding stacks gives you direct insight into how recursion, undo/redo systems, browser back-buttons, and depth-first search all work — each is fundamentally tracking a history of decisions that must be reversed in LIFO order.
