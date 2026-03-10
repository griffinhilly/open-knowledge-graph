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
status: draft
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
