---
id: arrays-and-lists
title: Arrays and Lists
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
- id: for-loops
  type: hard
- id: primitive-data-types
  type: soft
builds-toward:
- list-operations
- nested-loops
- list-comprehensions
tags:
- arrays
- lists
- sequences
- indexing
- mutable collections
stage: abstract-reasoning
status: validated
---

# Arrays and Lists

## Core Idea
A list (or array) is an ordered, indexed collection of values that can be traversed, modified, and grown or shrunk. Elements are accessed by zero-based index; negative indices count from the end. Unlike strings, lists are mutable — elements can be added, removed, or changed in place. Lists are the foundational data structure for representing sequences of related items and are traversed naturally with for loops.

## How It's Best Learned
Build, modify, and traverse lists by hand and in code. Implement accumulation patterns: start with an empty list, append items inside a loop, then process the result. Compare list access patterns to string slicing.

## Common Misconceptions
- Forgetting that list assignment (b = a) does not copy the list — both names point to the same object.
- Modifying a list while iterating over it.
- Assuming lists must hold a single type in dynamically typed languages.
