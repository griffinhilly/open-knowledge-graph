---
id: list-abstract-data-type-interface
title: 'List Abstract Data Type: Interface and Semantics'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: array-representation-operations-efficiency
  type: hard
builds-toward:
- linked-lists
- stack-adt-using-arrays-linked-lists
- queue-adt-circular-implementation
tags:
- adt
- interface
- semantics
stage: formal-systems
status: draft
---

# List Abstract Data Type: Interface and Semantics

## Core Idea
An Abstract Data Type (ADT) specifies what operations are supported and their expected behavior, but not how they are implemented. A List ADT defines access, insertion, deletion, and traversal without prescribing array or linked-list implementation.

## How It's Best Learned
Define a List interface with operations (get, insert, remove, size), then implement it twice—once with arrays and once with linked lists—and compare performance on a suite of use cases.

## Common Misconceptions
- Confusing the ADT interface with a particular implementation.
- Assuming one implementation is universally better; the choice depends on usage patterns.
- Not considering that the same ADT operations have different complexities across implementations.
