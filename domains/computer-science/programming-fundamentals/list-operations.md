---
id: list-operations
title: List Operations and Methods
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arrays-and-lists
  type: hard
- id: string-operations
  type: soft
builds-toward:
- list-comprehensions
- algorithm-design-basics
tags:
- lists
- append
- remove
- sort
- slicing
- searching
stage: abstract-reasoning
status: validated
---

# List Operations and Methods

## Core Idea
Lists expose methods for in-place modification: append() adds to the end, insert() adds at a position, remove() deletes by value, and pop() removes by index. Sorting (sort() for in-place, sorted() for a new list) reorders elements. Slicing copies a portion of a list. Membership testing with in searches linearly. Understanding whether an operation modifies the list in place or returns a new one is critical for avoiding subtle bugs.

## How It's Best Learned
Write programs that build sorted frequency tables: read words, append to a list, sort, and count duplicates. Experiment with sort vs. sorted, and pop vs. remove, to feel their differences.

## Common Misconceptions
- Calling sort() and ignoring that it returns None (not the sorted list).
- Confusing remove(value) with pop(index).
- Assuming sort() and sorted() use the same interface — sort() is an in-place method; sorted() is a built-in function that returns a new list.
